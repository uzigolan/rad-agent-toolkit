# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 10.3 Inventory

*Manual `MiNID_ver_2_6_mn.pdf`, pages 235–236.*


## Standards Compliance  *(p.235)*


## Benefits  *(p.235)*


## Displaying Inventory Information  *(p.235)*

10. Administration 
Active    Status: Exist Version: 2.4.0(0.37)  
SW-PACK 1 Status: Exist Version: 2.4.0(0.37) Date: 21-06-2016 
SW-PACK 2 Status: Exist Version: 2.1.0(0.53) Date: 17-05-2015 
 To display the contents of the startup or user configuration files: 
• 
At the file# prompt, enter one of the following: 
 
show startup-config 
 
show user-default-config 
The contents of the specified configuration file are displayed. 
10.3 Inventory 
You can view the MiNID inventory table, displaying the unit’s description, hardware and software 
revisions, as well as the device serial number (S\N). 
Standards Compliance 
RFC 4133: Entity MIB 
Benefits 
You can monitor the installed components and hardware and software revisions. 
Displaying Inventory Information 
 To display the inventory table: 
Do one of the following: 
• 
In the web interface, go to Inventory: 
  
10. Administration 
MiNID 
 Inventory 
  
 
 
 Name 
 
MiNID.Chassis 
 Description 
 
RAD.MiNID.Chassis 
 Hw version 
 
1.2\1.1 [GE] 
 Board Type 
 
MiNID SFP / MiNID Sleeve / 
 CSL 
 
D 
 FP Rev 
 
2016-04-17(99) 
 CP Rev 
 
2015-06-01(0.2) 
 FW Rev 
 
2016-03-16(0) 
 SW Rev 
 
2.4.1(0.03) [PLATINUM \ DEMARC] 
 BootVer 
 
2.0.0(0.12) 
 SW Date\Time 
 
Sep 18 2016\15:51:56 
 S\N 
 
1234567890ABCDEF 
  
 
 
• 
In the CLI, in the root context enter: 
inventory 
For example: 
MiNID# inventory 
                Inventory 
[--------------------------------------] 
Name:           MiNID.Chassis 
Description:    RAD.MiNID.Chassis 
HW Rev:         1.2\1.1 [GE] 
CSL:            D 
Board Type:     MiNID Sleeve 
FP Rev :        2016-06-26(101) 
CP Rev :        2016-09-05(0.4) 
FW Rev :        2016-06-14(0) 
SW Rev:         2.6.0(0.07) [PLATINUM] 
BootVer:        2.0.0(0.12) 
SW Date\Time:   Sep 18 2018\15:51:56 
S\N:            1234567890ABCDEF 
[--------------------------------------] 