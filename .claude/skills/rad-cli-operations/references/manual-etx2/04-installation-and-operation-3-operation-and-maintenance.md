# Installation and Operation – 3 Operation and Maintenance

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 183–228.*


## 3.1 Turning On the Unit  *(p.183)*


## 3.2 Indicators  *(p.183)*

3 Operation and Maintenance 
3.1 Turning On the Unit  
 To turn on ETX-2i: 
• 
Connect the power cord to the mains. 
The PWR indicator lights up and remains lit while ETX-2i receives power. 
ETX-2i requires no operator attention once installed, except for occasional monitoring of front panel 
indicators. Intervention is only required when ETX-2i must be configured to its operational 
requirements, or diagnostic tests are performed. 
 
Note 
Outdoor installations must use protected cables, which are resistant to UV, 
sunlight, and water. 
3.2 Indicators 
The unit’s LED indicators are located on the device’s front panel, back panel, and/or inside the chassis 
(for outdoor units), depending on the specific device and ordering option. These LEDs enable the user to 
quickly observe the state of the device. Each LED has a default “normal” functionality (see LED Behavior 
below). 
You can also configure the TST/ALM LED for LED signaling, instead of its normal function (see LED 
Signaling below). 
 
Note 
In case of slow fans or fan failure, the unit must be replaced as soon as 
possible. 
Once a replacement unit is available and configured, the estimated time to 
replace it by a qualified technician is about two minutes. 
ETX-2i Devices 
3. Operation and Maintenance 
LED Behavior 
The following tables summarize the normal functions of the ETX-2i LED indicators per device. 
Note 
In ETX-203AX/X/ODU, the LEDs described in the following table are inside the 
chassis. 
ETX-2i 
 
ETX-2i Front Panel 
ETX-2i Front Panel Controls and Indicators  
Name 
Color 
State 
LINK 
Ethernet port (MNG-ETH) 
Green  
ON – Ethernet interface is synchronized. 
ACT 
Ethernet port (MNG-ETH) 
Yellow  
ON – Data is being transmitted/received at the Ethernet link. 
LINK/ACT 
Ethernet ports 
(User/Network GbE/100Fx 1-8) 
Green 
ON – Ethernet interface is synchronized. 
Flashing – Sending/receiving data 
AIS 
T3 port(s) on modular uplink 
Yellow 
ON – AIS (Alarm Indication Signal) occurred.  
OFF – No AIS alarm 
FD 
 
Contains push button for setting unit to default configuration 
LINK 
Ethernet port 
(User/Network/MNG) 
Green  
ON – Ethernet interface is synchronized. 
LOC  
E1/T1 ports on modular uplink 
Red 
ON – Local synchronization loss (LOS, LOF, or AIS occurred)  
OFF – No local synchronization alarm 
LOS 
T3 port(s) on modular uplink 
Red 
ON – Local synchronization loss (LOS)  
OFF – No local synchronization alarm 
ETX-2i Devices 
3. Operation and Maintenance 
Name 
Color 
State 
POWER 
Green/
Red  
ON (green) – This power supply unit is connected to power and 
output voltage is okay. 
ON (red) – This power supply unit is not connected to power or 
output voltage failed (in case of dual power supply with 
redundancy mode).  
PWR 
Green  
ON – Power is ON. 
OFF – Power is OFF. 
EXT-CLK 
1PPS 
Green  
ON – Station clock port is synchronized. 
SHDSL SYNC  
SHDSL ports on modular uplink 
Green/
red 
ON (green) – SHDSL line is synchronized. 
ON (red) – SHDSL line is not synchronized. 
Blinking (red/green): SHDSL line is activating, after exchanging 
connection parameters (handshaking) with remote side. 
TST/ALM  
Red  
ON – There is at least one active alarm. 
Blinking – Diagnostic loopback is active. 
 
ETX-2i-64E1 
 
ETX-2i-64E1 Front Panel 
ETX-2i-64E1 Front Panel Controls and Indicators 
Name 
Color 
State 
LINK 
Ethernet port 
(MNG-ETH) 
Green  
ON – Corresponding Ethernet link is synchronized. 
OFF – Corresponding Ethernet link is not synchronized. 
ETX-2i Devices 
3. Operation and Maintenance 
Name 
Color 
State 
ACT  
Ethernet port 
(MNG-ETH) 
Yellow  
ON – Data is being transmitted or received at the Ethernet link. 
OFF – Data is not being transmitted or received at the Ethernet link. 
LINK/ACT 
Ethernet ports 
(1-6) 
Green 
ON – Ethernet interface is synchronized. 
Flashing – Sending/receiving data. 
LOC (E1 ports) 
1–64   
Red 
ON – Local synchronization loss (LOS, LOF, or AIS occurred)  
OFF – No local synchronization alarm 
PWR 
Green/Red  
ON (green) – This power supply unit is connected to power and output voltage 
is as expected. 
ON (red) – This power supply unit is not connected to power or output voltage 
failed (in case of dual power supply with redundancy mode).  
PWR 
Green 
ON – Power is ON. 
OFF – Power is OFF. 
REM (E1 ports) 
1–64 
Red 
ON – Remote synchronization loss (RDI)  
OFF – No remote synchronization alarm 
TST/ALM  
Red  
ON – There is at least one active alarm. 
Blinking – Diagnostic loopback is active. 
ETX-2i-B 
 
ETX-2i-B Metal 2+4 Front Panel  
 
ETX-2i-B Metal 2+2 Combo Front Panel 
ETX-2i Devices 
3. Operation and Maintenance 
 
ETX-2i-B-DNFV Front Panel 
 
ETX-2i-B-DNFV Back Panel 
 
ETX-2i-B 2U Front Panel 
 
ETX-2i-B (6 SFP + 4 UTP) 
 
ETX-2i Devices 
3. Operation and Maintenance 
ETX-2i-B Front and Back Panel Controls and Indicators  
Name 
Color 
State 
LINK 
Ethernet port (MNG-
ETH) 
Green  
ON – Corresponding Ethernet link is synchronized. 
OFF – Corresponding Ethernet link is not synchronized. 
ACT  
Ethernet port (MNG-
ETH) 
Yellow  
ON – Data is being transmitted or received at the Ethernet link. 
OFF – Data is not being transmitted or received at the Ethernet link. 
LINK/ACT 
Ethernet ports (1-6) 
Green 
ON – Ethernet interface is synchronized. 
Flashing – Sending/receiving data. 
Active 
Green  
ON – LINUX is up and running. 
Relevant for ETX-2i-B-DNFV (back panel) 
FD 
 
Contains push button for setting unit to default configuration 
LINK 
Ethernet port 
(User/Network/MNG) 
Green  
ON – Ethernet link is synchronized. 
PWR 
Green  
ON – Power is ON. 
TST/ALM  
Red  
ON – There is at least one active alarm. 
Blinking – Diagnostic loopback is active. 
 
ETX-2i-10G and ETX-2i-10G-B 
 
ETX-2i-10G Half 19-inch Front Panel (4 SFP+, 4 SFP 4 UTP Combo)   
ETX-2i Devices 
3. Operation and Maintenance 
 
ETX-2i-10G Half 19-inch Front Panel (4 SFP+ and 8 SFP)   
 
ETX-2i-10G Full 19-inch Front Panel (4 SFP+, 12 SFP, and 12 UTP) 
 
ETX-2i-10G Full 19-inch Front Panel (4 SFP+ and 24 SFP) 
 
ETX-2i-10G Full 19-inch Front Panel (4 SFP+, 12 SFP 12 UTP Combo)   
 
ETX-2i-10G-B Half 19-inch (4 SFP+, 4 SFP, and 4 UTP) 
  
