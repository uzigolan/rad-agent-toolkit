# 7 Resiliency and Optimization

*Manual `MP-1-mn_ver 2.2.pdf`, pages 269–280.*


## 7.1 Fault Propagation  *(p.269)*

Service reliability in Megaplex-1 is based on the following resiliency features: 
•
Fanless operation
•
Dual power supply and NNI ports
•
Hitless PW protection.
7.1 Fault Propagation  
The fault propagation function can be used to notify equipment at a far end port that a fault condition 
has been detected at a local port connected to it.  
Fault propagation response in Megaplex-1 is set at the factory and cannot be configured by the user. 
For each entity type, the following table lists: 
•
Failure or alarm conditions at this (failed) entity used to initiate a response at another (affected)
entity
•
Response (action) at this entity when it is affected.
Fault Propagation Response 
Entity Type 
Detected Failure or Alarm 
Condition 
Action at the Entity when it is Affected 
E1/T1 (unframed mode) 
•
AIS/LOS/OOF is observed on
the port
•
L-BIT is received over the PW and
“fe_rx_failure” alarm is generated on the
corresponding PW in the remote device.
•
AIS generated as a result of receiving L-BIT
(when working with framed E1/T1)

## 7.2 PW Protection  *(p.270)*

Megaplex-1 
7. Resiliency and Optimization 
Entity Type  
Detected Failure or Alarm 
Condition 
Action at the Entity when it is Affected  
E1/T1 (framed mode) 
• AIS/LOF/OOF is observed on 
the port 
• PW “fe_rx_failure” alarm is generated on 
the coresponding pw (only if a single E1/T1 
port is connected to this pw, direct or 
indirect mode ) 
PW (SATOP) 
• Local failure/ Remote failure 
• AIS is automatically  generated and sent to 
the corresponding e1/t1 port 
PW (CESoPSN) 
• Local failure/ Remote failure 
• OOS is automatically  generated and sent to 
the corresponding e1/t1 port 
• AIS is automatically  generated and sent to 
the corresponding ds1-opt port 
• The DCD signal of the corresponding serial 
port is dropped. 
 
 
 
7.2 PW Protection  
PW protection mechanism protects pseudowire traffic in case of network path failure. The user defines 
different network paths for the working and protection pseudowires.  
Benefits 
The PW protection provides the following main advantages: 
• 
Automatically restores service within a short time without user intervention 
• 
Provides zero packet loss protection 
• 
In case of technical failure, allows service to continue while technical staff finds the source of 
the failure and corrects it. 
Moreover, when protection is used, tasks such as planned maintenance or installing modules with 
enhanced capabilities, can also be performed without disrupting service, provided a few precautions are 
taken (see below). 
Megaplex-1 
7. Resiliency and Optimization 
The maximum number of PW protection groups that can be configured in Megaplex-1 is 6. 
Standards 
PW Protection is RAD proprietary technology.  
Factory Defaults 
Megaplex-1 is supplied with PW protection disabled.  
Functional Description  
For PW protection, two PWs are connected to the same DS1 port. A typical configuration is shown in the 
figure below. 
During normal operation, the operational state of the working and protection PWs is continuously 
monitored to ensure that it is operating properly. In the case of faulty condition on one of the PWs, the 
traffic is routed to the DS1 port from the other PW, which is not suffering from faulty conditions.  
The protection mode is non-revertive. 
 
GbE
GbE
User/Data 
Port
DS1
PW #1
Working 
PW #2
Protection
 
PW Protection  
Working and Protection Port Parameters  
For two ports configured to PW protection, the following parameters must be the same for both ports: 
• 
psn type (udp-over-ip or Ethernet)  
• 
tdm-oos  
Megaplex-1 
7. Resiliency and Optimization 
• 
tdm-payload-size. 
Configuring PW Protection  
The PW protection is configured as follows. 
 To add an PW protection group: 
1. Navigate to configure protection. 
2. Type pw and enter a group number.  
The config>protection>pw(group number)# prompt is displayed.  
 To configure the PW protection group: 
• 
At the config>protection>pw(group number)# prompt, enter all necessary commands according 
to the tasks listed below: 
Task 
Command 
Comments 
Assigning a name to the 
PW protection group 
name <up to 80 characters> 
 
Administratively enabling 
TDM group 
no shutdown 
Using shutdown disables the group 
Adding working and 
protection PW to the PW 
protection group   
bind  {working | protection} 
<pw-number> 
 
 
Using no bind protection removes the 
protection port from the group. There is 
no need to remove the working port 
from the group.  
Defining operation mode 
of the PW protection 
oper-mode  1-plus-1  
Permanently set to 1-plus-1  
Example  
 To add and configure a PW protection group: 
• 
Protection group number – 4 
• 
Working PW number – 1 
• 
Protection PW number – 2 
Megaplex-1 
7. Resiliency and Optimization 
config# protection 
config>protection# pw 4 
config>protection>pw(4)$ bind working 1 
config>protection>pw(4)$ bind protection 2 
config>protection>pw(4)$ no shutdown 
 To delete PW protection group 4: 
