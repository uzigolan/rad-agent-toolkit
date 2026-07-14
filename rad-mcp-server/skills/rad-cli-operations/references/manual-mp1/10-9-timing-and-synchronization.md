# 9 Timing and Synchronization

*Manual `MP-1-mn_ver 2.2.pdf`, pages 357–376.*


## 9.1 Clock Selection  *(p.357)*

9.1 Clock Selection  
Megaplex-1 flexible timing options enable reliable distribution of timing together with flexible selections 
of timing sources, including support for an external station clock interface that enables daisy-chaining 
the clock signals to other equipment.  
Functional Description  
System Timing Modes  
The Megaplex-1 timing subsystem can use the following types of reference sources: 
• 
Internal Megaplex-1 oscillator 
• 
Clock signal derived from the pseudowire  
• 
Station clock, which uses an external clock signal supplied to the Megaplex-1 CLOCK connector.  
• 
Recovered from one of the 8 E1/T1 interfaces 
When clock source selection is purely TDM-based (Internal / Station timing / External E1/T1 timing), 
timing quality meets Stratum-4 level with timing precision of ± 32ppm. 
When clock source selection comes from PSN clock recovery the quality is according to ITU G.8261 and 
MEF-22 recommendations with timing precision of 16 ppb. ACR (Adaptive Clock Recovery) meets jitter 
and wander requirements of G.8261, G.823 and G.824 recommendations. 
Internal Timing Mode 
In most Megaplex-1 applications, an external clock source is used. The internal oscillator is used as a last 
recourse timing source: it is automatically selected when no source is capable of providing a good timing 
reference.  
Megaplex-1 
9. Timing and Synchronization 
Station Timing 
When the station timing mode is used as one of the 4 clock sources, the Megaplex-1 system (nodal) 
timing is synchronized to an external clock signal delivered to the dedicated station clock interface. This 
signal is usually provided by a highly-accurate clock source, configured with the highest priority, which is 
often available in communication facilities (for example, a signal provided by a GPS-based timing source, 
an independent primary clock source, or other suitable clock source). The clock signal frequency is 
user-selectable: 2048 Mbps, or 1.544 Mbps.  
The station clock has software-selectable interfaces: 
• 
ITU-T Rec. G.703 interface. The clock interface (balanced/unbalanced) and sensitivity (long or 
short range) are also user-selectable 
• 
RS-422 interface for squarewave signals, which is the recommended interface when timing 
quality is critical. Note that this interface is suitable for short cable runs, interconnecting 
equipment units located in close proximity. 
The station clock interface also provides an output clock signal, for chaining applications. The source of the 
output clock is locked to the system timing.   
Clock Domain  
Clock Mode 
The domain clock mode can be one of the following: 
• 
Auto mode – domain timing is determined by the clock selection algorithm (default) 
• 
Free-run mode – the domain clock is based on the main card local oscillator  
Clock Domain States 
Clock domain states indicate operation modes of the system clock (T0 timing generator). 
System clock: 
• 
Locked – Locked to selected clock source 
• 
Free-run – Locked to internal oscillator 
Note 
By default, the Megaplex-1 system clock is in free-run state, until a valid clock 
source is selected 
 
Megaplex-1 
9. Timing and Synchronization 
Note 
Switching between clock sources might cause a momentary hit in traffic.  
External Switch Commands 
You can issue manual or forced switch commands to choose a specific clock source. The manual 
command overrides the clock priority setting and allows selection of a clock with a priority lower than an 
automatically selected clock source.  
The forced switch command allows selection of any clock source, regardless of its priority. It overrides 
the previously issued manual switch command. 
The manual and forced switch commands are cleared using the clear command. 
Station/System Clock Squelch per Remote Domain Failure   
Megaplex-1 features station clock squelch with fault propagation over PWE between clock sources and 
station clock. This capability allows disabling the transmit (squelch) of the station clock when the central 
devices lose connectivity to the external clock source. 
Squelching is done according to the user configured QL minimum value, by comparing this user-
configured value to the reported quality level of the current selected synchronization source. 
To activate the squelch, you need to configure the station clock  quality min-level-station and/or the 
system clock (quality min-level-system) to quality above sec or sts3e. 
If quality level of domain clock is less than the configured ‘min-level-system’ or no valid sources are 
defined, the following happens: 
• 
 ‘system_clock_ql_low’ alarm is reported 
