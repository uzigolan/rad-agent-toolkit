# 13 Application Tutorial

*Manual `SecFlow-1p_6.4_Mn_05-26_GA.pdf`, pages 743–771.*


## (chapter introduction)  *(p.743)*

13. Application Tutorial 
Configuring the Service 
2. 
Configure  as follows: 
    configure 
        echo "Terminal Configuration" 
#       Terminal Configuration 
        terminal 
            no serial-port-console 
        exit 
        echo "System Configuration" 
#       System Configuration 
        system 
            date-and-time 
                echo "NTP (Network Time Protocol)" 
#               NTP (Network Time Protocol) 
                ntp 
                    server 1 
                        address 172.17.171.141 
                        prefer 
                        no shutdown 
                    exit 
                exit 
            exit 
            echo "Serial port global configuration level" 
#           Serial port global configuration level 
            serial 
                terminal-server 
                    buffer-mode frame 
                    no shutdown 
                exit 
            exit 
        exit 
        access-control 
            access-list "lte" 
                permit icmp any any sequence 10 
                permit tcp 94.188.177.132 95.35.55.118 32000 sequence 50 
            exit 
            access-list "mng" 
                permit tcp 172.17.190.38 172.17.191.111 443 sequence 20 
                permit tcp 172.17.190.38 172.17.191.111 22 sequence 40 
                permit udp 172.17.171.141 123 172.17.191.111 sequence 50 
                permit tcp 172.17.190.121 172.17.191.111 22 sequence 60 
            exit 
            access-list "rtu" 
                permit tcp 192.168.2.100 94.188.177.132 established sequence 20 
            exit 
        exit 
        echo "Management configuration" 
#       Management configuration 
        management 
            login-user "netconf-su" 
13. Application Tutorial 
                password 
"n/4MO9kiMveW.X56$X5pBIRMaY72dseiCGlenjgdZmYGagAze4yvIgl7hHAl3j4zmJs8LER0VfXH5a7rgS.CztQl2k5s3
hXR6Sk2mq1" hash 
                shutdown 
            exit 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                snmp-engine-id mac 18-06-F5-C5-9E-35 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            ethernet 3 
                no shutdown 
            exit 
            ethernet 5 
                access-group "mng" inbound 
                no shutdown 
            exit 
            ethernet 6 
                no shutdown 
            exit 
            echo "Cellular - Port Configuration" 
#           Cellular - Port Configuration 
            cellular lte 
                access-group "lte" inbound 
                no shutdown 
            exit 
            echo "PPP - Port Configuration" 
#           PPP - Port Configuration 
            ppp 1 
                name "PPP 1" 
                no bind 
            exit 
            echo "Serial port level" 
#           Serial port level 
            serial 1 
                no shutdown 
                terminal-server 1 
                    local-address 95.35.55.118 
                    telnet-server-tcp port 32000 
                exit 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 1 
                bind cellular lte 
                dhcp 
                dhcp-client 

## 13.2 Terminal Sever (IP to Serial) over IPsec over LTE  *(p.745)*

13. Application Tutorial 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 5 
                address 172.17.191.111/24 
                bind ethernet 5 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 10 loopback 
                address 10.1.1.1/32 
                no shutdown 
            exit 
            interface 32 
                address 169.254.1.1/16 
                bind ethernet 6 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 172.17.171.0/24 address 172.17.191.1 metric 1 
            static-route 172.17.190.0/24 address 172.17.191.1 metric 1 
        exit 
    exit 
save 
13.2 Terminal Sever (IP to Serial) over IPsec over LTE 
This application can be implemented for RTUs with no IP connection support (RS-232 port only). 
SecFlow-1p converts IP packets (Scada Server) to RS-232 serial connection (RTU). 
13. Application Tutorial 
 
Note: Adjust the IP addresses according to your application requirements. 
Equipment List 
Product Name 
Description 
H/W 
Version 
S/W 
Version 
SF-1P/E1/DC/4U2S/1RS/L1 
Type 2 Router, DC PS, 4 UTP, 2 SFP, 1 Serial and LTE 
0.4 
5.4.0.62.20 
PF-2/ETR/48VDC/2SFP/4PU 
48VDC, 2x 100/1000Base-X SFP, 4x 10/100/1000Base-T  
1.2  
1.121 
Installing SecFlow-1p 
Use the relevant chapters for installation, power connection and device management instructions. 
It is assumed that all the devices are configured to factory default (use the admin factory-default 
command). 
Configuring the Service 
3. 
Configure SecFlow-1p as follows: 
    configure 
        echo "Terminal Configuration" 
#       Terminal Configuration 
        terminal 
