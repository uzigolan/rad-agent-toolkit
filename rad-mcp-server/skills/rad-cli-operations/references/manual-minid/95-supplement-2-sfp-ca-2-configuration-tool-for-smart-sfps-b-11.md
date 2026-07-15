# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – B.11 Testing Device Reset

*Manual `MiNID_ver_2_6_mn.pdf`, pages 395–402.*


## Estimated Duration  *(p.395)*


## Setup and Configuration  *(p.395)*

B. Test Plan 
 
# 
Action 
Expected Result 
Result 
1 
Set local ETX as master clock  
 
 
2 
Set remote ETX as slave clock with 
clock source Ethernet port 2 
Verify the local and remote ETX are locked 
 
3 
Set local IPmux to internal clock 
 
 
4 
Set remote IPmux to loopback clock 
 
 
5 
In UUT1, set the Sync-E clock source 
to the MSA port  
After five minutes, verify that the connection statistics 
in the remote IPmux do not indicate errors  
 
6 
Set local ETX as slave clock with 
clock source Ethernet port 2  
 
 
7 
Set remote ETX as master clock 
Verify the local and remote ETX are locked 
 
8 
Set local IPmux to loopback clock 
 
 
9 
Set remote IPmux to internal clock 
 
 
10 
In UUT1, set the Sync-E clock source 
to the SFP port  
After five minutes, verify that the connection statistics 
in the local IPmux do not indicate errors 
 
 
B.11 Testing Device Reset 
This test verifies the correct execution of device reboot, and verifies that all configured entities operate 
properly after the reboot. 
Estimated Duration 
The estimated duration of this test is one hour. 
Setup and Configuration 
See Connecting the Test Layout and Configuring Devices. 

## Test Procedure  *(p.396)*

B. Test Plan
Test Procedure 
# 
Action 
Expected Result 
Result 
1 
Save the UUT configuration 
File is saved successfully 
2 
Upload configuration file 
File is uploaded 
successfully 
3 
Verify that traffic is running 
through all relevant ports 
Traffic is running without 
errors or packet loss  
4 
Reboot UUT 
•
UUT retains its
configuration after
the reboot
•
The device responds
to pings
•
Management access
(Telnet/SSH)has been
restored
Traffic is running 
error-free. 
5 
Upload the device configuration 
file, and compare it to the 
configuration file uploaded 
before the reboot 
The uploaded 
configuration files before 
and after the reboot are 
the same 
Drilling Template for Wall Installation 
-
SFP.CA-2 
Configuration Tool for Smart SFPs 
Product page > 
Controlled Availability 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Supplement 
SFP-CA.2 is a desktop adapter that is used for configuration of miniature devices such as smart SFPs and MiNID. The adaptor operates 
under the following environmental conditions: 
• Storage temperature: -40 to 85⁰C 
• Operating temperature: 0 to 37⁰C 
• Humidity: up to 90% 
You can perform the following operations with the miniature device connected to your PC via the SFP-CA.2 unit: 
• Assign a new IP address to the smart SFP/MiNID device  
• Configure the smart SFP/MiNID device 
• Download new software to the smart SFP/MiNID device  
This figure Illustrates the SFP-CA.2 unit and its connections. 
 
 
 
Note 
All SFP-CA.2 modules have the same MAC address (00-00-E8-00-00-01).  
 
For SFP-CA.2 to work, you must use one of the following supported operating systems: 
• Windows XP 
• Windows 7 
• Windows 8 
• Windows 8.1 
• Windows 10 
• Windows 11 
Note 
Both 32 bit and 64 bit operating systems are supported. 
You must perform the following before you can use SFP-CA.2: 
1. Install SFP-CA.2 driver (see Installing Driver for SFP-CA.2) 
2. Configure PC network parameters for communication with SFP-CA.2 (see Configuring PC Network Parameters for Communication with 
SFP-CA.2) 
3. Configure HyperTerminal parameters (only required for downloading software to the miniature device) (see Configuring HyperTerminal 
Parameters). 
SFP.CA-2 
Configuration Tool for Smart SFPs 
 
 
 
 
 
 
2 
INSTALLING DRIVER FOR SFP-CA.2 
Before you can use SFP-CA.2, you must install its driver. 
 