• 
If the PW is configured to ‘domain-failure-indication’, the indication is sent to the far-end device. 
To define a PW to carry a failure indication if local domain clock fails, you must configure the PW using 
the following commands:  
• 
Set domain-failure-indication to activate fault propagation 
• 
Define the conditions when the PW is considered failed for the CSM by source-clock-fail [pw-
down] [remote-domain-down] command: 
 
pw-down – PW failure (always enabled) 
 
remote-domain-down – Once the PW receives an indication of failure from the far-end side, 
the PW clock moves to the fail state.  
Megaplex-1 
9. Timing and Synchronization 
If quality level of domain clock less than the configured ‘min-level-station’ or no valid sources are 
defined, the alarm ‘station_clock_ql_low’ is reported and station clock is squelched. 
The WTR functionality is automatically derived from the configuration of each clock source. 
This configuration is performed per PW under config>pwe>pw(<pw-number>)# prompt (see 
Configuring Pseudowires in Chapter 8). 
Factory Defaults 
The table below lists the parameter defaults for the Clock Domain, Clock Source and Station Clock 
configuration. 
Parameter  
Default Value 
domain  
mode 
auto 
clock-source 
priority 
4 
wait-to-restore 
300 (s) 
hold-off 
300 (ms) 
station 
interface-type  
e1, balanced 
rx-sensitivity  
short-haul  
line-type  
g732n-crc 
Configuring the Clock Domain  
 To configure the clock domain: 
1. Navigate to configure system clock domain 1. 
The config>system>clock>domain(1)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Megaplex-1 
9. Timing and Synchronization 
Task 
Command 
Comments 
Setting minimum 
clock quality levels 
for the station and 
system clocks 
 
Network type 1 (Europe): 
quality [min-level-station | 
min-level -system <ql1>]  
Network type 2 (USA): quality 
[min -level-station | 
min-level -system <ql2>]  
no quality 
 
ql1 – quality level (according to network type 
1 Europe) 
Possible values: quality-level {prc | ssu-a | 
ssu-b | sec | dnu}  
Default: dnu 
ql2 – quality level (according to network type 
2 USA) 
quality-level { prs | stu | st2 | tnc | st3e | st3 
| smc | st4 | dus | prov } 
Default: dus 
The quality values are according to the 
synchronization network type defined for the 
domain.  
no quality removes the minimum quality 
parameter. If no minimum quality is defined 
for the domain, you cannot configure the 
quality level for the sources. A clock source 
with a quality level lower than the defined 
minimum quality is ignored by the clock 
selection mechanism. 
Setting clock mode 
mode {auto | free-run} 
auto –Clock selection mechanism functions 
normally, e.g. the best available clock source 
is selected for synchronization 
free-run – Internal oscillator is used for 
synchronization 
Forcing selection of 
a particular clock 
source when the 
sources have 
different quality 
levels 
force <source-id> 
The range of source-id is 1 to 4. 
Manually selecting 
a particular clock 
source  
manual <source-id> 
The selection is performed in the following 
conditions: 
• No quality is defined for the clock domain 
•  The sources have the same qualities 
• The sources have different priorities. 
Megaplex-1 
9. Timing and Synchronization 
Task 
Command 
Comments 
Canceling 
previously issued 
force or manual 
command 
clear 
 
Adding clock source 
source <src-id> station 0/1 
source <src-id> pw <pw 
number> 
source <src-id> rx-port e1 
<1/port> 
source <src-id> rx-port t1 
<1/port> 
Typing no source <src-id> deletes the source. 
Refer to Configuring the Clock Sources  
 
Configuring clock 
source  
source <src-id>  
Typing no source <src-id> deletes the source  
Refer to Configuring the Clock Sources 
Example  
 
#Central device Megaplex-4 (device that distributes clock over the 
system): 
 
configure pwe pw 13 
   domain-failure-indication 
exit all 
 
configure system clock domain 1 
sync-network-type 1  
    quality min-level-system prc 
    source 1 station cl-a/1 
        priority 1 
        quality-level prc 