13. Application Tutorial 
            no serial-port-console 
        exit 
        echo "System Configuration" 
#       System Configuration 
        system 
            name "Remote_1" 
            date-and-time 
                echo "NTP (Network Time Protocol)" 
#               NTP (Network Time Protocol) 
                ntp 
                    server 1 
                        address 172.17.171.141 
                        prefer 
                        no shutdown 
                    exit 
                exit 
            exit 
            echo "Serial port global configuration level" 
#           Serial port global configuration level 
            serial 
                terminal-server 
                    buffer-mode frame 
                    no shutdown 
                exit 
            exit 
        exit 
        access-control 
            access-list "lte" 
                permit icmp any any sequence 10 
                permit ip 95.35.55.33 95.35.55.118 sequence 50 
            exit 
            access-list "mng" 
                permit tcp 172.17.190.38 172.17.191.111 443 sequence 20 
                permit tcp 172.17.190.38 172.17.191.111 22 sequence 40 
                permit udp 172.17.171.141 123 172.17.191.111 sequence 50 
                permit tcp 172.17.190.121 172.17.191.111 22 sequence 60 
            exit 
            access-list "data-acl" 
                permit ip any any sequence 10 
            exit 
        exit 
        crypto 
            ipsec-transform-set "RAD" 
                algorithms esp-aes-gcm-256 
            exit 
            isakmp-key 
"77C6291611AE6632E5AA2454A52B87A3E331A04DF16D459B0601428B988D9D394740488D7D91687D7B24444C0E444
DA047290821529F617538D048DD09749FDB43CBEBDCFCB28E7143AB7C4C7240BBB2" address 95.35.55.33 hash 
            isakmp-policy 1 
                group 14 
                hash sha2-512 
            exit 
13. Application Tutorial 
            crypto-map "lincoln" 
                match-address "data-acl" 
                peer-address 95.35.55.33 
                pfs-group 14 
                transform-set "RAD" 
                ike-identity-local address 95.35.55.118 
                ike-identity-local-x509 distinguished-name 
                ike-identity-remote address 95.35.55.33 
                ike-identity-remote-x509 any 
                ike-version 2 
            exit 
        exit 
        echo "Management configuration" 
#       Management configuration 
        management 
            login-user "netconf-su" 
                shutdown 
            exit 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                snmp-engine-id mac 18-06-F5-B4-0F-AC 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            ethernet 5 
                no shutdown 
            exit 
            ethernet 6 
                no shutdown 
            exit 
            echo "Cellular - Port Configuration" 
#           Cellular - Port Configuration 
            cellular lte 
                access-group "lte" inbound 
                no shutdown 
            exit 
            echo "Serial port level" 
#           Serial port level 
            serial 1 
                baud-rate 19200 
                no shutdown 
                terminal-server 1 
                    local-address 192.168.2.100 
                    telnet-server-tcp port 32000 
                exit 
            exit 
        exit 
        router 1 
            name "Router#1" 
13. Application Tutorial 
            interface 1 
                bind cellular lte 
                dhcp 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 2 
                address 192.168.2.100/24 
                bind ethernet 3 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
 
 
    interface 5 
                address 172.17.191.111/24 
                bind ethernet 5 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 32 
                address 169.254.1.1/16 
                bind ethernet 6 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 95.35.55.33/32 interface 1 metric 1 
            static-route 172.17.171.0/24 address 172.17.191.1 metric 1 
            static-route 172.17.190.0/24 address 172.17.191.1 metric 1 
            echo "BGP configuration" 
#           BGP configuration 
            bgp 4100 
                router-id 10.1.40.2 
                no shutdown 
                echo "BGP Neighbor Configuration" 
#               BGP Neighbor Configuration 
                neighbor 10.1.40.1 
                    remote-as 4100 
                    no shutdown 
                exit 
                echo "IPv4 Unicast Address Family Configuration" 
#               IPv4 Unicast Address Family Configuration 
                ipv4-unicast-af 
                    echo "IPv4 Unicast Address Family - Neighbor Configuration" 
#                   IPv4 Unicast Address Family - Neighbor Configuration 
                    neighbor 10.1.40.1 

## 13.3 Point-to-Point Automation over IPsec over LTE  *(p.750)*

13. Application Tutorial 
                        active 
                    exit 
                exit 
                echo "IPv6 Unicast Address Family Configuration" 
#               IPv6 Unicast Address Family Configuration 
                ipv6-unicast-af 
                    echo "IPv6 Unicast Address Family - Neighbor Configuration" 