ETX-2i-10G-B Full 19-inch (4 SFP+, 4 SFP, and 4 UTP) 
ETX-2i Devices 
3. Operation and Maintenance 
 
ETX-2i-10G-B/8SFPP Half 19-inch (8 SFP+) 
 
ETX-2i-10G-B/8SFPP Full19-inch (8 SFP+) 
 
ETX-2i-10G-B/8SFPP/PTP Full19-inch (8 SFP+) 
 
ETX-2i-10G-B/8SFPP/ODU Full19-inch (8 SFP+) 
Note 
In ETX-2i-10G-B/8SFPP/ODU, only the Power LED is on the chassis front panel. 
All other LEDs and the “set to default” push button described in the following 
table are inside the chassis. 
 
ETX-2i Devices 
3. Operation and Maintenance 
ETX-2i-10G Front and Back Panel Controls and Indicators 
Name 
Color 
State 
ACT 
Ethernet port (User/Network/MNG) 
Yellow  
ON – Data is being transmitted/received at the 
Ethernet link. 
LINK 
Ethernet port (10G User/Network/MNG) 
Green  
ON – Ethernet interface is synchronized. 
LINK/ACT 
Ethernet ports (1G User) 
Green 
ON – Ethernet interface is synchronized. 
Flashing – Sending/receiving data. 
 
FD 
 
Contains push button for setting unit to 
default configuration 
Power (back panel for  
ETX-2i-10G-B/8SFPP half 19-inch model) 
Green/Red 
ON (green) – This power supply unit is 
connected to power and output voltage is 
okay. 
ON (red) – This power supply unit is not 
connected to power or output voltage failed 
(in case of dual power supply with redundancy 
mode).  
PWR 
POWER (On ETX-2i-10G-B/8SFPP/ODU) 
Green  
ON – Power is ON. 
OFF – Power is OFF 
TST/ALM  
Red  
ON – There is at least one active alarm. 
Blinking – Diagnostic loopback is active. 
EXT CLK 
1PPS 
Green  
ON – Station clock port is synchronized. 
ETX-2i-100G 
 
ETX-2i-100G/4Q Full 19-inch Front Panel 
ETX-2i Devices 
3. Operation and Maintenance 
ETX-2i-100G Front Panel Controls and Indicators  
Name 
Color 
State 
ACT 
Ethernet port (MNG-ETH) 
Yellow  
ON – Data is being transmitted/received at the Ethernet link. 
LINK 
Ethernet port (MNG-ETH) 
Green  
ON – Ethernet interface is synchronized. 
LINK/ACT 
Ethernet ports  
(1/1 -1/8, 2/2-2/8, 3/1-3/4) 
Green 
ON – Ethernet interface is synchronized. 
Flashing – Sending/receiving data. 
FD 
 
Contains push button for setting unit to default configuration 
LINK 
Ethernet port 
(User/Network/MNG) 
Green  
ON – Ethernet interface is synchronized. 
PS1, PS2  
Green/ 
Amber 
LEDs for monitoring Power Supply 1 and Power Supply 2 state 
Green – Output is ON and OK. 
OFF – No AC power to all power supplies OR power supply unit 
not inserted 
1Hz blinking green – AC present; only standby voltage to CPU is 
active (PS off) or PS in Cold redundant state 
Amber – Unplugged AC cord or lost AC power; with a second 
power supply in parallel, still with AC input power 
OR 
Power supply critical event causing a shutdown: failure, OCP, 
OVP, or Fan Fail 
1Hz blinking amber – power supply warning events where the 
power supply continues to operate; high temperature, high 
power, high current, slow fan 
2Hz blinking green – power supply firmware updating 
PWR 
Green  
ON – Power is ON. 
OFF – Power is OFF. 
TST/ALM  
Red  
ON – There is at least one active alarm. 
Blinking – Diagnostic loopback is active. 
ETX-2i Devices 
3. Operation and Maintenance 
LED Signaling 
ETX-2i supports LED signaling (blinking) using the TST/ALM LED. LED signaling is typically activated from 
the NOC to pass information to a technician on the field, by blinking the device LED in agreed patterns. 
For example, if the technician is not sure which device to reset in a rack, someone at the NOC can point 
to it by blinking its LED. 
You can use the led-blink command to set the color, pattern, and duration of a LED signal that is 
activated (see configuration details in the table below).  
While LED signaling is active, it overrides normal LED behavior. Once you cancel an active command (by 
entering the no led-blink command or rebooting the device), the LED behavior returns to normal. 
Configuring LED Signaling 
 To configure LED signaling: 
1. Navigate to configure reporting. 
2. At the prompt, enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Configuring LED blinking 
pattern 
led-blink <color> on 
<on-milliseconds> off 
<off-milliseconds> 
[forever | duration 
<seconds>] 
no led-blink 
<color> – LED color 
Possible values: red, green, yellow (provided the device 
has these colors) 
on-milliseconds – time the LED is on 
Possible values: 100-10000 
off-milliseconds – time the LED is off 
Possible values: 100-10000 
seconds – total time of LED blinking 
Possible values: 1-3600 
Notes:  
• The number of milliseconds (off or on) must be a 
multiple of 100ms. If you configure a different 
number, the device rounds it up to the nearest valid 
value and prints:  
Note: On-time/Off-time was rounded up to the 
nearest multiple of 100 not above 10000. 
• This command is not saved in the configuration and 
cannot be executed from a configuration file. 
• If this command is repeated while a previous one is 
active, it replaces the previous one. 
ETX-2i Devices 
3. Operation and Maintenance 
Task 
Command 
Comments 
• Entering no led-blink cancels an active command (if 
one exists), stops the blinking, and returns the LED 
behavior to normal. 
• When the blinking is finished, the device disables 
LED signaling. 
Displaying the LED blinking 
status 
show led-blink-status 
For detailed information on the LED blinking status 
report parameters, see Viewing LED Blinking Status.     
Viewing LED Blinking Status 
 To display LED blinking status: 
• 
Navigate to configure reporting show led-blink-status. 
A status report is displayed. 
LED Blinking Status        : On 
Remaining Time (Seconds)   : 147 
 
LED Color                  : Green 
On Time (Milliseconds)     : 100 
Off Time (Milliseconds)    : 100 
Blinking Duration (Seconds): 200 
 
Note 
If LED Blinking Status is Off, only the first row of the report is displayed.  
 
Parameter 
Description 
LED Blinking Status 
LED blink status 
Possible values: On, Off 
Remaining Time (Seconds) 
LED blinking remaining time 
Possible values: Forever, number  
Note: Only displayed if Blinking Duration has been configured. 
LED Color 
Possible values: Green, Red, Yellow 
On Time (Milliseconds) 
LED blink on time (in milliseconds) 
Off Time (Milliseconds) 
LED blink off time (in milliseconds) 
Blinking Duration (Seconds) 
LED blinking remaining time 
Possible values: Forever, number 

## 3.3 Startup  *(p.195)*

