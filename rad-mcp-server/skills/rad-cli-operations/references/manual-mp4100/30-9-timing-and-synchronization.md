# 9 Timing and Synchronization

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 777–801.*


## Standards  *(p.777)*


## Functional Description  *(p.777)*

Megaplex-4 flexible timing options enable reliable distribution of timing together with flexible selections 
of timing sources, including support for an external station clock interface that enables daisy-chaining 
the clock signals to other equipment.  Megaplex-4 also provides traceable timing quality and supports 
automatic selection of best-quality timing reference. 
Standards  
The CSM module complies with the ITU-T G.781 standard. 
Functional Description  
Megaplex-4 supports one clock domain with up to 5/10 clock sources. The timing subsystem 
automatically selects the best timing source to use for synchronization.  
The maximum number of clock sources is: 
• 
10 sources for /DS0, /155 or /622 assemblies  
• 
5 sources for GBEA assemblies. 
The user can define the following clock sources: 
• 
Recovered from the STM-1/STM -4/OC-3/OC-12 interface, including automatic selection based 
on SSM (Synchronization Status Messaging) 
• 
Recovered from the GbE interface (CL modules only), including automatic selection based on 
ESMC (Ethernet Synchronization Messaging Channel)   
• 
Internal crystal free-running oscillator-based clock 
• 
Clock derived from the receive clock of a specified module user port 
• 
Adaptive clock recovered from a pseudowire circuit (ACR) 
• 
External station clock. 
9. Timing and Synchronization 
Multiple clock sources can be set and assigned a corresponding clock source quality and priority. 
If SDH/SONET, GbE or station clock sources are configured as SSM-based, their quality can be 
determined by monitoring the synchronization status messages.  
Clock Synchronization  
The synchronization network type identifies the type of synchronization network connections and the 
synchronization level. Each synchronization network connection is provided by one or more 
synchronization link connections, each link connection supported by an SDH multiplex section trail.  
The synchronization network types are: 
• 
Option I (Europe)  
• 
Option II (USA).   
You can define the timing quality level of the source, or work without quality level. The supported 
quality levels are according to the synchronization network type, as shown in the following tables. The 
quality levels are shown in order of highest quality level to lowest quality level. 
  Option I Quality Levels 
Quality 
Level 
Description 
Rank 
PRC 
Timing source is Primary Reference Clock as defined in Recommendation 
G.811 
Highest 
SSU-A 
Timing source is Type I or V Synchronization Supply Unit (SSU) clock as 
defined in Recommendation G.812 
 
SSU-B 
Timing source is Type VI Synchronization Supply Unit (SSU)clock as defined in 
Recommendation G.812 
 
SEC 
Timing source is Synchronous Equipment Clock as defined in 
Recommendation G.813 or G.8262, Option I 
 
DNU 
Do Not Use – This signal should not be used for synchronization 
Lowest 
  Option II Quality Levels 
Quality 
Level 
Description 
Rank 
PRS 
Timing source is Primary Reference Source clock as defined in 
Recommendation G.811 
Highest 
9. Timing and Synchronization 
Quality 
Level 
Description 
Rank 
STU 
Synchronization Traceability Unknown – Timing signal does not carry a 
quality level indication of the source 
 
ST2 
Timing source is Stratum 2 clock as defined in Recommendation G.812, Type 
II 
 
TNC 
Timing source is Transit Node Clock as defined in Recommendation G.812, 
Type V 
 
ST3E 
Timing source is Stratum 3E clock as defined in Recommendation G.812, 
Type III  
 
ST3 
Timing source is Stratum 3 clock as defined in Recommendation G.812, Type 
IV 
 
SMC 
Timing source is SONET/Ethernet self-timed clock as defined in 
Recommendation G.813 or G.8262, Option II 
 
ST4 
Timing source is Stratum 4 free-running clock (applicable only to 1.5 Mbit/s 
signals) 
 
PROV 
Provisionable by the network operator 
 