#configure protection no pw 4 
Viewing the PW Protection Status  
This section illustrates the status display of a PW protection group. 
 To view the PW protection group status:  
• 
At the config>protection>pw (<group-id>)# prompt, enter show status. 
The PW protection group status appears. In this example, the PW protection group ID is 1.  
config>protection# pw 1 
config>protection>pw(1)# show status 
Group 
----------------------------------------------------------------------
-- 
Mode                  : 1+1 
Administrative Status : Up 
Last Command          : None 
 
PWs 
----------------------------------------------------------------------
-- 
Working    PW  Admin Oper            Active 
----------------------------------------------------------------------
-- 
Protection pw8 Up    Down            -- 
Working    pw7 Up    Up              Yes  
 
config>protection>pw(1)# info 
    bind protection 8 
    bind working 7 
    no shutdown 

## 7.3 TDM Group Protection  *(p.274)*

Megaplex-1 
7. Resiliency and Optimization 
Configuration Errors 
The following table lists the messages generated by Megaplex-1 when a configuration error is detected. 
 
Message 
Description 
PW protection: Fail to configure PW 
protection 
Database problem. Try to reconfigure PW protection. 
PW protection: PW should be in no-
shutdown state 
You cannot set protection between PWs in “shutdown” state. 
PW protection: PW XC should be 
configured for working member 
Working PW must have a cross-connect configured on it. 
PW protection: PW XC shouldn't be 
configured for protection member 
Protection PW cannot have a cross-connect configured on it. 
PW protection: PW already member in 
other group 
One PW cannot participate in two protection groups. 
PW protection: working and 
protection PWs must be different 
A PW cannot be set as working and protection in the same 
pw group. 
PW protection: Can't delete members, 
pw group must be in shutdown state 
To delete members of a PW protection group, you have to 
set it to “shutdown”. 
PW protection: Fail to delete pw 
protection group 
Database problem. Try to delete PW protection group again. 
PW protection: Working and 
protection pws should be configured 
for the pw group. 
To configure a protection PW group, you have to configure 
both working and protection PW. 
PW protection: Can't delete a PW if it 
is a protection member. 
You cannot delete a PW used in a PW protection group. 
7.3 TDM Group Protection  
One of the simplest methods to protect against link and hardware failure is to use the TDM group 
protection. This type of protection is used for DS1 ports connected to user ports carrying traffic. 
The maximum total number of TDM groups that can be configured for Megaplex-1 is 6.  
Megaplex-1 
7. Resiliency and Optimization 
Benefits 
The TDM group protection provides two main advantages: 
• 
Automatically restores service within a short time without user intervention 
• 
In case of technical failure, allows service to continue while technical staff finds the source of 
the failure and corrects it. 
Moreover, when protection is used, tasks such as planned maintenance, updating software versions, or 
installing modules with enhanced capabilities, can also be performed without disrupting service, 
provided a few precautions are taken (see below). 
Standards 
TDM Group Protection is RAD proprietary technology. 
Factory Defaults 
Megaplex-1 is supplied with TDM protection disabled. Other parameter defaults are listed in the table 
below.  
Parameter  
Default Value 
oper-mode  
dual-cable-tx 
revertive/no revertive 
revertive 
wait-to-restore  
300 sec 
Functional Description  
The TDM group (dual-cable) configuration provides protection against both transmission path failure 
and technical failure in the module hardware.  
For this type of protection, the user/data traffic is transmitted to both DS1 ports (parallel Tx mode). 
Defining these two ports as a TDM protection group ensures that traffic carrying capacity is available 
even if one of the ports fails.  
A typical configuration is shown in the figure below. 
Megaplex-1 
7. Resiliency and Optimization 
GbE #1
GbE #2
User/Data 
Port
DS1 #1
Working 
DS1 #2
Protection
 
TDM Group Protection  
During normal operation, the operational state of the working and protection ports is continuously 
monitored to ensure that they are operating properly. If the working port fails, the traffic is routed to 
the corresponding user/data port from the protection port.  
The maximum switching time between main and backup ports is 50 msec. Therefore protection 
switching will ensure essentially uninterrupted service for all the types of applications; in particular, it 
will not cause the disconnection of voice calls.  
The protection mode is non-revertive. 
Working and Protection Port Parameters 
For two ports configured to TDM group protection, the following parameters must be the same for both 
ports:  
• 
Admin Status 
• 
frame-type  
• 
signaling.  
Protection Mode 
The recovery mode after a protection switching can be selected in accordance with the application 
requirements: 
• 
Non-revertive mode – the module will not automatically flip back from protection to working 
port after the working port returns to normal operation, but only when the currently used port 
fails. 
• 
Revertive mode – the module will flip back from protection to working port when it returns to 
normal operation.  
To prevent switching under marginal conditions, the user can specify a restoration time (wait-to-
restore). This is the minimum interval before flipping back to the original port. During the restoration 
Megaplex-1 
7. Resiliency and Optimization 
time, alarms with the same weight, or with lower weights, are ignored. As a result, the module starts 
evaluating the criteria for protection switching (flipping) only after the restoration time expires, thereby 
ensuring that another flip cannot occur before the specified time expires.  
However, if an alarm with a weight exceeding that of the alarm which caused flipping appears, 
immediate flipping will occur, even if the restoration time has not yet expired. 
Configuring TDM Group Protection  
The TDM Group Protection is configured as follows. 
 To add a TDM protection group: 
