# 5 Ports

*Manual `ETX-1p_6.4_Mn_05-26_GA.pdf`, pages 205–272.*


## (chapter introduction)  *(p.205)*

ETX-1p supports the following port types:  
• 
Physical: Ethernet (including SFP), Cellular 
• 
Virtual and internal Ethernet  
• 
VLAN 
 To display the operational summary for all ports:  
1. At the prompt config>port#, enter:  
show summary 
The ports operational status is displayed.  
config>port# show summary 
Panel               Name                     Admin  Oper      Speed 
----------------------------------------------------------------------------- 
Ethernet wan1       Ethernet wan1            Down   Down      0 
Ethernet wan2       Ethernet wan2            Down   Down      0 
Ethernet lan1       Ethernet lan1            Down   Down      0 
Ethernet lan2       Ethernet lan2            Up     Up        100M 
Ethernet lan3       Ethernet lan3            Down   Down      0 
Ethernet lan4       Ethernet lan4            Up     LLD       0 
Ethernet switch1    Ethernet switch1         Up     Up        0 
Cellular lte        Cellular lte             Down   Down      0 
2.4G                2.4G                     Up     Up        0 
Virtual 1           Virtual 1                Down   Down      0 
Virtual 2           Virtual 2                Down   Down      0 
Virtual 3           Virtual 3                Down   Down      0 
Virtual 4           Virtual 4                Down   Down      0 
Virtual 5           Virtual 5                Down   Down      0 
Virtual 6           Virtual 6                Down   Down      0 
Virtual 7           Virtual 7                Down   Down      0 
Virtual 8           Virtual 8                Down   Down      0 
Virtual 9           Virtual 9                Down   Down      0 
Virtual 10          Virtual 10               Down   Down      0 
 
 
 

## 5.1 Cellular Ports  *(p.206)*

5. Ports 
 
5.1 Cellular Ports   
ETX-1p supports the cellular modem interface (LTE module) in both PPP and Eth/DHCP modes of 
operation.  
Applicability and Scaling 
This feature is applicable to ETX-1p with LTE ordering options. 
The number of supported APNs in the multi-APN mode is up to 4. 
Standards Compliance 
ETSI TS 127 060 (3GPP TS 27.060) 
3GPP TS 29.061 
RFC 1661  
The Point-to-Point Protocol (PPP)  
3GPP TS 23.060 
Functional Description 
Packet Domain Access Interfaces and Reference Points 
The following figure shows the packet domain access interfaces and reference points. 
5. Ports 
 
In the above diagram, the Cellular dongle is the Modem Termination (MT), and the Terminal Equipment 
(TE) is the ETX-1p cellular interface.  
The cellular interface also includes configuration for the cellular modem (MT), such as the pin code. 
IP-Based Services 
In a mobile network using Long Term Evolution (LTE) architecture, bearers are the tunnels used to 
connect the user equipment to Packet Data Networks (PDNs) such as the Internet. In practice, bearers 
are concatenated tunnels that connect the user equipment to the PDN through the Packet Data 
Network Gateway (P-GW). 
3G PPP supports bearers (tunnels) with IP-based services. 
The ETX-1p cellular interface supports two IP-based service modes:  
• 
PPP relay mode – Underlying Layer-2 is PPP. 
• 
Ethernet/DHCP mode – Underlying Layer-2 is Ethernet. 
PPP Relay Mode 
The following figure illustrates IP bearer in PPP relay mode. 
5. Ports 
 
IP-Based Services: PPP Mode 
In this mode, PPP is negotiated between Terminal Equipment (TE) and the modem with Link Control 
Protocol (LCP) and Internet Protocol Control Protocol (IPCP) to obtain the interface IP address. 
As TE transmits an IPCP request from an IP address, the modem relays this request to the network, and 
as soon as it receives an answer, it responds to TE. 
After the establishment of the connection, data is transmitted in PPP frames. 
 
Note 
ETX-1p supports PPP negotiation of IPv4 addresses only.  
 
PPP negotiation is illustrated in the following figure. 
5. Ports 
 
Ethernet/DHCP Mode 
The following figure illustrates IP bearer in Ethernet/DHCP mode. 
5. Ports 
 
 
In this mode, TE opens a transparent channel to the GGSN and obtains its IP address by DHCP with the 
GGSN. After the IP address is obtained, the channel is used for data transfer over Ethernet packets. 
 
Note 
ETX-1p supports DHCPv4 for IPv4.  
 
The following diagram illustrates DHCPv4 negotiation. 
5. Ports 
 
Cellular Interface IP Address 
As part of the network synchronization process, the modem cellular interface obtains dynamically an IP 
address from the network. 
Receive Signal Strength Indicator (RSSI)  
RSSI measures in a single figure both the usable signal and the noise (in dBm), with -50 a perfect signal 
and -120 when you fall off the network. 
• 
High signal: -50 to -75 dBm 
• 
Medium signal: -76 to -90 dBm 
5. Ports 
• 
Low signal: -91 to -100 dBm 
• 
Poor signal: -101 to -120 dBm 
Cellular Group (Dual SIM) Protection  
Cellular interface supports dual SIM protection. Each of the SIM cards may operate in a different 
operation mode (PPP relay or IP).  
Once enabled (cellular group set to ‘no shutdown’), the redundancy mechanism will select which SIM 
would be the active one.                                     
The redundancy mechanism is operating according to the following scheme: 
1. The Primary and Secondary interfaces are assigned by the user. 
2. The device tries to connect to the Primary interface. 
3. The device disconnects from the primary interface upon the following events: 
 
SIM failure (see ‘SIM failure’ definition below) declared after reconnect tryouts during 
‘connect-timeout’ time  
 
Interface (SIM) shutdown 
4. The modem is reset and tries to connect to the secondary interface. Once connected: 
 
If revertive mode is configured, the device is reset and tries to move back to the primary 
interface upon time-to-revert expired  
 
If non-revertive is considered, the device is reset and tries to move back to the primary 
interface upon the secondary interface failure. 
 
5. Ports 
 
 
Once the active cellular interface is changed, the Router Interface IP address is deleted, and a new IP 
address is learned from the new active cellular interface. 
The SIM failure is declared upon on of the following: 
• 
Oper status is ‘Down’ 
• 
No registration or registration denied for ‘connect-timeout’ period (the device could not 
reconnect) 
• 
RSSI is below the minimum threshold for ‘connect-timeout’ period 
• 
No IP is retrieved from cellular network for ‘connect-timeout’ period (the device could not 
reconnect) 
Dual Modems  
The devices supporting two modems (according to the ordering options) feature dual modem 
functionality. In this mode each of the two modems is represented by a dedicated SIM and can connect 
to another cellular network or cellular provider. 5.1The two modems are working simultaneously and 
independently from one another. Each of the modems is bound to a different IP interface (Router 
Interface).  
5. Ports 
 
 
The two modems are always ‘ON’, the traffic redirection and redundancy mechanisms are at the IP level. 
The configuration refers to the cellular interface in the case of Dual modem in the following way: 
• 
Modem 1: ‘lte-1’ 
• 
Modem 2: ‘lte-2’  
Multi-PDN (Multi-APN)  
The Multi-PDN (Multiple Packet Data Network) functionality allows the user to have more than one 
simultaneous WAN connection on a single SIM card by connecting to multiple APNs (Access Point 
Name). Multiple PDNs may be used to support access to both public/private networks, split billing, etc. 
Each PDN receives its own IP address allowing each PDN to be configured independently. For example, 
the first PDN could be configured as a public network, and the second as a private network, as shown in 
the figure below. The number of supported APNs in the multi-APN mode is up to 4. 
 
5. Ports 
 
 
With multi-apn mode activated, some of the cellular port parameters are configured on the individual 
APN level, as shown in the command trees below.  
Factory Defaults 
By default, cellular ports have the following configuration. 
Parameter 
Description 
Default Value 
radio-access-technology 
2G/3G/4G access permissions 
2g/3g/4g  
dialer-number 
Cellular network dialer number 
*99# 
name 
Cellular interface name 
cellular#1 
pin 
SIM PIN code 
0 
queue-group 
Attaching queue group profile to the 
port 
no queue-group 
rssi-threshold 
RSSI thresholds for TCA event 
-100 (lower threshold) -90 
(higher threshold) 
shutdown 
Disconnect/connect modem from 
cellular network 
shutdown 
 
5. Ports 
Parameter 
Description 
Default Value 
shutdown 
shutdown/no shutdown of the 
cellular protection group 
shutdown 
revertive/non-revertive  
Revertive mode for the protection 
group 
revertive 
time-to-revert (minutes)  
The time to stay on the secondary 
cellular interface before trying to 
reconnect back to primary (revertive 
mode) 
240 
connect-timeout (sec) 
Time of the failure persisting before 
switching to the standby SIM  
30 
Configuring a Cellular Port (via CLI) 
 To configure the cellular interface:  
1. Configure the cellular interface parameters (see below). 
2. If one of the SIM’s operates in Ethernet/DHCP mode, configure the router interface with DHCP 
enable (refer to Configuring Router Interfaces). 
3. Bind the cellular interface to the router interface (refer to Configuring Router Interfaces). 
 
 To configure the cellular port parameters:  
1. Navigate to the following: 
 
configure port cellular lte to configure the single cellular port 
 
configure port cellular lte-1 to configure the first cellular port for a dual modem device 
5. Ports 
 
configure port cellular lte-2 to configure the second cellular port for a dual modem device. 
2. Enter all necessary commands according to the tasks listed below.  
Important! 
Any change in the port parameters must be accompanied by shutdown 
command, followed by no shutdown. 
 
Task 
Command 
Comments 
Configuring the cellular 
protection level 
cellular-protection 
See Configuring Cellular Protection 
Clearing cellular interface 
counters of the active SIM 
clear statistics 
 