DUS 
Don't Use for Sync – This signal should not be used for synchronization 
Lowest 
System Timing Modes  
The Megaplex-4 timing subsystem can use the following types of reference sources: 
• 
Internal Megaplex-4 oscillator 
• 
Clock signal derived from the E1/T1 receive clock (Rx timing mode), SDH/SONET port, GbE port 
located on CL module, or pseudowire  
• 
Station clock, a special case of Rx timing, which uses an external clock signal supplied to the CL 
module CLOCK connector.  
Note 
Although GbE ports of M-ETH modules cannot serve as a reference source (Rx 
clock), they can distribute the clock transparently throughout the system. This 
feature requires a special ordering option (refer to M-ETH data sheet). 
The following table lists the reference clock sources that can be configured, together with the types of 
Megaplex-4 modules that can provide a timing reference signal.  
For each module, the table also lists the type of ports and, when applicable, the operating mode that 
must be selected for a port to provide a timing reference signal. 
9. Timing and Synchronization 
Clock Reference Sources  
Source Type 
Module Type 
Selectable Ports 
Specific Operating Mode 
Internal 
Not applicable 
Not applicable 
Not applicable 
Station (external) 
CL.2 
Station clock 
Not applicable 
RX Clock from  
Local User Port 
 
VS-16E1T1-EoP 
External E1 or T1 ports 
Not applicable 
VS-6/E1T1 
VS-16E1T1-PW  
External E1 or T1 ports 
Not applicable 
Pseudowire recovered 
clock 
 
VS-6/C37 
DS1 optical ports 
 
 
T3 
External T3 ports 
Internal T1 ports 
Not applicable 
CL modules without 
SDH/SONET ports 
Line (STM-1/OC-3/STM-4/OC-
12) Signal from SDH/SONET 
Subsystem  
CL.2  
Link port 
Not applicable 
Sync-E clock from GbE ports 
on CL modules  
CL.2  (HW Ver 1.0 and 
higher) 
GbE port 
Not applicable 
A timing source is defined by specifying the slot and the port to be used. The source slot can be any I/O 
slot with a module having ports capable of recovering a clock signal, or a CL slot.  
Internal Timing Mode 
In most Megaplex-4 applications, an external clock source is used. The internal oscillator is used as a last 
recourse timing source: it is automatically selected when no source is capable of providing a good timing 
reference.  
Rx Timing Mode  
In the Rx timing mode, the reference signal is derived from the receive (RX) clock of a specified user 
port, or a clock recovered from a user-specified pseudowire: 
• 
Megaplex-4 always permits locking the system (nodal) timing to a local user (that is, a user 
directly connected to a port of an I/O module installed in the chassis) from which a stable clock 
signal can be obtained. 
9. Timing and Synchronization 
• 
For Megaplex-4 equipped with VS-6/E1T1 or VS-16/E1T1/PW modules, it is also possible to 
configure certain pseudowires to provide recovered clock signals to serve as timing references. 
Any type of pseudowires, except HDLC, can provide recovered clock signals.  
The algorithm that selects the Megaplex-4 timing reference source is based on the user-defined 
priorities, and works to automatically select the operational port as the nodal timing reference: first 
according to the highest quality, and then according to the highest priority. If the quality level is not 
selected, Megaplex-4 selects the operational port with the highest available priority from the source list.  
If no operational port can be found in the source list, the Megaplex-4 switches to the holdover mode. In 
this mode, the timing subsystem selects the frequency used 26 msec before the fault condition that 
caused the switching to the next clock source mode (this is assumed to be a safe selection, at which the 
subsystem operated normally at the correct frequency). This frequency is maintained until one of the 
user-specified sources can again be selected as a reference. If time limit expires without any of the user-
specified clock sources returning to normal,  switches to the internal oscillator.  
Note 
When using GBEA/GBEAP CL.2 modules (without SDH/SONET), only a single 
clock source (from any port) can be configured per I/O module. 
Station Timing 
When the station timing mode is used as one of the clock sources, the Megaplex-4 system (nodal) timing 
is synchronized to an external clock signal delivered to the dedicated station clock interface located on 
each CL module. This signal is usually provided by a highly-accurate clock source, configured with the 
highest priority, which is often available in communication facilities (for example, a signal provided by a 
GPS-based timing source, an independent primary clock source, clock signals provided by an SDH/SONET 
ADM, or other suitable clock source). The clock signal frequency is user-selectable: 2.048 MHz, 
2048 Mbps, or 1.544 Mbps. 
The station clock quality can be set by the user. 
Each CL module can be connected to a separate station clock source, so that both station ports can 
serve as a clock source. 
The station clock has software-selectable interfaces: 
• 
ITU-T Rec. G.703 interface. The clock interface (balanced/unbalanced) and sensitivity (long or 
short range) are also user-selectable 
• 
RS-422 interface for squarewave signals, which is the recommended interface when timing 
quality is critical. Note that this interface is suitable for short cable runs, interconnecting 
equipment units located in close proximity. 
9. Timing and Synchronization 
The station clock interface also provides an output clock signal, for chaining applications. The source of the 
output clock is selectable:  
• 
The external clock signal applied to the station clock interface.  
• 
The external clock signal, after regeneration and filtering by a jitter attenuator 
When using the internal clock as the system timing reference, the transmitted SSM message is SEC (SDH) or 
SMC (SONET). 
Clock Domain  
Clock Mode 
The domain clock mode can be one of the following: 
• 
Auto mode – domain timing is determined by the clock selection algorithm (default) 
• 
Free-run mode – the domain clock is based on the main card local oscillator  
Note 
• Quality in free-run mode is SEC/SMC. 
• By default, Megaplex-4 uses free-run mode, until a valid clock source is selected. 
 
