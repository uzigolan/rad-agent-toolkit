# TP Distance Teleprotection Module

<!-- datasheet product=tp family=mp4100 kind=card source=tp_ds.pdf -->

*Datasheet `tp_ds.pdf`, 3 pages. Product `tp`, family `mp4100` (card).

## Megaplex-4  *(p.1)*

TP

## Distance Teleprotection Module  *(p.1)*

- Four inputs with soft-selectable or fixed DC voltage and eight outputs, galvanically
isolated with high EMC immunity for harsh environments
- Ultralow end-to-end propagation delay for commands and automation
- 1+1 path protection with less than 10 msec recovery time
- Built-in pseudowire engine
- Unidirectional broadcast for Automation commands
- T-line support
- Selected options certified for IEEE 1613
The TP module offers ultralow end-to-end
propagation delay for immediate delivery
of teleprotection commands and
automation, from protective relay/contact
transfer to remote-end substations.
Megaplex-4 with its TP modules delivers
teleprotection commands and automation
with mission critical accuracy over
dedicated fiber, TDM or PSN, to help
central control better manage the power
grid load and to protect termination and
transformation equipment from severe
damages resulting from faulty
high-voltage lines.
The TP module supports up to 4
command/automation inputs and 8
outputs, enabling teleprotection
equipment to utilize the advanced
transport capabilities offered by Megaplex.
Teleprotection commands can be locally
output or be carried to a peer card/
Megaplex unit over TDM/SDH or packet
switch network. Up to 4 commands can be
carried over a single DS0.
The teleprotection commands and
automation are triggered by the following
options of the input signal to the TP
module:
-
110 VDC
-
220 VDC
-
Soft-selectable nominal input control
voltage, selectable per port: ±24, ±48,
±110, ±125, ±220 or ±250 VDC.
The module is also used for the
automation processes by exchange of
data between the relay protection devices
and the control center, thus allowing for
uninterruptable power supply throughout
the grid when fault occurs.
T-Line application allows broadcast of a
trip event to several nodes via drop and
insert on Trip level.
Megaplex’s advanced carrier Ethernet and
pseudowire capabilities guarantee the
performance levels required when
migrating to packet networks with hard
QoS, as well as robust latency and jitter
protection.
Substation
Substation
Relay
SDH/SONET
PSN
Dark Fiber
Megaplex
Megaplex
Relay
E1/T1, STM-1/STM-4, ETH, C37.94
E1/T1, STM-1/STM-4, ETH, C37.94
TP
The module operates in conjunction with
other Megaplex modules catering for a
variety of interfaces, such as voice, high
speed, low speed and others, to provide
any possible service needed in a
substation.
PSEUDOWIRE
A powerful pseudowire engine saves the
need of two additional MPW-1 modules
and can act as a server card to other I/O
modules. The engine provides up to 4
protected PWs per module with up to 32
timeslots per each PW port.
Note: In cases involving adaptive clock recovery and
high differential delays, an MPW-1 module is
required.

## Specifications  *(p.2)*

TELEPROTECTION INTERFACES
Compliance
IEC 60834-1
Input
Connector: Terminal block, 8-pin
Number of command inputs: 4
Nominal input control voltage:
-
± 110 VDC
-
± 220 VDC
-
Soft-selectable: ±24, ±48, ±110, ±125,
±220 or ±250 VDC
Configurable Debounce for noise filtering
Output
Connectors: 2 terminal blocks, 8-pins each
Total number of outputs: 8 (4 primary + 4
secondary):
-
For each secondary output one
primary command can be selected.
-
More than one secondary output can
be bound to one primary command
Independent Rx/Tx processing
Switching: up to 250 VDC, 0.25A on
inductive load
Wire diameter: up to 2.5 sq. mm
Command-configurable prolongation time
Optimization
Security- or speed-optimized according to
application
Isolation
2500 VRMS between protection circuits
and chassis
Table 1.  Teleprotection Indicators
Indicator
Quantity per
Module
Color
Function
CMD CHANNEL
4 (2 per port)
Red/green
Green On: Port synchronized
Red On: RAI/LOF/Add mismatch
Red Blinking: CRC Errors
Off: Shutdown
CMD IN
Red/green
Green: No alarms
Red On: Alarm state
Off: Shutdown
CMD OUT
Red/green
Green: Steady State
Red On: Alarm State
Off: Shutdown
ALM
Red
Red Blinking: Events detected
Off: No events
24 Raoul Wallenberg Street
Tel Aviv 69719, Israel
Tel. 972-3-6458181
Fax 972-3-6498250, 6474436
E-mail market@rad.com
900 Corporate Drive
Mahwah, NJ 07430, USA
Tel. 201-5291100
Toll free 1-800-4447234
Fax 201-5295777
E-mail market@radusa.com
Order this publication by Catalog No. 805014
464-104-09/15  Specifications are subject to change without prior notice.  1988–2015 RAD Data Communications Ltd. RAD products/technologies are protected by registered patents. To review specifically which
product is covered by which patent, please see ipr.rad.com. The RAD name, logo, logotype, and the product names MiNID, Optimux, Airmux, and IPmux, are registered trademarks of RAD Data Communications Ltd. All
other trademarks are the property of their respective holders.
TP
Table 1. Typical Ranges over 2W@26 AWG Cable
Data Rate
[kbps]
Ranges
[km]                [mi]
6.6
4.1
1536
4.9
3.0
2048
4.5
2.8
4096
3.2
2.0
4608
3.0
1.9
5696
2.6
1.6
15296
0.70
0.43
Notes:The SHDSL data rate depends on the distance, number
of wires and far-end device.
The typical ranges are based on error-free lab tests without
noise and obtained on a 26 AWG cable line simulator
(DLS-6100, DLS-6300).
PSEUDOWIRE
Standard Compliance
IETF: RFC 5086 (CESoPSN)
MFA Forum: IA 8.0.0
MEF 8
Packet Switched Network Types
UDP over IP
MEF-8 Ethernet
Number of PW Connections
Up to 640 pseudowires per chassis
Up to 8 pseudowires (4 working +
4 protection) per module
Jitter Buffer Size
250 µsec to 8000 µsec, in 1-µsec steps
(the value entered by the user is rounded
upward to the closest n*125 µsec value).
RESILIENCY
Protection
Equipment protection
On-board CMD Channel protection
Megaplex TDM traffic protection
Protection Recovery
Less than 10 msec
MONITORING AND DIAGNOSTICS
Local loopback per command
Remote loopback per command
End-to-end delay measurements
Events time stamping with 1 msec
accuracy
Accepting GPS time via IEC-60870-5-104
or SNTP
GENERAL
Indicators
See Table 1
Environment
Operating temperature:
-
Regular: -10°C to 55°C (14°F to 131°F)
-
IEEE-1613 certified options: -20°C to
55°C (-4°F to 131°F)
Storage temperature: -20°C to +70°C
(-4°F to +158°F)
Humidity: up to 95%, non-condensing
Power Consumption
6.5W max

## Ordering  *(p.3)*

RECOMMENDED CONFIGURATIONS
MP-4100M-TP/110/EMR
Teleprotection module with ± 110 VDC
input control voltage and electro-
mechanical relay
MP-4100M-TP/220/EMR
Teleprotection module with ± 220 VDC
input control voltage and electro-
mechanical relay
MP-4100M-TP/CV/EMR
Teleprotection module with
soft-selectable input control voltage and
electro-mechanical relay
SPECIAL CONFIGURATIONS
Please contact your local RAD partner for
additional configuration options.