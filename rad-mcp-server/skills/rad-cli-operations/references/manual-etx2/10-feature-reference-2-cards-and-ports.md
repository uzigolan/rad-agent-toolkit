# Feature Reference – 2 Cards and Ports

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 531–696.*


## 2.1 Cards  *(p.531)*

2 Cards and Ports 
This chapter describes card and port-related features. 
2.1 Cards 
This section describes how to configure the module type (card type) for the modular option. 
The ability to pre-provision the module type before actually inserting the module provides more 
flexibility. 
Applicability and Scaling 
This feature is applicable to the ETX­2i modular option. 
Functional Description 
The ETX-2i module can contain ports of type GbE, E1, T1, T3, VDSL2, or SHDSL; or it can contain an 
optional embedded router. You can pre-provision the module type before physically inserting the 
module. The configured module type must match the actual module installed, for correct operation. 
When ETX-2i starts up, it verifies that the configured module type matches the module that is installed. 
If they do not match, the card_mismatch alarm is sent. 
The ETX-2i module is defined as slot 1; therefore, the ports on the module are referenced with slot 1. 
The device ports that are not on the module are referenced with slot 0. 
 
Note 
The ETX-2i module is not hot swappable; it can be removed/replaced only 
when ETX-2i is powered off.  
ETX-2i Devices 
2. Cards and Ports 
Factory Defaults 
By default, the module type is set according to the module type that is actually installed. 
Configuring Modules 
Note 
You can display the module type from the slot level by typing 
show cards-summary.  
 To configure the module: 
1. Navigate to configure slot 1. 
The config>slot(1)# prompt is displayed. 
2. In the config>slot(1)# prompt that is displayed, perform the required tasks according to the 
following table. 
Task 
Command 
Comments 
Configuring the module 
type as one of the 
following: 
Ethernet GbE 
E1/T1 with four 
channels 
E1/T1 with eight 
channels 
T3 with one channel 
T3 with two channels 
SHDSL with 4-wire 
option 
SHDSL with 8-wire 
option 
VDSL2 with 8-wire 
option 
card-type eth 1g-2-full 
card-type tdm {e1-t1-4-ch | e1-t1-8-ch} 
card-type tdm {t3-1-ch | t3-2-ch} 
card-type shdsl {shdsl-4w | shdsl-8w} 
card-type vdsl2 {vdsl2-4p-pots | vdsl2-4p-
isdn}  
Enter no card-type to set 
the module type to null. 
Note: 
• If the configured 
module type does not 
match the actual 
installed module, the 
card_mismatch alarm 
is sent. This includes 
the case of changing 
the module type to 
null while a module is 
installed. 
• When the module 
type is changed to 
null, ETX-2i 
automatically deletes 
all the interfaces that 
exist in the module. 
• You are not allowed to 
change the module 
type in the following 
cases: 

## 2.2 All Ports  *(p.533)*

ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
• An active service is 
defined over one or 
more of the module 
interfaces. 
• One or more of the 
module interfaces are 
bound to a router 
interface. 
• One or more of the 
module interfaces is 
being used as a timing 
reference (e.g., 
domain clock source). 
Administratively 
enabling the module  
no shutdown 
Enter shutdown to 
administratively disable 
the module. 
Resetting module SW 
reset 
Supported for VDSL only  
Displaying module 
status 
show status 
 
Administratively 
enabling the module  
no shutdown 
Enter shutdown to 
administratively disable 
the module. 
Resetting module SW 
reset 
Supported for VDSL only  
Displaying module 
status 
show status 
 
  
 
2.2 All Ports 
This section describes how to reference ports in the tasks that you can perform on all ports of an ETX-2i 
device. These tasks include: 
• 
Setting the sampling interval for port statistics 
• 
Displaying the port summary status  
• 
Saving the port summary output to an XML file in the user directory  
ETX-2i Devices 
2. Cards and Ports 
The following sections describe the tasks per port type (such as Ethernet, E1, SVI, and more).  
Applicability and Scaling 
These tasks are applicable to all ETX-2i devices. 
Functional Description 
Options 
ETX­2i has four, six, or eight fixed SFP/copper combo ports. If ordered with the modular GbE option, it 
has four fixed SFP/copper combo ports, and two fiber optic/copper (combo) Gigabit Ethernet ports on 
the module. If ordered with 64 E1 ports, it has six fixed SFP/copper combo ports. If ordered with a PMC 
option, the last two Ethernet ports (7 and 8) are used as internal ports to interconnect with the 
integrated x86 processor. 
ETX-2i-B has four or six fixed SFP/copper combo ports (two Network ports and two or four User ports, 
depending on the ordering option).  
ETX-2i-10G half 19-inch has either of the following:  
• 
Four ETH SFP+ ports, four UTP ports, and four combo or SFP ports.   
• 
Eight ETH SFP+ (1/10GbE) ports (ETX-2i-10G-B/8SFPP) 
ETX-2i-10G full 19-inch has either of the following: 
• 
Four ETH SFP+ ports, 12 UTP ports, and 12 SFP ports  
• 
Four ETH SFP+ ports and 24 SFP ports 
• 
Eight ETH SFP+ (1/10GbE) ports (ETX-2i-10G-B/8SFPP) 
ETX-2i-100G/4Q full 19-inch has four QSFP28 (100GbE), eight SFP28 (1/10/25GbE), and eight SFP+ 
(1/10GbE) ports. 
ETX-2i-100G/40G full 19-inch has two QSFP28 (100GbE), two QSFP+ (40GbE) ports, and 16 SFP+ 
(1/10GbE) ports. 
ETX-2i-10G-B/8SFPP/ODU has an IP66 outdoor enclosure, with either a single or dual power supply. 
ETX-2i Devices 
2. Cards and Ports 
Port Numbering 
The following table shows how to refer to the ports when configuring them with CLI commands. 
 
Port 
Unit 
CLI 
 
Port Number 
[Slot/]Port Number 
ETX-203AX-ODU-X 
 
 
Net 
1 or 2 
1 or 2 
User 
1 or 2 
1 or 2 
User 
3 
3 
User 
4 
4 
User 
5 
5 
User 
6 
6 
MNG-ETH 
 
101 
 
Port 
Unit 
CLI 
 
Port Number 
[Slot/]Port Number 
ETX-2i 
Fixed Ethernet ports 1-4 (SFP) 
1-4 
0/1, …, 0/4 
Fixed Ethernet ports 5-8 (SFP) (if applicable) 
5-8 
0/5, …, 0/8 
Modular port 1 (if applicable) 
1 
1/1 
Modular port 2 (if applicable) 
2 
1/2 
MNG-ETH 
 
0/101 
ETX­2i-64E1 
E1  
1, …, 64 
0/1, …, 0/64 
Network 
1 
0/1 
Net/User 
2 
0/2 
User 
3, 4, 5, 6 
0/3, 0/4, 0/5, 0/6 
MNG-ETH 
 
0/101 
ETX-2i Devices 
2. Cards and Ports 
Port 
Unit 
CLI 
 
Port Number 
[Slot/]Port Number 
ETX-2i-B 
Fixed Ethernet ports 1-4 (SFP) 
1-4 
0/1, …, 0/4 
Fixed Ethernet ports 5-10 (SFP) (if applicable) 
5-8 
0/5, …, 0/10 
MNG-ETH 
 
0/101 
ETX-2i-10G Half 19-inch 
Fixed Ethernet ports 1-4 (SFP+) 
1-4 
0/1, …, 0/4 
Fixed Ethernet ports 5-8 (SFP) 
5-8 
0/5, …, 0/8 
Fixed Ethernet ports 9 -12 (if applicable) 
9-12 
0/9, …, 0/12 
MNG-ETH 
 
0/101 
ETX-2i-10G Full 19-inch 
Fixed Ethernet ports 1-4 (SFP+) 
1-4 
0/1, …, 0/4 
Fixed Ethernet ports 5-12 (SFP) 
5-12 
0/5, …, 0/12 
Fixed Ethernet ports 13-28 (if applicable) 
13-28 
0/13, …, 0/28 
MNG-ETH 
 
0/101 
ETX-2i-10G-B/8SFPP Half and Full 19-inch, ETX-2i-10G-B/8SFPP/ODU 
Fixed Ethernet ports 1, …8 (SFP+) 
1-8 
0/1, …., 0/8 
MNG-ETH 
101 
0/101 
ETX-2i-100G/4Q 
 
 
Fixed Ethernet ports (QSFP28) 
3/1, …., 3/4 
3/1, …., 3/4 
MNG-ETH 
 
0/101 
Fixed Ethernet ports (SFP28) 
2/1, …, 2/8 
2/1, …, 2/8 
Fixed Ethernet ports (SFP+) 
1/1, …, 1/8 
1/1, …, 1/8 
ETX-2i-100G/40G 
 
 
Fixed Ethernet ports 1-2 (QSFP+) 
3/1, 3/2 
3/1, 3/2 
Fixed Ethernet ports 3-4 (QSFP28) 
3/3, 3/4 
3/3, 3/4 
Fixed Ethernet ports 5-20 (SFP+) 
1/1, …, 1/8; 2/1, …, 
2/8 
1/1, …, 1/8; 2/1, …, 2/8 
ETX-2i Devices 
2. Cards and Ports 
Note 
For ETX-2i or ETX-2i-B with D-NFV/PMC option, user ports 7 and 8 are not 
available. 
Port Reference 
ETX-2i, ETX-2i-B, and ETX-2i-10G ports are referenced as <slot>/<port> or <slot>/<port>/<tributary>: 
• 
<slot> = 1 for modular ports  
• 
<slot> = 0, 1, 2, or 3 for non-modular Ethernet ports 
• 
<tributary> is required only for smart SFP E1/T1/E3/T3/SDH/SONET ports and is always set to 1. 
ETX-2i-100G does not support Smart SFPs. 
EtherType 
EtherType tag configuration of a packet (IEEE 802.1Q) allows identification of incoming and outgoing 
VLAN-tagged packets.  
EtherType (tag protocol ID, or TPID) configured per port (Ethernet, Logical MAC, PCS) is used for: 
• 
Identification of (inner and outer) VLAN-tagged packets at ingress 
• 
Setting the EtherType value used in VLAN editing actions (Mark, Push) at egress 
ETX-2i comes preconfigured with two global EtherType tag values – 8100 (the default) and 88a8. These 
Ethernet tag values cannot be modified or deleted.  
ETX-2i supports the configuration of two additional global tag EtherType values (besides 8100 (the 
default) and 88a8). These tag values can be modified or deleted. 
You can configure the EtherType, used in the Port level and in Egress VLAN editing actions (Mark and 
Push), with one of the preconfigured or user-configured global EtherType tag values. EtherType 
configured per port is used for the identification of VLAN-tagged frames at ingress and VLAN editing at 
egress.  
 
 
ETX-2i Devices 
2. Cards and Ports 
Configuration (per port) of a packet’s inner and outer tag EtherTypes allows ingress identification of a 
packet’s inner and outer VLAN tags, as follows: 
• 
The incoming packet’s outer VLAN tag is identified as a VLAN-tagged frame if its outer tag 
EtherType matches the port’s configured tag EtherType. (Otherwise, the frame is considered 
untagged or dropped.) 
• 
The packet’s inner VLAN tag is identified if its inner tag EtherType is equal to one of the four 
device-level EtherTypes (two default and two user-configured). 
 
Note 
You cannot change an EtherType tag if a port (Ethernet or LAG) has flows 
attached to it. 
The following table describes the admission rules for different port and TPID types. 
Ports with Configured Port TPID Y (Tag EtherType port configuration) 
Outer TPID 
Inner TPID 
Admit/Drop 
Recognized Tag Levels 
Y 
None 
Admit 
1 
Y 
Any one of the four device-level global TPIDs 
Admit 
2 
Y 
None of the four device-level global TPIDs 
Admit 
1 
Z (other than Y) 
Don’t care 
Admit 
Untagged 
None 
– 
Admit 
Untagged 
Configuring EtherType (Global) 
This section describes how you can configure up to two additional global EtherType tags so that they can 
be used in EtherType tag configuration of a packet or port.   
If you do not define additional tag values, the port and packet can only be configured with the default 
global values 88a8 and 8100. 
 To configure the EtherType tag at the device level: 
3. Navigate to config>port. 
4. Enter tag-ether-type <ether-tag>, 
Where ether-tag can be 0x0000-0xFFFF. 
ETX-2i Devices 
2. Cards and Ports 
Note 
You can use no before tag-ether-type <ether-tag> to remove the two 
additional user-configurable EtherType tag values. You cannot remove the 
fixed 8100 and 88a8 values. 
Removing a Port 
You can remove a previously configured port. 
Note 
You cannot remove an Ethernet port.  
 To remove a port: 
• 
At the port prompt config>port#, enter:  
no <port type> <port number> 
For example: no gfp 1, no ppp 1, no lag 3  
Setting Port Statistics Sampling Interval 
You can configure a sampling interval of one to 30 minutes. The default is 15 minutes. 
 To set the sampling interval: 
• 
At the port prompt config>port#, enter:  
rate-sampling-window <1–30> 
The sampling interval is set to the specified number of minutes. 
Viewing Overflow Discarded Frames Statistics 
ETX-2i supports a counter that presents the number of frames discarded from all device ports due to 
capacity overflow. This counter enables diagnosing and monitoring network performance and traffic 
efficiency. 
ETX-2i Devices 
2. Cards and Ports 
Notes 
• 
This counter is per device, and not per port. It indicates an overflow of the 
ingress device capacity. 
• 
When the ingress capacity is exceeded, the device can no longer process 
ingress traffic accurately, and therefore cannot properly maintain this 
counter (i.e., does not count all lost frames). Therefore, this counter serves 
as an indicator, and not for accurate calculations. 
• 
 Port mirroring may cause the product’s overall switching capacity to be 
exceeded. In this case, overflow mirrored frames are dropped, and are 
included in the count of the overall discarded frames.  
You can display the Overflow Discarded Frames counter using the show statistics command from the 
port level and clear this counter at any time using the clear-statistics command, also from the port level.  
Note 
When ETX-2i discards frames from a port, due to overload, a corresponding 
event is issued for that port. Once this event is issued, a five-minute hold 
period commences. During this hold period, additional discarded frames on 
the port are counted but do not trigger a new event. At the end of the hold 
period, any newly discarded frames on that port trigger a new event that 
shows the number of discarded frames counted since the previous event.  
 To display the number of overflow frames of all ETX-2i ports: 
• 
At the port prompt config>port#, enter: 
show statistics 
 To clear the overflow frames counter: 
• 
At the port prompt config>port#, enter: 
clear-statistics 
Viewing Ports Summary 
You can display the logical inventory (summary) of all ETX-2i ports, in either of two formats: 
• 
Table (one row per port) – generated by show summary command; first 16 characters of port 
name are displayed. 
• 
List – generated by show summary-full-name command; all ports are listed in ascending order 
with each port’s information below it; full port name (up to 255 characters) is displayed.  
ETX-2i Devices 
2. Cards and Ports 
You can save the output of the show summary command (i.e., logical inventory) to an XML file in the 
user directory. The XML schema of the output file is stored in the read-only port-summary.xsd file in the 
RADOS file system xml-schema directory.  
 To display the status of all ETX-2i ports (in tabular format): 
• 
At the port prompt config>port#, enter: 
show summary 
The statuses and speeds of the ETX-2i ports are displayed. If a port is being tested via the 
loopback command, it is indicated in the operational status.   
 To display the status of all ETX-2i ports with full port names: 
• 
At the port prompt config>port#, enter: 
show summary-full-name 
Note 
The port operational status indicates if the port is down to fault propagation.  
 To save the device’s logical inventory to an XML file: 
1. Enter configure port xml-export summary <filename>. 
filename is the unique 1–32-character string name of the XML file to be saved in the user 
directory; it cannot contain a path (i.e., slashes and backslashes).  
2. If filename exists, the following message appears:  
/user/<filename> exists. Overwrite it? [Yes/No] 
Enter Yes to overwrite the existing file. 
Enter No to cancel the command. In this case, the CLI prompt returns (without further 
messages). 
3. If the file is successfully written, the following message appears: 
The output was written to /user/<filename>. 
Examples 
Global EtherType 
 To configure a port with global Ethertype tag 0x88a8: 
ETX-2i>config>port>tag-ether-type 0x88a8 
ETX-2i Devices 
2. Cards and Ports 
 To configure a port with global EtherType tag 0x88a4: 
ETX-2i>config>port>tag-ether-type 0x88a4 
Overflow Discarded Frames Statistics 
 To display the number of discarded frames on all flows: 
ETX-2i# configure port  
ETX-2i>config>port# show statistics 
Overflow Discarded Frames  :  331466 
Port Summary 
 To display the status of all ETX-2i ports: 
ETX-2i# configure port  
ETX-2i>config>port# show summary 
 
Port           Number         Name            Admin    Oper      Speed 
----------------------------------------------------------------------------- 
Ethernet       0/1            ETH 1           Up       Up        1000000000 
Ethernet       0/2            ETH 2           Up       Up        1000000000 
Ethernet       0/3            ETH 3           Up       Up        1000000000 
Ethernet       0/4            ETH 4           Up       Down      1000000000 
Ethernet       0/5            ETH 5           Up       Down      1000000000 
Ethernet       0/6            ETH 6           Up       Down      1000000000 
Ethernet       0/7            ETH-0/7         Up       Down      1000000000 
Ethernet       0/8            ETH-0/8         Up       Down      1000000000 
Ethernet       0/101          MNG-ETH         Up       Down      100000000 
Lag            1              LAG 1           Up       Up        1000000000 
SVI            1              SVI 1           Up       Up        0 
 To display the status of all ETX-2i-64E1 ports: 
ETX-2i-64E1# configure port  
ETX-2i-64E1>config>port# show summary 
Port           Number         Name            Admin    Oper      Speed 
----------------------------------------------------------------------------- 
Ethernet       0/1            ETH-0/1         Up       Up        1000000000 
Ethernet       0/2            ETH-0/2         Up       Up        1000000000 
Ethernet       0/3            ETH-0/3         Up       Up        1000000000 
Ethernet       0/4            ETH-0/4         Up       Up        1000000000 
Ethernet       0/5            ETH-0/5         Up       Down      1000000000 
Ethernet       0/6            ETH-0/6         Up       Up        1000000000 
Ethernet       0/101          MNG-ETH         Up       Up        100000000 
E1             0/1            DS1 0/1         Up       Up        2048000 
E1             0/2            DS1 0/2         Up       Up        2048000 
ETX-2i Devices 
2. Cards and Ports 
E1             0/3            DS1 0/3         Up       Up        2048000 
E1             0/4            DS1 0/4         Up       Up        2048000 
E1             0/5            DS1 0/5         Up       Up        2048000 
E1             0/6            DS1 0/6         Up       Up        2048000 
E1             0/7            DS1 0/7         Up       Up        2048000 
E1             0/8            DS1 0/8         Up       Up        2048000 
E1             0/9            DS1 0/9         Up       Up        2048000 
E1             0/10           DS1 0/10        Up       Down      2048000 
E1             0/11           DS1 0/11        Up       Down      2048000 
E1             0/12           DS1 0/12        Up       Down      2048000 
E1             0/13           DS1 0/13        Up       Down      2048000 
E1             0/14           DS1 0/14        Up       Down      2048000 
E1             0/15           DS1 0/15        Up       Down      2048000 
E1             0/16           DS1 0/16        Up       Down      2048000 
E1             0/17           DS1 0/17        Up       Down      2048000 
E1             0/18           DS1 0/18        Up       Down      2048000 
E1             0/19           DS1 0/19        Up       Down      2048000 
E1             0/20           DS1 0/20        Up       Down      2048000 
E1             0/21           DS1 0/21        Up       Down      2048000 
E1             0/22           DS1 0/22        Up       Down      2048000 
E1             0/23           DS1 0/23        Up       Down      2048000 
E1             0/24           DS1 0/24        Up       Down      2048000 
E1             0/25           DS1 0/25        Up       Down      2048000 
E1             0/26           DS1 0/26        Up       Down      2048000 
E1             0/27           DS1 0/27        Up       Down      2048000 
E1             0/28           DS1 0/28        Up       Down      2048000 
E1             0/29           DS1 0/29        Up       Down      2048000 
E1             0/30           DS1 0/30        Up       Down      2048000 
E1             0/31           DS1 0/31        Up       Down      2048000 
E1             0/32           DS1 0/32        Up       Down      2048000 
E1             0/33           DS1 0/33        Up       Down      2048000 
E1             0/34           DS1 0/34        Up       Down      2048000 
E1             0/35           DS1 0/35        Up       Down      2048000 
E1             0/36           DS1 0/36        Up       Down      2048000 
E1             0/37           DS1 0/37        Up       Down      2048000 
E1             0/38           DS1 0/38        Up       Down      2048000 
E1             0/39           DS1 0/39        Up       Down      2048000 
E1             0/40           DS1 0/40        Up       Down      2048000 
E1             0/41           DS1 0/41        Up       Down      2048000 
E1             0/42           DS1 0/42        Up       Down      2048000 
E1             0/43           DS1 0/43        Up       Down      2048000 
E1             0/44           DS1 0/44        Up       Down      2048000 
E1             0/45           DS1 0/45        Up       Down      2048000 
E1             0/46           DS1 0/46        Up       Down      2048000 
E1             0/47           DS1 0/47        Up       Down      2048000 
E1             0/48           DS1 0/48        Up       Down      2048000 
E1             0/49           DS1 0/49        Up       Down      2048000 
E1             0/50           DS1 0/50        Up       Down      2048000 
E1             0/51           DS1 0/51        Up       Down      2048000 
E1             0/52           DS1 0/52        Up       Down      2048000 
E1             0/53           DS1 0/53        Up       Down      2048000 
E1             0/54           DS1 0/54        Up       Down      2048000 
ETX-2i Devices 
2. Cards and Ports 
E1             0/55           DS1 0/55        Up       Down      2048000 
E1             0/56           DS1 0/56        Up       Up        2048000 
E1             0/57           DS1 0/57        Up       Up        2048000 
E1             0/58           DS1 0/58        Up       Up        2048000 
E1             0/59           DS1 0/59        Up       Up        2048000 
E1             0/60           DS1 0/60        Up       Up        2048000 
E1             0/61           DS1 0/61        Up       Up        2048000 
E1             0/62           DS1 0/62        Up       Up        2048000 
E1             0/63           DS1 0/63        Up       Up        2048000 
E1             0/64           DS1 0/64        Up       Up        2048000 
SVI            1              SVI 1           Up       Up        0 
SVI            2              SVI 2           Up       Up        0 
SVI            96             SVI 96          Up       Up        0 
 To display the status of all ETX-2i-B ports: 
ETX-2i-B# configure port  
ETX-2i-B>config>port# show summary 
Port           Number         Name            Admin    Oper      Speed 
----------------------------------------------------------------------------- 
Ethernet       0/1            ETH-0/1         Up       Down      1000000000 
Ethernet       0/2            ETH-0/2         Up       Up        1000000000 
Ethernet       0/3            ETH-0/3         Up       Down      1000000000 
Ethernet       0/4            ETH-0/4         Up       Up        1000000000 
Ethernet       0/101          MNG-ETH         Up       Up        100000000 
SVI            1              SVI 1           Up       Up        0 
SVI            96             SVI 96          Up       Up        0 
 To display the status of all ETX-2i-B ports with full name: 
ETX-2i-B# configure port  
ETX-2i-B>config>port# show summary-full-name 
Port : Ethernet       Number  : 0/1 
 
Name : ETH-0/1                                                                   
 
Admin : Up 
Oper  : Down 
Speed : 1Gbps 
 
 
Port : Ethernet       Number  : 0/2 
 
Name : ETH-0/2                                                                 
 
Admin : Up 
Oper  : Up 
Speed : 1Gbps 
 
 
Port : Ethernet       Number  : 0/3 
ETX-2i Devices 
2. Cards and Ports 
Name : ETH-0/3                               
 
Admin : Up 
Oper  : Down 
Speed : 1Gbps 
 
 
Port : Ethernet       Number  : 0/4 
 
Name : ETH-0/4     
Admin : Up 
Oper  : Up 
Speed : 1Gbps 
 
 
Port : Ethernet       Number  : 0/101 
 
Name : MNG-ETH                                                                            
 
Admin : Up 
Oper  : Up 
Speed : 100Mbps 
 
 
Port : SVI            Number  : 1 
 
Name : SVI 1                                                                         
 
Admin : Up 
Oper  : Up 
Speed : 0 
 
 
Port : SVI            Number  : 96 
 
Name : SVI 96                                                                       
 
Admin : Up 
Oper  : Up 
Speed : 0 
 To display the status of all ETX-2i-100G ports: 
ETX-2i-100G>config>port# show summary 
Port           Number         Name            Admin    Oper      Speed 
----------------------------------------------------------------------------- 
Ethernet       0/1            ETH-0/1         Up       Up        100000000000 
Ethernet       0/2            ETH-0/2         Up       Up        100000000000 
Ethernet       0/3            ETH-0/3         Up       Down      100000000000 
Ethernet       0/4            ETH-0/4         Up       Down      10000000000 
Ethernet       0/5            ETH-0/5         Up       Down      10000000000 
ETX-2i Devices 
2. Cards and Ports 
Ethernet       0/6            ETH-0/6         Up       Down      10000000000 
Ethernet       0/7            ETH-0/7         Up       Down      10000000000 
Ethernet       0/8            ETH-0/8         Up       Down      10000000000 
Ethernet       0/9            ETH-0/9         Up       Down      10000000000 
Ethernet       0/10           ETH-0/10        Up       Down      10000000000 
Ethernet       0/11           ETH-0/11        Up       Down      10000000000 
Ethernet       0/12           ETH-0/12        Up       Down      10000000000 
Ethernet       0/13           ETH-0/13        Up       Down      10000000000 
Ethernet       0/101          MNG-ETH         Up       Up        100000000 
SVI            96             SVI 96          Up       Up        0 
 To display the status of all ETX-2i-100G ports with full name: 
ETX-2i-100G>config>port# show summary-full-name 
 
Port : Ethernet       Number  : 0/1 
 
Name : ETH-0/1 
 
Admin : Up 
Oper  : Up 
Speed : 100Gbps 
 
 
Port : Ethernet       Number  : 0/2 
 
Name : ETH-0/2 
 
Admin : Up 
Oper  : Up 
Speed : 100Gbps 
 
 
Port : Ethernet       Number  : 0/3 
 
Name : ETH-0/3 
 
Admin : Up 
Oper  : Down 
Speed : 100Gbps 
 
 
Port : Ethernet       Number  : 0/4 
 
Name : ETH-0/4 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
 
Port : Ethernet       Number  : 0/5 
ETX-2i Devices 
2. Cards and Ports 
Name : ETH-0/5 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
 
Port : Ethernet       Number  : 0/6 
 
Name : ETH-0/6 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
 
Port : Ethernet       Number  : 0/7 
 
Name : ETH-0/7 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
 
Port : Ethernet       Number  : 0/8 
 
Name : ETH-0/8 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
 
Port : Ethernet       Number  : 0/9 
 
Name : ETH-0/9 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
 
Port : Ethernet       Number  : 0/10 
 
Name : ETH-0/10 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
ETX-2i Devices 
2. Cards and Ports 
Port : Ethernet       Number  : 0/11 
 
Name : ETH-0/11 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
 
Port : Ethernet       Number  : 0/12 
 
Name : ETH-0/12 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
 
Port : Ethernet       Number  : 0/13 
 
Name : ETH-0/13 
 
Admin : Up 
Oper  : Down 
Speed : 10Gbps 
 
 
Port : Ethernet       Number  : 0/101 
 
Name : MNG-ETH 
 
Admin : Up 
Oper  : Up 
Speed : 100Mbps 
 
 
Port : SVI            Number  : 96 
 
Name : SVI 96 
 
Admin : Up 
Oper  : Up 
Speed : 0 
 
 

## 2.3 DS1 (E1/T1) Ports  *(p.549)*

ETX-2i Devices 
2. Cards and Ports 
Configuration Errors 
The following table lists messages generated by ETX-2i when a configuration error is detected. 
Message 
Description 
Filename may not contain / or \ 
You attempted to save the show summary command to an XML file 
containing a path.  
Insufficient storage space 
The XML file containing the show summary output is too large to save in 
the user directory.  
Modify failed: EtherType tag 
value is in use 
The EtherType tag value cannot be changed because it is currently used by 
a port of a flow. 
Invalid port EtherType tag value 
The EtherType tag value for a port cannot be configured to the default 
value (0x8100) and cannot be different from the one configured at the 
system level. 
Cannot delete default EtherType 
tag value 
The default EtherType tag value (0x8100) cannot be deleted. 
Delete failed: EtherType tag 
value is in use 
The EtherType tag value cannot be deleted because it is currently being 
used by a port of a flow. 
Setting failed: EtherType tag 
value is unknown 
The EtherType tag value for a port or a flow is different from the one 
configured at system level. 
EtherType tag cannot be 
modified for a port attached to 
LAG 
The EtherType tag value is in use by the LAG. 
2.3 DS1 (E1/T1) Ports 
E1/T1 ports can be configured to work as E1 ports or T1 ports on the ds1 (digital signal) level. The E1/T1 
ports are bound to VCGs via GFP ports and logical MAC ports. 
This means that there is no need to choose E1 or T1 when ordering the unit. 
 
 
ETX-2i Devices 
2. Cards and Ports 
Applicability and Scaling 
This feature is applicable to the following: 
• 
ETX-2i with an E1/T1 module: 
 
The E1/T1 ports are bound to VCGs via GFP ports and logical MAC ports.  
 
The port numbers contain slot numbers. 
Functional Description 
All ports must work in the same mode; therefore, configuring any port sets all ports to the same mode.  
Before changing the E1/T1 port mode, any corresponding GFP ports/VCGs/logical MAC 
ports/pseudowires/PW cross connects must be deleted. After changing the mode, ETX-2i must be 
restarted. 
Factory Defaults 
By default, the E1/T1 ports are set to E1 mode. 
 
