# minid command tree (family: minid)

Captured live from minid-1 (MiNID (Miniature NID / sleeve device) SW 2.6, prompt MiNID#; verified live - shared context CLI, direct-write save; fragile/unique SSH (patient profile); CLI reference + manual harvested) via the root `tree` command on 2026-07-15
by scripts/harvest_cli.py — re-run `harvest` after firmware upgrades; the
tree is re-captured fresh each run. Use it to locate which context holds a
feature, then cli-reference-minid.md / the cli_help tool for exact,
firmware-current argument syntax.

Legend from the CLI's own `?` listings: `+` = sub-context you can enter,
`-` = command/leaf, `[no]` prefix = removable with `no <leaf>`.

```
|
+---admin
|   |
|   +---factory-default
|   |
|   +---user-default
|   |
|   +---reboot
|   |
|   +---software
|   |   |
|   |   +---install
|
+---configure
|   |
|   +---access-control
|   |   |
|   |   +---access-list
|   |   |   |
|   |   |   +---permit
|   |   |   |
|   |   |   +---deny
|   |   |   |
|   |   |   +---delete
|   |
|   +---management
|   |   |
|   |   +---timeout
|   |   |
|   |   +---user
|   |   |
|   |   +---manager
|   |   |
|   |   +---zero-touch
|   |   |
|   |   +---access
|   |   |   |
|   |   |   +---auth-policy
|   |   |   |
|   |   |   +---wait-to-restore-auth-method
|   |   |   |
|   |   |   +---sfp
|   |   |   |
|   |   |   +---msa
|   |   |   |
|   |   |   +---snmp-read-only
|   |   |   |
|   |   |   +---static-ip-access
|   |   |   |   |
|   |   |   |   +---snmp
|   |   |   |   |
|   |   |   |   +---tftp/sftp
|   |   |   |   |
|   |   |   |   +---ssh
|   |   |   |   |
|   |   |   |   +---telnet
|   |   |   |   |
|   |   |   |   +---http
|   |   |   |
|   |   |   +---loaned-ip-access
|   |   |   |   |
|   |   |   |   +---snmp
|   |   |   |   |
|   |   |   |   +---tftp/sftp
|   |   |   |   |
|   |   |   |   +---ssh
|   |   |   |   |
|   |   |   |   +---telnet
|   |   |   |   |
|   |   |   |   +---http
|   |   |   |   |
|   |   |   |   +---rpcap
|   |   |   |
|   |   |   +---access-group
|   |   |
|   |   +---host
|   |   |   |
|   |   |   +---loaned-ip
|   |   |   |
|   |   |   +---dhcp
|   |   |   |
|   |   |   +---ip-address
|   |   |   |
|   |   |   +---default-gw
|   |   |   |
|   |   |   +---vlan
|   |   |   |
|   |   |   +---vlan-id
|   |   |   |
|   |   |   +---vlan-pbits
|   |   |   |
|   |   |   +---vlan-tpid
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---snmp
|   |   |
|   |   +---tacacsplus
|   |   |   |
|   |   |   +---privilege-level
|   |   |   |
|   |   |   +---group
|   |   |   |   |
|   |   |   |   +---accounting
|   |   |   |
|   |   |   +---server
|   |   |   |   |
|   |   |   |   +---accounting-port
|   |   |   |   |
|   |   |   |   +---authentication-port
|   |   |   |   |
|   |   |   |   +---clear-statistics
|   |   |   |   |
|   |   |   |   +---group
|   |   |   |   |
|   |   |   |   +---key
|   |   |   |   |
|   |   |   |   +---retry
|   |   |   |   |
|   |   |   |   +---timeout
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |
|   |   |   +---wait-to-restore-server
|   |   |
|   |   +---show access
|   |   |
|   |   +---show users
|   |
|   +---router
|   |   |
|   |   +---interface
|   |   |   |
|   |   |   +---ipv6-autoconfig
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---vlan
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---dhcp
|   |   |   |
|   |   |   +---vlan-tpid
|   |   |   |
|   |   |   +---loaned-ip
|   |   |   |
|   |   |   +---dhcpv6-client
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---static-route
|   |   |
|   |   +---management-cfg
|   |
|   +---oam
|   |   |
|   |   +---cfm
|   |   |   |
|   |   |   +---alarm-type
|   |   |   |
|   |   |   +---availability
|   |   |   |
|   |   |   +---measurement-bin-profile
|   |   |   |   |
|   |   |   |   +---thresholds
|   |   |   |
|   |   |   +---maintenance-domain
|   |   |   |   |
|   |   |   |   +---md-level
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---maintenance-association
|   |   |   |   |   |
|   |   |   |   |   +---ccm-interval
|   |   |   |   |   |
|   |   |   |   |   +---interface-status-tlv
|   |   |   |   |   |
|   |   |   |   |   +---name
|   |   |   |   |   |
|   |   |   |   |   +---tag-mode
|   |   |   |   |   |
|   |   |   |   |   +---service-name
|   |   |   |   |   |
|   |   |   |   |   +---mep
|   |   |   |   |   |   |
|   |   |   |   |   |   +---ais
|   |   |   |   |   |   |
|   |   |   |   |   |   +---bind
|   |   |   |   |   |   |
|   |   |   |   |   |   +---client-md-level
|   |   |   |   |   |   |
|   |   |   |   |   |   +---lbm
|   |   |   |   |   |   |
|   |   |   |   |   |   +---linktrace
|   |   |   |   |   |   |
|   |   |   |   |   |   +---dest-addr-type
|   |   |   |   |   |   |
|   |   |   |   |   |   +---priority
|   |   |   |   |   |   |
|   |   |   |   |   |   +---outer-priority
|   |   |   |   |   |   |
|   |   |   |   |   |   +---inner-priority
|   |   |   |   |   |   |
|   |   |   |   |   |   +---vlan
|   |   |   |   |   |   |
|   |   |   |   |   |   +---vlan
|   |   |   |   |   |   |
|   |   |   |   |   |   +---outer-vlan
|   |   |   |   |   |   |
|   |   |   |   |   |   +---remote-mep
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---show remote-mep-id <remote-mep-id>
|   |   |   |   |   |   |
|   |   |   |   |   |   +---dest-mac-addr
|   |   |   |   |   |   |
|   |   |   |   |   |   +---ccm-initiate
|   |   |   |   |   |   |
|   |   |   |   |   |   +---shutdown
|   |   |   |   |   |   |
|   |   |   |   |   |   +---service
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---delay-threshold
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---delay-var-threshold
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---lmm-interval
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---dmm-interval
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---interval
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---loss-threshold
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---loss-dei-bit-color
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---priority
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---shutdown
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---dest-ne
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---delay
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---bind-delay-measurement-bin
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---bind-delay-var-measurement-bin
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---loss
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---remote-mep
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---clear-statistics
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---shutdown
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---show-statistics
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---running
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---current
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---interval
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---total-intervals
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---all-intervals
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---show-delay-measurement-bins
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---running
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---current
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---interval
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---all-intervals
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---total-intervals
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---clear-statistics
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show status
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show lbm-results
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show linktrace-results
|   |   |   |   |   |
|   |   |   |   |   +---mip
|   |   |   |   |   |   |
|   |   |   |   |   |   +---priority
|   |   |   |   |   |   |
|   |   |   |   |   |   +---outer-priority
|   |   |   |   |   |   |
|   |   |   |   |   |   +---inner-priority
|   |   |   |   |   |   |
|   |   |   |   |   |   +---vlan
|   |   |   |   |   |   |
|   |   |   |   |   |   +---vlan
|   |   |   |   |   |   |
|   |   |   |   |   |   +---outer-vlan
|   |   |   |   |   |   |
|   |   |   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---show mips
|   |   |   |
|   |   |   +---show summary
|   |   |
|   |   +---efm
|   |   |   |
|   |   |   +---mode
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---show status
|   |   |   |
|   |   |   +---show statistics
|   |   |
|   |   +---twamp
|   |   |   |
|   |   |   +---profile
|   |   |   |   |
|   |   |   |   +---payload-length
|   |   |   |   |
|   |   |   |   +---transmit-rate
|   |   |   |   |
|   |   |   |   +---loss-timeout
|   |   |   |   |
|   |   |   |   +---loss-ratio-threshold
|   |   |   |   |
|   |   |   |   +---delay-variation-threshold
|   |   |   |   |
|   |   |   |   +---delay-threshold
|   |   |   |   |
|   |   |   |   +---delay-variation-event-type
|   |   |   |
|   |   |   +---responder
|   |   |   |   |
|   |   |   |   +---ip-address
|   |   |   |   |
|   |   |   |   +---udp-port
|   |   |   |   |
|   |   |   |   +---tx-seq-num
|   |   |   |   |
|   |   |   |   +---ip-loan
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---unbind-all-flows
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---controller
|   |   |   |   |
|   |   |   |   +---local-ip-address
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---peer
|   |   |   |   |   |
|   |   |   |   |   +---calculation-mode
|   |   |   |   |   |
|   |   |   |   |   +---responder-seq-num
|   |   |   |   |   |
|   |   |   |   |   +---test-session
|   |   |   |   |   |
|   |   |   |   |   +---activate
|   |   |   |   |   |
|   |   |   |   |   +---show-status
|   |   |   |   |   |
|   |   |   |   |   +---show-summary-report
|   |   |   |   |   |
|   |   |   |   |   +---show-report
|   |   |   |   |
|   |   |   |   +---show status
|   |
|   +---qos
|   |   |
|   |   +---policer-profile
|   |   |   |
|   |   |   +---bandwidth
|   |   |   |
|   |   |   +---color_aware
|   |   |   |
|   |   |   +---compensation
|   |   |   |
|   |   |   +---coupling-flag
|   |   |
|   |   +---envelope-profile
|   |   |   |
|   |   |   +---cf-policy
|   |   |   |
|   |   |   +---color_aware
|   |   |   |
|   |   |   +---compensation
|   |   |   |
|   |   |   +---cos
|   |   |   |   |
|   |   |   |   +---bandwidth
|   |   |   |
|   |   |   +---cos
|   |   |   |   |
|   |   |   |   +---bandwidth
|   |   |   |
|   |   |   +---coupling-flag-0
|   |   |
|   |   +---cos-map-profile
|   |   |   |
|   |   |   +---map
|   |
|   +---flows
|   |   |
|   |   +---classification
|   |   |
|   |   +---dscp-marking
|   |   |
|   |   +---fallback-action
|   |   |
|   |   +---in-service-mac
|   |   |
|   |   +---in-service-l3-l4
|   |   |   |
|   |   |   +---ip-loop
|   |   |   |   |
|   |   |   |   +---ip-address
|   |   |   |
|   |   |   +---udp-loop
|   |   |   |   |
|   |   |   |   +---ip-address
|   |   |   |   |
|   |   |   |   +---udp-port
|   |   |   |
|   |   |   +---udp-echo
|   |   |   |   |
|   |   |   |   +---ip-address
|   |   |   |   |
|   |   |   |   +---udp-port
|   |   |
|   |   +---inner-vlan-marking
|   |   |
|   |   +---port-mode-action
|   |   |
|   |   +---l2cp-mac
|   |   |
|   |   +---l2cp-protocol
|   |   |
|   |   +---l2cp-profile
|   |   |   |
|   |   |   +---mac
|   |   |   |
|   |   |   +---protocol
|   |   |
|   |   +---in-service-loops-mac
|   |   |   |
|   |   |   +---in-serv-mode
|   |   |   |
|   |   |   +---in-serv-action
|   |   |   |
|   |   |   +---in-serv-src-mac
|   |   |   |
|   |   |   +---in-serv-dst-mac
|   |   |
|   |   +---in-service-loops-l3-l4
|   |   |   |
|   |   |   +---in-serv-l3-l4
|   |   |   |
|   |   |   +---responder
|   |   |
|   |   +---port-l2cp
|   |   |
|   |   +---fallback-l2cp
|   |   |
|   |   +---tpid-pushed-replaced-vlan
|   |   |
|   |   +---tpid-outer-vlan
|   |   |
|   |   +---tpid-inner-vlan
|   |   |
|   |   +---flow
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---flow-action
|   |   |   |
|   |   |   +---policer
|   |   |   |   |
|   |   |   |   +---profile
|   |   |   |   |
|   |   |   |   +---regular-accounting-only
|   |   |   |   |
|   |   |   |   +---envelope
|   |   |   |
|   |   |   +---cos-mapping
|   |   |   |
|   |   |   +---classifier
|   |   |   |
|   |   |   +---classifier
|   |   |   |
|   |   |   +---service-name
|   |   |   |
|   |   |   +---l2cp
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---in-service-loops
|   |   |   |   |
|   |   |   |   +---in-serv-mode
|   |   |   |   |
|   |   |   |   +---in-serv-action
|   |   |   |   |
|   |   |   |   +---in-serv-src-mac
|   |   |   |   |
|   |   |   |   +---in-serv-dst-mac
|   |   |   |
|   |   |   +---in-service-l3-l4-loops
|   |   |   |   |
|   |   |   |   +---in-serv-l3-l4
|   |   |   |   |
|   |   |   |   +---responder
|   |   |   |
|   |   |   +---test
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---show statistics
|   |   |
|   |   +---rename-flow
|   |   |
|   |   +---lbm-reflector
|   |   |   |
|   |   |   +---md-level
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---ip-agnostic-loop
|   |   |
|   |   +---clear-statistics
|   |   |
|   |   +---fallback-policer
|   |   |
|   |   +---fallback-pm-collection
|   |   |
|   |   +---port-mode-policer
|   |   |
|   |   +---port-mode-pm-collection
|   |   |
|   |   +---show summary
|   |   |
|   |   +---show unclassified-statistics
|   |   |
|   |   +---show port-mode-statistics
|   |
|   +---port
|   |   |
|   |   +---ethernet
|   |   |   |
|   |   |   +---auto-negotiation
|   |   |   |
|   |   |   +---force-direct-i2c
|   |   |   |
|   |   |   +---force-speed
|   |   |   |
|   |   |   +---i2c-stretching-clock
|   |   |   |
|   |   |   +---mtu
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---show status
|   |   |   |
|   |   |   +---show statistics
|   |
|   +---reporting
|   |   |
|   |   +---pm
|   |   |
|   |   +---clear-log
|   |   |
|   |   +---file-interval-duration
|   |   |
|   |   +---interval-duration
|   |   |
|   |   +---show log
|   |
|   +---service
|   |   |
|   |   +---
|   |   |
|   |   +---show summary
|   |
|   +---system
|   |   |
|   |   +---device-name
|   |   |
|   |   +---location
|   |   |
|   |   +---contact
|   |   |
|   |   +---date-and-time
|   |   |   |
|   |   |   +---date-format
|   |   |   |
|   |   |   +---date
|   |   |   |
|   |   |   +---date
|   |   |   |
|   |   |   +---date
|   |   |   |
|   |   |   +---date
|   |   |   |
|   |   |   +---ntp
|   |   |   |   |
|   |   |   |   +---poll-interval
|   |   |   |   |
|   |   |   |   +---server
|   |   |   |   |   |
|   |   |   |   |   +---address
|   |   |   |   |   |
|   |   |   |   |   +---query-server
|   |   |   |   |   |
|   |   |   |   |   +---shutdown
|   |   |   |   |   |
|   |   |   |   |   +---udp
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---summer-time
|   |   |   |   |
|   |   |   |   +---recurring
|   |   |   |   |
|   |   |   |   +---date
|   |   |   |
|   |   |   +---time
|   |   |   |
|   |   |   +---zone
|   |   |   |
|   |   |   +---show summer-time
|   |   |
|   |   +---clock
|   |   |   |
|   |   |   +---sync-e-src
|   |   |
|   |   +---fault-propagation
|   |   |   |
|   |   |   +---ais
|   |   |   |
|   |   |   +---phy-disable
|   |   |   |
|   |   |   +---los-propagation
|   |   |   |
|   |   |   +---tx-disable
|   |   |   |
|   |   |   +---tx-fault
|   |   |   |
|   |   |   +---cfm-fault
|   |   |   |
|   |   |   +---if-status-tlv
|   |   |
|   |   +---syslog
|   |   |   |
|   |   |   +---accounting
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---facility
|   |   |   |
|   |   |   +---port
|   |   |   |
|   |   |   +---severity-level
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---show-statistics
|   |   |
|   |   +---show status
|   |
|   +---test
|   |   |
|   |   +---l3sat
|   |   |   |
|   |   |   +---peer-profile
|   |   |   |   |
|   |   |   |   +---performance-duration
|   |   |   |   |
|   |   |   |   +---udp-port
|   |   |   |   |
|   |   |   |   +---responder-type
|   |   |   |
|   |   |   +---session-profile
|   |   |   |   |
|   |   |   |   +---loss-ratio-threshold
|   |   |   |   |
|   |   |   |   +---delay-threshold
|   |   |   |   |
|   |   |   |   +---delay-variation-threshold
|   |   |   |   |
|   |   |   |   +---packet-size
|   |   |   |   |
|   |   |   |   +---L1-rate
|   |   |   |
|   |   |   +---generator
|   |   |   |   |
|   |   |   |   +---local-ip-address
|   |   |   |   |
|   |   |   |   +---short-packet-mode
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---peer
|   |   |   |   |   |
|   |   |   |   |   +---peer-profile
|   |   |   |   |   |
|   |   |   |   |   +---test-session
|   |   |   |   |   |
|   |   |   |   |   +---activate
|   |   |   |   |   |
|   |   |   |   |   +---show status
|   |   |   |   |   |
|   |   |   |   |   +---show report
|   |   |   |   |   |
|   |   |   |   |   +---show summary-report
|   |   |   |   |
|   |   |   |   +---show status
|   |
|   +---packet-capture
|   |   |
|   |   +---capture-dscp
|   |   |
|   |   +---local-ip-address
|   |   |
|   |   +---rpcap-tcp-port
|   |   |
|   |   +---inactive-timeout
|   |   |
|   |   +---timestamp-source
|   |   |
|   |   +---capture
|   |   |
|   |   +---show status
|
+---inventory
|
+---factory
|   |
|   +---eprom_ins
|   |
|   +---eprom_set
|   |
|   +---cfg_set
|   |
|   +---erase
|   |
|   +---cfg_ins
|   |
|   +---fpga
|   |   |
|   |   +---read
|   |   |
|   |   +---write
|   |   |
|   |   +---show-statistics
|   |   |
|   |   +---clear-statistics
|   |   |
|   |   +---read_l2cp_table
|   |   |
|   |   +---read_flows_table
|   |
|   +---print-arp-table
|   |
|   +---show eprom
|   |
|   +---show cfg
|
+---logon
|
+---file
|   |
|   +---copy
|   |
|   +---delete
|   |
|   +---show startup-config
|   |
|   +---show user-default-config
|   |
|   +---show sw-pack
```
