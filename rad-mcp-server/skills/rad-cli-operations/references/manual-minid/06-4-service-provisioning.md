# 4 Service Provisioning

*Manual `MiNID_ver_2_6_mn.pdf`, pages 89–91.*


## 4.1 Ethernet Service  *(p.89)*


## 4.2 Service Summary  *(p.89)*

4.1 Ethernet Service 
To create an Ethernet service via MiNID, you need to define how MiNID should handle each type of 
traffic by configuring service flows. See Traffic Processing. 
4.2 Service Summary 
You can display the associations between service names and their associated flows/MAs. 
Benefits 
Viewing the associated entities of service names is useful for service administration, and to ensure 
correct discovery of service-related entities by network management systems. 
Functional Description 
If you have defined service names for flows and MAs (see Service Demarcation and Configuring MAs, 
respectively), you can display the flows/MAs associated with the service names. 
Viewing Service Summary 
In the Web interface, you can view a summary per service name of the associated flows/MAs; in the CLI 
interface, you can view a summary of all service names and their associated flows/MAs. 
4. Service Provisioning 
 To view the service summary: 
Do one of the following: 
• 
In the web interface, go to Configuration > Physical Port > Flows Classification > Config Flow or 
Configuration > OAM > CFM (see Monitoring and Diagnostics), and click the service name for 
which you would like to view the associated flows/MAs. 
MiNID 
  
 
 
 Configuration Physical Port>Flows>Flow(11)>Service Info 
  
 
 
 Service ID Name 
Gold 
 
 Flow 
 
 
 Name: 
22 
 
 Status: 
Enable 
 
 
Classifier: 
match vlan-min 0 pbit-min 5 vlan-max 4095 pbit-max 
5 
 
 Ingress Port: 
SFP/port 1 
 
  
 
 
 Name: 
11 
 
 Status: 
Enable 
 
 
Classifier: 
match vlan-min 0 pbit-min 5 vlan-max 4095 pbit-max 
5 
 
 Ingress Port: 
MSA/port 2 
 
  
 
 
 MA 
 
 
 MD Level: 
2 
 
 MA Name: 
MA4 
 
  
 
 
Service Summary 
• 
In the CLI, go to the configure service context, and enter: 
show summary 
For example: 
# show summary 
service name:     Gold 
===================================== 
Flow     | 
---------- 
4. Service Provisioning 
    :22 
    :11 
 
---------- 
MA       | 
---------- 
    :MA5 
 
 
 