# 5 Cards and Ports – 5.14 Logical MAC Ports

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 337–340.*


## Applicability and Scaling  *(p.337)*


## Factory Defaults  *(p.337)*

5. Cards and Ports 
 To clear all statistics data except for from the current interval: 
1. Navigate to the corresponding entity as described above. 
2. Enter clear-statistics current-all. 
The statistics for the specified entity are cleared. 
5.14 Logical MAC Ports 
Applicability and Scaling 
To describe and map the Ethernet traffic passing over different media (E1/T1, T3, SDH/SONET, etc), the 
Megaplex-4 architecture uses a concept of Logical MAC ports. Logical MAC represents the MAC layer of 
the entity. It should be bound to a gfp, hdlc or mlppp port, which, in its turn, should be bound to the 
physical layer.   
The following table lists the possible entities that can be bound to the Logical MAC, with their 
corresponding media, protocols and possible values.  
Entities Bound to Logical MAC  
Entities 
Media  
Protocol 
Module  
Scaling/ 
Comments 
gfp 
Ethernet over 
SDH/SONET 
GFP encapsulation 
protocol 
CL.2 
1 to 32 
gfp 
Ethernet over T3 
GFP encapsulation 
protocol 
T3 
1 to 16 
 
gfp 
 
Ethernet over 
E1/T1 
GFP encapsulation 
protocol 
VS-16E1T1-EoP 
1 to 16 
hdlc 
Ethernet over 
SDH/SONET 
LAPS encapsulation 
protocol 
CL.2 
1 to 32 
Factory Defaults 
By default, the Logical MAC ports have the following configuration. 

## Configuring Logical MAC Ports  *(p.338)*

5. Cards and Ports 
For CL module: 
config>port>log-mac(cl-a/5)$ info detail 
    name  "CL-A Logical mac 05" 
    shutdown 
    egress-mtu  1790 
    queue-group profile  "LMDefaultQueueGroup" 
    tag-ethernet-type  0x8100 
For T3 module: 
config>port>log-mac(cl-a/5)$ info detail 
    name  "IO-3 Logical mac 05" 
    shutdown 
For VS-16E1T1-EoP module:  
config>port>log-mac(cl-a/5)$ info detail 
   name "IO-10 Logical mac 05" 
   shutdown 
   tag-ethernet-type 0x8100 
   egress-mtu 1790 
   queue-group profile "LMDefaultQueueGroup" 
For description of the Logical Mac default queue group profile, see Queue Group Profiles section in 
Chapter 8.  
Configuring Logical MAC Ports  
 To configure the Logical MAC port: 
1. Navigate to configure port logical-mac <slot>/<port> to select the Logical Mac entity to 
configure.  
The config>port>logical-mac>(<slot>/<port>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below.  
Task 
Command 
Comments 
Assigning short description to 
Logical MAC  
name <string>* 
Using no name removes the name 
Administratively enabling Logical 
MAC 
no shutdown* 
Using shutdown disables the Logical MAC 
Binding HDLC port to Logical MAC  
bind hdlc <slot>/<port> 
 
Ethernet over E1/T1: port=HDLC bundle  
Ethernet over SDH/SONET: port=VCG using 
LAPS encapsulation protocol  

## Viewing MAC Address  *(p.339)*

5. Cards and Ports 
Task 
Command 
Comments 
Binding GFP port to Logical MAC  
bind gfp <slot>/<port>* 
GFP port=VCG using GFP encapsulation 
protocol 
Binding MLPPP port to Logical 
MAC  
bind mlppp <slot>/<port> 
 
Enabling OAM (EFM) on the 
Logical MAC port  
efm  
See Ethernet OAM (EFM) in Chapter 8. 
no efm disables OAM (EFM)  
Setting maximum frame size  (in 
bytes) to transmit (frames above 
the specified size are discarded) 
egress-mtu <64–9600> 
 
 
Assigning queue group profile to 
Ethernet port 
queue-group <queue-
group-profile-name> 
no queue-group removes queue group 
association 
Specifying the Ethertype expected 
in Ethernet packet 
tag-ethernet-type 
<0x0000-0xFFFF> 
 
Note 
The only parameters used for configuration of logical-mac ports of T3 modules 
are marked with an asterisk (*). 
To bind a flow to a Logical MAC port, see ingress-port logical-mac command under config>flows>flow.  
Viewing MAC Address  
For viewing the MAC address used by the Logical MAC port, follow the instructions below. 
 To view the MAC address used by the Logical MAC port: 
1. Navigate to config>port> log-mac (<slot>/<port>)#  
2. Type show status. 
The status is displayed, for example as follows:  
config>port>log-mac(cl-a/1)$ show status  
MAC Address : 00-20-D2-F3-BC-D5 
Note 
For MAC address allocation mechanism, see Chapter 10. 

## Displaying Logical MAC Statistics  *(p.340)*

5. Cards and Ports 
Displaying Logical MAC Statistics 
You can display statistics for the Logical MAC ports of T3 modules.  
 To display the Logical MAC statistics: 
At the prompt config>slot>port>log-mac (<slot>/<port>)#, enter show statistics.  Logical MAC statistics 
are displayed. The counters are described in the table below. For example:  
config>port>log-mac(9/1)# show statistics 
Running 
----------------------------------------------------------------- 
Counter          Rx                   Tx 
Total Frames     23785                23789 
Total Octets     2473744              2473952 
Total Frames/Sec 914                  914 
Total Bits/Sec   761152               761216 
Minimum Bits/Sec 0                    0 
Maximum Bits/Sec 761152               0 
Unicast Frames   23786                23788 
Multicast Frames 0                    0 
Broadcast Frames 0                    0 
Error Frames     0 
64 Octets        0                    0 
65-127 Octets    23784                23784 
128-255 Octets   0                    0 
256-511 Octets   0                    0 
512-1023 Octets  0                    0 
1024-1518 Octets 0                    0 
1519-2047 Octets 0                    0  
2048-Max Octets  0                    0 
Logical MAC Statistics Parameters 
Parameter 
Description 
Total Frames Rx/Tx 
Total number of frames received/transmitted 
Total Octets Rx/Tx 
Total number of bytes received/transmitted 
Unicast Frames Rx/Tx 
Total number of unicast frames received/transmitted 
Multicast Frames Rx 
Total number of multicast frames received/transmitted 
Broadcast Frames Rx 
Total number of broadcast frames received/transmitted 
Total Frames/Sec Rx/Tx 
Number of frames received/transmitted per second 
Total Bits/Sec Rx/Tx 
Number of bits received/transmitted per second 
Minimum Bits/Sec Rx/Tx 
Minimum number of bits received/transmitted per second 