To install the SFP-CA.2 driver: 
1. Click the SFP-CA.2 driver links below: 
• 
USB UART drivers 
• 
USB Ethernet drivers 
2. Log in to the site. 
A dialog box is displayed requesting to save the file. 
3. Click Save. 
4. Open the .zip file to install the driver. 
The SFP-CA.2 driver is installed in the background. No further action is required to install the driver. 
CONFIGURING PC NETWORK PARAMETERS FOR COMMUNICATION WITH SFP-CA.2  
You must configure the relevant network parameters of your PC to establish a communication link with SFP-CA.2 and the smart SFP/MiNID 
device.  
Note 
Before performing this procedure, ensure that you have installed the SFP-CA.2 driver, as described in 
Installing Driver for SFP-CA.2. 
 
To configure your PC for communication with SFP-CA.2 and smart SFP/MiNID device: 
1. Connect power to the SFP-CA.2 unit with smart SFP/MiNID plugged in. 
The RDY LED on SFP-CA.2 lights up. The smart SFP DIP switch must be in DB INIT\CONFIG or NORMAL mode. 
2. Plug the USB connector of SFP-CA.2 into a USB port on your PC. 
New Hardware is Detected notice appears. SFP-CA.2 is identified as a new network. 
3. Navigate to My Network Places(WinXP)/Network and Sharing Center(Win7/Win8). 
A new network connection appears in the list of network connections. 
The dialog box closes and your settings are applied. 
4. Type in the network properties. 
5. In the Internet Protocol (TCP/IP) field, configure the IP address, subnet mask and default gateway: 
• 
IP Address: 192.168.205.20 
• 
Subnet Mask: 255.255.255.0 
• 
Default Gateway: 192.168.205.1 
6. Click OK. 
7. Close My Network Places. 
The PC communication link with SFP-CA.2 and the miniature device is ready. 
CONFIGURING HYPERTERMINAL PARAMETERS 
You must establish a HyperTerminal connection, including configuring the serial (COM) port, in order to use the HyperTerminal application 
to download software to the smart SFP/MiNID device. 
 
Note 
• 
Before performing this procedure, ensure that you have installed the SFP-CA.2 driver and 
configured the PC network parameters, as described in Installing Driver for SFP-
CA.2 and Configuring PC Network Parameters for Communication with SFP-CA.2. 
• 
Do not connect the smart SFP/MiNID device to SFP-CA.2 during this procedure. 
 
To configure the HyperTerminal parameters: 
1. 
If the SFP-CA.2 unit is not connected to your PC, connect power to SFP-CA.2 and plug the USB connector of SFP-CA.2 into a USB 
port on your PC. 
2. Open the HyperTerminal application. 
SFP.CA-2 
Configuration Tool for Smart SFPs 
 
 
 
 
 
 
3 
The Connection Description dialog box for a new connection appears. 
3.  Specify a name for the HyperTerminal connection, and click OK. 
The Connect To dialog box appears. 
4. Choose a virtual COM port, for example COM8, and click OK. 
The COM Properties dialog box appears. 
5. Specify the settings as listed below and then click OK. 
• 
Bits Per Second: 115200 
• 
Data Bits: 8 
• 
Parity: None 
• 
Stop Bits: 1 
• 
Flow Control: None. 
6. Click Properties. 
The Connection Properties dialog box appears. 
7. Select the Settings tab and under Emulation, choose VT100, and then click OK. 
The COM port configuration is complete, and the HyperTerminal connection is ready for use.  
8. Close the HyperTerminal application. 
ASSIGNING A NEW IP ADDRESS TO SMART SFPS/MINID 
You can configure the smart SFP/MiNID via SFP-CA.2, including assigning it a new IP address. 
 
Note 
Before performing this procedure, ensure that you have installed the SFP-CA.2 driver and configured 
the PC network parameters, as described in Installing Driver for SFP-CA.2 and Configuring PC 
Network Parameters for Communication with SFP-CA.2. 
 