Configuring E1/T1 Ports 
 To configure E1/T1 ports: 
1. At the config>port# prompt, type: 
ds1 [<slot>/]<port> 
The config>port>ds1([<slot>/]<port>)# prompt is displayed. 
2. To configure the E1/T1 port to E1 or T1 mode, type: 
frame-type { e1 | t1 } 

## 2.4 E1 Ports  *(p.551)*

ETX-2i Devices 
2. Cards and Ports 
2.4 E1 Ports 
The European Conference of Postal and Telecommunications Administrations (CEPT) standardized the 
E-Carrier system, which was then adopted by the International Union Telecommunication 
Standardization sector (ITU-T) and is used in almost all countries outside the USA, Canada, and Japan. 
The most commonly used versions are E1 and E3. E1 lines are high-speed dedicated lines that enable 
large volume usage. E1 circuits are very common in most telephone exchanges and used to connect 
medium and large companies to remote exchanges. In many cases, E1 connects exchanges with each 
other. 
Applicability and Scaling 
E1 ports are applicable to the ETX-2i products as follows: 
• 
ETX­2i and ETX-2i-B (and for ETX-2i-10G in standalone mode only): 
 
Smart SFP E1 ports are available when smart SFPs such as MiRICi-E1 or MiTOP-E1 are 
provisioned (see Smart SFPs). 
 
Smart SFP E1 ports do not support encapsulation via VCG. 
 
Smart SFP E1 ports are referenced as [<slot>/]<port>/<tributary>, with the following 
condition: 
 
<tributary> is always set to 1. 
• 
ETX­2i with an E1/T1 module: 
 
Modular E1/T1 ports can be configured to E1 mode (see DS1 (E1/T1) Ports). The default 
mode is E1.  
 
Modular E1 ports support encapsulation via VCG (see VCGs). 
 
Modular E1 ports are referenced as <slot>/<port>. 
• 
ETX-2i with 64 built-in E1 ports: 
 
Built-in E1 ports support TDM pseudowires. 
 
Built-in E1 ports are referenced as <slot>/<port>. 
E1 ports (built-in, modular, and smart SFP) are not applicable to ETX-2i-100G. 
 
 
ETX-2i Devices 
2. Cards and Ports 
Standards Compliance 
CCITT G.732 
ITU-T G.703 
ITU-T G.704 
ITU-T G.823 
Functional Description 
An E1 link operates over a twisted pair of cables. A nominal 3-volt peak signal is encoded with pulses 
using a method that avoids long periods without polarity changes. The line data rate is 2.048 Mbps at 
full duplex, which means 2.048 Mbps downstream and 2.048 Mbps upstream. The E1 signal splits into 
32 timeslots each of which is allocated 8 bits. Each timeslot sends and receives an 8-bit sample 
8000 times per second (8 x 8000 x 32 = 2,048,000), which is ideal for voice telephone calls where the 
voice is sampled into an 8-bit number at that data rate and restored at the other end. The timeslots are 
numbered 0 to 31. 
E1 Line Signal Characteristics 
E1 signal characteristics are specified in ITU-T Rec. G.703. The nominal data rate of the E1 signal is 2.048 
Mbps. The E1 line signal is encoded in the High-Density Bipolar 3 (HDB3) code.  
HDB3 is based on the alternate mark inversion (AMI) code. In the AMI code, “1”s are alternately 
transmitted as positive and negative pulses, whereas “0”s are transmitted as a zero voltage level. To 
prevent the transmission of long strings of “0”s, which do not carry timing information, the HDB3 coding 
rules restrict the length of a “0” string that can be transmitted through the line to a maximum of three 
pulse intervals. Longer strings of “0”s are encoded at the transmit end to introduce non-zero pulses. 
To allow the receiving end to detect the artificially-introduced pulses and enable their removal, in order 
to restore the original data string, the encoding introduces intentional coding violations in the sequence 
transmitted to the line. The receiving end detects these violations; when they appear to be part of an 
encoded “0” string, they are removed. 
Coding violations can also be caused by transmission errors. Therefore, coding violations that cannot be 
interpreted as intentional coding violations can be counted, and thus provide information on the quality 
of the transmission link. 
ETX-2i Devices 
2. Cards and Ports 
E1 Signal Structure 
The E1 line operates at a nominal rate of 2.048 Mbps. The data transferred over the E1 line is organized 
in frames. Each E1 frame includes 256 bits.  
The E1 frame format, as defined in ITU-T Rec. G.704, is shown below. 
Time Slot 0
Time Slot 16
Time Slots 1-15, 17-31
FAS
MAS
a. Even Frames (0,2,4-14)
b. Odd Frames (1,3,5-15)
a. Frame 0
b. Frames 1-15
Channel Data
1
0
0
1
1
0
1
1
I
1 A N N N N N
0
0
0
0 X Y X X
A B C D A B C D
1
2
3
4
5
6
7
8
32 Time Slots/Frame
8 Bits per
Time Slot
16 Frames/Multiframe
TS
0
TS
1
TS
2
TS
3
TS
4
TS
5
TS
6
TS
7
TS
8
TS
9
TS
10
TS
11
TS
12
TS
13
TS
14
TS
15
TS
16
TS
17
TS
18
TS
19
TS
20
TS
21
TS
22
TS
23
TS
24
TS
25
TS
26
TS
27
TS
28
TS
29
TS
30
TS
31
FR
0
FR
1
FR
2
FR
3
FR
4
FR
5
FR
6
FR
7
FR
8
FR
9
FR
10
FR
11
FR
12
FR
13
FR
14
FR
15
Notes
ABCD
X
Y
MAS
I
N
A
FAS
International Bit
National Bits (Sa4 through Sa8)
Alarm Indication Signal (Loss of Frame Alignment - Red Alarm)
Frame Alignment Signal, occupies alternate
(but not necessarily even) frames
ABCD Signaling Bits
Extra Bit
Loss of Multiframe Alignment
Multiframe Alignment Signal
 
The 256 bits included in a frame are organized in 32 timeslots of eight bits each. The frame repetition 
rate is 8,000 per second; therefore, the data rate supported by each timeslot is 64 kbps. 
Timeslot 0 
Timeslot 0 of E1 frames is used for two main purposes: 
• 
Delineation of frame boundaries. For this purpose, in every second frame, timeslot 0 carries a 
fixed pattern, called frame alignment signal (FAS). Frames carrying the FAS are defined as even 
frames, because they are assigned the numbers 0, 2, 4, etc. when larger structures (multiframes) 
are used. 
The receiving equipment searches for the fixed FAS pattern in the data stream using a special 
algorithm, a process called frame synchronization. Once this process is successfully completed, 
the equipment can identify each bit in the received frames. 
 
 
ETX-2i Devices 
2. Cards and Ports 
• 
Interchange of housekeeping information. In every frame without FAS (odd frames), timeslot 0 
carries housekeeping information. This information is carried as follows: 
 
Bit 1 – this bit is called the international (I) bit. Its main use is for error detection using the 
optional CRC-4 function (CRC-4 stands for Cyclic Redundancy Check, using a fourth-degree 
polynomial). This function is described below. 
 
Bit 2 is always set to 1 and used by the frame alignment algorithm. 
 
Bit 3 is used as a remote alarm indication (RAI), to notify the equipment at the other end 
that the local equipment lost frame alignment or did not receive an input signal. 
 
The other bits, identified as Sa4 through Sa8, are designated national bits, and are actually 
available to the users, if there is an agreement regarding their use. The total data rate that 
can be carried by each national bit is 4 kbps. 
Multiframes 
To increase the information carrying capacity without wasting bandwidth, the frames are organized in 
larger patterns, called multiframes. ITU-T Rec. G.704 recommendations define the following types of 
multiframes:  
• 
Basic G.704 framing 
• 
G.704 framing with timeslot 16 multiframe. 
Basic G.704 Multiframe 
The basic G.704 structure consists of two frames, which are identified by means of the information 
included in timeslot 0:  
• 
The even frame of the pair includes the frame alignment signal (FAS). 
• 
The odd frame has a 1 in bit position 2, and housekeeping information in the other bits. 
The number of timeslots available for user data is 31, and therefore the maximum payload rate is 
1984 kbps. 
To enable the transmission of network management information, a separate timeslot may have to be 
assigned within the frame. This procedure is called common channel signaling (CCS). The CCS 
information is often transmitted in timeslot 16. 
 
 
ETX-2i Devices 
2. Cards and Ports 
G.704 Framing with Timeslot 16 Multiframe (“G.704 Multiframe”) 
The G.704 multiframe structure has 16 frames, which are identified by means of a separate multiframe 
alignment signal (MAS) contained in timeslot 16 of each frame.  
The G.704 multiframe structure is generally used when timeslot 16 serves for the end-to-end 
transmission of channel-associated signaling (CAS). A typical application in which timeslot 16 serves for 
the transmission of signaling is the transfer of voice channels by means of voice modules, which use 
channel-associated signaling. 
Since timeslot 16 must be reserved for the transmission of the MAS and system signaling, only 30 
timeslots are available for the user payload, and the maximum payload rate is 1920 kbps.  
When using the G.704 multiframe format, timeslot 16 of each of the 16 frames in each multiframe 
carries the following information: 
• 
The first four bits of timeslot 16 in multiframe 16 always carry the multiframe alignment 
sequence, 0000. 
• 
Bit 6 in timeslot 16 in multiframe 0 is used to notify the equipment at the other end of the link 
that the local equipment lost multiframe alignment. 
• 
The other bits of this timeslot do not have mandatory functions. 
Channel Associated Signaling 
When using the G.704 multiframe format, timeslots 16 in frames 1 through 15 of each multiframe are 
available for carrying user information. In general, this information is the signaling information for the 
30 payload timeslots (channels). 
As shown below, four signaling bits, designated A, B, C, and D, are available for each channel, thereby 
enabling end-to-end transmission of four signaling states. Each frame in the multiframe carries the 
signaling information of two channels. 
CRC-4 Error Detection 
The ETX-2i system supports the CRC-4 function in accordance with ITU-T Rec. G.704 and G.706. The 
CRC-4 function is used to detect errors in the received data, and therefore can be used to evaluate data 
transmission quality over E1 links. 
This function can be enabled or disabled independently for each link by the user.  
To enable error detection, additional information must be provided to the receiving equipment. The 
additional information is transmitted to the receiving equipment by using a multiframe structure called 
ETX-2i Devices 
2. Cards and Ports 
CRC-4 multiframes. A CRC-4 multiframe is an arbitrary group of 16 frames. This group is not related in 
any way to the G.704 16-frame multiframe structures explained above. 
• 
A CRC-4 multiframe always starts with an even frame (a frame that carries the frame alignment 
signal). The CRC-4 multiframe structure is identified by a six-bit CRC-4 multiframe alignment 
signal, which is multiplexed into bit 1 of timeslot 0 of each odd-numbered (1, 3, 5, etc.) frame of 
the CRC-4 multiframe (i.e., in frames 1 through 11 of the CRC-4 multiframe). 
• 
Each CRC-4 multiframe is divided into two submultiframes of 8 frames (2048 bits) each. The 
detection of errors is achieved by calculating a four-bit checksum on each 2048-bit block 
(submultiframe). The four checksum bits calculated on a given submultiframe are multiplexed, 
bit by bit, in bit 1 of timeslot 0 of each even-numbered frame of the next submultiframe. 
• 
At the receiving end, the checksum is calculated again on each submultiframe and then 
compared against the original checksum (sent by the transmitting end in the next 
submultiframe). The results are reported by two bits multiplexed in bit 1 of timeslot 0 in frames 
13, 15 of the CRC-4 multiframe, respectively. Errors are counted and used to prepare statistic 
data on transmission performance. 
Framing 
E1 ports can be configured in accordance with the desired ITU-T framing mode by means of the line-
type parameter: 
• 
Basic G.704 framing (identified as G.732N) for applications that require CCS.  
• 
G.704 framing with timeslot 16 multiframe (identified as G.732S and referred to as G.704 
multiframe mode) for applications that require CAS. 
• 
Unframed mode for transparent transfer of 2.048 Mbps streams, including streams with 
proprietary framing. Also enables transferring framed E1 streams without terminating timeslot 
0, and timeslot 16. 
The framer automatically adds the appropriate overhead. Unused timeslots are filled with a 
user-specified idle code.  
The framing mode can be independently selected for each E1 port. 
Interface Type 
E1 ports support two line interfaces: 
• 
120Ω balanced line interface. The nominal balanced interface transmit level is ±3V. 
• 
75Ω unbalanced interface. The nominal unbalanced interface transmit level is ±2.37V. 
ETX-2i Devices 
2. Cards and Ports 
Only one of these interfaces can be active at any time. The active interface can be selected by the user, 
separately for each port. 
Receive Signal Attenuation  
The E1 line interfaces have integral LTUs, which enable long-haul operation with line attenuation of up 
to 43 dB. The line interface can also emulate a DSU interface, for short-haul applications: in this case, 
the maximum line attenuation is 12 dB. The receive signal attenuation level is configured by means of 
the rx-sensitivity parameter. 
E1 Loopback Testing 
Diagnostic tools at the E1 level include loopback tests for checking the source of faults in a transmission 
path. You can configure the following types of loopback capabilities on an E1 port: 
• 
Local loopback – tests the connection between the E1 port in the device and the local TDM 
network. Packets sent from the TDM to an E1 port configured with local loopback, are looped 
back from the E1 port to the TDM.  
• 
Remote loopback – tests traffic between the E1 port in the device and the remote packet-
switching network (PSN). PSN packets sent from the packet-switching network (PSN) to an E1 
port configured with remote loopback, are looped back from the E1 port to the PSN.  
ETX
TDM
PSN
E1/T1
Local 
Loop
Remote 
Loop
 
Local and Remote Loopback on E1 Port 
Factory Defaults 
By default, no smart SFP E1 ports exist.  
By default, modular E1/T1 ports are set to E1 mode and have the following configuration. 
Parameter 
Value 
Remarks 
interface-type 
balanced 
Line impedance type 
line-code 
hdb3 
Transmission line code 
line-type 
Unframed   
Port framing mode 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Value 
Remarks 
name 
E1 <slot>/<port> DS1 <port>   
 
pm-enable 
no pm-enable 
Performance monitoring is 
disabled 
rx-sensitivity 
short-haul 
Attenuation level of received 
signal 
shutdown 
shutdown 
Administratively disabled 
Configuring E1 Ports 
Configuring Built-in E1 Ports 
 To configure E1 ports: 
1. Navigate to configure port e1 <slot>/<port>. 
2. At the config>port# prompt, type: 
e1 <slot>/<port>/<tributary> 
The prompt config>port>e1(<slot>/<port>/<tributary>)# is displayed. 
3. Perform the required tasks according to the following table. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Specifying 
out-of-service 
indication to transmit 
for E1 port with CAS 
signaling  
cas-oos-codes space <space-code> mark 
<mark-code> 
space-code - space 
signaling code allowed 
range: 0x0–0xf 
mark-code - mark 
signaling code allowed 
range: 0x0–0xf 
Note:  
• This command is 
relevant only with line 
type g732s or 
g732s-crc. 
• When R bits and L bits 
are used to indicate E1 
CAS faults on the 
remote side, the OOS 
code sent to the E1 
CAS interface is the 
default (0xFF), rather 
than the actual OOS 
code. 
 
Specifying transmission 
sequence for 
out-of-service 
indication for E1 port 
with CAS signaling 
cas-oos-pattern {space | mark | space-mark} 
Note: This command is 
relevant only with line 
type g732s or g732s-crc. 
Specifying code 
transmitted to fill idle 
(unused) timeslots in 
the E1 frames  
idle-code <idle-code-val> 
Possible values: 0x00–
0xFF (default 0x7E) 
CAS idle-code has fixed 
value of 0x5 (0101). 
Specifying E1 port 
impedance 
interface-type { balanced | unbalanced } 
Specifying impedance of 
E1 port: 
balanced – 120Ω 
balanced interface 
unbalanced 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Defining the 
transmission line code 
line-code { hdb3 | ami } 
hdb3 – Referred to as 
High Density Bipolar of 
order 3 code (HDB3), it is 
a telecommunication line 
code based on AMI and 
used in E1 lines. It is 
similar to B8ZS used in T1 
lines. 
ami – Referred to as 
Alternate Mark Inversion 
(AMI) because a 1 is 
referred to as a mark and 
a 0 as a space. 
Specifying threshold at 
which to trigger 
threshold crossing alert 
for line ES (errored 
seconds) 
line-interval-threshold es <es-value > 
 
Specifying the framing 
mode of the port 
line-type { unframed | g732n | g732n-crc | 
g732s | g732s-crc }  
unframed – no framing;  
g732n – G.732N framing 
with CRC disabled 
g732n-crc – G.732N 
framing with CRC enabled  
g732s – G.732S framing 
(CAS) with CRC disabled 
g732s-crc – G.732S 
framing (CAS) with CRC 
enabled. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Running loopback test 
on E1 port 
loopback {local | remote} 
[duration <seconds>]  
local – data sent from the 
local TDM to the E1 port, 
is looped back to the 
TDM. 
remote –  data sent from 
the remote PSN to the E1 
port, is looped back to the 
PSN. 
 
duration – specifies the 
duration of the loopback 
(in seconds).  
Possible values: 1 to 3600 
If duration is not 
specified, the loopback 
test runs forever, until 
stopped. 
Use no loopback to 
disable the loopback test. 
Assigning a name to the 
port 
name <string> 
 
Defining the value to be 
transmitted if the 
corresponding PW is 
out of service 
out-of-service <oos> 
Possible values: 0x00–
0xFF (default 0xFF) 
If the corresponding PW is 
out of service, ETX-2i 
transmits the configured 
value on a time slot that is 
assigned to the PW 
toward the TDM side 
(relevant only for framed 
E1 ports). 
Specifying if 
performance reporting 
is enabled for the port 
pm-enable 
 
Specifying the 
attenuation level of the 
received signal, 
compensated for by the 
interface receive path 
rx-sensitivity {short-haul | long-haul} 
short-haul – low 
sensitivity (-12 dB) 
long-haul – high 
sensitivity (-43 dB) 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Administratively 
enabling the port 
no shutdown 
Enter shutdown to 
administratively disable 
the port. 
Displaying list of 
interfaces bound to E1 
port 
show bind 
Displays ports bound to 
E1 (PW, GFP) 
Displaying loopback test 
status 
show loopback 
 
Displaying E1 port 
operational status 
show status 
See Viewing E1 Port 
Status. 
Displaying the port 
statistics 
show statistics current 
show statistics interval <interval-num> 
show statistics total 
show statistics all-intervals 
show statistics all 
E1 current and interval 
statistics for E1 unframed 
and E1 framed with CRC. 
You can specify the scope 
of the statistics, as 
follows: 
current – current 
statistics 
interval – interval 
statistics 
Where  
interval-num – interval 
number 
Possible values: 1-96 
total – preceding 24 
hours cumulative 
statistics 
all-intervals – all interval 
statistics 
all – all statistics 
See Viewing E1 Port 
Statistics. 
Clearing the statistics 
clear-statistics 
 
ETX-2i Devices 
2. Cards and Ports 
Configuring Modular E1 Ports 
 To configure E1 ports: 
1. If the module type is not E1/T1, power off ETX-2i, insert the E1/T1 module, and then power on 
ETX-2i. 
2. Provision the module type as E1/T1 (see Configuring Module). 
3. Configure the port to E1 mode (see Configuring E1/T1 Ports). 
4. At the config>port# prompt, type: 
e1 [<slot>/]<port>/<tributary> 
The prompt config>port>e1([<slot>/]<port>/<tributary>)# is displayed. 
5. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying if E1 interface is 
balanced or unbalanced 
interface-type { balanced | unbalanced } 
 
Defining the transmission line 
code 
line-code { hdb3 | ami } 
hdb3 – Referred to as High 
Density Bipolar of order 3 
code (HDB3), it is a 
telecommunication line code 
based on AMI and used in E1 
lines. It is similar to B8ZS 
used in T1 lines. 
ami – Referred to as 
Alternate Mark Inversion 
(AMI) because a 1 is referred 
to as a mark and a 0 as a 
space. 
Note: Only hdb3 can be 
configured for modular E1 
ports. 
 
Specifying the framing mode of 
the port 
line-type g732n-crc  
g732n-crc – G.732N framing 
with CRC enabled 
Note: Only g732n-crc can be 
configured for modular E1 
ports. 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Running loopback test on E1 port 
loopback {local | remote}  
[duration <seconds>]  
local – data sent from the 
local TDM to the E1 port, is 
looped back to the TDM. 
remote –  data sent from the 
remote PSN to the E1 port, is 
looped back to the PSN. 
Currently not supported. 
duration – specifies the 
duration of the loopback (in 
seconds).  
Possible values: 1 to 3600 If 
duration is 0 or is not 
specified, the loopback test 
runs forever, until stopped. 
Use no loopback to disable 
the loopback test. 
Assigning a name to the port 
name <string> 
 
Specifying if performance 
reporting is enabled for the port 
pm-enable 
 
Specifying the attenuation level 
of the received signal, 
compensated for by the interface 
receive path 
rx-sensitivity {short-haul | long-haul} 
short-haul – low sensitivity 
long-haul – high sensitivity 
Administratively disabling or 
enabling the port 
shutdown 
Enter no shutdown to 
administratively enable the 
port. 
Displaying list of interfaces 
bound to port 
show bind 
 
Displaying loopback test status 
show loopback 
 
Displaying the port status 
show status 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Displaying the port statistics 
show statistics current 
show statistics interval <interval-num> 
show statistics total 
show statistics all-intervals 
show statistics all 
You can specify the scope of 
the statistics, as follows: 
current – current statistics 
interval – interval statistics 
Where  
interval-num – interval 
number 
Possible values: 1-96 
total – preceding 24 hours 
cumulative statistics 
all-intervals – all interval 
statistics 
all – all statistics 
Clearing the statistics 
clear-statistics 
 
Configuring Smart SFP E1 Ports 
 To configure smart SFP E1 ports: 
1. Provision a smart SFP port with type MiRICi-E1 or MiTOP-E1 (see Smart SFPs). 
2. Insert the MiRICi-E1/MiTOP-E1 into the Ethernet port. 
Note 
Initialize the database of the MiTOP before inserting it into the device. Refer 
to Setting the Switches in the Installation and Setup chapter of the MiTOP 
E1T1 Installation and Operation manual.  
3. At the config>port# prompt, type: 
e1 [<slot>/]<port>/<tributary> 
The prompt config>port>e1([<slot>/]<port>/<tributary>)# is displayed. 
4. Perform the required tasks according to the following table, and the type of smart SFP. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
MiRICi 
MiTOP 
Defining the 
transmission line code 
line-code { hdb3 | ami } 
hdb3 – Referred to as High Density 
Bipolar of order 3 code (HDB3), it 
is a telecommunication line code 
based on AMI and used in E1 lines. 
It is similar to B8ZS used in T1 
lines. 
ami – Referred to as Alternate 
Mark Inversion (AMI) because a 1 
is referred to as a mark and a 0 as 
a space. 
 
 
Specifying the framing 
mode of the port 
line-type { unframed | 
g732n | g732n-crc | g732s 
| g732s-crc }  
unframed – no framing  
g732n – G.732N framing with CRC 
disabled 
g732n-crc – G.732N framing with 
CRC enabled 
g732s – G.732S framing (CAS) with 
CRC disabled 
g732s-crc – G.732S framing (CAS) 
with CRC enabled 
Note: 
• For MiRICi, only g732n and 
g732n-crc are relevant. 
• For MiRICi-E1, only g732n-crc is 
relevant. 
• For MiTOP, only g732n, 
g732n-crc, and unframed are 
relevant. 
• Selecting incorrect line-type 
generates an “Unsupported 
line type” error. 
 
 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
MiRICi 
MiTOP 
Running loopback test 
on E1 port 
loopback {local | remote}  
[duration <seconds>]  
local – data sent from the local 
TDM to the E1 port, is looped back 
to the TDM. 
remote –  data sent from the 
remote PSN to the E1 port, is 
looped back to the PSN. 
duration – specifies the duration 
of the loopback (in seconds).  
Possible values: 1 to 3600 
If duration is not specified, the 
loopback test runs forever, until 
stopped. 
Use no loopback to disable the 
loopback test. 
 
 
Assigning a name to the 
port 
name <string> 
 
 
 
Specifying if 
performance reporting is 
enabled for the port 
pm-enable 
 
 
 
Specifying the 
attenuation level of the 
received signal, 
compensated for by the 
interface receive path 
rx-sensitivity {short-haul | 
long-haul} 
short-haul – low sensitivity 
long-haul – high sensitivity 
 
 
Specifying the port clock 
quality 
source-clock-quality 
{stratum1 | stratum2 | 
stratum3 | stratum3e | 
stratum4} 
Clock quality used in adaptive 
clock recovery set according to 
parameter specified: 
stratum1 – PRC G.811  
stratum2 – Type II G.812 
stratum3 – Type IV G.812 
stratum3e – Type III G.812 
stratum4 – Free running 
× 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
MiRICi 
MiTOP 
Selecting the transmit 
clock source 
tx-clock-source {loopback 
| internal | 
domain <number> | 
pw <number>} 
loopback – Rx clock; clock 
retrieved from the port's incoming 
(Rx) data 
internal – clock provided by 
internal oscillator 
domain – clock provided by clock 
domain, if device has timing 
option. 
pw – clock provided by PW bundle 
Note: The domain and pw options 
are available only for MiTOP. 
 
 
Administratively 
disabling or enabling the 
port 
shutdown 
Enter no shutdown to 
administratively enable the port. 
Note: Following shutdown and 
then no shutdown of Smart SFP 
port, you must perform shutdown 
and then no shutdown of PW. 
 
 
Displaying list of 
interfaces bound to port 
show bind 
 
 
 
Displaying loopback test 
status 
show loopback 
 
 
 
Displaying the port 
status 
show status 
 
 
 
Displaying the port 
statistics 
show statistics current 
show statistics interval 
<interval-num> 
show statistics total 
show statistics 
all-intervals 
show statistics all 
You can specify the scope of the 
statistics, as follows: 
current – current statistics 
interval – interval statistics 
Where  
interval-num – interval number 
Possible values: 1-96 
total – preceding 24 hours 
cumulative statistics 
all-intervals – all interval statistics 
all – all statistics 
 
 
Clearing the statistics 
clear-statistics 
 
 
 
 
ETX-2i Devices 
2. Cards and Ports 
Viewing E1 Port Status 
You can display the current status of an E1 port, including port name, administrative and operation 
status, and interface type.  
 To display the status of a specific E1 port: 
• 
At the prompt config>port>e1([<slot>/]<port-num>)#, enter: 
show status 
The E1 port status parameters are displayed.  
 To display the status of E1 1/3 port 
ETX­2i# show con port e1 1/3 status 
Name                  : E1 1/3                                               
Administrative Status : Up                                                   
Operation Status      : Up                                                   
Interface Type        : Balanced                                             
Detailed Status       :            
Viewing E1 Port Statistics 
Internal E1 ports collect performance monitoring data at the line and path level. 
 To display the E1 port statistics: 
1. Verify that statistics collection is enabled (pm-enable) for the E1 port. 
2. At the prompt config>slot>port>e1 (<slot/port/tributary>)#, enter show statistics followed by 
parameters listed below. 
E1 statistics are displayed. The counters are described below. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Displaying statistics 
show statistics {current | interval <interval-
num 1..96> | current-day | previous-day | all-
intervals | all}  
current – Displays the current 
interval statistics 
interval (1–96) – Displays statistics 
for a selected interval 
current-day – Displays statistics for 
current day starting from 12:00 
midnight 
previous-day – Displays statistics for 
24 hours before last 12:00 midnight 
all-intervals – Displays statistics for 
all existing intervals (up to 96) 
all – Displays all statistics in 
succession: current > all intervals > 
current day > previous day 
 To display the statistics for E1 port 1/3: 
ETX-2i# configure port e1 1/3 
ETX-2i>config>port>e1(1/3)# show statistics current 
Current 
---------------------------------------------------------------------------- 
Time Elapsed (Sec) : 606 
Valid Intervals    : 96 
 
Line 
---------------------------------------------------------------------------- 
CV                         : 0 
ES                         : 0 
SES                        : 
 
Path 
---------------------------------------------------------------------------- 
CV                         : 0          UAS                        : 0 
ES                         : 0          FC                         : 
SES                        : 0 
SEFS                       : 0 
Rx Frames Slip             : 0 
 
 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
Time Elapsed (Sec) 
The elapsed time (in seconds) since the beginning of the current interval, in 
seconds. The range is 1 to 900 seconds. 
Valid Intervals 
Number of elapsed finished 15-min intervals for which statistics data can be 
displayed, in addition to the current (not finished) interval (up to 96). 
Line 
CV 
Number of CRC-4 errors 
ES 
Number of Errored Seconds. 
Number of seconds during which at least one FE or CS was detected or a SEF 
defect or an AIS defect was present. 
SES 
Number of severely errored seconds (SES). 
Number of seconds during which 805 or more CRC-4 errors were detected or 
an OOF defect was present. 
Path 
 
CV 
Same as for Line (see above) 
ES 
Same as for Line (see above).  
This parameter is inhibited during UAS state. 
SES  
Same as for Line (see above) 
This parameter is inhibited during UAS state. 
SEFS 
Number of Severely Errored Framing Seconds. The number of seconds during 
which at least one OOF defect or AIS defect was present. 
Rx Frames Slip 
Total number of loss of Rx Frames Slip events in the interval 
UAS 
Number of seconds for which the E1 path is unavailable. The E1 path becomes 
unavailable at the onset of 10 contiguous SESs. The 10 SESs are included in 
unavailable time. Once unavailable, the E1 path becomes available at the onset 
of 10 contiguous seconds with no SESs. The 10 seconds with no SESs are 
excluded from unavailable time. 
FC 
Number of E1 path failure events.  
A failure event begins when a Loss of Frame (LOF) failure or Alarm Indication 
Signal (AIS) failure is declared, and ends when the failure is cleared. A failure 
event that begins in one period and ends in another period is counted only in 
the period in which it begins. 
For unframed E1 ports, only FC counter is available. 