#                   IPv6 Unicast Address Family - Neighbor Configuration 
                    neighbor 10.1.40.1 
                    exit 
                exit 
            exit 
            tunnel-interface 1 ipsec 
                tunnel-source router-interface 1 
                tunnel-destination 95.35.55.33 
                ip-address static 10.1.40.2/24 
                crypto-map "lincoln" 
                no shutdown 
            exit 
        exit 
    exit 
13.3 Point-to-Point Automation over IPsec over LTE 
This application can be implemented for RTUs with IP connection support (over IPsec over LTE).  
 
Note: Adjust the IP addresses according to your application requirements. 
13. Application Tutorial 
Equipment List 
Product Name 
Description 
H/W 
Version 
S/W 
Version 
SF-1P/E1/DC/4U2S/1RS/L1 
Type 2 Router, DC PS, 4 UTP, 2 SFP, 1 Serial and LTE 
0.4 
5.4.0.62.20 
PF-2/ETR/48VDC/2SFP/4PU 
48VDC, 2x 100/1000Base-X SFP, 4x 10/100/1000Base-T  
1.2  
1.121 
Installing SecFlow-1p and PowerFlow-2 
Use the relevant manual chapters for installation, power connection and device management 
instructions. 
It is assumed that all the devices are configured to factory default (use the admin factory-default 
command). 
Configuring the Service 
4. 
Configure  as follows: 
    configure 
        echo "Terminal Configuration" 
#       Terminal Configuration 
        terminal 
            no serial-port-console 
        exit 
        echo "System Configuration" 
#       System Configuration 
        system 
            name "Remote_1" 
            date-and-time 
                echo "NTP (Network Time Protocol)" 
#               NTP (Network Time Protocol) 
                ntp 
                    server 1 
                        address 172.17.171.141 
                        prefer 
                        no shutdown 
                    exit 
                exit 
            exit 
            echo "Serial port global configuration level" 
#           Serial port global configuration level 
            serial 
                terminal-server 
13. Application Tutorial 
                    buffer-mode frame 
                    no shutdown 
                exit 
            exit 
        exit 
        access-control 
            access-list "lte" 
                permit icmp any any sequence 10 
                permit ip 95.35.55.33 95.35.55.118 sequence 50 
            exit 
            access-list "mng" 
                permit tcp 172.17.190.38 172.17.191.111 443 sequence 20 
                permit tcp 172.17.190.38 172.17.191.111 22 sequence 40 
                permit udp 172.17.171.141 123 172.17.191.111 sequence 50 
                permit tcp 172.17.190.121 172.17.191.111 22 sequence 60 
            exit 
            access-list "rtu" 
                permit tcp 192.168.2.100 10.10.10.100 established sequence 20 
                permit tcp 10.2.1.1 10.10.10.100 established sequence 30 
 
 
 
 
permit icmp any any sequence 40 
            exit 
            access-list "data-acl" 
                permit ip any any sequence 10 
            exit 
        exit 
        crypto 
            ipsec-transform-set "RAD" 
                algorithms esp-aes-gcm-256 
            exit 
            isakmp-key 
"77C6291611AE6632E5AA2454A52B87A3E331A04DF16D459B0601428B988D9D394740488D7D91687D7B24444C0E444
DA047290821529F617538D048DD09749FDB43CBEBDCFCB28E7143AB7C4C7240BBB2" address 95.35.55.33 hash 
            isakmp-policy 1 
                group 14 
                hash sha2-512 
            exit 
            crypto-map "lincoln" 
                match-address "data-acl" 
                peer-address 95.35.55.33 
                pfs-group 14 
                transform-set "RAD" 
                ike-identity-local address 95.35.55.118 
                ike-identity-local-x509 distinguished-name 
                ike-identity-remote address 95.35.55.33 
                ike-identity-remote-x509 any 
                ike-version 2 
            exit 
        exit 
        echo "Management configuration" 
#       Management configuration 
        management 
            login-user "netconf-su" 
13. Application Tutorial 
                shutdown 
            exit 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                snmp-engine-id mac 18-06-F5-B4-0F-AC 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            ethernet 3 
                vlan 10 
                    no shutdown 
                exit 
                vlan 20 
                    no shutdown 
                exit 
                access-group "rtu" inbound 
                no shutdown 
            exit 
            ethernet 5 
                no shutdown 
            exit 
            ethernet 6 
                no shutdown 
            exit 
            echo "Cellular - Port Configuration" 
#           Cellular - Port Configuration 
            cellular lte 
                access-group "lte" inbound 
                no shutdown 
            exit 
            echo "Serial port level" 
#           Serial port level 
            serial 1 
                baud-rate 19200 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 1 
                bind cellular lte 
                dhcp 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 2 
                dhcp-client 
                    client-id mac 