mp4100>config>system>clock>domain(1)# show status 
System Clock Source      : 2    State  : Locked    Quality  : PRC 
Force Switch        : Inactive                                     Manual Switch 
      : Inactive 
Clock Domain States 
Clock domain states indicate operation modes of the system clock (T0 timing generator). 
System clock: 
• 
Locked – Locked to selected clock source 
• 
Free-run – Locked to internal oscillator 
• 
Holdover – Input lock is lost, the clock mechanism uses data stored during normal operation for 
timing output. 
Note 
By default, the Megaplex-4 system clock is in free-run state, until a valid clock 
source is selected. 
9. Timing and Synchronization 
External Switch Commands 
You can issue manual or forced switch commands to choose a specific clock source. The manual 
command overrides the clock priority setting and allows selection of a clock with a priority lower than an 
automatically selected clock source. Both clock sources must have the same quality level. 
The forced switch command allows selection of any clock source, regardless of its priority or quality 
level. It overrides the previously issued manual switch command. 
The manual and forced switch commands are cleared using the clear command. 
Station/System Clock Squelch per Remote Domain Failure  
Megaplex-4 features station clock squelch with fault propagation over PWE between clock sources and 
station clock. This capability allows disabling the transmit (squelch) of the station clock when the central 
devices lose connectivity to the external clock source. 
Squelching is done according to the user configured QL minimum value, by comparing this user-
configured value to the reported quality level of the current selected synchronization source. 
You can set a minimum clock quality level for the Megaplex-4 station clock (quality min-level-station) 
and/or the system clock (quality min-level-system).  
To configure the quality of the sources to a higher value than the ‘quality min-level-station’/‘quality min-
level-system is under the user responsibility. 
If quality level of domain clock (selected source Quality level) is less than the configured ‘min-level-
system’ or no valid sources are defined, the following happens: 
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
If quality level of domain clock less than the configured ‘min-level-station’ or no valid sources are 
defined, the alarm ‘station_clock_ql_low’ is reported and station clock is squelched. 
9. Timing and Synchronization 
The WTR functionality is automatically derived from the configuration of each clock source. 
This configuration is performed per PW under config>pwe>pw(<pw-number>)# prompt (see 
Configuring Pseudowires in Chapter 8). 
Factory Defaults 
The table below lists the parameter defaults for the Clock Domain, Clock Source and Station Clock 
configuration. 
Parameter  
Default Value 
domain  
sync-network-type 
1 
quality 
sdh-sonet: ssm-based 
other ports, Type 1: dnu 
other ports, Type 2: dus 
mode 
auto 
clock-source 
priority 
10 
wait-to-restore 
300 (s) 
hold-off 
300 (ms) 
station 
 
tx-clock-source  
system  
interface-type  
e1, balanced 
rx-sensitivity  
short-haul  
line-code  
hdb3 
recovered 
network-type  
type-b 
9. Timing and Synchronization 
Configuring the Clock Domain  
 To configure the clock domain: 
3. Navigate to configure system clock domain 1. 
The config>system>clock>domain(1)# prompt is displayed. 
4. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting 
synchronization 
network type 
 
sync-network-type {1 | 2} 
Type 1 – Europe  
Type 2 – USA   
When you change the synchronization network type, 
you must redefine the clock sources. 
Setting minimum 
clock quality levels for 
the station and 
system clocks 
 
Network type 1 (Europe): 
quality [min-level-station | 
min-level -system <ql1>]  
Network type 2 (USA): quality 
[min -level-station | 
min-level -system <ql2>]  
no quality 
 
