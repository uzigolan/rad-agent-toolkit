# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 8.2 Quality of Service (QoS)

*Manual `MiNID_ver_2_6_mn.pdf`, pages 205–216.*


## Applicability and Scaling  *(p.205)*


## Standards Compliance  *(p.205)*


## Benefits  *(p.205)*


## CoS Map Profiles  *(p.205)*

8. Traffic Processing 
3. View MiNID statistics (see Viewing Flow Statistics) and check that no traffic has been lost. 
8.2 Quality of Service (QoS) 
The MiNID Quality of Service (QoS) parameters include the following profiles: 
• 
CoS map profiles 
• 
Policer profiles 
• 
Envelope profiles 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
MEF 10.3 
Benefits 
• 
QoS allows you to optimize bandwidth, avoiding the need to allocate excessive bandwidth to 
facilitate the necessary bandwidth for traffic at different requirements of speed and quality. 
CoS Map Profiles 
Class of Service (CoS) mapping profiles map the following user priorities to internal CoS values:  
• 
p-bit — when ingress traffic is prioritized according to 802.1p requirements 
Factory Defaults 
By default, there are no CoS mapping profiles. When you create a CoS mapping profile, it is configured 
as follows: 
8. Traffic Processing 
• 
Classification p-bit 
• 
Mappings: 
 
Map 0 to CoS 7 
 
Map 1 to CoS 6 
 
Map 2 to CoS 5 
 
Map 3 to CoS 4 
 
Map 4 to CoS 3 
 
Map 5 to CoS 2 
 
Map 6 to CoS 1 
 
Map 7 to CoS 0 
Configuring CoS Mapping Profiles 
 To define a CoS profile: 
1. Navigate to the qos context (config>qos). 
2. Define a CoS profile and assign a classification to it: 
cos-map-profile <cos-mapping-profile-name> 
3. Map the user priority to a CoS value (user priority values 0–7 for p-bit CoS values 0–7): 
map <0-7> to <0-7> 
Examples 
 To create and configure a CoS mapping profile: 
• 
Profile name: my-p-bit 
• 
Map priority 6–7 to CoS 0 
• 
Map priority 3–5 to CoS 1 
• 
Map priority 0–2 to CoS 2 
exit all  
configure qos cos-map-profile my-p-bit  
  map 6..7 to-cos 0 
  map 3..5 to-cos 1 
  map 0..2 to-cos 2 
   exit all 

## Envelope Bandwidth Profiles  *(p.207)*

8. Traffic Processing 
 To create and configure a CoS mapping profile for a multi-CoS flow: 
• 
Profile name: p-bit-multi 
• 
Map priority 0 to CoS 7 
• 
Map priority 7 to CoS 0 
• 
Map untagged traffic to CoS 0 
exit all  
configure qos cos-map-profile p-bit-multi classification p-bit 
untagged-map to-cos 0 
   exit all 
Envelope Bandwidth Profiles 
An envelope profile as defined in MEF 10.3 contains a set of bandwidth profiles, each of which has been 
assigned a unique rank from 1 (lowest) to 4 (highest). Excess bandwidth from a higher rank can overflow 
to a lower rank to be shared, either to the committed or to the excess bucket. In MiNID, each profile 
corresponds to a separate CoS. The figure below illustrates an envelope profile with three CoSs. The 
coupling flags specify the path of overflow bandwidth. For the CoS coupling flags (CFi), 0=committed 
token bucket of the next lower rank, and 1=excess token bucket of the same rank. For coupling flag 0, 
0=discard, and 1=excess token bucket of the highest rank.  
CIR3
CBS3
EIR3
1
0
CIR2
CF3
EIR2
1
0
CBS2
CIR2
EIR1
1
0
CBS1
CF2
CF1
1
0 CF0
EBS3
EBS2
EBS1
Rank #3
Rank #2
Rank #1
Envelope
 
MEF 10.3 Bandwidth Profiles 
8. Traffic Processing 
When the envelope profile is assigned to a multi-CoS flow, it enables the flow to share excess 
bandwidth. The bandwidth sharing can be overflowed to the excess bucket or independent from the 
excess bucket.  
CIR3
CBS3
EIR3
1
CIR2
CF3
EIR2
1
CBS2
CIR2
EIR1
1
CBS1
CF2
CF1
EBS3
EBS2
EBS1
 
Sharing Excess Bandwidth 
CIRenv
CBS3
CF3
CBS2
CBS1
CF2
CF1
EBS3
EBS2
EBS1
EIRenv
0
0
0
 
Uncoupled from EIR/EBS 
8. Traffic Processing 
Configuring Envelope Profiles Using the Web Interface 
 To configure an envelope profile: 
1. Navigate to Configuration > QoS > Envelope Profile. 
1. MiNID 
2.  
 
 
 
 
 
