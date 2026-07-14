# mp1 command tree (family: mp1)

Captured live from mp-one (MP-1 lab unit (provisional mp1 family - shared context-CLI assumed, NOT verified live)) via the root `tree` command on 2026-07-14
by scripts/harvest_cli.py — re-run `harvest` after firmware upgrades; the
tree is re-captured fresh each run. Use it to locate which context holds a
feature, then cli-reference-mp1.md / the cli_help tool for exact,
firmware-current argument syntax.

Legend from the CLI's own `?` listings: `+` = sub-context you can enter,
`-` = command/leaf, `[no]` prefix = removable with `no <leaf>`.

```
|
+---admin
|   |
|   +---factory-default-all
|   |
|   +---factory-default
|   |
|   +---reboot
|   |
|   +---scheduler
|   |   |
|   |   +---clear-finished-schedules
|   |   |
|   |   +---clear-schedule-log
|   |   |
|   |   +---show scheduler
|   |   |
|   |   +---show scheduler-details
|   |
|   +---software
|   |   |
|   |   +---install
|   |   |
|   |   +---undo-install
|   |   |
|   |   +---show status
|   |
|   +---user-default
|   |
|   +---show reboot
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
|   |   |   |
|   |   |   +---remark
|   |   |
|   |   +---logging
|   |   |
|   |   +---resequence
|   |
|   +---bridge
|   |   |
|   |   +---aging-time
|   |   |
|   |   +---clear-mac-table
|   |   |
|   |   +---name
|   |   |
|   |   +---port
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---vlan
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---tagged-egress
|   |   |
|   |   +---show mac-table
|   |   |
|   |   +---show vlans
|   |
|   +---chassis
|   |   |
|   |   +---inventory
|   |   |   |
|   |   |   +---alias
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---temperature-threshold
|   |   |
|   |   +---show environment
|   |   |
|   |   +---show summary-inventory
|   |
|   +---cross-connect
|   |   |
|   |   +---ds0
|   |   |
|   |   +---pw-tdm
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
|   |   |   +---egress-port
|   |   |   |
|   |   |   +---ingress-port
|   |   |   |
|   |   |   +---reverse-direction
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---vlan-tag
|   |   |   |
|   |   |   +---show status
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
|   |   |   +---sftp-server
|   |   |   |
|   |   |   +---snmp
|   |   |   |
|   |   |   +---ssh
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
|   |   |   |
|   |   |   +---show statistics
|   |   |
|   |   +---dscp
|   |   |
|   |   +---login-user
|   |   |   |
|   |   |   +---authentication-method
|   |   |   |
|   |   |   +---level
|   |   |   |
|   |   |   +---password
|   |   |   |
|   |   |   +---public-key
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---management-address
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
|   |   |   +---bootstrap-notification
|   |   |   |
|   |   |   +---community
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---sec-name
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---tag
|   |   |   |
|   |   |   +---config-change-notification
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
|   |   |   +---snmp-engine-id
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
|   |   |   +---trap-sync-group
|   |   |   |   |
|   |   |   |   +---tag-list
|   |   |   |   |
|   |   |   |   +---target-params
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
|   |   |   |
|   |   |   +---show snmpv3
|   |   |   |
|   |   |   +---show trap-sync
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
|   |   +---user
|   |   |
|   |   +---show ssh-server
|   |   |
|   |   +---show users-details
|   |   |
|   |   +---show users
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
|   |   +---ds1
|   |   |   |
|   |   |   +---clear-bert-counters
|   |   |   |
|   |   |   +---line-type
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---e1
|   |   |   |
|   |   |   +---clear-bert-counters
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---idle-code
|   |   |   |
|   |   |   +---interface-type
|   |   |   |
|   |   |   +---line-type
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---out-of-service
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---rx-sensitivity
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tx-clock-source
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ethernet
|   |   |   |
|   |   |   +---auto-negotiation
|   |   |   |
|   |   |   +---clear-statistics
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
|   |   |   +---queue-mapping
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---speed-duplex
|   |   |   |
|   |   |   +---show sfp-status
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---logical-mac
|   |   |
|   |   +---mng-ethernet
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---pcs
|   |   |
|   |   +---pdh-frame-type
|   |   |
|   |   +---serial
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---cts-rts
|   |   |   |
|   |   |   +---encapsulation-mode
|   |   |   |
|   |   |   +---end-to-end-control
|   |   |   |
|   |   |   +---interface
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---mode
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---rate
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---svi
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---t1
|   |   |   |
|   |   |   +---clear-bert-counters
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---idle-code
|   |   |   |
|   |   |   +---line-buildout
|   |   |   |
|   |   |   +---line-code
|   |   |   |
|   |   |   +---line-interface
|   |   |   |
|   |   |   +---line-length
|   |   |   |
|   |   |   +---line-type
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---out-of-service
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tx-clock-source
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show summary
|   |   |
|   |   +---show svi-summary
|   |
|   +---protection
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
|   |   |   +---manual-switch-to-protection
|   |   |   |
|   |   |   +---manual-switch-to-working
|   |   |   |
|   |   |   +---revertive
|   |   |   |
|   |   |   +---wait-to-restore
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show summary-tdm-group
|   |
|   +---pwe
|   |   |
|   |   +---pw
|   |   |   |
|   |   |   +---arp-table-refresh
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---description
|   |   |   |
|   |   |   +---domain-failure-indication
|   |   |   |
|   |   |   +---egress-port
|   |   |   |
|   |   |   +---exp-bits
|   |   |   |
|   |   |   +---jitter-buffer
|   |   |   |
|   |   |   +---jitter-buffer-centering
|   |   |   |
|   |   |   +---label
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---peer
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---shutdown
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
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show summary
|   |
|   +---qos
|   |   |
|   |   +---policer-profile
|   |   |   |
|   |   |   +---bandwidth
|   |   |
|   |   +---queue-block-profile
|   |   |   |
|   |   |   +---queue
|   |   |   |   |
|   |   |   |   +---internal-profile
|   |   |
|   |   +---queue-group-profile
|   |   |   |
|   |   |   +---queue-block
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---profile
|   |   |   |   |
|   |   |   |   +---shaper
|   |   |
|   |   +---queue-internal-profile
|   |   |   |
|   |   |   +---scheduling
|   |   |
|   |   +---queue-map-profile
|   |   |   |
|   |   |   +---map
|   |   |
|   |   +---shaper-profile
|   |   |   |
|   |   |   +---bandwidth
|   |
|   +---reporting
|   |   |
|   |   +---acknowledge
|   |   |
|   |   +---active-alarm-rebuild
|   |   |
|   |   +---alarm-input
|   |   |
|   |   +---alarm-source-attribute
|   |   |
|   |   +---alarm-source-type-attribute
|   |   |
|   |   +---clear-alarm-log
|   |   |
|   |   +---led-blink
|   |   |
|   |   +---log-file-timestamp-type
|   |   |
|   |   +---low-memory-alarm
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
|   |   +---show brief-alarm-log
|   |   |
|   |   +---show brief-log
|   |   |
|   |   +---show event-information
|   |   |
|   |   +---show event-list
|   |   |
|   |   +---show led-blink-status
|   |   |
|   |   +---show log
|   |   |
|   |   +---show log-summary
|   |
|   +---router
|   |   |
|   |   +---arp-timeout
|   |   |
|   |   +---clear-arp-table
|   |   |
|   |   +---clear-statistics
|   |   |
|   |   +---interface
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---management-access
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---name
|   |   |
|   |   +---static-route
|   |   |
|   |   +---show arp-table
|   |   |
|   |   +---show routing-table
|   |   |
|   |   +---show statistics
|   |   |
|   |   +---show summary-interface
|   |
|   +---system
|   |   |
|   |   +---announcement
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
|   |   |   |   |   +---wait-to-restore
|   |   |   |   |   |
|   |   |   |   |   +---show status
|   |   |   |   |
|   |   |   |   +---sync-network-type
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
|   |   |   |   +---rx-sensitivity
|   |   |   |   |
|   |   |   |   +---shutdown
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
|   |   |   +---summer-time
|   |   |   |
|   |   |   +---time
|   |   |   |
|   |   |   +---zone
|   |   |   |
|   |   |   +---show summer-time
|   |   |
|   |   +---location
|   |   |
|   |   +---login-message
|   |   |
|   |   +---name
|   |   |
|   |   +---syslog
|   |   |   |
|   |   |   +---accounting
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
|   |   +---show copyright
|   |   |
|   |   +---show device-information
|   |   |
|   |   +---show memory
|   |   |
|   |   +---show memory-details
|   |   |
|   |   +---show system-date
|   |   |
|   |   +---show tech-support
|   |
|   +---terminal
|   |   |
|   |   +---baud-rate
|   |   |
|   |   +---length
|   |   |
|   |   +---serial-port-disable
|   |   |
|   |   +---timeout
|   |
|   +---show peer-summary
|
+---file
|   |
|   +---delete
|   |
|   +---dir
|   |
|   +---show banner-text
|   |
|   +---show configuration-files
|   |
|   +---show copy
|   |
|   +---show factory-default-config
|   |
|   +---show schedule-log
|   |
|   +---show script-result
|   |
|   +---show startup-config
|   |
|   +---show sw-pack
|   |
|   +---show user-default-config
|   |
|   +---show user-script
|
+---logon
|
+---on-configuration-error

Global commands:
|
+---commit
|
+---copy
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
+---popup-suspend
|
+---sanity-check
|
+---save
|
+---schedule
|
+---telnet
|
+---trace-route
|
+---tree
```