## 2.5 E3 Ports  *(p.572)*

ETX-2i Devices 
2. Cards and Ports 
2.5 E3 Ports 
Groups of E1 circuits are bundled into higher-capacity E3 links, which are mainly used between 
exchanges, operators, and/or countries, and have a transmission speed of 34.368 Mbps. 
E3 ports are available when smart SFPs such as MiRICi-E3 or MiTOP-E3 are provisioned (see Smart SFPs). 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, except for ETX-2i-100G that does not support smart 
SFPs. 
Smart SFP E3 ports are referenced as [<slot>/]<port>/<tributary>, with the following condition: 
• 
<tributary> is always set to 1. 
Standards Compliance  
ITU-T G.703 
ITU-T G.704 
ITU-T G.823 
Functional Description 
Each E3 signal has 16 E1 channels, and each channel transmits at 2.048 Mbps. E3 links use all eight bits 
of a channel. 
Factory Defaults 
By default, no E3 ports exist. 
ETX-2i Devices 
2. Cards and Ports 
Configuring E3 Ports 
 To configure E3 ports: 
1. Provision a smart SFP such as MiRICi-E3 or MiTOP-E3 and insert it into an Ethernet port (see 
Smart SFPs). 
Note 
Initialize the database of the MiTOP before inserting it into the device. Refer 
to Setting the Switches in the Installation and Setup chapter of the MiTOP 
E1T1 Installation and Operation manual.  
2. At the config>port# prompt, enter: 
e3 [<slot>/]<port>/<tributary> 
The prompt config>port>e3([<slot>/]<port>/<tributary>)# is displayed. 
3. Perform the required tasks according to the following table, and the type of smart SFP. 
Task 
Command 
Comments 
MiRICi 
MiTOP 
Specifying the framing 
mode of the port 
line-type { framed | 
unframed } 
framed – framing 
unframed – no framing 
Note: Only unframed option is 
supported. 
 
 
Running loopback test 
on E3 port 
loopback {local | remote } 
[start <seconds> ] 
[duration <seconds>]  
local – data sent from the local 
TDM to the E1 port, is looped 
back to the TDM. 
remote –  data sent from the 
remote PSN to the E1 port, is 
looped back to the PSN. 
start – specifies the time (in 
seconds) until the loopback 
starts. Possible values: 1 to 3600 
duration – specifies the duration 
of the loopback (in seconds). 
Possible values: 1 to 3600 
If duration is not specified, the 
loopback test runs forever, until 
stopped. 
Use no loopback to disable the 
loopback test. 
 
 
Assigning a name to 
the port 
name <string> 
 
 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
MiRICi 
MiTOP 
Specifying if 
performance reporting 
is enabled for the port 
pm-enable 
 
 
 
Specifying the port 
clock quality 
source-clock-quality 
{stratum1 | stratum2 | 
stratum3 | stratum3e | 
stratum4} 
Clock quality used in adaptive 
clock recovery set according to 
parameter specified: 
stratum1 – PRC G.811  
stratum2 – Type II G.812 
stratum3 – Type IV G.812 
stratum3e – Type III G.812 
stratum4 – Free running 
× 
 
Selecting the transmit 
clock source 
tx-clock-source {loopback | 
internal | pw <number>} 
loopback – clock retrieved from 
the port's incoming (Rx) data 
internal – clock provided by 
internal oscillator 
pw – clock provided by PW 
bundle 
Note: The pw option is available 
only for MiTOP. 
 
 
Administratively 
enabling the port 
no shutdown 
Enter shutdown to 
administratively disable the port. 
Note:  Following shutdown and 
then no shutdown of Smart SFP 
port, you must perform 
shutdown and then no shutdown 
of PW. 
 
 
Displaying list of 
interfaces bound to 
port 
show bind 
 
 
 
Displaying loopback 
test status 
show loopback 
 
 
 
Displaying the port 
status 
show status 
 
 
 

## 2.6 Ethernet Ports  *(p.575)*

ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
MiRICi 
MiTOP 
Displaying the port 
statistics 
show statistics current 
show statistics interval 
<interval-num> 
show statistics total 
show statistics all-intervals 
show statistics all 
You can specify the scope of the 
statistics, as follows: 
current – current statistics 
interval – interval statistics 
Where  
interval-num – interval number 
Possible values: 1-96 
total – preceding 24 hours 
cumulative statistics 
all-intervals – all interval 
statistics 
all – all statistics 
 
 
Clearing the statistics 
clear-statistics 
 
 
 
2.6 Ethernet Ports 
Applicability and Scaling 
Attribute 
ETX-
2i 
ETX-
2i-B 
ETX-2i-10G 
ETX-2i-100G 
Scaling/Comments 
Access control via 
802.1x 
authentication 
✓ 
✓ 
✓ 
✓ 
This protocol uses the 
RADIUS client 
authentication. 
Auto-negotiation 
✓ 
✓ 
SFP+ ports configured to 
1G 
SFP+ ports 
configured to 1G 
Auto-negotiation can be 
enabled only if silent start 
is disabled. 
Clock-related 
parameters 
✓ 
✓ 
✓ 
Except for 
ETX-2i-10G-B/  
8SFPP 
✓ 
 
Ethernet 100GbE 
ports 
 
 
 
✓ 
 
ETX-2i Devices 
2. Cards and Ports 
Attribute 
ETX-
2i 
ETX-
2i-B 
ETX-2i-10G 
ETX-2i-100G 
Scaling/Comments 
Ethernet 10GbE 
ports 
 
 
✓ 
✓ 
 
Ethernet GbE 
ports 
✓ 
✓ 
✓ 
Except for 
ETX-2i-10G-B/  
8SFPP 
✓ 
 
Fat Pipe 
 
 
ETX-2i-10G half 19-inch; 
ETX-2i-10G-B full and 
half 19-inch; ETX-2i-
10G-B/8SFPP (full and 
half 19-inch models), 
ports 1-4 
ETX-2i-100G/4Q 
user ports, ETX-
2i-100G/40G user 
ports 
 
See the following table for 
more specific information. 
FEC 
 
 
 
SFP28 and 
QSFP28 ports 
 
Link Fail Signal 
(LFS) 
 
 
ETX-2i-10G-B/  
8SFPP 10G ports 
ETX-2i-100G 10G 
and 100G ports 
 
SFP/RJ-45 combo 
ports 
✓ 
 
Half 19-inch (specific 
flavor) 
✓ 
 
Slot 
✓ 
✓ 
✓ 
✓ 
 
Tunable SFPP 
 
 
ETX-2i-10G-B/8SFPP 
(and ETX-2i-10G full 19-
inch in Charter ver. 6.4 
only) 
10G SFPP ports only  
 
 
Tunable QSFP28 
 
 
✓ 
✓ 
 
Self-tuning  
 
 
 
✓ 
Supported for the 100G 
self-tuning transceiver 
(QSFP28-10DH). 
The following table indicates the Fat pipe features supported in various devices. 
 
ETX-2i-10G 
(4+8) 
ETX-2i-10G-B 
(4+8) 
ETX-2i-10G-
B/8SFPP 
ETX-2i-100G/4Q 
business 
ETX-2i-
100G/40G 
Basic support  
(IPv4 and IPv6) 
✓ 
✓ 
✓ 
Only UNI 
Only UNI 
ETX-2i Devices 
2. Cards and Ports 
ETX-2i-10G 
(4+8) 
ETX-2i-10G-B 
(4+8) 
ETX-2i-10G-
B/8SFPP 
ETX-2i-100G/4Q 
business 
ETX-2i-
100G/40G 
Partial field 
detection 
(non-IP, no 
VLAN) 
 
 
✓ 
Only UNI 
Only UNI 
Over LAG 
✓ 
✓ 
✓ 
Only UNI 
Only UNI 
Detection 
behind three 
MPLSoIP tags 
 
 
✓ 
Only UNI 
 
 
Note 
ETX-2i-10G (4+24) , and ETX-2i-100G/4Q CSG do not support Fat pipe. 
Functional Description 
Port Access Control via 802.1x Authentication 
This additional security layer allows controlling access to specific Ethernet ports using the 802.1x 
authentication protocol. IEEE 802.1x is part of the IEEE 802.1 group of networking protocol standards, 
and it is used to define Port-based Network Access Control (PNAC). It provides an authentication 
mechanism to devices wishing to attach to a LAN or WLAN. 
802.1x defines the encapsulation of the Extensible Authentication Protocol (EAP), known as "EAP over 
LAN" or EAPOL. 
802.1X authentication involves three parties: a supplicant, authenticator, and authentication server.  
• 
The supplicant is a client device (e.g., laptop) that wishes to attach to the LAN/WLAN.  
• 
The authenticator is a network device which provides a data link between the client and the 
network and can allow or block network traffic between the two. Examples include Ethernet 
switches and wireless access points. 
• 
The authentication server is typically a trusted server that can receive and respond to requests 
for network access, and can tell the authenticator if the connection is to be allowed. 
The authenticator acts like a security guard for a protected network. The supplicant (i.e., client device) is 
not allowed access through the authenticator to the protected side of the network until the supplicant's 
identity has been validated and authorized. With 802.1x port-based authentication, the supplicant must 
initially provide the required credentials and the authenticator forwards these credentials to the 
ETX-2i Devices 
2. Cards and Ports 
authentication server to decide whether access is to be granted. If the authentication server determines 
the credentials are valid, it informs the authenticator, which in turn allows the supplicant (client device) 
access to resources located on the protected side of the network. 
ETX-2i supports the following 802.1x functions: 
• 
Authenticator role 
• 
Port-based authentication 
The ETX-2i authenticator uses its RADIUS client to communicate with the RADIUS authentication server. 
Ethernet Local Management Interface (E-LMI) 
The Ethernet Local Management Interface (LMI) is an Ethernet layer operation, administration, and 
management (OAM) protocol. It provides information that enables devices to automatically configure 
customer edge (CE) devices, and also provides the status of Ethernet virtual connections (EVCs) for large 
Ethernet metropolitan-area networks (MANs) and WANs. Specifically, Ethernet LMI notifies a CE device 
on the operating state of an EVC and the time when an EVC is added or deleted. Ethernet LMI also 
communicates the attributes of an EVC and a user-network interface (UNI) to a CE device. 
The E-LMI protocol includes the procedures below as specified in MEF 16: 
• 
Notification to the CE of the addition of an EVC 
• 
Notification to the CE of the deletion of an EVC 
• 
Notification to the CE of the availability state of a configured EVC (Active, Not Active, or Partially 
Active) 
• 
Communication of UNI and EVC attributes to the CE. 
In addition to the CLI below, the following configuration is required: 
• 
L2CP profile at the port or untagged flow level with configured  
MAC ADDRESS = 01-80-C2-00-00-07 for E-LMI operations. 
• 
For EVCs distributed by E-LMI, the ‘service name’ attribute must be configured in the EVC flows. 
MAC Addresses 
ETX-2i has multiple MAC addresses. Each Ethernet port is assigned a different MAC address. 
You can view the MAC address assigned to an Ethernet port via show status (see Viewing Ethernet Port 
Status). For information on which MAC address is used by a particular feature, refer to the relevant 
section in this manual.   
ETX-2i Devices 
2. Cards and Ports 
EtherType 
EtherType configured per-port is used for identification of VLAN-tagged frames at ingress and EtherType 
stacking at egress. This refers to the outer VLAN only. The outer VLAN of an incoming packet must 
match the configured EtherType of the port in order to be considered a VLAN-tagged frame (otherwise 
the frame is considered untagged or dropped). Refer to the EtherType section in the Traffic Processing 
chapter for details.  
Fat Pipe Detection and Rate Limiting 
ETX-2i-10G half 19-inch, ETX-2i-10G-B (full and half 19-inch), ETX-2i-10G-B/8SFPP ports 1 to 4, and 
ETX-2i-100G/4Q and ETX-2i-100G/40G user ports, support Fat pipe (AKA elephant flow) detection, a 
mechanism that detects exceptionally high BW sessions (micro flows; both IPv4 and IPv6 packets) 
according to a search key, and binds a preconfigured BW Policer to the session, thus limiting its BW.  
 
Notes 
• 
When applying Fat pipe to a LAG port, you should bind the Fat pipe 
detection profile to the LAG anchor port.  
• 
ETX-2i-10G-B/8SFPP supports Fat pipe over UNI ports 1 to 4 only. 
• 
ETX-2i-100G/4Q and ETX-2i-100G/40G support Fat pipe over user ports 
only, i.e., ports 1/3-1/8, 3/3-3/4, and 2/1-2/8. 
It is also possible to run the release-fat-pipe command to release all flows caught as a result of a prior 
Fat pipe command, including clearing all invoked Policer allocations and the list of active Fat pipes. 
When running this command, all cleared results enter the Fat pipe history. 
At any time, you can display the information of active and history (closed) Fat pipes of an Ethernet port 
(see Viewing Fat Pipe Information). 
For a detailed description, refer to Fat Pipe Detection and Rate Limiting in the Traffic Processing 
chapter. 
Forward Error Correction (FEC)  
ETX-2i-100G/4Q supports Forward Error Correction (FEC) over their SFP28 and QSFP28 ports. This 
technique enables correcting errors in data transmitted over unreliable or noisy communication 
channels, without having to request retransmission of the data.   
Layer-2 Control Protocol (L2CP) Processing 
You can configure L2CP profiles (for details, refer to Layer-2 Control Protocol (L2CP) Processing in the 
Traffic Processing chapter), and then assign relevant L2CP profiles to the Ethernet ports (see below) 
ETX-2i Devices 
2. Cards and Ports 
and/or to flows (refer to Configuring Flows in the Traffic Processing chapter). You can also display the 
L2CP port statistics for an Ethernet port associated with an L2CP profile that is configured with tunneling 
and MAC swap (see Viewing Layer-2 Control Processing (L2CP) Statistics).  
 
Note 
• 
An L2CP profile that is attached to a port or flow can be modified or 
replaced, but it cannot be deleted. 
• 
L2CP MAC Swap supports up to 100 packets per second (pps).  
ETX-2i supports Layer-2 Protocol Tunneling (L2PT) – L2CP tunneling with MAC swap, which means that 
L2CP packets can be forwarded over networks that are not transparent to L2CP.  
L2PT is supported at the port level and applies for PTP flows, as well as for bridged traffic. 
• 
ETX-2i supports multiple network ports with L2PT functionality for both PTP and Bridge 
applications.  
• 
Any port configured as NNI is L2PT Network, by default.  
• 
Any other port can be configured to be L2PT Network (default ‘no’). 
• 
Any port assigned with an L2CP profile with MAC swap, including port 1, can function as an L2PT 
user port. 
You can bind an L2CP profile configured with L2CP MAC swap to a user port; it cannot be bound to a 
flow. A port assigned with an L2PT profile expects “native” L2CP frames. MAC swap is performed toward 
the relevant network port or user port that is configured for use as L2PT network ports.  
Policer Profiles 
You can limit the rate and burst size of traffic passing through an Ethernet port, in ONE of the following 
ways: 
• 
By applying a single Policer profile to the Ethernet port (policer command). This Policer profile 
defines the traffic types to be policed, as well as a single CIR and single CBS value to limit the 
rate and burst size of these traffic types.  
• 
By applying up to three Policer profiles to the Ethernet port (multi-policer command); one per 
traffic type (Broadcast, Multicast, and Unicast traffic). Each Policer profile defines a CIR and CBS 
to limit the rate and burst size of the traffic type.  
For a detailed explanation on Policer profiles, refer to Configuring Policer Profiles in the Traffic 
Processing chapter. 
ETX-2i Devices 
2. Cards and Ports 
Silent Start 
Network operators use both point-to-point and point-to-multipoint Optical Access Networks (OANs), 
depending on the application. For example, a Passive Optical Network (PON) is a point-to-multipoint 
OAN. One of the major challenges to operating and maintaining such OANs securely is that 
misconnecting a point-to-point Optical Network Terminal (ONT) or Ethernet equipment to a branch of a 
PON can cause a service outage in the PON system. In order to address this issue, a Silent Start function 
is introduced in all types of ONTs, which inhibits an ONT transmitter's power at startup until the receiver 
recognizes consistent incoming data. On recovery of "understandable" data by the receiver, the 
transmitter is enabled to enter a handshaking process with the Optical Line Terminal (OLT). 
Optical Network Units (ONUs) transmit in assigned time slots to avoid disturbing each other over the 
shard fiber, as a non-GPON device transmitting continuously is likely to bring down a GPON segment. 
Ethernet equipment can also be connected by mistake to a PON network and bring down the PON 
segment, to address this the ETX also supports a silent start functionality, which once enabled, allows 
optical Tx once a valid Ethernet signal is received. 
 
 
Passive Optical Network (PON) 
ETX-2i supports Silent Start functionality for the following ports: 
• 
Both 1GbE and 10GbE ports 
• 
Optical Ethernet port only 
 
 
ETX-2i Devices 
2. Cards and Ports 
• 
Ports configured to Auto-negotiation disabled (1GbE ports): 
 
Sanity prevents user from enabling Silent Start if Autoneg is enabled. 
 
Sanity prevents user from enabling Autoneg if Silent Start is enabled.  
When Silent Start is enabled and the optical transceiver detects Rx optical power down (no ‘Signal 
Detect’), Tx power shuts down (laser shutdown) and restarts the Silent Start ‘ETH search’ functionality. 
When Silent Start is enabled, optical Tx power becomes enabled when all the following conditions apply: 
• 
Rx optical power is detected. 
• 
Ethernet level synchronization is detected (PCS, PMD level). 
A Silent Start alarm is issued if Silent Start In Progress state lasts for at least one minute. 
 
Silent Start 
Tunable SFPP Modules 
DWDM networks support ETX-2i 10G and now ETX-2i-100G tunable QSFP28 devices as well. 
Typically, a DWDM network is set up with fixed wavelength DWDM transceivers. The laser hardware 
inside a DWDM optics has a fixed wavelength for transmitting over a DWDM channel. Meaning that if 
one channel fails, you need to replace the specific channel device with one from your spare part stock. 
ETX-2i Devices 
2. Cards and Ports 
As a DWDM network can be used with 40 channels, you need to stock 40 fixed wavelength DWDM 
modules. However, with Tunable SFP+ modules, you have the possibility to configure the wavelength of 
the DWDM SFPP modules, enabling you to reduce OPEX and store less spare parts. 
ETX-2i-10G-B/8SFPP (and ETX-2i-10G full 19-inch in Charter ver. 6.4 only) support DWDM tunable 10G 
SFP+ modules. 
ETX-2i-100G/QSFP28 support DWDM tunable QSFP28 modules. 
• 
Applicable for 10GbE SFPP ports only (not for native copper ports) 
• 
Band C, 50GHz or 100GHz channel spacing 
The device identifies the SFPP type (50G or 100G) and allows configuration of valid frequencies 
accordingly. 
Factory Defaults 
By default, the non-management Ethernet ports have the following configuration. 
Parameter 
Description 
Default Value 
auto-negotiation 
Enable or disable auto-negotiation 
Note: Not relevant to 10GbE and 
100GbE interfaces. 
auto-negotiation 
classification-key 
Classification key 
legacy 
dhcp-trust 
Trust server DHCP packets 
no dhcp-trust  
(i.e. trust client DHCP packets) 
dwdm-frequency 
Tune SFPP frequency (GHz). 
193100 
Relevant for 10G SFPP ports and 100G 
QSFP28 
efm 
Enable or disable OAM EFM  
no efm 
egress-mtu 
Packet size 
1790 
fat-pipe-detection 
Bind a Fat pipe detection profile to 
a port. 
Note: Relevant to ETX-2i-10G half 
19-inch, ETX-2i-10G-B (full and half 
19-inch), ETX-2i-10G-B/8SFPP (full 
and half 19-inch models) ports 1 to 
4, and ETX-2i-100G/4Q. 
no fat-pipe-detection 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
Default Value 
fec 
Invoke Forward Error Correction 
(FEC) for SFP28 and QSFP28 
Relevant for ETX-2i-100G/4Q SFP28 
and QSFP28 ports only 
fec auto 
functional-mode 
Functional mode 
user – default for ETX-2i port 0/2, 
ETX-2i-B port 2, ETX-2i-10G-B/8SFPP 
ports 2-4, and ETX-2i-100G/4SFPP ports 
2/1 and 2/2. 
network – default for ETX-2i-
100G/4SFPP port 3/2 and all other 
relevant ports. 
l2cp profile 
L2CP profile 
“L2cpDefaultProfile”           
l2pt-network 
L2PT network functionality 
no l2pt-network           
lldp 
802.1-management-vlan-id 
LLDP: no transmission of IEEE 802.1 
management VLAN ID 
no 802.1-management-vlan-id 
lldp customer-bridge-mode 
LLDP: no customer bridge mode 
no customer-bridge-mode 
lldp nearest-bridge-mode 
LLDP: no nearest bridge mode 
no nearest-bridge-mode         
lldp non-tpmr-bridge-mode 
LLDP: no non-TPMR bridge mode 
no non-tpmr-bridge-mode 
max-capability 
Maximum advertised capability 
Note: Not relevant to 10GbE and 
100GbE ports 
1000-full-duplex 
max-ql  
Maximum quality level of clock 
source 
eprtc               
Name 
Port name 
“ETH-[<slot>/] 
<port-number>”      
Policer 
Policer profile 
no policer 
queue-group  
Queue group profile 
“DefaultQueueGroup”    
shutdown 
Administrative status 
no shutdown           
silent-start 
Silent start functionality 
Note: Not relevant to 100GbE ports 
no silent-start         
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
Default Value 
speed-duplex 
Data rate and duplex mode 
For 1G port: 1000-x-full-duplex 
For SFP+ port: 10g-r 
For 25GbE port: 25g-r 
For 40GbE port: 40g-r 
Note: Not relevant to 100GbE ports 
tag-ethernet-type 
Ethernet tag protocol identifier 
0x8100 
tx-ssm 
Transmit SSM 
Note: Not relevant to 100GbE ports 
no tx-ssm 
Configuring Ethernet Port Parameters 
Note 
If a smart SFP has been provisioned, the Ethernet port parameters are not 
accessible for configuration.  
 To configure the Ethernet port parameters: 
1. Navigate to configure port ethernet [<slot>/] <port-num> to select the Ethernet port to 
configure. 
The config>port>eth([<slot>/] <port-num>)# prompt is displayed. 
Note 
The only parameter that can be configured for the management Ethernet port 
is PM collection. To configure the management Ethernet port, navigate to 
configure port mng-ethernet.  
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Enabling auto-negotiation for GbE 
port 
auto-negotiation 
Auto-negotiation is supported on 
1G interfaces only. 
Entering no auto-negotiation 
disables auto-negotiation. 
auto-negotiation can be enabled 
only if silent-start is disabled 
(sanity check). 
Note: Auto-negotiation can be 
enabled on SFP+ ports with speed-
duplex configured to 1G; not 
applicable for SFP+ ports with 
speed-duplex configured to 10G 
(10g-r) (ETX-2i-10G, ETX-2i-10G-B,  
ETX-2i-100G). It is also not 
applicable to ETX-2i-100G QSFP28 
(100G), QSFPP (40G), and SFP28 
(25G) ports.  
Specifying classification key per 
port 
classification-key [legacy] [vlan] 
[inner-vlan] 
legacy – No classification key is 
used. 
vlan – classification key according 
to VLAN 
inner-vlan – classification key 
according to VLAN + Inner VLAN 
Valid for flow classifier only. 
You can change the port 
classification key only if all flows 
using this port are administratively 
disabled.  
Refer to the relevant table in 
Classification Keys in the Traffic 
Processing chapter to see the 
queue/priority mapping methods 
for the selected classification key, 
as well as the flows / flow 
parameters that can be configured 
for the key.  
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Configuring port classification 
[no] classifier 
Refer to Configuring Port 
Classification in the Traffic 
Processing chapter. 
Not relevant for ETX-2i-100G, as it 
does not support port 
classification. 
Clearing OAM EFM statistics 
clear-efm-statistics 
 
Clearing L2CP statistics 
clear-l2cp-statistics 
See Clearing Statistics. 
Clearing all port statistics 
clear-statistics 
See Clearing Statistics. 
Configuring port to trust DHCP 
packets sent from server 
[no] dhcp-trust 
Client ports must always be 
untrusted (no dhcp-trust); 
otherwise, the DHCP relay discards 
the discovery messages sent from 
the client port to the server. 
Relevant only if DHCP snooping is 
enabled. 
Configuring 802.1x port access 
control 
dot1x 
See Configuring Ethernet Port 
Access via 802.1x for more details. 
Enabling/disabling self-tuning 
[no] self-tuning 
When enabled, the QSFP28 on 
both ends of the link negotiate and 
agree on the wavelength to be 
used. 
Configuring DWDM frequency of 
tunable SFPP 
dwdm-frequency <frequency> 
Relevant for 10G SFPP ports  
and 100G QSFP28 
frequency – tunable SFPP 
frequency (GHz) 
Possible values:  
191600-195900 GHz, 
in steps of 50/100 GHz for 
50G/100G channel spacing SFPPs 
respectively. 
Default: 193100 GHz 
The SFPP frequencies translate to 
the wavelengths listed below: 
195900GHz  1530.33nm 
191600GHz  1564.67nm 
193100GHz  1552.52nm (default) 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Configuring OAM EFM descriptor 
[no] efm descriptor 
<efm-descriptor-index> 
Refer to OAM EFM in the 
Monitoring and Diagnostics 
chapter. 
Setting maximum frame size to 
transmit. Frames above the 
specified size are discarded. 
egress-mtu < max-frame-size > 
max-frame-size – maximum size of 
transmitted frames 
Possible values: 64-12288 bytes 
Binding a Fat pipe detection profile 
to a port 
fat-pipe-detection profile <profile-
name> 
profile-name – name of a 
predefined Fat pipe detection 
profile (only one can be defined in 
the system - refer to Configuring 
Fat Pipe Detection in the Traffic 
Processing chapter) 
Enter no fat-pipe-detection to 
unbind the Fat pipe detection 
profile from the port. 
Note: Relevant for ETX-2i-10G half 
19-inch, ETX-2i-10G-B (full and half 
19-inch), ETX-2i-10G-B/8SFPP ports 
1 to 4, as well as for ETX-2i-
100G/4Q user ports. See the 
second table in Applicability and 
Scaling for relevance of Fat pipe 
features for each device. 
Invoking Forward Error Correction 
(FEC)  
fec {auto | off | on} 
Relevant for ETX-2i-100G/4Q, and  
ETX-2i-100G/40G SFP28 and 
QSFP28 ports only. 
You can set FEC to one of the 
following operating modes: 
off – disables FEC  
on – enables FEC 
auto – FEC is enabled automatically 
as specified and explained below. 
Note: When installing an SFP28 or 
QSFP28, certain installation 
conditions such as long fiber lines 
or an attenuating environment may 
require you to set fec to on. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Defining the FEC automation policy 
auto-fec-policy {mm-on | lr-sr-off} 
• mm-on (default): The FEC mode 
is always enabled for Multi 
mode. This applies to the 
100GBASE-SR4 and the 
25GBASE-SR transceivers. 
• lr-sr-off: The FEC mode is 
disabled for 100GBASE-SR4, 
100GBASE-LR4, 100GBASE-LR1 
(25GBASE-SR and the 25GBASE-
LR) transceivers. The FEC mode 
is enabled for 100GBase-ER and 
100GBase-ZR transceivers. 
Setting port to function as network 
or user  
functional-mode {network | user} 
Relevant to the following Ethernet 
ports: 
• ETX-2i, ETX-2i-B, ETX-2i-10G – 
port 0/2 
• ETX-2i-10G-B/8SFPP – ports 
0/2, 0/3, and 0/4 
• ETX-2i-100G/4Q – ports 3/2 
(100G) (default: network), 2/1 
and 2/2 (1/10G) (default: user) 
• ETX-2i-100G/40G – ports 
3/1,3/2 (40G) (default: 
network), 3/3, 3/4 (100G) 
(default: user) 
See Setting Functional Mode to 
Network or User Port for further 
information. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Associating a Layer-2 control 
processing profile with the port 
l2cp profile <l2cp-profile-name> 
Be sure to assign the same L2CP 
profile to both network ports. 
The associated L2CP profile must 
specify peer action for MAC 0x02 in 
the following cases: 
• The port needs to receive clock 
signals (i.e., is defined as clock 
source). 
• LACP (LAG) is enabled for the 
port. 
• Link OAM (EFM) is enabled for 
port. 
 
