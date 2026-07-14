# 13 Application Guide

*Manual `MP-1-mn_ver 2.2.pdf`, pages 438–483.*


## 13.1 Introduction  *(p.438)*

13.1 Introduction  
Overview  
This guide is designed to allow you to set up, demonstrate, test and troubleshoot TDM services using 
MP-1. The configuration can be performed via: 
• 
CLI 
• 
Shelf View application (Standalone and RADview Shelf View application) - OR - 
• 
RADview-Service Manager (RADview SM). 
• 
This application guide illustrates all these options. 
List of Required Equipment 
Item 
Catalog 
Qty 
MP-1/PSR/2GEU/6S/4E&M/1FEU 
6940140000 
4 
MP-1/PSR/2GEU/6S/C37/1FEU 
6940130000 
2 

## 13.2 MP1 P2P PW Services via MP-4 ERP  *(p.439)*

Megaplex-1 
13. Application Guide 
 
 
 
13.2 MP1 P2P PW Services via MP-4 ERP  
Operational WAN Application 
In this guide we will refer to the MP-4 ERP as a cloud. 
The diagram shows an ERP built with RAD MP-4100 and MP-1 devices as extensions. 
We will focus on the creating PW services between MP-1 A  to  MP-1 B  using RADview SM over this 
topology. 
Megaplex-1 
13. Application Guide 
 
PW Services 
In this application we used 2x MP1_6S_4EM,  HW: 0.0,  SW: 2.00(0.29) 
 
• 
Up to 12 PWs 
• 
Up to 12 DS-1s 
• 
Single PW per DS-1 

## 13.3 Configuring PW services with CLI  *(p.441)*

Megaplex-1 
13. Application Guide 
 
13.3 Configuring PW services with CLI 
E&M services 
 
 To configure an E&M Service: 
1. Create SVI.  
2. Create the interface with address.  
3. Configure the endpoint peer address. 
4. Enable the relevant bridge ports. 
5. Create flows & VLAN for the ETH port. 
6. Create UDP-over-IP PW with peer. 
Voice 
Voice 
Megaplex 1 
ERP 
ETH 
Megaplex 1 
ETH 
Megaplex-1 
13. Application Guide 
7. Enable the relevant DS1 port (logic port) with frame-type E1, and signaling. 
8. In the voice port choose:  
 
Coding: µ-law 
 
signaling  
 
2-wire 
 
E&M type 1 
9. Cross-Connect the voice TDM to the PW through DS1 port 
Megaplex-1 
13. Application Guide 
 
 
 
Megaplex-1 
13. Application Guide 
 
Serial (C.37) Services  
IEEE C37.94 is an IEEE standard that defines the rules to interconnect teleprotection 
and multiplexer devices of power utility companies. 
For the C37.94 service we will use 2 MP-1 units and one MP-4. 
Application Diagram 
 
Connections 

## 13.4 Configuring MP-1 PW Services Using the RADview Shelf View Application  *(p.445)*

Megaplex-1 
13. Application Guide 
 To configure a Serial C.37 Service: 
1. Create SVI.  
2. Create interface with address.  
3. Configure the endpoint peer address.   
4. Enable the relevant bridge ports. 
5. Create flows & VLAN for the ETH port. 
6. Create UDP-over-IP PW with peer. 
7. Enable the relevant DS1 port (logic port) with frame-type E1 and signaling. 
 
13.4 Configuring MP-1 PW Services Using the RADview Shelf 
View Application 
Login 
1. Enter RADview Front-End as illustrated below. 
2. Sign in to RADview by entering admin for the user name, the password and the tenant. 
Megaplex-1 
13. Application Guide 
 
3. Point to the MP-1 icon. 
 
The toolbar appears. 
4. Click the Shelf View icon. 
 
 
Shelf View Operation 
The MP-1 Shelf View window appears. 
Megaplex-1 
13. Application Guide 
1. Go to Configuration and select Read… 
 
2. Select the Read line and click <Apply>. 
 
3. Click <OK> when finished. 
Megaplex-1 
13. Application Guide 
 
RADview Shelf View Serial Service (C.37) Configuration 
Port Configuration 
 To open the relevant ports 
1. Choose the serial port section in the Edit screen. 
 