ql1 – quality level (according to network type 1 
Europe) 
Possible values: quality-level {prc | ssu-a | ssu-b | 
sec | dnu}  
Default: dnu 
ql2 – quality level (according to network type 2 USA) 
quality-level { prs | stu | st2 | tnc | st3e | st3 | smc 
| st4 | dus | prov } 
Default: dus 
The quality values are according to the 
synchronization network type defined for the 
domain.  
no quality removes the minimum quality parameter. 
If no minimum quality is defined for the domain, you 
cannot configure the quality level for the sources. A 
clock source with a quality level lower than the 
defined minimum quality is ignored by the clock 
selection mechanism. 
Setting clock mode 
mode {auto | free-run} 
auto –Clock selection mechanism functions normally, 
e.g. the best available clock source is selected for 
synchronization 
free-run – Internal oscillator is used for 
synchronization 
9. Timing and Synchronization 
Task 
Command 
Comments 
Forcing selection of a 
particular clock 
source when the 
sources have different 
quality levels 
force <source-id> 
The range of source-id is 1 to 10. 
Manually selecting a 
particular clock 
source  
manual <source-id> 
The selection is performed in the following 
conditions: 
• No quality is defined for the clock domain 
•  The sources have the same qualities 
• The sources have different priorities. 
Canceling previously 
issued force or 
manual command 
clear 
 
Adding clock source 
source <src-id> rx-port {e1 | t1 
| ds1-opt | sdh-sonet | 
ethernet } <slot><port> 
source <src-id> station 
<slot>/1 
source <src-id> recovered 
<recovered-id > 
Refer to Error! Reference source not found.. 
When using GBEA/GBEAP CL.2 modules (without 
SDH/SONET), only a single clock source (from any 
port) can be configured per I/O module. 
 
 
 
Configuring clock 
source  
source <src-id>  
Typing no source <src-id> deletes the source 
Refer to Error! Reference source not found. 
Example 
 
#Central device Megaplex-4 (device that distributes clock over the system): 
 
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
 
 
9. Timing and Synchronization 
#Remote device Megaplex-1 (any node that takes clock from Central device) 
 
configure pwe pw 13 
   source-clock-fail remote-domain-down  
exit all 
 
configure system clock domain 1 
sync-network-type 1 
      quality min-level-station prc  
      source 1 pw 13 
            priority 1 
exit all 
Displaying the Clock Domain Status  
 To view the clock domain status: 
• 
At the system>clock>domain(1)#, enter show status. 
The clock source status is displayed.   
The last row displays the clock deviation in PPM for 622GbEa or GbEa CL.2 modules (not applicable for 
DS0 module). 
Example 1: Megaplex-4 domain is locked to Source 2, with PRC quality. 
mp4100>config>system>clock>domain(1)# show status 
System Clock Source      : 2    State  : Locked    Quality  : PRC 
Force Switch             : Inactive                                      
Manual Switch            : Inactive  
TO offset <PPM>          : -37.0                                     
Example 2: The nodal timing system entered the holdover state after all the configured sources failed.  
mp4100>config>system>clock>domain(1)# show status 
System Clock Source : 0    State  : Holdover    Quality  : SEC 
Force Switch        : Inactive                                     
Manual Switch       : Inactive  
TO offset <PPM>     : -37.0  
 
Example 3: Clock Domain Mode is configured to “free-run” and no clock selection is performed.  
mp4100>config>system>clock>domain(1)# show status 
System Clock Source : 0    State  : Freerun     Quality  : SEC 
Force Switch        : Inactive                                      
Manual Switch       : Inactive        
TO offset <PPM>     : -37.0 
9. Timing and Synchronization 
Example 4: Clock Domain Mode is configured to “free-run” and no clock selection is performed. The CL 
module is DS0. 
mp4100>config>system>clock>domain(1)# show status 
System Clock Source : 0    State  : Freerun     Quality  : SEC 
Force Switch        : Inactive                                      
Manual Switch       : Inactive        
TO offset <PPM>     : N/A 
The possible clock states are explained in the following table. 
Parameter Displayed 
Description 
Free Run  
Indicates that the nodal timing system is locked to the internal oscillator  
Note: When using the internal clock as the system timing reference, the transmitted 
SSM message is SEC (SDH) or SMC (SONET).  
Holdover 
 
Indicates whether the nodal timing system is in the holdover state (yes) or not (no).   
The nodal timing system enters the holdover state when all the configured sources fail. 
In the holdover mode, the clock maintains the incoming reference frequency at the last 
value acquired before the failure. This situation persists until at least one of the 
configured sources returns to normal operation, and thus is selected again as reference.  
Note 1: This field is not relevant for “DS0 only” CL option. In this case after clock source 
failure, the next available clock source is selected. If no valid clock source is available, 
the Megaplex internal clock is used as a clock source.  
 Note 2: The transmitted quality level is SEC (SDH) or SMC (SONET). 