For an explanation on how to 
configure an L2CP profile, refer to 
Layer-2 Control Protocol (L2CP) 
Processing in the Traffic Processing 
chapter. 
Configuring user port with L2PT 
network functionality 
l2pt-network 
Configurable for user ports only. 
Enter no l2pt-network to disable 
user port from functioning as L2PT 
network port. 
Configuring LLDP parameters 
lldp 
Refer to Link Layer Discovery 
Protocol (LLDP) in the Traffic 
Processing chapter for details. 
Executing a loopback test 
[no] loopback {local | remote} 
[duration <seconds>] 
See Testing Ethernet Ports. 
Setting maximum advertised 
capability (highest traffic handling 
capability to be advertised during 
the auto-negotiation process) for 
FE/GbE port if auto-negotiation is 
enabled 
max-capability {10-full-duplex | 
100-full-duplex | 1000-full-duplex | 
1000-x-full-duplex } [{sfp | rj45}] 
Relevant for ETX-2i-100G/40G, and 
ETX-2i-100G/4Q SFP+ (1/10 GbE) 
ports that are set to 1GbE. 
Relevant for ETX-2i-10G/8SFPP, 
ETX-2i-10G-B/8SFPP in case of 
copper-SFP to select max-capability 
100 or 1000 Mbps. 
Relevant for auto-negotiation 
enabled.  
10-full-duplex – 10BASE-T full 
duplex 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
100-full-duplex – 100BASE-T full 
duplex 
1000-full-duplex – 1000BASE-T full 
duplex 
1000-x-full-duplex – 1000BASE-X, 
1000BASE-LX, 1000BASE-SX, or  
1000BASE-CX full duplex 
Note:  
• The values 1000-full-duplex 
and 1000-x-full-duplex are 
relevant only for GbE ports. 
• Use sfp or rj45 for combo ports 
to configure different values for 
the SFP and RJ-45 modes. If 
neither sfp nor rj45 is 
specified, the command applies 
to both modes. The device 
works with the values that 
apply according to whether an 
SFP is inserted. 
• Maximum advertised capability 
for combo fiber optic ports is 
permanently set to 1000-x-full 
duplex. 
Defining maximum quality level of 
clock source, if SyncE is transmitted 
over the port 
max-ql { eprtc | prtc | prc | ssu-a | 
ssu-b | eec | sec | dnu | ssm-based 
| prs | stu | st2 | tnc | st3e | st3 | 
smc | st4 | dus | prov | unk } 
Not relevant for ETX-2i-10G-
B/8SFPP. 
The quality level of the SyncE 
transmitted over this port is the 
minimum of the quality level set by 
this command, and the system 
quality level set by clock selection. 
Possible values are: 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
eprtc –  Enhanced Primary 
Reference Time Clock 
prtc – Primary Reference Time 
Clock 
prc – Primary Reference Clock 
ssu-a – Types I or V slave clock that 
is defined in Recommendation 
G.812 
ssu-b – Type VI slave clock that is 
defined in Recommendation G.812. 
eeec – Synchronous Equipment 
Clock 
sec – Synchronous Equipment 
Clock 
dnu – This signal should not be 
used for synchronization 
ssm-based – QL is received via 
Synchronous Status Messages 
prs – PRS traceable 
(Recommendation G.811). 
stu – Synchronized   Traceability 
Unknown 
st2 – Traceable to Stratum 2 
(Recommendation G.812, Type II). 
tnc – Traceable to Transit Node 
Clock (Recommendation G.812, 
Type V). 
st3e – Traceable to Stratum 3E 
(Recommendation G.812, Type III). 
st3 – Traceable to Stratum 3 
(Recommendation G.812, Type IV). 
smc – Traceable to SONET Clock 
Self Timed 
st4 – Traceable to Stratum 4 
Freerun 
dus – This signal should not be 
used for synchronization 
prov – Provisionable by the 
Network Operator 
unk – Unknown clock source 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Note: Refer to the Clock Selection 
section in the Timing and 
Synchronization chapter for further 
explanation of the quality levels. 
Configuring a BUM Policer that is 
composed of several separate BW 
profiles 
multi-policer {traffic-type}  
<profile-name> 
no multi-policer  {traffic-type} 
traffic-type – type of traffic that 
the Policer is to be applied to 
Possible values: broadcast, 
multicast, unknown-unicast. 
profile-name – name of an existing 
BW profile. 
Note: 
• This command is available only 
if no policer is configured for 
this port (see below). 
• This command can be invoked 
multiple (up to three) times 
with different traffic types. 
• The traffic type specified in the 
command must match the type 
specified in the profile. 
Selecting a traffic type, which is 
already associated to the port, 
replaces the existing Policer values 
(for this traffic type) with the 
values of the new BW profile. 
Assigning description to port 
name <string> 
no name 
Entering no name removes the 
name. 
Configuring collection of 
performance management 
statistics for the port, that are 
presented via the RADview 
Performance Management portal 
pm-collection interval <seconds> 
no pm-collection 
Note: You can enable PM statistics 
collection for all Ethernet ports 
rather than enabling it for 
individual ports. In addition to 
enabling PM statistics collection for 
the ports, it must be enabled for 
the device. Refer to the 
Performance Management section 
in the Monitoring and Diagnostics 
chapter for details. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Associating a Policer profile for 
broadcast/multicast traffic with the 
port 
policer profile 
<policer-profile-name> 
no policer 
Entering no policer removes any 
Policer profile from the port. 
Note:  
This command is available only if 
there are no multi-policers 
associated with the port. (no multi-
policer <traffic-type> for each 
Policer profile.) 
Associating a queue group profile 
with the port 
[no] queue-group profile 
<queue-group-profile-name> 
 
Measuring port data rate and line 
rate 
[no] rate-measure interval 
<seconds> 
Possible values: 10–300  
See Viewing Ethernet Port Data 
Rate and Line Rate for details. 
Releasing all Fat pipe flows 
release-fat-pipe {all | profile  
<fat-pipe-profile-name>} 
Relevant for ETX-2i-10G half 19-
inch,  
ETX-2i-10G-B (full and half 19-inch),  
ETX-2i-10G-B/8SFPP ports 1 to 4 , 
as well as for ETX-2i-100G/4Q and 
ETX-2i-100G/40G user ports. 
Clears all flows caught by a prior 
Fat pipe command, as well as all 
invoked Policer allocations and the 
list of active Fat pipes. All the 
cleared results enter the Fat pipe 
history. 
Note: Currently there is one active 
Fat pipe profile in the system, and 
therefore both options (all and 
selecting a specific profile) delete 
the same flows. 
Enabling/disabling Silent Start 
[no] silent-start 
This parameter is visible for optical 
ports only. 
Note: 
• silent-start can be configured 
only if auto-negotiation is 
disabled (no auto-negotiation). 
• When Silent Start is enabled, 
1:1 Protection does not work.  
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
• Silent Start is not relevant for 
100Gbps ports. 
Setting data rate and duplex mode 
speed-duplex {auto | 10g-r | 25g-r}  
{10 full duplex | 100 full duplex | 
1000 full duplex | 1000 x full 
duplex | multirate-100fx | 
multirate-1000fx } [{sfp | rj45}] 
Supported for ETX-2i-10G and  
ETX-2i-100G SFPP, SFP28, QSFPP, 
and QSFP28 ports. 
auto – Speed & duplex mode is set 
automatically, according to SFP 
type inserted (1/10/25G) 
Relevant for SFP+ and SFP28 ports  
10 g-r – Sets SFP+ port speed to 
10GbE (relevant for SFP+ ports that 
are 1GbE capable). 
25g-r – Sets SFP28 port speed to 
25GbE 
10-full-duplex – 10BASE-T full 
duplex  
100-full-duplex – 100BASE-T full 
duplex 
1000-full-duplex – 1000BASE-T full 
duplex 
1000-x-full-duplex – 1000BASE-X, 
1000BASE-LX, 1000BASE-SX, or  
1000BASE-CX full duplex 
multirate-100fx – multirate 100 
BASE-FX; for SFP ports only. 
Selecting this value forces the SFP 
speed to 100 Mbps. 
multirate-1000fx – multirate 1000 
BASE-FX; for SFP ports. Selecting 
this value forces the SFP speed to 
1000 Mbps. 
Note:  
• Speed-duplex is not applicable 
to 100G and 40G ports, which 
are always 100G or 40G, 
respectively. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
• Auto-negotiation is not 
applicable for SFP+ ports with 
speed-duplex configured to 
10g-r. Nor is it applicable to 
SFP28, QSFP+, or QSFP28 ports. 
• Upgrading or downgrading an 
SFP+ port between 1GbE and 
10GbE returns the port 
configuration to its default 
values. 
• The values 10-full-duplex, 
100-full-duplex, 
1000-full-duplex, and 
1000-x-full-duplex are relevant 
only when auto negotiation is 
disabled; multirate-100fx and 
multirate-1000fx are relevant 
for both auto-negotiation 
enabled and disabled. 
• The values 1000-full-duplex 
and 1000-x-full-duplex are 
relevant only for GbE ports; not 
for FE ports. 
• The values multirate-100fx and 
multirate-1000fx are relevant 
only for dual-rate SFP 
(100/1000) 
• Use sfp or rj45 for combo ports 
to configure different values for 
the SFP and RJ-45 modes. If 
neither sfp nor rj45 is 
specified, the command applies 
to both modes. The device 
works with the values that 
apply according to whether an 
SFP is inserted. 
• Speed/duplex for combo fiber 
optic ports is permanently set 
to 1000-x-full duplex. 
• It is not possible to downgrade 
SFP+ ports that are set to 
10Gby the ordering option- 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Setting the VLAN tagged frame 
ETH II frame EtherType (tag 
protocol identifier) 
tag-ethernet-type 
<0x0000-0xFFFF> 
Port EtherType can be set to one of 
the following values: 
0x8100 (default) 
0x88a8  
A user-configured global EtherType   
(provided it has been defined at 
the device (chassis) level) 
Note:  
• If you do not configure an 
EtherType for the port, the port 
uses the default setting (8100). 
• You cannot change the 
EtherType tag if the port 
(Ethernet or LAG) has flows 
attached to it. 
Enabling transmitting of clock 
availability and quality via SSM 
[no] tx-ssm 
You should enable this for Ethernet 
ports that transmit clock signals. 
The MAC address of the 
transmitting port is used in the 
SSM message. 
Entering no tx-ssm disables 
sending SSM messages. 
Relevant for ETX-2i, ETX-2i-B, and 
ETX-2i-10G with timing options. 
Not relevant for ETX-2i-100G. 
Displaying information on active 
and history (closed) Fat pipes 
show fat-pipe-list { active | history 
| all } 
all option shows both Active and 
History entries. 
See Viewing Fat Pipe Information. 
Relevant for ETX-2i-10G half 19-
inch, 
ETX-2i-10G-B (full and half 19-inch),  
ETX-2i-10G-B/8SFPP (full and half 
19-inch models) ports 1 to 4, and   
ETX-2i-100G/4Q user ports.  
Displaying L2CP statistics 
show l2cp-statistics 
See Viewing Layer-2 Control 
Processing (L2CP) Statistics. 
Displaying loopback test status 
show loopback 
 
Displaying OAM EFM status 
show oam-efm 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Displaying OAM EFM statistics 
show oam-efm-statistics 
 
Displaying measured port data rate 
and line rate 
show rate 
See Viewing Ethernet Port Data 
Rate and Line Rate for details. 
Displaying  
show sfp-extended-information 
See Viewing SFP Extended 
Information. 
Displaying the port statistics 
show statistics 
See Viewing Ethernet Port 
Statistics. 
Displaying the port status 
show status 
See Viewing Ethernet Port Status. 
Administratively enabling port 
no shutdown 
Entering shutdown disables the 
port. 
Enabling auto-negotiation for GbE 
port 
auto-negotiation 
Auto-negotiation is supported on 
1G interfaces only. 
Entering no auto-negotiation 
disables auto-negotiation. 
auto-negotiation can be enabled 
only if silent-start is disabled 
(sanity check). 
Note: Auto-negotiation can be 
enabled on SFP+ ports with speed-
duplex configured to 1G; not 
applicable for SFP+ ports with 
speed-duplex configured to 10G 
(10g-r) (ETX-2i-10G, ETX-2i-10G-B,  
ETX-2i-100G). It is also not 
applicable to ETX-2i-100G QSFP28 
(100G), QSFPP (40G), and SFP28 
(25G) ports.  
 
Specifying classification key per 
port 
classification-key [legacy] [vlan] 
[inner-vlan] 
legacy – No classification key is 
used. 
vlan – classification key according 
to VLAN 
inner-vlan – classification key 
according to VLAN + Inner VLAN 
Valid for flow classifier only. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
You can change the port 
classification key only if all flows 
using this port are administratively 
disabled.  
Refer to the relevant table in 
Classification Keys in the Traffic 
Processing chapter to see the 
queue/priority mapping methods 
for the selected classification key, 
as well as the flows / flow 
parameters that can be configured 
for the key.  
Configuring port classification 
[no] classifier 
Refer to Configuring Port 
Classification in the Traffic 
Processing chapter. 
Note: Not relevant for ETX-2i-
100G, as it does not support port 
classification. 
Clearing OAM EFM statistics 
clear-efm-statistics 
 
Clearing L2CP statistics 
clear-l2cp-statistics 
See Clearing Statistics. 
Clearing all port statistics 
clear-statistics 
See Clearing Statistics. 
Configuring port to trust DHCP 
packets sent from server 
[no] dhcp-trust 
Client ports must always be 
untrusted (no dhcp-trust); 
otherwise, the DHCP relay discards 
the discovery messages sent from 
the client port to the server. 
Note: Relevant only if DHCP 
snooping is enabled. 
Configuring 802.1x port access 
control 
dot1x 
See Configuring Ethernet Port 
Access via 802.1x for more details. 
Configuring DWDM frequency of 
tunable SFPP 
dwdm-frequency <frequency> 
Relevant for 10G SFPP ports  
and 100G QSFP28 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
frequency – tunable SFPP 
frequency (GHz) 
Possible values: 191600-195900 
GHz 
For 50G/100G channel spacing 
SFPP, in steps of 50/100 GHz 
respectively. 
195900GHz  1530.33nm 
191600GHz  1564.67nm 
Configuring OAM EFM descriptor 
[no] efm descriptor 
<efm-descriptor-index> 
Refer to OAM EFM in the 
Monitoring and Diagnostics 
chapter. 
Setting maximum frame size (in 
bytes) to transmit (frames above 
the specified size are discarded) 
egress-mtu < max-frame-size > 
max-frame-size – maximum size of 
transmitted frames 
Possible values: 64-12288 bytes 
Binding a Fat pipe detection profile 
to a port 
fat-pipe-detection profile <profile-
name> 
profile-name – name of a 
predefined Fat pipe detection 
profile (only one can be defined in 
the system - refer to Configuring 
Fat Pipe Detection in the Traffic 
Processing chapter) 
Enter no fat-pipe-detection to 
unbind the Fat pipe detection 
profile from the port. 
Note: Relevant for ETX-2i-10G half 
19-inch, ETX-2i-10G-B (full and half 
19-inch), ETX-2i-10G-B/8SFPP ports 
1 to 4, as well as for ETX-2i-
100G/4Q user ports. See the 
second table in Applicability and 
Scaling for relevance of Fat pipe 
features for each device. 
Invoking Forward Error Correction 
(FEC)  
fec {auto | off | on} 
Relevant for ETX-2i-100G/4Q, and  
ETX-2i-100G/40G SFP28 and 
QSFP28 ports only. 
You can set FEC to one of the 
following operating modes: 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
auto – If QSFP operates in 
multimode, enables FEC (on); 
otherwise disables FEC (off). 
off – disables FEC  
on – enables FEC 
Note: When installing an SFP28 or 
QSFP28, certain installation 
conditions such as long fiber lines 
or an attenuating environment 
may require you to set fec to on. 
Setting port to function as network 
or user  
functional-mode {network | user} 
Relevant to the following Ethernet 
ports: 
• ETX-2i, ETX-2i-B, ETX-2i-10G – 
port 0/2 
• ETX-2i-10G-B/8SFPP – ports 
0/2, 0/3, and 0/4 
• ETX-2i-100G/4Q – ports 3/2 
(100G) (default: network), 2/1 
and 2/2 (1/10G) (default: user) 
• ETX-2i-100G/40G – ports 
3/1,3/2 (40G) (default: 
network), 3/3, 3/4 (100G) 
(default: user) 
See Setting Functional Mode to 
Network or User Port for further 
information. 
Associating a Layer-2 control 
processing profile with the port 
l2cp profile <l2cp-profile-name> 
Be sure to assign the same L2CP 
profile to both network ports. 
The associated L2CP profile must 
specify peer action for MAC 0x02 in 
the following cases: 
• The port needs to receive clock 
signals (i.e., is defined as clock 
source). 
• LACP (LAG) is enabled for the 
port. 
• Link OAM (EFM) is enabled for 
port. 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
For an explanation on how to 
configure an L2CP profile, refer to 
Layer-2 Control Protocol (L2CP) 
Processing in the Traffic Processing 
chapter. 
Configuring user port with L2PT 
network functionality 
l2pt-network 
Configurable for user ports only. 
Enter no l2pt-network to disable 
user port from functioning as L2PT 
network port. 
Configuring LLDP parameters 
lldp 
Refer to Link Layer Discovery 
Protocol (LLDP) in the Traffic 
Processing chapter for details. 
Executing a loopback test 
[no] loopback {local | remote} 
[duration <seconds>] 
See Testing Ethernet Ports. 
Setting maximum advertised 
capability (highest traffic handling 
capability to be advertised during 
the auto-negotiation process) for 
FE/GbE port if auto-negotiation is 
enabled 
max-capability {10-full-duplex | 
100-full-duplex | 1000-full-duplex | 
1000-x-full-duplex } [{sfp | rj45}] 
Relevant for ETX-2i-100G/40G, and 
ETX-2i-100G/4Q SFP+ (1/10 GbE) 
ports that are set to 1GbE. 
Relevant for ETX-2i-10G/8SFPP, 
ETX-2i-10G-B/8SFPP in case of 
copper-SFP to select max-capability 
100 or 1000 Mbps. 
Relevant for auto-negotiation 
enabled.  
10-full-duplex – 10BASE-T full 
duplex 
100-full-duplex – 100BASE-T full 
duplex 
1000-full-duplex – 1000BASE-T full 
duplex 
1000-x-full-duplex – 1000BASE-X, 
1000BASE-LX, 1000BASE-SX, or  
1000BASE-CX full duplex 
Note: 
• The values 1000-full-duplex 
and 1000-x-full-duplex are 
relevant only for GbE ports. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
• Use sfp or rj45 for combo ports 
to configure different values for 
the SFP and RJ-45 modes. If 
neither sfp nor rj45 is 
specified, the command applies 
to both modes. The device 
works with the values that 
apply according to whether an 
SFP is inserted. 
• Maximum advertised capability 
for combo fiber optic ports is 
permanently set to 1000-x-full 
duplex. 
 
Defining maximum quality level of 
clock source, if SyncE is 
transmitted over the port 
max-ql { eprtc | prtc | prc | ssu-a | 
ssu-b | eec | sec | dnu | ssm-based 
| prs | stu | st2 | tnc | st3e | st3 | 
smc | st4 | dus | prov | unk } 
Not relevant for ETX-2i-10G-
B/8SFPP. 
The quality level of the SyncE 
transmitted over this port is the 
minimum of the quality level set by 
this command, and the system 
quality level set by clock selection. 
Possible values are: 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
eprtc –  Enhanced Primary 
Reference Time Clock 
prtc – Primary Reference Time 
Clock 
prc – Primary Reference Clock 
ssu-a – Types I or V slave clock that 
is defined in Recommendation 
G.812 
ssu-b – Type VI slave clock that is 
defined in Recommendation G.812. 
eeec – Synchronous Equipment 
Clock 
sec – Synchronous Equipment 
Clock 
dnu – This signal should not be 
used for synchronization 
ssm-based – QL is received via 
Synchronous Status Messages 
prs – PRS traceable 
(Recommendation G.811). 
stu – Synchronized   Traceability 
Unknown 
st2 – Traceable to Stratum 2 
(Recommendation G.812, Type II). 
tnc – Traceable to Transit Node 
Clock (Recommendation G.812, 
Type V). 
st3e – Traceable to Stratum 3E 
(Recommendation G.812, Type III). 
st3 – Traceable to Stratum 3 
(Recommendation G.812, Type IV). 
smc – Traceable to SONET Clock 
Self Timed 
st4 – Traceable to Stratum 4 
Freerun 
dus – This signal should not be 
used for synchronization 
prov – Provisionable by the 
Network Operator 
unk – Unknown clock source 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Note: Refer to the Clock Selection 
section in the Timing and 
Synchronization chapter for further 
explanation of the quality levels. 
Configuring a BUM Policer that is 
composed of several separate BW 
profiles 
multi-policer {traffic-type}  
<profile-name> 
no multi-policer  {traffic-type} 
traffic-type – type of traffic that 
the Policer is to be applied to 
Possible values: broadcast, 
multicast, unknown-unicast  
profile-name – name of an existing 
BW profile 
Note: 
• This command is available only 
if no policer is configured for 
this port (see below). 
• This command can be invoked 
multiple (up to three) times 
with different traffic types. 
• The traffic type specified in the 
command must match the type 
specified in the profile. 
• Selecting a traffic type, which is 
already associated to the port, 
replaces the existing Policer 
values (for this traffic type) 
with the values of the new BW 
profile. 
Assigning description to port 
name <string> 
no name 
Entering no name removes the 
name. 
Configuring collection of 
performance management 
statistics for the port, that are 
presented via the RADview 
Performance Management portal 
pm-collection interval <seconds> 
no pm-collection 
Note: You can enable PM statistics 
collection for all Ethernet ports 
rather than enabling it for 
individual ports. In addition to 
enabling PM statistics collection for 
the ports, it must be enabled for 
the device. Refer to the 
Performance Management section 
in the Monitoring and Diagnostics 
chapter for details. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Associating a Policer profile for 
broadcast/multicast traffic with the 
port 
policer profile 
<policer-profile-name> 
no policer 
Entering no policer removes any 
Policer profile from the port. 
Note:  
• This command is available only 
if there are no multi-policers 
associated with the port. (no 
multi-policer <traffic-type> for 
each Policer profile.) 
Associating a queue group profile 
with the port 
[no] queue-group profile 
<queue-group-profile-name> 
 
Measuring port data rate and line 
rate 
[no] rate-measure interval 
<seconds> 
Possible values: 10–300  
See Viewing Ethernet Port Data 
Rate and Line Rate for details. 
Releasing all Fat pipe flows 
release-fat-pipe {all | profile  
<fat-pipe-profile-name>} 
Relevant for ETX-2i-10G half 19-
inch,  
ETX-2i-10G-B (full and half 19-
inch),  
ETX-2i-10G-B/8SFPP ports 1 to 4 , 
as well as for ETX-2i-100G/4Q and 
ETX-2i-100G/40G user ports. 
Clears all flows caught by a prior 
Fat pipe command, as well as all 
invoked Policer allocations and the 
list of active Fat pipes. All the 
cleared results enter the Fat pipe 
history. 
Note: Currently there is one active 
Fat pipe profile in the system, and 
therefore both options (all and 
selecting a specific profile) delete 
the same flows. 
Enabling/disabling Silent Start 
[no] silent-start 
This parameter is visible for optical 
ports only. 
Note: 
• silent-start can be configured 
only if auto-negotiation is 
disabled (no auto-negotiation). 
• When Silent Start is enabled, 
1:1 Protection does not work. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
• Silent Start is not relevant for 
100Gbps ports. 
Setting data rate and duplex mode 
speed-duplex {auto | 10g-r | 
25g-r}  {10 full duplex | 100 full 
duplex | 1000 full duplex | 1000 x 
full duplex | multirate-100fx | 
multirate-1000fx }  [{sfp | rj45}] 
Supported for ETX-2i-10G and  
ETX-2i-100G SFPP, SFP28, QSFPP, 
and QSFP28 ports 
auto – Speed & duplex mode is set 
automatically, according to SFP 
type inserted (1/10/25G) 
Relevant for SFP+ and SFP28 ports  
10 g-r – Sets SFP+ port speed to 
10GbE (relevant for SFP+ ports that 
are 1GbE capable). 
25g-r – Sets SFP28 port speed to 
25GbE 
10-full-duplex – 10BASE-T full 
duplex  
100-full-duplex – 100BASE-T full 
duplex 
1000-full-duplex – 1000BASE-T full 
duplex 
1000-x-full-duplex – 1000BASE-X, 
1000BASE-LX, 1000BASE-SX, or  
1000BASE-CX full duplex 
multirate-100fx – multirate 100 
BASE-FX; for SFP ports only. 
Selecting this value forces the SFP 
speed to 100 Mbps. 
multirate-1000fx – multirate 1000 
BASE-FX; for SFP ports. Selecting 
this value forces the SFP speed to 
1000 Mbps. 
Note:  
• Speed-duplex is not applicable 
to 100G and 40G ports, which 
are always 100G or 40G, 
respectively. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
• Auto-negotiation is not 
applicable for SFP+ ports with 
speed-duplex configured to 
10g-r. Nor is it applicable to 
SFP28, QSFP+, or QSFP28 ports. 
• Upgrading or downgrading an 
SFP+ port between 1GbE and 
10GbE returns the port 
configuration to its default 
values. 
• The values 10-full-duplex, 
100-full-duplex, 
1000-full-duplex, and 
1000-x-full-duplex are relevant 
only when auto negotiation is 
disabled; multirate-100fx and 
multirate-1000fx are relevant 
for both auto-negotiation 
enabled and disabled. 
• The values 1000-full-duplex 
and 1000-x-full-duplex are 
relevant only for GbE ports; not 
for FE ports. 
• The values multirate-100fx and 
multirate-1000fx are relevant 
only for dual-rate SFP 
(100/1000) 
• Use sfp or rj45 for combo ports 
to configure different values for 
the SFP and RJ-45 modes. If 
neither sfp nor rj45 is 
specified, the command applies 
to both modes. The device 
works with the values that 
apply according to whether an 
SFP is inserted. 
• Speed/duplex for combo fiber 
optic ports is permanently set 
to 1000-x-full duplex. 
• It is not possible to downgrade 
SFP+ ports that are set to 10G 
by the ordering option. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Setting the VLAN tagged frame 
ETH II frame EtherType (tag 
protocol identifier) 
tag-ethernet-type 
<0x0000-0xFFFF> 
Port EtherType can be set to one of 
the following values: 
0x8100 (default) 
0x88a8  
A user-configured global EtherType   
(provided it has been defined at 
the device (chassis) level) 
Note:  
• If you do not configure an 
EtherType for the port, the port 
uses the default setting (8100). 
• You cannot change the 
EtherType tag if the port 
(Ethernet or LAG) has flows 
attached to it. 
Enabling transmitting of clock 
availability and quality via SSM 
[no] tx-ssm 
You should enable this for Ethernet 
ports that transmit clock signals. 
The MAC address of the 
transmitting port is used in the 
SSM message. 
Entering no tx-ssm disables 
sending SSM messages. 
Relevant for ETX-2i, ETX-2i-B, and 
ETX-2i-10G with timing options. 
Not relevant for ETX-2i-100G. 
Displaying information on active 
and history (closed) Fat pipes 
show fat-pipe-list { active | history 
| all } 
all option shows both Active and 
History entries. 
See Viewing Fat Pipe Information. 
Note: Relevant for ETX-2i-10G half 
19-inch, 
ETX-2i-10G-B (full and half 19-
inch),  
ETX-2i-10G-B/8SFPP (full and half 
19-inch models) ports 1 to 4, and   
ETX-2i-100G/4Q user ports.  
Displaying L2CP statistics 
show l2cp-statistics 
See Viewing Layer-2 Control 
Processing (L2CP) Statistics. 
Displaying loopback test status 
show loopback 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Displaying OAM EFM status 
show oam-efm 
 
Displaying OAM EFM statistics 
show oam-efm-statistics 
 
Displaying measured port data rate 
and line rate 
show rate 
See Viewing Ethernet Port Data 
Rate and Line Rate for details. 
Displaying  
show sfp-extended-information 
See Viewing SFP Extended 
Information. 
Displaying the port statistics 
show statistics 
See Viewing Ethernet Port 
Statistics. 
Displaying the port status 
show status 
See Viewing Ethernet Port Status. 
Administratively enabling port 
no shutdown 
Entering shutdown disables the 
port. 
Classification Key Priority Map Scheme 
Classification Key 
Queue Mapping Method  
Legacy  (current ‘key’) 
NA 
VLAN  
vlan 
Flow (Fixed) 
DSCP 
P-bit 
VLAN Inner VLAN  
inner-vlan 
Flow (Fixed) 
DSCP 
P-bit 
Configuring Ethernet Port Access via 802.1x 
User and network ports can be authorized to connect to a network via 802.1x authentication. You can 
configure ETX-2i to act as an authenticator. 
Note 
If a Wi-Fi access point has PSK enabled or security set to none, 802.1x cannot 
be used. 
 To configure Ethernet port access control via 802.1x: 
1. Navigate to configure port ethernet dot1x to configure 802.1x settings. 
The config>port>eth>dot1x# prompt is displayed. 
ETX-2i Devices 
2. Cards and Ports 
Note 
The following commands can also be accessed from configure port wlan 
access-point dot1x. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Configuring 802.1x 
authenticator 
authenticator 
See Configuring 802.1x Authenticator 
for more details. 
Clearing 802.1x statistics 
clear-statistics 
 
Initializing 802.1x port access 
control 
initialize 
 
Viewing 802.1x statistics 
show statistics 
See Viewing 802.1x Statistics 
Viewing 802.1x status 
show status 
See Viewing 802.1x Status 
Viewing detailed status of 
802.1x authenticator 
show status details 
See Viewing 802.1x Detailed Status 
Configuring 802.1x Authenticator 
 To configure the 802.1x authenticator: 
1. Navigate to configure port ethernet dot1x authenticator to configure 802.1x authenticator 
settings. 
The config>port>eth>dot1x>authenticator# prompt is displayed. 
Note 
The following commands can also be accessed from configure port wlan 
access-point dot1x. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Configuring authentication 
mode 
authentication mode {multi-
supplicants | port | single-
supplicant} 
multi-supplicants –  
port –  
single-supplicants –  
Note: When using Wi-Fi access 
points, this command is hidden and 
set to multi-supplicants. 
Disabling authenticator 
[no] shutdown 
 
ETX-2i Devices 
2. Cards and Ports 
Viewing 802.1x Statistics 
You can display 802.1x statistics for authenticator and supplicant Ethernet ports.  
 To display 802.1x statistics: 
• 
At the prompt config>port>eth>dot1x#, enter show statistics 
Relevant 802.1x port statistics are displayed. The counters are described in the following table. 
Note 
This output is repeated for each supplicant with an altered heading and 
without Rx Last Frame MAC. 
 