13. Application Tutorial 
                exit 
                shutdown 
            exit 
            interface 3 
                address 192.168.2.200/24 
                bind ethernet 3 vlan 20 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 5 
                address 172.17.191.111/24 
                bind ethernet 5 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 11 
                address 10.2.1.100/24 
                bind ethernet 3 vlan 10 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 32 
                address 169.254.1.1/16 
                bind ethernet 6 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 10.2.1.0/24 address 10.2.1.1 metric 1 
            static-route 95.35.55.33/32 interface 1 metric 1 
            static-route 172.17.171.0/24 address 172.17.191.1 metric 1 
            static-route 172.17.190.0/24 address 172.17.191.1 metric 1 
            static-route 192.168.2.0/24 interface 3 metric 1 
            echo "BGP configuration" 
#           BGP configuration 
            bgp 4100 
                router-id 10.1.40.2 
                no shutdown 
                echo "BGP Neighbor Configuration" 
#               BGP Neighbor Configuration 
                neighbor 10.1.40.1 
                    remote-as 4100 
                    no shutdown 
                exit 
                echo "IPv4 Unicast Address Family Configuration" 
13. Application Tutorial 
#               IPv4 Unicast Address Family Configuration 
                ipv4-unicast-af 
                    network 10.2.1.0/24 
                    network 192.168.2.0/24 
                    echo "IPv4 Unicast Address Family - Neighbor Configuration" 
#                   IPv4 Unicast Address Family - Neighbor Configuration 
                    neighbor 10.1.40.1 
                        active 
                    exit 
                exit 
                echo "IPv6 Unicast Address Family Configuration" 
#               IPv6 Unicast Address Family Configuration 
                ipv6-unicast-af 
                    echo "IPv6 Unicast Address Family - Neighbor Configuration" 
#                   IPv6 Unicast Address Family - Neighbor Configuration 
                    neighbor 10.1.40.1 
                    exit 
                exit 
            exit 
            tunnel-interface 1 ipsec 
                tunnel-source router-interface 1 
                tunnel-destination 95.35.55.33 
                ip-address static 10.1.40.2/24 
                crypto-map "lincoln" 
                no shutdown 
            exit 
        exit 
    exit 
5. 
Configure PowerFlow-2 as follows: 
PowerFlow2# show running-config 
Building configuration... 
hostname PowerFlow2 
username su privilege 15 password encrypted MTIzNA== 
! 
vlan 1,10 
! 
! 
! 
! 
ip route 0.0.0.0 0.0.0.0 10.2.1.100 
spanning-tree mst name 00-20-d2-ba-30-72 revision 0 
snmp-server contact Name of contact person 
snmp-server location The location of this device 
! 
interface GigabitEthernet 1/1 
 switchport trunk native vlan 10 
 switchport trunk allowed vlan 10,20,30,40,50 
 switchport trunk vlan tag native 
 switchport mode trunk 
 no pvlan 1 
 pvlan 10 
13. Application Tutorial 
! 
interface GigabitEthernet 1/2 
 switchport access vlan 20 
 switchport hybrid native vlan 20 
 switchport hybrid allowed vlan 20 
 switchport hybrid acceptable-frame-type untagged 
 switchport mode hybrid 
 no pvlan 1 
 pvlan 10,20 
! 
interface GigabitEthernet 1/3 
 switchport access vlan 30 
 switchport hybrid native vlan 12 
 switchport hybrid allowed vlan 12 
 switchport hybrid acceptable-frame-type tagged 
 switchport hybrid ingress-filtering 
 switchport hybrid egress-tag all 
 no pvlan 1 
 pvlan 10 
! 
interface GigabitEthernet 1/4 
 switchport access vlan 40 
 switchport hybrid native vlan 13 
 switchport hybrid allowed vlan 13 
 switchport hybrid acceptable-frame-type tagged 
 switchport hybrid ingress-filtering 
 switchport hybrid egress-tag all 
 no pvlan 1 
 pvlan 10 
! 
interface GigabitEthernet 1/5 
 switchport access vlan 50 
 switchport hybrid native vlan 14 
 switchport hybrid allowed vlan 14 
 switchport hybrid acceptable-frame-type tagged 
 switchport hybrid ingress-filtering 
 switchport hybrid egress-tag all 
 no pvlan 1 
 pvlan 10 
! 
interface GigabitEthernet 1/6 
 switchport access vlan 10 
 switchport hybrid native vlan 10 
 switchport hybrid allowed vlan 10 
 switchport hybrid acceptable-frame-type untagged 
 switchport mode hybrid 
 no pvlan 1 
 pvlan 10 
! 
interface GigabitEthernet 1/7 
 switchport access vlan 10 
 no pvlan 1 
13. Application Tutorial 
 pvlan 10 
