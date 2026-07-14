# MP-1-mn user manual — chapter index (family: mp1)

Extracted from `MP-1-mn_ver 2.2.pdf` by scripts/ingest_manual.py.
COMPANION to the harvested CLI reference: syntax questions -> cli-reference-mp1.md; concepts, procedures, limits, alarm
meanings -> the chapter files below. Grep a chapter file for the
topic, or start from the cross-link table.

| Chapter file | Pages | Sections |
|---|---|---|
| `01-quick-start-guide.md` | 28–33 | Installing the Unit; Connecting the Interfaces; Connecting to a Terminal; Connecting to Power; Configuring the Unit for Management; Starting a Terminal Session for the First Time; Configuring Management Flows; Saving Management Configuration; ... |
| `02-1-introduction.md` | 47–67 | 1.1 Overview; 1.2 New in this Version; 1.3 Physical Description; 1.4 Functional Description; 1.5 Technical Specifications |
| `03-2-installation-and-setup.md` | 68–91 | 2.1 Storage and Transportation; 2.2 Site Requirements and Prerequisites; 2.3 Package Contents; 2.4 Required Equipment; 2.5 Mounting the Unit; 2.6 Installing SFP Modules; 2.7 Connecting to Ethernet Equipment; 2.8 Connecting to E1/T1 Equipment; ... |
| `04-3-operation-and-maintenance.md` | 92–129 | 3.1 Turning On the Unit; 3.2 Indicators; 3.3 Startup; 3.4 Working with Custom Configuration Files; 3.5 Configuration and Management; 3.6 Factory Default Push Button; 3.7 CLI-Based Configuration; 3.8 GUI-Based Configuration; ... |
| `05-4-service-provisioning.md` | 130–141 | 4.1 Service Entities; 4.2 Ethernet Service; 4.3 TDM Service over UDP IP PW; 4.4 TDM Service over MEF-8 PW |
| `06-5-ports.md` | 142–215 | 5.1 Port-Related Profiles; 5.2 DS1 Ports; 5.3 DS1 Optical Ports; 5.4 E1 Ports; 5.5 Ethernet Ports; 5.6 Service Virtual Interfaces; 5.7 Serial Ports; 5.8 T1 Ports; ... |
| `07-6-management-and-security.md` | 216–268 | 6.1 Access Control List (ACL); 6.2 Access Policy; 6.3 Authentication via RADIUS Server; 6.4 Authentication via TACACS+ Server; 6.5 Control Port; 6.6 Management Access Methods; 6.7 RSA Key Generation; 6.8 SNMP Management; ... |
| `08-7-resiliency-and-optimization.md` | 269–280 | 7.1 Fault Propagation; 7.2 PW Protection; 7.3 TDM Group Protection |
| `09-8-traffic-processing.md` | 281–356 | 8.1 Bridge; 8.2 Cross-Connections; 8.3 Flows; 8.4 Quality of Service (QoS); 8.5 Peer; 8.6 Pseudowires; 8.7 Router |
| `10-9-timing-and-synchronization.md` | 357–376 | 9.1 Clock Selection; 9.2 Date and Time |
| `11-10-administration.md` | 377–404 | 10.1 MAC Address Allocation; 10.2 Memory Utilization; 10.3 Device Information; 10.4 Environment; 10.5 Inventory; 10.6 Login Banner; 10.7 Reset; 10.8 Tech-Support Commands; ... |
| `12-11-monitoring-and-diagnostics.md` | 405–426 | 11.1 Performance Management; 11.2 Detecting Problems; 11.3 Handling Alarms and Events; 11.4 Syslog; 11.5 Troubleshooting; 11.6 Technical Support |
| `13-12-software-upgrade.md` | 427–437 | 12.1 Compatibility Requirements; 12.2 Prerequisites; 12.3 Upgrading the Device Software via CLI; 12.4 Upgrading the Device Software via the Boot Menu; 12.5 Verifying Upgrade Results |
| `14-13-application-guide.md` | 438–483 | 13.1 Introduction; 13.2 MP1 P2P PW Services via MP-4 ERP; 13.3 Configuring PW services with CLI; 13.4 Configuring MP-1 PW Services Using the RADview Shelf View Application; 13.5 Configuring MP-1 PW Services using RADview SM; 13.6 Success criteria |
| `15-a-connection-data.md` | 484–508 | A.1 Alarm Relay Connector; A.2 NNI Ethernet Port Connectors; A.3 UNI Ethernet Port Connector; A.4 CONTROL Connector; A.5 CLOCK Connector; A.6 MNG-ETH Connector; A.7 Serial Connector and Cables; A.8 E&M Connector; ... |
| `16-b-security.md` | 509–510 | B.1 Passwords |
| `17-rm-50-mounting-kit.md` | 511–517 |  |

