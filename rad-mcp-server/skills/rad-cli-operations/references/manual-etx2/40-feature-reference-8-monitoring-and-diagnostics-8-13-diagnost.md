# Feature Reference – 8 Monitoring and Diagnostics – 8.13 Diagnostic Tests

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1566–1569.*


## (chapter introduction)  *(p.1566)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Displaying brief alarm and 
event history log, 
optionally according to 
specified criteria 
show brief-log 
show brief-log {<source-type> [<source-id>] | all} 
[minimum-severity {critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] [start <yyyy-mm-dd> 
[<hh:mm[:ss]>]] [end <yyyy-mm-dd> [<hh:mm[:ss]>]] 
show brief-log {<source-type> [<source-id>] | all} 
[minimum-severity {critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] {[last-seconds <seconds>] | 
[last-entries <entries>]} 
Displaying alarm and 
event history log, 
optionally according to 
specified criteria 
show log 
show log {<source-type> [<source-id>] | all} 
[minimum-severity {critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] [start <yyyy-mm-dd> 
[<hh:mm[:ss]>]] [end <yyyy-mm-dd> [<hh:mm[:ss]>]] 
show log {<source-type> [<source-id>] | all} 
[minimum-severity {critical | major | minor | cleared}] 
[order-ascending] [time-zone-utc] 
[acknowledged-included] {[last-seconds <seconds>] | 
[last-entries <entries>]} 
 
8.13 Diagnostic Tests 
ETX‑2i supports the following diagnostic tests: 
• 
Ping test – pings IPv4 or IPv6 addresses to check the ETX‑2i IP connectivity with that host. 
• 
Trace route – diagnostic utility that traces the route through the network from ETX‑2i to the 
destination host.  
 
 

## Applicability and Scaling  *(p.1567)*


## Functional Description  *(p.1567)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Applicability and Scaling 
All router entities support ping and trace route applications.  
Ping test supports a maximum of 1pps pings. 
The trace route utility supports up to 30 hops. 
Functional Description 
Ping Test 
The ETX‑2i router module provides a ping application that enables pinging IPv4 or IPv6 addresses to 
check the ETX‑2i IP connectivity with that host. When the user initiates a ping test, the routing protocol 
(static, OSPF, BGP, etc.) selects the router interface on the specified router, from which the pings are 
sent to the specified IP address. This is usually the router interface closest to the IP address. By default, a 
router interface on Router 1 sends five 32-byte pings to the specified IP address. However, you can 
configure another router to send the pings, as well as a different packet size, number of pings (packets) 
to generate, or a continuous ping (infinite).  
The ping generator continues to generate ping requests according to the number of configured pings, or 
until you manually disrupt it (by pressing Ctrl+C). 
 
Note 
Pings affect packet counters. 
Ping Test Results 
When generating a ping, a waiting timeout of 10 seconds is initiated.  
One of the following messages is generated, according to the response during the timeout period. 
• 
Reply received within the timeout:  
Reply from 1.1.1.1: bytes = 32, packet number = 0, time = 10 ms 
• 
No reply within the timeout: 
Timed Out 
• 
The destination network is not reachable: 
Network Unreachable 
 
 

## Factory Defaults  *(p.1568)*


## Configuring a Ping Test  *(p.1568)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
When the Ping process ends, the following message is generated (for Ping test with five packets): 
5 packets transmitted. 5 packets received, 0% packet loss 
round-trip (ms) min/avg/max = 0/4/10 
If the remote host answers, ETX‑2i displays the ping results including the round-trip delay, rounded as in 
the following table.  
Round Trip Delay 
Displayed in Ping Results 
<= 10 msec 
time < 10 ms 
>= 11 msec and <= 20 msec 
time < 20 ms 
>= 21 msec and <= 30 msec 
time < 30 ms 
>= 31 msec and <= 40 msec 
time < 40 ms 
: 
: 
: 
: 
Factory Defaults 
When a ping test is added, it has the following default settings:       
Parameter  
Default Value 
number-of-packets 
5 
payload-size (bytes) 
32 
router-entity 
1 
Configuring a Ping Test 
 To ping an IP host: 
• 
In any level, start pinging the host, specifying its IP address (IPv4 or IPv6) and optionally the 
number of packets to send, payload size (in bytes), and router entity number: 
 
ping <ip-address> [number-of-packets <packets>] [payload-size <bytes>] [router-entity 
<number>] 
 

## Tracing the Route  *(p.1569)*


## Examples  *(p.1569)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Parameter 
Description 
Value 
<ip-address> 
IP address of the remote device (destination) 
 
Valid IPv4 or IPv6 address of the 
remote device 
1.1.1.1–255.255.255.255 
Note: Multicast address is not 
allowed. 
number-of-packets 
Number of test packets (pings) to be sent 
Possible values:  
0 (forever), 1-10000 
payload-size 
Size of payload (packet) in bytes 
Possible values:  
32-1450 bytes 
router-entity 
Router entity related to Ping command 
Possible values: 1-max-vrf-number 
Note: Ping is sent from specified 
router, or if not specified, from 
router 1. 
Tracing the Route 
This diagnostic utility traces the route through the network from ETX‑2i to the destination host. The 
trace route utility supports up to 30 hops. 
 To trace a route: 
• 
In any level, start the trace route and specify the IP address (IPv4 or IPv6) of the host to which 
you intend to trace route: 
trace-route <1.1.1.1–255.255.255.255> 
Examples 
The following is an example of a ping test. 
ETX‑2i# ping 10.10.10.10 
 
Reply from 10.10.10.10: bytes = 32, packet number = 0, time < 10 ms 
Reply from 10.10.10.10: bytes = 32, packet number = 1, time < 10 ms 
Reply from 10.10.10.10.44: bytes = 32, packet number = 2, time < 10 ms 
The following is an example of tracing a route. 
ETX‑2i# trace-route 172.17.92.113 
Trace Route 1: Destination 172.17.92.113 reached 