2. Open a serial port and a DS1 port (internal port). 
3. Select serial port 6 (CH 6) and double-click it. 
Megaplex-1 
13. Application Guide 
 
4. Change:  
 
Administrative status to Up 
 
Interface Type to RS-232 
 
Encapsulation Mode to V-110 
 
Mode to Sync 
 
Rate(Kbps) to 9.6 
 
5. Click < Set>. 
6. Click <OK> to acknowledge the popup message. 
Megaplex-1 
13. Application Guide 
 
7. Select DS1 port 6 (Int-DS1 6) and double-click it. 
 
The port configuration screen opens. 
8. Change  
 
Administrative Status to Up 
 
Frame Type  to E1 
 
Signaling to No 
9. Click <Set>. 
Megaplex-1 
13. Application Guide 
 
Peer Setup 
1. Go to Configuration Peers… 
Megaplex-1 
13. Application Guide 
 
 
2. Add a new peer by clicking <Add…>. 
3. Enter Name: PEER 3 
 
Address Type: IP 
 
IP Address: 30.30.30.1 
4. Click <Set>. 
Megaplex-1 
13. Application Guide 
 
 
 
Pseudowire Setup 
1. Go to Configuration PW… 
 
2. Add a pseudowire by  clicking < Add> >. 
Megaplex-1 
13. Application Guide 
 
3. Choose: Based On Selected PW… 
 
4. Ensure that Admin.Status is Up. 
5. Choose Peer – if we didn’t create one yet, we can do it here too 
Select 3 
6. Change the Out/In PW Labels to 3. 
7. Click <Select>. 
8. Click <Set>. 
Megaplex-1 
13. Application Guide 
 
9. Go to Configuration Port SVI… 
Megaplex-1 
13. Application Guide 
  
SVI Configuration 
1. Create a new SVI by clicking <Add…>. 
 
2. Change the Administrative Status to Up. 
3. Click <Apply>. 
Megaplex-1 
13. Application Guide 
 
Router Interface 
1. Go to Configuration Router… Router  Create Interface. 
 
2. Go to the router interface Router#1 . 
3. Add new interface by clicking <Add…>. 
Megaplex-1 
13. Application Guide 
 
4. Enter the following:  
 
Name: Router Interface 4 
 
Admin Status: Up 
 
Bind: SVI# 
 
IP Address: 30.30.30.2 
 
IP Mask: 255.255.255.0 
5. When complete, select: 
 
Apply 
 
Verify the Router interface is created 
 
Close this view 
Megaplex-1 
13. Application Guide 
 
Creating ETH Flows 
1. Go to Configuration Flows…  
 
We need to create two flows: 
• 
One flow from the GbE 1 to the Bridge port 
• 
The second flow from the SVI to the Bridge port 
 
Megaplex-1 
13. Application Guide 
 
Flow #1:  
2. Enter the Flow Name: 01 
3. Set Admin Status: Up 
4. Ingress Port: GbE 1 
5. Egress Port: Bridge Port 1 3 
6. Under Profiles 
 
Check the classifier 
 
Select the Vlan (V101) 
 
Under VLAN Tags 
 
No action required 
 
Apply 
Megaplex-1 
13. Application Guide 
 
Flow #2:  
7. Set: 
 
Flow Name: 02 
 
Set Admin Status: Up 
 
Ingress Port: SVI 2 
 
Egress Port: Bridge Port 1 4 
 
Reverse Direction: Yes  
8. Under VLAN Tags 
 
Set Outer VLAN to Push 
 
Enter the relevant VLAN ID 
9. Under Profiles 
 
Check the Classifier Profile 
 
Choose all 
10. Click <Apply>. 
Megaplex-1 
13. Application Guide 
 
Building Cross-Connects 
1. Go to Configuration X-Connect DS0… 
 
2. Select the DS1 port (Int-DS1 6) that you want to connect to the PW and click  
<DS0 X-Connect…>. 
Megaplex-1 
13. Application Guide 
 
3. Click < Edit View…> 
 
4. Click <Add…> 
Megaplex-1 
13. Application Guide 
 
5. Select Serial port CH 6 . 
6. Click <Select>. 
 
7. Point to Port TS #1 . 
8. Click <Group…>. 
Megaplex-1 
13. Application Guide 
 