Locked 
Indicates that the nodal timing is locked on one of the clock references. 
 
Configuring the Clock Sources  
You can define up to 5/10 clock sources for the domain (10 sources for /DS0 and /155 assemblies, 5 
sources for GBEA assemblies). 
. The sources can be:  
• 
GbE port on CL module  
• 
SDH/SONET port  
• 
Station clock 
• 
E1/T1 ports on I/O modules 
• 
Recovered clock from a PW. 
9. Timing and Synchronization 
 To add a clock source:  
1. Verify that the clock source to be used as an input is valid. 
Note 
You can choose an invalid clock source. However, this input will be rejected by 
the domain during the clock selection process 
2. Verify that the card whose port will be used as a source clock is provisioned. 
3. Verify that the port to be used as a source clock is enabled (no shutdown). 
4. Navigate to configure system clock domain 1. 
The config>system>clock>domain(1)# prompt is displayed. 
5. Type one of the following, according to the required clock source: 
source <src-id> rx-port ethernet <slot>/<port> 
source <src-id> rx-port e1 <slot>/<port> 
source <src-id> rx-port t1 <slot>/<port> 
source <src-id> rx-port sdh-sonet <slot>/<port> 
source <src-id> rx-port ds1-opt <slot>/<port>  
source <src-id> station <slot>/1 
source <src-id> recovered <recovered-id>  
no source   
Note 
Recovered ID range is 1 to 99 
 
Note 
For Ethernet clock source, to ensure correct distribution of ESMC traffic, you 
must configure a flow with an L2CP profile with peer action on the 01-80-c2-
00-00-02 address. The flow must have the following attributes: 
• 
Untagged classification 
• 
Ingress port – Ethernet port/LAG, serving as the ESMC source (Sync-E port) 
• 
Egress port – according to application requirements. 
If you use the flow only to peer the SSM frames and do not need to forward 
the untagged traffic, discard it, using the drop command on the flow. 
 
Note 
All fractional E1/T1 ports should be locked on a single system clock, 
transparent clocking can be achieved by using unframed E1/T1’s over 
SDH/SONET and for some cases over PW. 
 
9. Timing and Synchronization 
The clock source is created and the config>system>clock>domain(1)>source(<1–10>)# prompt 
is displayed.  
6. Enter all necessary commands according to the tasks listed below the following procedure. 
 To configure a clock source for which the port has been defined: 
1. Navigate to configure system clock domain 1. 
The config>system>clock>domain(1)# prompt is displayed. 
2. Type source <1–10> to select the source to configure. 
The config>system>clock>domain(1)>source(<1–10>)# prompt is displayed. 
3. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting priority 
 
priority <1–10> 
Priority 1 is the highest.  
Setting quality level 
 
For Type 1: quality-level 
{prc | ssu-a | ssu-b | sec | 
dnu | ssm-based} 
For Type 2: quality-level { 
prs | stu | st2 | tnc | st3e | 
st3 | smc | st4 | dus | 
ssm-based | prov } 
 If no quality is defined for the domain, this 
command is not available  
The quality level ssm-based indicates that the 
quality level is based on SSM messages and is not 
available on DS0 only CL.2 modules  
Using no quality cancels the quality hierarchy and 
the clock becomes priority-based only 
Defining the time that a 
previously failed 
synchronization source must 
be fault-free in order to be 
considered available  
wait-to-restore <0–720> 
The time is defined in seconds. 
Defining the time  that signal 
failure must be active before 
it is transmitted  
hold-off <300–1800> 
The time is defined in milliseconds. 
Canceling the wait-to-restore 
timer of a clock source 
clear-wait-to-restore 
This option is useful if a timing source fault is 
cleared and you want to souce to be immediately 
available.   
9. Timing and Synchronization 
Displaying the Clock Source Status 
 To view the clock source status: 
• 
At the system>clock> domain(1)>source(<1–10>)#, enter show status. 
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
 
ESMC Fail – Ethernet port with ESMC-based clock has not received a SSM-packet stream 
for 5 seconds. Make sure the Ethernet port has been configured to supply ESMC and a 
dedicated flow has been directed to the port. 
 
Tx quality – Transmit clock quality 
 
Rx quality – Receive clock quality 
 
ESMC State – State of the Ethernet Synchronization Messaging Channel (ESMC) 
 
WTR State – Wait-to-restore counter status 
 
Running – WTR Timer is running (when the clock source returns after signal failure (SF), 
WTR timer is used to verify that the clock source stable state is not intermittent) 
 