Configuration>QoS> Envelope Profiles 
 
 
 
 
New Profile Name 
 
 
 
 
 
Apply 
 
 
 
 
 
Profile Name 
 
 
 
 
 
 
 
2. In the New Profile Name field, type the envelope profile name. 
3. Click <Apply>. 
The new envelope profile is added to the list. 
MiNID 
 
 
 
 
 
Configuration>QoS> Envelope Profile 
 
 
 
 
New Profile Name 
 
 
 
 
 
Apply 
 
 
 
 
 
Profile Name 
 
 
1 
Remove 
 
 
 
 
4. Click the desired profile to configure profile parameters. 
8. Traffic Processing 
MiNID 
 
 
 
 
 
Configuration>QoS> Envelope Profile>Cfg Profile 1 
 
 
 
 
CF Policy 
sharing-excess-bw 
 
Color Aware 
Disable 
 
Compensation 
0 
 
Cos 
0 
 
CIR 
0 
 
CIR Max 
1000000 
 
CBS 
0 
 
EIR 
1000000 
 
 
EIR Max 
1000000 
 
EBS 
32767 
 
 
Coupling Flag 
 
 
 
 
 
 
 
 
Apply 
 
 
5. Configure the profile: 
 
CIR: Defines the Committed Information Rate (CIR) for the current profile. The CIR specifies 
a bandwidth with committed service guarantee (“green bucket” rate). 
 
CBS: Defines the Committed Burst Size (CBS) for the current profile. The CBS specifies the 
maximum guaranteed burst size (“green bucket” size). 
 
EIR: Defines the Excess Information Rate (EIR). The EIR specifies an extra bandwidth with no 
service guarantee (“yellow bucket” rate). 
 
EBS: Defines the Excess Burst Size (EBS). The EBS specifies the extra burst with no service 
guarantee (“yellow bucket” size). 
 
Compensation: You can specify the amount of bytes that the policer can compensate for the 
layer 1 overhead (preamble and IFG) and the overhead for the added VLAN header in case 
of stacking. 
 
Color Aware: The policer profile can be specified as color aware. 
6. Click <Apply>. 
Configuring Envelope Profiles Using the CLI 
This section explains how to configure envelope profiles, to apply to multi-Cos flows per MEF 10.3.  
8. Traffic Processing 
Adding Envelope Policer Profiles 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type: 
envelope-profile <envelope-profile-name> 
An envelope profile with the specified name is created and the following prompt is displayed: 
config>qos>envelope-profile(<envelope-profile-name>)$  
The new envelope profile parameters are configured by default.  
3. Configure the envelope profile as described in Configuring Envelope Profile Parameters. 
Configuring Envelope Profile Parameters 
1. Navigate to configure qos envelope-profile <envelope-profile-name> to select the envelope 
profile to configure. 
The config>qos>policer-profile(<envelope-profile-name>)# prompt is displayed. 
2. Enter all necessary commands according to the tasks listed below. 
Task 
Command 
Comments 
Defining policy for 
excess bandwidth 
sharing  
cf-policy {sharing-excess-bw 
| uncoupled-bw-sharing} 
sharing-excess-bw –Excess bandwidth is shared to 
excess token bucket (see Sharing Excess 
Bandwidth figure). Selecting this parameter 
automatically sets coupling-flag-0 to 0, and sets 
each CoS coupling flag to 1.  
uncoupled-bw-sharing – Excess bandwidth is 
shared independently from EIR/EBS (see 
Uncoupled from EIR/EBS figure). Selecting this 
parameter automatically sets coupling-flag-0 to 0, 
and sets each CoS coupling flag to 0. 
If you enter no cf-policy, then coupling-flag-0 and 
each CoS coupling flag determine the bandwidth 
sharing. 
Specifying if the 
envelope profile is 
color aware 
color-aware 
 
Specifying the 
compensation (bytes) 
compensation <value> 
<value> is –(–32)-31 

## Policer Profiles  *(p.212)*

