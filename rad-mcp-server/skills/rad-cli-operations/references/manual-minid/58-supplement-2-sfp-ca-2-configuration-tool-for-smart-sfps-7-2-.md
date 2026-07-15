# Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 7.2 Functional Description

*Manual `MiNID_ver_2_6_mn.pdf`, pages 138–138.*


## Supplement 2 SFP.CA-2 Configuration Tool for Smart SFPs – 7.2 Functional Description  *(p.138)*

7 Resiliency (Fault Propagation) 
Fault propagation enables you to specify what actions to take when failure indication is received by one 
of the MiNID ports, e.g. whether to pass on the failure indication to the other MiNID port or block it.  
Note 
If no fiber is connected to the MSA (SFP sleeve option) port, ensure that all 
fault propagation actions are disabled (this is the default setting). 
7.1 Standards Compliance 
Loss of Signal (LOS), Tx fault, and Tx disable are defined in the CFP Multi-Source Agreement. 
7.2 Functional Description 
MiNID handles the following failure indications: 
• 
LOS received by the SFP port –indicates loss of signal, for instance it can be caused by 
disconnecting the fiber from the SFP that is inserted in MiNID. 
You can configure MiNID to do any of the following upon receiving LOS from the provider-side 
SFP port, depending on the ordering option: 
 
SFP sleeve: 
 
Propagate LOS to the customer-side MSA port 
 
Disable the physical interface (PHY) towards the host 
 
Send OAM CFM AIS to the MSA port (in this case it is recommended to configure a MEP 
with ingress port MSA, in order to transfer the AIS to the remote MEP) 
Note 
• 
You can enable sending AIS only if propagating LOS and disabling host 
PHY are both disabled, and you must disable sending AIS in order to 
enable propagating LOS or disabling host PHY 
• 
If you wish to block the LOS, you should disable all three actions. 