ETX-2i Devices 
3. Operation and Maintenance 
3.3 Startup 
Applicability and Scaling 
All configuration and software files, as well as the loading sequence, are applicable to all ETX-2i products 
and to PMC in ETX-2i. 
ZTP is relevant for all ETX-2i products, except for PMC in ETX-2i. 
Configuration and Software Files 
ETX-2i software files are named sw-pack-1 through sw-pack-4. One of the software packs is designated 
as active. 
Note 
Although the CLI allows sw-pack-1 through sw-pack-4, you can define only 
two SW packs simultaneously.  
The integrated x86 module in ETX­2i and ETX­2i-B with DNFV can store up to two software files of its 
own, named im-sw-pack-1 and im-sw-pack-2. One of these integrated module software packs is 
designated as active. It can also store two software update files, named im-sw-update-1 and im-sw-
update-2. 
The following files contain configuration settings: 
• 
factory-default-config – contains the manufacturer default settings. At startup, 
factory-default-config is loaded if startup-config, rollback-config, and user-default-config are 
missing or invalid. 
• 
rollback-config – serves as a backup for startup-config. At startup, rollback-config is loaded if it 
exists and is valid, and if startup-config is missing or invalid. 
• 
restore-point-config – created by ETX-2i when software is installed with restore point option. 
Refer to the Software Upgrade chapter for more details. 
• 
running-config – contains the current configuration that the device is running. This file is deleted 
and rebuilt at device reboot. 
• 
startup-config – contains saved non-default user configuration. This file is not automatically 
created. You can use the save or copy command to create it. At startup, startup-config is loaded 
if it exists and is valid. 
ETX-2i Devices 
3. Operation and Maintenance 
• 
user-default-config – contains default user configuration. This file is not automatically created. 
You can use the copy command to create it. At startup, user-default-config is loaded if 
startup-config and rollback-config, are missing or invalid.  
Note 
Configuration files should contain only printable ASCII characters (0x20–0x7E), 
<Enter> (0x0D), <Line Feed> (0x0A), and <Tab> (0x09).  
Refer to File Operations in the Administration chapter for details on file operations. 
Loading Sequence 
At startup, the device attempts to load configuration files in the following sequence until a valid one is 
found: 
• 
startup-config 
• 
rollback-config 
• 
user-default-config 
• 
factory-default-config 
If an error is encountered while loading a file, the default is to ignore the error and continue loading. 
You can use the on-configuration-error command to change this behavior, to either stop loading the file 
when the first error is encountered or reject the file and reboot. After rebooting, the next file in the 
loading sequence is loaded). 
To display the parameter values after startup, use the info [detail] command. 
Working with Custom Configuration Files 
In large deployments, often a central network administrator sends configuration files to remote 
locations and all that remains for the local technician to do is replace the IP address in the file or other 
similar minor changes and then download the file to the device. Alternatively, the technician can 
download the file as is to the device, log in to the device and make the required changes, and then save 
the configuration. 
You can download the configuration file using the copy command (refer to the Administration chapter) 
and then reset the unit to execute the file. After the unit completes its startup, the custom configuration 
is complete. 
 
 
ETX-2i Devices 
3. Operation and Maintenance 
You can ease the deployment of large numbers of devices by automatically distributing to the devices an 
IP address, and software and configuration files, using the following methods: 
• 
On-net Zero Touch provisioning (ZTP)  
• 
PPPoE (Point-to-Point Protocol over Ethernet). 
Staging for Mass Deployment by ZTP 
Zero Touch (ZT) is a technology for automatic mass-provisioning of network devices. Upon first boot, 
ETX-2i connects to the service provider’s NOC (Network Operations Center) over private or public 
networks, based on preparation steps performed at various locations. It requires the RADview NMS 
(Network Management System). 
For a description of all aspects of ZT provisioning, including security considerations, read RAD’s Zero 
Touch Provisioning document. 
Staging for Mass Deployment by PPPoE  
You can use Point-to-Point Protocol over Ethernet (PPPoE) to establish a management channel through 
which an IP address can be acquired (refer to Point-to-Point Protocol over Ethernet (PPPoE) in the 
Management and Security chapter, for details). For instance, the IP address can be acquired from a 
broadband remote access server (BRAS). The BRAS then notifies a Radius server, which in turn reports to 
a management system, such as RADview, that a new device is up. The management system then sends 
software and configuration files to the device. 
Saving Configuration Changes 
Changes to configuration files are not saved automatically unless you enable auto-save.  
Once enabled, the configuration is automatically saved each time when logging out. This means after 
logging out manually and when the user is logged out automatically, for example when the session times 
out. If a user runs multiple sessions, the configuration is saved upon logging out of each session.  
An event/trap is sent each time when the configuration is saved automatically. 
You can manually save the configuration file using the following commands: 
• 
save command to save running-config as startup-config. 
• 
copy command to copy running-config to startup-config or user-default-config. 
ETX-2i Devices 
3. Operation and Maintenance 
Note 
If you perform admin reboot, admin factory-default, or admin factory-
default-all while the save command is being processed, these operations are 
blocked until save completes. 
If the saving process takes too long or encounters complications, you can 
perform force-reboot from the admin prompt. 
Additionally, some commands erase the configuration saved in startup-config by copying another file to 
it and then resetting the device. The following figure indicates the commands that copy to 
startup-config, and whether the device resets after copying. 
 
 To save the user configuration in startup-config, do either of the following: 
• 
On any level, enter: save. 
• 
On any level, enter: copy running-config startup-config. 
 To save the user default configuration in user-default-config:  
• 
On any level, enter: copy running-config user-default-config. 
 To save device configuration changes automatically: 
• 
On the admin level, enter admin# auto-save: 
 To return to manually saving the device configuration after changes: 
• 
On the admin level, enter admin# no auto-save: 
Auto-save command default minimum level is ‘tech’ (same as the ‘save’ command). When autosave is 
performed, an event/trap is sent with the reason for the save. 

## 3.4 Replacing Power Supply Units  *(p.199)*

ETX-2i Devices 
3. Operation and Maintenance 
Confirming Startup Configuration 
You can request that startup-config be confirmed after the next reboot. When you execute the request, 
the next time the device reboots, if startup-config is loaded successfully, you must confirm 
startup-config within the configured timeout period.  
If the confirmation is not received before timeout, the device rejects startup-config, reboots, and 
attempts to load the next available configuration file (rollback-config, user-default-config, 
factory-default-config). After rebooting, startup-config goes into Confirm not Received state (displayed 
in the output of the dir command). As long as startup-config is in this state, it is not possible to perform 
any configuration changes or install a new sw-pack. In order to release startup-config from this state, 
save must be performed. 
 To request confirmation of startup-config after next reboot: 
• 
At the admin# prompt enter: 
startup-confirm-required [time-to-confirm <minutes>] [rollback {startup-config | 
user-default-config | factory-default-config | running-config}] 
The <minutes> parameter defines the confirmation timeout, range 1–65535 (default 5). If 
rollback <config-file> is specified, the specified configuration file is copied to rollback-config. 
 To confirm startup-config after reboot: 
• 
In any level, enter:  
startup-config-confirm 
3.4 Replacing Power Supply Units 
Note 
• 
This section is relevant for devices with modular power supply units (PSUs) 
only. 
• 
If you are extracting a PSU and not replacing it, place a blank panel over 
the empty slot and secure the screws into place. 
• 
If the empty power supply slot is covered, before installing the PSU, loosen 
and remove the screws from the blank panel, and remove it.  
ETX-2i devices with modular power supplies support hot swapping of the PSUs, meaning that you can 
insert and extract a PSU into/from the device without interrupting the device’s operation (i.e., powering 
it down). During hot swapping, the output voltages remain within the limits, with the capacitive load 
specified. 
ETX-2i Devices 
3. Operation and Maintenance 
In the DCR or ACR options, when both PSUs are present and functional, an ETX-2i device operates in load 
balancing/sharing mode via a load-share bus signal that connects between the PSUs. Failure of one PSU 
does not affect the output voltage of the other operating PSU. 
The following devices support a dual hot swappable power supply (AC or DC):  
• 
ETX-2i full 19-inch 
• 
ETX-2i/64E1 
• 
ETX-2i-10G full 19-inch 
• 
ETX-2i-10G-B/4SFPP full 19-inch 
• 
ETX-2i-10G-B/8SFPP full 19-inch (also ACDC) 
• 
ETX-2i-100G/4Q (PSUs of specific vendors, as described in detail below) 
• 
ETX-2i-100G/40G 
 
