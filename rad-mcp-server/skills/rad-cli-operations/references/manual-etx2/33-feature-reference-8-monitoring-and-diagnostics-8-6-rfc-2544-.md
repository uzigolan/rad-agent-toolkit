# Feature Reference – 8 Monitoring and Diagnostics – 8.6 RFC-2544 Testing

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1462–1475.*


## Applicability and Scaling  *(p.1462)*


## Standards  *(p.1462)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
#*********Configure L3 SAT generator 
      generator gen1 
        local-ip-address 20.20.20.101 
        router-entity 1 
        no shutdown 
        peer 20.20.20.20 
          peer-profile peer1 
          test-session test1 session-profile session1 bw 10000 dscp 11 
          test-session test2 session-profile session2 bw 5000 dscp 12 
          activate 
        exit all 
save 
8.6 RFC-2544 Testing 
You can perform BERT testing based on RFC-2544: 
Throughput test 
Detects the maximum frame rate without lost frames. 
Packet loss test 
Detects the point at which frame loss does not occur. 
Latency test 
Determines average frame roundtrip time. 
 
Note 
You can run the RFC-2544 tests up to 1 GbE at a time. 
These tests enable evaluation of the performance of network devices to provide performance metrics of 
the Ethernet network and validate the SLA. 
Applicability and Scaling 
This feature is applicable to all ETX‑2i products. 
RFC-2544 test supports eight generators. 
Standards  
RFC-2544, Benchmarking Methodology for Carrier Ethernet Networks 

## Functional Description  *(p.1463)*


## Factory Defaults  *(p.1463)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Functional Description 
RFC-2544 testing uses OAM CFM messages such as Loopback (LB), Loss Measurements (LM), and Delay 
Measurements (DM) frames. Therefore, end-to-end OAM CFM is necessary for the testing. User data 
can’t be transmitted via associated OAM service data/flows while an RFC-2544 test is running. 
In a bidirectional throughput test, the local ETX‑2i generates LBM + data TLV messages towards the 
far-end device, which responds with LBR messages. The local ETX‑2i calculates the roundtrip throughput. 
In a unidirectional throughput test, the local ETX‑2i generates 1DM messages towards the far-end 
device, which verifies the frames and calculates unidirectional throughput. The convergence algorithm is 
based on a binary search using LMM and LMR messages. 
The packet loss test is performed as follows for all selected frame sizes: 
• 
Transmit x frames at a rate of 100% throughput. 
• 
Calculate frame loss with the formula: (tx - rx) / 100 * tx 
• 
Decrease rate by 10% and repeat the test until two trials result in no frame loss. 
The latency test is performed as follows: 
• 
Transmit DMM frames at throughput rate for 10 seconds. 
• 
Calculate the latency using DMM and DMR frames that are transmitted after 1 second.   
• 
The test result is the average number of iterations per frame size (up to 5 minutes per frame 
size). 
• 
Applicable for round-trip mode 
Note 
If the remote MEP status is NEW, ETX‑2i does not launch the RFC-2544 test, 
unless the relevant dest NE is configured with the remote MAC address. 
Factory Defaults 
By default, no profiles or tests are defined. 
When you create a test profile, it is configured by default as shown below. 
ETX‑2i# config test rfc2544 
ETX‑2i>config>test>rfc2544# profile-name Testprf 
ETX‑2i>config>test>rfc2544>profile-nam(Testprf)$ inf d 
    frame-size  64 
    pattern  all-ones 
    tlv-type  data 

## Performing Tests  *(p.1464)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
    test-direction  bidirectional 
    frames-number-in-attempt 200000 
    frame-loss-tolerance  20 
    throughput-measurement-accuracy 100000 
    number-of-trials  1 
    no learning-frames 
When you create a test, it is configured by default as shown below. 
ETX‑2i# config test rfc2544 
ETX‑2i>config>test>rfc2544# test 1 
ETX‑2i>config>test>rfc2544>test(1)$ inf d 
    no bind 
    max-rate  0 convention data-rate compensation 0 
    type  throughput 
    no max-test-duration 
    no associated-flow 
