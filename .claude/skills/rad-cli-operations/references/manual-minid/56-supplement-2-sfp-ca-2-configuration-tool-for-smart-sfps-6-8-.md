# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 6.8 User Access

*Manual `MiNID_ver_2_6_mn.pdf`, pages 135–137.*


## Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 6.8 User Access  *(p.135)*

6. Management and Security 
 To configure the SNMP communities: 
Do one of the following: 
• 
In the web interface, go to Configuration > System > Management > SNMP 
MiNID 
  
 
 
 Configuration>System>Management>SNMP 
  
 
 
 Community Read/Write 
 
private 
 Community Read only 
 
public 
 Community Trap 
 
public 
  
 
 
SNMP Communities 
a. Set Community Read/Write to the name of a community with read/write authorization. 
b. Set Community Read only to the name of a community with read-only authorization. 
c. Set Community Trap to the name of a community for sending traps. 
d. Click <Apply> to implement the changes, and then click <Save Configuration>. 
• 
In the CLI, go to the config>mngmnt>snmp level, and enter the following command: 
snmp community {rw|ronly|trap} <name> 
Where: 
 
rw – indicates configuring read/write community to <name> 
 
ronly – indicates configuring read-only community to <name> 
 
trap – indicates configuring trap community to <name>. 
6.8 User Access 
Two user accounts exist for both of the two configuration interfaces (web and CLI). The usernames are 
fixed: 
• 
su: Superuser account with permission for all configuration. 
• 
user: Read-only user. Can view all current configuration. 
6. Management and Security 
The initial password for both accounts is: 1234. For better security, change the password as explained 
below. 
Up to four user sessions are accepted by the device at any one time. It is recommended not to exceed 
one web session at a time, which means that you can have one web session and three more CLI sessions 
simultaneously. 
As the superuser (su), you can modify the username and password for both user accounts (su and user). 
As the read-only user, you cannot configure your password. The following procedure is for the superuser 
to change credentials. 
 To configure the user accounts: 
Do one of the following: 
• 
Use the web interface: 
a. In the web interface, go to Configuration> System > Management > User Access: 
The User access screen appears. If you are logged in as the superuser, you can change your 
password or the read-only user password. If you’re logged in as the read-only user, you cannot 
modify any parameters. 
MiNID 
  
 
 
 Configuration>System>Management>User Access 
  
 
 
 User Level 
 
Super User 
 User Name 
 
su 
 Old Password  
 
**** 
 New Password  
 
 
 Confirm New 
Password 
 
 
  
 
 
 
User Access – Logged In as Superuser 
6. Management and Security 
MiNID 
  
 
 
 Configuration>System>Management>User Access 
  
 
 
 User Level 
 
User 
 User Name 
 
user 
  
 
 
 
User Access – Logged In as Read-Only User 
b. In User Level, select Super User or User, according to which user credentials you wish to 
configure. 
c. Define the User Name. 
d. Type the Old Password, type the New Password and Confirm it. 
e. Click <Apply> to implement the changes, and then click <Save Configuration>. 
• 
Use the CLI: 
a. Log into the CLI as the superuser, and go to the config>mngmnt level. 
b. To define the username and password of the superuser, enter: 
user <new username> level su password <new password> 
c. To define the username and password of the regular user, enter: 
user <new username> level user password <new password> 
If you’re logged in as the read-only user (not the superuser), the command user is not 
available. 
Note 
Make sure not to assign the same username to the super user and the 
read-only user. 
 
You can view the current usernames by going to the config>mngmnt level and entering show users. 