Inactive – WTR Timer is inactive (clock source status is OK). 
Displaying Clock Source Statistics  
You can display the Ethernet Synchronization Messaging Channel (ESMC) statistics for the clock sources. 
ESMC is used as a transport layer for SSMs in Sync-E. The ESMC statistic counters are available for CL 
GbE ports only.  
9. Timing and Synchronization 
 To display the ESMC statistics for a clock source: 
1. Navigate to configure system clock domain 1 source <src-id>. 
The following prompt is displayed: config>system>clock>domain(1)>source(<src-id>)#. 
2. Enter show statistics. 
The ESMC statistics are displayed. 
mp4100>config>system>clock>domain(1)>source(1)#  
mp4100>config>system>clock>domain(1)>source(1)# show statistics 
ESMC Failure Counter : 1 
                       Rx         Tx 
ESMC Events          : 0          1 
ESMC Information     : 0          29 
 
ESMC Events – Number of changed quality level messages sent and received 
 
ESMC Information – Number of quality level information messages sent and received. 
Configuring the Station Clock 
The station clock is an E1/2MHz or T1/1.5MHz port that can be used for synchronization. You can set the 
station clock timing to be based on the system clock or recovered from the received signal of the station 
clock (with or without jitter attenuator). 
 To configure the station clock:  
1. Navigate to configure system clock station <slot>/1 (<slot> is cl-a or cl-b). 
The config>system>clock>station(<slot>/1)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Selecting the source of the 
clock output signal  provided 
in the station clock 
connector, for connection to 
other equipment 
tx-clock-source {system | station-
rclk-plus-ja} 
 
system – The output (transmit) clock is 
derived from the Megaplex-4 nodal 
timing  
station rclk after ja – The external clock 
signal applied to the station clock receive 
input is regenerated and filtered by a 
jitter attenuator, before being returned 
through the transmit output 
9. Timing and Synchronization 
Task 
Command 
Comments 
Selecting the rate and type of 
signal accepted and 
transmitted via the station 
clock port  
 
interface-type {e1 | 2mhz  | t1}  
 
 
e1 – 2.048 Mbps signal per ITU-T Rec. 
G.703 Para. 9 
2mhz – 2.048 MHz signal per ITU-T Rec. 
G.703 Para. 13 
t1 –1.544 Mbps signal per ITU-T Rec. 
G.703 Para. 5.  
Selecting the impedance of 
signal accepted and 
transmitted via the station 
clock port  
impedance {balanced | unbalanced} 
For e1 and 2mhz options only. If you 
specify e1 or 2mhz and do not specify 
balanced or unbalanced, by default the 
interface is set as balanced 
Setting line code 
 
line-code {b8zs | ami | hdb3} 
hdb3 –High Density Bipolar coding of 
order 3, used for e1 and 2mhz options 
ami –Alternate Mark Inversion coding, 
used for t1 and 1.5mhz options 
b8zs – Binary-8 zero suppression coding, 
used for t1 and 1.5mhz options 
Specifying E1 framing mode  
line-type { g732n | g732n-crc | 
unframed} 
This command is not available when 
CL.2  type is DS0 (ignore an AIS alarm 
that appears in the remote equipment).  
Specifying T1 framing mode  
line-type { sf | esf| unframed} 
 
This command is not available when 
CL.2  type is DS0 (ignore an AIS alarm 
that appears in the remote equipment). 
Setting receiver sensitivity to 
adjust the signal capability to 
reach destinations close by or 
farther away 
rx-sensitivity {short-haul | 
long-haul} 
short-haul – maximum allowable 
attenuation of 10 dB, relative to the 
nominal transmit level 
long-haul – maximum allowable 
attenuation of 34 dB, relative to the 
nominal transmit level  
Enabling SSM transmission 
tx-ssm 
Using no tx-ssm disables SSM 
transmission 
This command is not available when 
CL.2  type is DS0 
Specifying bits in TS0 for 
transfering clock quality via 
SSM (E1 only) 
ssm-channel  { sa4 | sa5 | sa6 | sa7 
| sa8 }  
This command is not available when 
CL.2  type is DS0 
Administratively enabling 
station clock 
no shutdown 
Using shutdown disables the station 
clock 
9. Timing and Synchronization 
Displaying the Station Clock Status  
 To view the station clock status: 