Caution 
• 
Only skilled personnel are permitted to hot swap the PSUs. 
• 
Do not leave an empty power supply slot. Either insert a new PSU or 
close it with a blank panel. 
• 
Check that the approved PSU models appear on the power supply unit 
labels before inserting them into the device. 
• 
Inserting an incorrect or uncertified power supply unit can cause system 
shutdown or damage to the system.   
• 
Remove/insert the PSU from/into the slot gently. Otherwise, you may 
damage the internal system back-plane connectors. 
• 
Firmly secure the installed PSU to avoid undefined false identification. 
 
 
Warning  
• 
To reduce the risk of personal injury from hot surfaces, following 
extraction, allow the power supply unit to cool before touching it. 
• 
To reduce the risk of electric shock, do not disassemble the power supply 
unit or attempt to repair it.   
 
 
To reduce the risk of electric shock or damage to the equipment, connect the 
power cord to the power connector only after the power supply unit is 
installed. 
For instructions on how to connect the power supply to AC/DC power, refer to Connecting to Power in 
the Installation and Setup chapter. 
ETX-2i Devices 
3. Operation and Maintenance 
ETX-2i full 19-inch 
Extracting a PSU 
 To extract a PSU: 
1. Remove the power cord from the mains outlet. 
2. For AC PSU: Detach the power cord retainer from the AC power cord of the PSU that you are 
removing. 
3. Disconnect the AC/DC power cord from the power supply unit connector. Verify that the 
corresponding PSU PWR LED turns red. 
4. Release the locking screw. 
5. Lift the latch, while gently pulling the extraction handle upward and removing the power supply 
unit out of the slot.  
  
6. If you are not replacing the power supply, place a blank panel over the empty slot and secure 
the two flathead screws into place. Otherwise, insert a new AC/DC PSU (see the following 
instructions from step 2). 
Installing a PSU 
 To install a PSU: 
1. If you are installing the power supply into an empty slot, remove the blank panel from the 
empty power supply slot by loosening and removing the two flathead screws. Otherwise, if you 
are replacing the power supply, remove the PSU currently in the slot (see above procedure). 
ETX-2i Devices 
3. Operation and Maintenance 
2. Make sure no power cord is plugged into the PSU, and then gently slide it into the power supply 
slot, until it is fully inserted and clicks into place.  
3. Lower the latch and fold the handle. 
4. Tighten the locking screw to lock the PSU into place. 
 
PSU Locked into Chassis 
5. Connect the AC/DC power cord to the power connector. Verify that the corresponding PSU PWR 
LED is green. 
6. For AC PSU: Snap the power cord retainer into place to secure the AC power cord. This prevents 
the power cord from being pulled out accidentally. 
Hot Swapping a PSU 
 To hot swap a PSU: 
1. Extract the PSU from the slot (see Installing a PSU from step 2). 
2. Install the new PSU into the now empty slot (see Installing a PSU). 
ETX-2i Devices 
3. Operation and Maintenance 
ETX-2i/64E1, ETX-2i-10G full 19-inch, ETX-2i-10G-B/4SFPP, ETX-2i-10G-
B/8SFPP  
Extracting a PSU  
 To extract a PSU: 
1. Remove the power cord from the mains outlet. 
2. For AC PSU: Detach the power cord retainer from the AC power cord of the PSU that you are 
removing. 
3. Disconnect the power cord from the PSU connector. Verify that the Power LED on the 
corresponding PSU turns red. 
 
4. Release the two front captive screws of the PSU, and while grasping the screws, gently remove 
the PSU from the slot. 
Installing a PSU  
 To install a PSU:  
1. Make sure no power cord is plugged into the PSU, and then gently slide the PSU into the power 
supply slot, until it is fully inserted and clicks into place.  
2. Connect the power cord to the power connector. Verify that the corresponding PSU Power LED 
is green. 
3. For AC PSU: Snap the power cord retainer into place to secure the AC power cord. This prevents 
the power cord from being pulled out accidentally. 
ETX-2i Devices 
3. Operation and Maintenance 
Hot Swapping a PSU 
ETX-2i-10G-B/8SFPP full 19-inch supports one or two AC PSUs, one or two DC PSUs, or one AC and one 
DC PSU.  
 To hot swap a PSU: 
