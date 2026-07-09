# Installation and Operation – 4 Configuration and Management Methods

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 229–294.*


## (chapter introduction)  *(p.229)*

4 Configuration and Management 
Methods 
By default, an ETX-2i device comes preconfigured to handle management traffic on an out-of-band 
interface.  
You can configure any other required functions on ETX-2i and manage a device, using the following 
methods described in this chapter:  
• 
Push button – for setting unit to its default configuration  
• 
Terminal 
• 
ShelfView GUI 
• 
RADview 
• 
Third-party SNMP-based network management systems (NMS) 
Usually, initial configuration of the management parameters is performed via an ASCII terminal. Once 
the management flows and corresponding router interface have been configured, it is possible to access 
ETX-2i via Telnet (IPv4 only), NETCONF, or SNMP for operation configuration. See Preconfiguring ETX-2i 
for SNMP Management for an example of management configuration. For details on configuring the 
router, refer to the Router section in the Traffic Processing chapter. 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
The following table summarizes management options for ETX-2i. 
Port 
Manager 
Location 
Transport Method 
Management 
Protocol 
Application 
CONTROL 
Local 
Out-of-band 
RS-232 
Terminal emulation applications such 
as HyperTerminal, ProComm, Putty, 
SecureCRT, Tera Term (see Working 
with Terminal below) 
MNG-ETH 
Local, remote 
Out-of-band 
Telnet (IPv4 
only), SSH 
Terminal emulation application (see 
Working with Telnet and Working 
with SSH below) 
NETCONF 
Third-party NETCONF client 
See 
NETCONF-Based Network 
Management below. 
SNMP 
RADview (see Working with 
RADview below) 
Third-party NMS (see Working with 
other SNMP-Based NMS below) 
Ethernet 
FE/GbE/ 
10GbE 
Local, remote 
Inband 
Telnet (IPv4 
only), SSH 
RADview (see Working with 
RADview below) 
Terminal emulation application (see 
Working with Telnet and Working 
with SSH below) 
NETCONF 
Third-party NETCONF client 
See  
NETCONF-Based Network 
Management below. 
SNMP 
Third-party NMS (see Working with 
other SNMP-Based NMS below) 
 
Notes 
• 
By default, the terminal, Telnet (SSH), NETCONF, and SNMP management 
access methods are enabled. See  
• 
Configuring Management Access for details on how to enable/disable a 
particular method.  
• 
To prevent conflicts and ensure a stable and consistent network setup, use 
either RADview Service Manager, NETCONF or CLI, but not multiple 
management methods simultaneously. 

## 4.1 Management Access  *(p.231)*

ETX-2i Devices 
4. Configuration and Management Methods 
4.1 Management Access 
You can enable or disable access to the ETX-2i management system via Telnet (IPv4 only), SSH, 
NETCONF, or SNMP applications. By disabling Telnet, SSH, NETCONF, or SNMP, you prevent 
unauthorized access to the system when security of the ETX-2i IP address has been compromised. When 
Telnet, SSH, NETCONF, and SNMP are disabled, ETX-2i can be managed via an ASCII terminal only. 
Additionally, you can enable or disable file transfer via SFTP/TFTP. 
 
Note 
This section describes how you can control and limit management access to 
the device by configuring the management access methods. You can also set 
the management access methods via ACL configuration (refer to Access 
Control List (ACL) in the Management and Security chapter).  
Applicability and Scaling 
This feature is applicable to all ETX-2i products and to PMC in ETX-2i.  
It is now possible to limit the SSH key exchange to strong algorithms (version 6.8.2 (0.75)). 
Factory Defaults 
By default, access is enabled for all the applications. 
In the default factory configuration, ETX-2i allows management from the OOB management port.  
The default factory configuration includes the following:  
• 
Allows untagged management access from the OOB port  
• 
Default IP address of the Router Interface is 169.254.1.1/16 
• 
No default Gateway configuration 
• 
Allows local management access using a PC to an ‘out of the box’ ETX-2i device: 
 
When PC uses DHCP, access to ETX-2i device is automatically established (PC address 
defaults to 169.254.x.y as no DHCP server  Microsoft protocol). 
• 
Includes flows to and from an SVI Router and a Router Interface with a fixed and set IP address 
• 
SVI, RI, and flow are assigned with indexes at the end of the device range and reserved flow 
names (to coexist with existing scripts). 
ETX-2i Devices 
4. Configuration and Management Methods 
 
SVI #: 96 (highest valid SVI index) 
 
RI #: highest valid RI number (for example, for ETX-2i: 31)   
 
Flows: mng_access_default_in, mng_access_default_out 
• 
Not backward compatible to user configuration CLI scripts that configure OOB port 
 
Untagged Management Access from OOB MNG Port 
The factory default configuration is only loaded if there is no startup-config or user-default-config (for 
example, after executing the factory-default command).  
If you copy a script and paste it to the terminal after factory-default-config is loaded, it is important to 
verify that the configuration in the script does not conflict with the factory default configuration. 
You can delete the factory default configuration. You can also replace the factory-default with a 
download of a fresh startup-config, by performing Reset. 
You can add an additional IP address over the RI to allow remote access. 
When accessing remotely, it is possible to delete the local IP 169.254.1.1/16. 
The following table lists the factory defaults for the management access parameters. 
Parameter 
Default Value 
telnet 
 
ssh 
 
snmp 
 
sftp 
 
tftp 
 
ssh-encryption  
all 
ssh-mac 
all 
auth-policy 1st-level  
local 
ETX-2i Devices 
4. Configuration and Management Methods 
The following table lists the factory defaults for the Control port parameters. 
Parameter 
Default Value 
baud-rate 
9600 bps 
console-timeout 
limited 10 (minutes) 
serial-port-disable 
no serial-port-disable 
timeout  
limited 10 (minutes) 
length 
20 
Functional Description 
Inband and Out-of-Band (OOB) Management Access 
Two types of ETX management access are supported: 
• 
Inband – ETX host (management RI) resides directly over one or two VLANs in a specific port or 
over a Bridge port (for example, to allow management access in a Ring topology).  
Router
MNG RI 
(ETX Host)
NNI
 
ETX Host over VLANs 
ETX-2i Devices 
4. Configuration and Management Methods 
Router
Bridge
NNI
NNI
Bridge Port
MNG RI 
(ETX Host)
Ring Port East
Ring Port West
 
ETX Host over Bridge Port 
• 
Out-of-band (OOB) – MNG access via OOB port is supported to access the device host only, and 
not the management VLAN Bridge domain.  
Router
MNG RI 
(ETX Host)
OOB
MNG
Port
 
Direct Host OOB MNG Access  
Limiting SSH Encryption Algorithms  
By default, when a user accesses a device with SSH, the device accepts any supported SSH encryption 
algorithm. 
ETX-2i enables you to limit the SSH server to up to six of the following supported SSH encryption 
algorithms:  
• 
AES-CBC 128, 192, 256 
• 
AES-CTR 128, 192, 256 
• 
3DES-CBC 168 
• 
3DES-EDE-CBC 112  
• 
ARC4 128, 256 
ETX-2i Devices 
4. Configuration and Management Methods 
Limiting SSH MAC Algorithms  
By default, when a user accesses a device with SSH, the device accepts any supported SSH message 
authentication code (MAC) algorithm. 
ETX-2i enables you to limit the SSH server to up to four of the following supported SSH MAC algorithms:  
• 
MD5-96 
• 
MD5-128 
• 
SHA1-160  
• 
SHA1-96 
• 
SHA2-256 
• 
SHA2-512  
Limiting SSH Key-Exchange Algorithms  
By default, when a user accesses a device with SSH, the device accepts any supported SSH key-exchange 
algorithm. 
ETX-2i enables you to limit the SSH key-exchange algorithm to one of the following supported 
authentication algorithms:  
• 
curve25519-sha256 
• 
ecdh-sha2-nistp521 
• 
ecdh-sha2-nistp384 
• 
ecdh-sha2-nistp256 
• 
diffie-hellman-group-exchange-sha256 
• 
diffie-hellman-group-exchange-sha1 
• 
diffie-hellman-group14-sha256 
• 
diffie-hellman-group15-sha512 
• 
diffie-hellman-group16-sha512 
• 
diffie-hellman-group17-sha512 
• 
diffie-hellman-group18-sha512 
• 
diffie-hellman-group14-sha1 
• 
diffie-hellman-group1-sha1 
ETX-2i Devices 
4. Configuration and Management Methods 
Control Port 
You can configure the control port parameters, which include specifying the data rate, security terminal 
timeout, console timeout, and screen size from which you are accessing the device. You can also disable 
management via the console serial port.  
ETX-2i supports two commands under the terminal level to control CLI inactivity timeout: 
• 
timeout – inactivity timeout for CLI sessions from remote Telnet/SSH CLI connection. 
• 
console-timeout – inactivity timeout for local console CLI sessions  
If a CLI session is inactive (i.e., no input is received) for the configured timeout, (in terminal timeout for 
remote connection or terminal console-timeout for local connection), the device terminates the 
session, and logs the logout event, with the due to inactivity timeout string. 
 
Note 
ETX-2 also supports configuration of an inactivity timeout value for each login-
user, using the inactivity-timeout command under the login-user level (see 
Configuring User Access below). The login-user inactivity-timeout 
configuration takes precedence over the general timeout and console-
timeout values configured here. However, if the login-user inactivity timeout 
is not configured or is configured as default, the timeout and console-timeout 
values configured here apply to the login-user. 
Source IP Address 
The management source IP address provides a single point of contact for management applications that 
interface with ETX-2i.  
When a router interface responds to management packets, the responding packet source IP address is 
set to the router interface IP address. If the router interface sends a management packet that is not a 
response, the packet source IP address is set to the ETX-2i management source IP address. If the 
management source IP address is not configured or the corresponding router interface is down, the 
packet source IP address is set to the router interface IP address. You can configure a single 
management source address for IPv4 and IPv6 to be used in all client management applications, 
including: SNMPv3 (for trap), Radius, TACACS+, Syslog, SNTP, TFTP, and SFTP. 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Configuring Management Access 
This section describes how to configure general management parameters. It also describes the 
command for selecting a subset of the supported SSH encryption algorithms, when using SSH 
management access.  
 
Note 
There is no explicit configuration for inband and outband management 
access.  
 To configure management access: 