• 
At the system>clock>station (<slot>/<1>)# prompt, enter show status. 
The station clock status is displayed. 
mp4100>config>system>clock>station(cl-a/1)# show status 
Name                  : CL-A station 01 
Administrative Status : Down 
Operational Status    : Down 
Configuring the Recovered Clock  
Pseudowires of all types, except HDLCoPSN, can be selected as timing sources for the Megaplex-4 nodal 
timing subsystem. This timing mode is called adaptive clock recovery and is supported by VS-16E1T1-PW 
and VS-6/E1T1 modules.   
 To configure the recovered clock:  
1. Navigate to configure system clock recovered <ID 1..99>. 
The config>system>clock>recovered (<ID>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Associating the PW number 
to recovered clock   
pw <PW number> 
 
The possible PW number range is 1 to 640. 
Specifies the type of packet 
switched network used to 
transport the pseudowire  
 
network-type {type-a | type-b}  
  
type-a – Switch-based network, for example, 
an MPLS/ETH network 
type-b – Router-based network, for example, 
an UDP/IP network 
Administratively enabling 
recovered clock 
no shutdown 
Using shutdown disables the recovered clock 
Displaying the Recovered Clock Status  
You can display the recovered clock status and the current status of the pseudowire adaptive clock 
recovery mechanism. 
9. Timing and Synchronization 
 To view the recovered clock status and pseudowire adaptive clock recovery mechanism state:  
• 
At the system>clock>recovered (<PW number)# prompt, enter show status. 
The recovered clock status is displayed. 
mp4100>config>system>clock>recovered(1)# show status 
Clock State : Frequency Acquisition 
The possible clock states are explained in the following table. 
Parameter Displayed 
Description 
Holdover 
 
Indicates whether the nodal timing subsystem is in the holdover state (yes) or not (no).   
The nodal timing system enters the holdover state when all the configured sources fail 
or during clock switching. In the holdover mode, the clock maintains the incoming 
reference frequency at the last value acquired before the failure. This situation persists 
until at least one of the configured sources returns to normal operation, and thus is 
selected again as reference.  
Note 1: This field is not relevant for “DS0 only” CL option.  
Note 2: The transmitted quality level is SEC (SDH) or SMC (SONET). 
Frequency 
Acquisition 
Indicates that the clock recovery mechanism is learning the frequency of the selected 
reference. 
Rapid Phase Lock 
Indicates that the clock recovery mechanism is in the training process 
Fine Phase Lock 
 
Indicates that the clock recovery mechanism successfully completed the training 
process, and is now locked. At this stage, the clock recovery mechanism provides a 
stable clock of good quality. 
Not Applicable 
The adaptive clock recovery status is not relevant. 
You can also display the number of the PW the recovered clock is locked to, and the network type by 
means of the following command. 
 To display the network type and the PW number:  
mp4100>config>system>clock>recovered(1)# info detail 
    pw  1 
    network-type  type-b 
    no shutdown 
Configuration Errors 
The following table lists messages generated by Megaplex-4 when a configuration error is detected. 

## 9.1 Date and Time (Manual)  *(p.796)*

9. Timing and Synchronization 
Clock Sanity Messages  
Code 
Type 
Syntax 
Meaning 
110 
 
Error 
ILLEGAL CLOCK SOURCE  
The selected clock source is invalid for one of the following 
reasons: 
• The configured module port cannot supply a reference 
clock 
• For CL module with SDH/SONET ports: the T1 ports of 
the T3 module can’t serve as clock source if they are 
cross-connected to E1-i/T1-i ports of the CL module.  
112 
Error 
CLOCK SOURCE IS IN 
SHUTDOWN STATE  
When configuring the clock source to be locked to the 
receive clock of a module/channel, the source 
module/channel must be connected 
115 
Error 
RECOVERED CLOCK - PW DOES 
NOT EXIST 
You are trying to configure a recovered clock source but the 
PW associated to it does not exist. 
116 
Error 
DOMAIN NET TYPE DOES NOT 
MATCH 
SDH/SONET         
Domain network type 1 and 2 must match sdh and sonet 
frame-type, respectively.  
9.1 Date and Time (Manual) 
You can set the date and time for the Megaplex-4 internal real-time clock.  
Note 
The internal real-time clock is used to time-stamp various messages, alarms, 
etc. The previously attached time stamps are not changed when the time-of-
day is changed as a result of updates. 
Setting the Date and Time  
 To specify the system date and time: 
1. At the config>system# prompt, enter date-and-time. 
The config>system>date-time# prompt appears. 
2. Specify the date and time and associated parameters as illustrated and explained below. 
9. Timing and Synchronization 
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
dd-mm-yyyy – European format 
mm-dd-yyyy – US format 
yyyy-dd-mm – Japanese format 
dd stands for day, mm for 
month and yyyy for year  
Specifying the system time 
time <hh:mm[:ss]> 
Seconds are optional. 
It is recommended to set the 
time about one minute beyond 
the desired time, and then save 
at the correct instant. 
Example 
 To define dd-mm-yyyy as a date format: 
mp4100>config>system>date-and-time# date-format dd-mm-yyyy 
 To define January 2, 2011 as the  date: 
mp4100>config>system>date-and-time# date 02-01-2011 
 To define 18:23 as the  time: 
mp4100>config>system>date-and-time# time 18:23 
Displaying the Date and Time 
 To view the date and time settings: 
• 
At the config>system# prompt, enter show date-and-time. 
The date, time and the time zone are displayed. 
config>system# show date-and-time UTC +00:00 
2018-03-04   19:52:23    

## 9.2 Date and Time (from NTP Server)  *(p.798)*

9. Timing and Synchronization 
9.2 Date and Time (from NTP Server) 
This section explains how to receive the clock signal from NTP servers in the network.  Megaplex-4 can 
synchronize with up to ten servers, sending NTP requests to the servers at user-defined intervals. 
You can set one of the active SNTP servers as the preferred server, so that Megaplex-4 sends NTP 
requests to the preferred server. If there is no preferred server or if the preferred server does not 
answer, then Megaplex-4 sends NTP requests to any enabled servers. 
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
Task 
Command 
Comments 
Enabling Megaplex-4 to listen to 
NTP broadcast messages to 
obtain accurate timestamps 
broadcast 
Type no broadcast to disable 
broadcast mode 
Setting polling interval (in 
minutes) for SNTP requests 
poll-interval interval <minutes>         
      
Allowed range is 1–1440 
9. Timing and Synchronization 
Task 
Command 
Comments 
Defining and configuring SNTP 
servers (see Error! Reference 
source not found. and Error! 
Reference source not found.)  
server <server-id> 
 
 
 
Displaying SNTP status 
show status 
 
Defining SNTP Servers  
 To define an SNTP server: 
1. Navigate to config system date-and-time sntp. 
The config>system>date-time>sntp# prompt is displayed. 
2. Type server <server-id> to define an SNTP server with ID <server-id>. 
The following prompt is displayed: config>system>date-time>sntp>server(<server-id>)$. The 
SNTP server parameters are configured by default as described in Error! Reference source not 
found.. 
3. Configure the SNTP server parameters as needed, as described in Error! Reference source not 
found.. 
Configuring SNTP Server Parameters 
 To configure SNTP server parameters: 
1. Navigate to config system date-and-time sntp. 
The config>system>date-time>sntp# prompt is displayed. 
2. Type server <server-id> to select the SNTP server to configure. 
The following prompt is displayed: config>system>date-time>sntp>server(<server-id>)# 
3. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Setting the IP address of the 
server 
address <IP-address> 
 
9. Timing and Synchronization 
Task 
Command 
Comments 
Set SNTP server as preferred 
server. 
prefer 
 
Type no prefer to remove 
preference 
Note: Only one server can be 
preferred. 
Setting UDP port for NTP 
requests, to a specific UDP port or 
to default UDP port (123) 
udp port <udp-port> 
udp default 
Allowed range is 1–65535 
Administratively enabling server 
no shutdown 
Using shutdown disables the 
server 
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
mp4100# configure system date-and-time sntp 
mp4100>config>system>date-time>sntp# server 1 
mp4100>config>system>date-time>sntp>server(1)# address 172.17.155.226 
mp4100>config>system>date-time>sntp>server(1)# no shutdown 
mp4100>config>system>date-time>sntp>server(1)# commit 
Result : OK 
 To display server information: 
mp4100>config>system>date-time>sntp>server(1)$ query-server 
 
Query Server Reply 
-------------------------------------------------------------- 
Server  : 172.17.155.226  UDP        : 123 
Date    : 11-04-2013      Time(UTC)  : 07:13:54 
Stratum : 4 
mp4100>config>system>date-time>sntp>server(1)# exit 
mp4100>config>system>date-time>sntp# show status 
 
System Uptime       : 000 Days 02:24:59 
System Time (Local) : 2013-04-11                               07:18:07 
 
9. Timing and Synchronization 
Current Source : 172.17.155.226 
 
NTP Server       UDP Port     Tstamp DateTime        Stratum Received 
--------------------------------------------------------------------------- 
172.17.155.226 Enable 123     11-04-2013 07:14:00  4     000Days00:04:07 
 