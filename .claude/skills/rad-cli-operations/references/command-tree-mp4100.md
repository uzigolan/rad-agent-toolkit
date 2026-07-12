# mp4100 command tree (family: mp4100)

Captured live from marks-mp4 (Mark's Megaplex-4100 (prompt mp4100#, Mn 4.91) - FIRST mp4100-family unit; candidate-DB CLI (commit/discard-changes)) via the root `tree` command on 2026-07-12
by scripts/harvest_cli.py — re-run `harvest` after firmware upgrades; the
tree is re-captured fresh each run. Use it to locate which context holds a
feature, then cli-reference-mp4100.md / the cli_help tool for exact,
firmware-current argument syntax.

Legend from the CLI's own `?` listings: `+` = sub-context you can enter,
`-` = command/leaf, `[no]` prefix = removable with `no <leaf>`.

```
|
+---admin
|   |
|   +---factory-default
|   |
|   +---license
|   |   |
|   |   +---license-enable
|   |   |
|   |   +---show summary
|   |
|   +---reboot
|   |
|   +---software
|   |   |
|   |   +---install
|   |   |
|   |   +---undo-install
|   |   |
|   |   +---show status
|   |
|   +---startup-confirm-required
|   |
|   +---user-default
|
+---clear-statistics
|
+---configure
|   |
|   +---access-control
|   |   |
|   |   +---access-list
|   |   |   |
|   |   |   +---delete
|   |   |   |
|   |   |   +---deny
|   |   |   |
|   |   |   +---permit
|   |
|   +---bridge
|   |   |
|   |   +---aging-time
|   |   |
|   |   +---clear-mac-table
|   |   |
|   |   +---filtering
|   |   |
|   |   +---mode
|   |   |
|   |   +---port
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pvid
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show bind
|   |   |
|   |   +---root
|   |   |
|   |   +---vlan
|   |   |   |
|   |   |   +---maximum-mac-addresses
|   |   |   |
|   |   |   +---mode
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---root
|   |   |   |
|   |   |   +---tagged-egress
|   |   |
|   |   +---vlan-aware
|   |   |
|   |   +---show mac-address-table
|   |   |
|   |   +---show mac-address-table
|   |
|   +---chassis
|   |   |
|   |   +---inventory
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show environment
|   |   |
|   |   +---show manufacture-info
|   |   |
|   |   +---show summary-inventory
|   |
|   +---cross-connect
|   |   |
|   |   +---ds0
|   |   |
|   |   +---pw-tdm
|   |   |
|   |   +---sdh-sonet
|   |   |
|   |   +---split-ts
|   |   |
|   |   +---tdm
|   |   |
|   |   +---show summary
|   |
|   +---crypto
|   |   |
|   |   +---key
|   |   |   |
|   |   |   +---generate-rsa
|   |   |   |
|   |   |   +---show my-public-key-rsa
|   |
|   +---fault
|   |   |
|   |   +---cfm
|   |   |   |
|   |   |   +---service
|   |   |   |   |
|   |   |   |   +---frames-report
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |
|   |   +---fault-propagation
|   |   |   |
|   |   |   +---description
|   |
|   +---flows
|   |   |
|   |   +---classifier-profile
|   |   |   |
|   |   |   +---match
|   |   |
|   |   +---flow
|   |   |   |
|   |   |   +---classifier
|   |   |   |
|   |   |   +---drop
|   |   |   |
|   |   |   +---egress-port
|   |   |   |
|   |   |   +---ingress-port
|   |   |   |
|   |   |   +---mark
|   |   |   |   |
|   |   |   |   +---inner-marking-profile
|   |   |   |   |
|   |   |   |   +---inner-p-bit
|   |   |   |   |
|   |   |   |   +---inner-vlan
|   |   |   |   |
|   |   |   |   +---marking-profile
|   |   |   |   |
|   |   |   |   +---p-bit
|   |   |   |   |
|   |   |   |   +---vlan
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---policer
|   |   |   |
|   |   |   +---reverse-direction
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---test
|   |   |   |
|   |   |   +---vlan-tag
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show test
|   |   |
|   |   +---rate-sampling-window
|   |   |
|   |   +---service-ping
|   |   |
|   |   +---service-ping-response
|   |   |
|   |   +---show summary
|   |
|   +---management
|   |   |
|   |   +---access
|   |   |   |
|   |   |   +---access-group
|   |   |   |
|   |   |   +---auth-policy
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---sftp
|   |   |   |
|   |   |   +---snmp
|   |   |   |
|   |   |   +---ssh-encryption
|   |   |   |
|   |   |   +---ssh-key-exchange
|   |   |   |
|   |   |   +---ssh-mac
|   |   |   |
|   |   |   +---ssh
|   |   |   |
|   |   |   +---telnet
|   |   |   |
|   |   |   +---tftp
|   |   |   |
|   |   |   +---show access-list
|   |   |
|   |   +---enable-mng-ethernet-traffic
|   |   |
|   |   +---manager
|   |   |   |
|   |   |   +---trap-sync-group
|   |   |
|   |   +---radius
|   |   |   |
|   |   |   +---attribute-send
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---map-service-type
|   |   |   |
|   |   |   +---server
|   |   |   |   |
|   |   |   |   +---address
|   |   |   |   |
|   |   |   |   +---auth-port
|   |   |   |   |
|   |   |   |   +---key
|   |   |   |   |
|   |   |   |   +---retry
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---timeout
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---snmp
|   |   |   |
|   |   |   +---access-group
|   |   |   |   |
|   |   |   |   +---context-match
|   |   |   |   |
|   |   |   |   +---notify-view
|   |   |   |   |
|   |   |   |   +---read-view
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---write-view
|   |   |   |
|   |   |   +---community
|   |   |   |
|   |   |   +---notify
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---tag
|   |   |   |
|   |   |   +---notify-filter
|   |   |   |   |
|   |   |   |   +---mask
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---type
|   |   |   |
|   |   |   +---notify-filter-profile
|   |   |   |   |
|   |   |   |   +---profile-name
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---security-to-group
|   |   |   |   |
|   |   |   |   +---group-name
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---server
|   |   |   |   |
|   |   |   |   +---trap-source-address
|   |   |   |
|   |   |   +---snmp-engine-id
|   |   |   |
|   |   |   +---snmpv3
|   |   |   |
|   |   |   +---target
|   |   |   |   |
|   |   |   |   +---address
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---tag-list
|   |   |   |   |
|   |   |   |   +---target-params
|   |   |   |   |
|   |   |   |   +---trap-sync-group
|   |   |   |
|   |   |   +---target-params
|   |   |   |   |
|   |   |   |   +---message-processing-model
|   |   |   |   |
|   |   |   |   +---security
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---version
|   |   |   |
|   |   |   +---user
|   |   |   |   |
|   |   |   |   +---authentication
|   |   |   |   |
|   |   |   |   +---privacy
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---view
|   |   |   |   |
|   |   |   |   +---mask
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---type
|   |   |
|   |   +---tacacsplus
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
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---timeout
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |
|   |   +---trap-sync-group
|   |   |   |
|   |   |   +---trap-mask
|   |   |
|   |   +---user
|   |   |
|   |   +---show trap-sync
|   |   |
|   |   +---show users
|   |
|   +---oam
|   |   |
|   |   +---cfm
|   |   |   |
|   |   |   +---ethertype
|   |   |   |
|   |   |   +---maintenance-domain
|   |   |   |   |
|   |   |   |   +---maintenance-association
|   |   |   |   |   |
|   |   |   |   |   +---ccm-interval
|   |   |   |   |   |
|   |   |   |   |   +---classification
|   |   |   |   |   |
|   |   |   |   |   +---mep
|   |   |   |   |   |   |
|   |   |   |   |   |   +---ais
|   |   |   |   |   |   |
|   |   |   |   |   |   +---bind
|   |   |   |   |   |   |
|   |   |   |   |   |   +---ccm-initiate
|   |   |   |   |   |   |
|   |   |   |   |   |   +---ccm-priority
|   |   |   |   |   |   |
|   |   |   |   |   |   +---classification
|   |   |   |   |   |   |
|   |   |   |   |   |   +---client-md-level
|   |   |   |   |   |   |
|   |   |   |   |   |   +---continuity-verification
|   |   |   |   |   |   |
|   |   |   |   |   |   +---dest-addr-type
|   |   |   |   |   |   |
|   |   |   |   |   |   +---dest-mac-addr
|   |   |   |   |   |   |
|   |   |   |   |   |   +---direction
|   |   |   |   |   |   |
|   |   |   |   |   |   +---lbm
|   |   |   |   |   |   |
|   |   |   |   |   |   +---linktrace
|   |   |   |   |   |   |
|   |   |   |   |   |   +---queue
|   |   |   |   |   |   |
|   |   |   |   |   |   +---remote-mep
|   |   |   |   |   |   |
|   |   |   |   |   |   +---service
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---classification
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---clear-statistics
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---delay-threshold
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---delay-var-threshold
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---dest-ne
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---clear-statistics
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---delay
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---delay-measurement-bin
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---delay-var-measurement-bin
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---loss
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---pm-collection
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---remote
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---show delay-measurement-bins
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---show statistics
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---dmm-interval
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---lmm-interval
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---pm-collection
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---shutdown
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---show statistics
|   |   |   |   |   |   |
|   |   |   |   |   |   +---shutdown
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show lbm-results
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show linktrace-results
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show status
|   |   |   |   |   |
|   |   |   |   |   +---mip-policy
|   |   |   |   |   |
|   |   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---md-level
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---proprietary-cc
|   |   |   |
|   |   |   +---md-level-mip
|   |   |   |
|   |   |   +---measurement-bin-profile
|   |   |   |   |
|   |   |   |   +---thresholds
|   |   |   |
|   |   |   +---multicast-addr
|   |   |   |
|   |   |   +---show mips
|   |   |   |
|   |   |   +---show mips
|   |   |   |
|   |   |   +---show summary
|   |   |
|   |   +---efm-descriptor
|   |   |   |
|   |   |   +---loopback-operation
|   |   |   |
|   |   |   +---rate-limit
|   |
|   +---peer
|   |
|   +---port
|   |   |
|   |   +---analog-signaling-profile
|   |   |   |
|   |   |   +---a-bit-rx
|   |   |   |
|   |   |   +---a-bit-tx
|   |   |   |
|   |   |   +---b-bit-rx
|   |   |   |
|   |   |   +---b-bit-tx
|   |   |   |
|   |   |   +---c-bit-rx
|   |   |   |
|   |   |   +---c-bit-tx
|   |   |   |
|   |   |   +---d-bit-rx
|   |   |   |
|   |   |   +---d-bit-tx
|   |   |
|   |   +---bri
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---port-id
|   |   |   |
|   |   |   +---rate-bits
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---clear-cmd-led
|   |   |
|   |   +---cmd-channel
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---oos-recovery
|   |   |   |
|   |   |   +---rate
|   |   |   |
|   |   |   +---reactivate
|   |   |   |
|   |   |   +---rx-address
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---trigger-mode
|   |   |   |
|   |   |   +---tx-address
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---cmd-in
|   |   |   |
|   |   |   +---bounce-override
|   |   |   |
|   |   |   +---clear-cmd-led
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---force-active
|   |   |   |
|   |   |   +---input-active
|   |   |   |
|   |   |   +---led-latched
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---preset-duration
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---switching-voltage
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---cmd-in-i
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---trigger-bind
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---cmd-out
|   |   |   |
|   |   |   +---alarm-state-energized
|   |   |   |
|   |   |   +---clear-cmd-led
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---led-latched
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---prolongation
|   |   |   |
|   |   |   +---pulse-duration
|   |   |   |
|   |   |   +---secondary-bind
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---trigger-bind
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---cmd-out-i
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---oos-code
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ds0-bundle
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---bypass
|   |   |   |   |
|   |   |   |   +---bundle
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---control-bit
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---signaling-method
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ds0-g703
|   |   |   |
|   |   |   +---bert
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show bert
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ds1
|   |   |   |
|   |   |   +---line-type
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---signaling
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ds1-opt
|   |   |   |
|   |   |   +---inband-management
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---e1
|   |   |   |
|   |   |   +---bert
|   |   |   |
|   |   |   +---clear-bert-counters
|   |   |   |
|   |   |   +---idle-code
|   |   |   |
|   |   |   +---inband-management
|   |   |   |
|   |   |   +---interface-type
|   |   |   |
|   |   |   +---line-code
|   |   |   |
|   |   |   +---line-type
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---out-of-service
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---timeslots-signaling-profile
|   |   |   |
|   |   |   +---show bert
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---e1-i
|   |   |   |
|   |   |   +---bert
|   |   |   |
|   |   |   +---clear-bert-counters
|   |   |   |
|   |   |   +---idle-code
|   |   |   |
|   |   |   +---inband-management
|   |   |   |
|   |   |   +---line-type
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---out-of-service
|   |   |   |
|   |   |   +---remote-crc
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---ts0-over-dsl
|   |   |   |
|   |   |   +---show bert
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ethernet
|   |   |   |
|   |   |   +---auto-negotiation
|   |   |   |
|   |   |   +---clear-efm-statistics
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---efm
|   |   |   |   |
|   |   |   |   +---loopback
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---flow-control
|   |   |   |
|   |   |   +---l2cp
|   |   |   |
|   |   |   +---max-capability
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---policer
|   |   |   |
|   |   |   +---queue-group
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---speed-duplex
|   |   |   |
|   |   |   +---tag-ethernet-type
|   |   |   |
|   |   |   +---show oam-efm
|   |   |   |
|   |   |   +---show oam-efm-statistics
|   |   |   |
|   |   |   +---show sfp-status
|   |   |   |
|   |   |   +---show statistics
|   |   |
|   |   +---gfp
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---fcs-payload
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---scrambler-payload
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---vc
|   |   |   |
|   |   |   +---show bind
|   |   |
|   |   +---hdlc
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---encapsulation
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---vc
|   |   |   |
|   |   |   +---show bind
|   |   |
|   |   +---int-ethernet
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---min-tagged-frame-length
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---policer
|   |   |   |
|   |   |   +---queue-group
|   |   |   |
|   |   |   +---tag-ethernet-type
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---l2cp-profile
|   |   |   |
|   |   |   +---default
|   |   |   |
|   |   |   +---mac
|   |   |   |
|   |   |   +---protocol
|   |   |
|   |   +---lag
|   |   |   |
|   |   |   +---admin-key
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-lacp-statistics
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---distribution-method
|   |   |   |
|   |   |   +---lacp
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---queue-group
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show bind
|   |   |   |
|   |   |   +---show lacp-statistics
|   |   |   |
|   |   |   +---show lacp-status
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---logical-mac
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---efm
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---queue-group
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tag-ethernet-type
|   |   |   |
|   |   |   +---show bind
|   |   |
|   |   +---lre
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-node-table
|   |   |   |
|   |   |   +---clear-proxy-table
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---duplicate-discard
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---rx-supervision-packets
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show node-table
|   |   |   |
|   |   |   +---show proxy-table
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---mlppp
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---mtu
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show bind
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---mng-ethernet
|   |   |   |
|   |   |   +---auto-negotiation
|   |   |   |
|   |   |   +---flow-control
|   |   |   |
|   |   |   +---max-capability
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---speed-duplex
|   |   |   |
|   |   |   +---show bind
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---mux-eth-tdm
|   |   |   |
|   |   |   +---far-end-name
|   |   |   |
|   |   |   +---far-end-type
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---remote
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show sfp-status
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---pcs
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-efm-statistics
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---efm
|   |   |   |   |
|   |   |   |   +---loopback
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---l2cp
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---queue-group
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tag-ethernet-type
|   |   |   |
|   |   |   +---show bind-summary
|   |   |   |
|   |   |   +---show oam-efm
|   |   |   |
|   |   |   +---show oam-efm-statistics
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ppp
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show bind
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---sdh-sonet
|   |   |   |
|   |   |   +---aug
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---pm-collection
|   |   |   |   |
|   |   |   |   +---tug3
|   |   |   |   |   |
|   |   |   |   |   +---pm-collection
|   |   |   |   |   |
|   |   |   |   |   +---vc12
|   |   |   |   |   |   |
|   |   |   |   |   |   +---pm-collection
|   |   |   |   |
|   |   |   |   +---vc
|   |   |   |
|   |   |   +---automatic-laser-shutdown
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---dcc
|   |   |   |
|   |   |   +---frame-type
|   |   |   |
|   |   |   +---j0-pathtrace
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---oc3
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---pm-collection
|   |   |   |   |
|   |   |   |   +---sts1
|   |   |   |   |   |
|   |   |   |   |   +---loopback
|   |   |   |   |   |
|   |   |   |   |   +---pm-collection
|   |   |   |   |   |
|   |   |   |   |   +---vc
|   |   |   |   |   |
|   |   |   |   |   +---vt1-5
|   |   |   |   |   |   |
|   |   |   |   |   |   +---pm-collection
|   |   |   |   |
|   |   |   |   +---vc
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---rdi-on-failure
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---speed
|   |   |   |
|   |   |   +---threshold
|   |   |   |
|   |   |   +---tim-response
|   |   |   |
|   |   |   +---tx-ssm
|   |   |   |
|   |   |   +---show sfp-status
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---serial
|   |   |   |
|   |   |   +---activation-type
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---clock-mode
|   |   |   |
|   |   |   +---conference
|   |   |   |
|   |   |   +---cts-rts
|   |   |   |
|   |   |   +---data-bits
|   |   |   |
|   |   |   +---data-position
|   |   |   |
|   |   |   +---encapsulation-mode
|   |   |   |
|   |   |   +---end-to-end-control
|   |   |   |
|   |   |   +---fifo-size
|   |   |   |
|   |   |   +---interface
|   |   |   |
|   |   |   +---llb
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---mode
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---parity
|   |   |   |
|   |   |   +---rate-adaptive
|   |   |   |
|   |   |   +---rate
|   |   |   |
|   |   |   +---rlb
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---signaling
|   |   |   |
|   |   |   +---stop-bits
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---serial-bundle
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---rate
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---shdsl
|   |   |   |
|   |   |   +---bert
|   |   |   |
|   |   |   +---clear-bert-counters
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---data-rate
|   |   |   |
|   |   |   +---far-end-type
|   |   |   |
|   |   |   +---loop-attenuation-threshold
|   |   |   |
|   |   |   +---loop-attenuation-threshold
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---power-backoff
|   |   |   |
|   |   |   +---power-feeding
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---snr-margin-threshold
|   |   |   |
|   |   |   +---stu
|   |   |   |
|   |   |   +---show bert
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---signaling-profile
|   |   |   |
|   |   |   +---a-bit-code
|   |   |   |
|   |   |   +---b-bit-code
|   |   |   |
|   |   |   +---busy-code
|   |   |   |
|   |   |   +---c-bit-code
|   |   |   |
|   |   |   +---d-bit-code
|   |   |   |
|   |   |   +---idle-code
|   |   |
|   |   +---svi
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---t1
|   |   |   |
|   |   |   +---bert
|   |   |   |
|   |   |   +---clear-bert-counters
|   |   |   |
|   |   |   +---idle-code
|   |   |   |
|   |   |   +---inband-management
|   |   |   |
|   |   |   +---line-code
|   |   |   |
|   |   |   +---line-type
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---out-of-service
|   |   |   |
|   |   |   +---restoration-time
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---timeslots-signaling-profile
|   |   |   |
|   |   |   +---show bert
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---t1-i
|   |   |   |
|   |   |   +---bert
|   |   |   |
|   |   |   +---idle-code
|   |   |   |
|   |   |   +---inband-management
|   |   |   |
|   |   |   +---line-type
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---out-of-service
|   |   |   |
|   |   |   +---restoration-time
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---t3
|   |   |   |
|   |   |   +---channelized
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---line-length
|   |   |   |
|   |   |   +---line-type
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---vc
|   |   |   |
|   |   |   +---show loopback
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---tdm-bridge
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---vcg
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---lcas
|   |   |   |
|   |   |   +---minimum-number-of-links
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show bind
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---vc-profile
|   |   |   |
|   |   |   +---day-threshold
|   |   |   |
|   |   |   +---interval-threshold
|   |   |   |
|   |   |   +---pathtrace
|   |   |   |
|   |   |   +---payload-label
|   |   |   |
|   |   |   +---plm-response
|   |   |   |
|   |   |   +---rate-threshold
|   |   |   |
|   |   |   +---tim-response
|   |   |
|   |   +---voice
|   |   |   |
|   |   |   +---activity-detection
|   |   |   |
|   |   |   +---analog-signaling-profile
|   |   |   |
|   |   |   +---coding
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---loop-disconnect-time
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---omni-signaling
|   |   |   |
|   |   |   +---operation-mode
|   |   |   |
|   |   |   +---ring-voltage
|   |   |   |
|   |   |   +---rx-sensitivity
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---signaling
|   |   |   |
|   |   |   +---tx-gain
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show lag-summary
|   |   |
|   |   +---show summary
|   |   |
|   |   +---show svi-summary
|   |
|   +---protection
|   |   |
|   |   +---accelerated-eth-hw-switchover
|   |   |
|   |   +---aps
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear
|   |   |   |
|   |   |   +---flip-upon-sd
|   |   |   |
|   |   |   +---force-switch
|   |   |   |
|   |   |   +---force-switch-to-protection
|   |   |   |
|   |   |   +---force-switch-to-working
|   |   |   |
|   |   |   +---lockout
|   |   |   |
|   |   |   +---lockout-of-protection
|   |   |   |
|   |   |   +---manual-switch-to-protection
|   |   |   |
|   |   |   +---manual-switch-to-working
|   |   |   |
|   |   |   +---oper-mode
|   |   |   |
|   |   |   +---revertive
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---wait-to-restore
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ds0-group
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear
|   |   |   |
|   |   |   +---force-switch-to-protection
|   |   |   |
|   |   |   +---force-switch-to-working
|   |   |   |
|   |   |   +---manual-switch-to-protection
|   |   |   |
|   |   |   +---manual-switch-to-working
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---oper-mode
|   |   |   |
|   |   |   +---revertive
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---wait-to-restore
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---erp
|   |   |   |
|   |   |   +---bridge
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---data-vlan
|   |   |   |
|   |   |   +---east-port
|   |   |   |
|   |   |   +---force-sf
|   |   |   |
|   |   |   +---r-aps
|   |   |   |
|   |   |   +---rpl
|   |   |   |
|   |   |   +---sf-trigger
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---timers
|   |   |   |
|   |   |   +---wait-to-restore
|   |   |   |
|   |   |   +---west-port
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ethernet-group
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---wait-to-restore
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---io-group
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear
|   |   |   |
|   |   |   +---force-switch-to-protection
|   |   |   |
|   |   |   +---force-switch-to-working
|   |   |   |
|   |   |   +---manual-switch-to-protection
|   |   |   |
|   |   |   +---manual-switch-to-working
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---pw
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---oper-mode
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---tdm-group
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear
|   |   |   |
|   |   |   +---force-switch-to-protection
|   |   |   |
|   |   |   +---force-switch-to-working
|   |   |   |
|   |   |   +---manual-switch-to-protection
|   |   |   |
|   |   |   +---manual-switch-to-working
|   |   |   |
|   |   |   +---oper-mode
|   |   |   |
|   |   |   +---revertive
|   |   |   |
|   |   |   +---wait-to-restore
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---tdm-ring
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---wait-to-restore
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---vc-path
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear
|   |   |   |
|   |   |   +---force-switch-to-protection
|   |   |   |
|   |   |   +---force-switch-to-working
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---revertive
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---wait-to-restore
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show summary-ds0-group
|   |   |
|   |   +---show summary-tdm-group
|   |   |
|   |   +---show summary-vc-path
|   |
|   +---pwe
|   |   |
|   |   +---pw
|   |   |   |
|   |   |   +---arp-table-refresh
|   |   |   |
|   |   |   +---domain-failure-indication
|   |   |   |
|   |   |   +---egress-port
|   |   |   |
|   |   |   +---exp-bits
|   |   |   |
|   |   |   +---far-end-type
|   |   |   |
|   |   |   +---jitter-buffer
|   |   |   |
|   |   |   +---jitter-buffer-centering
|   |   |   |
|   |   |   +---label
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---oam
|   |   |   |
|   |   |   +---peer
|   |   |   |
|   |   |   +---sensitivity
|   |   |   |
|   |   |   +---source-clock-fail
|   |   |   |
|   |   |   +---tdm-oos
|   |   |   |
|   |   |   +---tdm-payload
|   |   |   |
|   |   |   +---tos
|   |   |   |
|   |   |   +---udp-mux-method
|   |   |   |
|   |   |   +---vlan
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show summary
|   |
|   +---qos
|   |   |
|   |   +---marking-profile
|   |   |   |
|   |   |   +---mark
|   |   |
|   |   +---policer-profile
|   |   |   |
|   |   |   +---bandwidth
|   |   |   |
|   |   |   +---color-aware
|   |   |   |
|   |   |   +---compensation
|   |   |   |
|   |   |   +---coupling-flag
|   |   |   |
|   |   |   +---traffic-type
|   |   |
|   |   +---queue-block-profile
|   |   |   |
|   |   |   +---queue
|   |   |   |   |
|   |   |   |   +---congestion-avoidance
|   |   |   |   |
|   |   |   |   +---depth
|   |   |   |   |
|   |   |   |   +---scheduling
|   |   |
|   |   +---queue-group-profile
|   |   |   |
|   |   |   +---queue-block
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---profile
|   |   |   |   |
|   |   |   |   +---shaper
|   |   |
|   |   +---queue-map-profile
|   |   |   |
|   |   |   +---map
|   |   |
|   |   +---shaper-profile
|   |   |   |
|   |   |   +---bandwidth
|   |   |   |
|   |   |   +---compensation
|   |   |
|   |   +---wred-profile
|   |   |   |
|   |   |   +---color
|   |
|   +---reporting
|   |   |
|   |   +---acknowledge
|   |   |
|   |   +---active-alarm-rebuild
|   |   |
|   |   +---alarm-cut-off
|   |   |
|   |   +---alarm-input
|   |   |
|   |   +---alarm-output
|   |   |
|   |   +---alarm-source-attribute
|   |   |
|   |   +---alarm-source-type-attribute
|   |   |
|   |   +---bind-alarm-source-to-relay
|   |   |
|   |   +---bind-alarm-to-relay
|   |   |
|   |   +---clear-alarm-log
|   |   |
|   |   +---log-file-timestamp-type
|   |   |
|   |   +---mask-minimum-severity
|   |   |
|   |   +---pm
|   |   |
|   |   +---pm-collection
|   |   |
|   |   +---show active-alarms
|   |   |
|   |   +---show active-alarms-details
|   |   |
|   |   +---show alarm-information
|   |   |
|   |   +---show alarm-input
|   |   |
|   |   +---show alarm-list
|   |   |
|   |   +---show alarm-log
|   |   |
|   |   +---show alarm-outputs
|   |   |
|   |   +---show brief-alarm-log
|   |   |
|   |   +---show brief-log
|   |   |
|   |   +---show event-information
|   |   |
|   |   +---show event-list
|   |   |
|   |   +---show log
|   |
|   +---router
|   |   |
|   |   +---arp-timeout
|   |   |
|   |   +---interface
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---ip-forwarding
|   |   |   |
|   |   |   +---mtu
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---rip
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---static-route
|   |   |
|   |   +---show routing-table
|   |
|   +---slot
|   |   |
|   |   +---card-type
|   |   |
|   |   +---ms-module
|   |   |   |
|   |   |   +---remote-terminal
|   |   |   |
|   |   |   +---reset-wake
|   |   |
|   |   +---reset
|   |   |
|   |   +---show card-type
|   |   |
|   |   +---show power-inline-status
|   |
|   +---system
|   |   |
|   |   +---clear-cpu-utilization
|   |   |
|   |   +---clock
|   |   |   |
|   |   |   +---domain
|   |   |   |   |
|   |   |   |   +---clear
|   |   |   |   |
|   |   |   |   +---force
|   |   |   |   |
|   |   |   |   +---manual
|   |   |   |   |
|   |   |   |   +---mode
|   |   |   |   |
|   |   |   |   +---quality
|   |   |   |   |
|   |   |   |   +---source
|   |   |   |   |   |
|   |   |   |   |   +---clear-wait-to-restore
|   |   |   |   |   |
|   |   |   |   |   +---hold-off
|   |   |   |   |   |
|   |   |   |   |   +---priority
|   |   |   |   |   |
|   |   |   |   |   +---quality-level
|   |   |   |   |   |
|   |   |   |   |   +---wait-to-restore
|   |   |   |   |   |
|   |   |   |   |   +---show status
|   |   |   |   |
|   |   |   |   +---sync-network-type
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---recovered
|   |   |   |   |
|   |   |   |   +---network-type
|   |   |   |   |
|   |   |   |   +---pw
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---station
|   |   |   |   |
|   |   |   |   +---impedance
|   |   |   |   |
|   |   |   |   +---interface-type
|   |   |   |   |
|   |   |   |   +---line-code
|   |   |   |   |
|   |   |   |   +---line-type
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---rx-sensitivity
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---tx-clock-source
|   |   |   |   |
|   |   |   |   +---show status
|   |   |
|   |   +---contact
|   |   |
|   |   +---date-and-time
|   |   |   |
|   |   |   +---date-format
|   |   |   |
|   |   |   +---date
|   |   |   |
|   |   |   +---sntp
|   |   |   |   |
|   |   |   |   +---broadcast
|   |   |   |   |
|   |   |   |   +---poll-interval
|   |   |   |   |
|   |   |   |   +---server
|   |   |   |   |   |
|   |   |   |   |   +---address
|   |   |   |   |   |
|   |   |   |   |   +---prefer
|   |   |   |   |   |
|   |   |   |   |   +---query-server
|   |   |   |   |   |
|   |   |   |   |   +---shutdown
|   |   |   |   |   |
|   |   |   |   |   +---udp
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---time
|   |   |   |
|   |   |   +---zone
|   |   |
|   |   +---dot1x
|   |   |   |
|   |   |   +---access-control
|   |   |   |
|   |   |   +---show version-information
|   |   |
|   |   +---location
|   |   |
|   |   +---macsec
|   |   |   |
|   |   |   +---gcm-aes-128
|   |   |   |
|   |   |   +---gcm-aes-256
|   |   |
|   |   +---name
|   |   |
|   |   +---syslog
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---facility
|   |   |   |
|   |   |   +---port
|   |   |   |
|   |   |   +---severity-level
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show statistics
|   |   |
|   |   +---show cpu-utilization
|   |   |
|   |   +---show date-and-time
|   |   |
|   |   +---show device-information
|   |   |
|   |   +---show license
|   |   |
|   |   +---show memory
|   |
|   +---terminal
|   |   |
|   |   +---baud-rate
|   |   |
|   |   +---length
|   |   |
|   |   +---timeout
|   |
|   +---test
|   |   |
|   |   +---rfc2544
|   |   |   |
|   |   |   +---profile-name
|   |   |   |   |
|   |   |   |   +---frame-size
|   |   |   |   |
|   |   |   |   +---pattern
|   |   |   |
|   |   |   +---test
|   |   |   |   |
|   |   |   |   +---activate
|   |   |   |   |
|   |   |   |   +---associated-flow
|   |   |   |   |
|   |   |   |   +---clear-reports
|   |   |   |   |
|   |   |   |   +---max-rate
|   |   |   |   |
|   |   |   |   +---max-test-duration
|   |   |   |   |
|   |   |   |   +---test-profile
|   |   |   |   |
|   |   |   |   +---type
|   |   |   |   |
|   |   |   |   +---show report
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |   |
|   |   |   |   +---show summary
|   |
|   +---show cards-summary
|   |
|   +---show peer-summary
|
+---file
|   |
|   +---copy
|   |
|   +---delete
|   |
|   +---dir
|   |
|   +---show copy
|   |
|   +---show sw-pack
|
+---logon

Global commands:
|
+---commit
|
+---discard-changes
|
+---echo
|
+---exec
|
+---exit
|
+---help
|
+---history
|
+---info
|
+---level-info
|
+---logout
|
+---ping
|
+---sanity-check
|
+---save
|
+---startup-config-confirm
|
+---tree
|
+---virtual-terminal
```