! 
interface GigabitEthernet 1/8 
 switchport access vlan 10 
 no pvlan 1 
 pvlan 10 
! 
interface GigabitEthernet 1/9 
 switchport access vlan 10 
 no pvlan 1 
 pvlan 10 
! 
interface GigabitEthernet 1/10 
 switchport access vlan 10 
 no pvlan 1 
 pvlan 10 
! 
interface GigabitEthernet 1/11 
 no pvlan 1 
 pvlan 9 
! 
interface GigabitEthernet 1/12 
 no pvlan 1 
 pvlan 9 
! 
interface GigabitEthernet 1/13 
! 
interface GigabitEthernet 1/14 
! 
interface GigabitEthernet 1/15 
! 
interface GigabitEthernet 1/16 
! 
interface GigabitEthernet 1/17 
! 
interface GigabitEthernet 1/18 
! 
interface GigabitEthernet 1/19 
! 
interface GigabitEthernet 1/20 
! 
interface GigabitEthernet 1/21 
! 
interface GigabitEthernet 1/22 
! 
interface GigabitEthernet 1/23 
! 
interface GigabitEthernet 1/24 
! 
interface vlan 1 
 no ip address 
! 
13. Application Tutorial 
interface vlan 10 
 ip address 10.2.1.1 255.255.255.0 
! 
! 
spanning-tree aggregation 
 spanning-tree link-type point-to-point 
! 
! 
line console 0 
! 
line vty 0 
! 
line vty 1 
! 
line vty 2 
! 
line vty 3 
! 
line vty 4 
! 
line vty 5 
! 
line vty 6 
! 
line vty 7 
! 
line vty 8 
! 
line vty 9 
! 
line vty 10 
! 
line vty 11 
! 
line vty 12 
! 
line vty 13 
! 
line vty 14 
! 
line vty 15 
! 
en 

## 13.4 Terminal Sever (IP to Serial) over IPSec over LTE and Satellite (Ethernet)  *(p.759)*

13. Application Tutorial 
13.4 Terminal Sever (IP to Serial) over IPSec over LTE and 
Satellite (Ethernet) 
This application can be implemented for RTUs with no IP connection support (RS-232 port only). 
SecFlow-1p converts IP packets (Scada Server) to RS232 serial connection (RTU). 
 
Note: Adjust the IP addresses according to your application requirements. 
Equipment List 
Product Name 
Description 
H/W 
Version 
S/W 
Version 
SF-1P/E1/DC/4U2S/1RS/L1 
Type 2 Router, DC PS, 4 UTP, 2 SFP, 1 Serial and LTE 
0.4 
5.4.0.62.20 
PF-2/ETR/48VDC/2SFP/4PU 
48VDC, 2x 100/1000Base-X SFP, 4x 
10/100/1000Base-T 
1.2  
1.121 
Installing SecFlow-1p and PowerFlow-2 
Use the relevant manual chapters for installation, power connection and device management 
instructions. 
It is assumed that all the devices are configured to factory default (use the admin factory-default 
command). 
13. Application Tutorial 
Configuring the Service 
6. 
Configure  as follows: 
    configure 
        echo "Terminal Configuration" 
#       Terminal Configuration 
        terminal 
            no serial-port-console 
        exit 
        echo "System Configuration" 
#       System Configuration 
        system 
            name "Remote_1" 
            date-and-time 
                echo "NTP (Network Time Protocol)" 
#               NTP (Network Time Protocol) 
                ntp 
                    server 1 
                        address 172.17.171.141 
                        prefer 
                        no shutdown 
                    exit 
                exit 
            exit 
            echo "Serial port global configuration level" 
#           Serial port global configuration level 
            serial 
                terminal-server 
                    buffer-mode frame 
                    no shutdown 
                exit 
            exit 
        exit 
        access-control 
            access-list "lte" 
                permit icmp any any sequence 10 
                permit ip 95.35.55.33 95.35.55.118 sequence 60 
            exit 
            access-list "mng" 
                permit tcp 172.17.190.38 172.17.191.111 443 sequence 20 
                permit tcp 172.17.190.38 172.17.191.111 22 sequence 40 
                permit udp 172.17.171.141 123 172.17.191.111 sequence 50 
                permit tcp 172.17.190.121 172.17.191.111 22 sequence 60 
            exit 
            access-list "rtu" 
                permit tcp 192.168.2.100 10.10.10.100 established sequence 20 
                permit tcp 10.2.1.1 10.10.10.100 established sequence 30 
                permit icmp any any sequence 40 
            exit 
            access-list "data-acl" 
                permit ip any any sequence 10 