• 
At the configure management access prompt, perform the required tasks according to the 
following table. 
Task 
Command 
Comments 
Allowing SFTP access 
sftp 
Entering no sftp blocks access by SFTP 
client. 
Allowing SSH (Secure Shell) access 
ssh 
Entering no ssh blocks access by SSH. 
Selecting acceptable SSH encryption 
algorithms 
ssh-encryption {all | 
algorithm 
<algorithm-1> 
[algorithm-2] 
[algorithm-3] 
[algorithm-4] 
[algorithm-5] 
[algorithm-6]} 
Possible values: 
all – all algorithms are accepted 
(default) 
algorithm-1 to algorithm-6 – one of 
the following: aes-cbc-128, aes-cbc-
192, aes-cbc-256, aes-ctr-128,  
aes-ctr-192, aes-ctr-256, 3des-cbc-168, 
arc4-128, arc4-256 
Notes:  
• If all is selected, there is no need to 
select any algorithms, and if you 
do, your selection is ignored. 
• If the command is repeated, the 
latest instance replaces the 
previous one. 
• If all is not selected, you must 
select at least one algorithm. 
• If multiple algorithms are selected, 
they must be different ones. 
• The order of the algorithms is not 
important; usually the strongest is 
negotiated first. 
ETX-2i Devices 
4. Configuration and Management Methods 
Task 
Command 
Comments 
Selecting strong SSH key exchange algorithms 
ssh-key-exchange { 
algorithm 
<algorithm-1> 
[algorithm-2] 
[algorithm-3] 
[algorithm-4] 
[algorithm-5] 
[algorithm-6] } 
Possible values: 
Entering no ssh-key-exchange re-
enables the SSH key exchange for all 
algorithms regardless the strength. 
Entering ssh-key-exchange without 
value enables the SSH key exchange 
for all strong algorithms. 
Entering ssh-key-exchange with up to 
six values for algorithm-1 to 
algorithm-6 enables the SSH key 
exchange for the specified algorithms. 
The following algorithms are available 
and supported: 
curve25519-sha256,  
ecdh-sha2-nistp521,  
ecdh-sha2-nistp384,  
ecdh-sha2-nistp256,  
diffie-hellman-group-exchange-
sha256,  
diffie-hellman-group-exchange-sha1, 
diffie-hellman-group14-sha256,  
diffie-hellman-group15-sha512,  
diffie-hellman-group16-sha512,  
diffie-hellman-group17-sha512,  
diffie-hellman-group18-sha512,  
diffie-hellman-group14-sha1,  
diffie-hellman-group1-sha1. 
Notes: 
• If no algorithms are selected, all 
strong algorithms are used. 
• If multiple algorithms are selected, 
they must be different ones. 
• If the command is repeated, the 
latest instance of the command 
replaces the previous one. 
The order of the algorithms is not 
important. Usually, the strongest one 
is negotiated first. 
ETX-2i Devices 
4. Configuration and Management Methods 
Task 
Command 
Comments 
Selecting strong SSH key exchange algorithms 
ssh-key-exchange { 
algorithm 
<algorithm-1> 
[algorithm-2] } 
Possible values: 
Entering no ssh-key-exchange re-
enables the SSH key exchange for all 
algorithms regardless the strength. 
Entering ssh-key-exchange without 
value enables the SSH key exchange 
for all strong algorithms. 
Entering ssh-key-exchange with up to 
two values for algorithm-1 to 
algorithm-2 enables the SSH key 
exchange for the specified algorithms. 
The following algorithms are available 
and supported: 
diffie-hellman-group14-sha1,  
diffie-hellman-group1-sha1 
Notes: 
• If no algorithms are selected, all 
strong algorithms are used. 
• If the command is repeated, the 
latest instance of the command 
replaces the previous one. 
The order of the algorithms is not 
important. Usually, the stronger one is 
negotiated first. 
Selecting acceptable SSH MAC algorithms  
ssh-mac { all | 
algorithm 
<algorithm-1> 
[algorithm-2] 
[algorithm-3] 
[algorithm-4] } 
Possible values: 
all – all algorithms are accepted 
(default) 
algorithm-1 to algorithm-4 – one of 
the following: sha1-96, sha1-160,  
md5-96, md5-128, sha2-256, sha2-512 
Notes:  
• If all is selected, there is no need to 
select any algorithms, and if you 
do, your selection is ignored. 
• If the command is repeated, the 
latest instance replaces the 
previous one. 
• If all is not selected, you must 
select at least one algorithm. 
ETX-2i Devices 
4. Configuration and Management Methods 
Task 
Command 
Comments 
• If multiple algorithms are selected, 
they must be different ones. 
• The order of the algorithms is not 
important; usually the strongest is 
negotiated first. 
• To allow strong algorithms only, 
use the above-listed command. 
Allowing SNMP access 
snmp 
Entering no snmp blocks access by 
SNMP. 
Allowing Telnet access (for IPv4 only) 
telnet 
Entering no telnet blocks access by 
Telnet. 
Allowing TFTP access 
tftp 
Entering no tftp blocks access by TFTP. 
Configuring Control Port 
 To define the control port parameters: 
1. Navigate to configure terminal. 
2. At the config>terminal# prompt, perform the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying the desired data rate 
baud-rate { 9600bps | 19200bps | 
38400bps | 57600bps | 115200bps } 
The control port data rate of ETX-2i 
with PMC should be set to 9600 bps 
or higher to be compatible with the 
x86 terminal. 
Setting local console inactivity 
timeout 
console-timeout {forever | limited 
<minutes>} 
Maximum number of minutes that 
local CLI session can be without 
activity before it automatically 
disconnects 
forever – no timeout 
minutes – maximum length of 
timeout 
Possible values: 1-60  
Note: This command does not affect 
remote sessions. 
ETX-2i Devices 
4. Configuration and Management Methods 
Task 
Command 
Comments 
Specifying the number of rows 
to display 
length <number-of-rows> 
The number of rows to print before 
pausing, or 0 for no pausing (i.e., no 
limit on the number of lines 
displayed). 
Possible values: 0-255 
Disabling the control port  
serial-port-disable 
no serial-port-disable (default)  
serial-port-disable command denies 
console access via remote access 
(inband or OOB via Telnet/SSH, 
SNMP) for normal operation. It only 
allows access during boot process. 
Management connectivity can be 
resumed in one of the following 
ways: 
• Issuing the no serial-port-disable 
command from remote access 
(inband or OOB via Telnet, 
SNMP). 
• Setting to default configuration, 
by pressing the external push 
button on the front panel.  
Setting remote Telnet/SSH 
session inactivity timeout 
timeout {forever | limited 
<minutes>} 
Maximum number of minutes that 
remote Telnet/SSH CLI session can 
be without activity before it 
automatically disconnects 
forever – no timeout 
minutes – maximum length of 
timeout 
Possible values: 1-60  
Note: This command does not affect 
local console sessions.  
 
 

## 4.2 User Access  *(p.242)*

ETX-2i Devices 
4. Configuration and Management Methods 
Configuring the Source IP Address 
 To configure the management source IP address: 
1. Navigate to configure management. 
2. Enter management-address <ip-address> 
Note 
According to the format of the IP address (IPv4 or IPv6), it is saved as the IPv4 
or IPv6 management source IP address.  
The management source IP address is set to the specified IP address. 
3. To delete the IPv4 or IPv6 management address, enter: 
no management-address {ipv4 | ipv6} 
4.2 User Access 
ETX-2i supports the User Access sub-system for definition of login users, user privileges, and user 
authentication.  
Applicability and Scaling 
This feature is applicable to all ETX-2i products.  
Factory Defaults 
By default, the following users exist, with default password 1234: 
• 
su 
• 
oper 
• 
tech 
• 
user 
The default users cannot be deleted but can be disabled (shut down). 
By default, authentication is via the locally stored database (1st-level local). 
ETX-2i Devices 
4. Configuration and Management Methods 
Functional Description 
Users Administration 
ETX-2i management software allows you to define new users, and their management and access rights. 
You can also view connected users, their details, and their failed login attempts. 
ETX-2i supports the following four user access levels: 
• 
Superuser (su) can perform all the activities supported by the system, including the following: 
 
Creating new users 
 
Deleting and disabling other users 
 
Changing its own and other users’ access levels and passwords 
 
Monitoring the device (info, show status, show statistics). 
• 
Operator (oper) can perform the following: 
 
Changing other users’ access levels and passwords 
• 
Technician (tech) can do the following: 
 
Monitoring the device (info, show status, show statistics) 
 
Additional tasks as defined by a Superuser or Operator. 
• 
User (user) can do the following: 
 
Monitoring the device (info, show status, show statistics) 
 
Additional tasks as defined by a Superuser or Operator. 
In addition, all users are allowed to change their current passwords and view all CLI levels. 
Password Hashing 
A user’s password is used for access via terminal, Telnet, and SSH. 
You can specify a user’s password as a text string or as a hashed value, that you obtain by using info 
detail to display user data. 
ETX-2i Devices 
4. Configuration and Management Methods 
Note 
• 
User passwords are stored in a database so that the system can perform 
password verification when a user attempts to log in. To preserve 
confidentiality of system passwords, the password verification data is 
typically stored after a one-way hash function is applied to the password, 
in combination with other data. When a user attempts to log in by 
entering a password, the same function is applied to the entered value 
and the result is compared with the stored value. 
• 
A cryptographic hash function is a deterministic procedure that takes an 
arbitrary block of data and returns a fixed-size bit string, the 
(cryptographic) hash value, such that any change to the data changes the 
hash value.  
SSH Authentication 
In addition to password, ETX-2i can be configured to use a more robust and secure public key user 
authentication method for SSH sessions. 
The two methods of performing user (SSH client) authentication are summarized, as follows: 
• 
Using password (default) – ETX-2i has default usernames and passwords. 
 
SSH client waits for the user to enter their username and password. 
 
SSH client sends the username and password to the SSH server. 
 
The SSH server verifies the username and password and then provides CLI access. 
• 
Using public key (2048-bit RSA) – more robust and secure. 
 
SSH client waits for the user to enter their username 
 
SSH client sends the username to the server 
 
The SSH server verifies the username and public key and then provides CLI access. 
Inactivity Timeout 
ETX-2i supports the inactivity-timeout command under the login-user level to control inactivity timeout 
per CLI user for all types of sessions (local, Telnet, and SSH). The login-user inactivity-timeout 
configuration takes precedence over the general timeout and console-timeout values configured under 
config>terminal level (see Configuring Control Port). However, if the login-user inactivity timeout is not 
configured or is configured as default, the timeout and console-timeout values under config>terminal 
level apply to the login-user.  
If a CLI session (remote or local) is inactive (i.e., no input is received) during the configured timeout, the 
device terminates the session, and logs the logout event, with the due to inactivity timeout string. 
ETX-2i Devices 
4. Configuration and Management Methods 
Access Policy 
The access policy allows specifying up to three user authentication methods (local, RADIUS, TACACS+). If 
an authentication method is not available, the next method is used if applicable. 
Command Authorization 
ETX-2i allows specifying one or two methods for command authorization (local and/or TACACS+). If one 
method is not available, the next method is used if applicable. The user can require NETCONF 
commands to be authorized according to the configured sequence. If this option is disabled (the 
default), they are locally authorized. 
In local authorization, the device decides whether to allow a user to execute a command. For each 
command, a list of users allowed to execute it is preconfigured. This configuration can be overridden 
with the access-level command in the admin level. Local authorization always works. 
In TACACS+ authorization, the device sends each command to the configured TACACS+ servers and acts 
as directed. The second method, if configured, is only used if none of the TACACS+ servers replies. 
If a user attempts to execute a command without authorization, it will result in the following CLI error: 
You are not authorized to execute this command 
Access Level 
Users can change the minimum level authorized to execute a CLI command from what is predefined in 
the ETX-2i operating system. For example, they may want to limit reboot for su rather than oper. This 
can be done with the access-level command in the admin level. 
The user must provide a full-path command (or level) without arguments. Longest match policy is 
applied in case a command matches multiple rules. For example, if a user sets the minimum level of port 
ethernet to oper, and that of port ethernet shutdown to su, then an oper-level user will be allowed to 
execute all ethernet-level commands, except shutdown, which will require an su-level user. 
 
Note 
Setting the rights of a command applies to its no form as well. Setting the 
rights of a no form command applies to its natural form as well. 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Configuring User Access 
 To add a new user: 