Port EAPOL Frames 
----------------- 
Rx EAP Total          : 200 
Rx Start              : 2 
Rx Logoff             : 1 
Rx Invalid            : 0 
Rx Length Error       : 0 
Rx Last Frame Version : 2 
Rx Last Frame MAC     : 00:11:00:11:00:11 
Tx Start              : 2 
Tx Logoff             : 1 
Tx Authenticator      : 100 
Tx Supplicant         : 50 
 
Parameter 
Description 
Rx EAP Total 
Number of EAPOL-EAP frames received 
Rx Start  
Number of EAPOL-Start frames received 
Rx Logoff 
Number of EAPOL-Logoff frames received 
Rx Invalid 
Number of invalid EAPOL frames received 
Rx Length Error 
Number of EAPOL frames received with wrong length 
Rx Last Frame Version 
Version of last received EAPOL frame 
Rx Last Frame MAC 
Source MAC address of last received EAPOL frame 
Tx Start 
Number of EAPOL-Start frames transmitted 
Tx Logoff 
Number of Tx EAPOL-Logoff frames transmitted 
Tx Authenticator 
Number of EAPOL-EAP frames transmitted by the authenticator 
Tx Supplicant  
Number of EAPOL-EAP frames transmitted by the supplicant 
ETX-2i Devices 
2. Cards and Ports 
Viewing 802.1x Status 
You can display the status of 802.1x ports, including the authenticator and supplicants. 
 To display 802.1x status: 
• 
At the prompt config>port>eth>dot1x#, enter show status 
The 802.1x port access control status parameters are displayed. The parameters are described in 
the table below. 
 
Note 
Wi-Fi access points do not support the supplicant table. 
 
Note 
If no RADIUS server has been configured, the authenticator cannot be 
initialized and therefore the supplicant table will be empty. 
 
Authenticator  
  Administrative State : Enabled 
  Authentication Mode  : Multi Supplicants 
 
  Supplicants 
    Connected          : 3 
    Max Allowed        : 100 
 
  MAC Address        Status 
  ---------------------------------- 
  00:00:00:00:00:00  Authenticated 
  22:22:22:22:22:22  Unauthenticated 
 
Supplicant  
  Administrative State : Enable 
  Operational status   : Authenticated 
 
Parameter 
Description 
authenticator-admin 
Admin status of authenticator 
authentication-mode 
Mode of authentication (multi-supplicant, port, or single-supplicant) 
supplicant-number 
The number of connected supplicants 
supplicant-max 
Maximum number of supplicants allowed on this port 
supp-mac 
MAC address of connected supplicant 
supp-s 
Status of connected supplicant 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
supplicant-admin 
Admin status of supplicant 
supplicant-oper 
Operational status of supplicant 
supplicant-failure 
Reason for supplicant authorization failure, if relevant 
Viewing 802.1x Detailed Status 
You can display the detailed status and statistics of 802.1x ports, including the authenticator and 
supplicants. 
 To display 802.1x status details: 
• 
At the prompt config>port>eth>dot1x#, enter: 
show status details 
The 802.1x status and statistics appear listed. 
Authenticator 
----------------------------------------------------------------------------- 
Administrative State : Enabled 
Authentication Mode : Port 
 
MAC Address Status 
00-04-23-c5-29-16 Authenticated 
 
Port Rx Last Frame Version : 1 
Port Rx Last Frame MAC : 00-04-23-c5-29-16 
 
Port EAPOL Frames 
----------------------------------------------------------------------------- 
Rx EAP Total   
: 23 
Rx Start  
 
: 4 
Rx Logoff  
 
: 0 
Rx Invalid   
: 0 
Rx Length Error  
: 0 
 
Authenticator Frames 
----------------------------------------------------------------------------- 
Tx Authenticator  
: 24 
Request Identity 
: 5 
Request Other  
: 17 
Rx Authenticator  
: 23 
Response Identity  : 2 
Response Other  
: 17 
 
 
 
ETX-2i Devices 
2. Cards and Ports 
Last Session Tx Rx 
----------------------------------------------------------------------------- 
Octets 0 17680 
Frames 0 198 
 
Session Identifier  : 3-20240430114510 
Session Time   
: 217 seconds 
Session User Name  : 00-04-23-c5-29-16 
Termination Cause  : Not Terminated Yet 
 
RADIUS 
----------------------------------------------------------------------------- 
Authentication Server  
 
: 1 (Address = 172.17.232.208) 
Last Authentication Message  
: RADIUS Access Accept 
 
Last Authentication Server Statistics 
----------------------------------------------------------------------------- 
Access Requests  
: 0 
Access Retransmits  : 0 
Access Accepts  
: 0 
Access Rejects  
: 0 
Access Challenges  : 0 
Malformed Response  : 0 
Bad Authenticators  : 0 
Pending Requests  
: 0 
Timeouts  
 
: 0 
Unknown Types  
: 0 
Packets Dropped  
: 0 
Setting Functional Mode to Network or User Port 
You can set the following Ethernet port to function as network or user: 
• 
ETX-2i, ETX-2i-B, ETX-2i-10G: port 0/2 
• 
ETX-2i-10G-B/8SFPP: 10G ports 0/2, 0/3, and 0/4 
• 
ETX-2i-100G/4Q: 
 
100G port 3/2 – default NNI (network) 
 
10G ports 2/1, 2/2 – default UNI (user) 
• 
ETX-2i-100G/40G 
 
40G ports 3/1,3/2 – default NNI (network) 
 
100G ports 3/3, 3/4 – default UNI (user) 
 
ETX-2i Devices 
2. Cards and Ports 
Note 
• 
When you change the functional mode, all flows related to the port are 
deleted. 
• 
The port must be administratively disabled before you can change the 
functional mode. 
• 
Functional mode change is for database setting only. Functionality, such 
as L2PT, is not modified.  
 To change the functional mode of the Ethernet interface: 
1. Navigate to configure port ethernet [<slot>/]<port>. 
The config>port>eth([<slot>/]<port>)# prompt is displayed. 
2. Enter shutdown to administratively disable the port. 
3. Enter the command to change the functional mode: 
 
To change to user port, enter:  
functional-mode user 
 
To change to network port, enter: 
functional-mode network 
The functional mode of the port is changed. 
4. Enter no shutdown to administratively enable the port. 
The example below illustrates the setting. 
exit all 
configure port ethernet 0/2 
shutdown 
functional-mode user 
no shutdown 
save 
Viewing Ethernet Port Status 
You can display the status and configuration of an individual Ethernet port, including SFP information if 
an SFP is inserted. 
 
Note 
The port operational status indicates if the port is down due to fault 
propagation.  
 
 
ETX-2i Devices 
2. Cards and Ports 
If the port participated in a port mirroring session, this fact is indicated in the port status, as follows: 
• 
Specifies whether the port is acting as source or destination for the mirrored traffic.  
• 
Specifies the part of traffic on this port that is mirrored (Rx, Tx, both Rx and Tx), if the port is the 
source of traffic. 
Display of an optical Ethernet port status includes the Silent Start status, provided that Silent Start is 
enabled.  
 To display the status of a specific Ethernet port: 
• 
At the prompt config>port>eth(<port-num>)#, enter: 
show status 
The Ethernet port status parameters are displayed, including SFP information if applicable. The 
parameters are described in the table below. 
Note 
• 
The SFP wavelength values display the exact values from the SFP registers. 
• 
In case of DDM SFP/SFP+/QSPF28/QSFP+, 1/100 nanometer resolution is 
supported (e.g 1536.61).  
 To display the status of Ethernet port 0/1 with SFP that supports DDM: 
ETX-2i-100G>config>port>eth(0/1)# show status 
Name ETH-0/1 
Administrative Status        : Up 
Operational Status           : Up 
Connector Type               : QSFP In 
Auto Negotiation             : Disabled 
Speed And Duplex             : 100G FX Full Duplex 
MAC Address                  : 00-20-D2-5B-0D-7F 
 
SFP 
--------------------------------------------------------------- 
Connector Type                : MPO 1x12 
Manufacturer Name             : Gigalight 
Manufacturer Part Number      : GQS-MPO101-SR4CL 
Manufacturer CLEI Code        : E5PSN24ACF      or    Not Available 
SFP Manufacture Date          : 25 Apr 2018 
SFP Serial Number             : M1712230241 
Typical Maximum Range (Meter) : 100 
Wave Length (nm)              : 850.00 
Fiber Type                    : MM 
RX Power (dBm)              : -3.74 dBm  
TX Power (dBm)              : 1.18 dBm  
Laser Bias (mA)             : 6.168 mA  
Laser Temperature (Celsius) : 29.84 C  
Power Supply (V)            : 3.24 V 
ETX-2i Devices 
2. Cards and Ports 
 To display the status of Ethernet port 0/7 with 100mbps SFP inserted into MiNID in  
ETX-2i-10G-B/8SFPP SFPP port: 
ETX-2i-10G-B-8SFPP>config>port>eth(0/7)# show status 
Name ETH-0/7 
 
Administrative Status        : Up 
Operational Status           : Up 
Connector Type               : SFP In 
Auto Negotiation             : Complete 
Speed And Duplex             : 1000 FX Full Duplex 
MAC Address                  : 18-06-F5-E8-38-FC 
 
SFP 
------------------------------------------------------------ 
Connector Type                : UNKNOWN                      
Manufacturer Name             : RAD                          
Manufacturer Part Number      : MiNID/GE                     
Manufacturer CLEI Code        : E5PSN24ACF      or    Not Available 
SFP Manufacture Date          : 00   2000                    
    
Typical Maximum Range (Meter) : 0                           
Wave Length (nm)              :                             
 SM                                                         
 To display the status of Ethernet port 0/3 if an SFP is inserted: 
ETX-2i# configure port ethernet 0/3 
ETX-2i>config>port>eth(0/3)# show status  
Administrative Status  : Up 
Operational Status     : Down 
Connector Type         : Combo RJ45+SFP In - SFP Active 
Auto Negotiation (SFP) : Other 
MAC Address            : 00-20-D2-E4-A2-66 
 
SFP 
--------------------------------------------------------------- 
Connector Type                : LC                           
Manufacturer Name             : RAD data comm.               
Manufacturer Part Number      : MiRICi-155                   
SFP Manufacture Date          : 09 Jul 2017                     
SFP Serial Number             : GL1707100384                    
Typical Maximum Range (Meter) : 15000                        
Wave Length (nm)              : 1310.00                      
Fiber Type                    : Not Applicable  
 
 
ETX-2i Devices 
2. Cards and Ports 
 To display the status of Ethernet port 0/3 (SFPP) with a DAC cable (sfp-h10gb-cu3m) 
ETX-2i# configure port ethernet 0/3 
ETX-2i>config>port>eth(0/3)# show status  
Administrative Status  : Up 
Operational Status     : Down 
Connector Type         : Combo RJ45+SFP In - SFP Active 
Auto Negotiation (SFP) : Other 
MAC Address            : 00-20-D2-E4-A2-66 
 
SFP 
--------------------------------------------------------------- 
Connector Type                : Copper pigtail                           
Manufacturer Name             : RAD data comm.               
Manufacturer Part Number      : MiRICi-155                   
SFP Manufacture Date          : 09 Jul 2017                     
SFP Serial Number             : GL1707100384                    
Typical Maximum Range (Meter) : 3                        
Wave Length (nm)              : 1310.00                      
Fiber Type                    : Not Applicable 
 To display the status of Ethernet port 1 with Silent Start enabled: 
ETX-2i# show con port eth 1 status 
Name Eth-1 
  
Administrative Status         : Up 
Operational Status            : Up 
Connector Type                : SFP  
Auto Negotiation ………..        : Disabled 
Speed And Duplex ………..        : 1000 Full Duplex 
MAC Address                   : 00-20-D2-51-0C-50 
Silent Start                  : In progress 
 To display the status of an Ethernet port 0/1 that took part in a mirroring session: 
 
Eth 0/1 is the source of traffic, and mirrors RX traffic. 
 
Eth 0/1 does not act as the destination of mirrored traffic. 
ETX-2i-10G>config>port# eth 0/2 
ETX-2i-10G>config>port>eth(0/1)# show status 
Name ETH-0/1 
 
Administrative Status        : Up 
Operational Status           : Down 
Connector Type               : SFP+ Out 
Auto Negotiation             : Disabled 
MAC Address                  : 00-20-D2-56-BA-D9 
Mirroring source status      : Rx 
Mirroring destination status : False 
ETX-2i Devices 
2. Cards and Ports 
 To display the status of an Ethernet port 0/2 that took part in a mirroring session: 
• 
Eth 0/2 is not the source of traffic. 
• 
Eth 0/2 acts as the destination of mirrored traffic. 
ETX-2i-10G>config>port# eth 0/2 
ETX-2i-10G>config>port>eth(0/2)# show status 
Name ETH-0/2 
 
Administrative Status        : Up 
Operational Status           : Down 
Connector Type               : SFP+ Out 
Auto Negotiation             : Disabled 
MAC Address                  : 00-20-D2-CD-7F-4C 
Mirroring source status      : -- 
Mirroring destination status : True 
 
Parameter 
Description 
Name 
Port name  
Administrative Status 
Possible values: Up, Down, Testing  
Operational Status 
Possible values: Up, Down, Testing, Unknown, Dormant, Not 
Present, Lower Layer Down 
Connector Type 
Possible values: RJ45, SFP 
Auto Negotiation 
Auto Negotiation status 
Possible values: --, Configuring, Completed, Disabled, Parallel 
Detection Failure 
Speed and Duplex 
Possible values: --, 10 Half, 10 Full, 100 Half, 100 Full, 1000 Half, 
1000 Full 
MAC Address 
MAC address, formatted 00-00-00-00-00-00 
Silent Start 
Visible only if Silent Start is enabled. 
Possible values: 
In Progress - Rx signal was detected but Ethernet was not 
completely recognized (Eth sync and Eth frames). 
Completed – Ethernet was recognized. 
No Signal Detected - No Rx optical signal detected (fiber 
disconnected). 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
Mirroring source status 
Possible values: 
-- 
Rx 
Tx 
Rx, Tx 
Mirroring destination status 
Possible values: --, True, False 
SFP 
Visible for SFP ports only 
Connector Type 
SFP connector type; string 
For example: LC, RJ-45, MOP, Copper Pigtail (when DAC-10G cable 
is in SFPP port),  Unknown 
Manufacturer Name 
SFP manufacturer name; string 
Manufacturer Part Number 
SFP manufacturer part number; string 
SFP Manufacturer Date 
Date, formatted as DD Month-Name Year. For example, 29 May 
2019 
SFP Serial Number 
SFP serial number; string 
Typical Maximum Range (Meter) 
SFP maximum range 
Wave Length (nm) 
SFP wave length 
Fiber Type 
SFP fiber type 
Possible values: --, Single-mode, Multi-mode 
SFP with DDM 
Visible only for SFPs that support DDM 
RX Power (dBm) 
SFP Rx power 
Note: For QSFP, displays the minimum value of its four channels. 
TX Power (dBm) 
SFP Tx power 
Note: For QSFP, displays the minimum value of its four channels. 
Laser Bias (mA) 
SFP laser bias 
Note: For QSFP, displays the maximum value of its four channels. 
Laser Temperature (Celsius) 
SFP laser temperature 
Power Supply (V) 
SFP power supply in volts 
ETX-2i Devices 
2. Cards and Ports 
Viewing SFP Extended Information 
ETX-2i supports reading the SFP vendor part number and user specific information from the SFP/SFP+, 
and displaying their ASCII values in the output of the show sfp-extended-information command. If an 
SFP/SFP+ field contains nonprintable control characters, the report shows “space” characters; if no 
information is present in the field, the report displays N/A. 
 To display SFP extended information: 
ETX-2i# configure port ethernet 0/3 
show sfp-extended-information  
 
sfp-vendor-specific 1 
--------------------------------------------------------------- 
Vendor Specific 1 : N/A   
                                                                
sfp-vendor-specific 2 
--------------------------------------------------------------- 
Vendor Specific 2 : 
                                                                
sfp-vendor-specific 3 
--------------------------------------------------------------- 
Vendor Specific 3 : N/A   
                                                                
sfp-user-specific 
--------------------------------------------------------------- 
User Specific : T-UNISFP40340960 
Testing Ethernet Ports 
The physical layer runs at the PHY of the ports. When the loopback is active the data forwarded to a port 
is looped from the Tx path to the Rx path. 
The loopback can be one of the following types: 
Local 
Loopback is closed toward the user interface. 
Remote 
Loopback is closed toward the network interface. 
 To run a physical layer loopback test: 
1. Navigate to configure port ethernet [<slot>/]<port-num> to select the Ethernet port to test. 
The config>port>eth([<slot>/]<port-num>)# prompt is displayed. 
2. Enter: 
loopback {local | remote} [duration <seconds>] 
ETX-2i Devices 
2. Cards and Ports 
The duration is in seconds, with range 0–86400. Entering 0 or not specifying the duration 
disables the timer, e.g., the loopback runs forever until you disable it. 
While the test is running, entering show summary at the port level displays the port’s 
operational status as Testing (see Viewing Ethernet Port Status).  
3. To end the loopback test, enter: 
no loopback 
 To run loopback on Ethernet port 0/3: 
exit all 
configure port ethernet 0/3 
loopback remote duration 30 
 To display loopback status: 
ETX-2i>config>port>eth(0/3)# show loopback 
Loopback : Remote         Remain (sec)  : 21 
Viewing Ethernet Port Statistics 
You can display statistics for the Ethernet ports, as well as L2CP statistics.  
 To display Ethernet port statistics: 
• 
At the prompt config>port>eth([<slot>/]<port-num>)#, enter: 
show statistics 
Ethernet port statistics are displayed. The counters are described in the following table. 
 To display the statistics for Ethernet port 0/2 in ETX-2i: 
ETX-2i# configure port ethernet 0/2 
ETX-2i>config>port>eth(0/2)# show statistics 
Rates Sampling Window 
--------------------------------------------------------------- 
Window Size [Min.]        : 15 
Window Remain Time [Min.] : 14 
 
 
Running 
--------------------------------------------------------------- 
Counter                    Rx                   Tx 
Total Frames               312248842            0 
Total Octets               41216847144          0 
Total Frames/Sec           0                    0 
ETX-2i Devices 
2. Cards and Ports 
Total Bits/Sec (L1)        0                    0 
Minimum Bits/Sec (L1)      0                    0 
Maximum Bits/Sec (L1)      0                    0 
Total Bits/Sec (L2)        0                    0 
Minimum Bits/Sec (L2)      0                    0 
Maximum Bits/Sec (L2)      0                    0 
Unicast Frames             312248842            0 
Multicast Frames           0                    0 
Broadcast Frames           0                    0 
 
CRC Errors                 0 
Error Frames               0                    0 
L2CP Discarded             0 
OAM Discarded              0 
Unknown Protocol Discarded 0 
CRC Errors/Sec             0 
Jabber Errors              0 
Oversize Frames            0                    0 
Unmapped Cos Frames        0                    -- 
MTU Discarded              --                   0 
 
64 Octets                  0                    0 
65-127 Octets              0                    0 
128-255 Octets             312248842            0 
256-511 Octets             0                    0 
512-1023 Octets            0                    0 
1024-1518 Octets           0                    0 
1519-2047 Octets           0                    0 
2048-Max Octets            0                    0 
 
MTU Discarded Flow         --                   -- 
 To display statistics for 100GbE Ethernet port 0/1 in ETX-2i-100G/4Q: 
ETX-2i-100G>config>port>eth(0/1)# show statistics 
Rates Sampling Window 
----------------------------------------------------------------------------- 
Window Size [Min.]        : 15 
Window Remain Time [Min.] : 3 
 
 
Running 
----------------------------------------------------------------------------- 
Counter                    Rx                   Tx 
Total Frames               0                    0 
Total Octets               0                    0 
Total Frames/Sec           0                    0 
Total Bits/Sec (L1)        0                    0 
Minimum Bits/Sec (L1)      0                    0 
Maximum Bits/Sec (L1)      0                    0 
Total Bits/Sec (L2)        0                    0 
Minimum Bits/Sec (L2)      0                    0 
ETX-2i Devices 
2. Cards and Ports 
Maximum Bits/Sec (L2)      0                    0 
Unicast Frames             0                    0 
Multicast Frames           0                    0 
Broadcast Frames           0                    0 
 
CRC Errors                 0 
Error Frames               0                    0 
L2CP Discarded             0 
OAM Discarded              0 
Unknown Protocol Discarded 0 
CRC Errors/Sec             0 
Jabber Errors              0 
Oversize Frames            0                    0 
Unmapped Cos Frames        0                    -- 
MTU Discarded              --                   0 
 
64 Octets                  0                    0 
65-127 Octets              0                    0 
128-255 Octets             0                    0 
256-511 Octets             0                    0 
512-1023 Octets            0                    0 
1024-1518 Octets           0                    0 
1519- Max Octets           0                    0 
 
MTU Discarded Flow         --                   -- 
 