13. Application Tutorial 
            exit 
            access-list "satellite" 
                permit icmp any any sequence 10 
                permit tcp 20.20.20.2 20.20.20.1 sequence 20 
                permit tcp 10.10.10.100 192.168.2.100 sequence 30 
            exit 
        exit 
        crypto 
            ipsec-transform-set "RAD" 
                algorithms esp-aes-gcm-256 
            exit 
            isakmp-key 
"77C6291611AE6632E5AA2454A52B87A3E331A04DF16D459B0601428B988D9D394740488D7D91687D7B24444C0E444
DA047290821529F617538D048DD09749FDB43CBEBDCFCB28E7143AB7C4C7240BBB2" address 95.35.55.33 hash 
            isakmp-policy 1 
                group 14 
                hash sha2-512 
            exit 
            crypto-map "lincoln_2" 
                match-address "data-acl" 
                peer-address 95.35.55.33 
                pfs-group 14 
                transform-set "RAD" 
                ike-identity-local address 95.35.55.118 
                ike-identity-local-x509 distinguished-name 
                ike-identity-remote address 95.35.55.33 
                ike-identity-remote-x509 any 
                ike-version 2 
            exit 
        exit 
        echo "Management configuration" 
#       Management configuration 
        management 
            login-user "netconf-su" 
                shutdown 
            exit 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                snmp-engine-id mac 18-06-F5-B4-0F-AC 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            echo "Ethernet - Port Configuration" 
#           Ethernet - Port Configuration 
            ethernet 1 
                name "xDSL" 
                vlan 96 
                    name "ADSL" 
                    no shutdown 
13. Application Tutorial 
                exit 
                vlan 101 
                    name "VDSL" 
                    no shutdown 
                exit 
            exit 
            ethernet 3 
                access-group "rtu" inbound 
                no shutdown 
            exit 
            ethernet 4 
                access-group "satellite" inbound 
                no shutdown 
            exit 
            ethernet 5 
                access-group "mng" inbound 
                no shutdown 
            exit 
            ethernet 6 
                no shutdown 
            exit 
            echo "Cellular - Port Configuration" 
#           Cellular - Port Configuration 
            cellular lte 
                access-group "lte" inbound 
                no shutdown 
            exit 
            echo "PPP - Port Configuration" 
#           PPP - Port Configuration 
            ppp 1 
                no name 
                bind ethernet 1 
                chap-hostname "rad.co.il" 
                chap-password "418756FEF5EEBE3E939B01520075243D" hash 
                ipcp-address 1.0.0.5 
            exit 
            echo "Serial port level" 
#           Serial port level 
            serial 1 
                baud-rate 19200 
                no shutdown 
                terminal-server 1 
                    local-address 192.168.2.100 
                    telnet-server-tcp port 32000 
                exit 
            exit 
        exit 
        router 1 
            name "Router#1" 
            interface 1 
                bind ppp 1 
                dhcp-client 
13. Application Tutorial 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 2 
                bind cellular lte 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 3 
                address 192.168.2.100/24 
                bind ethernet 3 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 4 
                address 20.20.20.1/24 
                bind ethernet 4 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 5 
                address 172.17.191.111/24 
                bind ethernet 5 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 10 loopback 
                address 10.1.1.1/32 
                no shutdown 
            exit 
            interface 32 
                address 169.254.1.1/16 
                bind ethernet 6 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 95.35.55.33/32 interface 2 metric 1 
            static-route 172.17.171.0/24 address 172.17.191.1 metric 1 
            static-route 172.17.190.0/24 address 172.17.191.1 metric 1 
            echo "Router policy configuration - route maps" 
#           Router policy configuration - route maps 
13. Application Tutorial 
            route-map "LOCAL-PREF-80" 
                permit set local-preference 80 sequence 10 
            exit 
            echo "BGP configuration" 
#           BGP configuration 
            bgp 4100 
                router-id 10.1.20.2 
                no shutdown 
                echo "BGP Neighbor Configuration" 
#               BGP Neighbor Configuration 
                neighbor 10.1.20.1 
                    remote-as 4100 
                    no shutdown 
                exit 
                neighbor 20.20.20.2 
                    remote-as 4100 
                    no shutdown 
                exit 
                echo "IPv4 Unicast Address Family Configuration" 
#               IPv4 Unicast Address Family Configuration 
                ipv4-unicast-af 
                    network 10.1.1.1/32 
                    network 10.2.1.0/24 
                    network 192.168.2.0/24 
                    echo "IPv4 Unicast Address Family - Neighbor Configuration" 
#                   IPv4 Unicast Address Family - Neighbor Configuration 
                    neighbor 10.1.20.1 
                        active 
                    exit 
                    neighbor 20.20.20.2 
                        active 
                        route-map-bind "LOCAL-PREF-80" in 
                    exit 
                exit 
                echo "IPv6 Unicast Address Family Configuration" 
