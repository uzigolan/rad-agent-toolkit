# VC-4-OMNI 4-Channel PCM Voice Module

<!-- datasheet product=vc-4-omni family=mp4100 kind=card source=vc-4-omni_ds_0.pdf -->

*Datasheet `vc-4-omni_ds_0.pdf`, 4 pages. Product `vc-4-omni`, family `mp4100` (card).
*Note: also fits Megaplex-2100/2104 I/O slots*

## (overview)  *(p.1)*

- Four analog voice channels employing toll-quality 64-kbps PCM encoding
- Daisy chain of 5-way digital conference calls, per channel
- Voice band modems for polling application in point-to-multipoint mode
- Point-to-point and point-to-multipoint channel operating modes
- For any I/O slot of Megaplex-2100, Megaplex-2104 or Megaplex-4100

## Megaplex Module VC-4/OMNI PCM Omnibus Voice Module “Omnibus” protocol enables simultaneous communication with multiple remote stations  *(p.1)*

The VC-4/OMNI module provides four
toll-quality voice channels to enable
“omnibus” applications where each site
communicates with multiple remote
stations simultaneously (such as
broadcasting an important message).
Voice signals are digitized using PCM, in
compliance with ITU-T G.711 standards.
Encoding and decoding are in full
compliance with ITU-T requirements
G.712, G.713 and G.714. Voice channel
companding is selectable for A-law or
μ-law.
VC-4/OMNI accesses any of the Megaplex
internal TDM buses so that, when
operating with two, three or four different
E1 or T1 links (trunks), a channel can be
transmitted simultaneously to all of them.
This enables establishing up to 5-way
conference calls per channel.
A conference call is established between
the local party connected to the
VC-4/OMNI channel (external port) and the
remote parties, connected to up to four
timeslots (internal ports) assigned to this
external port (see Figure 2). All
conferencing parties can speak to and
hear each other. A single VC-4/OMNI
module supports up to four independent
conference calls simultaneously.

## VC-4/OMNI  *(p.2)*

VC-4/OMNI modules, together with the
E1/T1 link modules, enable a fully
functional omnibus application. A single
2U-high compact Megaplex-2104 chassis
accomodates up to 16 omnibus voice
channels.
Point-to-multipoint applications for voice
or voice band modems are supported as
well (see Figure 2). The PCM data is
broadcasted from the master side towards
the stations. The stations can reply to the
master without being heard by the other
parties. Any signaling is passed on
transparently.
In point-to-point mode (see Figure 3) the
channel is operated as a regular E&M
voice channel.
Gain control is soft-selectable for both the
receive and transmit directions, enabling
easy installation in all environments.
All operating parameters are configurable
via the management system for both the
local and remote modules.
Enhanced diagnostics include local and
remote loopbacks and tone injection on
each channel.
Figure 2.  Typical Point-to-Multipoint (Modem) Connection
Figure 1.  Omnibus Connection

## Specifications  *(p.3)*

Number of Voice Channels
Voice Digitizing Technique
PCM (per ITU-T G.711 and AT&T
PUB-43801), A-law or -law
Bandwidth Requirement
64 kbps per enabled channel (one
timeslot), on both links
Line Type
Point-to-point: E&M, 2 or 4-wire,
soft-selectable
Other topologies: E&M 4-wire
Signaling
CAS over Timeslot 16
DTMF transparently transferred
Analog Parameters
ITU-T standards: G.712, G.714
Nominal level: 0 dBm
Nominal impedance:  600
Return loss (ERL) at 300 to 3400 Hz:
better than 20 dB
Frequency response (Ref:1020 Hz):
-
0.5 dB at 300 to 3000 Hz
-
1.1 dB at 250 to 3400 Hz
Level adjustment (soft-selectable):
-
TX: +5 dBm to -8 dBm
-
RX: +2 dBm to -10 dBm
-
Steps: 0.5 dB (0.1 dB), nominal
Signal to total distortion (G.712, G.713
Method 2):
-
-30 to 0 dBm0: better than 33 dB
-
-45 to +3 dBm0: better than 22 dB
Idle channel noise: better than -70 dBm0
(+20 dBrnc)
Transformer isolation: 1500 VRMS
Indicators (per channel)
E (green)
M (green)
Connectors
RJ-45, one per port
Diagnostics
Local digital loopback
Remote analog loopback
1 kHz tone towards the remote or local
side
Power Consumption
5.6W
Environment
Operating temperature: -10°C to 55°C
(0°F to 131°F)
Storage temperature: -20°C to 70°C
(-4°F to 158°F)
Humidity: up to 95%, non-condensing
Figure 3.  Basic E&M Point-to-Point Connection
764-141-01/12 Specifications are subject to change without prior notice.  1988–2012 RAD Data Communications Ltd. The RAD name, logo, logotype, and the terms EtherAccess, TDMoIP and TDMoIP Driven, and the
product names Optimux and IPmux, are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.

## VC-4/OMNI  *(p.4)*

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

## Ordering  *(p.4)*

MP2100M-VC-4/E&M/OMNI
Omnibus PCM Voice module with E&M
signaling for MP-2100/2104 and MP-4100
chassis
Table 4. Megaplex Voice Modules
VC-4/8/16
VC-4A/8A
VC-16A
VC-4/OMNI
VC-6/LB, VC-6/4LB
Number of ports
4/8/16
4/8
4/6
FXS


FXO


E&M



Local battery

Omnibus

Polarity reversal
& metering


ADPCM


Supported by
Megaplex-4100


