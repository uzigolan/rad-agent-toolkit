# Feature Reference – 8 Monitoring and Diagnostics – 8.15 Frequently Asked Questions

*Manual `Etx-2i_6.8.5_1.150_MN_06-26_GA.pdf`, pages 1572–1573.*


## Feature Reference – 8 Monitoring and Diagnostics – 8.15 Frequently Asked Questions  *(p.1572)*

ETX-2i Devices 
8. Monitoring and Diagnostics 
8.15 Frequently Asked Questions 
Q How should ETX‑2i be configured for management? 
A You need to configure a router interface for management by assigning it an IP address and 
binding it to an SVI for which management flows have been configured. Additionally, you need 
to configure the default gateway address in the router.  
Q If I change the functional mode of a network Ethernet port to user, what happens to the 
associated flows? 
A When you change the functional mode, all flows related to the port are deleted. 
Q How can one optimize Transmission Control Protocol (TCP) based throughput tests in L2 
switch products? 
A TCP, a reliable transmission mechanism, uses an acknowledge mechanism and retransmissions. 
The TCP transmit procedure uses a Tx window (number of bytes that can be transmitted before 
getting an acknowledgement), which is dynamic and increases with time. Note that a larger 
window size means higher bursts and higher throughput. TCP also has backoff mechanisms that 
restart the window size as a result of network packet loss. 
From the above, the following is apparent: 
 
TCP (transmit window) has a bursty nature. 
 
Packet loss affects TCP throughput (backs off to smaller window size and restarts window 
increase). 
 
Burst tolerant mechanisms can improve TCP throughput. 
You can improve TCP throughput in the following ways: 
 
If a Policer is configured in the data path, use a larger CBS (so that the Policer allows higher 
bursts). See the first configuration example below. 
 
Use larger egress queues for better burst tolerance. See the second configuration example 
below. 
Configuration Examples 
Increased CBS: 
config qos  
        policer-profile "1G"  
            bandwidth cir 1000000 cbs 1500  
        exit 
        policer-profile "750M"  
            bandwidth cir 750000 cbs 1500 eir 850000  
        exit 
ETX-2i Devices 
8. Monitoring and Diagnostics 
Increased queue depth and frame-buffers: 
config qos          
        queue-block-profile "QB1"  
            queue 0  
                scheduling strict  
                depth 6000000  
                frame-buffers 3000  
            exit all                      
#       Queue Group Configuration 
config qos 
        queue-group-profile "QG1"             
            queue-block 0/1  
                profile "QB1"                  
            exit all             
#       Ethernet - Port Configuration 
config port  
   ethernet 0/3            
            queue-group profile "QG1"  
        exit all 
config port  
   ethernet 0/5           
            queue-group profile "QG1"         
 
 