#               IPv6 Unicast Address Family Configuration 
                ipv6-unicast-af 
                    echo "IPv6 Unicast Address Family - Neighbor Configuration" 
#                   IPv6 Unicast Address Family - Neighbor Configuration 
                    neighbor 10.1.20.1 
                    exit 
                    neighbor 20.20.20.2 
                    exit 
                exit 
            exit 
            tunnel-interface 2 ipsec 
                tunnel-source router-interface 2 
                tunnel-destination 95.35.55.33 
                ip-address static 10.1.20.2/24 
                crypto-map "lincoln_2" 
                no shutdown 
            exit 

## 13.5 Point-to-Point Automation over IPsec over LTE and Satellite (Ethernet)  *(p.765)*

13. Application Tutorial 
        exit 
    exit 
13.5 Point-to-Point Automation over IPsec over LTE and 
Satellite (Ethernet) 
This application can be implemented for RTUs with IP connection support (over IPsec over LTE and 
satellite). 
 
Note: Adjust the IP addresses according to your application requirements. 
Equipment List 
Product Name 
Description 
H/W 
Version 
S/W 
Version 
SF-1P/E1/DC/4U2S/1RS/L1 
Type 2 Router, DC PS, 4 UTP, 2 SFP, 1 Serial and LTE 
0.4 
5.4.0.62.20 
PF-2/ETR/48VDC/2SFP/4PU 
48VDC, 2x 100/1000Base-X SFP, 4x 
10/100/1000Base-T 
1.2  
1.121 
Installing SecFlow-1p and PowerFlow-2 
Use the relevant manual chapters for installation, power connection and device management 
instructions. 
13. Application Tutorial 
It is assumed that all the devices are configured to factory default (use the admin factory-default 
command). 
Configuring the Service 
7. 
Configure  as follows: 
    configure 
        echo "Terminal Configuration" 
#       Terminal Configuration 
        terminal 
            no serial-port-console 
        exit 
        echo "System Configuration" 
#       System Configuration 
        system 
            name "Remote_1" 
            date-and-time 
                echo "NTP (Network Time Protocol)" 
#               NTP (Network Time Protocol) 
                ntp 
                    server 1 
                        address 172.17.171.141 
                        prefer 
                        no shutdown 
                    exit 
                exit 
            exit 
            echo "Serial port global configuration level" 
#           Serial port global configuration level 
            serial 
                terminal-server 
                    buffer-mode frame 
                    no shutdown 
                exit 
            exit 
        exit 
        access-control 
            access-list "lte" 
                permit icmp any any sequence 10 
                permit ip 95.35.55.33 95.35.55.118 sequence 60 
            exit 
            access-list "mng" 
                permit tcp 172.17.190.38 172.17.191.111 443 sequence 20 
                permit tcp 172.17.190.38 172.17.191.111 22 sequence 40 
                permit udp 172.17.171.141 123 172.17.191.111 sequence 50 
                permit tcp 172.17.190.121 172.17.191.111 22 sequence 60 
            exit 
            access-list "rtu" 
                permit tcp 192.168.2.100 10.10.10.100 established sequence 20 
13. Application Tutorial 
                permit tcp 10.2.1.1 10.10.10.100 established sequence 30 
                permit icmp any any sequence 40 
            exit 
            access-list "data-acl" 
                permit ip any any sequence 10 
            exit 
            access-list "satellite" 
                permit icmp any any sequence 10 
                permit tcp 20.20.20.2 20.20.20.1 sequence 20 
                permit tcp 10.10.10.100 192.168.2.100 sequence 30 
            exit 
        exit 
        crypto 
            ipsec-transform-set "RAD" 
                algorithms esp-aes-gcm-256 
            exit 
            isakmp-key 
"77C6291611AE6632E5AA2454A52B87A3E331A04DF16D459B0601428B988D9D394740488D7D91687D7B24444C0E444
DA047290821529F617538D048DD09749FDB43CBEBDCFCB28E7143AB7C4C7240BBB2" address 95.35.55.33 hash 
            isakmp-policy 1 
                group 14 
                hash sha2-512 
            exit 
            crypto-map "lincoln_2" 
                match-address "data-acl" 
                peer-address 95.35.55.33 
                pfs-group 14 
                transform-set "RAD" 
                ike-identity-local address 95.35.55.118 
                ike-identity-local-x509 distinguished-name 
                ike-identity-remote address 95.35.55.33 
                ike-identity-remote-x509 any 
                ike-version 2 
            exit 
        exit 
        echo "Management configuration" 