1. Navigate to configure protection. 
2. Type tdm-group and enter a group number.  
The config>protection>tdm-group(group number)# prompt is displayed. 
 To configure the TDM protection group: 
• 
At the config>protection>tdm-group(group number)# prompt, enter all necessary commands 
according to the tasks listed below: 
Task 
Command 
Comments 
Administratively enabling 
TDM group 
no shutdown 
Using shutdown disables the group 
Defining operation mode 
of the TDM group 
oper-mode dual-cable-tx 
This string is optional (this is the only 
option) 
Adding working and 
protection ds1/e1/t1 
ports to the TDM group  
bind  {working | protection} 
{ds1|e1|t1}  1/<port 1..12> 
 
Enabling the reverting 
from the protection port 
to the working port  
revertive 
Using no revertive disables the 
reverting 
 
Defining the wait-to-
restore period (after the 
switching criteria are 
cleared, the time to 
elapse before traffic 
switches back) 
wait-to-restore <0–720> 
 
 
The unit of time is seconds. This 
parameter is relevant only for revertive 
mode. 
Megaplex-1 
7. Resiliency and Optimization 
Task 
Command 
Comments 
Forced switching of 
traffic from the working 
port to the protection 
port 
force-switch-to-protection 
 
 
Manual switching of 
traffic from the 
protection port back to 
the working port, unless 
a failure condition exists 
on the working port or an 
equal/higher priority 
switch command is in 
effect 
manual-switch-to-working 
 
 
 
 
 
Forced switching of 
traffic from the working 
port to the protection 
port, unless a failure 
condition exists on the 
protection port or an 
equal/higher priority 
switch command is in 
effect 
manual-switch-to-protection 
 
 
Clearing the force switch 
command 
clear  
Once the force-switch command is 
cleared, the ports returns back to 
normal operation. 
 To remove a TDM protection group: 
• 
Type no tdm-group followed by the group number.  
Example  
 To add and configure TDM protection group: 
• 
Protection group number – 1 
• 
Working link – DS1 port 1 
• 
Protection link – DS1 port 2 
Megaplex-1 
7. Resiliency and Optimization 
• 
Operation mode – dual cable protection (this is the only option so the 3rd string is optional)   
# configure protection tdm-group 1 bind working ds1 1/1 
# configure protection tdm-group 1 bind protection ds1 1/2 
# configure protection tdm-group 1 oper-mode dual-cable-tx 
 To display the protection status: 
MP-1>config>protection>tdm-group(1)# show status 
Group 
--------------------------------------------------------------- 
Mode                   : Dual Cable Tx 
Administrative Status  : Up 
Last Switchover Reason : None 
Last Command           : 
 
Cards 
--------------------------------------------------------------- 
           Port                   Admin    Oper     Active 
Working    DS1         1/1        Up       Up     Yes 
Protection DS1         1/2        Up       Up     -- 
Configuration Errors 
The following table lists messages generated by Megaplex-1 when a configuration error is detected. 
Message 
Description 
TDM GROUP: Manual switch is not 
allowed before clear 
After previous use of “manual switch” or “force switch” 
commands, you have to use “clear” before using another 
“manual switch” command. 
TDM GROUP: Working and protection 
DS1 are the same 
The same port cannot be defined as both working and 
protection port 
TDM GROUP: The same DS1 exist in 
two different TDM Group 
A DS1 port cannot be member of several TDM protection 
groups. 
TDM GROUP: Different types of DS1 
frame in the same TDM Group 
When TDM protection is configured between two DS1 ports, 
all their physical layer parameters (admin, frame type, 
signaling) must be identical 
TDM GROUP: Different types of DS1 
signaling in the same TDM Group 
When TDM protection is configured between two DS1 ports, 
all their physical layer parameters must be identical 
Megaplex-1 
7. Resiliency and Optimization 
Message 
Description 
TDM GROUP: Different admin status of 
DS1 in the same TDM Group 
When TDM protection is configured between two DS1 ports, 
all their physical layer parameters must be identical 
TDM GROUP: DS0 cross connect exists 
on protection DS1 
DS1 port cannot be configured as protection port if a cross-
connect is configured on it. 
TDM GROUP: Different line types in 
the same TDM Group  
When TDM protection is configured between two ports, their 
line types must be identical 
 