8. Traffic Processing 
Task 
Command 
Comments 
Specifying the CIR 
(Kbps), CBS (bytes), 
EIR (Kbps), and EBS 
(bytes) bandwidth 
limits, for a particular 
CoS 
cos <value> bandwidth 
[cir <cir-kbit-sec>] 
[cir-max <cir-max-kbit-sec>] 
[cbs <cbs-bytes>] 
[eir <eir-kbit-sec>] 
[eir-max <eir-max-kbit-sec>] 
[ebs <ebs-bytes>] 
[coupling-flag <coupling-fla
g>] 
Range for cos value is 0–7; you can define up to 
four or eight cos values in an envelope profile. 
Range for <cir-kbit-sec>, 
<cir-max-kbit-sec>, <eir-kbit-sec>, 
and <eir-max-kbit-sec>: 
0–1000000 (0–1 Gbps) 
Range for <cbs-bytes>, <ebs-bytes>:  
0–1000000 (0–1Mbytes) 
<cir-max-kbit-sec> must be greater 
than or equal to <cir-kbit-sec>. 
<eir-max-kbit-sec> must be greater 
than or equal to <eir-kbit-sec>. 
coupling-flag controls the path of 
overflow tokens: 0=overflow to 
committed token bucket, 1= 
overflow to excess token bucket. 
Specifying path of 
overflow bandwidth 
(see CF0 in MEF 10.3 
Bandwidth Profiles 
figure) 
coupling-flag-0 <value> 
<value> is 0–1: 
0=discard, and 1=excess token bucket of the 
highest rank 
Policer Profiles 
This section explains how to configure non-envelope policer profiles to limit traffic. The profiles can be 
applied to flows. 
Configuring Policer Profiles Using the Web Interface 
 To configure a policer profile: 
1. Navigate to Configuration > Qos > Policer Profile. 
8. Traffic Processing 
MiNID 
 
 
 
 
 
Configuration>QoS> Policer Profiles 
 
 
 
 
New Profile Name 
 
 
 
 
 
Apply 
 
 
 
 
 
Profile Name 
 
 
 
 
 
 
 
2. In the New Profile Name field, type the profile name. 
3. Click <Apply>. 
The new policer profile is added to the list. 
MiNID 
 
 
 
 
 
Configuration>QoS> Policer Profiles 
 
 
 
 
New Profile Name 
 
 
 
 
 
Apply 
 
 
 
 
 
Profile Name 
 
 
1 
Remove 
 
 
 
 
4. Click the desired profile to configure profile parameters. 
8. Traffic Processing 
MiNID 
 
 
 
 
 
Configuration>QoS> Policer Profile>Cfg Profile 
 
 
 
 
CIR [Kbps] 
0 
 
CBS [Bytes] 
0 
 
 
EIR [Kbps] 
1000000 
 
EBS [Bytes] 
32767 
 
 
Coupling Flag 
Disable 
 
 
Color Aware 
Disable 
 
Compensation 
0 
 
 
 
 
 
Apply 
 
 
5. Use the table below to fill in and select the desired parameters. 
6. Click <Apply>. 
Configuring Policer Profiles Using the CLI 
 To add a policer profile: 
1. Navigate to configure qos. 
The config>qos# prompt is displayed. 
2. Type: 
policer-profile <policer-profile-name> 
A policer profile with the specified name is created and the following prompt is displayed: 
config>qos>policer-profile(<policer-profile-name>)$  
The new policer profile parameters (except for name) are configured by default as described in 
the table below. 
3. Configure the policer profile as described in Configuring Policer Profile Parameters. 
 To configure policer profile parameters: 
1. Navigate to configure qos policer-profile <policer-profile-name> to select the policer profile to 
configure. 
The config>qos>policer-profile(<policer-profile-name>)# prompt is displayed. 
8. Traffic Processing 
2. Enter all necessary commands according to the tasks listed below. 
Policer Profile Parameters 
Task 
Command 
Comments 
Specifying the CIR (Kbps), 
CBS (bytes), EIR (Kbps), and 
EBS (bytes) bandwidth 
limits  
bandwidth [cir <cir-kbit-sec>] 
[cbs <cbs-bytes>] 
[eir <eir-kbit-sec>] 
[ebs <ebs-bytes>] 
Notes: 
• CIR & EIR allowed values: 
 
0–1000000 
• CBS & EBS allowed values: 
 
0–1000000 
• CIR can be set to zero only if CBS is 
set to zero and vice versa 
• EIR can be set to zero only if EBS is 
set to zero 
• CBS should be greater than the 
maximum frame size 
Specifying if the policer 
profile is color aware 
color-aware 
 
Specifying the 
compensation (bytes) 
compensation <-32–31> 
 
Specifying whether to 
check CIR+EIR when 
determining packet color 
coupling-flag 
Relevant only for color-aware policer 
profile in  
 
Examples 
 To create and configure a policer profile named Policer4: 
• 
CIR = 50,000 Kbps 
• 
CBS = 28,000 bytes  
• 
EIR = 30,000 Kbps 
• 
EBS = 20,000 bytes 
• 
Compensation = 30 
exit all 
configure qos policer-profile Policer4 
  bandwidth cir 50000 cbs 28000 eir 30000 ebs 20000 
  compensation 30 
8. Traffic Processing 
exit all 
 To display the configuration information for policer profile Policer4: 
MiNID# configure qos policer-profile Policer4 
MiNID>config>qos>policer-profile(Policer4)# info 
    bandwidth cir  49984 cbs  28000 eir  29952 ebs  20000 
    compensation  30  
 
 