exit all 
 
 
#Remote device Megaplex-1 (any node that takes clock from Central 
device) 
 
configure pwe pw 13 
   source-clock-fail remote-domain-down  
exit all 
 
configure system clock domain 1 
sync-network-type 1 
      quality min-level-station prc  
Megaplex-1 
9. Timing and Synchronization 
      source 1 pw 13 
            priority 1 
exit all 
Displaying the Clock Domain Status  
 To view the clock domain status: 
• 
At the system>clock>domain(1)#, enter show status. 
The clock source status is displayed.   
The possible clock states are explained in the following table. 
Parameter 
Displayed 
Description 
Free Run  
Indicates that the nodal timing system is locked to the internal oscillator  
Locked 
Indicates that the nodal timing is locked on one of the clock references.  
Example 1: Megaplex-1 domain is locked to Source 1 
config>system>clock>domain(1)# show status 
System Clock Source : 1         State  : Locked     
Force Switch        : InActive 
Manual Switch       : InActive  
Example 2: Clock Domain Mode is configured to “free-run” or “auto” but all sources are down and no 
clock selection is performed.  
config>system>clock>domain(1)# show status 
System Clock Source      : 0    State  : Freerun      
Force Switch        : Inactive                                   
  Manual Switch       : Inactive        
Configuring the Clock Sources 
You can define up to 4 clock sources for the domain. The sources can be:  
• 
Station clock (1) 
• 
PW clock (4).  
• 
Rx-port E1/T1 clock (1 or 2) 
Megaplex-1 
9. Timing and Synchronization 
 To add a clock source:  
1. Verify that the clock source to be used as an input is valid. 
Note 
You can choose an invalid clock source. However, this input will be rejected by 
the domain during the clock selection process.  
2. Verify that the card whose port will be used as a source clock is provisioned. 
3. Verify that the port to be used as a source clock is enabled (no shutdown). 
4. Navigate to configure system clock domain 1. 
The config>system>clock>domain(1)# prompt is displayed. 
5. Type one of the following, according to the required clock source: 
source <src-id> station <slot>/1 
source <src-id> pw <pw-id>  
source <src-id> rx-port e1 <1/port> 
source <src-id> rx-port t1 <1/port> 
no source   
The clock source is created and the config>system>clock>domain(1)>source(<1–10>)# prompt 
is displayed.  
6. Enter all necessary commands according to the tasks listed below the following procedure. 
 To configure a clock source for which the port has been defined: 
1. Navigate to configure system clock domain 1. 
The config>system>clock>domain(1)# prompt is displayed. 
2. Type source <1–4> to select the source to configure.  
The config>system>clock>domain(1)>source(<1–4>)# prompt is displayed. 
3. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting priority 
 
priority <1–4> 
Priority 1 is the highest.  
Defining the time that a 
previously failed 
synchronization source 
must be fault-free in order 
to be considered available  
wait-to-restore <0–720> 
The time is defined in seconds. 
Megaplex-1 
9. Timing and Synchronization 
Task 
Command 
Comments 
Defining the time  that 
signal failure must be 
active before it is 
transmitted  
hold-off <300–1800> 
The time is defined in milliseconds.  
Canceling the 
wait-to-restore timer of a 
clock source 
clear-wait-to-restore 
This option is useful if a timing source fault is 
cleared and you want to souce to be 
immediately available.   
Displaying the Clock Source Status  
 To view the clock source status: 
• 
At the system>clock> domain(1)>source(<1–4>)#, enter show status. 
The clock source status is displayed.  
config>system>clock>domain(1)>source(1)# show status 
Status     : OK 
WTR State  : Inactive 
The clock status provides information about: 
 
Clock source status: 
 
OK – The clock source is valid and can be considered as clock input candidate for the 
system clock 
 
Physical Fail – Clock failure has been detected at the physical level 
 
WTR State – Wait-to-restore counter status 
 
Running – WTR Timer is running (when the clock source returns after signal failure (SF), 
WTR timer is used to verify that the clock source stable state is not intermittent) 
 