1. Verify that you are logged on as superuser (su). 
2. Navigate to the management context (config>mngmnt). 
3. Enter login-user, followed by a new username if you intend to create a new user, or an existing 
name, if you intend to change previously defined user. 
Note 
Maximum username length is 20 characters.  
4. The prompt changes to config>mngmnt>login-user<username>#. 
5. Perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
Specifying user 
authentication method 
authentication-method 
{password | public-key} 
The default user authentication method 
is password. ETX-2i has default 
usernames and passwords. 
If you change the authentication 
method of a user with access level su to 
public key, and no public key has been 
defined, you are warned that the super 
user is going to be disabled and 
prompted to confirm the operation. 
Notes:  
• You can create a public key, by 
configuring config>mngmnt>login-
user<user-name> public-key 
<public-key>. Alternately, you can 
create a public key using the 
generate-rsa command under 
config>crypto-key command that 
supports SSHv2 RSA 2048-bit key 
generation. Refer to RSA Key 
Generation in the Management and 
Security chapter. 
• The password that you enter for a 
user is masked in TACACS+ and 
Syslog, appearing in the TACACS+ 
and Syslog command logs as 
asterisks (*), thus providing 
protection from sniffers. 
ETX-2i Devices 
4. Configuration and Management Methods 
Task 
Command 
Comments 
Setting inactivity 
timeout for user 
inactivity-timeout { default | 
forever | limited <minutes> } 
Maximum number of minutes that 
user’s CLI session (local, Telnet, or SSH) 
can be without activity before it 
automatically disconnects. 
default – user inactivity timeouts are 
those configured in the timeout and 
console-timeout commands under the 
config>terminal level.  
forever –no inactivity timeout for this 
user’s sessions. 
minutes – maximum length of timeout 
Possible values: 1-60  
Note: login-user level inactivity-timeout 
overrides timeout and  
console-timeout values under 
config>terminal level. However, if 
default is configured, timeout and 
console-timeout values, configured 
under config>terminal level, apply.  
Defining a user access 
level 
level { su | oper | tech | user } 
 
Specifying user 
password 
password <password> [hash] 
Maximum password length is as follows: 
• Non-hashed – 20 characters 
• Hashed – 40 characters 
The use of hash function is illustrated in 
the example below. 
ETX-2i Devices 
4. Configuration and Management Methods 
Task 
Command 
Comments 
Setting user public key 
for authentication 
public-key <public-key> 
Public key configuration is relevant only 
for the public key authentication 
method. 
Public key format: “ ssh-rsa <space> 
public key string <space> comment “ 
[1..512 chars] 
Use the Base64 encoding (ASCII ‘A’ to 
‘Z’, ‘a’ to ‘z’, ‘0’ to ‘9’, ’+’, ‘/’ and ‘space’) 
for the public key configuration. 
Entering no public-key deletes the 
public key.  
Note: ETX-2i does not have default 
public keys. 
Enabling/disabling a 
user 
shutdown  
no shutdown 
Default users (su, oper, tech, user) can 
be disabled but cannot be deleted. 
 To delete an existing user: 
1. Verify that you are logged on as superuser (su). 
2. Navigate to the management context (config>mngmnt).  
3. Enter no login-user, followed by the name of the user that you intend to delete. 
Configuring Access Policy 
 To define the access policy: 
• 
Navigate to the management access level. At the config>mngmnt>access# prompt, perform 
the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying authentication via 
locally stored database 
auth-policy 1st-level local 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Task 
Command 
Comments 
Specifying authentication 
method preferably via TACACS+, 
then local 
auth-policy 1st-level tacacs+ 
[2nd-level { local | none } ] 
If 2nd-level is set to local, 
authentication is performed via the 
TACACS server. If the TACACS server 
does not answer the authentication 
request, then ETX-2i authenticates 
via the local database. If the TACACS 
server rejects the authentication 
request, ETX-2i ends the 
authentication process. 
If 2nd-level is set to none, 
authentication is performed via the 
TACACS server only. 
Specifying authentication 
method preferably via RADIUS/ 
TACACS+, then TACACS+/ 
RADIUS, then local 
auth-policy 1st-level radius 
[2nd-level tacacs+ [3rd-level {local | 
none}]] 
auth-policy 1st-level tacacs+ 
[2nd-level radius [3rd-level {local | 
none}]] 
ETX-2i first attempts authentication 
via the server specified by 1st-level. If 
the server does not answer the 
authentication request, then ETX-2i 
attempts to authenticate via the 
server specified by 2nd-level. If the 
server does not answer the 
authentication request, then ETX-2i 
attempts to authenticate according 
to 3rd-level: 
• local – ETX-2i authenticates via 
the local database. 
• none – No further authentication 
is done, and the authentication 
request is rejected. 
Note: If at any time in this process, 
an authentication server rejects an 
authentication request, ETX-2i ends 
the authentication process and does 
not attempt authentication at the 
next level. 
ETX-2i Devices 
4. Configuration and Management Methods 
Configuring Command Authorization 
 To define the command authorization method: 
• 
Navigate to the management access level. At the config>mngmnt>access# prompt, perform 
the required tasks according to the following table. 
Task 
Command 
Comments 
Specifying command 
authorization via locally stored 
database 
command-authorization 1st-
method local [netconf-include] 
 
Specifying command 
authorization method 
preferably via TACACS+, then 
local 
command-authorization 1st-
method tacacs+ [2nd-method {local 
| none}] [netconf-include] 
If 2nd-method is set to local, 
command authorization is performed 
via the TACACS server. If the TACACS 
server does not answer the 
authentication request, then ETX-2i 
authenticates via the local database. 
If the TACACS server rejects the 
authentication request, ETX-2i ends 
the command authorization process. 
If 2nd-level is set to none, command 
authorization is performed via the 
TACACS server only. 
Configuring Access Level 
 To change the minimum level authorized to execute a CLI command: 
• 
Navigate to the admin level. At the admin# prompt, perform the required tasks according to 
the following table. 
Task 
Command 
Comments 
Changing the minimum level 
authorized to execute a 
command 
access-level command <command-
string> min-level { oper | su | tech | 
user } 
 
Returning the command to its 
default minimum level 
no access-level command 
<command-string> 
 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Examples 
Defining Users 
 To define a new user: 
• 
Username – staff 
• 
Access level – su 
• 
Password – 1234 
exit all 
configure management 
login-user staff 
level su 
password 1234 
no shutdown 
exit 
 To add a new user with a hashed password: 
1. Define a new user with a text password. 
2. Use info detail to display the password hash value. 
3. Define another user with the hashed password from the info detail output. 
For example, to add the following users: 
• 
Username: staff1 
• 
User password: 4222 
• 
Username: staff2 
• 
User password: hash of 4222 (user staff2 can log in with password 4222) 
exit all 
configure management 
login-user staff1 
level su 
password 4222 
no shutdown 
exit 
exit all 
configure management login-user staff1 info detail 
    level su 
    password "3fda26f8cff4123ddcad0c1bc89ed1e79977acef" hash 
    no shutdown 
ETX-2i Devices 
4. Configuration and Management Methods 
exit all 
configure management 
login-user staff2 
level su 
password "3fda26f8cff4123ddcad0c1bc89ed1e79977acef" hash 
no shutdown 
exit 
 
exit all 
configure management login-user staff2 info detail 
    level su 
    password "3fda26f8cff4123ddcad0c1bc89ed1e79977acef" hash 
    no shutdown 
Displaying Users 
 To display all connected users: 
• 
At the config>mngmnt# prompt, enter show users. 
A list of all connected users is displayed, showing their access level, the type of connection, and 
the IP address from which they are connected. 
ETX-2i# configure management 
ETX-2i>config>mngmnt# show users 
 
Num       User                          Access Level  Source    IP Address 
----------------------------------------------------------------------------- 
1.        su                            Su            Terminal  0.0.0.0 
2.        su                            Su            Netconf   172.17.160.69 
 
Viewing User Information 
The details of the currently logged-in users are available in the show users-details screen. 
The screen for show users-details provides the following information: 
User 
Username 
Level 
User access level 
Popup 
Alarm/event popup status (enabled or disabled) 
From 
Source IP address of the management session, followed by protocol type (serial, Telnet, SSH, 
NETCONF) 
ETX-2i Devices 
4. Configuration and Management Methods 
For (sec) 
Duration of the current management session in seconds 
Connected To 
Destination IP/ protocol type of the active client Telnet session (to a remote device) 
For (sec) 
Duration of the active client Telnet session (to a remote device) in seconds 
 To display the user information: 
• 
In the config>mngmnt# prompt, enter show users-details. 
ETX-2i# configure management 
ETX-2i>config>mngmnt# show users-details 
User:1234  Level:su  Popup:Disabled 
    From:1.1.1.1/SSH  For(sec):120  
User:123456  Level:oper  Popup:Disabled 
    From:100.100.100.100/Telnet  For(sec):120  
    Connected To:1111:2222:3333:4444:5555:6666:7777:8888/Telnet  For(sec):100 
User:su  Level:su  Popup:Enabled 
        From:Serial  For(sec):94 
User:su  Level:su  Popup:Enabled 
        From:172.17.160.69/Netconf  For(sec):77 
Viewing SSH Server Information 
You can display the fingerprint of the SSH server public key. 
 To display the SSH server information: 
• 
At the config>mngmnt# prompt, enter show ssh-server fingerprint. 
The SSH fingerprint information stored on the SSH server is displayed. 
ETX-2i# configure management 
ETX-2i>config>mngmnt# show ssh-server fingerprint 
RSA key fingerprint is ef:ab:28:81:53:c2:a3:8d:77:0d:06:e7:89:2b:81:9c 
Viewing Failed Login Attempts 
You can view failed login attempts to the device. 
 To display failed login attempts: 
• 
At the config>mngmnt# prompt, enter show failed-login-attempts. 

## 4.3 Services for Management Traffic  *(p.254)*


## 4.4 Configuring Mass Deployments  *(p.254)*

ETX-2i Devices 
4. Configuration and Management Methods 
ETX-2i# configure management 
ETX-2i>config>mngmnt# show failed-login-attempts 
Recent Failed Login Attempts 
 
Source           Attempts  First Attempt    Blocked for 
------------------------------------------------------- 
1.1.1.1          5         302 seconds ago  277 seconds 
100.100.100.100  2         100 seconds ago  -- 
 
Parameter 
Description 
Source 
Source that failed login due to wrong username or password  
Possible values: Local Console, <IP address> 
Attempts 
Number of failed login attempts since the source was last unblocked Possible 
values: <number> 
First Attempt 
The first failed login attempt recorded from the source  
Possible values: <number> second 
Blocked for 
Time remaining until the source will be unblocked from login  
Possible values: 
-- (if the source is not blocked) 
<number> seconds (if the source is blocked) 
4.3 Services for Management Traffic 
Refer to the Service Provisioning chapter. 
4.4 Configuring Mass Deployments 
Configuration files can be downloaded to many devices at once using ZTP (zero touch process). It 
requires the RADview NMS (Network Management System). For a description of all aspects of ZT 
provisioning, including security considerations, read RAD’s Zero Touch Provisioning document. 

## 4.5 CLI-Based Configuration  *(p.255)*

