# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 6.5 Router Interface

*Manual `MiNID_ver_2_6_mn.pdf`, pages 124–133.*


## Functional Description  *(p.124)*

6. Management and Security 
6.5 Router Interface 
MiNID supports up to five router interfaces. 
Management traffic is transmitted via the router interface number 1 based on the configured IP address, 
static route and mask. 
The router interface can be set with VLAN parameters, which will be added as a VLAN tag to the traffic 
transmitted via this interface. 
Note 
If VLAN is not configured, traffic is transmitted untagged. 
Functional Description 
You can define the IP address as: 
• 
DHCP – MiNID receives its IP address from a DHCP server for management router interface 
Note 
If DHCP is enabled, option 61 (client identifier) is supported by sending the 
device MAC address to the DHCP server. 
• 
Static – A specific IP address is configured for MiNID that is used for all types of access 
• 
Loaned IP – MiNID uses the IP address of the host device. When packets arrive at MiNID, the 
packets are forwarded to the host device or are processed by MiNID, depending on the packet 
TCP/UDP port number (see Management Access Control for details).  
The loaned IP feature allows a network management system such as RADview to communicate 
with MiNID and the MiNID host device by sending management packets to the same IP address 
but with different TCP/UDP port values, according to which packets should be processed by 
MiNID and which should be forwarded to its host device. 
Note 
If loaned IP address is enabled, TWAMP, Packet Capture and L3SAT 
configurations based on Router Interface # 1 cannot be enabled. However, 
TWAMP, Packet Capture and L3SAT configurations based on another router 
interface can be successfully enabled. 
 
Note 
For loaned IP configuration having EtherType other than 0x8100, the 
EtherType should be defined specifically by config flows tpid-outer-vlan 
command. 
 

## Factory Defaults  *(p.125)*


## Configuring Router Interface  *(p.125)*

6. Management and Security 
 
 
Factory Defaults 
 IP address is statically configured to 192.168.205.1. 
No management VLAN is configured. 
By default, only the router interface #1, which includes additional functionality for host management, is 
defined. No additional router interface is defined. 
By default, IPv6 address is disabled. 
Configuring Router Interface 
 To configure a router interface using the web interface: 
1. Navigate to Configuration > Router > Interface. 
 
 
 
  
 
 
 
 
Configuration – Router - Interface 
 
 
 
Add new Interface 
 
 
 
ID 
Admin Status 
Interface IP 
 
 
 
 
 
1 
Enabled 
192.168.205.1/24 
Delete Interface 
 
 
 
 
 
Configuring a Router Interface 
1. To add a new router interface: 
 
Click Add new Interface. 
6. Management and Security 
 
 
 
 
 
Configuration – Router – Interface - New Interface 
 
 
 
 
Admin Status 
Disable 
 
 
Interface ID 
2 
 
 
IPv4 Address 
0.0.0.0 
 
 
Network Mask 
0.0.0.0 
 
 
Interface Vlan 
Untagged 
 
 
Port 
Port 1 
 
 
 
 
Apply 
 
 
 
 
 
New Router Interface 
 
Fill in the parameters as specified in the following table. 
 
Click <Apply> to create the router interface. 
The Configuration>Router>Interface screen (see above) appears, with an entry containing the 
new router interface. 
1. To delete a router interface, click Delete Interface in the corresponding row. 
The router interface is deleted. 
2. Click <Save Configuration>. 
 To configure a router interface using the CLI: 
1. Navigate to configure router interface <number>. 
The config>router>interface<number>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Router Interface Parameters 
Task 
Command 
Comments 
Assigning an IP address to the 
router interface 
address <ip-address/mask> 
The controller should have the same IP 
address as in the router interface 
Associating router interface 
with VLAN 
[no] vlan <vlan-id> pbit <p-bit> [inner-bit 
<vlan-id> inner-pbit <p-bit>] 
 

## Configuring Router Interface for Management  *(p.127)*

6. Management and Security 
Task 
Command 
Comments 
Binding router to Ethernet port  
bind ethernet <1|2> or <SFP|MSA> 
For Router Interfaces 2-5, you can bind 
the router to either SFP or MSA port. 
For Router Interface 1, you can bind the 
router to both. 
Administratively enabling or 
disabling the router 
[no] shutdown 
Enter shutdown to administratively 
disable the router 
 To disable a router interface: 