Inactive – WTR Timer is inactive (clock source status is OK). 
Configuring the Station Clock 
The station clock is an E1 or T1 port that can be used for synchronization. You can set the station clock 
timing to be based on the system clock or recovered from the received signal of the station clock. 
 To configure the station clock:  
1. Navigate to configure system clock station 0/1. 
Megaplex-1 
9. Timing and Synchronization 
The config>system>clock>station(0/1)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
 
Task 
Command 
Comments 
Selecting the rate and 
type of signal accepted 
and transmitted via the 
station clock port  
 
interface-type {e1 | t1}  
 
 
e1 – 2.048 Mbps signal per ITU-T 
Rec. G.703 Para. 9 
t1 –1.544 Mbps signal per ITU-T Rec. 
G.703 Para. 5.  
Selecting the impedance 
of signal accepted and 
transmitted via the station 
clock port  
impedance {balanced | 
unbalanced} 
For e1 option only. If you specify e1 
and do not specify balanced or 
unbalanced, by default the interface 
is set as balanced 
Setting line code 
 
line-code {b8zs | ami | hdb3} 
hdb3 –High Density Bipolar coding of 
order 3, used for e1 option 
ami –Alternate Mark Inversion 
coding, used for t1 option 
b8zs – Binary-8 zero suppression 
coding, used for t1 option 
Specifying E1 framing 
mode  
line-type { g732n | g732n-crc | 
unframed} 
 
Specifying T1 framing 
mode  
line-type { sf | esf| unframed} 
 
 
Setting receiver sensitivity 
to adjust the signal 
capability to reach 
destinations close by or 
farther away 
rx-sensitivity {short-haul | 
long-haul} 
short-haul – maximum allowable 
attenuation of 10 dB, relative to the 
nominal transmit level 
long-haul – maximum allowable 
attenuation of 34 dB, relative to the 
nominal transmit level  
Administratively enabling 
station clock 
no shutdown 
Using shutdown disables the station 
clock 
Megaplex-1 
9. Timing and Synchronization 
Displaying the Station Clock Status  
 To view the station clock status: 
• 
At the system>clock>station (0/1)# prompt, enter show status. 
The station clock status is displayed. 
mp4100>config>system>clock>station(0/1)# show status 
Name                  : station 0/1 
Administrative Status : Down 
Operational Status    : Down 
Configuring the PW Clock  
Pseudowires can be selected as timing sources for the Megaplex-1 nodal timing subsystem. This timing 
mode is called adaptive clock recovery.   
 To configure the PW clock:  
