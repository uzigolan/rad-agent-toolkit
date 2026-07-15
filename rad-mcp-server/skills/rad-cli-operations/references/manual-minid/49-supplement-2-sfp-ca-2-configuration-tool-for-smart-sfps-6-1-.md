# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 6.1 Access Control List

*Manual `MiNID_ver_2_6_mn.pdf`, pages 101–103.*


## Applicability and Scaling  *(p.101)*


## Standards Compliance  *(p.101)*


## Benefits  *(p.101)*


## Functional Description  *(p.101)*

6 Management and Security 
6.1 Access Control List 
Access control lists are used to flexibly filter incoming management traffic by the source IP address. 
Applicability and Scaling 
A single access group list can be configured per device. 
Standards Compliance 
Relevant sections of RFC 1812. 
Benefits 
The service providers use the ACLs to maintain the network security by preventing the malicious traffic 
from entering the device. The ACLs can be used to save the network resources by dropping the 
unwanted packets.  
Functional Description 
Devices featuring ACLs can flexibly filter management traffic, by denying or permitting IP packets to 
enter or exit entities in the device, according to the packet’s IP address and mask. 
ACL entries are sequentially numbered rules containing statements (Deny or Permit). 
Packets are permitted or denied access, based on the following conditions: 
• 
IP source 

## Factory Defaults  *(p.102)*


## Configuring ACL Using the Web Interface  *(p.102)*

6. Management and Security 
• 
Mask 
For the ACL to take effect, it must be enabled using the configure access-control command in CLI or via 
Configuration>System> Management>Access Control page in the web interface. 
When ACL is enabled, by default, MiNID denies any management packet, unless there is a matching rule 
that permits the source IP address of the packet. 
Note 
• 
Working with ACL and IPv6, you must create a permit rule for the Link 
Local IP in addition to the Global IP address. 
• 
You have to add rules to permit IP addresses of any server that 
communicates with MiNID (RADview, NTP, etc.) for proper operation, 
otherwise the traffic from these servers will be blocked by ACL. 
Factory Defaults 
By default, no access list is defined on the MiNID. 
Configuring ACL Using the Web Interface 
 To configure ACL: 
1. Navigate to Configuration > System > Management > Access Control. 
2. In the New ACL Name field, type the ACL name. 
MiNID 
  
 
 
 Configuration – System – Management – Access Control 
  
 
 
 New ACL Name 
 
AccesMng 
  
 
 
 Apply 
 
 
  
 
 
 ACL Name 
 
 
  
 
  
3. Click <Apply>. 

## Configuring ACL Using the CLI  *(p.103)*

6. Management and Security 
4. In the table, click the ACL name to configure the list. 
The ACL Configuration page opens. 
 MiNID 
  
 
 
 Configuration – System – Management – Access Control – Config 
ACL AccessMng 
  
 
 
 Action Permit IP-net 
0.0.0.0. /32 
Sequence 10 
Add 
 
  
 
 
 Access list records 
 
 
 Sequence # 
Action 
IP net 
 
  
 
 
 Activate 
Disable 
 
  
 
 
 Apply 
 
 
  
 
 
 
5. Create the access list: 
a. Select the desired action: Deny/Permit. 
b. In the IP-net field, type the IP address and mask (the default mask is 32). 
c. Click <Add>. 
The item is added to the Access list records table. 
6. In the Activate field, select Enable to activate the ACL.  
7. Click <Apply>. 
Configuring ACL Using the CLI 
The ACL configuration tasks are performed at the access control and management levels. 
 To configure ACL: 
1. Configure the ACL using the commands listed in the table below: 
Task 
Command 
Comments 
Create ACL name 
access-list <acl-name> 
 