Performing Tests 
In order to perform RFC-2544 tests, you must configure: 
• 
Bidirectional data flows that are administratively enabled. If one of the flows is associated with 
the test, its egress port and queue block must be identical to the associated port and queue 
block of the MEP to which the test is bound.  
• 
MEP and Destination NE 
• 
RFC-2544 profile – Template to create test runs. You can configure up to eight test profiles. 
• 
RFC-2544 test – Associated with RFC-2544 profile. Up to eight tests can use the same test 
profile. In one RFC-2544 test, you can perform one or more of the three test types. 
Note 
Up to eight RFC-2544 tests can run concurrently. 
If you are performing more than one type of test, they are performed in the following order: 
• 
Throughput  
• 
Packet loss  
• 
Latency – Up to 20 latency test attempts are performed in the remaining time, according to the 
configured maximum test duration (each attempt requires 15 seconds).  
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
 To configure RFC-2544 test profiles: 
1. Navigate to configure test rfc2544. 
2. Enter: 
profile-name <name> 
A test profile with the specified name is created if it does not already exist, and the 
config>test>RFC2544> profile-name(<name>)$ prompt is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Enabling/disabling ETH-
LCK frame when 
activating RFC-2544 test 
eth-lck 
no eth-lck 
By default, ETH-LCK is enabled. 
Configuring frame loss 
tolerance 1/1 (one to 
one) 
frame-loss-tolerance <frames> 
Defines the success criteria for the 
throughput test. 
Each throughput attempt is defined 
as a success only if the number of 
lost packets is less than or equal to 
the number of frames configured for 
frame-loss-tolerance. 
Success in a throughput attempt sets 
the next attempt to a higher rate, 
while a failure in an attempt sets the 
next attempt to a lower rate. 
Configuring frame sizes 
for the test  
frame-size [64] [128] [256] [512] [1024] 
[1280] [1518] [1700] [1900] [2000] [custom 
<custom>] 
You can specify one or more 
standard frame sizes, as well as a 
custom frame size (64–2000).  
Configuring how many 
frames in attempt 
frames-number-in-attempt 
The maximum number of frames 
(transmitted packets) is the maximal 
value of unsigned long (4294967295 
(0xffffffff)). 
Configuring amount and 
frequency of learning 
frames  
learning-frames number <value> 
frequency { once | once-per-trial }  
no learning-frames  
 
Configuring the number 
of trials for the test 
number-of-trials <value> 
Possible values: 1–3 
Configuring pattern of 
test frame payload 
pattern { all-ones | all-zeros-without-crc | 
all-zeros-with-crc | alternate | 
prbs-with-crc | prbs-without-crc } 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring direction of 
test (unidirectional or 
bidirectional)  
test-direction { unidirectional | 
bidirectional } 
 
Configuring accuracy of 
throughput 
measurement 
throughput-measurement-accuracy <bps> 
 
Configuring TLV type as 
test or data 
tlv-type { test | data } 
 
 To configure RFC-2544 tests: 
1. Navigate to configure test rfc2544. 
2. Enter: 
test <id> 
The config>test>rfc2544> test(<id>)# prompt is displayed. 
3. Perform the required tasks according to the following table. 
Task 
Command 
Comments 
Activating the test 
activate date <dd-mm-yyyy> <hh:mm:ss> 
activate recurring <hours>  
Enter no activate to stop the 
test. 
Associating test with flow in order to 
retrieve bandwidth profile and QoS 
information.   
associated-flow <name> 
Flow must be active, and its 
egress port and queue block 
must be identical to the 
associated port and queue block 
of the MEP to which the test is 
bound. 
Binding to destination NE 
bind oam-cfm md <md-id> ma <ma-id> mep <mep-id> 
service <service-id> dest-ne <dest-ne-id>  
There must be bidirectional flows 
using the same classification and 
port associated with the MEP. 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Configuring maximum rate for test 
max-rate <bps> [convention { line-rate | data-rate }] 
[compensation <compensation>] 
max-rate – The maximum rate 
applies to throughput and loss 
tests. 
convention – Determines 
whether the interpacket gap is 
included in test result 
calculations: 
line-rate – Interpacket gap is 
included. 
data-rate – Interpacket gap is 
not included.  
compensation – Allowed range is 
0–63. The compensation value is 
added to frame size, to allow for 
Layer-1 overhead in the network. 
Note: It is not necessary to 
configure the maximum rate if 
associated-flow is used to 
associate the test with a flow 
that has a Policer profile, as in 
that case the maximum rate is 
derived from the flow Policer 
profile. 
Configuring maximum duration of test 
max-test-duration <minutes> 
Possible values: 0, or 2–60 
The value 0 indicates no limit; 
the test runs until completion. If 
a value from 2–60 is configured, 
the test is stopped when the 
configured maximum duration 
has elapsed, whether or not all 
the configured test types have 
completed. 
Associating a test profile with the test 
test-profile <name> 
 
