# B Integration with Actility TPE

*Manual `SecFlow-1p_6.4_Mn_05-26_GA.pdf`, pages 776–787.*


## B.1 Actility ThingPark Enterprise Platform  *(p.776)*

Integration with Actility TPE 
B.1 Actility ThingPark Enterprise Platform
ThingPark Enterprise (TPE) platform is a scalable and easy to use and manage LoRa Network Server (LNS) 
platform. TPE can be deployed as SaaS or On-premise (OCP) platform.  More information can be found 
at the following link: https://www.actility.com/enterprise-iot-connectivity-solutions/  
An example of using Actility ThingPark Enterprise GUI is shown in the figure below. 
IoT Platforms
& Applications
ThingPark Enterprise
ecFlow-1p
LORA
https, MQTT, AWS IoT,
Azure IoT, ThingWorx,
Cumulocity, etc.
Geolocation
Roaming
Reliable multicast
& FUOTA
High Availability
Device payload 
drives
&
Cloud 
connectors
Network
Server
Join
Server
Device & BS
Management
Connectivity Management Platform
for dedicated LoRaWANTM Networks
SaaS, Private Cloud or 
On premise deployment
Business Applications
& Cloud Connections

## B.2 SecFlow-1p Integration to Actility TPE  *(p.777)*

RAD’s SecFlow-1p can be easily connected to Actility TPE for efficient LoRa management. Actility LRR 
(Long-Range Relay) is running on SecFlow-1p as a Docker Container. LRR converts LoRaWAN sensor 
messages to IP packets and forwards them to TPE, with optional TLS encryption.  
The solution below describes how LoRaWAN sensors communicate with Actility ThingPark Enterprise 
(TPE) via Actility LRR installed on SecFlow-1p.  
The solution is similar for TPE-SaaS and TPE-On-Premise. 
Note 
This release version includes integration to Actility on-premise only, Actility 
SAAS integration will be part of the next release. 
B.2 SecFlow-1p Integration to Actility TPE 
In this section we describe the procedure of LoRaWAN Integration to Actility ThingPark OCP On-premise 
platform, illustrating it with a specific example of a LoRa sensor (see the diagram below). 
The solution includes the following steps:  
• 
Using SecFlow-1p CLI: 
 
Configuring the router (IP address to OCP server and NTP server IP address) 
 
Accessing LRR as Linux user 
• 
Using the LRR SUPLOG configuration utility (Actility utility installed in Docker): 
 
Configuring Actility LRR (OCP server IP address)  
 
Inserting the SecFlow-1p UUID into OCP server (copy & paste the UUID from LRR Suplog) 
• 
Using Actility TPE: Setting SecFlow-1p as a base station and defining a sensor. 
8. 
The following sections describe the above steps in detail. 
Configuring the SecFlow-1p CLI 
 To configure the CLI: 
1. Configure the SecFlow-1p router and NTP server 
configure router 1 interface 32 address 172.18.92.249/24 **IP address to OCP server** 
configure system date-and-time ntp server 1 address 172.18.92.174 **IP address to NTP 
server** 
configure system date-and-time ntp server 1 no shutdown 
2. Create a Linux user:  
configure management login-user Actility_user level linux-tech 
configure management login-user Actility_user password 9999 
### Loging as username= su  password=1234 
ThingPark Enterprise
Actility Server
OCP On-Premise
Substation
IEC 61850 
Certified
LoRa IO 
Controller
Sensor 
Transformers
Load Break
Switch
Circuit 
Breakers
LoRa IO 
Controller
LoRa IO 
Controller
Actility LRR
Docker
SecFlow-1p
LORA
Option for Fiber or Cellular
Backhaul
3.
Login with new user level 'linux-tech':
#  admin login
username: Actility_user
password: 9999
user>Actility_user
docker1@localhost's password: 9999
The LRR application (SUPLOG) opens.
Actility Menu Setting – SUPLOG 
The SUPLOG menu provides two functions:  
•
Reading the SecFlow-1p UUID
•
Entering the IP address to Actility OCP server
 To activate the Actility SUPLOG utility:  
1.
Login to Actility SUPLOG level with the linux-tech user
2.
Activate SUPLOG by entering the following command: root@localhost:/$ docker exec -it
actility-lrr-v4 /home/actility/lrr/suplog/suplog.x
The following menu appears:
3. The LRR UID (or LRR UUID) is the LRR unique identifier. To retrieve it from the Suplog menu, 
browse to Identifiers, then Get LRR UUID 
LRR UID is displayed at the third line (UID=) 
 
4. Copy the UID into ThingPark Enterprise Actility Server 
Important! Copy paste the UID and keep it for future use when creating a new base station on 
Actility Local server.  
 To configure the IP address to reach the OCP server: 
1.
Go to SUPLOG main menu and select System Configuration:
2.
Go to System Configuration> Backhaul from the Main Menu
3.
Update the ‘Backhaul’ IP address (IP address of TPE OCP server) in all the rows below:
•
LRC0 address
•
FTP/SFTP download 0
•
FTP/SFTP upload 0
•
Rev SSH 0
4.
Click ‘Confirm’ to activate the application.
Creating a new Base Station 
Now we will define our SecFlow-1p device as an Actility TPE base station. 
 To define a new base station: 
1.
Navigate to https://enterprise.actility.local
2.
Select 'Base Stations' > 'Create'.
3.
Select RAD as the base station manufacturer.
4.
Fill in the base station information:

Model* = SecFlow-1p

Name* = Your gateway name (any value)

LRR-UUID*= Your gateway LRR UUID taken previously from the gateway SUPLOG menu

RF Region*= AU 915(8 channels:CH8-CH15)
5.
Click 'Create' to activate the configuration.
The UUID appears on the Actility OCP server.  
 
 
Creating the Device (Sensor)  
In this example we show how to create a new sensor (RAK811_A). 
1. Select Devices > Create. 
2. Select 'LoRaWAN' generic. 
 
3. Configure the relevant parameters: 
 
Model* = LoRaWAN 1.0.2 revA - class A 
 
Name* = RAK811_1_AU915Mhz_channel_8_15  (can be any value) 
 
DevEUI*= 60C5A8FFFE7841BA 
 
Activation mode* = Over-the-Air activation (OTAA) with local join Server 
 
JoinEUI(AppEUI)* = 60C5A8FFF86808BA 
 
AppKey* = 60C5A8FFF86808BA60C5A8FFF86808BA 
*DevEUI, AppEUI and AppKey values are available from the sensor manufacturer 
4. Click 'Create' to activate the device. 
 
The sensor is defined and can be now displayed in the Dashboard: 
 