To assign a new IP address to smart SFP/MiNID: 
1. 
Select Configuration operation mode in the smart SFP/MiNID by setting its DIP switches as needed. Refer to the smart SFP/MiNID 
documentation for details on setting the operation mode. 
2. If the SFP-CA.2 unit is not connected to your PC, connect power to SFP-CA.2 and plug the USB connector of SFP-CA.2 into a USB port 
on your PC. 
3. Plug the smart SFP/MiNID into the SFP socket on the opposite side of the SFP-CA.2 unit. 
The smart SFP/MiNID is ready for configuration. 
4. Open the Web browser on your PC and type http://192.168.205.1 into the Web browser’s address field. 
The Opening screen appears. 
5. Click Login. 
The Login screen appears. 
6. Enter the default user name su and the default password 1234 for Superuser access, and then click Submit. 
A menu appears to the left and you are able to configure smart SFP/MiNID. 
7. Use the menus of the smart SFP/MINID to assign a new IP address. You may continue specifying additional parameters or connect to 
the smart SFP/MiNID from any PC on your network at a later stage, using the newly assigned IP address. 
 
Note 
When Configuration mode is selected in smart SFP/MiNID via the DIP switches, the miniature device 
responds to only the default IP address 192.168.205.1, even if the device’s IP address has been 
changed. 
 
DOWNLOADING SOFTWARE TO SMART SFP/MINID 
You can upgrade the smart SFP/MiNID software by downloading software via SFP-CA.2. The HyperTerminal application is used for the 
software download. 
 
SFP.CA-2 
Configuration Tool for Smart SFPs 
 
 
 
 
 
 
4 
Note 
Before performing this procedure, ensure that you have installed the SFP-CA.2 driver, configured the 
PC network parameters, and configured the HyperTerminal parameters, as described in Installing 
Driver for SFP-CA.2, Configuring PC Network Parameters for Communication with SFP-CA.2, and 
Configuring HyperTerminal Parameters. 
 
To download software to smart SFP/MiNID: 
1. Verify that the upgrade image file is accessible from your PC. 
2. Select SW Download (SW DNLD) mode in the smart SFP/MiNID by setting its DIP switches as needed. Refer to the smart SFP/MiNID 
documentation for details on setting the operation mode.  
3. If the SFP-CA.2 unit is not connected to your PC, connect power to SFP-CA.2 and plug the USB connector of SFP-CA.2 into a USB port on 
your PC. 
4. Plug the miniature device into the SFP socket on the SFP-CA.2 unit. 
5. Open the HyperTerminal application and load the HyperTerminal connection that you established previously (refer to Configuring 
HyperTerminal Parameters). 
6. Follow the smart SFP/MiNID device procedure for downloading software. Refer to the smart SFP/MiNID documentation for details.  
REMOVING SMART SFP/MINID AND SFP-CA.2 FROM PC 
 
To remove smart SFP/MiNID and SFP-CA.2 from the PC: 
1. Close all relevant management applications. 
2. On your operation system, allocate the remove hardware icon. 
3. Select the required USB port from the listed devices and click Stop. 
 
Note 
If you disconnect the smart SFP/MiNID and/or SFP-CA.2 before releasing it as described, your PC may 
stop responding. 
 
4. Push the release button at the front of the smart SFP/MiNID device to disconnect it from SFP-CA.2. 
5. Remove the smart SFP/MiNID from the SFP socket on SFP-CA.2. 
6. Disconnect SFP-CA.2 from the PC and from the power. 
SFP.CA-2 
Configuration Tool for Smart SFPs 
 
 
 
 
 
 
International Headquarters 
24 Raoul Wallenberg St., Tel Aviv 6971920, Israel 
Tel/Fax 972-52-4748272 | Fax 972-3-6498250 
Email market@rad.com 
North American Headquarters 
900 Corporate Drive, Mahwah, NJ 07430, USA 
Tel 201-529-1100 | Toll Free: 800-444-7234 | Fax: 201-529-5777 
Email market@radusa.com 
 
 
www.rad.com 
412-203-08/25 (2.0) Specifications are subject to change without prior notice. © 1988–2025 RAD Data Communications Ltd. The RAD name, logo, logotype, and the product 
names Airmux, IPmux, MiNID, MiCLK, Optimux, and SecFlow are registered trademarks of RAD Data Communications Ltd. All other trademarks are the property of their 
respective holders. 
 
 