Defining the type(s) of benchmark test 
to perform on this run 
type [throughput] [latency] [frame-loss] 
 
Clearing test report 
clear-reports 
 
Displaying number of lost frames for 
each test attempt 
show attempt-lost-frames 
See Viewing Lost Frames Per 
Test Attempt. 

## Examples  *(p.1468)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
Task 
Command 
Comments 
Displaying test report 
show report all 
show report iteration <iteration-number> 
See Viewing Test Report. 
Displaying test status 
show status 
See Viewing Test Status. 
Displaying test summary 
show summary 
See Viewing Test Results. 
Examples 
Running RFC-2544 Test 
 To run RFC-2544 test: 
• 
Test direction – bidirectional  
• 
Number of trials – 2  
• 
Frame sizes – 64, 256, 1400 [custom] 
• 
Test types – throughput, frame loss, latency 
• 
Bound to MD 1 MA 1 service 1 MEP 1 Destination NE 1 
• 
Associated to flow test_flow1, that has associated Policer profile test_policer with CIR=9984, EIR 
= 0, and is associated with classification, port, and queue block of the above MEP  
• 
Maximum test duration – 1 hour 
ETX‑2i# configure test rfc2544 
ETX‑2i>config>test>rfc2544# profile-name p1 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$  
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ frame-size 64 256 custom 1400 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ pattern all-ones 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ tlv-type data 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ test-direction bidirectional 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ frames-number-in-attempt 5000 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ frame-loss-tolerance 10 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ number-of-trials 2 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ no learning-frames 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ no eth-lck 
ETX‑2i>config>test>rfc2544>profile-nam(p1)$ exit 
ETX‑2i>config>test>rfc2544# test 1 
ETX‑2i>config>test>rfc2544>test(1)$ test-profile p1 
ETX‑2i>config>test>rfc2544>test(1)$ type throughput latency frame-loss 
ETX‑2i>config>test>rfc2544>test(1)$ bind oam-cfm md 1 ma 1 mep 1 service 1 dest-ne 1 
ETX-2i Devices 
8. Monitoring and Diagnostics 
ETX‑2i>config>test>rfc2544>test(1)$ associated-flow test_flow1 
ETX‑2i>config>test>rfc2544>test(1)$ max-test-duration 60 
ETX‑2i>config>test>rfc2544>test(1)$ activate 
ETX‑2i>config>test>rfc2544>test(1)$ show status 
Activity Status            : In Progress 
Elapsed Time <dd:hh:mm:ss> : <00:00:15:24> 
ETX‑2i>config>test>rfc2544>test(1)$ show status 
Activity Status            : Completed 
 
ETX‑2i>config>test>rfc2544>test(1)$ show summary 
Iteration Start       Start     Duration Duration 
          Date        Time      Days     Time 
----------------------------------------------------------------------------- 
1         08-01-2012  11:31:43  0        <00:38:25> 
Viewing Test Report 
You can display the test report for all iterations, or for a specific iteration. 
The following illustrates displaying the test report for the test from the above section (all iterations). 
 To display the complete test report: 
• 
In the config>test>rfc2544>test<test number># prompt, enter show report all. 
The complete report screen is displayed. For information on the test report counters, see the 
table below. 
ETX‑2i>config>test>rfc2544>test(1)$ show report all 
Test ID                : 1 
Iteration Number       : 1 
Date & Time            : 08-01-2012                       11:31:43 
Profile Name           : p1 
Number of Trials       : 2 
Duration <dd:hh:mm:ss> : <00:00:38:25> 
 
