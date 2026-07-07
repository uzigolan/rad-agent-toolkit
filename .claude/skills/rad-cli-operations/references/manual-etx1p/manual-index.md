# ETX-1p user manual — chapter index (family: etx1p)

Extracted from `ETX-1p_6.4_Mn_05-26_GA.pdf` by scripts/ingest_manual.py.
COMPANION to the harvested CLI reference: syntax questions -> cli-reference-etx1p.md; concepts, procedures, limits, alarm
meanings -> the chapter files below. Grep a chapter file for the
topic, or start from the cross-link table.

| Chapter file | Pages | Sections |
|---|---|---|
| `01-1-introduction.md` | 45–66 | 1.1 Overview; 1.2 New in this Version; 1.3 Technical Specifications |
| `02-2-hardware-installation.md` | 67–88 | 2.1 Pre-installation; 2.2 Installation Process |
| `03-3-operation-and-maintenance.md` | 89–125 | 3.1 Turning On the Unit; 3.2 Indicators; 3.3 FD Button; 3.4 Startup; 3.5 Upgrading the Software; 3.6 Working with Custom Configuration Files; 3.7 Information elements essential for Zero Touch procedure (se; 3.8 Periodical Maintenance; ... |
| `04-4-configuration-and-management.md` | 126–204 | 4.1 CLI-Based Configuration; 4.2 Web-based Configuration; 4.3 SNMP-Based Network Management; 4.4 NETCONF-Based Network Management |
| `05-5-ports.md` | 205–272 | 5.1 Cellular Ports; 5.2 Ethernet Ports; 5.3 PPP Ports; 5.4 Virtual Ports; 5.5 VLAN Ports; 5.6 WiFi |
| `06-6-management-and-security.md` | 273–421 | 6.1 Access Control List (ACL); 6.2 Authentication via RADIUS Server; 6.3 Authentication via TACACS+ Server; 6.4 IEEE 802.1X - Port-based Network Access Control; 6.5 DHCP Server; 6.6 DHCPv6 Server; 6.7 Enrollment Notification; 6.8 Firewall; ... |
| `07-7-traffic-processing.md` | 422–603 | 7.1 Bridge; 7.2 DMVPN; 7.3 GRE Tunneling; 7.4 IPsec; 7.5 LoRaWAN; 7.6 Network Address Translator (NAT); 7.7 Policy-Based Routing (PBR); 7.8 Quality of Service (QoS); ... |
| `08-8-resiliency-and-optimization.md` | 604–628 | 8.1 Ethernet Ring Protection (ERP); 8.2 Fault Propagation; 8.3 Link Redundancy; 8.4 SD-IoT |
| `09-9-containerization.md` | 629–635 | 9.1 Applicability and Scaling; 9.2 Functional Description; 9.3 Configuring the Docker; 9.4 Use Cases and Examples |
| `10-10-timing-and-synchronization.md` | 636–649 | 10.1 GNSS Location Reporting; 10.2 Date and Time; 10.3 Daylight Saving Time |
| `11-11-administration.md` | 650–678 | 11.1 Product Information; 11.2 File Operations; 11.3 Resetting to Default; 11.4 Inventory; 11.5 Login Banner |
| `12-12-monitoring-and-diagnostics.md` | 679–704 | 12.1 Generating Log Report; 12.2 Syslog; 12.3 IP Monitoring; 12.4 Performance Management; 12.5 Port Mirroring; 12.6 Detecting Problems; 12.7 Running a Ping Test; 12.8 Tracing the Route; ... |
| `13-a-connection-data.md` | 705–706 | A.1 Ethernet Connector; A.2 CONTROL Connector |
| `14-b-integration-with-actility-tpe.md` | 707–719 | B.1 Actility ThingPark Enterprise Platform; B.2 ETX-1p Integration to Actility TPE |

## CLI topic -> manual chapter cross-links

| CLI area | Manual sections (chapter file) |
|---|---|
| configure system mqtt | 6.9 MQTT Server (`06-6-management-and-security.md`); 6.14 MQTT Server (`06-6-management-and-security.md`) |
| configure crypto / pki / certificates | 6.15 Public Key Infrastructure (`06-6-management-and-security.md`) |
| configure crypto (IPsec/IKE) | 7.4 IPsec (`07-7-traffic-processing.md`) |
| configure router (routing, static routes) | 7.7 Policy-Based Routing (PBR) (`07-7-traffic-processing.md`); 7.9 Router (`07-7-traffic-processing.md`); 7.10 Routing Protocol BGP (`07-7-traffic-processing.md`); 7.11 Routing Protocol OSPF (`07-7-traffic-processing.md`); ... |
| configure router bgp | 7.10 Routing Protocol BGP (`07-7-traffic-processing.md`) |
| configure router ospf | 7.11 Routing Protocol OSPF (`07-7-traffic-processing.md`) |
| configure port ethernet / vlan | 5.2 Ethernet Ports (`05-5-ports.md`); 5.5 VLAN Ports (`05-5-ports.md`); 8.1 Ethernet Ring Protection (ERP) (`08-8-resiliency-and-optimization.md`); A.1 Ethernet Connector (`13-a-connection-data.md`) |
| configure port cellular (LTE) | 5.1 Cellular Ports (`05-5-ports.md`) |
| configure port wifi-client / wlan | 5.6 WiFi (`05-5-ports.md`) |
| LoRa gateway | 7.5 LoRaWAN (`07-7-traffic-processing.md`) |
| configure management snmp | 4.3 SNMP-Based Network Management (`04-4-configuration-and-management.md`); 6.16 SNMPv3 Management (`06-6-management-and-security.md`) |
| configure management (users, AAA, tacacs+) | 6.2 Authentication via RADIUS Server (`06-6-management-and-security.md`); 6.3 Authentication via TACACS+ Server (`06-6-management-and-security.md`); 6.17 User Access (`06-6-management-and-security.md`) |
| NETCONF / YANG | 4.4 NETCONF-Based Network Management (`04-4-configuration-and-management.md`); 6.13 NETCONF-Based Network Management (`06-6-management-and-security.md`) |
| configure reporting (alarms, syslog) | 11.5 Login Banner (`11-11-administration.md`); 12.1 Generating Log Report (`12-12-monitoring-and-diagnostics.md`); 12.2 Syslog (`12-12-monitoring-and-diagnostics.md`) |
| configure system date-and-time / ntp | 10.2 Date and Time (`10-10-timing-and-synchronization.md`) |
| configure qos | 7.8 Quality of Service (QoS) (`07-7-traffic-processing.md`) |
| configure protection erp | 8.1 Ethernet Ring Protection (ERP) (`08-8-resiliency-and-optimization.md`); B.1 Actility ThingPark Enterprise Platform (`14-b-integration-with-actility-tpe.md`) |
| access-control / firewall | 6.1 Access Control List (ACL) (`06-6-management-and-security.md`); 6.4 IEEE 802.1X - Port-based Network Access Control (`06-6-management-and-security.md`); 6.8 Firewall (`06-6-management-and-security.md`) |
| dhcp | 6.5 DHCP Server (`06-6-management-and-security.md`); 6.6 DHCPv6 Server (`06-6-management-and-security.md`) |
| admin software / file (upgrade, backup) | 2.1 Pre-installation (`02-2-hardware-installation.md`); 2.2 Installation Process (`02-2-hardware-installation.md`) |