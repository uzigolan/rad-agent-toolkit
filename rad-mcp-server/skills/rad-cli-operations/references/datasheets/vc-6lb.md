# VC-6/LB 6-Channel PCM Voice Modules for Local Battery Telephones

<!-- datasheet product=vc-6lb family=- kind=card source=vc-6lb_ds.pdf -->

*Datasheet `vc-6lb_ds.pdf`, 2 pages. Product `vc-6lb`, no inventory family (card).
*Note: Megaplex-2100/2104 module only — NOT a Megaplex-4 card; no mp2100 family exists*

## Megaplex-2100/2104  *(p.1)*

VC-6/LB

## 6-Channel PCM Voice Modules for Local Battery Telephones  *(p.1)*

- Six analog voice channels for connection to 2-wire Local Battery (LB) field telephones
- Toll-quality 64 kbps PCM encoding
- Optional inband signaling with A-law encoded channels
VC-6/LB modules are user-programmable
voice interface modules for connecting
Megaplex-2100/2104 to 2-wire local
battery-powered (LB) telephones. Each
module provides six voice channels using
toll-quality 64 kbps PCM voice encoding in
compliance with ITU-T Rec. G.711 and
AT&T Pub. 43801.
The modules connect between LB military
field telephones at different remote
locations, in a point-to-point topology.
Each LB telephone is connected to one
module channel. The module digitizes the
connected LB telephone’s analog voice
signal and transfers it over a timeslot
assigned for the channel on the Megaplex
E1/T1 link. At the receiving LB telephone
side, the digital signal is converted back to
an analog signal by the remote VC-6/LB
module.
Encoding and decoding are in full
compliance with ITU-T requirements
G.712, G.713 and G.714. Voice channel
companding is user-selectable for A-law or
µ-law operation.
Each PCM voice channel is allocated a
timeslot on the E1/T1 link in a DS0
compatible format, permitting voice
channel switching in systems based on
digital cross-connect (DACS).
In the basic point-to-point application, LB
telephones at one site are connected to
LB telephones at another location via the
E1/T1 link between the Megaplex units
(see Figure 1). The main advantage here is
that all local/remote pairs of LB
telephones communicate via the single
Megaplex link, rather than via separate
lines.
Three user-selectable signaling transfer
modes are available:
-
Channel Associated Signaling (CAS)
transmitted in Timeslot 16, compatible
with ITU-T Rec. G.704 (available for E1
links only);
-
Inband “Robbed Bit Multiframe”
(RBMF) signaling transfer, compatible
with ITU-T Rec. G.704 and AT&T
Pub. 43801 (available for T1 links
only);
-
Proprietary “Robbed Bit Frame” (RBF)
signaling, which avoids the need for
multiframe synchronization. RBF
allocates the least significant bit of
each channel to its own signaling
information. This proprietary method
allows a Megaplex system to transmit
31 voice channels on each E1 link,
when using G.732N framing.
E1/T1
Megaplex-2100/2104
Megaplex-2100/2104
VC-6/LB
VC-6/LB
LB
Telephone
LB
Telephone
Figure 1.  Point-to-Point LB Telephone Connection
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
Order this publication by Catalog No. 803257
764-136-06/14  Specifications are subject to change without prior notice.  1988–2014 RAD Data Communications Ltd. The RAD name, logo, logotype, and the terms EtherAccess, TDMoIP and TDMoIP Driven, and
the product names Optimux and IPmux, are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.
VC-6/LB

## 6-Channel PCM Voice Modules for Local Battery Telephones  *(p.2)*

Although LB telephones provide their own
operating voltage, the VC-6/LB modules
require a -48 VDC (nominal) source in
order to generate the voltage for ringing
the connected LB telephone. The -48 VDC
is supplied to the module internally via the
Megaplex chassis voltage distribution bus.
This power can be provided either from
the DC-powered chassis, from external
Ringer-2000 or Ringer-2200N power
supply units or Ringer-2100R module for
AC-powered chassis (see separate data
sheet for information on Ringers).
Gain control is soft-adjustable for both
the receive and transmit direction,
enabling easy installation in all
environments.
All operating parameters are configurable
via the management system for both the
local and remote modules.
Diagnostic features include loopbacks
towards the local user equipment and
towards the remote user equipment. Test
tone injection of 1 kHz, 0 dBm0 towards
the remote equipment is also available.
Additionally, LED channel activity
indicators are provided on the module
panel.

## Specifications  *(p.2)*

Number of Voice Channels
Voice Digitizing Technique
Modulation: PCM per ITU-T G.711 and
AT&T PUB-43801
Companding: µ-law or A-law
Bandwidth Requirement
64 kbps (one timeslot) per enabled
channel
Analog Interface
Line type: 2-wire
ITU-T standards: G.713
Analog Parameters
Nominal level: 0 dBm
Nominal impedance:  600Ω
Return loss (ERL) at 300 to 3400 Hz:
better than 20 dB
Frequency response (Ref:1020 Hz):
-
±0.5 dB at 300 to 3000 Hz
-
±1.1 dB at 250 to 3400 Hz
Level adjustment (soft-selectable):
-
TX: +8 to -17 dBm
-
RX: +2 to -23 dBm
-
Steps: 0.5 dB (±0.15 dB), nominal
Signal to total distortion (G.713
Method 2):
-
-30 to 0 dBm0: better than 33dB
-
-45 to +3 dBm0: better than 22dB
Idle channel noise:
better than -65 dBm0 (+25 dBrnc)
Transformer isolation: 1500 VRMS
Ringer
Required DC input: -36 VDC to -72 VDC
Ring signal output: 86 VRMS (when
providing 4 REN or less) to 45 VRMS
(when providing 12 REN max), 20 Hz
(±10%),
2-second signal duration
Overload protected
End-to-End Signaling
T1 Links:
-
Robbed Bit Multiframe signaling:
-
667 samples per second with D4;
333 samples per second with ESF
-
Robbed Bit Frame (proprietary)
signaling: 8000 samples per second
E1 Links:
-
Channel Associated Signaling
per ITU-T G.704 para. 3.3.3.2
-
Robbed Bit Frame (proprietary)
signaling: 8000 samples per sec
Diagnostics
-
Local digital loopback for each channel,
towards the local user equipment
-
Remote analog loopback for each
channel, towards the remote user
equipment
-
1 kHz, 0 dBm0 test tone injection for
one channel at a time, towards the
remote user equipment
-
Self-test for entire system upon power
up
Indicators (per channel)
Remote Off-Hook
Local Off-Hook
Connectors (per channel)
6-pin RJ-11
Configuration
Programmable via the Megaplex
management system
Power Consumption
3.5W

## Ordering  *(p.2)*

RECOMMENDED CONFIGURATIONS
MP-2100M-VC-6/LB
6-Channel PCM Voice Module for Local
Battery Telephones for MP-2100/2104
OPTIONAL ACCESSORIES
The modules in an AC-powered MP-2100
chassis may require a -48 VDC (nominal)
source for feed and ring voltages. This
power can be provided by a
Ringer-2000/2200N unit or Ringer-2100R
module (see Ringer data sheet for
ordering). -48 VDC-powered chassis, or
AC-powered MP-2104 chassis with built-in
ringer option, do not require an additional
Ringer.