1. Go to configure router interface <number>. 
2. Type shutdown. 
Configuring Router Interface for Management 
 To configure the router interface in the web interface: 
1. Navigate to the Configuration > Router > Interface. 
2. Click 1 in the row of the default router interface to change its parameters.  
6. Management and Security 
 
 Configuration – Router – Interface - Update Management Interface 
  
 
 
 IPv4 Configuration: 
 
 
 IP addressing mode 
Static IP 
 
 IP Address 
192.168.205.1 
 
 Network Mask 
255.255.255.0 
 
  
 
 
 IPv6 Configuration: 
 
 
 Static Address 
Disable 
 
 Autoconfig 
Disable 
 
 DHCPv6-Client 
Disable 
 
  
 
 
 General Configuration: 
 
 
 Bind 
Both 
 
 Host VLAN 
Untagged 
 
  
 
 
 Apply  
 
 
  
 
 
Management Router Interface Configuration 
1. Enter all necessary commands according to the tasks listed in the table below. 
2. Click <Apply>. 
 To configure the router interface for management in the CLI: 
Do one of the following: 
1. Use a unified command: 
a. Go to the config>router level. 
b. Enter management configuration parameters: 
management-cfg {router-interface} <ri-number> {address} <ri-ip-address-mask> [vlan 
<value> pbit <value> [inner-vlan <value> inner-pbit <value>]] {static-route} <dest-subnet> 
{address} <next-hop ip address> 
2. Use a set of commands according to the tasks listed below. 
6. Management and Security 
Router Interface for Management 
Task 
Command 
Comments 
Configuring the IP address, 
if DHCP is not enabled 
[no] address <ip-address/mask> 
Specify the mask in CIDR notation, which 
means that it is a decimal number that 
specifies the number of high-order 
consecutive bits set to 1 in the mask. For 
example, the CIDR notation for mask 
255.255.255.0, is 24. 
For router interface #1, the IP address can 
have IPv4 (e.g. 10.10.10.1) or IPv6 format 
(e.g. 10:10:10:10:10:10:10:10). 
• Note: Only IPv6 address can be deleted 
by entering no address in the router 
interface # 1. 
Binding router to Ethernet 
port 
bind ethernet {1} {2} 
 
Enabling or disabling DHCP 
[no] dhcp 
Use the no form to disable the mode (for 
management interface) 
You cannot enable DHCP (for IPv4) in the 
following cases: 
• Router interface is bound to a PPP 
port. 
• IPv4 address is configured. 
• Router interface is not unnumbered. 
DHCPv6 is enabled. 
Enabling or disabling 
DHCPv6 client for the router 
interface 
[no] dhcpv6-client 
You can enable DHCPv6 client provided 
that the following conditions exist: 
• Router entity is Router # 1. 
• There is no other DHCPv6 client 
defined in the device. 
DHCPv4 is not enabled. 
Enabling or disabling IPv6 
autoconfiguration on the 
router interface 
[no] ipv6-autoconfig  
Enter no ipv6-autoconfig to disable IPv6 
autoconfiguration. 
Enabling or disabling loaned 
IP address mode 
[no] loaned-ip 
Use the no form to disable the mode. 
If loaned IP address is enabled, then DHCP 
cannot be enabled. 

## Configuring Static Route  *(p.130)*

6. Management and Security 
Task 
Command 
Comments 
Displaying router interface 
status 
show status 
See Viewing Router Interface Status 
Creating a management 
traffic VLAN by configuring 
the management VLAN ID 
and specifying its priority by 
setting the VLAN p-bits 
[no] vlan <vlan-id> pbit <p-bit> 
[inner-vlan <vlan-id> inner-pbit <p-
bit>] 
Possible values for pbit: 0–7 
 
Note 
IPv6 autoconfiguration must be enabled before you start configuring static 
address and DHCPv6 client. 
 
Note 
Router Interface parameters cannot be changed if the interface is used for 
configuring TWAMP, Packet Capture, or L3SAT parameters. 
Configuring Static Route 
 To configure the static route in the web interface: 