Test Parameters 
----------------------------------------------------------------------------- 
Bind: MD                       : 1             MA         : 1 
MEP         : 1 
P-Bit                          : 0             VLAN       : 200 
Max Rate (bps)    : 1000000000 
Convention        : Data Rate           Compensation  : 0 
Frames in Burst   : 200000 
Pattern           : All Ones 
Frame Type  : Data 
Search Resolution              : 1        Tolerance  : 5 
Learning Frames:               : 0        Frequency  : 
Direction                      : Bidirectional 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Flow Parameters 
----------------------------------------------------------------------------- 
Flow Name    : test_flow1 
Fixed Queue  : 0                               Mapping Profile  : 
Policer Name : test_policer 
CIR (Kbps)   : 9984                            EIR (Kbps)       : 0 
 
Throughput Report 
----------------------------------------------------------------------------- 
Trial  : 1 
Status : Success                 Duration  : <00:00:00:49> 
Frame Size     Theoretical Max     Throughput Throughput Success 
               (FPS)               (FPS)       (Mbps)    (%) 
----------------------------------------------------------------------------- 
64             1953125             1490312      763.040    76 
256            488281              453309       928.379    92 
1400           97656               96173        984.812    98 
 
Throughput Report 
----------------------------------------------------------------------------- 
Trial  : 2 
Status : Success                 Duration  : <00:00:00:52> 
Frame Size     Theoretical Max     Throughput Throughput Success 
               (FPS)               (FPS)       (Mbps)    (%) 
----------------------------------------------------------------------------- 
64             1953125             1490312      763.040    76 
256            488281              453309       928.379    92 
1400           97656               96173        984.812    98 
 
Loss Report 
----------------------------------------------------------------------------- 
Trial  : 1 
 
Status : Success                 Duration  : <00:00:02:21> 
 
Frame Size            : 64 
Theoretical Max (FPS) : 1953125 
 
Throughput of Max    Success 
(%)                  (%) 
----------------------------------------------------------------------------- 
100                  76 
90                   84 
80                   95 
70                   100 
60                   100 
 
Frame Size            : 256 
Theoretical Max (FPS) : 488281 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Throughput of Max    Success 
(%)                  (%) 
----------------------------------------------------------------------------- 
100                  92 
90                   100 
80                   100 
 
Frame Size            : 1400 
Theoretical Max (FPS) : 97656 
 
Throughput of Max    Success 
(%)                  (%) 
----------------------------------------------------------------------------- 
100                  98 
90                   100 
80                   100 
 
Loss Report 
----------------------------------------------------------------------------- 
Trial  : 2 
 
Status : Success                 Duration  : <00:00:02:21> 
 
 
Frame Size            : 64 
Theoretical Max (FPS) : 1953125 
 
Throughput of Max    Success 
(%)                  (%) 
----------------------------------------------------------------------------- 
100                  76 
90                   84 
80                   95 
70                   100 
60                   100 
 
Frame Size            : 256 
 
Theoretical Max (FPS) : 488281 
 
Throughput of Max    Success 
(%)                  (%) 
----------------------------------------------------------------------------- 
100                  92 
90                   100 
80                   100 
 
Frame Size            : 1400 
Theoretical Max (FPS) : 97656 
 
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Throughput of Max    Success 
(%)                  (%) 
----------------------------------------------------------------------------- 
100                  98 
90                   100 
80                   100 
 
Latency Report 
----------------------------------------------------------------------------- 
Trial  : 1 
 
Status : Success                 Duration  : <00:00:15:15> 
Num of Attempts : 20 
 
Frame Size     Latency 
               (micro-sec) 
----------------------------------------------------------------------------- 
64             1 
256            1 
1400           1 
 
Latency Report 
----------------------------------------------------------------------------- 
Trial  : 2 
 
Status : Success                 Duration  : <00:00:15:14> 
Num of Attempts : 20 
 
Frame Size     Latency 
               (micro-sec) 
----------------------------------------------------------------------------- 
64             0 
256            0 
1400           0 
 
ETX‑2i>config>test>rfc2544>test(1)$ 
 To display the test report for a specific iteration: 