1. Navigate to configure system clock pw <1..16>.  
The config>system>clock>pw (<pw number>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Associating the PW 
number to the clock   
pw <PW number> 
 
The possible PW number range is 1 to 16. 
Administratively enabling 
the PW clock 
no shutdown 
Using shutdown disables the PW clock 
Displaying the Pseudowire Clock Status  
 To view the PW clock status:  
• 
At the system>clock>pw (<PW number)# prompt, enter show status. 
The PW clock status is displayed. 
Megaplex-1 
9. Timing and Synchronization 
You can also display the number of the PW the recovered clock is locked to, and the network type by 
means of the following command. 
 To display the PW number:  
config>system>clock>pw(1)# info detail 
    pw  1 
    no shutdown 
Configuring the E1/T1 Clock  
 To configure the E1/T1 clock:  
1. Navigate to configure system clock domain 1. 
The config>system>clock>domain(1)# prompt is displayed. 
2. Type one of the following, according to the required clock source: 
3. source <src-id> rx-port e1 <slot>/<port> 
source <src-id> rx-port t1 <slot>/<port> 
The corresponding prompt is displayed. 
4. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Administratively enabling 
the E1/T1 clock 
no shutdown 
Using shutdown disables the E1/T1 clock 
Setting priority 
 
priority <1–4> 
Priority 1 is the highest.  
Defining the time that a 
previously failed 
synchronization source 
must be fault-free in order 
to be considered available  
wait-to-restore <0–720> 
The time is defined in seconds. 
Defining the time  that 
signal failure must be 
active before it is 
transmitted  
hold-off <300–1800> 
The time is defined in milliseconds. 
Megaplex-1 
9. Timing and Synchronization 
Task 
Command 
Comments 
Canceling the 
wait-to-restore timer of a 
clock source 
clear-wait-to-restore 
This option is useful if a timing source 
fault is cleared and you want to souce to 
be immediately available.   
 
Displaying the E1/T1 Clock Source Status 
 To view the clock source status: 
• 
At the system>clock> domain(1)>source(<1–4>)#, enter show status. 
The clock source status is displayed.  
mp4100>config>system>clock>domain(1)>source(1)# show status 
Status     : Physical Fail 
Tx Quality : DNU 
Rx Quality : PRC 
ESMC State : Unlocked  
WTR State  : Running   
The clock status provides information about: 
 
Clock source status: 
 
OK – The clock source is valid and can be considered as clock input candidate for the 
system clock 
 
Physical Fail – Clock failure has been detected at the physical level 
 
Monitoring Fail – Clock failure has been detected by the clock monitoring entity of the 
domain. One reason for declaring a monitoring failure state is that the maximum 
frequency deviation of the clock source has been exceeded. 
 
WTR State – Wait-to-restore counter status 
 
Running – WTR Timer is running (when the clock source returns after signal failure (SF), 
WTR timer is used to verify that the clock source stable state is not intermittent) 
 
Inactive – WTR Timer is inactive (clock source status is OK). 
Configuration Errors 
The following table lists messages generated by Megaplex-1 when a configuration error is detected. 
 

## 9.2 Date and Time  *(p.370)*

Megaplex-1 
9. Timing and Synchronization 
Message 
Description 
Invalid Domain Number 
Megaplex-1 support only domain 1.  
Invalid Source Number       
Only 4 clock sources are supported.  
Duplicated Source           
You are trying to configure the same source twice 
Invalid Priority 
Only 4 clock priorities are supported (1 is the highest priority) 
Invalid Holdoff Timer       
Holdoff timer value is out of range [300..1800] 
Invalid WTR Timer       
Wait-to-restore timer value is out of range [0..720] 
Wait to restore is running 
Force command cannot be executed when WTR timer is 
running. 
Domain source: Station in shutdown 
state 
The station clock in shutdown state cannot be configured as 
a clock source. 
Domain source: PW in shutdown state 
A pw in shutdown state cannot be configured as a clock 
source. 
Domain source: e1/t1 in shutdown 
state                 
An e1/t1 port in shutdown state cannot be configured as a 
clock source 
 
9.2 Date and Time 
You can set the date and time for the Megaplex-1 internal real-time clock.  
Note 
The internal real-time clock is used to time-stamp various messages, alarms, 
etc. The previously attached time stamps are not changed when the time-of-
day is changed as a result of updates.  
When Megaplex-1 is turned off, the real-time clock is kept updated for up to 40 hours. After that, the 
internal real-time clock is reset and will require reconfiguration on the next power-up of the device. 
Setting the Date and Time  
You can set the date and time for the Megaplex-1 internal real-time clock. 
Megaplex-1 
9. Timing and Synchronization 
 To specify the system date and time: 
1. At the config>system# prompt, enter date-and-time. 
The config>system>date-time# prompt appears. 
2. Specify the date and time and associated parameters as illustrated and explained below. 
Task 
Command 
Comments 
Specifying the system date 
date <selected format> 
Default: yyyy-mm-dd 
Selecting the date format 
 
date-format {yyyy-mm-dd | dd-mm-
yyyy | mm-dd-yyyy | yyyy-dd-mm}  
yyyy-mm-dd – ISO format 
dd-mm-yyyy – European 
format 
mm-dd-yyyy – US format 
yyyy-dd-mm – Japanese 
format 
dd stands for day, mm for 
month and yyyy for year  
Specifying the system time 
time <hh:mm[:ss]> 
Seconds are optional. 
It is recommended to set the 
time about one minute 
beyond the desired time, and 
then save at the correct 
instant. 
Example 
 To define dd-mm-yyyy as a date format: 
config>system>date-and-time# date-format dd-mm-yyyy 
 To define January 2, 2011 as the Megaplex-1 date: 
config>system>date-and-time# date 02-01-2011 
 To define 18:23 as the Megaplex-1 time: 
config>system>date-and-time# time 18:23 
Megaplex-1 
9. Timing and Synchronization 
Displaying the Date and Time 
 To view the date and time settings: 
• 
At the config>system# prompt, enter show date-and-time. 
The date, time and the time zone are displayed. 
config>system# show date-and-time UTC +00:00 
2018-03-04   19:52:23    
Working with SNTP  
This section explains how to receive the clock signal from NTP servers in the network. Megaplex-1 can 
synchronize with up to ten servers, sending NTP requests to the servers at user-defined intervals. 
You can set one of the active SNTP servers as the preferred server, so that Megaplex-1 sends NTP 
requests to the preferred server. If there is no preferred server or if the preferred server does not 
answer, then Megaplex-1 sends NTP requests to any enabled servers. 
Factory Defaults 
The default configuration of the SNTP parameters is: 
• 
No SNTP servers defined 
• 
Polling interval set to 15 minutes. 
When an SNTP server is defined, its default configuration is: 
• 
IP address set to 0.0.0.0 
• 
Not preferred 
• 
Administratively disabled (shutdown). 
Configuring SNTP Parameters 
 To configure SNTP parameters: 
1. Navigate to configure system date-and-time sntp. 
The config>system>date-time>sntp# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Megaplex-1 
9. Timing and Synchronization 
3.  
Task 
Command 
Comments 
Enabling Megaplex-1 to listen 
to NTP broadcast messages to 
obtain accurate timestamps 
broadcast 
Type no broadcast to 
disable broadcast mode 
Setting polling interval (in 
minutes) for SNTP requests 
poll-interval interval 
<minutes>         
      
Allowed range is 1–1440 
Defining and configuring SNTP 
servers (see Defining SNTP 
Servers and Configuring SNTP 
Server Parameters)  
server <server-id> 
 
 
 
Displaying SNTP status 
show status 
 
Defining SNTP Servers  
 To define an SNTP server: 
1. Navigate to config system date-and-time sntp. 
The config>system>date-time>sntp# prompt is displayed. 
2. Type server <server-id> to define an SNTP server with ID <server-id>. 
The following prompt is displayed: config>system>date-time>sntp>server(<server-id>)$. The 
SNTP server parameters are configured by default as described in Factory Default. 
3. Configure the SNTP server parameters as needed, as described in Configuring SNTP Server 
Parameters. 
Configuring SNTP Server Parameters 
 To configure SNTP server parameters: 
1. Navigate to config system date-and-time sntp. 
The config>system>date-time>sntp# prompt is displayed. 
2. Type server <server-id> to select the SNTP server to configure. 
The following prompt is displayed: config>system>date-time>sntp>server(<server-id>)# 
3. Enter all necessary commands according to the tasks listed below. 
Megaplex-1 
9. Timing and Synchronization 
Task 
Command 
Comments 
Setting the IP address of the 
server 
address <IP-address> 
 
Set SNTP server as preferred 
server. 
prefer 
 
Type no prefer to remove 
preference 
Note: Only one server can 
be preferred. 
Setting UDP port for NTP 
requests, to a specific UDP 
port or to default UDP port 
(123) 
udp port <udp-port> 
udp default 
Allowed range is 1–65535 
Administratively enabling 
server 
no shutdown 
Using shutdown disables 
the server 
Sending query to server and 
displaying result 
query-server 
 
Example 
 To define SNTP server: 
• 
Server ID = 1 
• 
IP address = 172.17.155.126 
• 
Administratively enabled. 
# configure system date-and-time sntp 
config>system>date-time>sntp# server 1 
config>system>date-time>sntp>server(1)# address 172.17.155.226 
config>system>date-time>sntp>server(1)# no shutdown 
config>system>date-time>sntp>server(1)# commit 
Result : OK 
 To display server information: 
config>system>date-time>sntp>server(1)$ query-server 
Query Server Reply 
----------------------------------------------------------------------
------- 
Server  : 172.17.155.226                          UDP        : 123 
Megaplex-1 
9. Timing and Synchronization 
Date    : 00-00-0000                              Time(UTC)  : 
00:00:00 
Stratum : 0 
Megaplex-1 
0.  
 
 