Configuring cellular 
interface name 
name <interface-name> 
no name <interface-name> 
interface-name – cellular interface 
name; character string 
Configuring cellular 
modem operation mode, 
either single SIM (#1 or #2) 
or dual SIM protection 
mode 
mode {dual-sim | sim { 1 | 
2}} 
Default: dual-sim  
 
 
Configuring the sim level 
sim  
See Configuring the SIM level 
Displaying the cellular 
connection status of the 
active SIM 
show status 
 
Saving/removing the 
Network Connectivy 
configuraton 
no shutdown 
shutdown 
• no shutdown – The Network 
Connectivy configuration is saved; 
used later to configure PPP or WWAN 
when binding the interface to an 
upper layer interface (such as Router 
Interface).  
• shutdown – The Network Connectivy 
configuration is removed. 
Note 1: When the Network Connectiviity 
configuration is removed, the oper status 
alarm turns on; and when it is saved, the 
alarm turns off. 
Note 2: To reduce power consumption, 
each cellular modem can be 
reset/shutdown independently.  
5. Ports 
Configuring Cellular Protection 
If you selected the dual-sim mode, you can configure the following cellular protection parameters. 
 To configure cellular protection:  
1. At the prompt config>port>cellular(<port-index>)#, enter: 
cellular-protection 
The system switches to the cellular-protection context. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Select revertive or non revertive 
SIM redundancy scheme 
 
[no] revertive 
 
Traffic is switched back to the primary 
port after it recovers. 
no revertive sets the port recovery mode 
to non-revertive. Traffic continues being 
transmitted over the secondary port 
after the primary port recovers. 
Configuring the primary sim in the 
cellular protection scheme 
 
primary-sim {1 | 2}  
Select primary SIM in the protection 
scheme  
Default: 1 
Setting the time to stay on the 
secondary cellular interface 
before switching back to primary 
(revertive mode in dual SIM 
redundancy) 
time-to-revert <minutes> 
 
 
The primary port resumes transmitting 
traffic once the link has been restored 
and the specified time has elapsed. 
Possible Values: 2..14,400 minutes 
Setting the time before switching 
to the standby SIM  
connect-timeout <seconds> 
 
Possible values: 30..600 seconds 
Configuring the SIM Level  
Two SIM cards can be relevant for dual sim protection, each having different network configuration. 
Some of the parameters are configured on the specific SIM level. 
 To configure the SIM level: 
1. At the prompt config>port>cellular(<lte, lte-1, lte-2>)>, enter: 
sim # 
The system switches to the sim context. 
5. Ports 
4. Perform the required tasks according to the following table. 
 
 
Task 
Command 
Comments 
Configuring SIM cellular 
provider Access Point Name 
(APN)  
 
[no] apn-name <name> 
 
name – SIM cellular provider APN   
For example: apn-name 
internet.golantelecom.net.il 
The APN contains the settings to set up a 
connection to the gateway between your 
carrier's cellular network and the public 
Internet (or private network) 
Leaving APN name blank (or setting ‘no apn-
name’) allows the cellular network to 
determine the correct APN  
Configuring individual APNs on 
the apn level (if multi-apn was 
selected) 
 [no] apn <apn-index>  
This command is valid only if multi-apn was 
selected.  
See Configuring the APN Level below 
Configuring cellular network 
dial sequence 
dialer-number <dial-
string> 
dial-string – cellular network dialer number. 
The modem uses this number in the ATD 
command to dial into the cellular network to 
set up a data call. 
Possible values: string (excluding the ATD 
string) 
Configuring SIM PIN code 
pin <pin-number> 
pin-number – SIM PIN code number 
Possible values: 0-9999 
Notes: 
• Required for a locked SIM. Pin code is 
required to allow the modem (MT) to 
communicate with the SIM. 
• When you configure a PIN, you should 
configure the modem with this code 
(AT+CPIN). 
5. Ports 
Task 
Command 
Comments 
Configuring type of cellular 
network that modem can 
connect to  
radio-access-technology 
<access-technology> 
 
access-technology – allowed radio access 
technology for this modem 
Possible values:  
• 2g, 3g, 4g, 2g/3g, 3g/4g, 2g/3g/4g 
(default) 
Note 1: The configuration applies according 
to the modem capabilities. For example, for a 
3G modem, the default 2G/3G/4G is NA (only 
3G is possible). For a 2G/3G modem, the 
2G/3G/4G configuration is actually 2G/3G. 
 
Configuring RSSI thresholds for 
TCA event  
rssi-threshold <low-
threshold>  <high-
threshold> 
low-threshold – When RSSI goes below this 
value, a TCA event is issued to indicate too 
low receive power. 
Possible values: -50 to -120 dBm 
high-threshold – When RSSI goes above this 
value, a TCA event is issued to indicate 
receive power recovered. 
Possible values: -50 to -120 dBm 
Selecting LTE bands enabled on 
the modem 
 
 
lte-bands <band1> 
[<band2>] [<band3>]  
[<band4>] [<band5>] 
[<band6>] 
This configuration limits the LTE bands the 
modem is allowed to work with. Up to 6 
bands can be selected.  
This parameter is relevant if 'radio-access-
technology' includes 4G 
Possible Values for different ordering options:  
• L1: b1, b3, b5, b7, b8, b20, b38, b40, b41, 
any 
• L3: b1, b2, b3, b4, b5, b7, b28, b40, any 
• L4: b2, b4, b5, b12, b13, b14, b66, b71, 
any 
• L5: b1, b3, b8, b8, b18, b19, b26 
• LTA: b2, b4, b5, b12, b13, b14, b25, b26, 
b66, b71  
• L450A: b3, b7, b20, b31, b72  
• L450B: b3, b20, b87  
Default: b3 
If ‘any’ is selected, the modem will connect 
automatically to the band it has detected.  
5. Ports 
Task 
Command 
Comments 
Configuring PDP type to set 
data call mode per 3GPP 
definitions 
pdp-type {ip | relayed-
ppp}  
 
Default: ip 
Configuring CHAP hostname 
chap-hostname <name> 
[no] chap-hostname 
[name] 
name –CHAP hostname  
Possible values: 1-80 character string 
This command is valid when pdp-type is ip 
Configuring CHAP default 
password 
chap-password 
<pass> [{hash}] 
[no] chap-password 
[name] 
pass – CHAP password 
Possible values: 1-40 character string 
hash – password encrypted 
Possible values: hash, “” 
Notes:  
• Valid when pdp-type is ip 
• If you enter a clear password (chap-
password), the device encrypts it, saves 
the encrypted password in 
pppSecuritySecret and sets 
pppSecuritySecretType to ‘off’. 
• If you enter an encrypted password (chap-
password hash) the device saves the 
encrypted password in pppSecuritySecret 
and sets pppSecuritySecretType to ‘off’. 
Enabling multiple APN 
configurations 
[no] multi-apn 
 
Default: no multi-apn 
Configuring the SIM name 
name <name> 
no name [name] 
name – SIM name 
Possible values: 1-80 character string 
5. Ports 
Task 
Command 
Comments 
Configuring PAP credentials 
(not when pdp-type is ip) 
 
pap-username <name> 
password <pass> [{hash}] 
[no] pap-username 
[name] 
name – PAP username; string 
Possible values: string up to 80 characters 
pass – PAP password 
Possible values: string up to 80 characters 
Notes:  
• If you enter a clear password (pap-
password), the device encrypts it, saves 
the encrypted password in 
pppSecuritySecret and sets 
pppSecuritySecretType to ‘off’. 
• If you enter an encrypted password (pap-
password hash) the device saves the 
encrypted password in pppSecuritySecret 
and sets pppSecuritySecretType to ‘off’. 
Refusing CHAP authentication 
(not when pdp-type is ip) 
[no] refuse-chap 
 
Refusing PAP authentication 
(not when pdp-type is ip) 
[no] refuse-pap 
 
Refusing no authentication (not 
when pdp-type is ip) 
[no] refuse-no-auth 
 
Configuring the APN Level  
Using multi-apn functionality, you can simultaneously forward the traffic over multiple APNs (PDP) to 
allow for traffic separation. In this case some of the parameters are configured on the specific APN level.  
 To configure the APN level: 
1. At the prompt config>port>cellular(<lte, lte-1, lte-2>) sim # >, enter: 
apn <apn-index>  # 
The system switches to the apn context. 
5. Perform the required tasks according to the following table. 
 
Task 
Command 
Comments 
5. Ports 
Task 
Command 
Comments 
Configuring SIM cellular 
provider Access Point Name 
(APN) in the case of multiple 
APNs 
apn-name <name> 
no apn-name [name] 
name – SIM cellular provider APN   
For example: apn-name 
internet.golantelecom.net.il 
Possible values: 1-80 character string 
Configuring PDP type to set 
data call mode per 3GPP 
definitions 
pdp-type {ip | relayed-
ppp}  
 
Default: ip 
 
Configuring CHAP hostname 
chap-hostname <name> 
[no] chap-hostname 
[name] 
name –CHAP hostname  
Possible values: 1-80 character string 
This command is valid when pdp-type is ip 
Configuring CHAP default 
password 
chap-password 
<pass> [{hash}] 
[no] chap-password 
[name] 
pass – CHAP password 
Possible values: 1-40 character string 
hash – password encrypted 
Possible values: hash, “” 
Notes:  
• Valid when pdp-type is ip 
• If you enter a clear password (chap-
password), the device encrypts it, saves 
the encrypted password in 
pppSecuritySecret and sets 
pppSecuritySecretType to ‘off’. 
• If you enter an encrypted password (chap-
password hash) the device saves the 
encrypted password in pppSecuritySecret 
and sets pppSecuritySecretType to ‘off’. 
5. Ports 
Task 
Command 
Comments 
Configuring PAP credentials 
(not when pdp-type is ip) 
 
pap-username <name> 
password <pass> [{hash}] 
[no] pap-username 
[name] 
name – PAP username; string 
Possible values: string up to 80 characters 
pass – PAP password 
Possible values: string up to 80 characters 
Notes:  
• If you enter a clear password (pap-
password), the device encrypts it, saves 
the encrypted password in 
pppSecuritySecret and sets 
pppSecuritySecretType to ‘off’. 
• If you enter an encrypted password (pap-
password hash) the device saves the 
encrypted password in pppSecuritySecret 
and sets pppSecuritySecretType to ‘off’. 
Refusing CHAP authentication 
(not when pdp-type is ip) 
[no] refuse-chap 
 
Refusing PAP authentication 
(not when pdp-type is ip) 
[no] refuse-pap 
 
Refusing no authentication (not 
when pdp-type is ip) 
[no] refuse-no-auth 
 
Viewing Cellular Port Status 
You can display the status and configuration of an individual cellular port. 
 To display the status of a specific cellular port:  
• 
At the prompt config>port>cellular(<port-index>)#, enter: 
show status 
The cellular port status is displayed differently, depending on whether multi-apn mode was 
enabled.  
For the single APN: 
Interface Status 
----------------------------------------------------------------------------- 
Name                  : Cellular lte 
Administrative Status : Up 
Operational Status    : Up 
IP Address            : 2.55.105.206 
5. Ports 
IP Gateway            : 0.0.0.0 
 
 
Cellular Modem Information 
----------------------------------------------------------------------------- 
Modem    : Manufacturer: Sierra Wireless, Incorporated Model: EM9191 
Firmware : Revision: SWIX55C_03.09.06.00 340b2d jenkins 2022/03/16 00:37:53 
Mode     : sim-1 
IMEI     : 355890340323406 
 
SIM Information 
----------------------------------------------------------------------------- 
SIM           : SIM 1 SIM 1  
SIM Status    : ready 
Provider Name : Partner 
MCC           : 1 
MNC           : 425 
IMSI          : 425010781023027 
ICCID         : 89972010219040724880 
MSISDN        : N/A 
 
 
Cellular Connectivity Information  
Cellular Network Connection: Connected 
Registration Status  
: Registered, home network 
RAT Selected               : TDD LTE 
LAC/TAC 
 
 
: 50  
Cell ID 
 
 
: 10  
Band                       : LTE Band 6 
Channel                    : 100 
Uplink BW                  : 1.4MHz 
Downlink BW  
 
: 1.4MHz 
 
 
Carrier Aggregation  
#            Scell Band               State         RSSI     RSRP    RSRQ    SINR 
             n78                      Active        -55      -92    -11      20 
 
Signal Quality 
----------------------------------------------------------------------------- 
RSSI (dBm)               : -53 
RSRP (dBm)               : -89 
RSRQ (tenths of decibel) : -15 
SINR (tenths of decibel) : 14 
 
Traffic Statistics 
----------------------------------------------------------------------------- 
Counter         Rx                   Tx 
Total packets   2996                 2195 
Total Octets    205507               188492 
5. Ports 
Packets Dropped 0                    0 
Packets Errors  0                    0 
Overflows       0                    0 
For the multiple APN: 
 
Interface Status 
----------------------------------------------------------------------------- 
Name                  : Cellular lte 
Administrative Status : Up 
Operational Status    : Up 
                              IP Address                                IP Gateway 
SIM 1  APN 1                  10.10.10.10                               10.10.10.1 
SIM 1  APN 2                  20.10.10.10                               20.10.10.1 
 
Cellular Modem Information 
----------------------------------------------------------------------------- 
Modem    : Manufacturer: Sierra Wireless, Incorporated Model: EM9191 
Firmware : Revision: SWIX55C_03.09.06.00 340b2d jenkins 2022/03/16 00:37:53 
Mode     : sim-1 
IMEI     : 355890340323406 
 
 
 
SIM Information 
----------------------------------------------------------------------------- 
SIM           : SIM 1 SIM 1  
SIM Status    : ready 
Provider Name : Partner 
MCC           : 1 
MNC           : 425 
IMSI          : 425010781023027 
ICCID         : 89972010219040724880 
MSISDN        : N/A 
 
Cellular Connectivity Information  
Cellular Network Connection 
: Connected 
Registration Status  
 
: Registered, home network 
RAT Selected                      : ENDC 
LAC/TAC 
 
 
 
: 20131  
Cell ID 
 
 
 
: 5591053 
Band                              : 7  
Channel                           : 3050 
Uplink BW                           : 5MHz 
Downlink BW  
 
 
  : 5MHz 
 
Carrier Aggregation  
#            Scell Band               State         RSSI     RSRP    RSRQ    SINR 
             n78                      Active        -55      -92    -11      20 
 
5. Ports 
Signal Quality 
----------------------------------------------------------------------------- 
RSSI (dBm)               : -53 
RSRP (dBm)               : -89 
RSRQ (tenths of decibel) : -15 
SINR (tenths of decibel) : 14 
 
Traffic Statistics 
 
APN 1 Orange  
 
Counter         Rx                   Tx 
Total packets   2996                 2195 
Total Octets    205507               188492 
Packets Dropped 0                    0 
Packets Errors  0                    0 
Overflows       0                    0 
 
APN 2 Cellcom 
 
Counter         Rx                   Tx 
Total packets   2996                 2195 
Total Octets    205507               188492 
Packets Dropped 0                    0 
Packets Errors  0                    0 
Overflows       0                    0 
 
The fields are explained in the table below. 
Parameter 
Description 
Interface Status 
 
Administative status  
Cellular interface administrative status 
Possible values:  
• Up – the port is enabled 
• Down – the port is deabled 
Operational Status 
Operation status of the cellular port  
Possible values:  
• Up – the ‘dial in’ to the network was successful and connected 
• Down – Data call is disconnected 
IP Address 
IP address acquired from the cellular network (IPCP/DHCP phase) 
Possible values: None, IPv4 address 
Note: Each time the cellular interface fails, the Interface IP address is cleared 
and set after the end of the initiated IPCP/DHCP stage. 
5. Ports 
Parameter 
Description 
IP Gateway 
The gateway IP address acquired from the cellular network 
Cellular Modem Information 
 
Modem name 
Manufacturing information of the cellular modem 
Firmware 
Modem firmware  
Mode  
 
 
Modem operation mode  
Possible Values: dual-sim, sim 1, sim 2 
This field is not displayed for a dual modem device 
IMEI  
International Mobile Station Equipment (modem HW identifier) 
SIM Information 
  
SIM 
Displays which SIM is active (SIM 1 or SIM 2), followed by the name of the 
active SIM. 
SIM Status 
 
SIM operational status 
Possible Values:  not-inserted, general-failure, ready, unknow, locked-pin-
required, locked-puk-required 
Provider Name 
Cellular provider name  
MCC  
Mobile Country Code 
MNC 
Mobile Network Code 
IMSI 
International Mobile Subscriber Identity 
ICCID  
Integrated Circuit Card Identifier: SIM serial number 
MSISDN 
 
           A number uniquely identifying a subscription in a mobile network (SIM burnt 
number) 
Cellular Connectivity 
Information  
 
Cellular network connection 
Status of cellular connection. Possible values:  
• Unknown – No modem, no SIM, SIM locked, or modem failure 
• Connecting – dial mode is either dialing or ringing 
• Connected  
• Failed 
5. Ports 
Parameter 
Description 
Registration Status 
Cellular network registration status. Possible Values: 
• Registered, home network  
• Registered, roaming 
• Not Registered, MT not searching  
• Not Registered, trying to attach 
• Denied 
• Unknown 
RAT Selected 
Radio Access Technology selected 
LAC/TAC 
Tracking Area Code 
Cell ID  
Cell ID 
Band  
Frequency Band 
Channel  
Rx Channel 
Uplink Bandwidth 
 
Uplink Bandwidth 
Possible Values:  
• Unknown, 1.4MHz, 3MHz, 5MHz, 10Mhz, 15MHz, 20MHz 
Downlink Bandwidth 
 
Downlink Bandwidth 
Possible Values:  
• Unknown, 1.4MHz, 3MHz, 5MHz, 10Mhz, 15MHz, 20MHz 
Carrier Aggregation (Relevant for Sierra modem only) 
Scell Band 
Secondary Cell Frequency Band 
Scell State 
Carrier aggregation status 
Possible Values: Active, Inactive, Disabling , Not Configured 
Scell RSSI 
 
Received Signal Strength Indication of secondary cell radio signal. Zero 
indicates not applicable 
Scell RSRP 
 
Reference signal received power (dbm) of secondary cell radio signal 
Possible Values:  -140 dBm to – 44 dBm with 1 dB resolution 
Scell RSRQ 
Reference signal received quality (db) of secondary cell radio signal 
Possible Values:  -3…-19.5dB with 0.1 dB resolution 
Scell SINR 
Signal To Interference Plus Noise Ratio (db) of secondary cell radio signal  
Possible Values:  -20…+50dB with 0.1 dB resolution 
Signal Quality 
 
5. Ports 
Parameter 
Description 
RSSI 
Received Signal Strength Indication of cellular radio signal (in dbm) 
RSRP  
Reference signal received power (dbm), applicable for LTE only 
Possible values: -140 dBm to – 44 dBm with 1 dB resolution 
RSRQ 
Reference signal received quality (db), applicable for LTE only 
Possible values: -3…-19.5 dB with 0.1 dB resolution 
SINR 
Signal To Interference Plus Noise Ratio (db), applicable for LTE only 
Possible values: -20…+50 dB with 0.1 dB resolution 
Traffic Statistics 
 
Rx Total Packets 
Number of packets received from cellular interface 
Tx Total Packets 
Number of packets transmitted to cellular interface 
Rx Total Octets 
Number of bytes received from cellular interface 
Tx Total Octets 
Number of bytes transmitted to cellular interface 
Rx packets Dropped 
Number of valid packets received from cellular interface that were dropped 
Rx packets Errors 
Number of errored packets received from cellular interface that were dropped 
Tx packets Dropped 
 
Number of valid packets at transmit direction to cellular interface that were 
dropped 
Tx packets Errors 
Number of errored packets at transmit direction to cellular interface that 
were dropped 
Tx Overflows 
Number of transmit queue overflows 
Rx Overflows 
Number of receive queue overflows 
If pdp-type is ‘relayed-ppp’, the PPP status is also displayed (for each APN if multi-apn mode was 
selected).  
PPP Status  
 
LCP 
--------------------------------------------------------------------- 
State     : Opened  
MRU Local : 1280 
Peer : 1500 
 
Authentication 
--------------------------------------------------------------------- 
Of Us : CHAP 
    State : Completed 
 
    Identity : Hostname  
 
5. Ports 
IPCP 
--------------------------------------------------------------------- 
State              : Opened 
Local Address : 20.20.20.5 
Peer Address  : 20.20.20.2 
 
Parameter 
Description 
LCP 
 
State 
 
LCP status 
Possible Values: Initial, Starting, Closed, Stopped, Closing, Stopping, Request-Sent, 
Ack-Received, Ack-Sent, Opened 
MRU Local 
Local PPP MRU size advertized in LCP negotiations 
MRU Peer 
Peer PPP MRU size received in LCP negotiations 
Authentication 
 
Of Us 
 
Authentication protocol of the device 
Possible Values: CHAP, PAP, None 
State 
Authentication phase state  
Possible Values: Initial, Completed, In Progress, Failed 
Identity 
Authentication identity  
IPCP 
 
State 
 
IPCP status 
Possible Values: Initial, Starting, Closed, Stopped, Closing, Stopping, Request-Sent, 
Ack-Received, Ack-Sent, Opened 
Local Address 
IPCP local IP address 
Peer Address 
IPCP remote IP address   
Viewing Cellular Port Status using Swagger  
ETX-1p supports Swagger, an interactive user-friendly API explorer that enables you to design, build, 
document, and simulate sending REST API calls to ETX-1p API directly from your browser.  
The documentation that you build describes what each API function does, its request parameters, and 
response objects, all without any indication of code implementation. 
5. Ports 
The Swagger UI makes an existing YAML document interactive. You can access the YAML files of each 
device per port (according to REST API), and perform operations on the YAML’s functions. It is possible 
to build functions, specify the function parameters, and what the functions do. Swagger uses these 
YAML files for documentation.  
 To retrieve the cellular port status:  
1. Configure the management: 
configure 
    management 
        login-user su 
            level virt 
            password 1234 
            no shutdown 
2. Enter the Swagger portal: 
http://<ip-address>:8008/swagger 
 
The Swagger portal opens: 
 
5. Ports 
 
 
5. Ports 
3. In the Swagger portal, above the functions, click 
. 
The Available authorizations box opens. 
 
4. Wait for some time to see the asterisks appear. 
 
5. Click the Close Button to finish authentication.  
6. Click Try it out. If you would like to get results for a specific entity, under Parameters, enter id of 
that entity. Click Execute. 
Each request in Swagger shows the equivalent Curl command. 
You can copy/paste the curl command into your computer, which has curl installed, to run the 
same API call.  
5. Ports 
 
7. If you entered the correct credentials, Server response displays Code of 200 (Successful 
operation) and Response body shows the requested information. 
 
 
 
  

## 5.2 Ethernet Ports  *(p.236)*

5. Ports 
 
 
5.2 Ethernet Ports  
ETX-1p is connected to Ethernet equipment via the following interfaces: 
• 
WAN side: one fiber GbE optic SFP transceiver (WAN1) + one electrical GbE port with the 
standard RJ-45 connectors (WAN2) 
• 
LAN side: 4 UTP (RJ-45) GbE ports 
Applicability and Scaling 
This feature is applicable to all the ETX-1p versions.  
Functional Description 
The Ethernet ports are disabled by default, with one exception. The factory default configuration 
enables and contains configuration of router 1 interface 32, attached to the last RJ-45 Ethernet port. The 
router interface is configured to non-forwarding mode, to limit it to management traffic. No VLAN is 
configured, assuming management traffic is likely to be untagged. 
5. Ports 
Internal Ethernet Ports  
An internal Ethernet port (ethernet switch1) is used as bridge port when a bridge is configured. This port 
can be bound to the router interface to represent the bridge entity in the router. The internal Ethernet 
port supports ACL/802.1X/QoS/PBR/force-next-hop/mac-access-control features. 
Quality of Service (QoS)  
ETX-1p supports QoS (traffic management) on Ethernet ports. 
Configuration of QoS requires that you first configure the Ethernet port with the following features (see 
table below):  
• 
Classifier 
• 
Traffic-class (TC) action option: 
 
Marking 
 
Traffic-classes per port: 20 
For full details on how to configure QoS, refer to Quality of Service (QoS) in the Traffic Processing 
chapter. 
MAC Access Control  
Flooding a device with MAC addresses and filling its MAC address table is a well-known attack. Bridges, 
for example, flood packets of unknown MAC destination to all ports, a process that impairs performance 
and generates excessive traffic on all ports. MAC access control allows the user to limit the number of 
source MAC addresses allowed to send traffic to a port. If you know which legitimate devices are going 
to be connected to a port, you can whitelist them, and reject other addresses. This can be done by 
entering the mac-access-control level. 
Factory Defaults 
By default, Ethernet ports have the following configuration. 
Parameter 
Description 
Default Value 
egress-mtu 
Packet size 
1790  
name 
Port name 
Ethernet <port-name> 
5. Ports 
Parameter 
Description 
Default Value 
shutdown 
Administrative status 
Shutdown  
Note: Exception is the no shutdown default 
status of the last RJ-45 Ethernet port (lan4) 
Configuring Ethernet Port Parameters  
1. Navigate to configure port ethernet <port-name> to select the Ethernet port to configure. 
Physical port names correspond to the front panel designation: wan1, wan2, lan1, lan2, lan3 and 
lan4. The internal Ethernet port name is switch1.  
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Administratively enabling 
port 
no shutdown 
Enter shutdown to disable the port. 
This command is inactive for internal 
ports. 
Binding ACL to the port 
access-group <acl-name> in 
[{ipv4 | ipv6}] 
no access-group in {ipv4 | 
ipv6} 
acl-name: 1-80 characters 
 
 
Clearing ACL statistics 
clear-access-list-statistics [in] 
[{ipv4 | ipv6}] 
 
Setting maximum frame 
size (in bytes) to transmit  
egress-mtu <68–12288> 
Frames above the specified size are 
fragmented or discarded. 
Mapping the traffic 
originated by a router 
interface to its egress port 
force-next-hop [next-hop <ip-
address>]  
no force-next-hop 
 
 
Configuring MAC access 
control 
mac-access-control 
See Configuring MAC Access Control 
below. 
Assigning description to 
port 
[no] name <port-name> 
port-name – 0-64 characters 
Note: Configured name included in 
events and traps. 
5. Ports 
Task 
Command 
Comments 
Configuring collection of 
performance management 
statistics for the port, that 
are presented via the 
RADview Performance 
Management portal 
[no] pm-collection interval 
<seconds> 
 
Note: In addition to enabling PM 
statistics collection for the ports, it 
must be enabled for the device. 
Refer to Performance Management in 
the Monitoring and Diagnostics 
chapter for details. 
Binding PBR rule to the 
port 
policy-based-route priority 
<priority> match-acl <name> 
{next-hop <ip-address>} 
interface <type, index> 
no policy-based-route priority 
<priority> 
See Configuring PBR 
 
Associating a queue group 
profile with the port 
[no] queue-group profile 
<queue-group-profile-name> 
 
Displaying ACL statistics 
show access-list statistics [in] 
[{ipv4|ipv6}] 
See Viewing Ethernet Port Statistics 
below.   
Displaying the summary of 
ACLs bound to the VLAN 
show access-list summary 
Displays ACL summary at the current 
level 
See Ethernet Port Status below. 
Displaying the port 
statistics 
show statistics  
See Viewing Ethernet Port Statistics  
Displaying the port status 
show status 
See Viewing Ethernet Port Status  
Configuring VLAN port 
vlan <vlan-id> 
 
 
 
See VLAN Ports for details on VLAN 
port configuration. 
Type no vlan <vlan-id> to delete the 
Ethernet port VLAN. 
Note: You can delete a VLAN port only 
when its administrative status is down. 
5. Ports 
Task 
Command 
Comments 
Configuration required for QoS 
Enabling classifier at the 
port level 
[no] classifier {ingress} 
ingress – classifier classification 
direction is ingress, i.e. from port to 
application. For example, router 
interface. 
Enter no classifier { ingress } to remove 
a classifier. 
For details on how to configure 
classifier parameters, refer to Port 
Classification in the Traffic Processing 
chapter.  
Defining a traffic-class 
entity  
traffic-class <tc-name> 
tc-name – traffic class name. 
Possible values: variable length string, 
up to 32 characters. 
Enter no traffic-class <tc-name> to 
remove the traffic-class entity. 
For details on how to configure traffic-
class parameters, refer to Traffic-Class. 
Configuring MAC Access Control  
 To configure MAC Access Control: 
1. Navigate to configure port ethernet <port-name> mac-access-control. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Configuring static MAC 
address  
mac <mac-address>  
no mac <mac-address> 
mac: Valid unicast MAC address 
no mac: Any hex string 
formatted as MAC address 
Disabling MAC access 
control 
[no] shutdown 
By default, MAC access control 
is disabled. 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
5. Ports 
 
Message 
Cause 
Corrective Action 
Address not found 
You tried to delete a non-existing 
static MAC address  
 
Address must be unicast MAC not 
owned by the device 
mac-address must be a valid 
unicast MAC address not owned by 
the device.  
 
 
Viewing Ethernet Port Status 
You can display the status and configuration of an individual Ethernet port. 
 To display the status of a specific Ethernet port: 
• 
At the prompt config>port>eth(<port-name>)#, enter: 
show status 
The Ethernet port status parameters are displayed. The parameters are described in the 
following table. 
 To display Ethernet port 1 status:   
# configure port ethernet wan1 
config>port>eth(wan1)# show status 
Name                  : Ethernet wan1  
 
Administrative Status : Up 
Operational Status    : Up 
Connector Type        : RJ45 Ethernet 
Speed And Duplex      : 100 Half Duplex 
MAC Address           : 00-08-A2-0B-95-58 
 To display Ethernet switch1 port status:  
config>port>eth(switch1)# show status 
Name Ethernet switch1 
 
Administrative Status : Up 
Operational Status    : Up 
Connector Type        : -- 
MAC Address           : 9A-49-55-C6-0B-F4 
5. Ports 
 
Parameter 
Description 
Name 
Port name 
Administrative Status 
Possible values: Up, Down 
Operational Status 
Possible values: Up, Down 
Connector Type 
Possible value: RJ45 Ethernet 
Speed and Duplex 
Possible values: 
-- 
10 Half Duplex 
10 Full Duplex 
100 Half Duplex 
100 Full Duplex 
MAC Address 
MAC address, formatted 00-00-00-00-00-00 
Note: Ethernet wan1 address is considered the system MAC address. It is 
used when ETX-1p host has to uniquely identify itself, such as when 
providing a MAC address on which to base the license file.  
 To display an SFP port status:   
# configure port ethernet wan1  
config>port>eth(wan1)# show status 
Name                  : Ethernet wan1 
 
Administrative Status : Up 
Operational Status    : Up 
Connector Type        : SFP in 
Speed And Duplex      : 1000 Full Duplex 
MAC Address           : 02-09-C0-95-BB-E3 
 
SFP 
---------------------------------------------------------- 
Connector Type                       : LC 
Manufacturer Name                    : RAD Data Comm. 
Manufacturer Part Number             : SFP-6D 
Typical Maximum Range (Meter)        : 10000 
Wave Length (nm)                     : 1310.00 
Fiber Type                           : SM 
 To display the ACL status of the Ethernet port: 
1. Navigate to the corresponding Ethernet port and enter show access-list summary command.  
5. Ports 
The following information is displayed: 
  
show access-list-summary 
 
ACL Name                        Type  Bound to                                Direction 
----------------------------------------------------------------------------- 
ip_port6_v4                     IPv4  Ethernet wan1                            In 
icmp_port6_v6                   IPv6  Ethernet wan1                            In 
 Viewing Ethernet Port Statistics 
The following port statistics can be displayed for an Ethernet port. The counters are described in the 
following table. 
Running 
----------------------------------------------------------------------------- 
Counter                      Rx                      Tx                    
Total Frames                 3539                    10                    
Total Octets                 236594                  1060                 
Multicast Frames             213                     --                 
Error Frames                 99999                   99999                 
Undersize Errors             99999                   -- 
 
Discard Frames               --                      99999    
 
Parameter 
Description 
Total Frames 
Total number of frames received/transmitted 
Total Octets 
Total number of bytes received/transmitted 
Error Frames 
Total number of error frames received/transmitted 
Undersize Frames 
Total number of undersize (less than 64 octets) received frames that 
were discarded 
Multicast Frames 
Total number of multicast frames received 
Discard Frames 
Total number of discarded Tx frames 
 To display the ACL statistics for the Ethernet port: 
1. Navigate to the corresponding Ethernet port and enter show access-list statistics in [{ipv4 | 
ipv6}]. 
The following statistical information is displayed: 
 

## 5.3 PPP Ports  *(p.244)*

5. Ports 
show access-list-statistics  
 
IPv4    access list:  ip_port6_v4                      (Inbound) 
 
Bound to:            Ethernet wan1 
Matches counted for: 0 days 0 hours 51 minutes 43 seconds 
 
Sequence  Action  Protocol Source    Port  Destination    Port ICMP Type Code DSCP   Log        Matches 
----------------------------------------------------------------------------------------------------------- 
10        permit    ip    172.18.92.111    172.18.92.78                             disable    (200 matches) 
 
 
show access-list-statistics in ipv6 
 
IPv6    access list:  ip_port6_v6                      (Inbound) 
 
Bound to:            Ethernet wan1 
Matches counted for: 0 days 0 hours 26 minutes 41 seconds 
 
Sequence Action Protocol Source Port            Destination Port           ICMP TypeCode DSCP Log   Matches 
----------------------------------------------------------------------------- 
10      permit  icmp     fd00:0::72e6:73f8:4b79 fd00::fd75:3fea:ecc6:a999           disable     (3 matches)  
5.3 PPP Ports 
ETX-1p supports a single Point-to-Point Protocol (PPP) session over Ethernet (PPPoE) interfaces.  
PPP provides a standard method for transporting multiprotocol datagrams over point-to-point links. 
Standards Compliance 
RFC 1332 - The PPP Internet Protocol Control Protocol (IPCP)  
RFC 1334 - PPP Authentication Protocols 
RFC 1661 - The Point-to-Point Protocol (PPP)  
RFC 1994 - PPP Challenge Handshake Authentication Protocol (CHAP) 
RFC 2516 - A Method for Transmitting PPP Over Ethernet (PPPoE) 
RFC 5072 - IP Version 6 over PPP 
5. Ports 
Functional Description 
Configuring an IPCP Address   
You can configure an IPCP address on a PPP link in the IPv4 format. 
By default no address is configured. If the address is not configured, it can be received from the peer.  
PPPoE Session Establishment 
PPPoE is used to build PPP sessions and encapsulate PPP packets over Ethernet. PPPoE is useful for 
device auto-configuration, typically for authentication.  
You can have a single PPPoE session on one router interface. 
On Ethernet interfaces, you are required to establish a PPPoE session before starting PPP negotiation 
(see PPP Negotiation below). You can establish the PPPoE session only on a router interface that is 
bound to a PPP port that is bound to an operational Ethernet port.  
 
Note 
There is no command to explicitly enable PPPoE. It is enabled on PPP ports 
that are bound to an Ethernet port.  
A PPPoE session is established as follows: 
1. ETX-1p sends a session initiation (PADI).  
 
If after sending a session initiation (PADI), ETX-1p does not receive an offer (PADO) within 
four seconds, ETX-1p resends the request (PADI) and doubles the waiting period. 
 
If ETX-1p does not receive an offer after four retries (five including the first), it restarts the 
session initiation process (i.e. resends a PADI and waits up to four seconds). 
2. When ETX-1p receives an offer (PADO), one of the following takes place: 
 
If a service name is configured, ETX-1p accepts the first offer it receives. 
 
If a service name is not configured, ETX-1p accepts the first offer it receives containing the 
same service name tag. 
3. After sending an offer (PADR), ETX-1p waits for session confirmation. 
 
If ETX-1p does not receive a session confirmation (PADS) within four seconds, ETX-1p 
resends the request (PADR) and doubles the waiting period. 
 
If ETX-1p does not receive an offer after four retries (five including the first), it restarts the 
session initiation process (i.e. resends a PADI and waits up to four seconds). 
5. Ports 
4. If a PPPoE session is terminated (receives PADT packe) or rejected, ETX-1p retries to establish a 
PPPoE session (by sending a PADI). 
5. If a PPPoE session is terminated due to a lower layer state changed to down, ETX-1p retries to 
establish a PPPoE session (by sending a PADI) as soon as the physical layer is up and there is Layer-
2 connectivity. 
PPP Negotiation 
ETX-1p negotiates a PPP session on any router interface that is bound to a PPP port (refer to Configuring 
Router Interface in the Traffic Processing chapter).  
 
Note 
If the PPP port is bound to an Ethernet port, PPP starts only after a PPPoE 
session has been established (see PPPoE Session Establishment above). If the 
PPP port is bound to a cellular port, PPP starts as soon as the cellular port is 
bound is operationally up.  
 
There are three phases in PPP negotiation: 
• 
Link establishment 
• 
Authentication (optional) 
• 
Network Control Protocols 
PPP Link Establishment Phase 
The first phase in PPP negotiation requires establishing a link. 
PPP establishes a link as follows: 
1. ETX-1p requests a Link Control Protocol (LCP), with the understanding that ETX-1p accepts the first 
legal LCP that it receives. 
 
If ETX-1p does not receive a response within four seconds, it resends the request and 
doubles the waiting period. 
 
If ETX-1p does not receive a response after four retries (five including the first), it restarts 
the LCP negotiation process (i.e. resends a configuration request and waits up to four 
seconds). 
2. If the peer rejects the LCP request, ETX-1p resends the request and doubles the waiting period.  
5. Ports 
 
If ETX-1p does not receive a response after four retries (five including the first), it restarts 
the LCP negotiation process (i.e. resends a configuration request and waits up to four 
seconds). 
3. If a PPP session is terminated due to reception of an LCP Terminate-Request packet, ETX-1p retries 
to establish a PPP session. 
4. If LCP fails, ETX-1p raises the lcp-failure alarm. 
PPP Authentication Phase 
 
Note 
Authentication is optional.  
PPP supports two authentication methods: Password Authentication Protocol (PAP) and Challenge 
Handshake Authentication Protocol (CHAP). 
CHAP is the recommended method. PAP is not secure as the username, as it passes the password in the 
clear. 
Authentication is unidirectional. The methods used to authenticate a peer are not necessarily the 
methods that a peer uses for authentication.  
ETX-1p performs PAP authentication only after  a username and password are configured. 
Chap authentication uses the challenge-response method. 
When a CHAP challenge is received, ETX-1p does the following: 
• 
If the username in the challenge matches a login-user, the login-user and its password are used. 
• 
If the username in the challenge does not match any of the login-users, the device uses the 
default CHAP password, if one is configured.  
• 
If the username does not match any of the login-users and a default CHAP password is not 
configured, the CHAP authentication fails. 
ETX-1p also supports configuration of a CHAP hostname. 
• 
By default (i.e. a CHAP hostname is not configured), ETX-1p identifies itself by its system name. 
If a CHAP hostname is configured, the device uses it to identify itself, instead of the system 
name. 
• 
ETX-1p supports configuration of the authentication methods that it may accept if requested by 
a peer.  
• 
If during the authentication phase, ETX-1p does not receive a response from the server within 
four seconds, it does the following: 
 
Resends the request and doubles the waiting period.  
5. Ports 
 
If a PPPoE session was established and ETX-1p does not receive a response after four retries 
(Five including the first), it must terminate the PPPoE session (by sending a PADT) and try 
negotiating it anew (by sending a PADI). 
PPP Network Control Protocols (NCP) Phase 
Once the authentication phase has completed successfully (or if you skipped authentication, once link 
establishment has completed successfully), ETX-1p begins the NCP phase, i.e. negotiating the set of 
supported network control protocols – IPCP and IPv6CP. 
ETX-1p performs the NCP phase, as follows: 
1. ETX-1p begins Internet Protocol Control Protocol (IPCP) negotiation. 
2. If ETX-1p does not receive a response within four seconds, it resends the request and doubles the 
waiting period. 
3. If the peer rejects IPCP, ETX-1p waits four seconds, resends the request, and doubles the waiting 
period for four retries (five including the first). 
4. If IPCP is terminated due to receiving a Terminate Request packet, ETX-1p retries to establish IPCP.  
5. ETX-1p begins IPv6 Control Protocol (IPv6CP) negotiation (same as steps 2 to 4 for IPCP 
negotiation). 
Factory Defaults 
By default, PPP ports have the following configuration. 
Parameter 
Description 
Default Value 
name 
Port name 
name “PPP <port-name>” 
refuse-chap 
Refuse CHAP authentication 
no refuse-chap 
refuse-no-auth 
Refuse no authentication 
refuse-no-auth 
refuse-pap 
Refuse PAP authentication 
refuse-pap 
pppoe 
PPPoE configuration 
pppoe 
service-name 
PPPoE service name 
no service-name 
5. Ports 
Configuring Ports 
PPP Port 
 To configure the PPP port:  
1. Navigate to configure port ppp <number> to select the PPP port to configure. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Binding PPP to a lower 
layer (Ethernet) 
[no] bind ethernet <port> 
no bind 
port – Ethernet port 
Configuring CHAP 
hostname 
chap-hostname <name> 
[no] chap-hostname [name] 
name –CHAP hostname 
Possible values: 1-80 character string 
Configuring CHAP 
default password 
chap-password 
<pass> [{hash}] 
[no] chap-password [name] 
pass – CHAP password 
Possible values: 1-80 character string 
hash – password encrypted 
Possible values: hash, “” 
Notes:  
• If you enter a clear password (chap-
password), the device encrypts it, 
saves the encrypted password in 
pppSecuritySecret and sets 
pppSecuritySecretType to ‘off’. 
• If you enter an encrypted password 
(chap-password hash) the device saves 
the encrypted password in 
pppSecuritySecret and sets 
pppSecuritySecretType to ‘off’. 
Configuring PPP IPv4 
address 
ipcp-address <ipv4-unicast-
address> 
no ipcp-address 
 
Configuring port name 
name <name> 
no name [name] 
name – port name 
Possible values: 1-80 character string 
5. Ports 
Task 
Command 
Comments 
Configuring PAP 
credentials 
pap-username <name> 
password <pass> [{hash}] 
[no] pap-username [name] 
name – PAP username; string 
Possible values: string up to 80 characters 
pass – PAP password 
Possible values: string up to 80 characters 
Notes:  
• If you enter a clear password (pap-
password), the device encrypts it, 
saves the encrypted password in 
pppSecuritySecret and sets 
pppSecuritySecretType to ‘off’. 
• If you enter an encrypted password 
(pap-password hash) the device saves 
the encrypted password in 
pppSecuritySecret and sets 
pppSecuritySecretType to ‘off’. 
Configuring PPPoE 
pppoe 
For detailed nformation on PPPoE 
configuration, see PPPoE below. 
Refusing CHAP 
authentication 
[no] refuse-chap 
 
Refusing PAP 
authentication 
[no] refuse-pap 
 
Refusing no 
authentication 
[no] refuse-no-auth 
 
PPPoE Port 
 To configure PPPoE: 
1. Navigate to configure port ppp <number> pppoe. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Configuring service 
name 
service-name <string> 
[no] service-name [string] 
service-name –service 
name 
Possible values: string up 
to 80 characters 
Displaying PPPoE status 
show status 
See Viewing Port Status 
5. Ports 
 
Note 
Changes in PPPoE port take effect only after reconfiguring the router 
interface. For workaround, proceed as follows:  
Navigate to configure > port > ppp 1, and change the value. 
Navigate to configure > router > Interface (number) and perform the 
following: 
• 
shutdown 
• 
no bind 
• 
bind ppp 1 
• 
no shutdown 
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
Message 
Cause 
Corrective Action 
Cannot execute: too 
long password 
You tried to configure an unencrypted 
password (PAP or CHAP) of more than 
80 characters. 
Shorten the password. 
Invalid IPv4 unicast 
address 
The address is not a not a valid IPv4 
unicast address 
 
Address configured on 
another interface 
The address is already configured on 
another interface 
 
Viewing Port Status 
PPPoE 
You can display the status and configuration of an individual PPP port, which is configured with PPPoE, 
provided it is bound to a router interface. 
 
Note 
If the PPP port, which is configured with PPPoE, is not bound to a router 
interface, the following output is displayed: PPP is not bound to an interface.  

## 5.4 Virtual Ports  *(p.252)*

5. Ports 
 To display status of PPP port 1 configured with PPPoE (and bound to a router interface): 
configure port ppp 1 pppoe 
config>port>ppp(1)>pppoe# show status 
Router Interface       : Router 1/If 2  
Physical Port          : Ethernet wan1  
State                  : Up 
Service Name Requested : Song 
PPP Configured with PPPoE Port Status Parameters 
Parameter 
Description 
Router Interface 
Router/router interface 
Physical Port 
Physical interface under the router interface  
Possible values: string 
State 
PPPoE state 
Possible values: Up, Down, Lower Layer Down, Admin Disabled 
Service Name Requested 
Service name 
5.4 Virtual Ports 
Virtual ports are router loopback ports. ETX-1p requires 10 predefined virtual ports. 
Applicability and Scaling 
This feature is applicable to all the ETX-1p versions. 
Benefits 
Virtual ports provide flexible binding of ports, networking functions, and virtualization layer. 
Factory Defaults 
By default, virtual ports have the following configuration. 
 
5. Ports 
Parameter 
Description 
Default Value 
name 
Assigns a port name  
no name 
Virtual # of port 
shutdown 
Sets virtual port administrative 
status 
shutdown 
Configuring Virtual Ports 
 To configure a virtual port: 
1. Navigate to configure port virtual <port-name>. 
The configure> port>virtual (<port-name>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
Administratively enabling port 
no shutdown 
Enter shutdown to disable the port. 
Setting maximum frame size  (in 
bytes) to transmit  
egress-mtu <68–12288> 
Frames above the specified size are 
fragmented or discarded. 
Mapping the traffic originated by a 
router interface to its egress port 
force-next-hop [next-hop <ip-
address>] 
no force-next-hop 
 
 
Assigning description to port 
[no] name <port-name> 
port-name – 0-64 characters 
Note: Configured name included in 
events and traps. 
Enter no name to revert the name to 
its default value (virtual < port-name>). 
Bind PBR rule to the port 
policy-based-route priority 
<priority> match-acl <name> 
{next-hop <ip-address> | 
interface <type, index>} 
no policy-based-route priority 
<priority> 
 
See Configuring PBR 
 
Displaying the port statistics 
show statistics  
See Viewing Virtual Port Statistics 
5. Ports 
Displaying the port status 
show status 
See Viewing Virtual Port Status 
Configuring VLAN port 
vlan <vlan-id> 
See VLAN Ports for details on VLAN 
port configuration. 
Type no vlan <vlan-id> to delete the 
Ethernet port VLAN. 
Note: You can delete a VLAN port only 
when its administrative status is down. 
 
Viewing Virtual Port Status 
The following port status can be displayed for a virtual port.  
Name                  : My Port 
Administrative Status : Up  
Operational Status    : Up 
MAC Address           : 41-41-42-42-43-43 
 
Parameter 
Description 
Name 
Port name 
Administrative Status 
Possible values: Up, Down 
Operational Status 
Possible values: Up, Down 
MAC Address 
MAC address, formatted 00-00-00-00-00-00 
Viewing Virtual Port Statistics 
The following port statistics can be displayed for a virtual port. The counters are described in the 
following table. 
Running 
----------------------------------------------------------------------------- 
Counter                      Rx                      Tx                    
Total Frames                 3539                    10                    
Total Octets                 236594                  1060                 
Discard Frames             --                     213                 
 
 

## 5.5 VLAN Ports  *(p.255)*

5. Ports 
Parameter 
Description 
Total Frames 
Total number of frames received/transmitted 
Total Octets 
Total number of bytes received/transmitted 
Discard Frames 
Total number of discarded Tx frames 
5.5 VLAN Ports 
ETX-1p supports the creation of VLAN ports over Ethernet and Virtual ports, thus providing single VLAN 
tag encapsulation.   
Applicability and Scaling 
This feature is applicable to all the ETX-1p versions. 
Functional Description 
VLAN port configuration is similar to Ethernet port configuration. You can configure traffic management, 
and binding entities (such as router interface) to port. However, in VLAN ports, you cannot configure 
physical properties, such as auto negotiation.   
 
Note 
VLAN tags have 0x8100 Ethertype. Other Ethertypes are not configurable or 
recognized.  
Factory Defaults 
By default, VLAN ports have the following configuration on creation. 
Parameter 
Description 
Default Value 
name 
Assign a port name  
no name 
VLAN #  
shutdown 
Administrative status 
shutdown 
5. Ports 
Configuring VLAN Port Parameters 
 To configure the VLAN port parameters: 
1. For Ethernet port VLAN: Navigate to configure port ethernet<port-name> vlan <vlan-id> to select 
the VLAN port to configure. VLAN ID can be 0-4094. 
For Virtual port VLAN:  
Navigate to configure port virtual <port-name> vlan <vlan-id>. VLAN ID can be 0-4094. 
2. Enter all necessary commands according to the tasks listed below.   
Task 
Command 
Comments 
Binding ACL to the port 
access-group <acl-name> in [{ipv4 | 
ipv6}] 
no access-group in {ipv4 | ipv6} 
Ethernet port VLAN only 
Clearing ACL statistics 
clear-access-list-statistics [in] 
[{ipv4|ipv6}] 
Ethernet port VLAN only  
Clearing statistics 
clear-statistics  
 
Setting maximum frame size  (in 
bytes) to transmit  
egress-mtu <68–12288> 
Frames above the 
specified size are 
fragmented or discarded. 
Mapping the traffic originated 
by a router interface to its 
egress port 
force-next-hop [next-hop <ip-
address>] 
no force-next-hop 
 
 
Configuring the VLAN port name 
name 
 
name – 0-64 character 
string  
Enter no name to revert 
the name to its default 
value (VLAN #). 
Bind PBR rule to the port 
policy-based-route priority <priority> 
match-acl <name> {next-hop <ip-
address> | interface <type, index>} 
no policy-based-route priority 
<priority> 
See Configuring PBR 
 
5. Ports 
Task 
Command 
Comments 
Binding PBR rule to this entity 
policy-based-route priority <priority> 
match-acl <name> {next-hop <ip-
address> } interface <type, index> 
no policy-based-route priority 
<priority> 
 
priority <number> - set 
PBR rule priority per 
interface; the lower is 
the number, the higher is 
the priority 
Possible values: 1 – 
4294967295 
match-acl <name> - 
attach ACL to PBR rule 
Possible values: 1–80 
characters string 
next-hop <ip-address> – 
Set next hop IP address 
to define the direction of 
PBR rule 
interface <type, index> –  
Set interface to define 
the direction of PBR rule. 
Possible values:  
• ethernet < port-
name> 
• ethernet < port-
name> vlan <vlan-
number> 
virtual <port-number> 
Displaying the summary of ACLs 
bound to the VLAN 
show access-list summary 
Displays ACL summary at 
the current level 
See Viewing VLAN Port 
Status below. 
Displaying the port statistics 
show statistics 
See Viewing VLAN Port 
Statistics 
Displaying the port status 
show status 
See Viewing VLAN Port 
Status 
5. Ports 
Task 
Command 
Comments 
Administratively disabling the 
port 
shutdown 
Entering no shutdown 
enables the port.  
Note: shutdown is 
possible only when the 
port is not bound to any 
entity (router interface, 
bridge port, and more).  
Configuration Errors 
The following table lists the messages generated by the device when a configuration error is detected. 
 
Message 
Cause 
Corrective Action 
Upper layer is bound to this 
VLAN port 
You tried performing shutdown while 
port was bound to an entity. 
Unbind port from all entities and then 
perform shutdown. 
Viewing VLAN Port Status 
The following port status can be displayed for a VLAN port.  
Name                  : My Port 
Administrative Status : Up  
Operational Status    : Up 
MAC Address           : 41-41-42-42-43-43 
 
Parameter 
Description 
Name 
Port name 
Administrative Status 
Possible values: Up, Down 
Operational Status 
Possible values: Up, Down 
MAC Address 
MAC address, formatted 00-00-00-00-00-00 
5. Ports 
 To display the ACL status for the VLAN: 
1. Navigate to configure port ethernet<port-name> vlan <vlan-id> and enter the show access-list 
summary command. 
The following status information is displayed:  
show access-list-summary 
 
ACL Name                        Type  Bound to                                Direction 
----------------------------------------------------------------------------- 
ip_port1_v4                     IPv4  Ethernet wan1 Vlan 100                     In 
ip_port1_v6                     IPv6  Ethernet wan1 Vlan 100                     In 
Viewing VLAN Port Statistics  
The following port statistics can be displayed for a VLAN port. The counters are described in the 
following table. 
config>port>eth(4)>vlan(200)# show statistics 
Running 
----------------------------------------------------------------------------- 
Counter                      Rx                      Tx                    
Total Frames                 3539                    10                    
Total Octets                 236594                  1060                         
Discard Frames               --                      99999    
 
Parameter 
Description 
Total Frames 
Total number of frames received/transmitted 
Total Octets 
Total number of bytes received/transmitted 
Discard Frames 
Total number of discarded Tx frames 
 To display the ACL statistics for the VLAN: 
1. Navigate to configure port ethernet<port-name> vlan <vlan-id> and enter show access-list 
statistics in [{ipv4 | ipv6}].  
The following statistical information is displayed:  
 
show access-list-statistics  
 
IPv4 access list:  Listv4                             (Inbound) 
 
Bound to:            Ethernet wan1 Vlan 100 

## 5.6 WiFi  *(p.260)*

5. Ports 
Matches counted for: 0 days 0 hours 5 minutes 43 seconds 
 
Sequence  Action  Protocol Source    Port Destination       Port ICMP Type Code DSCP  Log      Matches 
----------------------------------------------------------------------------- 
40        permit  tcp     10.10.10.100     20.20.20.100     1024                     enable (289317 matches) 
50        permit  tcp     10.10.10.100     20.20.20.100     600                      disable (288857 matches) 
60        deny    tcp     10.10.10.100     20.20.20.100     400                      disable (288216 matches) 
 
 
IPv6 access list:  Listv6                             (Inbound) 
 
Bound to:            Ethernet 1 Vlan 100 
Matches counted for: 0 days 0 hours 6 minutes 6 seconds 
 
Sequence Action Protocol Source     Port  Destination        Port    ICMP Type Code DSCP Log Matches 
----------------------------------------------------------------------------- 
40       permit  tcp  2005:db8:21:444::1  2006:db8:21:444::1 1024                  disable (307566 matches) 
50       permit  tcp  2005:db8:21:444::1  2006:db8:21:444::1 600          disable (307162 matches) 
60       deny    tcp  2005:db8:21:444::1  2006:db8:21:444::1 400          disable (306710 matches) 
 
 
5.6 WiFi  
ETX-1p can be equipped with a WiFi modem for wireless local area networking, in addition to its main 
modem. 
WiFi interface provides a single access point, within the frequency bands of 2.4 GHz and 5 GHz.  
Applicability and Scaling 
WiFi modem is installed on ETX-1p devices with WF ordering option. Devices with dual modems cannot 
hold a WiFi modem. 
ETX-1p supports up to two WiFi bands (2.5 Ghz and 5 Ghz) and up to six SSIDs. 
Standards Compliance 
Relevant sections of IEEE 802.11 
5. Ports 
Functional Description  
WiFi antennas are connected to the rear panel of ETX-1p being mounted to the connectors designated 
WIFI-MAIN and WIFI-AUX shown on the image below. 
  
For instructions on installing the WiFi antennas, refer to Mounting the unit.  
WiFi Band Level  
ETX-1p supports underlying dual-band WiFi interfaces : 
• 
UHF (2.4 GHz)   
• 
  
For each WiFi band, ETX-1p supports the following configurations: 
• 
Radio mode (802.11a/b/g/ng/na/ac or auto) 
• 
Operating channel for the WiFi interface 
Virtual AP Level  
ETX-1p operating with 2.4 GHz and 5 GHz bands supports one access point per WiFi band.  The bands 
cannot work simultaneously.  
5. Ports 
Once you configure the WiFi interface, you can bind a router interface to an access point (see 
Configuring Router Interfaces).  
For each access point, ETX-1p supports the following configurations:  
• 
Access point SSID 
• 
SSID broadcast (true | false) 
• 
Security type  
• 
Authentication password (stored as hash string) 
• 
Access point max associated clients 
• 
Access point partitioning 
• 
Access point MAC filtering policy 
ETX-1p supports configuration of MAC filtering table per access point. The table can contain up to 100 
MAC addresses. The policy of MAC filtering (allow/deny) is configured per access point. 
ETX-1p provides WiFi Protected Setup (WPS) functionality that can be applied to an access point.  
Wi-Fi Client  
One Wi-Fi client can be configured on a modem. To allow for devices with multiple modems the client 
has an index. However, the default index is 1, and if there is only one modem (as is currently with ETX-
1p, the user does not have to specify the index. The client is configured on the wifi-client level under 
configure>port and is disabled by default.  
An access point to which the device may connect is configured on the ssid level under 
configure>port>wifi-client. The SSID is a unique (including among WLAN access points) string of 1-32 
characters. No access point is configured by default. 
Connection Methods 
You can use the connection-method command in the configure>port>wifi-client level, to determine 
which SSID to attempt to connect to if the wifi client is enabled and the client is connected to no access 
point.  
The following connection methods are available: 
• 
Priority: The device will try the configured access points according to their priorities (highest to 
lowest), and if there are few with the same priority, they will be attempted in alphabetic order. 
5. Ports 
• 
Best: The device will try the configured access points starting with the one with the strongest 
signal. If there are few with the same strength, they will be attempted according to their 
priorities (highest to lowest), and if there are few with the same priority, they will be attempted 
in alphabetic order. 
• 
Last: The device tries the last access point it was connected to, if it is available. If not, or if it 
fails, it proceeds as in the priority method. 
Once a connection is made and as long as it is up, the device hangs on the access point and does not 
move to another access point, even if configuration (e.g., priorities, new network) or strength of the 
access points were changed.  
If the access point to which the device is connected is deleted or disabled, the device disconnects from it 
immediately, and tries to connect to another access point (if available). 
If all the configured SSID fail, the device keeps retrying the connection (according to the configuration 
order). 
Access Point Priority 
When the device chooses an access point to connect to, it follows the method configured by the wifi 
client connection-method command. The priority serves as a tiebreaker if the algorithm finds more than 
one access point (the SSID serves as a second tiebreaker in case of similar priorities). 
The priority can be 1-254, 100 being the default. Higher values represent higher priority. 
Security Methods 
The following security methods are used when connecting to the access point. 
• 
none (default), or wpa3-owe: If configured to none or wpa3-owe, anyone can connect, no 
authentication is needed. 
• 
wpa2-psk or wpa3-sae: the user must configure a password; otherwise authentication fails. 
• 
wpa2-dot1x is selected: the user must enable and configure 802.1X (supplicant); otherwise 
authentication fails (see Configuring 802.1X Access Control).  
Factory Defaults 
 By default, WLAN ports have the following configuration on creation. 
5. Ports 
Parameter 
Description 
Default Value 
radio-mode 
Wireless LAN interface operating 
radio mode 
802.11ng (for 2.4g) 
) 
channel 
Wireless LAN interface operating 
channel 
auto   
Access-point parameters 
 
 
shutdown 
Enable access point 
shutdown 
ssid 
 
no ssid 
broadcast-ssid 
Enable SSID broadcast 
broadcast-ssid 
security 
security method 
none 
password 
Authentication key (needed for the 
wpa2-psk and wpa3-sae security 
methods) 
no password 
max-clients 
Maximum clients allowed on 
access point 
22 
wlan-partition 
Enabling WLAN partitioning 
no wlan-partition 
wps 
Enabling WPS 
no wps 
mac-filter 
Add filtered MAC address 
The filter is empty 
mac-filter-enable 
Enabling MAC filter on access point 
no mac-filter-enable 
Wi-Fi client parameters 
 
 
connection-method 
Configuring the order in which to 
try to connect to the configured 
SSID 
last 
shutdown 
Disabling the wifi client 
shutdown 
ssid 
Configuring an SSID the client can 
connect to 
no ssid 
Commands under ssid  
 
 
password 
Configuring SSID authentication 
password (needed for the wpa2-
psk or wpa3-sae security methods) 
no password 
priority  
Determining priority (for 
connection order) 
100 
security  
Configuring security method 
none 
5. Ports 
Parameter 
Description 
Default Value 
shutdown 
Enabling/disabling SSID 
shutdown 
Configuring WLAN Port Parameters  
  To configure the WLAN port parameters with CLI: 
1. Navigate to configure port wlan <type> to select the operation band to configure. <type> possible 
values: 2.4g. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Configuring Access Point  
 
 
access-point <ap-number> 
ap-number – Access Point number 
Possible values:  
• 1   
 
Commands under access-point  
 
 
Enabling/disabling SSID broadcast 
[no] broadcast-ssid 
 
Entering 802.1X level 
dot1x 
See Configuring 802.1X Access Control 
Adding filtered MAC address 
[no] mac-filter [address 
<client-mac-address>] 
client-mac-address - EUI-48 MAC address 
Notes: 
• Command is accumulative. 
• Up to 100 Mac addresses are 
supported per access point. 
• The no mac-filter address [<client-
mac-address>] command deletes the 
specific entry. 
• The no mac-filter command clears 
the entire table. 
Enabling MAC filter on Access Point 
[no] mac-filter-enable [deny 
| allow] 
MAC addresses configured by the mac-
filter command are blacklisted or 
whitelisted, according to the policy 
defined by this command 
5. Ports 
Task 
Command 
Comments 
Configuring maximum clients 
allowed on Access Point 
max-clients <max-clients> 
max-clients – maximum clients allowed 
on Access Point 
Possible values: 1-22 
Configuring Virtual Access Point 
password 
password <pass-key > [hash] 
no password 
pass-key – preshared key used in the 
wpa2-psk and wpa3-sae security modes  
Possible values: string, up to 32 
characters 
Configuring Virtual Access Point 
security 
security {none | wpa2-psk | 
wpa2-dot1x } 
 
Displaying information on all the 
devices connected to the access 
point 
show connected-devices 
 
Enabling/disabling access point 
operation 
[no] shutdown 
An AP cannot be enabled if a country 
code is not configured. 
Configuring Access Point SSID 
ssid <ssid> 
SSID – Service Set Identifier; WiFi 
network name 
Possible values: 1-32 character string  
Configuring Access Point 
partitioning 
[no] wlan-partition 
 
Configuring WPS 
[no] wps 
WPS can only be enabled on one access 
point.  
Configuring WLAN interface 
operating channel 
 
channel {auto | channel-
number <channel-number>} 
 
channel – channel number 
Possible values:  
• 5 GHz: 32, 36, 40, 44, 48, 52, 56, 60, 
64, 68, 96, 100, 104, 108, 112, 116, 
120, 124, 128, 132, 136, 140, 144, 
149, 153, 157, 161, 165, 169, 173, 
177, auto 
• 2.4 GHz: 1-13, auto  
If either of the access point and client 
channels is not working, check the client 
channel as described in Viewing WiFi 
Client Status and reconfigure the AP 
channel to the same number (or modify 
the client channel via the external 
equipment).  
5. Ports 
Task 
Command 
Comments 
Configuring WLAN interface 
operating radio mode  
 
radio-mode < radio-mode> 
Possible values: 
802.11b 
802.11g  
802.111a  
802.11ng (default for 2.4g) 
802.11na 
Notes:  
• 802.11b, 802.11g and 802.11ng are 
only selectable on 2.4 GHz band  
• 802.11a, 802.11na and 802.11ac are 
only selectable on 5 GHz band  
•  
Configuring Wi-Fi Client Parameters  
  To configure the Wi-Fi client parameters with CLI: 
1. Navigate to configure port wifi-client [1] to select the Wi-Fi client to configure (currently only one 
Wi-Fi client is supported). Perform the required tasks according to the following table. 
            Task 
Command 
Comments 
Configuring the first SSID to 
connect to 
connection-method {last | 
best | priority} 
Default: last 
Entering 802.1X level 
dot1x 
See Configuring 802.1X Access Control 
Displaying the available networks 
show networks 
 
Displaying the client status 
show status 
 
Disabling the wifi client 
[no] shutdown 
Default: shutdown 
Entering the client SSID level  
ssid <name> 
no ssid <name> 
Possible values: string 1-32 characters 
Default: No SSID is configured 
Commands under ssid  
 
 
5. Ports 
            Task 
Command 
Comments 
Configuring SSID authentication 
password 
 
 
 
password <pass-key> [hash] 
no password 
 
 
 
pass-key – preshared key for PSK 
authentication 
Possible values: character string (1-32 
characters) 
Default: no password 
The password is used only when the 
security method is wpa2-psk or wpa3-
sae.  
Determining priority (connection 
order) 
priority <number>  
Possible Values: 1-254 
Default Value: 100 
Configuring security method 
security {none | wpa2-psk | 
wpa2-dot1x } 
Default: none 
 
Enabling/disabling SSID 
[no] shutdown 
By default, an access point client is 
disabled. 
 To configure and display the WiFi country code: 
1. Navigate to configure port #. 
2. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Configuring the WiFi 
country code 
wifi-country-code 
<country-name> 
no wifi-country-code 
Possible values: Country name  
Default: no wifi-country-code 
This command does not return to default using 
factory-default command.  
Display configured WiFi 
country code 
show wifi 
 
Examples 
echo "Wlan - Port Configuration" 
#   Wlan - Port Configuration 
    2.4g  
        radio-mode 802.11b 
        channel auto 
5. Ports 
        access-point 1 
            ssid "QA-PCPE-260-Pass" 
            broadcast-ssid 
            password "2419756A246CC8BB07943FA7C3A163EC" hash 
            security wpa2-psk 
             
            max-clients 8 
            no wlan-partition 
            no wps 
            no mac-filter-enable 
            shutdown 
        exit 
        access-point 2 
            ssid "QA-PCPE-260-No-Pass" 
            broadcast-ssid 
            no password 
            security none 
             
            max-clients 8 
            no wlan-partition 
            no wps 
            no mac-filter-enable 
            no shutdown 
        exit 
Configuration Errors 
The following table lists the messages generated by ETX-1p when a configuration error is detected. 
 
Message 
Cause 
Corrective Action 
Maximum number of active access 
points has been reached  
Only one access point can be 
enabled  
 
Maximum number of access points 
has been reached 
 
No more than ten access points 
(SSIDs) can be configured with the 
wifi client.  
 
WiFi country code is not configured 
One of the following: 
• An access point cannot be 
enabled if a country code is not 
configured.  
• Wifi client cannot be enabled if 
the country code is not 
configured. 
 
5. Ports 
Message 
Cause 
Corrective Action 
This SSID is in use by a WLAN 
access point 
You tried to configure a SSID that is 
the same as of existing access point 
 
This SSID is in use by another client 
SSID 
You tried to configure SSID that is 
the same as of existing client SSID 
 
Must have country code if access 
point or wifi client is enabled 
no wifi-country-code cannot be 
configured if access point or wifi 
client is enabled 
 
This SSID is in use by a WLAN 
access point 
You tried to configure SSID that is 
the same as of existing access 
point 
 
This SSID is in use by another client 
SSID 
You tried to configure SSID that is 
the same as of existing client SSID 
 
Viewing WiFi Client Status 
 To display the WiFi client status:  
• 
At the config>port>wifi-client (1)# prompt, enter show status. 
The following status information is displayed: 
 
Administrative state (Enabled/Disabled) 
 
Operational status (Connected/Connecting/No Enabled SSID/Failed) 
 
Number of seconds since last status change 
 
Router interface or bridge port the client is bound to 
 
IP address / prefix length 
 
Connected SSID 
 
Security method 
 
Signal strength 
 
Frequency : 2.4 GHz/5 GHz) 
 
Radio mode : 802.11b/802.11g/802.11ng/802.11a/802.11na/802.11ac 
 
Channel number 
 
Peer MAC address 
 
Line speed in Mbps 
 
5. Ports 
Client Status  
 
Admin State                : Enabled 
Oper Status                : Connected  
  Last Change (seconds ago): 500 
Bound To                   : router-interface 1/1 
IP Address                 : 192.168.1.100/24  
MAC Address                : 55-44-33-22-11-00 
 
 
Connected SSID             : my-ssid 
------------------------------------- 
Security                   : WPA2 PSK 
Signal Strength            : -50 dBm 
Frequency                  : 5 GHz 
Channel                    : 100  
MAC Address                : 00:11:22:33:44:55 
Line Speed (Mbps)          : 120 
Viewing WiFi Client Information 
 To display the WiFi client information:  
• 
At the config>port>wifi-client(1)# prompt, enter show networks. 
The following information is displayed: 
 
SSID the client is connected to 
 
Security method (WPA2 PSK, WPA2 802.1X) 
 
Signal strength in dBm 
 
Frequency for 2.4 GHz/5 GHz Peer MAC address 
Currently Connected To: ssid-1 
 
SSID   Security Strength Frequency MAC Address   
---------------------------------------------------- 
ssid-1 WPA2-PSK -50 dBm  5 GHz     00:11:22:33:44:55 
 
Viewing WiFi Country Code 
 To display the WiFi country code:  
• 
At the config>port# prompt, enter show wifi. 
5. Ports 
The following status information is displayed: 
configure>port# show wifi  
WiFi Country Code: CN, China 
Testing WiFi  
When the WiFi access point is configured, client cellular devices can discover the network name (ssid) in 
the list of available networks, if the name is allowed for advertising (broadcast ssid value is set to yes). 