Parameter 
Description 
Window Size [Min.] 
Interval for sampling statistics, user-configurable (see Setting Port Statistics 
Sampling Interval) 
Window Remain Time [Min.] 
Amount of time remaining in statistics sampling window 
Total Frames 
Total number of frames received/transmitted 
Total Octets 
Total number of bytes received/transmitted 
Total Frames/Sec 
Number of frames received/transmitted per second 
Total Bits/Sec (L1) 
Number of bits received/transmitted per second in Layer 1, using the line rate: 
[Total number of bytes + (number of packets x 20 bytes of line overhead)] 
divided by the time interval  
Minimum Bits/Sec (L1) 
Minimum number of bits received/transmitted per second in Layer 1, using the 
line rate: [Total number of bytes + (number of packets x 20 bytes of line 
overhead)] divided by the time interval  
Maximum Bits/Sec (L1) 
Maximum number of bits received/transmitted per second in Layer 1, using the 
line rate: [Total number of bytes + (number of packets x 20 bytes of line 
overhead)] divided by the time interval  
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
Total Bits/Sec (L2) 
Number of bits received/transmitted per second in Layer 2, using the data rate: 
[Total number of bytes (not including line overhead) divided by the time 
interval 
Minimum Bits/Sec (L2) 
Minimum number of bits received/transmitted per second in Layer 2, using the 
data rate: [Total number of bytes (not including line overhead) divided by the 
time interval 
Maximum Bits/Sec (L2) 
Maximum number of bits received/transmitted per second in Layer 2, using the 
data rate: [Total number of bytes (not including line overhead) divided by the 
time interval 
Unicast Frames 
Total number of unicast frames received/transmitted 
Multicast Frames 
Total number of multicast frames received/transmitted 
Broadcast Frames 
Total number of broadcast frames received/transmitted 
CRC Errors 
Total number of frames received that are an integral number of octets in 
length, but do not pass the Frame Check Sequence (FCS) check. This count 
excludes frames received with Frame-Too-Long or Frame-Too-Short error. 
Error Frames 
Total number of discarded Rx/Tx error frames  
Rx Error frames counter includes the following cases: 
• Oversize frames - Received packet is larger than 12K.  
• MAC error packets - MAC ingress queue (FIFO) full (performance) 
• Short packets - Received packet is smaller than 64 bytes. 
Tx Error frames counter includes frames dropped due to unresolved forwarding 
destination, including frames with MAC SA = MAC DA 
L2CP Discarded 
Total number of L2CP frames discarded per L2CP profile action 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
OAM Discarded 
Total number of OAM frames discarded.  
OAM frames are discarded in the following cases: 
• low level discard - Packet’s OAM level is lower than the defined MEP’s level. 
• Packet received through the ‘Passive’ side of the MEP has an OAM level 
lower or equal to the defined MEP’s level. 
• The packet’s DA MAC matches the device MAC (My MAC), but there is no 
MEP/MIP match. 
• The packet’s DA MAC matches the device MAC (My MAC),  
There is a match for MIP, but the ingress packet is not Link Trace (LTM) or 
LoopBack message (LBM). 
• The packet’s DA MAC is Unicast, but the device’s MAC is not Unicast, 
resulting in a hit on a MEP. 
Refer to OAM Packet Handling in the Monitoring and Diagnostics chapter for 
all cases when OAM packet is discarded. 
Unknown Protocol Discarded 
Total number of frames with unknown protocol, which are discarded. This 
includes:  
• Packets dropped as they were not matched by a classifier profile 
• Packets dropped by the L2PT mechanism as a result of a non-existent 
forwarding path 
CRC Errors/Sec 
Number of frames per second received that are an integral number of octets in 
length, but do not pass the Frame Check Sequence (FCS) check. This count 
excludes frames received with Frame-Too-Long or Frame-Too-Short error. 
Jabber Errors 
Total number of frames received with jabber errors 
Oversize Frames 
Total number of oversized frames received/transmitted 
Unmapped CoS Frames 
 
MTU Discarded 
Total number of packets dropped due to exceeding the egress-mtu limit 
configured over the port. Relevant to Ethernet, PCS, and Logical MAC ports.  
64 Octets 
Total number of received/transmitted 64-byte packets  
65–127 Octets 
Total number of received/transmitted 65 to 127-byte packets 
128–255 Octets 
Total number of received/transmitted 128 to 255-byte packets 
256–511 Octets 
Total number of received/transmitted 256 to 511-byte packets 
512–1023 Octets 
Total number of received/transmitted 512 to 1023-byte packets 
1024–1518 Octets 
Total number of received/transmitted 1024 to 1518-byte packets  
1519–Max Octets 
Appears in ETX-2i-100G/4Q 1G, 10G, and 100G port statistics  
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
1519–2047 Octets 
Total number of received/transmitted 1519 to 2047-byte packets. 
Appears in 1G and 10G port statistics only, for all devices except  
ETX-2i-100G/4Q. 
2048–Max Octets 
Total number of received/transmitted packets with 2048 bytes and up to 
maximum. 
Appears in 1G and 10G port statistics only, for all devices except  
ETX-2i-100G/4Q. 
MTU Discarded Flow 
The last flow from which MTU packets were discarded. Relevant to Ethernet, 
PCS, and Logical MAC ports. 
Viewing Fat Pipe Information 
You can display Fat pipe information on active Fat pipes (up to 10), expired Fat pipes (up to 32), or both. 
 To display the Ethernet port Fat pipe information: 
• 
At the prompt config>port>eth([<slot>/]<port-num>)#, enter: 
show fat-pipe-list { active | history | all } 
where 
active – shows only the active Fat pipes 
history – shows only the expired Fat pipes 
all – shows both active and expired Fat pipes 
Only those L2-L4 packet attributes (up to five) that you configured in the Fat pipe detection profile (refer 
to Configuring Fat Pipe Detection) are displayed in the report. The parameters are described in the 
following table. 
 To display information of active Ethernet port 0/1 Fat pipes: 
ETX-2i-10G-B>config>port>eth(0/1)# show fat-pipe-list active 
 
Entity : e2000   
 
Entity         : 1         Detection Time        : 1970-01-01 00:02:18 
Duration (Sec) : 107       Detected Rate (Mbps)  : 1662 
Current Rate (Mbps): 1475 
 
Src MAC Address                                : AA-10-94-00-00-03  
 
ETX-2i Devices 
2. Cards and Ports 
 To display information of history (closed) Ethernet port 0/1 Fat pipes: 
ETX-2i-10G-B>config>port>eth(0/1)# show fat-pipe-list history 
Entity : e2000 
 
Entity         : 2         Detection Time        : 1970-01-01 00:02:18 
Duration (Sec) : 107  Detected Rate (Mbps): 1662  Current Rate (Mbps): 1876 
 
 
Src MAC Address                                : AA-10-94-00-00-02 
 
 
Entity : e2000 
 
Entity         : 3         Detection Time        : 1970-01-01 00:02:34 
Duration (Sec) : 91  Detected Rate (Mbps): 1185  Current Rate (Mbps): 801 
 
 
Src MAC Address                                : EE-10-94-00-00-02 
 To display information of active Ethernet port 0/4 Fat pipes: 
ETX-2i-10G-B>config>port>eth(0/4)# show fat-pipe-list active 
 
Entity : abc 
 
Entity         : 1         Detection Time        : 1970-01-01 00:00:14 
Duration (Sec) : 4280      Detected Rate (Mbps) : 167                     Current Rate 
(Mbps)  : 1081 
 
Src IP Address                     : 1234:5678:9abc:def1:2345:6789:abcd:ef12  
 
 
Entity : abc 
 
Entity         : 2         Detection Time        : 1970-01-01 00:00:15 
Duration (Sec) : 4279      Detected Rate (Mbps)  : 167                     Current Rate 
(Mbps)  : 1081 
 
Src IP Address                     : 192.85.55.95 
 
Parameter 
Description 
Entity 
Fat pipe profile name 
Entity 
Entry number 
Possible values: 1-10 for active list; 1-32 for history list 
Detection Time 
The time of day that the Fat pipe was detected 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
Duration (Sec) 
Duration that Fat pipe is active (in seconds)  
Detected Rate (Mbps) 
The Fat pipe rate measured at the time of Fat pipe detection. 
Possible values: 0-10,000 
Current Rate (Mbps) 
The current ingress Fat pipe flow rate 
Possible values: 0-10,000 
Src MAC Address 
Source MAC address of packet 
Dst MAC Address 
Destination MAC address of packet 
Ethertype 
Ethertype of packet 
VLAN 
Packet Vlan 
P-bit 
P-bit of packet 
Inner Ethertype 
Packet’s Inner Ethertype  
Inner VLAN 
Packet’s Inner VLAN  
Inner p-bit 
Packet’s Inner p-bit  
DSCP 
Packet’s DSCP value 
IP Precedence 
IP Precedence of packet 
ToS 
ToS of packet 
Protocol 
Packet protocol 
Src IP Address 
Packet source IP address 
Dst IP Address 
Packet destination IP address 
L4 Src Port 
Layer-4 source port 
L4 Dst Port 
Layer-4 destination port 
Viewing Layer-2 Control Processing (L2CP) Statistics 
You can view L2CP statistics for Ethernet, Logical MAC, and PCS ports. The following procedure describes 
how to generate L2CP statistics for an Ethernet port. The counters displayed relate to L2CP MAC swap 
functionality.  
 To display L2CP statistics for an Ethernet port: 
• 
At the prompt config>port>eth(1/1)#, enter show l2cp-statistics 
ETX-2i Devices 
2. Cards and Ports 
L2CP statistics are relevant to the tunnel with the MAC swap functionality only and are displayed 
for the specified port, showing the number of encapsulated and decapsulated packets for each 
protocol. 
ETX-2i>config>port>eth(0/1)# show l2cp-statistics 
Protocol              Encapsulated   Decapsulated 
----------------------------------------------------------------------------- 
LACP                  0              0 
STP                   0              0 
CDP                   3201           3184 
VTP                   0              0 
LLDP                  0              0 
PVSTP                 0              0 
PAGP                  0              0 
UDLD                  0              0 
DTP                   0              0 
LAMP                  0              0 
Link OAM              0              0 
ELMI                  1539           754 
802.1x                0              0 
GVRP                  0              0 
GMRP                  0              0 
MMRP                  0              0 
MVRP Customer Bridge  0              0 
MVRP Provider Bridge  0              0 
MSRP                  0              0 
MIRP                  0              0 
DLDP                  0              0 
HGMP                  0              0 
PTP                   3202           3184 
ESMC                  3201           3184 
 
Total                11143           10306 
Clearing Statistics 
 To clear statistics for an Ethernet port: 
• 
At the prompt config>port>eth([<slot>/]<port-num>)#, enter: 
clear-statistics 
 To clear L2CP statistics for an Ethernet port: 
• 
At the prompt config>port>eth([<slot>/]<port-num>)#, enter: 
clear-l2cp-statistics 

## 2.7 GFP Ports  *(p.632)*

ETX-2i Devices 
2. Cards and Ports 
Viewing Ethernet Port Data Rate and Line Rate 
You can measure the data rate and line rate at which Ethernet ports transmit and receive, for a 
configurable time interval of 10–300 seconds.  
After you enter the command to measure the rates, 
ETX-2i automatically displays the results when the specified time interval ends.  
The data rate is calculated by dividing the total number of bytes (not including line overhead) by the 
time interval. The line rate is calculated by dividing (total number of bytes + (number of packets x 20 
bytes of line overhead)) by the time interval. 
 To start data rate and line rate measurements for an Ethernet port: 
• 
At the prompt config>port>eth([<slot>/]<port-num>)#, enter: 
rate-measure interval <seconds> 
The rate measurement starts. You can use show rate to monitor how much of the time interval 
has elapsed. The result is automatically displayed, without the need to enter show rate, after 
the specified time interval ends. 
2.7 GFP Ports 
In order to run EoPDH, you are required to configure GFP logical ports.  
GFP logical ports provide a logical link to built-in E1/T1/T3 ports, smart SFP E1/T1/T3/SDH/SONET ports, 
or modular E1/T1/T3 ports. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, with the following conditions: 
• 
GFP ports are relevant to ETX-2i modular options. 
• 
VCG ports are relevant to ETX-2i modular options. 
Standards Compliance 
G.7041 
ETX-2i Devices 
2. Cards and Ports 
Functional Description 
ETX-2i uses GFP (Generic Framing Procedure) ports to provide a logical link to the TDM ports that 
become available when smart SFPs are inserted (see Smart SFPs), or an E1/T1/T3 module is installed.  
ETX-2i supports up to four GFP ports when inserting up to four Smart SFPs (MiRICs) into the device 
ports.  
When using the GFP module, up to eight E1/T1 or two T3 can be supported in a single GFP VCAToPDH 
group. 
Note 
• 
If a module with multiple E1/T1/T3 ports is installed, the GFP port is 
bound to the VCG port that is bound to the E1/T1/T3 ports. 
• 
If a module with a single T3 port is installed, the GFP port is bound directly 
to the T3 port.  
Factory Defaults 
By default, no GFP ports exist. When a GFP port is created, it is configured as shown below. 
Parameter 
Default  
Remarks 
name 
GFP <port> 
 
scrambler-payload 
rx-tx 
Scrambling on the GFP packet payload in both 
directions is enabled. 
fcs-payload 
no fcs-payload 
CRC-32 sequence of GFP packet payload is 
disabled. 
 
Configuring GFP Ports 
 To configure a GFP port: 
1. At the config>port# prompt, enter: 
gfp <port> 
The port is created if it does not already exist, and the config>port>gfp(<port>)# prompt is 
displayed. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Binding GFP port to E1, T1, T3, or 
SDH/SONET port 
bind e1 [<slot>/]<port> 
bind t1 [<slot>/]<port> 
bind e3 [<slot>/]<port> 
bind t3 [<slot>/]<port> 
bind sdh-sonet [<slot>/]<port> 
• The relevant smart SFP port must 
exist, or if binding to a modular T3 
port, a module with a single T3 
port must be installed. 
• The GFP port index must match the 
TDM port index. 
• Use the no bind form to remove 
the binding. 
Binding GFP port to VCG port 
bind vcg <port> 
• The VCG port must exist. 
• The GFP port index must match the 
VCG port index. 
• Use the no bind form to remove 
the binding. 
Enabling CRC-32 sequence of GFP 
packet payload 
fcs-payload  
Enter no fcs-payload to disable.  
Assigning name to GFP port  
name <string> 
 
Enabling scrambling on the GFP 
packet payload in both directions 
scrambler-payload rx-tx 
Enter no scrambler-payload to 
disable.  
Enabling/disabling VLI byte 
insertion on VCAT trunk or PDH 
vcat-header 
If enabled, VCAT header is added to 
frames. 
Note:  
• Not relevant to GFP port bound to 
SDH/SONET port, modular T3 port, 
or VCG port. 
• VCAT is supported only under E1 
framing with line type set to G.732 
with CRC. 
Displaying a list of interfaces 
bound to the port 
show bind  
Lower level binds to E1. 
Higher level binds to VCG. 
Displaying GFP port statistics 
show statistics 
 
Clearing port statistics 
clear-statistics 
 
Displaying GFP port status 
show status 
Operation Status: 
Up – if lower layer is up (if E1 is up) 
Down – if lower layer is down (if E1 is 
down) 
ETX-2i Devices 
2. Cards and Ports 
Examples 
 To configure GFP logical port 5: 
• 
Bind to VCG port 15, which must be bound to multiple E1/T1/T3 ports on the module. 
exit all 
config port gfp 15 
bind vcg 15 
exit all 
 To display information on GFP logical port 1: 
ETX-2i# config port gfp 15 
ETX-2i>config>port>gfp(15)# info detail 
    name  "GFP 15 " 
    bind  vcg 15 
    no fcs-payload 
    scrambler-payload rx-tx 
ETX-2i>config>port>gfp(15)# show status 
Name                  : GFP 15 
Operation Status      : Up 
ETX-2i>config>port>gfp(15)# show bind 
Higher Layer 
--------------------------------------------------------------- 
  
Lower Layer 
---------------------------------------------------------------VCG        1               
 To configure GFP logical port 3: 
• 
Bind to smart SFP E1 port 3. 
exit all 
config port gfp 3 
bind e1 0/3/1 
exit all 
 To display the status of GFP logical port 3: 
ETX-2i# config port gfp 3 
ETX-2i>config>port>gfp(3)# show status 
Name                  : GFP 3 
Operation Status      : Up 

## 2.8 Internal Ports for x86 Interconnection  *(p.636)*

ETX-2i Devices 
2. Cards and Ports 
2.8 Internal Ports for x86 Interconnection 
Two predefined internal Ethernet ports are used for interconnection between the ETX-2i NID and x86 
processor, if applicable.  
• 
Ethernet 1, interconnected to ETX-2i internal Ethernet port 8  
• 
Ethernet 2, interconnected to ETX-2i internal Ethernet port 7 
 
Note 
For ETX-2i or ETX-2i-B with D-NFV/PMC option, regular user ports 7 and 8 are 
not available.  
Applicability and Scaling 
This feature is applicable to ETX-2i or ETX-2i-B with the D-NFV/PMC option. 
Factory Defaults 
By default, the internal Ethernet ports have the following configuration. 
Parameter 
Description 
Default Value 
dhcp-trust 
Trust server DHCP packets 
Disabled (trust client DHCP 
packets) 
name 
Port name 
INT ETH <port-num> 
queue-group  
Queue group profile 
DefaultQueueGroup 
shutdown 
Administrative status 
no shutdown 
Functional Description 
The internal ports are always administratively enabled. They can be ingress or egress ports in flows, to 
enable transmitting data between the ETX-2i NID and the x86 processor.  
The internal ports cannot be members of a LAG or be assigned Ethernet protection group. 
 
 
ETX-2i Devices 
2. Cards and Ports 
You can configure flows between the internal ports and the following types of ports: 
• 
Bridge port 
• 
Ethernet port 
• 
ETP Subscriber port 
• 
LAG 
You cannot configure flows between the internal Ethernet ports and the following types of ports: 
• 
ETP subscriber port 
• 
SVI assigned to router interface 
Configuring the Internal Ports 
The internal ports are referred to in the CLI as int-ethernet <port-num>, where <port-num> is 7 or 8.  
 To configure the internal port parameters: 
1. Navigate to configure port int-ethernet <port-num> to select the internal port to configure. 
The config>port>int-eth(<port-num>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Configuring port to trust DHCP 
packets sent from server 
dhcp-trust 
Client ports must always be untrusted 
(no dhcp-trust); otherwise, the DHCP 
relay discards the discovery messages 
sent from the client port to the 
server. 
Relevant only if DHCP snooping is 
enabled. 
Assigning description to port 
name <string> 
Entering no name removes the name. 
Associating a queue group 
profile with the port 
queue-group profile 
<queue-group-profile-name> 
 
Displaying port status 
show status 
 
Displaying port statistics 
show statistics 
 

## 2.9 Link Aggregation Group (LAG) Ports  *(p.638)*


## 2.10 Logical MAC Ports  *(p.638)*

ETX-2i Devices 
2. Cards and Ports 
2.9 Link Aggregation Group (LAG) Ports 
LAG ports are used to logically combine a number of physical ports together to form a single high-
bandwidth data path. 
For full details, refer to Link Aggregation in the Resiliency and Optimization chapter. 
2.10 Logical MAC Ports 
Logical MAC ports connect between flows and modular E1/T1/T3 ports via GFP ports. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products, with the following conditions: 
• 
GFP ports are relevant to ETX-2i modular options. 
• 
VCG ports are relevant to ETX-2i modular options. 
Functional Description 
ETX-2i uses logical MAC ports to connect flows to GFP (Generic Framing Procedure) ports that provide a 
logical link to modular E1/T1/T3 ports, or to the TDM ports that become available when smart SFPs are 
inserted (see Smart SFPs). In the case of modular E1/T1/T3 ports, the logical MAC port can operate as a 
network or user port (user configurable). You can configure a logical MAC port that functions as a user 
port with L2PT network functionality (see Layer-2 Control Protocol (L2CP) Processing above for 
explanation). 
 
 
ETX-2i Devices 
2. Cards and Ports 
Factory Defaults 
By default, no logical MAC ports exist. When a logical MAC port is created, it is configured as shown 
below. 
Description 
Default Value 
Port name 
LOGICAL MAC <logical-mac-port-number> 
Administrative status 
Disabled 
Trust server DHCP packets 
Disabled 
Port to which the logical MAC is bound  
GFP 5 
Ethernet tag protocol identifier 
0×8100 
Egress MTU 
1790 
Functional mode 
network 
Queue group profile 
DefaultQueueGroup 
L2CP profile 
L2cpDefaultProfile 
Configuring Logical MAC Ports 
 To configure logical MAC ports: 
1. At the config>port# prompt, enter 
logical-mac <port> 
The port is created if it does not already exist, and the config>port>log-mac(<port>)# prompt is 
displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Possible Values 
Binding logical MAC port to GFP port 
bind gfp <port> 
The GFP port must exist. 
Use the no bind form to remove 
the binding. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
Specifying classification key per port 
classification-key [legacy] [vlan] 
[inner-vlan] 
legacy – No classification key is 
used. 
vlan – Classification key 
according to VLAN 
inner-vlan – Classification key 
according to VLAN + Inner VLAN 
Valid for flow classifier only. 
You can change the port 
classification key only if all flows 
using this port are 
administratively disabled.  
Refer to the relevant table in 
Classification Keys in the Traffic 
Processing chapter to see the 
queue/priority mapping 
methods for the selected 
classification key, as well as the 
flows / flow parameters that 
can be configured for the key. 
Configuring port classification 
classifier 
Refer to Configuring Port 
Classification in the Traffic 
Processing chapter. 
Configuring port to trust DHCP packets 
sent from server 
dhcp-trust 
Client ports must always be 
untrusted (no dhcp-trust); 
otherwise, the DHCP relay 
discards the discovery messages 
sent from the client port to the 
server. 
Relevant only if DHCP snooping 
is enabled. 
Configuring OAM EFM descriptor 
efm descriptor 
<efm-descriptor-index> 
Refer to Configuring OAM EFM 
in the Monitoring and 
Diagnostics chapter. 
Setting maximum frame size to transmit 
(frames above the specified size are 
discarded) 
egress-mtu < max-frame-size > 
max-frame-size – maximum size 
of transmitted frames 
Possible values: 64-12288 bytes 
Configuring the functional mode 
functional-mode {user | 
network} 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
Associating a Layer-2 control processing 
profile with the port 
l2cp profile <l2cp-profile-name> 
For an explanation on how to 
configure an L2CP profile, refer 
to Layer-2 Control Protocol 
(L2CP) Processing in the Traffic 
Processing chapter.  
Configuring logical MAC port with L2PT 
network functionality 
l2pt-network 
Configurable for logical MAC 
port that functions as a user 
port. 
Enter no l2pt-network to 
disable PCS port from 
functioning as an L2PT network 
port. 
Configuring LLDP parameters 
lldp 
Refer to Link Layer Discovery 
Protocol (LLDP) in the Traffic 
Processing chapter for details. 
Running loopback test on port 
loopback {local|remote} 
[duration <seconds>] 
Use the no loopback command 
to stop the test. 
 
Assigning a name to the port 
name <string> 
 
Configuring collection of performance 
management statistics for the port, that 
are presented via the RADview 
Performance Management portal 
pm-collection interval 
<seconds> 
Note: In addition to enabling 
PM statistics collection for the 
port, it must be enabled for the 
device. Refer to Performance 
Management in the Monitoring 
and Diagnostics chapter for 
details. 
Associating a queue group profile with 
the port 
queue-group profile 
<queue- profile-name> 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
Setting the VLAN tagged frame ETH II 
frame EtherType (tag protocol identifier) 
tag-ethernet-type 
<0x0000-0xFFFF> 
Port EtherType can be set to 
one of the following values: 
0x8100 (default) 
0x88a8  
A user-configured global 
EtherType (provided it has been 
defined at the device (chassis) 
level) 
Note:  
• If you do not configure an 
EtherType for the port, the 
port uses the default setting 
(8100). 
• You cannot change the 
EtherType tag if the port 
(Ethernet or LAG) has flows 
attached to it. 
Administratively enabling port 
no shutdown 
Entering shutdown disables the 
port. 
Displaying the interfaces that are bound 
to the port 
show bind 
 
Displaying link OAM (EFM) parameters 
show oam-efm 
 
Displaying OAM EFM statistics 
show oam-efm-statistics 
 
Displaying L2CP statistics 
show l2cp-statistics 
See Viewing Layer-2 Control 
Processing (L2CP) Statistics. 
Displaying port status 
show status 
 
Displaying port statistics 
show statistics 
 
Clearing OAM EFM statistics 
clear-efm-statistics 
 
Clearing L2CP statistics 
clear-l2cp-statistics 
 
Clearing port statistics 
clear-statistics 
 
 
 
ETX-2i Devices 
2. Cards and Ports 
 To change the logical MAC port back to ETH: 
1. At the config>port# prompt, enter 
no logical-mac <port> 
The port mode changes from Logical MAC to ETH. 
The config>port>eth([<slot>/]<port-num>)# prompt is displayed. 
2. Enter shutdown and then no shutdown. 
The ETH port hardware is disabled and then enabled, synchronizing the ETH port, provided that 
line/cable/fiber is connected. 
Examples 
 To configure logical MAC port 3: 
• 
Bind to GFP port 3. 
exit all 
logical-mac 3 
bind gfp 3 
no shutdown 
exit all 
 To display information on logical MAC port 3: 
ETX-2i>config>port# logical-mac 3 
ETX-2i>config>port>log-mac(3)# info detail 
    name  "LOGICAL MAC 3" 
    no shutdown 
    bind  gfp  3 
    tag-ethernet-type  0x8100 
    egress-mtu  1790 
    queue-group profile  "DefaultQueueGroup" 
    l2cp profile  "L2cpDefaultProfile 
 
ETX-2i>config>port>log-mac(3)# show status 
Name                  : LOGICAL MAC 3 
Administrative Status : Up 
Operational Status    : Up 

## 2.11 PCS Ports  *(p.644)*

ETX-2i Devices 
2. Cards and Ports 
2.11 PCS Ports 
The PCS port is the logical link to SHDSL or VDSL2 ports. You can create flows over the PCS port. 
Standards Compliance 
ITU-T G.991.2 
ETSI TS 101524 
Applicability and Scaling 
This feature is applicable to ETX-2i with an SHDSL or VDSL2 module. 
Functional Description 
The PCS (physical coding sublayer) port represents the bundling of the SHDSL/VDSL2 interfaces. By 
default, all SHDSL/VDSL2 lines are bound to a single PCS port. The PCS port can operate as a network or 
user port (user configurable). You can configure a PCS port that functions as a user port with L2PT 
network functionality (see Layer-2 Control Protocol (L2CP) Processing above for explanation). 
Factory Defaults 
The PCS port default configuration is shown below. 
Description 
Default Value 
Port name 
PCS 1 
Administrative status 
Enabled 
Classification key 
legacy 
DHCP trust 
no dhcp-trust 
Ethernet tag protocol identifier 
0×8100 
Egress MTU 
1790 
Functional mode 
Network 
ETX-2i Devices 
2. Cards and Ports 
Description 
Default Value 
Minimum links 
1 
OAM EFM 
no efm 
Queue group profile 
“DefaultQueueGroup” 
L2CP profile 
“L2cpDefaultProfile” 
Policer profile 
no policer 
Configuring PCS Ports 
 To configure the PCS port parameters: 
1. Navigate to configure port pcs <port> to select the PCS port to configure. 
The config>port>pcs(<port>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Binding port to PCS bundle 
[no] bind shdsl <port-index> 
[no] bind vdsl2 <port-index> 
 
Specifying classification key per 
port 
classification-key [legacy] [vlan] 
[inner-vlan] 
legacy – No classification key is used. 
vlan – Classification key according to 
VLAN 
inner-vlan – Classification key 
according to VLAN + Inner VLAN 
Valid for flow classifier only. 
You can change the port 
classification key only if all flows 
using this port are administratively 
disabled.  
Refer to the relevant table in 
Classification Keys in the Traffic 
Processing chapter to see the 
queue/priority mapping methods for 
the selected classification key, as 
well as the flows/flow parameters 
that can be configured for the key. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Clearing OAM EFM statistics 
clear-efm-statistics 
 
Clearing L2CP statistics 
clear-l2cp-statistics 
 
Clearing statistics 
clear-statistics 
 
Configuring port to trust DHCP 
packets sent from server 
[no] dhcp-trust 
Client ports must always be 
untrusted (no dhcp-trust); 
otherwise, the DHCP relay discards 
the discovery messages sent from 
the client port to the server. 
Relevant only if DHCP snooping is 
enabled. 
Enabling/disabling OAM EFM on 
PCS port 
[no] efm descriptor 
<efm-descriptor-index> 
Refer to Configuring OAM EFM in 
the Monitoring and Diagnostics 
chapter. 
Setting maximum frame size to 
transmit (egress MTU)  
egress-mtu <max-frame-size> 
max-frame-size – maximum size of 
transmitted frames  
Possible values: 64–12288 
Configuring the functional mode 
functional-mode {user | network} 
 
Associating a Layer-2 control 
processing profile with the port 
l2cp profile <l2cp-profile-name> 
For an explanation on how to 
configure an L2CP profile, refer to 
Layer-2 Control Protocol (L2CP) 
Processing in the Traffic Processing 
chapter. 
 
Configuring PCS port with L2PT 
network functionality 
l2pt-network 
Configurable for PCS port that 
functions as a user port. 
Enter no l2pt-network to disable PCS 
port from functioning as an L2PT 
network port. 
Running loopback test on port 
[no] loopback {local|remote} 
[duration <seconds>] 
Use the no loopback command to 
stop the test. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Configuring minimum active 
SHDSL ports 
minimum-links <minimum-links-
number> 
minimum-links-number – minimum 
number of active SHDSL ports 
required to set the PCS operational 
status to UP 
Possible values:  
1-4 (ports), for a device with SH8W 
(four SHDSL ports) 
1-2 (ports), for device with SH4W 
(two SHDSL ports). 
Default: 1 
The PCS oper status is declared 
DOWN if the number of active SHDSL 
ports falls below the configured 
minimum-links-number.  
• PCS oper status DOWN is 
declared with LLD (lower layer 
down). 
• Upon status change from UP to 
DOWN, a PCS alarm is issued.  
• If oper status goes DOWN due to 
a change in minimum-links-
number, Ethernet Tx and Rx 
traffic to/from the PCS port are 
blocked. 
The PCS oper status is declared UP if 
the number of active SHDSL ports is 
equal or higher than the configured 
minimum-links-number.  
• Upon status change from DOWN 
to UP, the PCS alarm is cleared.  
If oper status goes UP due to a 
change in minimum-links-number, 
Ethernet Tx and Rx traffic to/from 
the PCS port is reenabled. 
Assigning description to port 
name <string> 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Administratively enabling port 
no shutdown 
Entering shutdown disables the port. 
Note: If the PCS is disabled there is 
no traffic forwarding from/to the 
network side, although the lines may 
be physically synchronized. 
Configuring collection of 
performance management 
statistics for the port, that are 
presented via the RADview 
Performance Management 
portal 
[no] pm-collection interval 
<seconds> 
Note: In addition to enabling PM 
statistics collection for the ports, it 
must be enabled for the device. 
Refer to Performance Management 
in the Monitoring and Diagnostics 
chapter for details. 
Associating a Policer profile with 
the port 
[no] policer profile 
<policer-profile-name> 
Typing no policer removes any 
Policer profile from the port. 
Associating a queue group 
profile with the port 
[no] queue-group profile 
<queue-group-profile-name> 
Typing no queue-group removes any 
queue group profile from the port.  
Displaying the interfaces that 
are bound to the port 
show bind-summary 
 
Displaying L2CP statistics 
show l2cp-statistics 
See Viewing Layer-2 Control 
Processing (L2CP) Statistics. 
Displaying link OAM (EFM) 
parameters 
show oam-efm 
 
Displaying OAM EFM statistics 
show oam-efm-statistics 
 
Displaying port statistics 
show statistics running 
See Viewing PCS Port Statistics. 
Displaying port status 
show status 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Setting the VLAN tag EtherType 
tag-ethernet-type <0x0000-0xFFFF> 
Port EtherType can be set to one of 
the following values: 
0x8100 (default) 
0x88a8  
A user-configured global EtherType   
(provided it has been defined at the 
device (chassis) level) 
Note:  
• If you do not configure an 
EtherType for the port, the port 
uses the default setting (8100). 
• You cannot change the EtherType 
tag if the port (Ethernet or LAG) 
has flows attached to it. 
Viewing PCS Port Statistics 
You can display running statistics for the PCS ports. 
 To display the PCS port running statistics: 
• 
At the prompt config>port>pcs(<port>)#, enter: 
show statistics running 
PCS port statistics are displayed. The counters are described below. 
# configure port pcs 1 
ETX-2i>config>port>pcs(1)# show statistics running 
Rates Sampling Window 
--------------------------------------------------------------- 
Window Size [Min.]        : 15 
Window Remain Time [Min.] : 14 
 
 
Running 
---------------------------------------------------------------
Counter                    Rx                   Tx 
Total Frames               0                    0 
Total Octets               0                    0 
Total Frames/Sec           0                    0 
Total Bits/Sec             0                    0 
Minimum Bits/Sec           0                    0 
Maximum Bits/Sec           0                    0 
ETX-2i Devices 
2. Cards and Ports 
Unicast Frames             0                    0 
Multicast Frames           0                    0 
Broadcast Frames           0                    0 
CRC Errors                 0 
Error Frames               0                    -- 
L2CP Discarded             0                    -- 
CFM Discarded              0                    -- 
MTU Discarded              0                    56 
Unknown Protocol Discarded 0                    -- 
CRC Errors/Sec             0 
Jabber Errors              0                    -- 
Oversize Frames            0                    0 
64 Octets                  0                    0 
65-127 Octets              0                    0 
128-255 Octets             0                    0 
256-511 Octets             0                    0 
512-1023 Octets            0                    0 
1024-1518 Octets           0                    0 
1519-2047 Octets           0                    0 
2048-Max Octets            0                    0 
MTU Discarded Flow         : --/EVC1-TLV 
 
Parameter 
Description 
Window Size [Min.] 
Interval for sampling statistics, user-configurable (see Setting Port 
Statistics Sampling Interval) 
Window Remain Time 
[Min.] 
Amount of time remaining in statistics sampling window 
Total Frames 
Total number of frames received/transmitted 
Total Octets 
Total number of bytes received/transmitted 
Total Frames/Sec 
Number of frames received/transmitted per second 
Total Bits/Sec 
Number of bits received/transmitted per second 
Minimum Bits/Sec 
Minimum number of bits received/transmitted per second 
Maximum Bits/Sec 
Maximum number of bits received/transmitted per second 
Unicast Frames 
Total number of unicast frames received/transmitted 
Multicast Frames 
Total number of multicast frames received/transmitted 
Broadcast Frames 
Total number of broadcast frames received/transmitted 
CRC Errors 
Total number of frames received that are an integral number of octets in 
length, but do not pass the Frame Check Sequence (FCS) check. This 
count excludes frames received with Frame-Too-Long or Frame-Too-
Short error. 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
Error Frames 
Total number of frames with errors received 
L2CP Discarded 
Total number of L2CP frames discarded per L2CP profile action 
CFM Discarded 
Total number of CFM frames discarded. Refer to OAM Packet Handling 
in the Monitoring and Diagnostics chapter for all cases when OAM 
packet is discarded. 
MTU Discarded 
Total number of packets dropped due to exceeding the egress-mtu limit 
configured over the port  
Unknown Protocol 
Discarded 
Total number of frames with unknown protocol discarded 
CRC Errors/Sec 
Number of frames per second received that are an integral number of 
octets in length, but do not pass the Frame Check Sequence (FCS) check. 
This count excludes frames received with Frame-Too-Long or Frame-Too-
Short error. 
Jabber Errors 
Total number of frames received with jabber errors 
Oversize Frames 
Total number of oversized frames received/transmitted 
64 Octets 
Total number of received/transmitted 64-byte packets  
65–127 Octets 
Total number of received/transmitted 65 to 127-byte packets 
128–255 Octets 
Total number of received/transmitted 128 to 255-byte packets 
256–511 Octets 
Total number of received/transmitted 256 to 511-byte packets 
512–1023 Octets 
Total number of received/transmitted 512 to 1023-byte packets 
1024–1518 Octets 
Total number of received/transmitted 1024 to 1518-byte packets  
1519–2047 Octets 
Total number of received/transmitted 1519 to 2047-byte packets 
2048–Max Octets 
Total number of received/transmitted packets with 2048 bytes and up to 
maximum 
MTU Discarded Flow 
Last flow from which MTU packets were discarded  
 
 

## 2.12 Peers  *(p.652)*


## 2.13 SDH/SONET Ports  *(p.652)*

ETX-2i Devices 
2. Cards and Ports 
2.12 Peers 
Configuring peers provides access to remote devices. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
Peers are remote devices operating opposite router interfaces that can be linked in order to access the 
1588v2 master clock.  
Factory Defaults 
By default, no peers are defined in ETX-2i. 
Configuring Peers 
You can define up to 64 peers as explained below. 
 To define a peer: 
• 
At the config# prompt, do one of the following: 
 
To define the peer according to IP address, enter: 
peer <number> ip <ip-address> [name <name>] 
 
To define the peer according to MAC address, enter: 
peer <number> mac <mac-address> [name <name>] 
2.13 SDH/SONET Ports 
SDH/SONET ports are available when smart SFPs such as MiRICi-155 are provisioned (see Smart SFPs).  
SDH (Synchronous Digital Hierarchy) and SONET (Synchronous Optical Network) are standardized 
transport protocols that transfer multiple digital bit streams over optical fiber using lasers or 
light-emitting diodes (LEDs). SONET is the United States version and SDH is the international version. 
ETX-2i Devices 
2. Cards and Ports 
SDH and SONET allow many different circuits from different sources to be transported simultaneously 
within one single framing protocol. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products. Smart SFP SDH/SONET ports are referenced as 
[<slot>/]<port>/<tributary>. 
• 
<slot> is relevant to modular ports. 
• 
<tributary> is always set to 1. 
Standards Compliance 
SDH is defined by ITU-T G.707, G.781, G.782, G.783, and G.803. SONET is an ANSI standard defined in 
T1.105 and T1.119.  
Functional Description 
SDH is based on STM-1 which has a data rate of 155.52 Mbps, equivalent to STS-3. SONET is based on 
transmission at speeds of multiples of 51.840 Mbps, or STS-1.  
Factory Defaults 
By default, no SDH/SONET ports exist. 
Configuring SDH/SONET Ports 
 To configure SDH/SONET ports: 
1. Provision a smart SFP such as MiRICi-155 and insert it into an Ethernet port (see Smart SFPs). 
2. At the config>port# prompt, enter: 
sdh-sonet [<slot>/]<port>/<tributary> 
The prompt config>port>sdh-sonet([<slot>/]<port>/<tributary>)# is displayed. 
3. Perform the required tasks according to the following table. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Specifying the cell 
frame type 
frame-type { sdh | sonet } 
 
Running loopback test 
on port 
loopback { local | remote } 
[start <seconds> ] [duration <seconds>] 
local – returns the transmitted data at 
the physical layer to the receiving path 
remote – returns the received data at 
the physical layer to the transmitting 
path 
start – specifies the time (in seconds) 
until the loopback starts 
duration – specifies the duration of the 
loopback (in seconds). If duration is not 
specified, the loopback test runs 
forever, until stopped. 
Use no loopback to disable the 
loopback test. 
Assigning a name to 
the port 
name <string> 
 
Specifying if 
performance reporting 
is enabled for the port  
pm-enable 
 
Defining thresholds: 
• EED (Excessive 
Error Defect) –
detected if the 
equivalent BER (bit 
error rate) exceeds 
the selected 
threshold 
parameters 
• SD (Degraded 
Signal Defect) – 
detected if the 
equivalent BER 
exceeds the 
selected threshold 
parameter. 
threshold [ eed { 1e-3 |1e-4 | 1e-5 }] [ sd 
{ 1e-5 | 1e-6 | 1e-7 | 1e-8 | 1e-9 }] 
 

## 2.14 SFPs  *(p.655)*

ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Selecting the transmit 
clock source 
tx-clock-source { internal | loopback } 
internal – clock provided by internal 
oscillator 
loopback – clock retrieved from the 
port's incoming (Rx) data 
Displaying list of 
interfaces bound to 
port 
show bind 
 
Displaying the port 
status 
show status 
 
Displaying the port 
statistics 
show statistics current 
show statistics interval <interval-num> 
show statistics total 
show statistics all-intervals 
show statistics all 
You can specify the scope of the 
statistics, as follows: 
current – current statistics 
interval – interval statistics 
Where  
interval-num – interval number 
Possible values: 1-96 
total – preceding 24 hours cumulative 
statistics 
all-intervals – all interval statistics 
all – all statistics 
Clearing the statistics 
clear-statistics 
 
 
2.14 SFPs 
In ETX-2i, ETX-2i-B (ports 3 and 4), and ETX-2i-10G half 19-inch combo, the Ethernet ports are combo 
ports that have an RJ-45 connector and SFP slot, and the port can function as a copper port or SFP slot. 
In 
ETX-2i-100G, there are no combo ports; the Ethernet ports are fiber optic SFP+, SFP28, and QSFP28 
slots.  
The Ethernet ports that are fiber optic SFP slots, or combo ports functioning as SFP slots, are configured 
as shown in Ethernet Ports. When you display the port status, the SFP information is shown if applicable 
(see Viewing Ethernet Port Status).  
ETX-2i Devices 
2. Cards and Ports 
• 
You can insert regular SFP/SFP+ modules into the SFP/SFP+ slots (in ETX-2i, ETX-2i-B, and ETX-2i-
10G), or you can insert smart SFPs that provide integrated configuration and management (see 
Smart SFPs).  
• 
ETX-2i-10G 1G SFP ports support 1G copper SFPs (1G rate only); SFP+ (1/10G) ports support 1G 
copper SFPs (1G rate only) and 10G copper SFPPs.  
• 
In ETX-2i-10G-B/8SFPP, you can insert into the SFP side of a MiNID installed in an SFPP slot, a 
100M copper SFP. In this case, you should bind a Shaper profile configured with 100 Mbps 
bandwidth and 20 Bytes compensation (in order to avoid drops due to high Tx bursts), to the 
port level, i.e., to Queue Block 1/1 (level 1, QB1). MiNID should also be configured, as required. 
• 
In ETX-2i-100G QSFP28 slots, you can insert QSFP28 modules. ETX-2i-100G does not support 
smart SFPs in any of its SFP+, SFP28, or QSFP28 slots. 
• 
In ETX-2i-100G/4Q SFP28 slots, you can insert SFP28 modules. ETX-2i-100G does not support 
smart SFPs in any of its SFP+, SFP28, or QSFP28 slots. 
• 
In ETX-2i-100G/40G QSFPP slots, you can insert QSFPP modules. ETX-2i-100G does not support 
smart SFPs in any of its SFP+, QSFP28, or QSFPP slots. 
The following tables show the supported optical modules, features, and rates in the ETX-2i 1/10G, 
1/10/25G, 40G, and 100G port types: 
Optical Transceivers and Rates 
Inserted Optical 
Transceiver 
Speed&Duplex 
= 1G 
Speed&Duplex 
= 10G 
Speed&Duplex 
= 25G 
Speed&Duplex 
= 100G 
Speed&Duplex 
= Auto 
1G SFP 
1 Gb 
1 Gb 
NA 
NA 
1G 
10G SFPP 
NA 
10 Gb 
NA 
NA 
10G 
1/10G dual rate 
SFP 
1 Gb 
10 Gb 
NA 
NA 
10G 
SFP28 
NA 
NA 
25 Gb 
NA 
25G 
QSFP28 
NA 
NA 
NA 
100G 
NA 
MPO connector 
NA 
NA 
NA 
100G 
NA 
ETX-2i Devices 
2. Cards and Ports 
Default Port Parameters 
Feature 
SFPP Ports (1/10G) 
SFP28 Ports 
(1/10/25G) 
QSFPP Ports 
(40G) 
QSFP28 Ports 
(100G) 
 
Speed & 
Duplex=1G 
Speed&Duplex=
10G 
Speed&Duplex=
25G 
(ETX-2i-
100G/4Q) 
Speed&Duplex=
100G 
(ETX-2i-
100G/40G) 
Speed&Duplex=
100G 
(ETX-2i-100G) 
Auto-
negotiation 
Enabled  
10GbE - 
Disabled  
1GbE – Enabled 
Disabled 
Disabled 
Disabled 
Max capability 
advertised 
1G, FDX 
10GbE – NA 
1GbE – 1G, FDX 
NA 
NA 
NA 
Copper SFP/SFPP 
Parameter 
Copper SFP Type 
Single-Rate Copper 
SFP (1G Only) 
10G Copper SFP 
DAC-10G Cable 
1G Copper 
Mulit-Rate SFP 
(ETX-2i-10G-8SFPP 
only) 
Supported ports 
SFP/SFPP/SFP28 
SFPP/SFP28 
SFPP/SFP28 
SFPP 
Speed-duplex 
1000-full-duplex 
10g-r 
10g-r 
Configurable 
Autoneg 
Enabled 
NA 
NA 
Configurable 
Max capability 
1000Base-T full 
duplex 
NA 
NA 
100/1000M rates, 
configurable with or 
without autoneg 
 
Note 
ETX-2i does not support copper SFP. Combo ports are available. 
Port Features  
Feature 
SFPP Ports (1/10G) 
SFP28 Ports 
(1/10/25G) 
QSFPP Ports (40G) 
QSFP28 Ports 
(100G) 
LFS 
Supported for 
10Gbps 
Supported for 
10/25Gbps 
Supported 
Supported 
Optical connector 
LC 
LC 
LC 
LC 

## 2.15 Smart SFPs  *(p.658)*

ETX-2i Devices 
2. Cards and Ports 
SFPP Ports (1/10G) 
SFP28 Ports 
(1/10/25G) 
QSFPP Ports (40G) 
QSFP28 Ports 
(100G) 
DDM 
Supported 
Supported 
Supported 
Supported 
Flow Control 
Rx only 
Rx only 
Rx only 
Rx only 
FEC 
NA 
Supported 
NA 
Supported 
For information on installing SFP/SFP+/QSFP28/QSFP+ modules, and the SFP mismatch alarm, refer to 
Installing SFP/SFP+/QSFP28/QSFP+ Optical Transceivers in the Installation and Setup chapter. 
 
Note 
• 
For all ETX-2i, ETX-2i-B, and ETX-2i-10G temperature-hardened options, 
use hardened SFPs with maximum operating temperature 85°C (185°F).  
• 
It is strongly recommended to order this device with original RAD 
SFP/SFP+/QSFP28/QSFP+ transceivers (see Pluggable Transceivers data 
sheet). RAD cannot guarantee full compliance to product specifications 
for units using non-RAD transceivers.  
2.15 Smart SFPs 
ETX-2i offers the use of a wide variety of TDM E1/T1/E3/T3 OC-3/STM-1 ports via the smart SFP feature.  
ETX-2i supports integrated configuration and management of smart SFPs (such as MiRICi/MiTOP 
devices) to provide TDM port functionality. The following are supported: 
• 
MiRICi-E1/T1/E3/T3 
• 
MiRICi-155 
• 
MiTOP-E1/T1/E3/T3 
ETX-2i supports up to four smart SFPs per device. 
For ETX-2i-10G, smart SFPs are supported in standalone mode only. 
 
Applicability and Scaling 
This feature is applicable to ETX­2i, ETX-2i-B, and ETX-2i-10G. ETX-2i-100G does not support smart SFPs. 
ETX-2i Devices 
2. Cards and Ports 
Functional Description 
The smart SFP is provisioned in the specific Ethernet port where the SFP shall be inserted. After this 
provisioning, the Ethernet port is no longer available for normal Ethernet port functioning. If the smart 
SFP is provisioned in a combo Ethernet port, the copper connector can no longer be used. 
The TDM port is automatically created when the smart SFP is provisioned and can be configured. For 
information on configuring the TDM port, see the respective TDM port section. 
After you provision a smart SFP, you can do the following: 
• 
Define a logical GFP interface over the smart SFP port (see GFP Ports). 
• 
Define a logical MAC interface over the GFP interface (see Logical MAC Ports). 
• 
Create a flow over the logical MAC interface (refer to Classification by Port/Flow in the Traffic 
Processing chapter). 
Note 
If a smart SFP is inserted into ETX-2i while it is powered on, the smart SFP 
becomes operational only after resetting ETX-2i.  
Factory Defaults 
By default, no smart SFPs are provisioned. When a smart SFP interface is created, it is administratively 
disabled by default, with type set to not-applicable. 
Configuring Smart SFPs 
To provision a smart SFP, you use the smart-sfp command to specify the Ethernet port, and then you 
assign the type of smart SFP. 
 To configure smart SFPs: 
1. At the config>port# prompt, enter smart-sfp [<slot>/]<port>, where [<slot>/]<port> indicates 
the Ethernet port where the SFP is (or shall be) inserted (see Port Numbering for the port 
numbers). 
Note 
You can provision the smart SFP before you insert it.  
The smart SFP interface is created if it does not already exist and the 
config>port>smart-sfp([<slot>/]<port>)$ prompt is displayed. 
2. Perform the required tasks according to the following table. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Assigning the type of smart SFP 
type { mirici-e1 | mirici-t1 | mirici-e3 | 
mirici-t3 | mirici-155 | mitop-e1 | 
mitop-t1 | mitop-e3 | mitop-t3 | 
not-applicable } 
The smart SFP port must be 
administratively disabled 
before you can change the 
type. 
To change the type, you must 
first set it to not-applicable. 
Resetting smart SFP 
reset 
 
Displaying interface status 
show status 
 
Administratively enabling interface 
no shutdown 
You cannot administratively 
enable the smart SFP port if its 
type is set to not-applicable. 
Entering shutdown disables the 
interface. 
Examples 
This example shows how a smart SFP can be provisioned, and a flow created over the logical MAC port 
corresponding to a logical GFP port.  
 To provision a smart SFP and corresponding flow in ETX-2i: 
• 
Ethernet GbE port 0/1 
• 
Smart SFP type = MiRICi-E1 
• 
GFP port 1 
• 
Logical MAC port 1 
• 
Flow = flow1, with classification criterion VLAN 1 
#*****************Provision the smart SFP 
exit all 
configure port smart-sfp 1 
shutdown 
type not-applicable 
type mirici-e1 
no shutdown 
exit 
 
 
 
ETX-2i Devices 
2. Cards and Ports 
#*****************Create the GFP and bind it to the E1 port 
gfp 1 
bind e1 0/1/1 
exit 
 
#*****************Create the logical MAC port and bind it to GFP port 1 
logical-mac 1 
bind gfp 1 
no shutdown 
exit all 
 
#*****************Create the flow and activate it 
configure flows 
classifier-profile v1 match-any match vlan 1 
flow flow1 
classifier v1 
ingress-port logical-mac 1 
egress-port eth 0/3 queue 0 block 0/1 
no shutdown 
exit all 
 To display information on the entities configured in the above script: 
ETX-2i# configure port smart-sfp 1 
ETX-2i>config>port>smart-sfp(1)# info detail 
    type  mirici-e1 
    no shutdown 
ETX-2i>config>port>smart-sfp(1)# exit 
 
ETX-2i>config>port# gfp 1 
ETX-2i>config>port>gfp(1)# info detail 
    name  "GFP 1" 
    bind  e1  1/1 
    no fcs-payload 
    scrambler-payload rx-tx 
    no vcat-header 
ETX-2i>config>port>gfp(1)# exit 
 
ETX-2i>config>port# logical-mac 1 
ETX-2i>config>port>log-mac(1)# info detail 
    name  "LOGICAL MAC 1" 
    no shutdown 
    bind  gfp  1 
    tag-ethernet-type  0x8100 
    egress-mtu  1790 
    queue-group profile  "DefaultQueueGroup" 
    l2cp profile  "L2cpDefaultProfile" 
ETX-2i>config>port>log-mac(1)#exit all 
ETX-2i# configure flows 
 
 

## 2.16 SHDSL Ports  *(p.662)*

ETX-2i Devices 
2. Cards and Ports 
ETX-2i>config>flows>flow(flow1)# info detail 
    classifier  "v1" 
    no drop 
    policer  profile  "Policer1" 
    no mark  all 
    no vlan-tag 
    no l2cp 
    ingress-port  logical-mac  1 
    egress-port  ethernet 0/3  queue  0 block  0/1 
    no shutdown 
2.16 SHDSL Ports 
ETX-2i is optionally equipped with a module that has two or four Single Pair High-speed Digital 
Subscriber Line (SHDSL) ports (4-wire or 8-wire) 
ETX-2i can aggregate traffic over the SHDSL.bis links. 
The SHDSL interfaces are bundled into one PCS (physical coding sublayer) port. See PCS Ports for 
commands related to the PCS port. 
Applicability and Scaling 
This feature is applicable to ETX-2i with an SHDSL module. 
ETX-2i supports CPE mode (STU-R) only. K.21 is not supported. 
Standards Compliance 
ITU-T G.991.2 (SHDSL.bis) 
ITU-T G.994.1 (DSL Handshake) 
EFM 802.3ah (EFM and EFM bonding) 
ETX-2i Devices 
2. Cards and Ports 
Functional Description 
SHDSL is a data communications technology that enables faster data transmission over copper 
telephone lines than a conventional voice band modem can provide. Compared to ADSL, SHDSL employs 
frequencies that include those used by traditional POTS telephone services to provide equal data rates 
to transmit and receive. As such, a telephone line cannot be used by both an SHDSL service and a POTS 
service at the same time. Support of symmetric data rates has made SHDSL a popular choice by 
businesses for PBX, VPN, web hosting and other data services. 
The SHDSL uplink supports up to eight wires with ordering options of either four or eight wires. Each 
four wires is supported over an RJ-45 connector, meaning that a four-wire ordering option is supported 
with a single RJ-45 and an eight-wire option is supported with two RJ-45.  
SHDSL.bis per G.991.2 features symmetrical data rates in both upstream and downstream directions, Up 
to 5696 kbit/s of payload for one pair of wires is supported. The reach varies according to 
the loop rate and noise conditions (more noise or higher rate means decreased reach) and may be up to 
3,000 meters. 
SHDSL ports support EFM Bonding. The EFM Aggregation layer allows multiple pairs of copper ports 
used as a single, high-capacity link. This enables carrying far more bandwidth over the existing copper 
infrastructure.  
Dying Gasp is supported over an SHDSL port, using OAM-EFM messages per IEEE 802.3-2005. 
Configuring SHDSL Ports 
This section explains how to configure the SHDSL port. 
 To configure the SHDSL port parameters: 
1. Navigate to configure port shdsl 1/<port> to select the SHDSL port to configure, where 1 is the 
module slot number. 
2. At the prompt, perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
Displaying port status 
show status 
See Viewing SHDSL Port Status. 
Displaying port statistics 
show statistics { current | interval 
<interval-num> | current-day | all-
intervals | all-days-intervals | all } 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Clearing the port statistics 
clear-statistics 
 
Assigning port name 
name 
 
Administratively enabling port 
no shutdown 
Entering shutdown disables the 
SHDSL port, stops issuing alarms for 
the port, and turns off the SHDSL 
LED. 
Viewing SHDSL Port Status 
 To display the status of SHDSL port 1: 
ETX-2i# config port shdsl 1/1 
ETX-2i>config>port>shdsl(1/1)# show status 
Name                  : SHDSL-1/1 
Administrative Status : Up 
Operation Status      : Down 
Wires                 : 2 
Transmission Mode     : B-G 
Payload Rate (Kbps)   : 0 
 
Wires 
----------------------------------------------------------------------------- 
  State       SNR         Loop          Tx      PSD        Power 
             Margin     Attenuation   Power     Mask     Backoff 
             (db)         (db)         (dBm) 
----------------------------------------------------------------------------- 
Data          18            1           8.5    Symmetric     6 
 
Parameter 
Description 
Name 
Port name 
Administrative Status 
SHDSL line administrative status 
Up or Down 
Operation Status 
SHDSL line operational status 
Up or Down 
Wires 
Number of wires in port 
Transmission Mode 
Possible values: A-F, B-G 
Payload Rate (Kbps) 
Actual payload rate without the framing overhead of 8Kbps 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
Wires 
 
State 
Possible values: Pre Activation, Activation, Data 
SNR Margin (dB) 
Actual Rx SNR on this link 
Loop Attenuation (dB) 
Actual Rx Loop Attenuation on this link 
Tx Power (dBm) 
Actual Tx power (dBm) 
PSD Mask 
Masks for upstream and downstream 
Possible values: Symmetric, Assymetric 
Power Backoff 
Current Tx power backoff 
Viewing SHDSL Port Statistics 
 To display the SHDSL port 1 current statistics: 
ETX-2i# config port shdsl 1/1 
-DSLETX-2i>config>port>shdsl(1/1)# show statistics current 
Current 
----------------------------------------------------------------------------- 
Time Elapsed (Sec) : 712 
Valid Intervals    : 96 
 
ES                 : 0         LOSWS          : 0 
SES                : 0         CRC Anomalies  : 0 
UAS                : 0 
 
Parameter 
Description 
Time Elapsed (Sec) 
The elapsed time (in seconds) for the current interval/day 
Valid Intervals 
Number of valid intervals for which statistics are displayed; default is 15-minute 
intervals. 
ES 
Number of Errored Seconds where one or more CRC error events or one or 
more LOSW error events have been detected. This parameter is inhibited 
during UAS state. 
SES  
Number of Severely Errored Seconds where 50 or more CRC error events or 
one or more LOSW error events have been detected. This parameter is 
inhibited during UAS state. 

## 2.17 Service Virtual Interfaces (SVIs)  *(p.666)*

ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
UAS 
Number of Unavailable Seconds. This state begins after 10 consecutive 
severely-errored seconds, and ends after 10 consecutive error-free seconds. 
LOSWS 
Number of seconds during which Loss Of Sync Word events have been detected 
CRC Anomalies 
Number of errors detected by cyclic redundancy checks 
2.17 Service Virtual Interfaces (SVIs) 
Service Virtual Interface (SVI) is a virtual (logical) port that is used for binding router interfaces and 
tunnel interfaces (GRE), to Ethernet Logical MAC, and PCS ports (via Layer-2 flows). 
SVIs are used as ingress and egress ports for flows, serving as intermediaries for routers. 
Applicability and Scaling 
This feature is applicable to all ETX-2i products. 
SVI 
ETX-2i 
ETX-2i-B 
ETX-2i-10G 
ETX-2i-100G 
gre 
✓ 
✓ 
 
 
pw 
✓ 
✓ 
✓ 
✓ 
router 
✓ 
✓ 
✓ 
✓ 
twamp 
✓ 
✓ 
✓ 
✓ 
Functional Description 
You can define four types of SVIs: 
• 
router – SVI that can be bound to router interface via Layer-2 flows 
• 
twamp – In TWAMP Layer-2 Probe mode; TWAMP SVI allows administratively enabling the 
router interface, even though there are no flows to and from the SVI. After defining the TWAMP 
controller and responder, it becomes possible to bind SVI to the router interface via Layer-2 
flows. 
ETX-2i Devices 
2. Cards and Ports 
• 
gre – SVI that can be bound to GRE tunnel interface 
• 
pw – SVI that can be bound to pseudowires with PSN type Ethernet 
Note 
Router SVI is the default. In the CLI command, you do not specify a type for a 
Router SVI.  
 To create an SVI port: 
1. Create an SVI port of a specific number and name, and if other than a Router SVI, specify its type 
(TWAMP, GRE, PW). 
2. Enable the SVI by entering no shutdown. 
3. Configure flows with:  
 
Ingress Ethernet port and egress SVI port (defined in step 1). 
 
Ingress SVI port (defined in step 1) and egress Ethernet port. 
(Refer to Configuring Flows in the Traffic Processing chapter.) 
4. For Router or TWAMP SVI: Bind the router interface to the SVI (of type Router or TWAMP). 
(Refer to Configuring Router Interface in the Traffic Processing chapter.) 
5. For GRE SVI: Bind the tunnel interface to the GRE SVI. (Refer to Configuring GRE Tunneling in 
the Traffic Processing chapter.) 
6. For PW SVI: Set the PW egress port to the SVI. (Refer to the egress-port svi <port-number> 
command in Setting Pseudowire Bundle Parameters in the Traffic Processing chapter.) 
Note 
You can follow the steps above to create an SVI port between a Logical MAC 
or PCS port (instead of Ethernet port) and a router.  
Factory Defaults 
By default, SVI 96 (the highest SVI ID) is administratively enabled (configured in no shutdown mode).  
The following is the SVI configuration in the ETX-2i, ETX-2i-B,and ETX-2i-100G  factory default files. 
# Factory Default File 
configure 
    port 
        svi 96 
            no shutdown 
        exit 
    exit 
 
 
ETX-2i Devices 
2. Cards and Ports 
    flows 
        classifier-profile mng_untagged match-any 
            match untagged 
        exit 
        classifier-profile mng_all match-any 
            match all 
        exit 
        flow mng_access_default_in 
            classifier mng_untagged 
            no policer 
            ingress-port ethernet 0/101 
            egress-port svi 96 
            no shutdown 
        exit 
        flow mng_access_default_out 
            classifier mng_all 
            no policer 
            ingress-port svi 96 
            egress-port ethernet 0/101 
            no shutdown 
        exit 
    exit 
    router 1 
        interface 31            address 169.254.1.1/16 
            bind svi 96 
            no shutdown 
        exit 
    exit 
exit 
The following is the SVI configuration in the ETX-2i-10G factory default file. 
ETX-2i-10G# file 
ETX-2i-10G>file# show factory-default-config 
#header device-name "ETX-2I-10G" 
 
# Factory Default File 
configure 
    port 
        svi 96 
            no shutdown 
        exit 
    exit 
    flows 
        classifier-profile mng_untagged match-any 
            match untagged 
        exit 
        classifier-profile mng_all match-any 
            match all 
        exit 
 
 
ETX-2i Devices 
2. Cards and Ports 
        flow mng_access_default_in 
            classifier mng_untagged 
            no policer 
            ingress-port ethernet 0/101 
            egress-port svi 96 
            no shutdown 
        exit 
        flow mng_access_default_out 
            classifier mng_all 
            no policer 
            ingress-port svi 96 
            egress-port ethernet 0/101 
            no shutdown 
        exit 
    exit 
    router 1 
        interface 32 
            address 169.254.1.1/16 
            bind svi 96 
            no shutdown 
        exit 
    exit 
exit 
You can delete the default configuration, as required. 
Configuring Service Virtual Interfaces 
 To configure the SVI parameters: 
1. Navigate to configure port svi <svi-num> [twamp | gre | pw ] to select the SVI to configure. 
 
svi-num can be 1-96. 
The type indicates the kind of SVI port to create, and can be: 
 
twamp –for use with TWAMP 
 
gre –for use with ETHoGRE 
 
pw –for use with MEF8 PWs  
 
Note 
When the type is not specified, the default router is used.  
2. At the config>port>svi(<svi-num>)# prompt, perform the required tasks according to the 
following table. 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Setting the port name 
name <string> 
 
Administratively enabling SVI 
no shutdown 
Entering shutdown disables the SVI. 
 
 
Note 
Entering no svi <svi-num> at the config>port prompt, deletes the SVI.  
Examples 
 To configure router SVI: 
• 
Number – 3 
• 
Type – router 
• 
Name – svi_3 
ETX­2i>config>port>svi 3  
ETX-2i>config>port>svi(3)# name svi_3 
ETX-2i>config>port>svi(3)# no shutdown 
 To configure TWAMP SVI: 
• 
Number – 1 
• 
Type – TWAMP 
• 
Name – svi_1_twamp 
ETX-2i>config>port>svi 1 twamp 
ETX-2i>config>port>svi(1)# name svi_1_twamp 
ETX-2i>config>port>svi(1)# no shutdown 
 To configure GRE SVI: 
• 
Number – 2 
• 
Type – GRE 
• 
Name – svi_2_gre 
ETX-2i>config>port>svi 2 gre 
ETX-2i>config>port>svi(2)# name svi_2_gre 
ETX-2i>config>port>svi(2)# no shutdown 

## 2.18 T1 Ports  *(p.671)*

ETX-2i Devices 
2. Cards and Ports 
2.18 T1 Ports 
The T-carrier signaling scheme was devised by Bell Labs and is a widely used standard in 
telecommunications in the USA, Canada, and Japan to transmit voice and data between devices. T1, also 
referred to as DS-1, is a high-speed dedicated data line that transmits information of large volume at the 
speed of 1.544 Mbps. 
Applicability and Scaling 
T1 ports are applicable to ETX-2i products as follows: 
• 
Smart SFP T1 ports: 
 
Smart SFP T1 ports are available when smart SFPs such as MiRICi-T1 or MiTOP-T1 are 
provisioned (see Smart SFPs) 
 
Smart SFP T1 ports do not support encapsulation via VCG 
 
Smart SFP T1 ports are referenced as [<slot>/]<port>/<tributary>: 
 
<slot> is relevant to modular ports. 
 
<tributary> is always set to 1. 
• 
E1/T1 module: 
 
Modular E1/T1 ports can be configured to T1 mode (see DS1 (E1/T1) Ports). The default 
mode is E1.  
 
Modular T1 ports support encapsulation via VCG (see VCGs) 
 
Modular T1 ports are referenced as <slot>/<port>. 
Standards Compliance 
ITU-T G.703 
ITU-T G.704 
ITU-T G.823 
Functional Description 
A T1 link operates over a twisted pair of cables. A nominal 3-volt peak signal is encoded with pulses 
using a method that avoids long periods without polarity changes. The line data rate is 1.544 Mbps at 
ETX-2i Devices 
2. Cards and Ports 
full duplex, which means 1.544 Mbps for downstream and 1.544 Mbps for upstream. The T1 signal splits 
into 24 timeslots each which is allocated 8 bits. Each timeslot sends and receives an 8-bit sample 
8000 times per second (8 x 8000 x 24 = 1,544,000), which is ideal for voice telephone calls where the 
voice is sampled into an 8-bit number at that data rate and restored at the other end. The timeslots are 
numbered from 0 to 24. 
Factory Defaults 
By default, no smart SFP T1 ports exist. 
By default, modular E1/T1 ports are set to E1 mode. When they are configured to T1 mode, they have 
the following configuration. 
Parameter 
Value 
Remarks 
line-code 
b8zs 
Zero code suppression 
line-length  
0-133 
 
line-type  
ESF 
 
name 
T1 <slot>/<port> 
 
rx-sensitivity 
Short-haul 
Attenuation level of received 
signal 
shutdown 
shutdown 
Administratively disabled 
 
Configuring T1 Ports 
Configuring Built-in T1 Ports 
 To configure T1 ports: 
1. Configure the port to T1 mode (see Configuring E1/T1 Ports) 
2. At the config>port# prompt, enter: 
t1 <port>/<tributary> 
The prompt config>port>t1(<port>/<tributary>)# is displayed. 
3. Perform the required tasks according to the following table. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
Specifying out-of-service 
indication to transmit for T1 
port with CAS signaling 
cas-oos-codes space <space-code> 
mark <mark-code> 
space-code - space signaling code 
allowed range: 0x0–0xf 
mark-code - mark signaling code 
allowed range: 0x0–0xf 
Note:  
• This command is relevant only with 
line type esf or sf(D4). 
• When R bits and L bits are used to 
indicate T1 CAS faults on the 
remote side, the OOS code sent to 
the T1 CAS interface is the default 
(0xFF), rather than the actual OOS 
code. 
Specifying transmission 
sequence for out-of-service 
indication for T1 port with CAS 
signaling 
cas-oos-pattern {space | mark | 
space-mark} 
Note: This command is relevant only 
with line type esf or sf(D4). 
Specifying inband loopback 
inband-loopback { local | remote } 
csu 
inband-loopback { local | remote } 
niu { fac1 | fac2 } 
inband-loopback { local | remote } 
program <loop-up-code> 
<loop-up-len> <loop-down-code> 
<loop-down-len> 
 
Specifying TX gain of the DSL 
line (dB), when line-interface is 
set to csu 
line-buildout { 0db | -7dot5db 
| -15db | -22dot5db } 
0db: No db 
-7dot5db: -7.5 db 
-15db: -15 db 
-22dot5db: -22.5 db 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
Specifying the variety of zero 
code suppression used for this 
port 
line-code { ami | b8zs } 
ami – Referred to as Alternate Mark 
Inversion (AMI) because a 1 is referred 
to as a mark and a 0 as a space. 
b8zs – bipolar 8-zero substitution 
(B8ZS), in which two successive ones 
(bipolar violations) are inserted 
whenever the stream of user data 
contains a string of eight or more 
consecutive zeros. This insertion is 
done in a way that allows each of the 
24 channels to carry 64 kbsp of data.  
Specifying the length (in feet) of 
the T1 line, in DSU mode 
line-length { 0-133 | 134-266 | 
267-399 | 400-533 | 534-655 } 
 
Specifying the T1 line type 
line-type { unframed | esf | sf } 
unframed – No framing (this type is 
relevant only for built-in T1 ports) 
sf (D4) – Super Frame (12 T1 frames) 
esf – Extended Super Frame (24 T1 
frames, with on-line performance 
monitoring and 4 Kbps control data 
link) 
Running loopback test on T1 
port 
loopback { local | remote } 
[duration <seconds>] 
local – returns the transmitted data at 
the physical layer to the receiving path 
remote – returns the received data at 
the physical layer to the transmitting 
path 
start – specifies the time (in seconds) 
until the loopback starts. Possible 
values: 1 to 3600 
duration – specifies the duration of the 
loopback (in seconds). Possible values: 
1 to 3600  
If duration is not specified, the 
loopback test runs forever, until 
stopped. 
Use no loopback to disable the 
loopback test. 
Assigning a name to the port 
name <string> 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
Specifying if performance 
reporting is enabled for the 
port 
pm-enable 
 
Specifying attenuation level of 
the receive signal that is 
compensated for by the 
interface receive path 
rx-sensitivity { short-haul | 
long-haul } 
 
Specifying the port clock quality 
source-clock-quality { stratum1 | 
stratum2 | stratum3 | stratum3e | 
stratum4 } 
Clock quality used in adaptive clock 
recovery set according to parameter 
specified: 
stratum1 – PRC G.811  
stratum2 – Type II G.812 
stratum3 – Type IV G.812 
stratum3e – Type III G.812 
stratum4 – Free running 
Administratively disabling or 
enabling the port 
shutdown 
Enter no shutdown to administratively 
enable the port. 
Displaying list of interfaces 
bound to port 
show bind 
 
Displaying loopback test status 
show loopback 
 
Displaying the port status 
show status 
 
Displaying the port statistics 
show statistics current 
show statistics interval 
<interval-num> 
show statistics total 
show statistics all-intervals 
show statistics all 
You can specify the scope of the 
statistics, as follows: 
current – current statistics 
interval – interval statistics 
Where  
interval-num – interval number 
Possible values: 1-96 
total – preceding 24 hours cumulative 
statistics 
all-intervals – all interval statistics 
all – all statistics 
Clearing the statistics 
clear-statistics 
 
ETX-2i Devices 
2. Cards and Ports 
Configuring Modular T1 Ports 
 To configure T1 ports: 
1. If the module type is not E1/T1, power off ETX-2i, insert the E1/T1 module, and then power on 
ETX-2i. 
2. Provision the module type as E1/T1 (see Configuring Module). 
3. Configure the port to T1 mode (see Configuring E1/T1 Ports). 
4. At the config>port# prompt, enter: 
t1 [<slot>/]<port>/<tributary> 
The prompt config>port>t1([<slot>/]<port>/<tributary>)# is displayed. 
5. Perform the required tasks according to the following table. 
 
Task 
Command 
Possible Values 
Specifying TX gain of the DSL 
line (dB), in CSU mode 
line-buildout { 0db | -7dot5db 
| -15db | -22dot5db } 
0db: No db 
-7dot5db: -7.5 db 
-15db: -15 db 
-22dot5db: -22.5 db 
This command appears in the CLI 
only if rx-sensitivity is configured to 
long-haul, which indicates CSU 
mode. 
Specifying the variety of zero 
code suppression used for 
this port 
line-code { ami |b8zs } 
ami – Referred to as Alternate Mark 
Inversion (AMI) because a 1 is 
referred to as a mark and a 0 as a 
space. 
b8zs – bipolar 8-zero substitution 
(B8ZS), in which two successive 
ones (bipolar violations) are 
inserted whenever the stream of 
user data contains a string of eight 
or more consecutive zeros. This 
insertion is done in a way that 
allows each of the 24 channels to 
carry 64 kbsp of data. 
Note: Only B8ZS can be configured 
for modular T1 ports. 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
Specifying the length (in 
feet) of the T1 line, in DSU 
mode 
line-length { 0-133 | 134-266 | 
267-399 | 400-533 | 534-655}  
This command appears in the CLI 
only if rx-sensitivity is configured to 
short-haul, which indicates DSU 
mode. 
Specifying the T1 line type 
line-type { unframed |esf | sf } 
unframed – No framing  
sf – Super Frame (12 T1 frames) 
esf – Extended Super Frame (24 T1 
frames, with on-line performance 
monitoring and 4 Kbps control data 
link) 
Note: Only esf can be configured 
for modular T1 ports. 
 
Running loopback test on T1 
port 
loopback { local | remote } 
 [duration <seconds>] 
local – returns the transmitted data 
at the physical layer to the receiving 
path 
remote – returns the received data 
at the physical layer to the 
transmitting path 
start – specifies the time (in 
seconds) until the loopback starts 
Possible values: 1–3600 
duration – Specifies the duration of 
the loopback (in seconds) 
Possible values: 1–3600 
If duration is not specified, the 
loopback test runs forever, until 
stopped. 
Use no loopback to disable the 
loopback test. 
Assigning a name to the port 
name <string> 
 
Specifying if performance 
reporting is enabled for the 
port 
pm-enable 
 
Specifying attenuation level 
of the receive signal that is 
compensated for by the 
interface receive path 
rx-sensitivity { short-haul | 
long-haul } 
short-haul indicates DSU mode. 
long-haul indicates CSU mode. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
Administratively disabling or 
enabling the port 
shutdown 
Enter no shutdown to 
administratively enable the port. 
Displaying list of interfaces 
bound to port 
show bind 
 
Displaying loopback test 
status 
show loopback 
 
Displaying the port status 
show status 
 
Displaying the port statistics 
show statistics current 
show statistics interval 
<interval-num> 
show statistics all-intervals 
show statistics all 
 
Clearing the statistics 
clear-statistics 
 
Configuring Smart SFP T1 Ports 
 To configure smart SFP T1 ports: 
1. Provision a smart SFP port with type MiRICi-T1 or MiTOP-T1 (see Smart SFPs). 
2. Insert the MiRICi-T1/ MiTOP-T1 into the Ethernet port. 
Note 
Initialize the database of the MiTOP before inserting it into the device. Refer 
to the Setting the Switches section in the Installation and Setup chapter of the 
MiTOP E1T1 Installation and Operation manual.  
3. At the config>port# prompt, enter: 
t1 [<slot>/]<port>/<tributary> 
The prompt config>port>t1([<slot>/]<port>/<tributary>)# is displayed. 
4. Perform the required tasks according to the following table, and the type of smart SFP. 
Task 
Command 
Possible Values 
MiR
ICi 
MiT
OP 
Specifying TX gain of the DSL 
line (dB), when line-interface is 
set to csu 
line-buildout { -7dot5db 
| -15db | -22dot5db } 
-7dot5db: -7.5 db 
-15db: -15 db 
-22dot5db: -22.5 db 
× 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
MiR
ICi 
MiT
OP 
Specifying the variety of zero 
code suppression used for this 
port 
line-code { ami | b8zs } 
ami – Referred to as Alternate 
Mark Inversion (AMI) because a 
1 is referred to as a mark and a 0 
as a space. 
b8zs – bipolar 8-zero 
substitution (B8ZS), in which two 
successive ones (bipolar 
violations) are inserted 
whenever the stream of user 
data contains a string of eight or 
more consecutive zeros. This 
insertion is done in a way that 
allows each of the 24 channels 
to carry 64 kbsp of data. 
 
 
Specifying T1 operation mode 
line-interface { dsu | csu } 
dsu – Digital Service Unit 
csu – Channel Service Unit 
× 
 
Specifying the length (in feet) 
of the T1 line 
line-length { 0-133 | 
134-266 | 267-399 | 
400-533 | 534-655 } 
 
 
 
Specifying the T1 line type 
line-type { unframed |esf 
| sf } 
unframed – No framing 
(relevant only for MiTOP) 
sf – Super Frame (12 T1 frames) 
esf – Extended Super Frame (24 
T1 frames, with on-line 
performance monitoring and 
4 Kbps control data link) 
 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
MiR
ICi 
MiT
OP 
Running loopback test on T1 
port 
loopback { local | remote } 
[duration <seconds>] 
local – returns the transmitted 
data at the physical layer to the 
receiving path 
remote – returns the received 
data at the physical layer to the 
transmitting path 
start – specifies the time (in 
seconds) until the loopback 
starts 
Possible values: 1–3600  
duration – specifies the duration 
of the loopback (in seconds).  
Possible values: 1–3600 
If duration is not specified, the 
loopback test runs forever, until 
stopped. 
Use no loopback to disable the 
loopback test. 
 
 
Assigning a name to the port 
name <string> 
 
 
 
Specifying if performance 
reporting is enabled for the 
port 
pm-enable 
 
 
 
Specifying attenuation level of 
the receive signal that is 
compensated for by the 
interface receive path 
rx-sensitivity { short-haul 
| long-haul } 
 
 
 
Specifying the port clock 
quality 
source-clock-quality  
{ stratum1 | stratum2 | 
stratum3 | stratum3e | 
stratum4 }  
Clock quality used in adaptive 
clock recovery set according to 
parameter specified: 
stratum1 – PRC G.811  
stratum2 – Type II G.812 
stratum3 – Type IV G.812 
stratum3e – Type III G.812 
stratum4 – Free running 
× 
 

## 2.19 T3 Ports  *(p.681)*

ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
MiR
ICi 
MiT
OP 
Selecting the transmit clock 
source 
tx-clock-source { loopback 
| internal | 
domain <number> | 
pw <number> } 
loopback – clock retrieved from 
the port's incoming (Rx) data 
internal – clock provided by 
internal oscillator 
domain – clock provided by 
clock domain, if device has 
timing option 
pw – clock provided by PW 
bundle 
Note: The domain and pw 
options are available only for 
MiTOP. 
 
 
 
Administratively disabling or 
enabling the port 
shutdown 
Enter no shutdown to 
administratively enable the port. 
 
 
Displaying list of interfaces 
bound to port 
show bind 
 
 
 
Displaying loopback test status 
show loopback 
 
 
 
Displaying the port status 
show status 
 
 
 
Displaying the port statistics 
show statistics current 
show statistics interval 
<interval-num> 
show statistics 
all-intervals 
show statistics all 
 
 
 
Clearing the statistics 
clear-statistics 
 
 
 
2.19 T3 Ports 
T3, also referred to as DS-3 (Digital Signal Level 3), equates to 28 T-1 lines or 44.736 million bits per 
second (roughly 43-45 Mbps upstream/downstream speeds). DS-3s have enough bandwidth to allow 
very large database transfers over busy wide area networks. 
ETX-2i Devices 
2. Cards and Ports 
T3 lines enable high-capacity Ethernet services in remote locations and transparently connect corporate 
LANs over existing PDH infrastructure. 
Applicability and Scaling 
T3 ports are applicable to the ETX-2i products as follows: 
• 
Smart SFP T3 ports: 
 
Smart SFP T3 ports are available when smart SFPs such as MiRICi-T3 or MiTOP-T3 are 
provisioned (see Smart SFPs) 
 
Smart SFP T3 ports do not support encapsulation via VCG 
 
Smart SFP T3 ports are referenced as [<slot>/]<port>/<tributary>: 
 
<slot> is relevant to modular ports. 
 
<tributary> is always set to 1. 
• 
T3 module: 
 
Modular T3 ports support encapsulation via VCG (see VCGs) 
 
Modular T3 ports are referenced as <slot>/<port>. 
Standards Compliance 
ITU-T G.703 
ITU-T G.704 
ITU-T G.823 
Functional Description 
In North America, DS-3 translates into T-3, which is the equivalent of 28 T-1 channels, each operating at 
1.544 Mbps. Four T-1s are multiplexed to a T-2 frame, then seven T-2 frames are multiplexed, through 
an M23 (‘Multiplex 2-to-3’ multiplexer). As each frame is transmitted 8,000 times per second, the total 
T-3 signaling rate is 44.736 Mbps.  
ETX-2i Devices 
2. Cards and Ports 
Factory Defaults 
By default, no smart SFP T3 ports exist. 
If a T3 module is inserted, the modular T3 ports have the following configuration. 
Parameter 
Value 
Remarks 
line-length  
up-to-225ft 
 
line-type  
c-bit-parity 
 
name 
T3 <slot>/<port>  
 
pm-enable 
pm-enable 
Performance monitoring is enabled 
shutdown 
shutdown 
Administratively disabled 
 
Configuring T3 Ports 
Configuring Modular T3 Ports 
 To configure modular T3 ports: 
1. If the module type is not T3, power off ETX-2i, insert the T3 module, and then power on ETX-2i. 
2. Provision the module type as T3 (see Configuring Module). 
3. At the config>port# prompt, enter: 
t3 [<slot>/]<port>/<tributary> 
The prompt config>port>t3([<slot>/]<port>/<tributary>)# is displayed. 
4. Perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
Specifying the length 
(in feet) of the T3 line  
line-length { up-to-225ft | over-225ft } 
 
Specifying type of T3 
line 
line-type { c-bit-parity } 
c-bit-parity – The c-bit parity 
framing format is an enhancement 
of the M13 application, providing 
greater management and 
performance functions. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Running loopback test 
on T3 port 
loopback { local | remote } [start 
<seconds> ] [duration <seconds>] 
local – returns the transmitted 
data at the physical layer to the 
receiving path 
remote – returns the received data 
at the physical layer to the 
transmitting path 
start – specifies the time (in 
seconds) until the loopback starts. 
Possible values: 1–3600 
duration – specifies the duration of 
the loopback (in seconds).  
Possible values: 1–3600 
If duration is not specified, the 
loopback test runs forever, until 
stopped. 
Use no loopback to disable the 
loopback test. 
Assigning a name to 
the port 
name <string> 
 
Specifying if 
performance reporting 
is enabled for the port 
pm-enable 
 
Selecting the transmit 
clock source 
tx-clock-source { loopback | internal } 
loopback – clock retrieved from 
the port's incoming (Rx) data 
internal – clock provided by 
internal oscillator 
Note: This command is relevant 
only if the module has a single T3 
port. In the case of a module with 
two T3 ports, the Tx clock source is 
configured at the VCG port level 
(see Configuring VCG Ports). 
Displaying alarms for 
port 
show alarms 
 
Administratively 
disabling or enabling 
the port 
shutdown 
Enter no shutdown to 
administratively enable the port. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
Displaying list of 
interfaces bound to 
port 
show bind 
 
Displaying loopback 
test status 
show loopback 
 
Displaying the port 
status 
show status 
 
Displaying the port 
statistics 
show statistics current 
show statistics interval 
<interval-num> 
show statistics total 
show statistics all-intervals 
show statistics all 
You can specify the scope of the 
statistics, as follows: 
current – current statistics 
interval – interval statistics 
Where  
interval-num – interval number 
Possible values: 1-96 
total – preceding 24 hours 
cumulative statistics 
all-intervals – all interval statistics 
all – all statistics 
Clearing the statistics 
clear-statistics 
 
Configuring Smart SFP T3 Ports 
 To configure smart SFP T3 ports: 
1. Provision a smart SFP port with type MiRICi-T3 or MiTOP-T3 (see Smart SFPs). 
2. Insert the MiRICi-T3/ MiTOP-T3 into the Ethernet port. 
Note 
Initialize the database of the MiTOP before inserting it into the device. Refer 
to the Setting the Switches section in the Installation and Setup chapter of the 
MiTOP E1T1 Installation and Operation manual.  
3. At the config>port# prompt, enter: 
t3 [<slot>/]<port>/<tributary> 
The prompt config>port>t3([<slot>/]<port>/<tributary>)# is displayed. 
4. Perform the required tasks according to the following table, and the type of smart SFP. 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
MiR
ICi 
MiT
OP 
Specifying the 
length (in feet) 
of the T3 line  
line-length { up-to-225ft | 
over-225ft } 
 
 
 
Specifying type 
of T3 line 
line-type { m23 | c-bit-parity | 
unframed } 
m23 – Four DS1 signals are are 
multiplexed into one DS2 signal, then 
seven DS2 signals are multiplexed into 
one DS3 signal. 
c-bit-parity – The c-bit parity framing 
format is an enhancement of the M13 
application, providing greater 
management and performance 
functions. 
unframed – No framing (relevant only for 
MiTOP). 
 
 
Running 
loopback test 
on T3 port 
loopback { local | remote } [start 
<seconds> ] [duration <seconds>] 
local – Returns the transmitted data at 
the physical layer to the receiving path 
remote – Returns the received data at 
the physical layer to the transmitting 
path 
start – Specifies the time (in seconds) 
until the loopback starts.  
Possible values: 1–3600 
duration – Specifies the duration of the 
loopback (in seconds). 
Possible values: 1–3600 
If duration is not specified, the loopback 
test runs forever, until stopped. 
Use no loopback to disable the loopback 
test. 
 
 
Assigning a 
name to the 
port 
name <string> 
 
 
 
Specifying if 
performance 
reporting is 
enabled for the 
port 
pm-enable 
 
 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
MiR
ICi 
MiT
OP 
Specifying the 
port clock 
quality 
source-clock-quality { stratum1 | 
stratum2 | stratum3 | stratum3e 
| stratum4 } 
Clock quality used in adaptive clock 
recovery set according to parameter 
specified: 
stratum1 – PRC G.811  
stratum2 – Type II G.812 
stratum3 – Type IV G.812 
stratum3e – Type III G.812 
stratum4 – Free running 
× 
 
Selecting the 
transmit clock 
source 
tx-clock-source { loopback | 
internal | pw <number> } 
loopback – clock retrieved from the 
port's incoming (Rx) data 
internal – clock provided by internal 
oscillator 
pw – clock provided by PW bundle 
Note: The pw option is available only for 
MiTOP. 
 
 
 
Administrativel
y disabling or 
enabling the 
port 
shutdown 
Enter no shutdown to administratively 
enable the port. 
 
 
Displaying list 
of interfaces 
bound to port 
show bind 
 
 
 
Displaying 
loopback test 
status 
show loopback 
 
 
 
Displaying the 
port status 
show status 
 
 
 

## 2.20 VCGs  *(p.688)*

ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Comments 
MiR
ICi 
MiT
OP 
Displaying the 
port statistics 
show statistics current 
show statistics interval 
<interval-num> 
show statistics total 
show statistics all-intervals 
show statistics all 
You can specify the scope of the 
statistics, as follows: 
current – current statistics 
interval – interval statistics 
Where  
interval-num – interval number 
Possible values: 1-96 
total – preceding 24 hours cumulative 
statistics 
all-intervals – all interval statistics 
all – all statistics 
 
 
Clearing the 
statistics 
clear-statistics 
 
 
 
2.20 VCGs 
VCG ports provide a logical link to modular E1/T1/T3 ports, if applicable.  
Applicability and Scaling 
This feature is applicable to ETX-2i with an E1/T1/T3 module. 
Standards Compliance 
ITU-T G.7042 
ITU-T G.7043 
ETX-2i Devices 
2. Cards and Ports 
Functional Description 
A VCG (Virtual Concatenation Group) logical port is used to group the E1/T1/T3 ports that are available if 
the appropriate type of module has been provisioned and inserted.  
By default, the Tx clock of the E1/T1/T3 ports in the module is the internal clock provided by the internal 
oscillator of the module. You have the option of selecting instead the loopback clock retrieved from the 
port's incoming (Rx) data, as the Tx clock of the E1/T1/T3 ports. For the ETX-2i EoPDH AIO module, you 
have yet another option of selecting the domain clock provided by the ETX-2i CSM system clock as the 
Tx clock of the E1s. 
 
Notes 
• 
The Rx clock of an E1 in an ETX-2i EoPDH AIO module can also be provided 
as a source clock to ETX-2i CSM, provided the E1 port is bound to VCG 5. 
For further information, refer to Clock Selection section in the Timing and 
Synchronization chapter. 
• 
The VCG logical port is used only if the module contains multiple E1/T1/T3 
ports, and a GFP port is then bound to the VCG port. If a module with a 
single T3 port is installed, the GFP port is bound directly to the T3 port. 
Factory Defaults 
By default, no VCG ports exist. When a VCG port is created, it is configured as shown below. 
Parameter 
Value 
Remarks 
lcas  
lcas 
LCAS enabled 
minimum-number-of-links  
1 
Minimum number of links when working with LCAS 
name 
VCG <port> 
 
shutdown 
no shutdown 
Administratively enabled 
tx-clock-source  
internal 
Clock source for transmitted data 
 
 
ETX-2i Devices 
2. Cards and Ports 
Configuring VCG Ports 
Note 
One VCG port is available in ETX-2i.  
 To configure VCG ports: 
1. At the config>port# prompt, enter 
vcg <port> 
The port is created if it does not already exist, and the config>port>vcg(<port>)# prompt is 
displayed. 
2. Perform the required tasks according to the following table. 
 
Task 
Command 
Possible Values 
Binding VCG port to E1 port 
bind e1 <slot>/<port> 
no bind e1 <slot>/<port> 
Successful only if the E1/T1 
module is installed. 
Binding VCG port to T1 port 
bind t1 <slot>/<port> 
no bind t1 <slot>/<port> 
Successful only if the E1/T1 
module is installed. 
Binding VCG port to T3 port 
bind t3 <slot>/<port> 
no bind t3 <slot>/<port> 
Successful only if the T3 module 
is installed. 
Enabling link capacity adjustment 
scheme (LCAS) 
lcas 
no lcas 
 
Enabling loop detection 
loop-detection 
no loop-detection 
Relevant only for E1/T1  ports.  
Specifying minimum number of links 
when working with LCAS 
minimum-number-of-links 
<links> 
  
Assigning a name to the port 
name <string> 
no name 
 
ETX-2i Devices 
2. Cards and Ports 
Task 
Command 
Possible Values 
Selecting the transmit clock source 
tx-clock-source {loopback | 
internal | domain <number>} 
domain – clock provided by 
ETX-2i CSM system clock. This 
option is available only for 
modular E1 ports of ETX-2i 
EoPDH AIO module. 
loopback – clock retrieved from 
the port's incoming (Rx) data 
internal – clock provided by 
internal oscillator of the 
E1/T1/T3 module  
Administratively enabling port 
no shutdown 
Entering shutdown disables the 
port. 
Displaying list of interfaces bound to the 
port 
show bind 
 
Displaying the VCG port status 
show status 
 
Examples 
 To configure VCG port 5 with module containing two E1 ports, and with system clock from ETX-2i 
CSM: 
#*****ports E1 configuration*************************** 
configure port 
e1 1/1 
no shutdown 
exit  
e1 1/2 
no shutdown 
exit all 
#*****ports GFP bind MAC configuration****************** 
configure port 
vcg 5 
bind e1 1/1 
bind e1 ½ 
tx-clock-source domain 1 
exit 
 
 

## 2.21 VDSL2 Ports  *(p.692)*

ETX-2i Devices 
2. Cards and Ports 
gfp 5 
bind vcg 5 
exit 
logical-mac 5 
bind gfp 5 
no shutdown 
exit all 
 To configure VCG port 5 with module containing two T3 ports: 
ETX-2i >config>port# vcg 5 
ETX-2i >config>port>vcg(5)$ bind t3 1/1 
ETX-2i >config>port>vcg(5)$ bind t3 1/2 
ETX-2i >config>port>vcg(5)$ no shutdown 
ETX-2i >config>port>vcg(5)$ info detail 
    Name "VCG 5 " 
    no shutdown 
bind t3 1/1 
bind t3 1/2 
    tx-clock-source internal  
    lcas  
    minimum-number-of-links 1 
ETX-2i >config>port>vcg(5)$ show bind  
Higher Layer 
--------------------------------------------------------------- 
 
Lower Layer 
-----------------s---------------------------------------------- 
T3         1               
T3         2               
2.21 VDSL2 Ports 
ETX-2i is optionally equipped with a module having four VDSL2 ports (8-wire). ETX-2i can aggregate 
traffic over the VDSL.bis links. The VDSL2 interfaces are bundled into one PCS (physical coding sublayer) 
port. See PCS Ports for commands related to the PCS port. 
Applicability and Scaling 
This feature is applicable to ETX-2i with a VDSL2 module; operates in CPE mode only. 
ETX-2i Devices 
2. Cards and Ports 
Standards Compliance 
ITU-T G.993.2, G.997.1, G.998.2 
IEEE 802.3     
Functional Description 
Very High Speed Digital Subscriber Line Transceivers 2 (VDSL2) is an access technology that enables 
delivery of very high-speed internet access over copper telephone lines – much higher than a 
conventional voice band modem can provide.  
VDSL2 main features include: 
• 
Four VDSL2 ports 
• 
One bonding group; supports up to four VDSL port(s)  
• 
Payload rate 100Mbps DL/ 50Mbps UL per line 
• 
G.998.2 VDSL2 PTM (64/65-octet encapsulation) bonding  
• 
Bonding payload rate up to 400Mbps DL/ 200Mbps UL, with packet forwarding throughput 
380Mbps DL/180Mbps UL 
• 
Supports VDSL2 profiles 8a, 8b, 8c, 8d, 12a, 12b and 17a 
• 
Operation frequency scope up to 17.7MHz 
• 
Supports ADSL2/ADSL2+ fall back in PTM mode 
• 
Comply ITU-T Rec. G.993.2 Annex A  and Annex B power spectrum mask 
• 
Supports two HW SKUs - one for POTS overlay, the other for ISDN overlay 
• 
Supports Trellis coding and reed-Solomon code  
• 
SRA (Seamless Rate Adaptation) 
• 
Bit Swap 
• 
Upstream power backoff (UPBO) 
• 
Downstream power backoff (DPBO) 
• 
RFI notch  
• 
DMT  as line coding 
• 
G.INP (impulse noise protection) 
ETX-2i Devices 
2. Cards and Ports 
• 
G.993.2 DELT  
• 
G.993.5 vectoring system for NEXT and FEXT 
• 
G.993.2 Amd 7, timing synchronization 
• 
Dying Gasp  
Configuring VDSL2 Ports 
This section explains how to configure the VDSL2 port.  
 To configure the VDSL2 port parameters 
1. Navigate to configure port vdsl2 1/<port> to select the VDSL2port to configure. 
The config>port>vdsl2(1/<port>)# prompt is displayed. 
2. Perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
Displaying port status 
show status 
See Viewing VDSL2 Port Status. 
Displaying port statistics 
show statistics 
See Viewing VDSL2 Port Statistics. 
Clearing the port statistics 
clear-statistics 
 
Assigning port name 
name <string> 
Typing no name removes the port 
name. 
Administratively enabling port 
no shutdown 
Entering shutdown disables the port. 
 
Viewing VDSL2 Port Status 
 To display the status of VDSL2 port 1: 
ETX-2i # config port vdsl2 1/1 
ETX-2i >config>port>vdsl2(1/1)# show status 
Name                                   : VDSL2-1/1 
Administrative Status                  : Up 
Operation Status                       : Up 
Transmission System                    : g9932AnnexB 
Attainable Line Rate Downstream (Kbps) : 143439 
Attainable Line Rate Upstream (Kbps)   : 62592 
ETX-2i Devices 
2. Cards and Ports 
Loop Attenuation (dB)                  : 0.2dB 
SNR Margin (dB)                        : 9.2dB 
Far-End Vendor ID                      : 26 00 52 41 44 00 00 00 
 
 Parameter 
Description 
Name 
Port name 
Administrative Status 
VDSL2 line administrative status 
Up or Down 
Operation Status 
VDSL2 line operational status 
Up or Down 
Attainable Line Rate Downstream 
[Kbps] 
The maximum downstream net data-rate currently attainable on the VDSL2 
line, in Kbps 
Valid only during VDSL2 line showtime 
Attainable Line Rate Upstream 
[Kbps] 
The maximum upstream net data-rate currently attainable on the VDSL2 
line, in Kbps 
Valid only during VDSL2 line showtime 
SNR Margin [dB] 
The average SNR margin 
Far-end Vendor ID 
VTU-C vendor ID 
Viewing VDSL2 Port Statistics 
 To display the VDSL2 port statistics: 
• 
At the config>port>vdsl2(1/<port>)# prompt, enter show statistics [{current | interval |current-
day | day} {interval-num<interval-num> | day-num<day-num>}]. 
Relevant VDSL2 statistic parameters are displayed. 
 To display the VDSL2 current interval statistics for port 1: 
ETX-2i # config port vdsl2 1/1 
ETX-2i >config>port>vdsl2(1/1)# show statistics current 
Current 
--------------------------------------------------------------- 
Time Elapsed (Sec) : 895 
Valid Intervals    : 6         Invalid Intervals  : 90 
ES                 : 0         SES                : 0 
UAS                : 0         FEC                : 2 
LOSS               : 0 
ETX-2i Devices 
2. Cards and Ports 
Parameter 
Description 
Time Elapsed 
Total elapsed seconds for current interval/day 
Monitored Time 
Total seconds for this historical interval 
Interval Validity 
Indicates if the data for this historical interval is valid 
Valid Intervals 
The number of 15-minute PM intervals for which data was collected. The 
value is typically equal to the maximum number of 15-minute intervals 
the implementation is planned to store, unless the measurement was (re-
)started recently, in which case the value is the number of complete 15-
minute intervals for which the agent has at least some data. In certain 
cases (e.g., in the case where the agent is a proxy), it is possible that some 
intervals are unavailable, in which case, this interval is the maximum 
interval number for which data is available. 
Invalid Intervals 
The number of 15-minute PM intervals for which no data is available. The 
value is typically zero, except in cases where the data for some intervals 
are not available (for example, in proxy situations). 
ES 
Number of errored seconds during this interval 
SES 
Number of severely errored seconds during this interval 
UAS 
Number of seconds in Unavailability State during this interval 
FEC 
Number of seconds with at least one FEC correction during this interval 