1. Navigate to Configuration > Router > Static Route. 
2. Click Add new Static Route. 
 
 Configuration – Router - Static Route - New Static Route 
  
 
 
 IP Address 
0.0.0.0 
 
 Subnet Mask 
0.0.0.0 
 
 Next Hop Address 
0.0.0.0 
 
 Apply  
 
 
  
 
 
1. Set the parameters and click <Apply>. 
 To configure the static route in the CLI: 
1. Go to the config>router level. 

## Configuring Default Gateway  *(p.131)*

6. Management and Security 
2. Type static-route <ip-address/mask> address <next-hop-ip-address>.  
You can define two separate entities for IPv4 and IPv6 default gateway. 
Configuring Default Gateway 
The default gateway can be configured, if DHCP is not enabled. You can set two separate entries: one for 
IPv4 address and another for IPv6 address. 
 To configure the default gateway in the web interface: 
1. Navigate to Configuration > Router > Static Route. 
MiNID 
 Configuration – Router - Static Route 
  
 
 
 Add new Static Route 
 
 
  
 
 
 
Static Route IP 
Network 
Mask 
Next Hop IP 
 
 
 
0.0.0.0/0 
0 
0.0.0.0 
Delete Static 
Route 
 
 
::/0 
0 
:: 
Delete Static 
Route 
 
  
 
 
1. In the Next Hop IP column, click the 0.0.0.0 entry to edit the IPv4 default gateway, or the :: 
entry, to edit the IPv6 default router. 
2. Enter the default gateway address and click Apply. 
 To configure the default gateway in the CLI: 
1. Go to the config>router level. 
2. For IPv4 default gateway, type static-route 0.0.0.0/0 address <next-hop-ip-address>. 
For IPv6 default router, type static-route 0::0/0 address <next-hop-ip-address>. 

## Viewing the Configured Router Interface Parameters  *(p.132)*


## Viewing Router Interface Status  *(p.132)*

6. Management and Security 
Viewing the Configured Router Interface Parameters 
 To view the configured router interface parameters in the web interface: 
1. Navigate to Configuration > Router > Interface. 
2. In the row of the router interface 1, click 1. 
The router interface parameters are displayed. 
 To view the configured router interface parameters in the CLI: 
1. Go to the config>router level. 
2. Type info. 
interface 1 
 
ipv6-autoconfig 
 
address 192.168.205.11/24 
 
no vlan 
 
bind ethernet sfp msa 
 
no dhcp 
 
no loaned-ip 
 
no dhcpv6-client 
exit 
static-route 0.0.0.0/0 address 192.168.205.11 
static-route 0::0/0 address :: 
Viewing Router Interface Status 
You can view the router interface status by using the show status command:  
config>router>interface(<interface-num>)>show status. 
 To display the router interface status in the web interface: 
1. Navigate to Configuration > Router > Interface and click the interface row in the table. 
 To display the router interface status in the CLI: 
MiNID>config>router>interface(1)# show status 
Admin: up           Oper: Up 
IP Addresses: 
  101.101.101.1/24                            (manual)            (preferred) 
  1234:1234:1234:1234:1234:1234:1234:1234/126 (auto-configuration)(preferred) 
  FE80::220:D2FF:FE12:3456/64                 (link layer)        (preferred) 
 
IPv4 Default Router:  1.1.1.254 
IPv6 Default Router:  FE80::2AC7:CEFF:FEF4:68C4 
6. Management and Security 
The above fields are: 
Router Interface Status Parameters 
Field 
Description 
Admin 
Administrative status: 
• up – ready to pass packets 
• down  
Oper 
Operational status: 
• up – ready to pass packets 
• down  
IP Addresses 
IP Address/prefix 
length 
IPv4 or IPv6 address and prefix length  
Note: Supported for DHCPv6 
origin 
Origin of the IP address. 
Possible origins are:  
• other 
• manual 
• DHCP 
• link layer 
• random 
status 
Status of the IP address. 
Available statuses (from the IPv6 Stateless Address Autoconfiguration 
protocol) are: 
• preferred (default) 
• deprecated 
• invalid 
• inaccessible 
• unknown 
• tentative 
• duplicate 
• optimistic 
IPv4 Default Router 
IP address of the IPv4 default router 
IPv6 Default Router 
IP address of the IPv6 default router 