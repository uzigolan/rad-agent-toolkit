# MS-CESP Data/Voice Cross-Connect Processing Engine

<!-- datasheet product=ms-cesp family=mp4100 kind=card source=ms_cesp_ds_1.pdf -->

*Datasheet `ms_cesp_ds_1.pdf`, 4 pages. Product `ms-cesp`, family `mp4100` (card).

## Megaplex-4 MS-CESP Data/Voice Cross-Connect Processing Engine  *(p.1)*

- Point to multipoint data/voice services
- Data encapsulation protocols V.110, R111, oversampling
- Voice service conversion (PCM, ADPCM, G.729A, RTP)
- Service level protection
- Gateway from TDM to IP both for data (UDP/TCP) and
voice (RTP)
- Signaling plane for data and voice protocols
MS-CESP is a powerful processing engine, for data/voice,
providing sub-TS (DS0) cross-connect for compressed voice and
low-speed data.
High scale terminal server functionality for Megaplex-4100 and
Megaplex-4104 uses highly efficient multicore processor and
advanced algorithms. Advantages of software processing
compared to hardware (implemented in VS/VC Megaplex
modules) include:
- More feature-rich. In addition to voice/data cross-
connecting, compressing, converting and conferencing are
also available.
- Flexibility in new feature introduction
- Processing capabilities of up to 32-E1s-equivalent voice
channels, depending on the service required.
A built-in synchronization mechanism allows end-to-end services
over non-structured networks such as n x 64 kbps satellite links.
The bandwidth used for synchronization is 8 kbps (1 bit).
For applications involving Nokia Dynanet devices using National
bits in TS0 for inband management, the MS-CESP module cross-
connects these bits.

## MARKET SEGMENTS AND APPLICATIONS  *(p.1)*

Various applications can benefit from Megaplex-4 with MS-CESP
module:
- Centralized data processing for distributed networks over
PSN/TDM (not natively supported by Megaplex-4)
- Perfect solution for low-bandwidth lines, such as satellite
links
Its ability to handle a broad range of services by software, makes
the solution ideal for applications with broad and changing
requirements.

## ARCHITECTURE  *(p.1)*

The module occupies two module slots in the Megaplex-4 chassis.
It functions as a server: all the communication between the NNI
and UNI ports is performed via the Megaplex-4 CL module.

## VOICE COMPRESSION  *(p.1)*

Each voice channel can be re-coded into a smaller bandwidth
channel, using ADPCM 32K, ADPCM 16K  or G729A 8K. With
G.729A the compression ratio compared with PCM is 8:1,
meaning that just one bit is needed per voice channel. Signaling
CAS bit are also compressed, the bundle using just one or two
bits instead of a full timeslot.
MS-CESP uses voice channel activity data obtained from the CAS
pattern or calculated by the VAD (Voice Activity Detection)
algorithm over the received voice channel, to remove some
voice channels from the final bundle.
A transmitted bundle has fixed bandwidth (nxDS0) over TDM
ports while the payload is dynamically managed between active
and non-active channels.
Several voice and data channel can share same bundle.

## DATA SERVICES  *(p.1)*

The module features independent internal channels carrying
sync/async low-speed data. Each of the internal channels can
operate at programmable data rates of up to 64 kbps for
synchronous interfaces, and up to 38.4 kbps for asynchronous
interfaces.
Rate adaptation of serial async services is implemented by
V.110/R.111 protocols or oversampling.
The module cross-connects services at bit level, and multiplexes
voice and data on the same link.

## MS-CESP PSEUDOWIRE  *(p.2)*

The PW engine employing SAToP and CESoPSN encapsulation
methods provides connectivity of the MS-CESP module with
physical interfaces of local and remote devices.

## IP GATEWAY (TERMINAL SERVER)  *(p.2)*

A unique feature of the MS-CESP data application is the Gateway
to IP Endpoint. The server directly creates an IP endpoint at a UDP
or TCP Port. A packet received at this endpoint may include
multiple bytes. All of these bytes are sent to slave devices and
MS-CESP synthetizes an n x 64 kbps signal that includes an
oversampled async stream of received bytes.

## RESILIENCY  *(p.2)*

MS-CESP is designed to work in protecting pairs of two modules,
with 1+1 active-active redundancy for TDM processing, and virtual
IP addresses for any external service at both modules for
management.
In addition, the module employs optional protection schemes
between services created inside the module software.

## MANAGEMENT AND SECURITY  *(p.2)*

The MS-CESP module can be managed directly via CLI or via web
graphical application for Windows. The module supports SNMP
traps, SYSLOG, and SNTP.

## MONITORING AND DIAGNOSTICS  *(p.2)*