The following screen appears: 
9. Click <Set>. 
 
10. Click <Close>. 
Megaplex-1 
13. Application Guide 
 
The flag in the Edit pane appears. 
 
Final Steps 
1. In the Edit pane, go to Configuration Update. 
 
2. Choose the Configuration line and click <Apply>. 
 

## 13.5 Configuring MP-1 PW Services using RADview SM  *(p.467)*

Megaplex-1 
13. Application Guide 
13.5 Configuring MP-1 PW Services using RADview SM 
Before provisioning the services using RADview SM, we need to build corresponding profiles & 
infrastructure. 
CoS (Class of Service) Profile Creation 
 
Megaplex-1 
13. Application Guide 
CoS to pBit Profile Creation  
 
• 
Prepare the CoS to P-bit list as follows: 
 
CoS 
P-bit 
Platinum 
6 
Gold 
4 
Silver 
2 
Best effort 
0 
Megaplex-1 
13. Application Guide 
 
CoS to Queue Profile Creation 
 
The CoS-to-queue profile defines the relationship of each one of the CoS criteria to the specific queue 
inside the group/block. 
Remember – lower queue = higher priority 
 
Megaplex-1 
13. Application Guide 
 To start the CoS to queue creation: 
1. From the Profiles menu, select CoS to Queue.  
2. Click <+>. 
 
Creating Sub Domain 
Our goal now is to create a subdomain and then create an NE for each device. In this example, the 
default subdomain is NOC. You will then add network elements (your devices) to the newly created 
sublevel. 
Megaplex-1 
13. Application Guide 
 
Megaplex-1 
13. Application Guide 
 
 
Megaplex-1 
13. Application Guide 
 
 
Megaplex-1 
13. Application Guide 
Customer & Provider Creation 
 
 
Megaplex-1 
13. Application Guide 
Adding an NE 
 
Adding a Cloud 
The cloud option inside the RADview inventory will be used in order to simulate a 3rd party network. In 
our case, the cloud will act as provider’s network inside our setup. In order to walk through the cloud 
creation process within RADview, we have to understand the following terms: 
• 
Access point – this is the physical port for accessing the cloud from the outside network. 
• 
Cloud domain – this is the section which connects two cloud access points to each other and 
completes a path within the cloud itself.  
In our case, we have to create one domain which contains 2 access points as described in this scheme: 
Megaplex-1 
13. Application Guide 
 
 
 
Megaplex-1 
13. Application Guide 
Adding Topology Links 
 
Complete Topology 
This is the final topology scheme after all the NEs, the cloud and the links have been added. 
 
Megaplex-1 
13. Application Guide 
ERP Auto-Discovery 
 
Tunnel Creation 
Note: The tunnel should be created between your end-point (MPs with IO cards) elements 
Megaplex-1 
13. Application Guide 
 
 
Megaplex-1 
13. Application Guide 
Provisioning E&M TDM Service 
3. 
 

## 13.6 Success criteria  *(p.481)*

Megaplex-1 
13. Application Guide 
What is going on inside RADview? – E&M TDM Service 
 
13.6 Success criteria 
E&M Results 
 
When you finish the configuration process, follow these steps to test the service traffic: 
4. Connect each side of the E&M ports to the VSC device 
Megaplex-1 
13. Application Guide 
5. Connect a phone to each VSC device 
6. Lift both telephones and make sure you can hear your voice from one end point to another 
LBT Results 
C37.94 
For the C37.94 service, we will use two MP-1 units and one MP-4 unit. 
In order to use an LBT in MP-4, use the following cross connect: 
 
Working with LBT 
• 
On the LBT, choose the following parameters: 
 
ASY 
 
Rate = 9.6 KB 
 
RTS = ON 
• 
To move from parameter to parameter, use the PARAM button. 
• 
To change the values for each parameter, use the SCROLL arrows. 
• 
To start/stop the serial data, use the RUN/STOP button. 
Megaplex-1 
13. Application Guide 
 
 
 LBT Results 
• 
After configuring the LBT with the relevant parameters, start running the LBTs in the devices: 
 
We should see the received data in both devices. 
 
We should not have any errors at this stage, unless there is a problem with the  
Clock station. 
                      
 
 
 