#       Management configuration 
        management 
            login-user "netconf-su" 
                shutdown 
            exit 
            echo "SNMP Configuration" 
#           SNMP Configuration 
            snmp 
                snmp-engine-id mac 18-06-F5-B4-0F-AC 
            exit 
        exit 
        echo "Port Configuration" 
#       Port Configuration 
        port 
            echo "Ethernet - Port Configuration" 
#           Ethernet - Port Configuration 
13. Application Tutorial 
            ethernet 1 
                name "xDSL" 
                vlan 96 
                    name "ADSL" 
                    no shutdown 
                exit 
                vlan 101 
                    name "VDSL" 
                    no shutdown 
                exit 
                no shutdown 
            exit 
            ethernet 3 
                vlan 10 
                    no shutdown 
                exit 
                vlan 20 
                    no shutdown 
                exit 
                access-group "rtu" inbound 
                no shutdown 
            exit 
            ethernet 4 
                access-group "satellite" inbound 
                no shutdown 
            exit 
            ethernet 5 
                no shutdown 
            exit 
            ethernet 6 
                no shutdown 
            exit 
            echo "Cellular - Port Configuration" 
#           Cellular - Port Configuration 
            cellular lte 
                access-group "lte" inbound 
                no shutdown 
            exit 
            echo "PPP - Port Configuration" 
#           PPP - Port Configuration 
            ppp 1 
                no name 
                bind ethernet 1 
                chap-hostname "rad.co.il" 
                chap-password "418756FEF5EEBE3E939B01520075243D" hash 
                ipcp-address 1.0.0.5 
            exit 
            echo "Serial port level" 
#           Serial port level 
            serial 1 
                baud-rate 19200 
            exit 
13. Application Tutorial 
        exit 
        router 1 
            name "Router#1" 
            interface 1 
                bind ppp 1 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 2 
                bind cellular lte 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 3 
                address 192.168.2.200/24 
                bind ethernet 3 vlan 20 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 4 
                address 20.20.20.1/24 
                bind ethernet 4 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 5 
                address 172.17.191.111/24 
                bind ethernet 5 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            interface 10 loopback 
                address 10.1.1.1/32 
                no shutdown 
            exit 
            interface 11 
                address 10.2.1.100/24 
                bind ethernet 3 vlan 10 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
13. Application Tutorial 
            exit 
            interface 32 
                address 169.254.1.1/16 
                bind ethernet 6 
                dhcp-client 
                    client-id mac 
                exit 
                no shutdown 
            exit 
            static-route 95.35.55.33/32 interface 2 metric 1 
            static-route 172.17.171.0/24 address 172.17.191.1 metric 1 
            static-route 172.17.190.0/24 address 172.17.191.1 metric 1 
            echo "Router policy configuration - route maps" 
#           Router policy configuration - route maps 
            route-map "LOCAL-PREF-80" 
                permit set local-preference 80 sequence 10 
            exit 
            echo "BGP configuration" 
#           BGP configuration 
            bgp 4100 
                router-id 10.1.20.2 
                no shutdown 
                echo "BGP Neighbor Configuration" 
#               BGP Neighbor Configuration 
                neighbor 10.1.20.1 
                    remote-as 4100 
                    no shutdown 
                exit 
                neighbor 20.20.20.2 
                    remote-as 4100 
                    no shutdown 
                exit 
                echo "IPv4 Unicast Address Family Configuration" 
#               IPv4 Unicast Address Family Configuration 
                ipv4-unicast-af 
                    network 10.1.1.1/32 
                    network 10.2.1.0/24 
                    network 192.168.2.0/24 
                    echo "IPv4 Unicast Address Family - Neighbor Configuration" 
#                   IPv4 Unicast Address Family - Neighbor Configuration 
                    neighbor 10.1.20.1 
                        active 
                    exit 
                    neighbor 20.20.20.2 
                        active 
                        route-map-bind "LOCAL-PREF-80" in 
                    exit 
                exit 
                echo "IPv6 Unicast Address Family Configuration" 
#               IPv6 Unicast Address Family Configuration 
                ipv6-unicast-af 
                    echo "IPv6 Unicast Address Family - Neighbor Configuration" 
13. Application Tutorial 
#                   IPv6 Unicast Address Family - Neighbor Configuration 
                    neighbor 10.1.20.1 
                    exit 
                    neighbor 20.20.20.2 
                    exit 
                exit 
            exit 
            tunnel-interface 2 ipsec 
                tunnel-source router-interface 2 
                tunnel-destination 95.35.55.33 
                ip-address static 10.1.20.2/24 
                crypto-map "lincoln_2" 
                no shutdown 
            exit 
        exit 
    exit 
 