Comprehensive diagnostic capabilities include:
- Local and remote loopbacks
- Real-time alarms to alert the user on fault conditions
GbE
GbE
Megaplex-4
PSN
Network
Megaplex-4
GbE
Central Site
Serial Connection
DCN IP
Control Site
SCADA Controllers
Megaplex-4 “B”
with MS-CESP
module
Figure 1. Terminal Server in Central Site with MS-CESP module

## MS-CESP Specifications CAPACITY  *(p.3)*

Services
Voice/data point-to-multipoint or conference
with up to 16 end points per service
Up to 32 TDM virtual interfaces/entities
supporting SAToP, CESoPSN and TDMoIP
protocols
Up to 4 TDM interface domains (groups of TDM
interfaces) with independent processing and
configuration
Up to 10 service VLANs, plus management VLAN

## SERIAL INTERFACE  *(p.3)*

Protocols
Transparent
R111
V110
Oversampled
Channel
Activity
DAD (Data Activity Detection): based on RTS/DTR
(only for V110)

## VOICE INTERFACE  *(p.3)*

Voice Codecs  G729A (8K)
ADPCM (16,32K)
PCM-G.711
Number of
Voice
Channels
Codec
R2C
X8C
PCM
ADPCM32
ADPCM16
G729A
Voice
Compression
VAD
Silence suppression
Comfort noise generation
Echo
Cancelation
Up to 50 ms (G729A codec only)
Channel
Activity
CAS Pattern
VAD (Voice Activity Detection)

## USB PORT  *(p.3)*

Factory use only
Voice
Voice
ETH
Voice
Voice
ETH
Low Rate
ETH
Low Rate
ETH
Megaplex-4 “A”
with MS-CESP
module
Megaplex-4 “B”
with MS-CESP
module
TDM
Leased Line FE1
n x 64 kbps
Leased Line FE1
n x 64 kbps
Voice
Voice
ETH
Megaplex-4 “A”
with MS-CESP
module
E1
E1
ETH
ETH
Built in Jitter Buffer & Echo
cancellation for Voice
Built in Jitter Buffer & Echo
cancellation for Voice
Built in Jitter Buffer & Echo
cancellation for Voice
Figure 2. Voice and Data services over ETH and TDM links

## MS-CESP  *(p.4)*

24 Raoul Wallenberg St., Tel Aviv 6971923, Israel
Tel 972-3-6458181 | Fax 972-3-7604732
Email market@rad.com
North American Headquarters
900 Corporate Drive, Mahwah, NJ 07430, USA
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777
Email market@radusa.com
464-116-12/20 Specifications are subject to change without prior notice. © 1988–2021 RAD Data Communications Ltd. RAD products/technologies are protected by registered
patents. To review specifically which product is covered by which patent, please see ipr.rad.com. The RAD name, logo, logotype, and the product names MiNID, Optimux,
Airmux, IPmux, and MiCLK are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their respective holders.

## RESILIENCY  *(p.4)*

1+1 active-active
module-level
redundancy
below 50 msec protection
1+1 service level
redundancy
below 50 msec protection

## DIAGNOSTICS  *(p.4)*

LED Indicators RDY (green): The module is up and running
LINK (green) – for GbE port:
-
On: the port is connected to an active Ethernet
hub or switch
-
Off: Ethernet link is not detected
ACT (yellow) – for GbE port:
-
On or Blinking (in accordance with the traffic):
ETH frames are received or transmitted
-
Off: ETH frames are not received and
transmitted

## GENERAL  *(p.4)*

Processor
Rangeley2C (Intel Rangeley ATOM, 2-core
processor)
Xeon D 8-core processor
Environment
Operating
Temperature
0°C to 55°C (32°F to 131°F)
Storage
Temperature
-20°C to 70°C (-4°F to 158°F)
Humidity
Humidity: up to 95%, non-condensing
Power
Power
Consumption 35W max (at CPU operating frequency of 1.7GHz)

## Ordering  *(p.4)*

MP-4100M-MS/CESP/R2C
Megaplex-4 multiservice module, CES processor, 2C Rangeley
(Intel Rangeley ATOM, 2-core processor)
MP-4100M-MS/CESP/X8C
Megaplex-4 multiservice module, CES processor, Xeon D 8-core
processor
MP-CESP-LIC
License allowing processing of 8E1/T1 traffic capacity
Each module comes pre-loaded with a single instance of the MP-
CESP-LIC license.
X8C modules allow adding additional licenses to process more
than 8 E1/T1 traffic capacity. The number of additional licenses
depends on the module application. Please consult your Sales
representative on this subject.
The module must be ordered together with a RADcare package.