## CLI topic -> manual chapter cross-links

| CLI area | Manual sections (chapter file) |
|---|---|
| configure router (routing, static routes) | Router (`05-4-service-provisioning.md`); Router-Level Tasks (`07-6-management-and-security.md`); 8.7 Router (`09-8-traffic-processing.md`); Configuring the Router (`09-8-traffic-processing.md`); ... |
| configure port ethernet / vlan | Ethernet Switch (`02-1-introduction.md`); 2.7 Connecting to Ethernet Equipment (`03-2-installation-and-setup.md`); 4.2 Ethernet Service (`05-4-service-provisioning.md`); 5.5 Ethernet Ports (`06-5-ports.md`); ... |
| configure port cellular (LTE) | Simple Network Time Protocol (`02-1-introduction.md`); Filtering Output (`04-3-operation-and-maintenance.md`); Filtering and Marking (`07-6-management-and-security.md`) |
| configure management snmp | 3.9 SNMP-Based Network Management (`04-3-operation-and-maintenance.md`); Preconfiguring Megaplex-1 for SNMP Management (`04-3-operation-and-maintenance.md`); Working with other SNMP-Based NMS (`04-3-operation-and-maintenance.md`); 6.8 SNMP Management (`07-6-management-and-security.md`); ... |
| configure management (users, AAA, tacacs+) | Copying User Configuration to Default Configuration (`01-quick-start-guide.md`); Lost Superuser Password (`04-3-operation-and-maintenance.md`); 6.3 Authentication via RADIUS Server (`07-6-management-and-security.md`); 6.4 Authentication via TACACS+ Server (`07-6-management-and-security.md`); ... |
| configure reporting (alarms, syslog) | Syslog (`02-1-introduction.md`); Alarm Collection and Reporting (`02-1-introduction.md`); 2.15 Connecting to Alarm Equipment (`03-2-installation-and-setup.md`); Login (`04-3-operation-and-maintenance.md`); ... |
| configure system date-and-time / ntp | 2.12 Connecting to Station Clock (`03-2-installation-and-setup.md`); Connecting to a Balanced Clock Source (`03-2-installation-and-setup.md`); Connecting to an Unbalanced Clock Source (`03-2-installation-and-setup.md`); 9.1 Clock Selection (`10-9-timing-and-synchronization.md`); ... |
| configure qos | Queue Group Profile (`06-5-ports.md`); 8.4 Quality of Service (QoS) (`09-8-traffic-processing.md`); Configuring Shaper Profiles (`09-8-traffic-processing.md`); Queue Mapping Profiles (`09-8-traffic-processing.md`); ... |
| configure protection erp | Resiliency (`02-1-introduction.md`); 13.2 MP1 P2P PW Services via MP-4 ERP (`14-13-application-guide.md`); ERP Auto-Discovery (`14-13-application-guide.md`) |
| access-control / firewall | 6.1 Access Control List (ACL) (`07-6-management-and-security.md`); Binding Access Control Lists (`07-6-management-and-security.md`); Configuring ACL (`07-6-management-and-security.md`) |