ETX-2i Devices 
4. Configuration and Management Methods 
4.5 CLI-Based Configuration 
This section explains how to use CLI to configure and run ETX units. Every ETX unit supports up to 10 
concurrent CLI sessions. 
Working with Terminal 
ETX-2i has a V.24/RS-232 asynchronous DCE port, designated CONTROL, and terminated in a Mini USB 
(ETX-2i, ETX-2i-B, ETX-2i-10G, ETX-2i-100G/4QSFP), Micro USB (ETX-2i-10G-B/8SFPP)or RJ-45 (ETX-2i-
10G-E/8SFPP) connector. The control port continuously monitors the incoming data stream and 
immediately responds to any input string received through this port. You can use any terminal 
emulation program (such as HyperTerminal or PuTTY) to manage ETX-2i via the control port. The 
following procedure shows how to start a terminal control session using HyperTerminal. 
 To start a terminal control session: 
1. Make sure that ETX-2i is connected to a laptop, as explained in Connecting to a Terminal section 
in the Installation and Setup chapter.  
2. Start the terminal emulation program. 
For example, start HyperTerminal by navigating to 
Start>Programs>Accessories>Communications>HyperTerminal. 
3. From the menu of the New Connection –HyperTerminal window that opens, create a new 
terminal connection by selecting File>New Connection, and in the Connection Description 
window that opens, assign a Name to the connection, and click OK. 
ETX-2i Devices 
4. Configuration and Management Methods 
 
4. In the Connect To window that opens, in Connect using, select COM1, and then click OK. 
The Com Properties window opens. 
5. In the Com Properties window, configure the following laptop communication port parameters, 
and then click OK. 
 
Bits per second (speed): baud rate of 9.6 kbps (9600) 
 
Data bits: 8 bits/character 
 
Parity: no parity  
 
Stop bits: 1 stop bit  
 
Flow control: no flow control 
 
6. Configure character delay by navigating in the home page menu to File>Properties, and in the 
Serial Properties window that opens, clicking the Settings tab, and then the ASCII Setup button. 
ETX-2i Devices 
4. Configuration and Management Methods 
In Character delay, select 10, and then click OK. The terminal input delay between characters is 
now at least 10 msec. 
 
7. Power-up ETX-2i. 
The boot manager of ETX-2i starts and displays a message that you can stop the auto-boot and 
enter the boot manager by pressing any key. A running countdown of the number of seconds 
remaining until auto-boot is displayed. If it reaches 0 before you press a key, then after a few 
seconds a message is displayed showing that the active software pack is being loaded. 
After a few more seconds, the login prompt is displayed. See Login for details on logging in.  
 
ETX-2i Devices 
4. Configuration and Management Methods 
Working with Telnet 
Typically, the Telnet host is a PC or Unix station with the appropriate suite of TCP/IP protocols. Telnet is 
supported in IPv4 only.  
To enable the Telnet host to communicate with ETX-2i, it is necessary to configure the ETX-2i IP address 
settings (refer to the Router section in the Traffic Processing chapter for details). This is usually done via 
a terminal emulation program (see Working with Terminal). After this preliminary configuration, you 
can use a Telnet host connected directly or via a local area network.  
The following procedure describes how to connect to ETX-2i via Telnet.  
Connecting Via Telnet 
 To connect to ETX-2i via Telnet: 
1. At the Telnet host, enter the necessary command (e.g., at a PC enter: 
telnet <IP-address>). 
The Telnet login window appears for the device as shown below. 
 
2. Log into the device as explained in Login. See Using the CLI  for details on using the CLI 
commands.  
Adding a Telnet Client Session 
The ETX-2i management system allows you to open an additional Telnet session (terminal, Telnet, or 
SSH) to a remote device while you are in an active CLI management session (Standard IETF RFC 854). 
The Telnet client allows you to manage a remote unit without IP connectivity to the host device. 
Moreover, the remote unit usually treats the Telnet client traffic as originating from a secure source 
ETX-2i Devices 
4. Configuration and Management Methods 
(ETX-2i). This traffic is unlikely to be filtered out by an ACL rule of the remote unit, in contrast to 
non-secure PC traffic. 
PC
Network
Remote RAD 
Device
RS-232
Telnet
RAD Device
 
Managing Remote Device, Using Telnet Client Functionality 
Source IP Address 
The source IP address depends on the location in the CLI tree from which the Telnet client command is 
activated: 
• 
If the Telnet client command is activated from the router context, the routing table of the 
current router defines the IP address that the packets are sent from. 
• 
If the Telnet client command is activated outside the router context, the routing table of 
Router 1 defines the IP address that the packets are sent from. 
If the destination IP address is not a valid unicast IP address, ETX-2i rejects the command. 
Special Characters 
When the client session is open, its parent session passes all special characters (such as <Ctrl> + <any 
key>) without parsing or acting upon them. The only exception is the <Ctrl> + <_> key combination, 
which closes the client Telnet session. This allows you to terminate the connection and return to the 
parent session if the client session becomes unresponsive, rather than waiting for the inactivity timeout 
to end the connection. 
Inactivity Timeout 
When a Telnet client is used, the inactivity timer of the parent session rearms. This ensures that as long 
as the client session is active, its parent session is not terminated due to an inactivity timeout. Likewise, 
when the inactivity timer of the parent session expires, it is terminated together with its client session. 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Termination 
The client session is terminated if one of the following occurs: 
• 
You quit the client session by using the <Ctrl> + <_> key combination. When this key 
combination is entered, ETX-2i terminates the client session and returns to the parent session 
prompt. This is useful when the remote device stops responding or the connection to it is lost. 
• 
You quit the parent session. 
• 
The parent session is terminated due to inactivity timeout. 
Configuring Telnet Client 
Telnet client sessions can be invoked from any CLI context. 
 To start a client Telnet session: 
• 
At any level, start a client Telnet session by specifying the IP address of the remote device and 
(optionally) destination TCP port (default 23):  
telnet <ip-address> [port <0–65535>] 
 To close a client Telnet session: 
• 
At any level, enter: 
<Ctrl> + <_> 
ETX-2i terminates the client Telnet session and returns to the parent session prompt. 
Viewing Telnet Client Session Information 
The details of the client Telnet session (destination IP address and duration) are available in the output 
of the command show users-details. 
Activation and termination of a client Telnet session generate the remote_terminal_started and the 
remote_terminal_ended events, respectively. The events are stored in the ETX-2i log file and generate 
SNMP traps. 
 To display the Telnet client session information: 
• 
In the config>mngmnt# prompt, enter: 
show users-details. 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
The Connected To and For (sec) fields in the third line for User 123456 detail the destination IP/ 
protocol type and duration of the active client Telnet session. 
ETX-2i# configure management 
ETX-2i>config>mngmnt# show users-details 
User:1234  Level:su  Popup:Disabled 
    From:1.1.1.1/SSH  For(sec):120  
User:123456  Level:oper  Popup:Disabled 
    From:100.100.100.100/Telnet  For(sec):120  
    Connected To:1111:2222:3333:4444:5555:6666:7777:8888/Telnet  For(sec):100 
Working with SSH 
Typically, the SSH host is a PC or Unix station with the appropriate suite of TCP/IP protocols. 
To enable the SSH host to communicate with ETX-2i, it is necessary to configure the ETX-2i IP address 
settings (refer to the Router section in the Traffic Processing chapter for details). This is usually done via 
a terminal emulation program (see Working with Terminal). After this preliminary configuration, you 
can use an SSH host connected directly or via a local area network. 
You can connect to ETX-2i via SSH (more secure than Telnet) using a program, such as PuTTY. You can 
use the built-in RSA key for SSH authentication or create your own key (refer to RSA Key Generation in 
the Management and Security chapter). 
Login 
ETX-2i supports various access levels to prevent unauthorized modification of the operating parameters. 
Refer to User Access in the Management and Security chapter for more information on the access 
levels, as well as a list of the default users defined in the device and information on configuring 
additional users. 
Note 
The superuser (su) can perform all the activities supported by the ETX-2i 
management facility.  
You can log into your device with your username and password. 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
If you fail to log in to the terminal five times (due to wrong username or password) in less than five 
minutes, from the same IP address (or the local console), the device does the following: 
• 
Blocks further login attempts from the same IP (or the local console) for five minutes. Attempts 
from remote are answered with immediate TCP reset, without trying to authenticate the user. 
Attempts from the local console are rejected, and the following error is generated: Console 
temporarily blocked due to excessive failed login attempts. 
• 
Blocks any management protocol from the same IP (or the local console), such as SNMP and 
NETCONF, for five minutes. 
• 
Logs the failed_login event, with the maximum number of attempts exceeded string. 
When the locking period is over, the device lifts the block, even if there were further attempts during 
this time. Afterwards, you can fail five more attempts before being locked again. 
 
Note 
• 
An SNMP access attempt with wrong credentials does not count as a 
failed login attempt, and the user is not blocked due to it. 
• 
You can display information on recent failed login attempts (of sources 
that failed since last being unblocked) by invoking the show failed-login-
attempts command (under the management level). Refer to Viewing 
Failed Login Attempts in the Management and Security chapter. 
• 
<CR> for either username or password is ignored and is not considered a 
failed login attempt.  
Logging In 
 To log in to ETX-2i: 
1. At the user prompt (user>), enter the username and press <Enter>.  
The password prompt (password>) appears. 
2. Enter the password (default is 1234) and press <Enter>. 
The base prompt ETX-2i# appears.  
Note 
You can display a banner at login. Refer to the Administration chapter for 
details.  
ETX-2i Devices 
4. Configuration and Management Methods 
Changing Password 
It is recommended that you change the users’ default passwords to prevent unauthorized access to the 
unit using the special option chngpass. This option is also useful in case the user has forgotten their 
password. 
 To change/restore a password:  