• 
In the config>test>rfc2544>test<test number># prompt, enter show report iteration <iteration 
number>. 
The report screen is displayed for the requested iteration. For information on the test report 
counters, see the table below. 
ETX‑2i>config>test>rfc2544>test(1)# show report iteration  1 
Test ID                : 1 
Iteration Number       : 1 
Date & Time 
Profile Name           : p1 
Number of Trials       : 1 
Duration <dd:hh:mm:ss> 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Test Parameters 
----------------------------------------------------------------------------- 
Bind: MD          : 1             MA            : 1                   MEP         : 1 
P-Bit             : 0             VLAN          : 100 
Max Rate (bps)    : 100000 
Convention        : Data Rate     Compensation  : 0 
Frames in Burst   : 100000     
  Pattern       : All Ones            Frame Type  : Data 
Search Resolution : 10000         Tolerance     : 50 
Learning Frames   : 0             Frequency     : 
Direction         : Bidirectional 
 
 
Counter 
Description 
Bind 
The MEP parameters that the RFC-2544 test is running on 
P-Bit 
The P-Bit of the tested service  
VLAN 
The VLAN on which test is performed  
Max Rate (bps) 
The maximum rate at which the test starts 
Convention 
Convention used for this test: 
Line Rate or Data Rate  
Compensation 
Indicates whether compensation due to editing will be performed in the test and the 
number of bytes that will be compensated 
Frames in Burst 
The number of frames transmitted in each attempt 
Pattern 
The data pattern in the transmitted packets 
Frame Type 
The frame type (TLV) used in the transmitted packets: 
Data or Test 
Search Resolution 
Size of the smallest search resolution step 
Tolerance 
The number of packets that can be lost without declaring Fail 
Learning Frames 
Indicates whether some frames are transmitted before the test starts, in order to 
enable the network learning 
Frequency 
Indicates whether learning frames are transmitted once per test or once per trial 
Direction 
Bidirectional or Unidirectional  
ETX-2i Devices 
8. Monitoring and Diagnostics 
Viewing Test Status  
 To display the test status: 
• 
In the config>test>rfc2544>test<test number># prompt, enter show status. 
The status screen appears. For information on the test status values, see the following table. 
ETX‑2i>config>test>rfc2544>test(1)# show status 
Activity Status            : In Progress 
Elapsed Time <dd:hh:mm:ss> : <00:00:16:39> 
 
Current Test Type : Throughput    Current Frame Size  : 64 
Trial No.         : 1             Attempt No.         : 1 
Remote MEP Status : OK 
 
Parameter Displayed 
Description 
Current Test Type 
Test type can be: 
Throughput 
Packet Loss  
Latency 
Current Frame Size 
Current tested frame size 
Trial No. 
Current trial number. 1–3 
Attempt No. 
Current performed attempt number 
Remote MEP Status 
Peer OAM status  
Viewing Lost Frames Per Test Attempt 
The following illustrates displaying the number of lost frames for each test attempt. 
ETX‑2i>config>test>rfc2544>test(1)$ show attempt-lost-frames 
Test ID                     : 4 
Number of Frames in Attempt : 700000 
  
Trial : 1 
  
Frame Size : 128 
  
 
 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Attempt   Throughput    Loss Frames 
--------------------------------------------------------------- 
1         999999488     559210 
2         499999744     419391 
3         249999872     139756 
4         124999936     0 
5         187499904     0 
6         218749888     59908 
7         203124896     10805 
8         195312400     0 
9         199218648     0 
10        201171772     4070 
11        200195210     650 
Viewing Test Results 
You can display a summary of the RFC-2544 test results. 
 To display the summary test results: 
• 
In the config>test>rfc2544>test<test number># prompt, enter show summary. 
The summary report screen is displayed. For information on the test report summary counters, 
see the following table. 
ETX‑2i>config>test>rfc2544>test(5)# show summary 
Iteration Start       Start     Duration Duration 
          Date        Time      Days     Time 
--------------------------------------------------------------- 
1         10-08-2015  15:16:40  0        <04:17:04> 
 
Counter 
Description 
Iteration 
The iteration number of the test 
Start Date 
The date that the test started (dd-mm-yyyy) 
Start Time 
The time of day that the test started (hh:mm:ss) 
Duration Days 
The duration of the test in days  
Duration Time 
The duration of the test (hh:mm:ss) 
 