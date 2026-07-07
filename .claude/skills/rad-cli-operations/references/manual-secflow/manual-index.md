# SecFlow-1p user manual — chapter index (family: secflow)

Extracted from `SecFlow-1p_6.4_Mn_05-26_GA.pdf` by scripts/ingest_manual.py.
COMPANION to the harvested CLI reference: syntax questions -> cli-reference-secflow.md; concepts, procedures, limits, alarm
meanings -> the chapter files below. Grep a chapter file for the
topic, or start from the cross-link table.

| Chapter file | Pages | Sections |
|---|---|---|
| `01-1-introduction.md` | 47–71 | 1.1 Overview; 1.2 New in this Version; 1.3 Product Description; 1.4 Technical Specifications |
| `02-2-hardware-installation.md` | 72–100 | 2.1 Pre-installation; 2.2 Installation Process |
| `03-3-operation-and-maintenance.md` | 101–138 | 3.1 Turning On the Unit; 3.2 Indicators; 3.3 FD Button; 3.4 Startup; 3.5 Upgrading the Software; 3.6 Working with Custom Configuration Files; 3.7 Information elements essential for Zero Touch procedure (se; 3.8 Periodical Maintenance; ... |
| `04-4-configuration-and-management.md` | 139–222 | 4.1 CLI-Based Configuration; 4.2 Web-based Configuration; 4.3 SNMP-Based Network Management; 4.4 NETCONF-Based Network Management |
| `05-5-ports.md` | 223–305 | 5.1 Cellular Ports; 5.2 /Ethernet Ports; 5.3 Flash (SD Card) Ports; 5.4 PPP Ports; 5.5 Serial Ports; 5.6 Virtual Ports; 5.7 VLAN Ports; 5.8 WiFi |
| `06-6-management-and-security.md` | 306–453 | 6.1 Access Control List (ACL); 6.2 Authentication via RADIUS Server; 6.3 Authentication via TACACS+ Server; 6.4 IEEE 802.1X - Port-based Network Access Control; 6.5 DHCP Server; 6.6 DHCPv6 Server; 6.7 Enrollment Notification; 6.8 Firewall; ... |
| `07-7-traffic-processing.md` | 454–637 | 7.1 Bridge; 7.2 DMVPN; 7.3 DNP3 Gateway; 7.4 GRE Tunneling; 7.5 IPsec; 7.6 LoRaWAN; 7.7 Network Address Translator (NAT); 7.8 Policy-Based Routing (PBR); ... |
| `08-8-resiliency-and-optimization.md` | 638–663 | 8.1 Ethernet Ring Protection (ERP); 8.2 Fault Propagation; 8.3 Link Redundancy; 8.4 SD-IoT; 9.1 Applicability and Scaling; 9.2 Functional Description |
| `09-9-containerization.md` | 664–671 | 9.3 Configuring the Docker; 9.4 Use Cases and Examples; 10.1 GNSS Location Reporting |
| `10-10-timing-and-synchronization.md` | 672–685 | 10.2 Date and Time; 10.3 Daylight Saving Time; 11.1 Product Information |
| `11-11-administration.md` | 686–714 | 11.2 File Operations; 11.3 Resetting to Default; 11.4 Inventory; 11.5 Login Banner; 12.1 Dry Contacts |
| `12-12-monitoring-and-diagnostics.md` | 715–742 | 12.2 Generating Log Report; 12.3 Syslog; 12.4 IP Monitoring; 12.5 Performance Management; 12.6 Port Mirroring; 12.7 Detecting Problems; 12.8 Running a Ping Test; 12.9 Tracing the Route; ... |
| `13-13-application-tutorial.md` | 743–771 | 13.2 Terminal Sever (IP to Serial) over IPsec over LTE; 13.3 Point-to-Point Automation over IPsec over LTE; 13.4 Terminal Sever (IP to Serial) over IPSec over LTE and Satellite (Ethernet); 13.5 Point-to-Point Automation over IPsec over LTE and Satellite (Ethernet) |
| `14-a-connection-data.md` | 772–775 | A.1 Ethernet Connector; A.2 Serial Port |
| `15-b-integration-with-actility-tpe.md` | 776–787 | B.1 Actility ThingPark Enterprise Platform; B.2 SecFlow-1p Integration to Actility TPE |
| `16-rm-din-19-mounting-kit.md` | 788–789 | KIT CONTENTS; INSTALLATION PROCEDURE; Ordering |
| `17-rm-din-single-mounting-kit.md` | 790–792 | KIT CONTENTS; INSTALLATION PROCEDURE; Ordering |

## CLI topic -> manual chapter cross-links

| CLI area | Manual sections (chapter file) |
|---|---|
| configure system mqtt | 6.9 MQTT Server (`06-6-management-and-security.md`); 6.14 MQTT Server (`06-6-management-and-security.md`) |
| configure crypto / pki / certificates | 6.15 Public Key Infrastructure (`06-6-management-and-security.md`) |
| configure crypto (IPsec/IKE) | 7.5 IPsec (`07-7-traffic-processing.md`); 13.2 Terminal Sever (IP to Serial) over IPsec over LTE (`13-13-application-tutorial.md`); 13.3 Point-to-Point Automation over IPsec over LTE (`13-13-application-tutorial.md`); 13.4 Terminal Sever (IP to Serial) over IPSec over LTE and Satellite (Ethernet) (`13-13-application-tutorial.md`); ... |
| configure router (routing, static routes) | 7.8 Policy-Based Routing (PBR) (`07-7-traffic-processing.md`); 7.10 Router (`07-7-traffic-processing.md`); 7.11 Routing Protocol BGP (`07-7-traffic-processing.md`); 7.12 Routing Protocol OSPF (`07-7-traffic-processing.md`); ... |
| configure router bgp | 7.11 Routing Protocol BGP (`07-7-traffic-processing.md`) |
| configure router ospf | 7.12 Routing Protocol OSPF (`07-7-traffic-processing.md`) |
| configure port ethernet / vlan | 5.2 /Ethernet Ports (`05-5-ports.md`); 5.7 VLAN Ports (`05-5-ports.md`); 8.1 Ethernet Ring Protection (ERP) (`08-8-resiliency-and-optimization.md`); 13.4 Terminal Sever (IP to Serial) over IPSec over LTE and Satellite (Ethernet) (`13-13-application-tutorial.md`); ... |
| configure port cellular (LTE) | 5.1 Cellular Ports (`05-5-ports.md`); 13.1 Terminal Sever (IP to Serial) over LTE (`12-12-monitoring-and-diagnostics.md`); 13.2 Terminal Sever (IP to Serial) over IPsec over LTE (`13-13-application-tutorial.md`); 13.3 Point-to-Point Automation over IPsec over LTE (`13-13-application-tutorial.md`); ... |
| configure port wifi-client / wlan | 5.8 WiFi (`05-5-ports.md`) |
| LoRa gateway | 7.6 LoRaWAN (`07-7-traffic-processing.md`) |
| configure management snmp | 4.3 SNMP-Based Network Management (`04-4-configuration-and-management.md`); 6.16 SNMPv3 Management (`06-6-management-and-security.md`) |
| configure management (users, AAA, tacacs+) | 6.2 Authentication via RADIUS Server (`06-6-management-and-security.md`); 6.3 Authentication via TACACS+ Server (`06-6-management-and-security.md`); 6.17 User Access (`06-6-management-and-security.md`) |
| NETCONF / YANG | 4.4 NETCONF-Based Network Management (`04-4-configuration-and-management.md`); 6.13 NETCONF-Based Network Management (`06-6-management-and-security.md`) |
| configure reporting (alarms, syslog) | 11.5 Login Banner (`11-11-administration.md`); 12.2 Generating Log Report (`12-12-monitoring-and-diagnostics.md`); 12.3 Syslog (`12-12-monitoring-and-diagnostics.md`) |
| configure system date-and-time / ntp | 10.2 Date and Time (`10-10-timing-and-synchronization.md`) |
| configure qos | 7.9 Quality of Service (QoS) (`07-7-traffic-processing.md`) |
| configure protection erp | 8.1 Ethernet Ring Protection (ERP) (`08-8-resiliency-and-optimization.md`); B.1 Actility ThingPark Enterprise Platform (`15-b-integration-with-actility-tpe.md`) |
| access-control / firewall | 6.1 Access Control List (ACL) (`06-6-management-and-security.md`); 6.4 IEEE 802.1X - Port-based Network Access Control (`06-6-management-and-security.md`); 6.8 Firewall (`06-6-management-and-security.md`) |
| dhcp | 6.5 DHCP Server (`06-6-management-and-security.md`); 6.6 DHCPv6 Server (`06-6-management-and-security.md`) |
| admin software / file (upgrade, backup) | 2.1 Pre-installation (`02-2-hardware-installation.md`); 2.2 Installation Process (`02-2-hardware-installation.md`); INSTALLATION PROCEDURE (`16-rm-din-19-mounting-kit.md`); INSTALLATION PROCEDURE (`17-rm-din-single-mounting-kit.md`) |