1. Extract the PSU from the slot (see Extracting a PSU  from step 2). 
2. Install the new PSU into the now empty slot (see Installing a PSU . 
ETX-2i-100G/4Q 
The following table shows photos, model numbers, and RAD ordering numbers of the AC and DC PSUs 
from vendors (AcBel, Delta, and Gospower) approved for use in ETX-2i-100G/4Q. 
You can identify the PSU models installed in the unit according to the appearance of their front panels 
and their labels after removal. 
PSU 
AcBel 
Delta 
Gospower 
AC 
FSF008-GS0G 
ETX-2i-100G-PS/ACF 
DPS-550AB-53 A 
ETX-2i-100G-PS/ACF2 
G1342-0550WRB 
ETX-2i-100G-PS/ACF3 
ETX-2i Devices 
3. Operation and Maintenance 
PSU 
AcBel 
Delta 
Gospower 
DC 
FSG006-GS0G 
ETX-2i-100G-PS/DCF 
 
DPS-650AB-43 A 
ETX-2i-100G-PS/DCF2 
 
G1232-0550WRB  
ETX-2i-100G-PS/DCF3 
The Delta and Gospower AC PSUs are supplied with an installed power cord retainer to prevent the 
power cord from being pulled out unintentionally. 
 
Note 
• 
Both PSUs installed in ETX-2i-100G/4Q must be from the same vendor. 
• 
When using Gospower or Delta PSUs, an AC and DC PS mix (from same 
vendor) is allowed on a single unit. AcBel does not support an AC/DC PS 
mix. 
 
 
ETX-2i Devices 
3. Operation and Maintenance 
Extracting an AcBel AC PSU 
 To extract an AcBel AC PSU: 
1. Remove the AC power cord from the connector of the AcBel AC PSU that you are removing. 
Verify that the PS LED on the PSU front panel is amber (other PSU is working) or off (no PSU is 
working). 
2. Unfold the extraction handle on the PSU. 
3. Grasp the release latch to the right of the power supply slot and press it inward (in the direction 
of the PSU), while gently pulling the extraction handle to remove the AcBel AC PSU out of the 
slot.  
Installing an AcBel AC PSU 
 To install an AcBel AC PSU: 
1. Make sure no power cord is plugged into the AcBel AC PSU, and then gently slide it into the 
power supply slot until it is fully inserted and clicks into place. Do not force it in. If it does not 
slide in easily, make sure that it is properly oriented, and reinsert. 
2. Insert the AC power cord into the connector of the AcBel AC PSU. Verify that the PS LED on the 
PSU panel turns green. 
Extracting an AcBel DC PSU 
 To extract an AcBel DC PSU: 
1. Remove the TB plug from the VDC-IN connector of the AcBel DC PSU that you are removing (see 
diagram below). Verify that the PS LED on the PSU front panel is amber (other PSU is working) or 
off (no PSU is working). 
2. Unfold the extraction handle on the PSU. 
3. Grasp the release latch to the right of the power supply slot and press it inward (in the direction 
of the PSU), while gently pulling the extraction handle to remove the AcBel DC PSU out of the 
slot. 
ETX-2i Devices 
3. Operation and Maintenance 
Installing an AcBel DC PSU 
 To install an AcBel DC PSU: 
1. Make sure no TB plug is plugged into the AcBel DC PSU, and then gently slide it into the power 
supply slot until it is fully inserted and clicks into place. Do not force it in. If it does not slide in 
easily, make sure that it is properly oriented, and reinsert.  
2. Insert the TB plug into the VDC-IN connector of the AcBel DC PSU until it snaps into place. Verify 
that the PS LED on the PSU panel turns green. 
 
Extracting a Delta/Gospower AC PSU 
 To extract a Delta/Gospower AC PSU: 
1. Open the retainer clamp by pressing downward the lower tab on the retainer clamp and slide 
the AC power cord out of the retainer clamp. 
2. Press the tab under the retainer clamp inward while sliding the retainer clamp along the strip 
away from the PSU. This makes it possible to access the power connector on the PSU. 
3. Remove the AC power cord from the PSU connector. Verify that the PS LED on the PSU front 
panel is amber (other PSU is working) or off (no PSU is working). 
4. Unfold the extraction handle on the PSU. 
5. Grasp the release latch to the right of the power supply slot and press it inward (in the direction 
of the PSU), while gently pulling the extraction handle to remove the PSU out of the slot.  
ETX-2i Devices 
3. Operation and Maintenance 
Installing a Delta/Gospower AC PSU 
 To install a Delta/Gospower AC PSU: 
1. Make sure that no power cord is plugged into the new Delta/Gospower AC PSU, and then gently 
slide it into the power supply slot, until it is fully inserted and clicks into place. Do not force it in. 
If it does not slide in easily, make sure that it is properly oriented, and reinsert. 
2. Press the tab under the retainer clamp upward while sliding the retainer clamp along the strip 
away from the PSU. This makes it possible to access the power connector on the PSU. 
 
3. Insert the AC power cord into the power connector on the new AC PSU. Verify that the PS LED 
on the PSU panel turns green. 
4. Press downward the lower tab on the retainer clamp to open the retainer clamp and slide the 
retainer clamp around the AC power cord. 
5. Press the tab under the retainer clamp upward while sliding the retainer clamp along the strip 
until it is as close as possible to the PSU.  
 
 
ETX-2i Devices 
3. Operation and Maintenance 
1. Press the upper and lower tabs of the retainer clamp toward each other to close the clamp and 
secure the AC power cord.  
 
 
Extracting a Delta/Gospower DC PSU 
 To extract a Delta/Gospower DC PSU: 
1. On the Delta/Gospower DC PSU that you are removing, release the black screws above and 
below the terminal block and then remove the DC adapter from the PSU’s D-Sub connector. 
Verify that the PS LED on the PSU front panel is amber (other PSU is working) or off (no PSU is 
working). 
2. Unfold the extraction handle on the PSU. 
3. Grasp the release latch to the right of the power supply slot and press it inward (in the direction 
of the PSU), while gently pulling the extraction handle to remove the PSU out of the slot. 
 
 
ETX-2i Devices 
3. Operation and Maintenance 
Installing a Delta/Gospower DC PSU 
 To install a Delta/Gospower DC PSU: 
1. Make sure no power cord is plugged into the Delta/Gospower DC PSU, and then gently slide it 
into the power supply slot, until it is fully inserted and clicks into place.  
2. Using a crimping tool, connect DC wires into the three terminals supplied with the adapter: one 
wire per terminal. 
3. On the adapter, remove the cover from the terminal blocks. 
4. Release the three silver terminal screws on the terminal blocks. 
5. Insert each terminal into the appropriate terminal block, as follows: 
 
– black wire 
 
+ red wire 
 
Ground yellow/green wire  
 
6. Close the three silver terminal screws on the terminal blocks securely. 
7. Cover the DC adapter terminal blocks.  
ETX-2i Devices 
3. Operation and Maintenance 
 
8. Insert the DC adapter into the PSU’s D-Sub connector until it clicks into place and then close the 
black screws above and below the terminal block to secure it into place. Verify that the PS LED 
on the PSU panel is green. 
 
Note 
The D-Sub adaptor on a Delta PSU is identical to that on a Gospower PSU; 
they are installed in opposite directions (rotated 180 degrees), and therefore 
the adaptor is inserted into the Delta with its terminals on the right, and into 
the Gospower, with its terminals on the left.  
      
 
Left: Inserting DC Adapter into Delta PSU; Right: Inserting DC Adapter into Gospower PSU 
 
 
ETX-2i Devices 
3. Operation and Maintenance 
Hot Swapping an ETX-2i-10G-B/8SFPP Outdoor Unit Power Supply Unit 
ETX-2i-10G-B/8SFPP outdoor unit supports one or two AC PSUs, one or two DC PSUs, or one AC and one 
DC PSU.  
               
 
AC PSU                                                                            DC PSU 
 
Caution 
• 
Perform the PSU replacement exactly according to and in the order of 
the following instructions. Failure to do so may harm the product. 
• 
Do not open the unit in rainy, humid, or dusty conditions. 
 To hot swap a PSU of the ETX-2i-10G-B/8SFPP Outdoor Unit:  
1. Turn OFF the mains from the power supply to be replaced by opening the circuit breaker of that 
PS. 
Note 
It is recommended to label the circuit breakers as PS1 and PS2 so that it is 
clear which power supply needs to be closed. 
2. Release the ten captive screws (marked in the figure below) from the sides of the chassis.  
 
ETX-2i Devices 
3. Operation and Maintenance 
3. Grasp the left side of the chassis cover and raise it (from left to right) until the hold-open 
mechanism on the support bar is engaged. This prevents the cover from slamming shut in windy 
conditions.  
 
4. Release the two captive screws from the top of each PSU to be removed. In the above figure, 
the screws on each PSU are encircled.  
5. Lift from the chassis the PSU to be replaced. 
 
ETX-2i Devices 
3. Operation and Maintenance 
6. Remove the GND cable from the removed PSU. 
7. Connect the GND cable from the unit to the new PSU. Attachment of the GND cable to the PSU 
makes the PSU hot swappable. 
 
8. Only then install the new PSU into the unit and secure the captive screws on the PSU. 
9. Turn ON the mains to connect power to the newly installed power supply unit by closing the 
circuit breaker. 
10. Slightly lift the support bar to release the hold-open mechanism and then close the chassis 
cover. 
Replacing an ETX-2i-100G Unit Power Supply Unit 
ETX-2i-100G/4Q supports front access dual hot swapping (replacement while computer is running) 
between the following power supply units: 
• 
AcBel and AcBel (AC to AC or DC to DC) 
• 
Delta and Delta 
• 
Gospower and Gospower 
• 
Delta and Gospower 
Hot swapping means that you can insert and extract a PSU into/from the device without powering down 
the device and without interrupting the device operation. During hot swapping, the output voltages 
remain within the limits, with the capacitive load specified. 
During hot swapping, Delta and Gospower PSUs can coexist in the device for up to five minutes. At the 
end of any PSU replacement, both PSUs are required to be of the same vendor (no long-term 
coexistence of PSU from different vendors). 
ETX-2i Devices 
3. Operation and Maintenance 
ETX-2i-100G/4Q does not support hot swapping between AcBel AC and DC PSUs, and between AcBel 
PSUs and Delta/Gospower PSUs, meaning that prior to these replacements, you are required to power 
down the computer. 
The following table shows the possible PSU replacement possibilities, with limitations of each 
combination and a link to the replacement procedure. 
PSU to 
Replace 
Replace With 
AcBel AC 
AcBel DC 
Delta AC 
Gospower 
AC 
Delta DC 
Gospower 
DC 
AcBel AC 
See Hot Swapping an 
AcBel AC PSU with 
an AcBel AC PSU. 
Power down the unit. 
Replace both AC 
PSUs with DC PSUs.  
See Replacing an 
AcBel AC PSU with 
an AcBel DC PSU.  
Power down the unit. 
Replace both PSUs. 
See Replacing an AcBel 
AC PSU with a 
Delta/Gospower AC 
PSU. 
Power down the unit. 
Replace both PSUs. 
See Replacing an 
AcBel AC PSU with a 
Delta/Gospower DC 
PSU. 
AcBel DC 
Power down the unit. 
Replace both PSUs to 
AC. Don’t mix AC/DC.  
See Replacing an 
AcBel DC PSU with 
an AcBel AC PSU. 
See Hot Swapping an 
AcBel DC PSU with 
an AcBel DC PSU. 
Power down the unit. 
Replace both PSUs. 
See Replacing an AcBel 
DC PSU with a 
Delta/Gospower AC 
PSU. 
Power down the unit. 
Replace both PSUs. 
See Replacing an 
AcBel DC PSU with a 
Delta/Gospower DC 
PSU. 
Delta AC 
Power down the unit. 
Replace both PSUs to 
AC. Don’t mix AC/DC. 
See Replacing a 
Delta/Gospower AC 
PSU with an AcBel 
AC PSU. 
Power down the unit. 
Replace both PSUs to 
AC. Don’t mix AC/DC. 
See Replacing a 
Delta/Gospower AC 
PSU with an AcBel 
DC PSU. 
See Hot Swapping a 
Delta/Gospower AC 
PSU with a 
Delta/Gospower AC 
PSU. 
See Hot Swapping a 
Delta/Gospower AC 
PSU with a 
Delta/Gospower DC 
PSU. 
Gospower 
AC  
Delta DC 
Power down the unit. 
Replace both PSUs to 
AC. Don’t mix AC/DC. 
See Replacing a 
Delta/Gospower DC 
PSU with an AcBel 
AC PSU. 
Power down the unit. 
Replace both PSUs to 
DC. Don’t mix AC/DC. 
See Replacing a 
Delta/Gospower DC 
PSU with an AcBel 
DC PSU. 
See Hot Swapping a 
Delta/Gospower DC 
PSU with a 
Delta/Gospower AC 
PSU. 
See  
Hot Swapping a 
Delta/Gospower DC 
PSU with a 
Delta/Gospower DC 
PSU. 
• 
Both PSUs in a unit must be from the same vendor. 
• 
When using Gospower or Delta PSUs, AC and DC PS mix (from same vendor) is allowed on a 
single unit. AcBel does not support an AC/DC PS mix. 
ETX-2i Devices 
3. Operation and Maintenance 
Note 
For increased product survivability and improved redundancy efficiency, it is 
recommended to use a dual power supply fed by two different power sources 
(for the two AC or DC PSUs) or different phases (for the two AC PSUs). 
Hot Swapping an AcBel AC PSU with an AcBel AC PSU 
You can hot swap one or both AcBel AC PSUs with AcBel AC PSUs. 
 To hot swap an AcBel AC PSU with an AcBel AC PSU: 
1. Extract the AcBel AC PSU that you want to remove from the device (see  
 
ETX-2i Devices 
3. Operation and Maintenance 
2. Extracting an AcBel AC PSU). 
3. Install in the now empty PS slot, a new AcBel AC PSU (see Installing an AcBel AC PSU). 
Hot Swapping an AcBel DC PSU with an AcBel DC PSU 
You can hot swap one or both AcBel DC PSUs with AcBel DC PSUs. 
An AcBel DC PSU is supplied with a PS cable connected to a terminal block (TB) plug. 
Note 
It is not advisable to disconnect the PS cable from the TB plug.  
 To hot swap an AcBel DC PSU with an AcBel DC PSU: 
1. Extract the AcBel DC PSU that you want to remove from the device (see Extracting an AcBel DC 
PSU). 
2. Install in the now empty PS slot, a new AcBel DC PSU (see Installing an AcBel DC PSU). 
Replacing an AcBel AC PSU with an AcBel DC PSU 
When two AcBel PSUs of the same type reside in a single device – both must be AC or both DC. It is not 
permitted to mix AcBel AC and DC PSUs on the same device under power at any stage. Therefore, when 
changing a PSU from AC to DC, you must also replace the other PSU from AC to DC. 
Before replacing AcBel AC PSUs with AcBel DC PSUs, you must power down the unit and remove both 
installed AC PSUs, as hot swapping is not supported. Failure to do so can cause the device to reset. 
Each AcBel DC PSU is supplied with a PS cable connected to a terminal block (TB) plug. 
 
Note 
It is not advisable to disconnect the PS cable from the TB plug.  
 To replace an AcBel AC PSU with an AcBel DC PSU: 
1. Remove the power cord from the mains outlets (if two AcBel AC PSUs reside in the device, 
remove both power cords). Verify that the unit powers down and the PWR LED turns off.  
2. Remove each installed AcBel AC PSU: (see  
 
ETX-2i Devices 
3. Operation and Maintenance 
3. Extracting an AcBel AC PSU). After removing the AC power cords from the connectors of the AC 
PSUs, verify that the PS LED on each PSU front panel is not lit (no PSU is working). 
4. Install in one or both now empty PSU slots, an AcBel DC PSU (see Installing an AcBel DC PSU).  
5. Connect the power cables of the power supplies to the mains outlets. The unit turns on 
automatically. Verify that the PWR LED on the device is green. 
Replacing an AcBel DC PSU with an AcBel AC PSU 
When two AcBel PSUs of the same type reside in a single device – both must be AC or both DC. It is not 
permitted to mix AcBel AC and DC PSUs on the same device under power at any stage. Therefore, when 
changing a PSU from DC to AC, you must also replace the other PSU from DC to AC. 
Before replacing AcBel DC PSUs with AC PSUs, you must power down the unit, as hot swapping is not 
supported. Failure to do so can cause the device to reset. 
 To replace an AcBel DC PSU with an AcBel AC PSU: 
1. Remove the power cord from the mains outlets (if two AcBel DC PSUs reside in the device, 
remove both power cords). Verify that the unit powers down and the PWR LED turns off.  
2. Remove each installed AcBel DC PSU: (see Extracting an AcBel DC PSU). After removing the 
TB plugs from the VDC-IN connectors of the AcBel DC PSUs, verify that the PS LED on each PSU 
front panel is not lit (no PSU is working). 
3. Install in one or both now empty PSU slots, an AcBel AC PSU (see Installing an AcBel AC PSU). 
4. Connect the power cord to the mains outlets. The unit turns on automatically. Verify that the 
PWR LED on the device is green. 
Replacing an AcBel AC PSU with a Delta/Gospower AC PSU 
It is not permitted to mix an AcBel PSU and a PSU of another vendor on the same device under power at 
any stage. Therefore, when replacing an AcBel AC PSU with Delta/Gospower AC PSU, you must also 
replace the other AcBel AC PSU with a PSU (AC or DC) of the same vendor as the first. 
Before replacing AcBel AC PSUs with PSUs of another vendor, you must power down the unit, as hot 
swapping is not supported. Failure to do so can cause the device to reset. 
 To replace an AcBel AC PSU with a Delta/Gospower AC PSU: 
1. Remove the power cord from the mains outlets (if two AC PSUs reside in the device, remove 
both power cords). Verify that the unit powers down and the PWR LED turns off.  
ETX-2i Devices 
3. Operation and Maintenance 
2. Remove each installed AcBel AC PSU: (see  
 
ETX-2i Devices 
3. Operation and Maintenance 
3. Extracting an AcBel AC PSU). After removing the AC power cords from the connectors of the AC 
PSUs, verify that the PS LED on each PSU front panel is not lit (no PSU is working). 
4. Install a Delta/Gospower AC PSU into the empty PS slot (see Installing a Delta/Gospower AC 
PSU). 
5. If you are installing a second PSU, it must be from the same vendor as the first PSU.  
 
For AC, see Installing a Delta/Gospower AC PSU.  
 
For DC, see Installing a Delta/Gospower DC PSU.  
6. Connect the power cord to the mains outlets. The unit turns on automatically. Verify that the 
PWR LED on the device is green. 
Replacing an AcBel AC PSU with a Delta/Gospower DC PSU 
It is not permitted to mix an AcBel PSU and a PSU of another vendor on the same device under power at 
any stage. Therefore, when replacing an AcBel AC PSU with Delta/Gospower DC PSU, you must also 
replace the other AcBel AC PSU with Delta/Gospower PSU (AC or DC) of the same vendor as the first. 
Before replacing AcBel AC PSUs with PSUs of another vendor, you must power down the unit, as hot 
swapping is not supported. Failure to do so can cause the device to reset. 
A Delta or Gospower DC PSU is supplied with a DC adaptor and three terminals for connecting DC wires. 
 To replace an AcBel AC PSU with a Delta/Gospower DC PSU: 
1. Remove the power cord from the mains outlets (if two AC PSUs reside in the device, remove 
both power cords). Verify that the unit powers down and the PWR LED turns off.  
2. Remove each installed AcBel AC PSU: (see  
 
ETX-2i Devices 
3. Operation and Maintenance 
3. Extracting an AcBel AC PSU). After removing the AC power cords from the connectors of the AC 
PSUs, verify that the PS LED on each PSU front panel is not lit (no PSU is working). 
4. Install a Delta/Gospower DC PSU into the empty PS slot (see Installing a Delta/Gospower DC 
PSU).  
 
 
ETX-2i Devices 
3. Operation and Maintenance 
5. If you are installing a second PSU, it must be from the same vendor as the first PSU.  
 
For AC, see Installing a Delta/Gospower AC PSU.  
 
For DC, see Installing a Delta/Gospower DC PSU.  
6. Connect the power cables of the power supplies to the mains outlets. The unit turns on 
automatically. 
Replacing an AcBel DC PSU with a Delta/Gospower AC PSU 
It is not permitted to mix an AcBel PSU and a PSU of another vendor on the same device under power at 
any stage. Therefore, when replacing an AcBel DC PSU with Delta/Gospower AC PSU, you must also 
replace the other AcBel DC PSU with a PSU (AC or DC) of the same vendor as the first. 
Before replacing AcBel DC PSUs with PSUs of another vendor, you must power down the unit, as hot 
swapping is not supported. Failure to do so can cause the device to reset. 
 To replace an AcBel DC PSU with a Delta/Gospower AC PSU: 
1. Remove the power cord from the mains outlets (if two DC PSUs reside in the device, remove 
both power cords). Verify that the unit powers down and the PWR LED turns off.  
2. Remove each installed AcBel DC PSU: (see Extracting an AcBel DC PSU). After removing the 
TB plugs from the VDC-IN connectors of the AcBel DC PSUs, verify that the PS LED on each PSU 
front panel is not lit (no PSU is working). 
3. Install a Delta/Gospower AC PSU into the empty PS slot (see Installing a Delta/Gospower AC 
PSU). 
4. If you are installing a second PSU, it must be from the same vendor as the first PSU.  
 
For AC, see Installing a Delta/Gospower AC PSU.  
 
For DC, see Installing a Delta/Gospower DC PSU.  
5. Connect the power cable to the mains outlets. The unit turns on automatically. Verify that the 
PWR LED on the device is green. 
Replacing an AcBel DC PSU with a Delta/Gospower DC PSU 
It is not permitted to mix an AcBel PSU and a PSU of another vendor on the same device under power at 
any stage. Therefore, when replacing an AcBel DC PSU with a Delta/Gospower DC PSU, you must also 
replace the other AcBel DC PSU with a PSU (AC or DC) of the same vendor as the first. 
Before replacing AcBel DC PSUs with PSUs of another vendor, you must power down the unit, as hot 
swapping is not supported. Failure to do so can cause the device to reset. 
ETX-2i Devices 
3. Operation and Maintenance 
 To replace an AcBel DC PSU with a Delta/Gospower DC PSU: 
1. Remove the power cord from the mains outlets (if two DC PSUs reside in the device, remove 
both power cords). Verify that the unit powers down and the PWR LED turns off.  
2. Remove each installed AcBel DC PSU: (see Extracting an AcBel DC PSU). After removing the 
TB plugs from the VDC-IN connectors of the AcBel DC PSUs, verify that the PS LED on each PSU 
front panel is not lit (no PSU is working). 
3. Install a Delta/Gospower DC PSU into the empty PS slot (see Installing a Delta/Gospower DC 
PSU). 
4. If you are installing a second PSU, it must be from the same vendor as the first PSU.  
 
For AC, see Installing a Delta/Gospower AC PSU.  
 
For DC, see Installing a Delta/Gospower DC PSU.  
5. Connect the power cord to the mains outlets. The unit turns on automatically. Verify that the 
PWR LED on the device is green. 
Replacing a Delta/Gospower AC PSU with an AcBel AC PSU  
It is not permitted to mix an AcBel PSU and a PSU of another vendor on the same device under power at 
any stage. Also, when two AcBel PSUs of the same type reside in a single device – both must be AC or 
both DC. It is not permitted to mix AcBel AC and DC PSUs on the same device under power at any stage. 
Before replacing Delta/Gospower PSUs with AcBel AC PSUs, you must power down the unit and remove 
both installed Delta/Gospower PSUs, as hot swapping is not supported. Failure to do so can cause the 
device to reset.  
 To replace a Delta/Gospower AC PSU with an AcBel AC PSU: 
1. Remove the power cord from the mains outlets (if two PSUs reside in the device, remove both 
power cords). Verify that the unit powers down and the PWR LED turns off.  
2. Remove the power cords from each Delta/Gospower PSU installed in the device, and extract the 
PSUs:  
 
From AC PSU: See Extracting a Delta/Gospower AC PSU. 
 
From DC PSU: See Extracting a Delta/Gospower DC PSU. 
Verify that the PS LED on each PSU front panel is not lit (no PSU is working). 
3. Install an AcBel AC PSU in one or both now empty PSU slots (see Installing an AcBel AC PSU). 
4. Connect the power cords to the mains outlets. The unit turns on automatically. Verify that the 
PWR LED on the device is green. 
ETX-2i Devices 
3. Operation and Maintenance 
Replacing a Delta/Gospower AC PSU with an AcBel DC PSU 
It is not permitted to mix an AcBel PSU and a PSU of another vendor on the same device under power at 
any stage. Also, when two AcBel PSUs of the same type reside in a single device – both must be AC or 
both DC. It is not permitted to mix AcBel AC and DC PSUs on the same device under power at any stage. 
Before replacing Delta/Gospower PSUs with AcBel DC PSUs, you must power down the unit and remove 
both installed Delta/Gospower PSUs, as hot swapping is not supported. Failure to do so can cause the 
device to reset.  
 To replace a Delta/Gospower AC PSU with an AcBel DC PSU: 
1. Remove the power cord from the mains outlets (if two PSUs reside in the device, remove both 
power cords). Verify that the unit powers down and the PWR LED turns off. 
2. Remove the power cords from each Delta/Gospower PSU installed in the device, and extract the 
PSUs:  
 
From AC PSU: See Extracting a Delta/Gospower AC PSU. 
 
From DC PSU: See Extracting a Delta/Gospower DC PSU. 
Verify that the PS LED on each PSU front panel is not lit (no PSU is working). 
3. Install an AcBel DC PSU in one or both now empty PSU slots (see Installing an AcBel DC PSU).  
4. Connect the power cables of the power supplies to the mains outlets. The unit turns on 
automatically. Verify that the PWR LED on the device is green. 
Replacing a Delta/Gospower DC PSU with an AcBel AC PSU  
It is not permitted to mix an AcBel PSU and a PSU of another vendor on the same device under power at 
any stage. Also, when two AcBel PSUs of the same type reside in a single device – both must be AC or 
both DC. It is not permitted to mix AcBel AC and DC PSUs on the same device under power at any stage. 
Before replacing Delta/Gospower PSUs with AcBel AC PSUs, you must power down the unit and remove 
both installed Delta/Gospower PSUs, as hot swapping is not supported. Failure to do so can cause the 
device to reset.  
 To replace a Delta/Gospower DC PSU with an AcBel AC PSU: 
1. Remove the power cord from the mains outlets (if two PSUs reside in the device, remove both 
power cords). Verify that the unit powers down and the PWR LED turns off. 
 
 
ETX-2i Devices 
3. Operation and Maintenance 
2. Remove the power cords from each Delta/Gospower PSU installed in the device, and extract the 
PSUs:  
 
From AC PSU: See Extracting a Delta/Gospower AC PSU. 
 
From DC PSU: See Extracting a Delta/Gospower DC PSU. 
Verify that the PS LED on each PSU front panel is not lit (no PSU is working). 
3. Install an AcBel AC PSU in one or both now empty PSU slots (see Installing an AcBel AC PSU). 
4. Connect the power cable to the mains outlets. The unit turns on automatically. Verify that the 
PWR LED on the device is green. 
Replacing a Delta/Gospower DC PSU with an AcBel DC PSU  
It is not permitted to mix an AcBel PSU and a PSU of another vendor on the same device under power at 
any stage. Also, when two AcBel PSUs of the same type reside in a single device – both must be AC or 
both DC. It is not permitted to mix AcBel AC and DC PSUs on the same device under power at any stage. 
Before replacing Delta/Gospower PSUs with AcBel DC PSUs, you must power down the unit and remove 
both installed Delta/Gospower PSUs, as hot swapping is not supported. Failure to do so can cause the 
device to reset.  
 To replace a Delta/Gospower DC PS with an AcBel DC PSU: 
1. Remove the power cords from the mains outlets (if two PSUs reside in the device, remove both 
power cords). Verify that the unit powers down and the PWR LED turns off. 
2. Remove the power cords from each Delta/Gospower PSU installed in the device, and extract the 
PSUs:  
 
From AC PSU: See Extracting a Delta/Gospower AC PSU. 
 
From DC PSU: See Extracting a Delta/Gospower DC PSU. 
Verify that the PS LED on each PSU front panel is not lit (no PSU is working). 
3. Install an AcBel DC PSU in one or both now empty PSU slots (see Installing an AcBel DC PSU).  
4. Connect the power cable to the mains outlets. The unit turns on automatically. Verify that the 
PWR LED on the device is green. 
Hot Swapping a Delta/Gospower AC PSU with a Delta/Gospower AC PSU 
You can hot swap Delta/Gospower power supplies with Delta/Gospower power supplies. If there are 
two PSUs in the device, following replacement, both must be from the same vendor (Delta or 
Gospower), and can both be AC, DC, or an AC/DC mix. 
ETX-2i Devices 
3. Operation and Maintenance 
 To hot swap a Delta/Gospower AC PSU with a Delta/Gospower AC PSU: 
1. Remove the Delta/Gospower AC PSU (see Extracting a Delta/Gospower AC PSU).  
2. Install the new Delta/Gospower AC PSU (see (see Installing a Delta/Gospower AC PSU). 
3. If you switched to a PSU from a different vendor, replace the other PSU with one of that same 
vendor (can be AC or DC). 
Hot Swapping a Delta/Gospower AC PSU with a Delta/Gospower DC PSU 
You can hot swap Delta/Gospower power supplies with Delta/Gospower power supplies. If there are 
two PSUs in the device, following replacement, both must be from the same vendor (Delta or 
Gospower), and can both be AC, DC, or an AC/DC mix. 
 To hot swap a Delta/Gospower AC PSU with a Delta/Gospower DC PSU: 
1. Remove the Delta/Gospower AC PSU (see Extracting a Delta/Gospower AC PSU).  
2. Install the new Delta/Gospower DC PSU (see Installing a Delta/Gospower DC PSU). 
3. If you switched to a PSU from a different vendor, replace the other PSU with one of that same 
vendor (can be AC or DC).  
Hot Swapping a Delta/Gospower DC PSU with a Delta/Gospower AC PSU 
You can hot swap Delta/Gospower power supplies with Delta/Gospower power supplies. If there are 
two PSUs in the device, following replacement, both must be from the same vendor (Delta or 
Gospower), and can both be AC, DC, or an AC/DC mix. 
 To hot swap a Delta/Gospower DC PSU with a Delta/Gospower AC PSU: 
1. Remove the Delta/Gospower DC PSU (see Extracting a Delta/Gospower DC PSU). 
2. Install the new Delta/Gospower AC PSU (see Installing a Delta/Gospower AC PSU). 
3. If you switched to a PSU from a different vendor, replace the other PSU with one of that same 
vendor (can be AC or DC).  
 
 

## 3.5 Maintenance  *(p.227)*

ETX-2i Devices 
3. Operation and Maintenance 
Hot Swapping a Delta/Gospower DC PSU with a Delta/Gospower DC PSU 
You can hot swap Delta/Gospower power supplies with Delta/Gospower power supplies. If there are 
two PSUs in the device, following replacement, both must be from the same vendor (Delta or 
Gospower), and can both be AC, DC, or an AC/DC mix. 
 To hot swap a Delta/Gospower DC PSU with a Delta/Gospower DC PSU: 
1. Remove the Delta/Gospower DC PSU (see Extracting a Delta/Gospower DC PSU). 
2. Install the new Delta/Gospower DC PSU (see Installing a Delta/Gospower DC PSU). 
3. If you switched to a PSU from a different vendor, replace the other PSU with one of that same 
vendor (can be AC or DC). 
3.5 Maintenance 
Caution 
• 
In case of fan failure, the ETX unit must be replaced as soon as possible. 
Once a replacement unit is available and configured, the estimated 
replacement time is two minutes and must be performed by a qualified 
technician. 
The NOC technician is notified of a fan failure by a trap sent to the 
network management platform. 
• 
Only qualified, authorized, and skilled service personnel should carry out 
adjustment, maintenance, or repairs to this product. Operators and 
users should not perform installation, adjustment, maintenance, or 
repairs. 
• 
Always observe standard safety precautions during installation, 
operation, and maintenance of this product. Precautions listed in this 
document are supplements to local safety regulations for installation. 
• 
RAD shall be released from all obligations under its warranty in the 
event that the equipment has been subjected to misuse, neglect, 
accident, or improper installation, or if repairs or modifications were 
made by persons other than RAD's own authorized service personnel, 
unless such repairs by others were made with the written consent of 
RAD. 
One of the following warning labels is affixed to ETX-2i devices. 
Before servicing equipment, you are required to disconnect all power supply cords. 

## 3.6 Turning Off the Unit  *(p.228)*

ETX-2i Devices 
3. Operation and Maintenance 
                    
 
When an outdoor device requires servicing, open the external door of the unit using a Phillips 
screwdriver. Opening the door clicks the rails into place, thus securing the door into its open position, so 
that it doesn’t close on its own on windy days. 
When done servicing the device, push the rails upward to release the door, close the door, and then 
secure it closed using a Phillips screwdriver. 
3.6 Turning Off the Unit 
 To power off the unit: 
• 
Remove the power cord from the power source. 
 