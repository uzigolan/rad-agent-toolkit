# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 11.8 RFC-2544 Responder

*Manual `MiNID_ver_2_6_mn.pdf`, pages 360–360.*


## Applicability and Scaling  *(p.360)*


## Standards Compliance  *(p.360)*


## Benefits  *(p.360)*


## Functional Description  *(p.360)*


## Configuring RFC-2544 Responder  *(p.360)*

11. Monitoring and Diagnostics 
11.8 RFC-2544 Responder 
 MiNID provides an RFC-2544 responder that allows you to test the link at full capacity, and handles up 
to 1Gbps of traffic. 
Applicability and Scaling 
This feature is applicable to all MiNID options. 
Standards Compliance 
RFC-2544, Benchmarking Methodology for Carrier Ethernet Networks 
Benefits 
You can evaluate the performance of network devices to provide performance metrics of the Ethernet 
network and validate the SLA. 
Functional Description 
The RFC-2544 responder uses OAM CFM loopback messages (LBM) and loopback replies (LBR). 
Configuring RFC-2544 Responder 
 To use the RFC-2544 responder: 
1. In MiNID, create a MEP with the appropriate MD level, MA ID, and VLAN (refer to OAM (CFM)  
for details on configuring MEPs). 
2. To start the RFC-2544 test, send LBM frames towards the MEP in the desired rate, with the MD 
level, MA ID, and VLAN that correspond to the MEP. 
3. To start RFC-2544 latency tests, send DMM frames towards the MEP, with the MD level, MA ID, 
and VLAN that correspond to the MEP. 