1. At the User prompt (config>mngmnt# user>), enter chngpass and press <Enter>. 
2. Enter user as username and press <Enter> to receive a temporary password. With this password 
you can enter as a user and change the password to your own.   
A key code is displayed. 
3. Send the key code to the RAD Technical Support department. 
RAD technical support department will generate a temporary password which is valid for a 
single login. 
4. Use this temporary password to log in and set a new permanent username and password. 
Lost Superuser Password 
If you have lost your superuser password, contact Technical Support via the RADcare Online portal or by 
email. 
Using the CLI 
The CLI consists of commands organized in a tree structure of levels, starting at the base level. Each level 
(also referred to as context) can contain levels and commands (see Navigating for more information on 
the levels and commands available in ETX-2i). The level is indicated by the CLI prompt. 
 
Note 
Most commands are available only in their specific context. Global commands 
are available in any context. You can enter ? at any level to display the 
available commands.  
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
CLI Prompt 
The base level prompt contains the device name, which is ETX-2i by default (the device name can be 
configured in the system level; refer to Device Information in the Administration chapter). The prompt 
ends with $, #, or >, depending on the type of entity being configured and the user level. 
If a new dynamic entity is being configured, the last character of the prompt is $. Examples of dynamic 
entities include flows, QoS profiles, and OAM CFM entities.  
If a new dynamic entity is not being configured, the last character of the prompt is > (for tech or user 
access levels) or # (for other access levels). 
 
Note 
The examples in this manual use # as the last character of the prompt unless 
the creation of a new dynamic entity is being illustrated.  
After you type a command at the CLI prompt and press <Enter>, ETX-2i responds according to the 
command entered. 
CLI Sessions and Inactivity Timeout 
ETX-2i supports a maximum of ten concurrent CLI sessions. If a CLI session is inactive (i.e., no input 
received) for ten minutes (the default) or the number of minutes configured in the inactivity timer (refer 
to timeout and console-timeout configuration in the Control Ports section of the Management and 
Security chapter), the device terminates the session and logs the logout event, with the due to inactivity 
timeout string. 
Navigating 
To navigate down the tree, enter the name of the next level. The prompt then reflects the new location. 
To navigate up, use the global command exit. To navigate all the way up to the root, enter exit all.  
At the prompt, one or more level names separated by a space can be typed, followed (or not) by a 
command. If only level names are typed, navigation is performed, and the prompt changes to reflect the 
current location in the tree. If the level names are followed by a command, the command is executed, 
but no navigation is performed, and the prompt remains unchanged. 
 
Note 
To use show commands without navigating, type show followed by the level 
name(s) followed by the rest of the show command.  
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
In the following example, the levels and command were typed together and therefore no navigation was 
performed, so the prompt did not change. 
ETX-2i# configure system date-and-time date-format yyyy-mm-dd 
ETX-2i# show configure system system-date 
2013-06-10   15:08:20  UTC  +00:00 
ETX-2i# 
In the following example, the levels were typed separately, and the navigation is reflected by the 
changing prompt. 
ETX-2i# configure 
ETX-2i>config# system 
ETX-2i>config>system# date-and-time 
ETX-2i>config>system>date-time# date-format yyyy-mm-dd 
ETX-2i>config>system>date-time# exit 
ETX-2i>config>system# show system-date 
2013-06-10   15:13:23  UTC  +00:00 
 
ETX-2i>config>system# 
Full-Path Command 
Full-path command allows you to enter a CLI command anywhere in the tree as if the current level was 
the CLI root, by preceding the command or level change with a backslash character. The device executes 
the command as if it were invoked from the CLI root. 
If you enter a level change (preceded by \) without a command, the CLI does not return to the prompt of 
the level of the invoking command but remains at the changed level. For example, the \configure system 
command, when invoked from any level in the CLI tree, returns the ETX-2i>config>system# prompt. 
However, if you enter a level change followed by a command, the system performs the command and 
then returns the prompt of the level that the command was invoked from. For example, if following the 
command ETX-2i>admin>scheduler#, you enter \configure system name my-device, the latter 
command sets the device name to my-device and then returns the prompt my-
device>admin>scheduler#. 
 
Note 
Before executing a full path command, the CLI engine exits to the CLI root. 
Some commands (e.g., ping) behave differently, depending on the location 
they were executed from. The following command, for example, would use a 
router 1 source address, although executed from router 2:  
ETX-2i>config>router(2)# \configure router 1 ping 192.168.1.1 
ETX-2i Devices 
4. Configuration and Management Methods 
Command Tree 
The tree command displays a hierarchical list of all the commands in the CLI tree, starting from the 
current context. The commands are shown according to the user’s access level (su, oper, tech, or user) 
and the hardware capabilities of the product. 
Some examples:  
• 
The CLI commands config>chassis>overheat-auto-shutdown and config>terminal>baud-rate 
are available for su and oper users only and are displayed in the output of the tree command for 
users of those access levels only.  
• 
The config>terminal>length command, which specifies the number of rows to display before 
pausing, is available for all user access levels. 
• 
The CLI level config>port>shdsl and all commands under it are available only when SHDSL H/W 
exists. 
• 
The CLI level config>system>clock and all commands under it are available only when timing 
H/W exists (PTP and/or GNSS). 
• 
The CLI level config>virtualization and all commands under it are available only when x.86 H/W 
exists. 
 The CLI level config>port>int-eth and all commands under it are available only when x.86 H/W 
exists. To view the entire CLI tree (commands only): 
1. At the root level, enter tree. 
ETX-2i# tree 
| 
+---admin 
|   | 
|   +---factory-default-all 
|   | 
|   +---access-level 
|   | 
|   +---factory-default 
|   | 
|   +---force-reboot 
|   | 
|   +---license 
|   |   | 
|   |   +---license-enable 
|   |   | 
|   |   +---show summary 
|   | 
|   +---reboot 
|   | 
ETX-2i Devices 
4. Configuration and Management Methods 
|   +---scheduler 
|   |   | 
|   |   +---clear-finished-schedules 
more.. 
2. Press <Enter> to see more or <CTRL-C> to return to the prompt. 
When adding the detail parameter, the output also includes the parameters and values for each 
command. 
 To view the CLI tree including all parameters and values: 
1. Navigate to the required context by typing level names separated by a space and press <Enter>. 
2. Type tree detail and press <Enter>. 
ETX-2i>config# tree detail 
configure 
| 
+---access-control 
|   | 
|   +---access-list [{ipv4|ipv6}] <acl-name> 
|   |   no access-list <acl-name> 
|   |   | 
|   |   +---delete <sequence-number> 
|   |   | 
|   |   +---deny udp <src-address> [<src-port-range>] <dst-address> 
                 [<dst-port-range>] [dscp <dscp-value>] [log] [sequence 
                 <sequence>] 
|   |   |   deny tcp <src-address> [<src-port-range>] <dst-address> 
                 [<dst-port-range>] [dscp <dscp-value>] [log] [sequence 
                 <sequence>] 
|   |   |   deny icmp <src-address> <dst-address> [icmp-type <icmp-type-number>] 
                  [icmp-code <icmp-code-number>] [dscp <dscp-value>] [log] 
                 [sequence <sequence>] 
|   |   |   deny ip [protocol <ip-protocol-number>] <src-address> <dst-address> 
3. Press <Enter> to see more or <CTRL-C> to return to the prompt. 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Command Structure 
CLI commands have the following basic format: 
command [parameter]{ value1 | value2 | … | valuen } [ optional-parameter <value> ]  
 
where: 
{} 
Indicates that one of the values must be selected 
[] 
Indicates an optional parameter 
<> 
Indicates a value to be typed by the user according to parameter requirements 
You can type only as many letters of the level, command, or parameter as required by the system to 
identify it. For example, you can enter config manage to navigate to the management level. 
To finish configuration changes, enter commit. If this command is performed successfully, OK is 
displayed. Otherwise, ETX-2i displays the relevant error message. 
To verify whether the applied configuration changes are valid (before applying commit), use the sanity-
check command. 
You can remove all configuration activity after the last commit command using the discard-changes 
command. 
Special Keys 
The following keys are available at any time: 
? 
List all commands and levels available at the current level. 
<Tab> 
Command-line completion; complete the unambiguous characters of the command and 
display a list of available commands beginning with those characters (as when pressing ?). 
↑ 
Display the previous command (history forward). 
↓ 
Display the next command (history backward). 
<Backspace> 
Delete character before cursor. 
<Delete> 
Delete character before cursor. 
<- 
Move cursor one character leftward. 
ETX-2i Devices 
4. Configuration and Management Methods 
-> 
Move cursor one character rightward. 
<Alt>+B, <Esc>+B 
Move cursor left one word (or go to start of word). 
<Alt>+D, <Esc>+D 
Delete until end of word starting from the cursor. 
<Alt>+F, <Esc>+F 
Move cursor right one word (or go to end of word). 
<Ctrl>+<_>  or 
<Ctrl>+<Shift>+<-> 
Exit CLI. 
<Ctrl>+A 
Move cursor to start of line. 
<Ctrl>+B 
Move cursor one character leftward. 
<Ctrl>+C 
Interrupt current command. 
<Ctrl>+D 
Delete character to right of cursor. 
<Ctrl>+E 
Move cursor to end of line. 
<Ctrl>+G 
Return to upper level. 
<Ctrl>+H 
Delete character to left of cursor. 
<Ctrl>+K 
Delete text from cursor to end of line. 
<Ctrl>+L 
Redisplay current line. 
<Ctrl>+P 
Display the previous command (history forward). 
<Ctrl>+Q 
Resume transmission (XON). 
<Ctrl>+S 
Pause transmission (XOFF). 
<Ctrl>+U 
Delete text up to cursor. 
<Ctrl>+W 
Delete word to the left of cursor. 
<Ctrl>+Y 
Paste text last deleted by a shortcut. 
<Ctrl>+Z 
Navigate to base level. 
ETX-2i Devices 
4. Configuration and Management Methods 
Supported Characters in CLI Commands 
This table lists supported and unsupported characters for configuring parameters as listed below. 
Parameters 
Supported Characters 
Unsupported Characters 
Remarks 
File Name 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + =  ; , `^ ( ) [ ] { } 
' 
* | " < > ? / .\ : 
The file name that is 
used to copy the 
specific file. 
User Password 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
  
SNMP password 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
  
Radius key 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
  
TACACS key 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
  
Username 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
  
SFTP username 
Alphanumerical and the following 
special characters: 
~ ! # $ % & - _ + =   ; , `^ * ( ) [ ] { } 
| ' < > /  
\ @ : . " ? 
The SFTP username 
required for 
authentication to copy 
a file 
SFTP password 
Alphanumerical and the following 
special characters: 
~ ! # $ % & - _ + =   ; , `^ * ( ) [ ] { } 
| ' < > / 
\ @ : . " ? 
The SFTP password 
required for 
authentication to copy 
a file 
ETX-2i Devices 
4. Configuration and Management Methods 
Parameters 
Supported Characters 
Unsupported Characters 
Remarks 
Port name 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
  
PPP name 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
  
PPP chap 
hostname 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
  
PPP chap 
password 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
  
PPP pap 
username 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
 
PPP pap 
password 
Alphanumerical and the following 
special characters: 
~ ! @ # $ % & - _ + = \ : ; , . `^ * ( ) 
[ ] { } '  < > / 
| " ? 
 
NTP 
(authentication 
key) 
Numerical characters 
Alphanumerical and the 
following special characters: 
~ ! @ # $ % & - _ + = \ : ; , . 
`^ * ( ) [ ] { } '  < > | " ? 
 
NTP (trusted key) 
Numerical characters 
Alphanumerical and the 
following special characters: 
~ ! @ # $ % & - _ + = \ : ; , . 
`^ * ( ) [ ] { } '  < > | " ? 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Getting Help 
You can get help in the following ways: 
• 
Enter help to display general help (see General Help). 
• 
Enter help <command> to display information on a command and its parameters (see 
Command Help). 
• 
Enter ? to display the commands available in the level (see Level Help). 
• 
Use <Tab> while typing commands and parameters, for string completion (see Command-Line 
Completion). 
• 
Use ? after typing a command or parameter, for interactive help (see Interactive Help). 
General Help 
Enter help at any level to display general CLI help, including: 
• 
Short description of CLI interactive help 
• 
Commands and levels available at the current level 
• 
Globally available commands 
• 
CLI special keys (hotkeys) 
• 
Output modifiers for filtering output 
• 
URLs for device manual and ShelfView manual 
Example of help command output from the root level: 
ETX-2i# help 
1. Full help - 'help <cmd>'. 
2. To complete level name, command, keyword, argument - <tab> ('conf<tab>' => 
    'configuration'). 
3. To display all currently valid levels, commands, keywords or arguments - 
   '?' ('name ?' => '<name-of-device>'). 
Commands and levels: 
      admin                            + Adminstrative commands 
      clear-statistics                 - Clear all statistics 
      configure                        + Configure device 
      file                             + File commands 
      logon                            - Logon as Debug user 
      on-configuration-error           - Behavior for configuration error 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Global commands: 
      copy                             - Copy file 
      echo                             - Displays a line of text (command) on 
                                         the screen 
      exec                             - Execute script of CLI commands 
      exit                             - Returns to the next higher command 
                                         level (context) 
      help                             - Displays information regarding commands 
                                          in the current level 
      history                          - Displays the history of commands issued 
                                          since the last restart 
      info                             - Displays the current device 
                                         configuration 
      level-info                       - Displays the current device 
                                         configuration - commands from the 
                                         current level only 
      logout                           - Logs the device off 
      ping                             - Ping 
 [no] popup-suspend                    - Suspends popup messages 
      save                             - Save current settings 
 [no] schedule                         - Schedule a command to run in a future 
                                         time 
      telnet                           - Open telnet client session 
      trace-route                      - Traceroute 
      tree                             - Displays the command levels from the 
                                         current context downwards 
Hotkeys: 
      Ctrl-H, Del, Backspace            -Delete character left of cursor 
      Ctrl-D                            -Delete character right of cursor 
      Ctrl-U                            -Delete text up to cursor 
      Ctrl-K                            -Delete text from cursor to end of line 
      Ctrl-W                            -Delete word left of cursor 
      Alt-D, Esc-D                      -Delete word right of cursor 
      Ctrl-Y                            -Paste last deleted text 
      Tab                               -Completion token 
      ?                                 -Interactive help token 
      Ctrl-P, Up arrow                  -History forward 
      Down arrow                        -History backward 
      Ctrl-B, Left arrow                -Move cursor left one character 
      Right arrow                       -Move cursor right one character 
      Ctrl-A                            -Move cursor to beginning of line 
      Ctrl-E                            -Move cursor to end of line 
      Alt-B, Esc-B                      -Move cursor left one word 
      Alt-F, Esc-F                      -Move cursor right one word 
      Ctrl-L                            -Redisplay current line 
      Ctrl-S                            -Pause transmission (XOFF) 
      Ctrl-Q                            -Resume transmission (XON) 
      Ctrl-C                            -Interrupt current command 
      Ctrl-G                            -Return to upper level 
      Ctrl-Z                            -Return to CLI root 
      Ctrl-_                            -Exit CLI 
Output Modifiers (usage: 'command | modifier'): 
ETX-2i Devices 
4. Configuration and Management Methods 
      begin <regular-expression>      -Start printing once expression found 
      exclude <regular-expression>    -Print lines not containing expression 
      include <regular-expression>    -Print lines containing expression 
Show commands can be printed repeatedly by appending 'refresh' to them 
 
ETX-2i Installation and Operation Manual(Sign in is needed)  : https://www.rad.com/docs/497 
(version 6.7.1) 
Command Help 
Enter help <command> to display command and parameter information. 
ETX-2i>config>system# help name 
- name <name-of-device> 
 - no name 
 <name-of-device>     : Device name [0..255 chars] 
Level Help 
Enter ? at the command prompt to display the commands available in the current level. 
ETX-2i>file# ?  
      delete                           - Delete file 
      delete-user                      - Deletes a file from the device 
 [no] description                      - Description of the file 
      dir                              - Display file directory 
 [no] usb-enable                       - Enable USB 
      usb-temporarily-enable           - Enable USB temporarily 
      user-file-dir                    - List of all user files in the device 
 
 show banner-text                      - Display banner 
 show configuration-files              - Displays configuration files 
                                          properties 
 show copy                             - Display Copy progress 
 show factory-default-config           - Display factory-default-config 
 show file-details                     - Displays the details of the file 
 show rollback-config                  - Display rollback-config 
 show schedule-log                     - Display schedule-log 
 show startup-config                   - Display startup-config 
 show sw-pack                          - Display SW packs 
 show usb-status 
 show user-default-config              - Display user-default-config 
 show user-dir 
 show user-script                      - Display user-script 
Command-Line Completion 
Command-line completion saves you command-line entry time and reminds you the syntax of 
command-line entities (levels, commands, parameters, flows, and profiles).  
ETX-2i Devices 
4. Configuration and Management Methods 
In a command-line, ETX-2i completes command-line entities, when you press <Tab> immediately 
following a string (one or more characters). 
Some user-defined entity names, such as flow names or profile names, can be completed as well. If you 
enter an entity name (flow, profile, or similar) that does not exist in the database, ETX-2i creates this 
entity with the selected name.  
If the command-line entity name can be completed in only one way, when you press <Tab>, ETX-2i 
autocompletes the entire name and appends a space. 
If the command-line entity name can be completed in more than one way, ETX-2i appends the 
characters that are common to all possibilities and displays a list of the completion possibilities 
beginning with those characters.  
If the string is already a complete entity name (level/command/parameter/flow/profile) or cannot be 
completed to a complete name, no completion is done. 
Pressing <Tab> following a complete command name (followed by a space), displays a list of available 
command arguments, if they exist (same behavior as ?). 
Pressing <Tab> following a string and a space returns a CLI error: Ambiguous Command. This is because 
the string entered could be completed to more than one command and is therefore ambiguous. 
Pressing <Tab> at the beginning of a command line behaves like a regular tab, and unlike ?, does not 
display a list of available commands. 
The following table shows examples of string completion.  
Level 
String  
Possibilities for Completion 
Result After Pressing <Tab> 
file 
show c 
show configuration-files 
show copy 
show co 
file 
show con 
show configuration-files 
show configuration-files<space> 
config>flows 
class 
classifier-profile 
classifier-profile<space> 
config>sys 
name 
name 
name 
config 
mgm 
No possibilities 
mgm 
config>flows 
flows# flow my-f 
my-flow-1 
my-flow-2  
my-flow-  
config>flows 
flows# flow my-flow-1 
my-flow-1 
my-flow-1<space>  
ETX-2i Devices 
4. Configuration and Management Methods 
Level 
String  
Possibilities for Completion 
Result After Pressing <Tab> 
config>flows 
flows# flow my-flow-3 
No possibilities 
my-flow-3 
This is a new flow, as my-flow-3 
did not exist before. 
Interactive Help 
To get interactive help, enter ?. 
In general, typing a ? directly after a string displays possibilities for string completion, while typing 
<space> and then a ? displays possibilities of the next argument. 
When a <CR> appears in a ? list, the string you entered is itself a valid command needing no further 
additions. Pressing <Enter> executes the command or navigates to the indicated level. 
Entering ? immediately after a command or partial command with no space before the ?, tells ETX-2i to 
display all possibilities for completing the string. Help output is always followed by the string you typed 
with the cursor at the end of the string waiting for input. 
ETX-2i>config>flows# classifier-profile myclass m? 
match-any 
ETX-2i>config>flows# classifier-profile myclass m 
ETX-2i>admin# fact? 
factory-default-all            - Return to factory default and reboot 
factory-default                - Return to factory default configuration and 
                                 reboot  
ETX-2i>admin# fact 
ETX-2i>admin# factory-default? 
factory-default-all             - Return to factory default and reboot  
 <CR> 
ETX-2i>admin# factory-default 
Current configuration will be erased and device will reboot with factory default 
configuration. Are you sure   ? [yes/no] _ 
When a string cannot be completed, ETX-2i displays “cli error: Invalid Command”. 
ETX-2i>admin# stac? 
# cli error: Invalid Command 
ETX-2i>admin# stac 
 
ETX-2i>file# da ? 
# cli error: Invalid Command 
ETX-2i>file# da 
Entering <?> after a space between a command or level name and the ? tells ETX-2i to display 
possibilities of the next argument. If the string preceding the ? is ambiguous or invalid, an explanatory 
message is displayed. The string does not have to be a complete command. 
ETX-2i Devices 
4. Configuration and Management Methods 
If there is only one possible command starting with that string, pressing <Enter> executes the command. 
If there is more than one command that starts with the string, the CLI displays a message that it can’t 
clarify which command you want. 
ETX-2i>admin# factory? 
 
factory-default-all              - Return to factory default and reboot 
factory-default                  - Return to factory default configuration                                    
                                   and reboot 
A command followed by a ? without a space, shown above, returns a list of possible completions. The 
same command followed by a space and then ? returns an ambiguous command message. This means 
the string entered could be completed to more than one command and is therefore ambiguous, as 
shown below.  
ETX-2i>admin# factory ? 
# cli error: Ambiguous Command 
ETX-2i>admin# factory 
A string that is a complete command name followed by a space ? displays all possible command 
parameters. 
ETX-2i>config>flows# show ? 
      summary                - Displays list of flows 
ETX-2i>config>flows# show  
ETX-2i>config>flows# classifier-profile ? 
 <classification-n*>  : [1..32 chars] 
ETX-2i>config>flows# classifier-profile  
The next example shows a complete command to which a parameter could be appended. It also shows 
how a string that is a complete command is executed by pressing <CR> or <Enter>. 
ETX-2i>config>access-control# resequence access-list acl_1 ? 
 <CR> 
 <number>             : [0..100000] 
The next example shows a complete command that has no parameters. 
ETX-2i>config>flows# classifier-profile myclass match-any ? 
 <CR> 
ETX-2i>config>flows# classifier-profile myclass match-any  
Scheduling CLI Commands 
You can schedule the execution of CLI commands at a future date and time. By default, no scheduling is 
configured. 
The global schedule command is used to configure the scheduling of a command. You can specify any 
command to be scheduled except the logout command.  
ETX-2i Devices 
4. Configuration and Management Methods 
When you schedule a command, before saving it, ETX-2i prefixes the command with the path from 
which the schedule command was executed. To specify a CLI command with a full CLI level path, you 
should schedule it at the CLI root level. 
To save the schedule command, run the commit command. 
ETX-2i tests the command that is configured as scheduled in the same way that it would be tested when 
executed; if the tests fail, you are notified of this, but the command is still scheduled, since it may be 
valid when the scheduled time arrives. 
The following types of schedules can be configured: 
in <minutes> 
Executed once, after the specified number of minutes. This type of schedule is not 
saved in nonvolatile (permanent) ETX-2i memory; it is deleted at device reboot whether 
or not it was executed. 
at <date-and-time> 
Executed once at the specified date and time. This type of schedule can be optionally 
saved in permanent memory, in order to be available after device reboot. 
 
Note 
Schedules for date and time are saved in the system local time. If the local time 
changes, ETX-2i does not modify the schedules to compensate for the change; 
therefore, changing the time can cause schedules to be executed twice or not 
executed at all.  
Schedules are marked as finished after they are executed.  
When executing scheduled commands, ETX-2i assumes a Yes answer for any confirmation questions. 
When a scheduled command is executed, it is sent to TACACS+ and Syslog accounting, as if it were 
executed by a CLI user. 
Configuring Command Scheduling 
 To schedule a command: 
• 
In any level, enter the schedule command according to the type of schedule: 
 
In <minutes> – Enter: 
schedule <name> in <minutes> “<command>” 
The schedule is saved with its name set to <name>, and the specified <command> is 
executed after the specified amount of <minutes> has elapsed, regardless of changes to the 
local system time.  
Range for <minutes>: 1–14400 [10 days] 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
 
At <date-and-time> – Enter: 
schedule <name> at {january | february | march | april | may | june | july | august | 
september | october | november | december} <dd> <yyyy> <hh>:<mm> <command> 
[volatile | nonvolatile] 
The schedule is saved with its name set to <name> (in permanent memory if nonvolatile was 
specified), and the specified <command> is executed at the specified date and time. If the 
local system time is changed after the schedule is configured, the scheduled command 
might not be executed, or might be executed twice. 
 
Note 
• 
An invalid date and time is not allowed; however, a date and time in the 
past is allowed; a schedule with its date and time in the past will never be 
executed unless the device date/time is changed such that the schedule 
date and time is no longer in the past.  
• 
Schedules can be added or deleted, but not changed. If you wish to 
change the details of a schedule, you have to delete it and then recreate it 
with the changes. 
 To delete schedules: 
• 
To delete a specific schedule, in any level enter: 
no schedule <name> 
• 
To delete all finished schedules, navigate to the admin scheduler level and enter: 
clear-finished-schedules 
Viewing Scheduling Information 
You can view the following scheduled information: 
• 
Commands, with or without details of the commands 
• 
Daylight saving time (For an explanation on the configuration of daylight savings time, refer to 
Daylight Saving Time in the Timing and Synchronization chapter.) 
Note 
You can also enter the info command from the root of the device to view all 
commands of the device, including scheduled commands (see Viewing the 
Device Configuration below).  
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
 To view scheduling without command details: 
• 
Navigate to the admin scheduler level and enter: 
show scheduler 
ETX-2i# admin scheduler 
ETX-2i>admin>scheduler# show scheduler 
Current date: 27 December 2014 00:01 (UTC +2) 
 
Schedule Name                     Type       Prm  Fin  Activation 
--------------------------------------------------------------------------- 
sched-1                           Once (In)  No   No   1 day, 02:00:10 
sched-2                           Once (At)  Yes  Yes  -- 
sched-n                           Once (At)  Yes  No   1 October 2015 12:21 
 
Summer Time 
Start (Recurring): Last Sunday of May, 02:00 
End   (Recurring): Last Thursday of October, 02:00 
Offset           : 60 minutes 
Start       : 31 May 2015 12:21 
End         : 25 October 2015 12:21 
 To view scheduling with command details: 
• 
Navigate to the admin scheduler level and enter: 
show scheduler-details 
ETX-2i# admin scheduler 
ETX-2i>admin>scheduler# show scheduler-details 
Current date: 16 September 2014 10:45 (UTC +2) 
Schedule Name               : sched-1 
Type                        : Once (At) 
Permanent                   : Yes 
Finished                    : No 
Activation (Local Time)     : 22 March 2015 09:00 
Activation In(Seconds)      : 186 days 22:45:00 
Command: copy log tftp://1.1.1.1 
 
Schedule Name               : sched-2 
Type                        : Once (In) 
Permanent                   : No 
Finished                    : No 
Activation In(Seconds)      : 207 days 12:45:00 
Command: copy log tftp://1.1.1.1 
 
Summer Time 
Start (Recurring): Last Sunday of May, 02:00 
End   (Recurring): Last Thursday of October, 02:00 
Offset           : 60 minutes 
Start       : 31 May 2015 12:21 
End         : 29 October 2015 12:21 
Offset      : 60 
ETX-2i Devices 
4. Configuration and Management Methods 
 
Parameter 
Description 
Current date 
Current date and time, and current offset from UTC 
Schedule Name 
Name of schedule 
Type  
Type of schedule: 
Once (In) – to be executed in specified number of minutes 
Once (At) – to be executed at a specified date and time 
Prm/Permanent 
Indicates if schedule is saved in permanent memory 
Fin/Finished 
Indicates if schedule is marked as finished 
Activation 
In output of show scheduler, indicates the amount of time before the scheduled 
command will be executed, according to the type of schedule: 
Once (In) – Amount of time before the scheduled command will be executed, in the 
form <hh:mm:ss>, <1 day hh:mm:ss> or <ddd days, hh:mm:ss> 
Once (At) – Date and time at which the scheduled command will be executed 
For either type, -- is displayed if the schedule is marked as finished. 
Activation (Local 
Time) 
In output of show scheduler-details for schedule type Once (At), displays the date and 
time at which the scheduled command will be executed. 
Activation In 
(Seconds) 
In output of show scheduler-details for schedule types Once (In) and Once (At), displays 
the amount of time before the scheduled command will be executed. 
Command 
In output of show scheduler-details, displays the scheduled command. 
Start (Date) 
For one-shot daylight saving time scheduling, displays daylight saving time start date and 
time. 
End (Date) 
For one-shot daylight saving time scheduling, displays daylight saving time end date and 
time. 
Start (Recurring) 
For recurring daylight savings time scheduling, displays the configured week of the 
month, weekday, month, and time for daylight saving time start. 
End (Recurring) 
For recurring daylight savings time scheduling, displays the configured week of the 
month, weekday, month, and time for daylight saving time end. 
Start 
For recurring daylight savings time scheduling: 
If the device is currently not in daylight saving time, displays the next scheduled date 
and time for daylight saving time to start. 
If the device is currently in daylight saving time, displays the date and time at which the 
daylight savings time started. 
ETX-2i Devices 
4. Configuration and Management Methods 
Parameter 
Description 
End 
For recurring daylight savings time scheduling, displays the next scheduled date and 
time for daylight saving time end. 
Offset 
Number of minutes to move the clock during daylight saving time 
Configuration Errors 
The following table lists the messages generated by the device when a command scheduling 
configuration error is detected. 
Message 
Cause 
Corrective Action 
Schedule with this name 
already configured 
You tried to create a new schedule with a 
name that is used by an existing schedule. 
Specify a name that is not being used 
by an existing schedule. 
Warning: Scheduled 
command failed sanity 
The command that you specified to 
schedule may fail when executed. 
Check the command; if changes are 
needed, delete the schedule, and 
re-enter it with the changed 
command. 
The logout command 
may not be scheduled 
You specified the logout command as the 
command to schedule. 
None. You are not allowed to schedule 
the logout command. 
Viewing the Device Configuration 
You can enter the info command at the device root, to view all commands that have been configured for 
the device. This includes scheduled commands, as they are global commands. See Examples below. 
 To view commands of a device: 
• 
At the device root, enter info.  
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Refreshing Output 
You can specify that ETX-2i should periodically refresh the output of a show command. 
 To periodically refresh the output of a show command: 
• 
Append refresh [<sec>] to the command. The allowed range for <sec> is 3–100 seconds 
(default is 5 seconds). 
ETX-2i enters refresh mode and displays the output of the command periodically, along with an 
indication of how to exit refresh mode, at the interval specified by <sec>. You cannot enter any 
commands while ETX-2i is in refresh mode. 
 To exit refresh mode: 
• 
Enter <ESC> or press <Ctrl>+C. 
The example below shows the result of refreshing the status of an Ethernet port every 15 seconds and 
pressing <Ctrl>+C after the status is displayed twice. 
Note 
The following example uses a slot number to reference the port, which may 
not be applicable to every device.  
 
ETX-2i# configure port eth 1/1 
ETX-2i>config>port>eth(1/1)# show status refresh 15 
Name ETH-1/1 
 
Administrative Status        : Up 
Operational Status           : Up 
Connector Type               : SFP In 
Auto Negotiation             : Complete 
Speed And Duplex             : 1000 FX Full Duplex 
MAC Address                  : 00-20-D2-ED-01-35 
 
SFP 
--------------------------------------------------------------- 
Connector Type                : LC                                               
Manufacturer Name             : EOPTOLINK INC                                    
Manufacturer Part Number      : EOLS161280DIQRAD                                 
Manufacturer CLEI Code        : E5PSN24ACF      or    Not Available 
SFP Manufacture Date          : 30 Mar 2009                                      
SFP Serial Number             : S95F090018                                       
Typical Maximum Range (Meter) : 80000                                            
Wave Length (nm)              : 1590.00                                          
Fiber Type                    : SM                                               
 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
RX Power (dBm)              : -4.58 dBm 
TX Power (dBm)              : 1.21 dBm 
Laser Bias (mA)             : 7.293 mA 
Laser Temperature (Celsius) : 42.00 C 
Power Supply (V)            : 3.27 V 
To exit the refresh-mode press ESC or Ctrl+C 
Filtering Output 
Some commands, such as info and show display large amounts of information as their output. It is 
possible to control the type and amount of information displayed by filtering the output. 
To filter a command’s output, append to the command: 
 | [include | exclude | begin] <filter-expression> 
Keyword 
Description 
include 
The output includes only lines that match the filter expression. 
exclude 
The output includes only lines that do not match the filter 
expression. 
begin 
The output starts with the first line that matches the filter 
expression and continues with all further lines. 
<filter-expression> 
A filter expression is a regular expression that defines what to 
exclude, include or match at the beginning. Filter expressions can 
contain letters, numbers, and metacharacters (see below). Filter 
expressions are case sensitive. 
One and only one keyword is allowed. If no keyword is specified, no filtering is performed. 
The following example illustrates filtering output. 
ETX-2i>config>system# info detail | include date 
    date-and-time 
        date-format yyyy-mm-dd 
Filter Metacharacters 
Metacharacter 
Description 
Example 
. 
Matches any single character. 
r.t matches the strings rat, rut, and r t, but not 
root. 
$ 
Matches the end of a line. 
device$ matches the end of the string header 
device but not the string header device-name. 
ETX-2i Devices 
4. Configuration and Management Methods 
Metacharacter 
Description 
Example 
^ 
Matches the beginning of a line. 
^device matches the beginning of the string 
device loaded from but not the string header 
device-name. 
* 
Matches zero or more occurrences of 
the preceding character.  
.* means match any number of any characters. 
\ 
This character is used to treat the 
following metacharacter as an ordinary 
character. 
\$ is used to match the $ character rather than 
match the end of a line. 
\. is used to match a period rather than match 
any single character. 
[ ]  
[c1-c2]  
[^c1-c2] 
Matches any one of the characters 
between the brackets. 
Ranges of characters are specified by a 
beginning character (c1), a hyphen, and 
an ending character (c2); multiple 
ranges can be specified as well. 
To match any character except those in 
the range, use ^ as the first character 
after the opening bracket. 
r[aou]t matches rat, rot, and rut, but not ret. 
[0-9] matches any digit. 
[A-Za-z] matches any upper or lowercase letter. 
[^269A-Z] matches any character except 2, 6, 9, 
and uppercase letters. 
| 
Logical OR two conditions together 
(band|comp) matches the lines bandwidth cir 
999936 cbs 65535 and compensation 0. 
+ 
Matches one or more occurrences of 
the character or filter expression 
immediately preceding it. 
9+ matches 9, 99, and 999 
“” 
Matches the string enclosed in the 
quotation marks. The string may 
include spaces. See Regular Expression 
Syntax. 
“e s” matches "double star" 
{i}  
{i,j} 
Matches a specific number (i) or range 
(i through j) of instances of the 
preceding character. 
A[0-9]{3} matches A followed by exactly three 
digits, i.e., it matches A123 but not A1234. 
[0-9]{4,6} matches any sequence of 4, 5, or 6 
digits. 
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
Regular Expression Syntax 
A filter expression is a regular expression. A regular expression can be composed of characters and 
metacharacters. Any combination of metacharacters can be used. If you want spaces as part of the filter 
expression, enclose the expression with quote metacharacters. All characters found after a space not 
enclosed by quotes are ignored by the CLI. 
The following table provides some examples of regular expressions and the resulting string that will be 
used to filter the CLI output. 
Regular Expression 
Resulting Filter String 
“str” 
str 
“s t r” 
s t r 
“str 
“str 
“str\”str” 
str”str 
“str\”str 
“str\”str 
“str”str 
str 
\”str” 
\”str” 
“str1” | include str2 
First expression – str1, second expression – str2 
 
Enabling Entities 
Some dynamic entities are created as inactive by default. After the configuration is completed, the 
no shutdown command activates the entity, as shown below. 
Note 
The example uses a slot number to reference the port, which may not be 
applicable to every device.  
 
ETX-2i# configure flows flow flow1 
ETX-2i>config>flows>flow(flow1)$ ingress-port ethernet 0/3 
ETX-2i>config>flows>flow(flow1)$ egress-port ethernet 1/1 queue 1 block 0/1 
ETX-2i>config>flows>flow(flow1)$ classifier Classifier1 
ETX-2i>config>flows>flow(flow1)$ no shutdown 
ETX-2i>config>flows>flow(flow1)$exit 
ETX-2i>config>flows# 
The shutdown command is also used to deactivate/disable a hardware element (such as a port), while 
no shutdown enables/activates it. 
ETX-2i Devices 
4. Configuration and Management Methods 
Using Scripts 
CLI commands can be gathered into text files. They may be created using a text editor, by recording the 
user commands or by saving the current configuration. 
These files can be configuration files or scripts. Configuration files have specific names and contain CLI 
commands that ETX-2i can use to replace the current configuration, while scripts contain CLI commands 
that add to the current configuration. Configuration files can be imported from and exported to RAD 
devices via file transfer protocols. 
For more information on configuration files, refer to the description in the Administration chapter. 
In order to execute a CLI script, you have to copy/paste it to the CLI terminal or send it to ETX-2i via the 
RADview Jobs mechanism, CLI script option. 
To execute a script, run the commit command. 
Examples 
 To schedule copying a log file in two hours: 
schedule sched-copy-2hrs in 120 “copy log tftp://1.1.1.1” 
 To schedule copying a log file on April 2 at 6:00, with the schedule saved in permanent memory: 
schedule sched-copy-Apr2 at april 2 2015 06:00 “copy log tftp://1.1.1.1” permanent 
save 
 To schedule shutdown of the device in five minutes: 
ETX-2i#config>flows>flow(v100in)$ schedule sched1 in 5 “shutdown”  
 To display commands configured for the device (including scheduled shutdown command): 
ETX-2i# info 
. 
Bridge Configuration 
        bridge 1 
            name "BRIDGE 1" 
            echo "Bridge Port Configuration" 
#           Bridge Port Configuration 
            port 1 
                spanning-tree 
                    cost 10 
                    no shutdown 

## 4.6 GUI-Based Configuration  *(p.288)*


## 4.7 SNMP-Based Network Management  *(p.288)*

ETX-2i Devices 
4. Configuration and Management Methods 
                exit 
                no shutdown 
            exit 
            port 2 
                spanning-tree 
                    cost 20 
                    no shutdown 
                exit 
                no shutdown 
            exit 
schedule "sched1" in 5 "configure flows flow v100in shutdown" 
ETX-2i#  
4.6 GUI-Based Configuration 
ShelfView is an SNMP-based application with fully FCAPS-compliant element management. It displays a 
dynamic graphic representation of the device panel(s), providing an intuitive, user-friendly GUI. 
ShelfView includes port and/or card interfaces and their operational and communication statuses. 
ShelfView is distributed as an executable (*.exe) file. It can be run under Windows 7 and Windows 8 
with Java Runtime Environment 1.7.0 and above. The application (and its online help) is available via 
RAD partners.  
Refer to the ETX-2i Standalone ShelfView Online Help. 
4.7 SNMP-Based Network Management 
Preconfiguring ETX-2i for SNMP Management 
ETX-2i can be managed by any SNMP-based network management system, such as via the RADview 
network management system, provided IP communications is possible with the management system, as 
well as by the standalone RADview systems. 
To manage ETX-2i from a remote NMS, it is necessary to preconfigure the basic parameters using a 
supervision terminal connected to the ETX-2i CONTROL DCE port. RAD recommends Layer-3 
management access via the out-of-band Ethernet management port. 
ETX-2i Devices 
4. Configuration and Management Methods 
 To configure ETX-2i for management access: 
1. Add an SVI port. 
2. Create classifier profiles for matching all traffic and matching untagged traffic. 
3. Add two flows (incoming and outgoing) connecting the out-of-band Ethernet management port 
and the SVI. 
4. Add a router interface, bind it to the SVI, and add a static route to the next hop. 
The following script provides the necessary configuration steps for ETX-2i, ETX-2i-B, ETX-2i-10G, and 
ETX-2i-100G. Replace IP addresses and entity names with values suitable for your network environment. 
#*******************************Adding_SVI********************* 
config port  
  svi 92  
    no shutdown 
exit all 
 
#***************************Adding Classifier_Profiles*********  
config flows 
  classifier-profile all match-any match all 
  classifier-profile untagged match-any match untagged 
 
#***************************Configuring_Flows****************** 
  flow mng_in 
    classifier untagged 
    no policer 
    ingress-port ethernet 0/101 
    egress-port svi 92 
    no shutdown 
  exit  
 
  flow mng_out 
    classifier all 
    ingress-port svi 92 
    egress-port ethernet 0/101 queue 0 block 0/1 
    no shutdown 
exit all 
#*********************Configuring_Router_Interface************* 
configure router 1 
  interface 1 
    bind svi 92 
    address 172.18.141.39/24 
    no shutdown 
  exit 
  static-route 172.17.0.0/16 address 172.18.141.1 
exit all 
commit 
save 
ETX-2i Devices 
4. Configuration and Management Methods 
Working with RADview 
Overview 
RADview is a Windows- or Linux-based modular, client server, scalable management system that can be 
used in a distributed network topology or single-station configuration. RADview features Element 
Manager System (EMS) functionality (referred to as ‘system’) and the following optional modules: 
• 
Domain Orchestrator –creates, configures, and manages virtual machines on the x.86 D-NFV 
module within RAD’s customer edge devices. Domain Orchestrator accommodates the Network 
Planning functionality, which is part of RADview-Service Manager, and enables offline planning 
of networks with RAD products. 
• 
Service Manager (SM) – end-to-end intuitive, error-free Carrier Ethernet service provisioning for 
Ethernet and TDM products; calculates the shortest path.  
• 
Performance Monitor (PM) – portal for service SLA monitoring for both carriers and their 
customers. 
RADview supports the following optional modules and functionalities for ETX-2i products, as described 
in the following table: 
Modules/ Functionalities 
ETX-2i 
ETX-2i-B 
ETX-2i-10G 
ETX-2i-100G 
Service Manager (SM) 
✓ 
✓ 
✓ 
 
Performance Monitor (PM) 
✓ 
✓ 
✓ 
 
Domain Orchestrator 
✓ 
✓ 
 
 
Tasks 
✓ 
✓ 
✓ 
 
Faults 
✓ 
✓ 
✓ 
 
ShelfView 
EMS (desktop client) 
EMS (desktop client) 
EMS (desktop 
client) 
 
RADview includes a CORBA northbound interface, enabling easy integration into the customer’s 
umbrella NMS.  
 
 
ETX-2i Devices 
4. Configuration and Management Methods 
CORBA provides the following benefits: 
• 
Enables interconnectivity and communication across heterogeneous operating systems and 
telecommunication networks.  
• 
Effectively supplies a software interface that defines data models used between various 
management layers. 
• 
Supports multi-vendor distributed network management applications, providing the data 
interface between clients and servers. 
For more details about the RADview network management software, and for detailed instructions on 
how to install, set up, and use RADview, refer to the RADview (Windows) User’s Manual or contact your 
local RAD partner. 
Preconfiguring for Service Manager  
You can discover services via RADview, and view statistics for services and ports in the RADview 
Performance Monitoring portal. This also allows you to ensure that SLAs are met. 
• 
Discovery can be performed only on the user port (UNI). 
• 
Multi-port E-Line services cannot be discovered, and statistics cannot be collected on flows. 
• 
All flows belonging to the same service endpoint must use the same port. 
• 
Only one S-tag should be used for a service. 
 To preconfigure ETX-2i for service discovery, perform the following: 
1. Configure the service with parameters that enable RADview to recognize the flows that 
correspond to the service, as follows: 
 
Configure Rx and Tx traffic flows with the same service name. For configuration instructions, 
refer to the service-name command under Configuring a Flow under Traffic Processing. 
 
Assign the above Rx and Tx flows to the MEP corresponding to the service, by running flow 
uni-direction rx <rx-name> [ tx <tx-name>] or flow bi-direction <name> under 
config>oam>cfm>mep(<mepid>). For a detailed explanation, refer to Configuring 
Maintenance Endpoints in the Monitoring and Diagnostics chapter.  
Note 
The service name configuration is necessary only in the endpoint devices.  
2. Enable PM collection for the Rx and Tx flows, as well as for the corresponding destination NE. 
For full description and configuration instructions, refer to Performance Management in the 
Monitoring and Diagnostics chapter. 
To run the RADview Discovery Service function, refer to the RADview online help. 
ETX-2i Devices 
4. Configuration and Management Methods 
Working with other SNMP-Based NMS 
ETX-2i can be integrated into third-party network management systems at the following levels: 
• 
Viewing device inventory and receiving traps   
• 
Managing device, including configuration, statistics collection, and diagnostics, using the 
following standard and private MIBs:  
 
CFM MIB (IEEE8021-CFM-MIB) 
 
IANAifType-MIB 
 
IETF Syslog Device MIB 
 
IEEE8023-LAG-MIB 
 
MEF-R MIB 
 
RAD private MIB 
 
RFC 2819 (RMON-MIB) 
 
RFC 2863 (IF-MIB) 
 
RFC 3273 (Remote Network Monitoring MIB) 
 
RFC 3411 (SNMP-FRAMEWORK-MIB) 
 
RFC 3413 (SNMP-TARGET-MIB) 
 
RFC 3414 (SNMP-USER-BASED-SM-MIB) 
 
RFC 3415 (SNMP-VIEW-BASED-ACM-MIB) 
 
RFC 3418 (SNMPv2-MIB) 
 
RFC 3433 (ENTITY-SENSOR-MIB) 
 
RFC 3636 (MAU-MIB) 
 
RFC 4133 (ENTITY-MIB) 
 
RFC 4668 (RADIUS-AUTH-CLIENT-MIB) 
 
RFC 4836.MIB (MAU-MIB) 
 
RFC 4878.MIB (DOT3-OAM-MIB) 
 
 

## 4.8 NETCONF-Based Network Management  *(p.293)*

ETX-2i Devices 
4. Configuration and Management Methods 
4.8 NETCONF-Based Network Management 
The ETX-2i family of products supports full NETCONF. NETCONF transactions support includes: 
On-the-fly modifications 
If changing without shutdown / no shutdown is needed, it can be done 
internally by the device, but NETCONF is unaware of it. 
Multiple instances in the same RPC 
Takes into consideration the scale limits (such as max flows, etc.) 
Roll back on error 
For global tests 
Hierarchical delete 
Deletes entities in lower levels, without sanity check 
 
NETCONF transactions support the CLI configuration levels in the following table. 
Level 1 
Level 2 
Level 3 
Level 4 
configure 
 
 
 
 
bridge 
 
 
 
vlan 
 
port 
 
qos 
 
 
 
policer-profile 
 
policer-aggregate 
 
shaper-profile 
 
queue-block-profile 
 
 
queue 
queue-group-profile 
 
 
 
queue-block 
port 
 
 
 
ethernet 
 
flows 
 
 
classifier-profile 
 
 
match 
flow 
 
ETX-2i Devices 
4. Configuration and Management Methods 
For a full explanation and instructions on how to configure and monitor ETX-2i devices using NETCONF, 
refer to the NETCONF-based Network Management documentation (using Google Chrome).  
The credentials are as follows: 
Username: help 
Password: help 
 