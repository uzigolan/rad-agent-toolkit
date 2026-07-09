# Feature Reference – 5 Traffic Processing – 5.12 Virtual Router Redundancy Protocol (VRRP)

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1139–1148.*


## Testing OSPF  *(p.1139)*


## Standards Compliance and MIBs  *(p.1139)*

ETX-2i Devices 
5. Traffic Processing 
Testing OSPF 
After configuring OSPF on a router in an existing OSPF environment, you should test that OSPF is 
working properly.  
 To test OSPF: 
1. Wait a few seconds after configuration for OSPF communications to take place. 
2. Navigate to the CLI router OSPF context (config>router(<router_number>)> 
ospf#). 
3. Enter show interface-table and check that a DR and a BDR have been successfully elected. 
4. Enter show neighbor-table and check that connections have been established with all 
neighbors. 
5. Enter show routing-table and check that expected routes have been learned from OSPF 
neighbors. 
6. Exit the OSPF context, to the router CLI context. 
7. Enter show routing-table and check that there are new routes marked as originating in OSPF. 
 
5.12 Virtual Router Redundancy Protocol (VRRP) 
Virtual Router Redundancy Protocol (VRRP) enables a group of routers to act as a virtual router with a 
virtual IP address that can be configured as the default gateway for access devices in a LAN.  
A static default gateway router is a potential single point of failure, which is eliminated by VRRP; it 
increases the availability and reliability of routing paths without the need for dynamic routing or router 
discovery protocols on every access device. 
Standards Compliance and MIBs 
The VRRP feature complies with the following standards. 
Standard 
Title 
RFC 1071 
Computing the Internet Checksum 
RFC 2460 
Internet Protocol, Version 6 (IPv6) Specification 

## Functional Description  *(p.1140)*

ETX-2i Devices 
5. Traffic Processing 
Standard 
Title 
RFC 3768 
Virtual Router Redundancy Protocol (VRRP) 
RFC 5798 
Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6 
RFC 6527 
Definitions of Managed Objects for the Virtual Router Redundancy Protocol Version 3 
(VRRPv3) 
ETX-2i can support either of the following VRRP versions at any time: 
• 
VRRPv2 (RFC 3768) – supports only IPv4 
• 
VRRPv3 (RFC 5798) – supports IPv4 and IPv6 
The two versions cannot interwork together. 
Functional Description 
VRRP Group 
A VRRP group is defined as a group of routers that share one or more virtual IP addresses. If a router’s 
physical IP address matches a virtual IP address, it is referred to as the address owner. The routers in the 
group are assigned priorities ranging from 1–255, with 255 being the highest priority, however only 
priorities 1–254 are configurable. Priority 255 is automatically assigned to the address owner regardless 
of the configured priority. Up to 20 VRRP groups are supported per device. 
Master Router 
At any time, one of the routers is the master (active) and the others are backups. The router with the 
highest priority is selected as the master, therefore the address owner is the master unless it has failed. 
If more than one router has the highest priority, the one with the highest primary IP address is selected 
as master. The primary IP address is one of the router interface’s real (IPv4) or link-local (IPv6) IP 
addresses. It is used as the source address in VRRP advertisements 
The master router forwards upstream traffic packets destined for the virtual IP address(es) and sends 
periodic advertisements to the backup routers at a user-configurable interval. If a backup router does 
not receive an advertisement for a set period, the backup router with the next highest priority takes 
over as master.  

## Factory Defaults  *(p.1141)*

ETX-2i Devices 
5. Traffic Processing 
Preemption 
If preemption is enabled, then when a new router is added to a VRRP group and its priority is higher 
than any of the routers in the group, it preempts the master role. When a router with priority 255 
(address owner) is added to a VRRP group or becomes active, it preempts all lower-priority routers, even 
if preemption is disabled. If no router has priority 255 and preemption is disabled, then no preemption 
occurs. 
Fault Propagation 
If the VRRP master router’s uplink toward the network fails, it does not affect the VRRP state if VRRP is 
running on an Ethernet port connected to the user network; however, the master might not be able to 
forward packets, or might delay the packet forwarding by using an alternative route.  
To solve this, the status of an interface can be used as a fault propagation trigger, with the configured 
action of lowering the VRRP priority, in order to cause a backup router to become the master. This VRRP 
redundancy is supported within 50 ms from the start of switchover. When the interface recovers, the 
original priority is restored. 
Note 
In order for fault propagation to interact properly with a VRRP group, 
preemption must be enabled on all VRFs belonging to that group, and all the 
VRFs must not be address owners. 
Load Balancing 
The VRRP backup virtual routers do not forward traffic incoming from the LAN unless they become the 
master router. It would be advantageous to have multiple routers forwarding the traffic instead of one 
being the active master, and the rest idle backups. To achieve this, multiple VRRP groups (up to 255, 2) 
can be configured for a router interface, with each router acting as the master of a different virtual IP 
address.  
Each virtual address can then be configured as default gateway for some of the devices on the LAN, and 
each router handles the traffic of the devices for which it is the default gateway. If a router fails, one of 
the other routers transitions to master, and handles the failed router’s traffic. 
Factory Defaults 
The default device VRRP version is 2. 
By default, no VRRP groups exist. When a VRRP group is created, its default configuration is the 
following: 

## Configuring VRRP  *(p.1142)*

ETX-2i Devices 
5. Traffic Processing 
Parameter 
Default  
Remarks 
description 
 
virtual router <ip-ver> group <id> 
• <ip-ver> is either IPv4 or IPv6. 
• <id> is the group VRID. 
preempt 
Preempt 
Preemption is enabled by default. 
priority 
100 
 
shutdown 
shutdown  
VRRP is disabled by default; at least one 
virtual IP address must be associated with 
the group before the group can be 
enabled. 
timer-advertise 
VRRP v2: 1 second 
VRRP v3: 100 centiseconds 
 
Configuring VRRP 
VRRP is configured at the following levels: 
• 
System> router – Configure device VRRP version.  
• 
Router interface – Configure VRRP group parameters. 
Configuring VRRP Version 
You can configure the VRRP version at the system > router level. 
 To configure the device VRRP version: 
• 
At the config>system>router# prompt, enter the following command to specify VRRP version 2 
or 3: 
vrrp-version {2 | 3} 
Note 
See Viewing VRRP Summary for details on displaying VRRP group summary 
information at various levels 
Configuring VRRP Group Parameters 
You configure VRRP group parameters at the router interface level. 
ETX-2i Devices 
5. Traffic Processing 
Note 
A VRRP group cannot be associated with a router interface for which any of 
the following is true: 
• 
DHCP is enabled for the router interface. 
• 
The router interface is bound to a PPP port. 
• 
The router interface is a loopback interface. 
 To configure VRRP group parameters: 
1. At the config>router(<number>)>interface(<interface-num>)# prompt, enter the following, 
specifying the VRRP group ID (1–255) and IP version: 
vrrp <vrid> [{ipv4 | ipv6}] 
One of the following prompts is displayed, depending on the IP version entered: 
config>router(<number>)>interface(<interface-num>)>vrrp(<vrid>,ipv4)# 
config>router(<number>)>interface(<interface-num>)>vrrp(<vrid>,ipv6)# 
2. Perform the required tasks according to the following table. 
Note 
The commands ip and no shutdown are mandatory for VRRP group 
configuration. The other commands are optional; if they are not specified, 
then default values are used (see Factory Defaults). 
 
Task 
Command 
Comments 
Configuring VRRP group 
description 
description <string> 
Enter no description to use an 
empty (NULL) string. 
Associating a virtual IP address 
with the VRRP group 
ip <ip-address> 
Enter no ip <ip-address> to 
delete the association with the IP 
address. 
The IP address must be in the 
correct form for the configured IP 
version. 
Enabling preemption 
preempt 
Enter no preempt to disable 
preemption. 
Configuring VRRP priority 
priority <number> 
Possible values for number:  
1–254 

## Configuration Errors  *(p.1144)*

ETX-2i Devices 
5. Traffic Processing 
Task 
Command 
Comments 
Configuring interval for VRRP 
master router advertisements 
timer-advertise <number> 
[centiseconds] 
• If centiseconds is not entered, 
the range for <number> is 1–
40 seconds. 
• If centiseconds is entered, the 
range for <number> is 10–
4000 centiseconds. 
If the centiseconds parameter 
is entered when ETX-2i is 
working in VRRPv2, then the 
entered value is stored, but if 
it is not a multiple of 100, 
then ETX-2i uses a value that 
is rounded up to the next 
multiple of 100, e.g., for 
timer-advertise 201 
centiseconds, ETX-2i uses 
three seconds for the timer. 
When the configuration is 
displayed via the info 
command, the centiseconds 
keyword is displayed only if 
the device is working in 
VRRPv3 and the configured 
interval value in centiseconds 
is not a multiple of 100.  
Viewing VRRP status 
show status 
Refer to Viewing VRRP Status for 
additional information. 
Administratively enabling or 
disabling VRRP for router 
interface 
no shutdown 
• Enter shutdown to 
administratively disable VRRP. 
• VRRP can be enabled only if at 
least one virtual IP address 
has been associated. 
 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
ETX-2i Devices 
5. Traffic Processing 
Message 
Cause 
Corrective Action 
Too many VRRP groups on this 
interface 
You tried to create a VRRP 
group for a router interface for 
which the maximum number of 
groups already exists. 
Delete one of the VRRP groups from the 
interface. 
VRRP and DHCP not allowed on 
the same interface 
You tried to create a VRRP 
group for a router interface for 
which DHCP is enabled. 
Disable DHCP for the interface. 
VRRP cannot be configured on 
PPP 
You tried to create a VRRP 
group for a router interface 
that is bound to a PPP port. 
Remove the PPP port association from 
the interface. 
VRRP cannot be configured on a 
loopback router interface 
You tried to create a VRRP 
group for a router interface 
that is a loopback router 
interface. 
Create the VRRP group for a different 
router interface. 
Too many addresses associated 
with VRRP group  
You tried to associate an IP 
address with a VRRP group for 
which the maximum number of 
supported addresses is already 
associated. 
Delete one of the associated addresses 
before associating a new IP address with 
the group. 
Incorrect IP version 
You tried to associate an IPv4 
address with an IPv6 group or 
an IPv6 address with an IPv4 
group.  
Associate an IPv4 address with an IPv4 
group, or an IPv6 address with an IPv6 
group. 
Active VRRP group must have 
virtual IP 
You tried to dissociate the last 
IP address from an enabled 
VRRP group. 
Associate a virtual IP address with the 
VRRP group or disable the group. 
Cannot activate VRRP group 
without virtual IP address 
You tried to administratively 
enable a VRRP group that does 
not have at least one 
associated virtual IP address. 
Associate a virtual IP address with the 
VRRP group. 
VRRP priority preemption must 
be enabled for fault propagation 
You tried to disable preemption 
on a VRRP group that is defined 
in fault propagation as a 
to-element. 
Remove the fault propagation 
configuration. 

## Viewing VRRP Status  *(p.1146)*

ETX-2i Devices 
5. Traffic Processing 
Message 
Cause 
Corrective Action 
Priority decrement fault 
propagation banned on VRRP 
address owner 
You tried to configure one of 
the following: 
• Fault propagation 
to-element virtual IP 
address as the to-element 
IP address 
• Fault propagation 
to-element IP address as 
the to-element virtual IP 
address. 
Either configure the to-element with a 
different IP address that is not a virtual 
IP address or use a virtual address that is 
not a real address of the to-element. 
 
Viewing VRRP Status 
You can view VRRP status by using the show status command. This command is available in one of the 
following CLI contexts, depending on the IP version of the VRRP group:  
config>router(<number>)>interface(<interface-num>)>vrrp(<vrid>,ipv4)# 
config>router(<number>)>interface(<interface-num>)>vrrp(<vrid>,ipv6)# 
For example: 
ETX-2# configure router(1)>interface(7)>vrrp(1,ipv4)# show status 
Router/Interface                 : 1/7 
  Physical Port                  : Ethernet 1/2 
VRRP Group                       : 1 (IPv4)                   
  Administrative Status          : Enabled 
  Operational Status             : Master 
  Uptime (seconds)               : 1111 
Primary IP Address               : 10.20.0.01/24 
Protected IP Address             : 10.20.0.01/24 
                                 : 10.20.0.10/24 
Virtual MAC Address              : 00:00:5e:00:01:01 
Advertisement Interval (seconds) : 1 
Preemption                       : Enabled     
Priority                         : 254 
  Reduced By Fault Propagation to: 253 
  From Interface                 : Router Interface ½ 
 
 
ETX-2i Devices 
5. Traffic Processing 
Field 
Description 
Router/Interface 
Router and interface where the VRRP group is configured 
Physical Port 
Physical interface that is bound to the router interface 
VRRP Group 
VRRP group ID 
Administrative Status 
VRRP group administrative status – Disabled or Enabled 
Operational Status 
VRRP role: 
• Backup – Router interface is acting as backup. 
• Master – Router interface is acting as master. 
• Init – Router interface VRRP group parameters are being initialized. 
• Lower Layer Down – The interface with which the group is associated is 
non-operational. 
An event (protocol_state_change) with a new trap (vrrpProtocolStateChange) is 
triggered when the operational status changes from ‘Master’ to ‘Backup’ or vice 
versa. 
Uptime (seconds) 
Time since VRRP role changed from Init to Backup or Master 
Primary IP Address 
Primary IP address and mask of the VRRP group 
Protected IP Address 
One or more virtual IP address(es) protected by the VRRP group; one output line is 
displayed for each protected IP address. 
Virtual MAC Address 
Virtual MAC address of the VRRP group 
Advertisement Interval 
(seconds) 
Interval between VRRP advertisements (if the router is acting as master) 
Preemption 
Preemption state – Disabled or Enabled 
Priority 
Router VRRP priority (0–255) 
Reduced By Fault 
Propagation to 
Router VRRP actual priority, after being reduced by fault propagation if applicable 
From Interface 
Faulted interface that triggered priority decrease 
 
 
 

## Viewing VRRP Summary  *(p.1148)*

ETX-2i Devices 
5. Traffic Processing 
Viewing VRRP Summary 
You can view a VRRP group summary by using the show vrrp-summary command for router, or show 
summary-vrrp command for router interface. This command is available in the following CLI contexts: 
• 
config>system>router – displays information for all VRRP groups in the device 
• 
config>router(<number>) – displays information for all VRRP groups configured for any router 
interfaces belonging to the router 
• 
config>router(<number>)>interface – displays information for all VRRP groups configured for 
the router interface 
For example: 
ETX-2i# configure router(1)>interface(1)# show summary-vrrp 
Rtr If Phys If       Group     Pri Own Pre State  Primary Address  
1/1    Ethernet 1/2  111(IPv4) 100 Yes Ena Master 10.10.10.10 
1/1    Ethernet 1/2  222(IPv6) 200 --  Dis Backup FE80::1234 
 
Field 
Description 
Rtr 
Router and interface where the VRRP group is configured 
Phys If 
Physical interface that is bound to the router interface 
Group 
VRRP group ID 
Pri 
Router VRRP priority (0–255) 
Own 
Indicates if VRRP group is address owner: Yes or -- 
Pre 
Preemption state – Dis or Ena 
State 
VRRP role: 
• Backup – Router interface is acting as backup. 
• Master – Router interface is acting as master. 
• Init – Router interface VRRP group parameters are being initialized. 
• LLD – The router interface where the VRRP group is configured, is not 
operational. 
Primary Address 
Primary IP address of the VRRP group 
 