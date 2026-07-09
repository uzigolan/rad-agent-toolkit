# etx2 command tree (family: etx2)

Captured live from etx2i (ETX-2I (Hw 0.2/D, Sw 6.8.5(1.116)) - FIRST live etx2 driver verification; industrial variant of the ETX-2 line) via the root `tree` command on 2026-07-09
by scripts/harvest_cli.py — re-run `harvest` after firmware upgrades; the
tree is re-captured fresh each run. Use it to locate which context holds a
feature, then cli-reference-etx2.md / the cli_help tool for exact,
firmware-current argument syntax.

Legend from the CLI's own `?` listings: `+` = sub-context you can enter,
`-` = command/leaf, `[no]` prefix = removable with `no <leaf>`.

```
|
+---admin
|   |
|   +---access-level
|   |
|   +---auto-save
|   |
|   +---factory-default-all
|   |
|   +---factory-default
|   |
|   +---force-reboot
|   |
|   +---license
|   |   |
|   |   +---license-enable
|   |   |
|   |   +---show summary
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
|   +---send
|   |
|   +---software
|   |   |
|   |   +---install
|   |   |
|   |   +---software-confirm-required
|   |   |
|   |   +---undo-install
|   |   |
|   |   +---show status
|   |
|   +---startup-confirm-required
|   |
|   +---user-default
|   |
|   +---show reboot
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
|   |   +---duplicate-mac-rejection
|   |   |
|   |   +---filtering
|   |   |
|   |   +---mld-snooping
|   |   |   |
|   |   |   +---host-aging-interval
|   |   |   |
|   |   |   +---router-aging-interval
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---static-group
|   |   |   |
|   |   |   +---static-router-port
|   |   |   |
|   |   |   +---vlan
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---mode
|   |   |
|   |   +---name
|   |   |
|   |   +---port
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---spanning-tree
|   |   |   |   |
|   |   |   |   +---admin-edge
|   |   |   |   |
|   |   |   |   +---auto-edge
|   |   |   |   |
|   |   |   |   +---cost
|   |   |   |   |
|   |   |   |   +---mcheck
|   |   |   |   |
|   |   |   |   +---mst
|   |   |   |   |   |
|   |   |   |   |   +---cost
|   |   |   |   |   |
|   |   |   |   |   +---priority
|   |   |   |   |   |
|   |   |   |   |   +---show status
|   |   |   |   |
|   |   |   |   +---priority
|   |   |   |   |
|   |   |   |   +---restricted-role
|   |   |   |   |
|   |   |   |   +---restricted-tcn
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---show status
|   |   |
|   |   +---root
|   |   |
|   |   +---spanning-tree
|   |   |   |
|   |   |   +---forward-time
|   |   |   |
|   |   |   +---hello-time
|   |   |   |
|   |   |   +---max-age
|   |   |   |
|   |   |   +---max-hops
|   |   |   |
|   |   |   +---mode
|   |   |   |
|   |   |   +---mst
|   |   |   |   |
|   |   |   |   +---priority
|   |   |   |   |
|   |   |   |   +---vlan
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---priority
|   |   |   |
|   |   |   +---revision-level
|   |   |   |
|   |   |   +---tx-hold-count
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---static-mac
|   |   |
|   |   +---vlan
|   |   |   |
|   |   |   +---maximum-mac-addresses
|   |   |   |
|   |   |   +---mode
|   |   |
|   |   +---vlan-aware
|   |   |
|   |   +---show mac-address-table
|   |   |
|   |   +---show mac-address-table
|   |   |
|   |   +---show mac-table
|   |   |
|   |   +---show mac-table
|   |   |
|   |   +---show vlans
|   |
|   +---chassis
|   |   |
|   |   +---overheat-auto-shutdown
|   |   |
|   |   +---temperature-threshold
|   |   |
|   |   +---show environment
|   |
|   +---cross-connect
|   |   |
|   |   +---pw-tdm
|   |
|   +---crypto
|   |   |
|   |   +---ca
|   |   |   |
|   |   |   +---ocsp
|   |   |   |
|   |   |   +---revocation-check
|   |   |
|   |   +---crypto-map
|   |   |   |
|   |   |   +---ike-identity-local
|   |   |   |
|   |   |   +---ike-identity-remote
|   |   |   |
|   |   |   +---ike-sa-lifetime
|   |   |   |
|   |   |   +---ike-sa-negotiation
|   |   |   |
|   |   |   +---match-address
|   |   |   |
|   |   |   +---match-destination
|   |   |   |
|   |   |   +---match-source
|   |   |   |
|   |   |   +---peer-address
|   |   |   |
|   |   |   +---pfs-group
|   |   |   |
|   |   |   +---sa-lifetime
|   |   |   |
|   |   |   +---sequence-number
|   |   |   |
|   |   |   +---transform-set
|   |   |
|   |   +---ipsec-transform-set
|   |   |   |
|   |   |   +---algorithms
|   |   |   |
|   |   |   +---mode
|   |   |
|   |   +---isakmp-identity
|   |   |
|   |   +---isakmp-key
|   |   |
|   |   +---isakmp-policy
|   |   |   |
|   |   |   +---authentication
|   |   |   |
|   |   |   +---encryption
|   |   |   |
|   |   |   +---group
|   |   |   |
|   |   |   +---hash
|   |   |
|   |   +---key
|   |   |   |
|   |   |   +---generate-rsa
|   |   |   |
|   |   |   +---show public-key-rsa
|   |   |
|   |   +---pki
|   |   |   |
|   |   |   +---authenticate
|   |   |   |
|   |   |   +---delete-certificate
|   |   |   |
|   |   |   +---enroll
|   |   |   |
|   |   |   +---import-certificate
|   |   |   |
|   |   |   +---show certificate
|   |   |   |
|   |   |   +---show certificate-summary
|   |
|   +---etps
|   |   |
|   |   +---etp
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---port
|   |   |   |   |
|   |   |   |   +---loopback
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---show loopback
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---protection
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---master-etp
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---show flows-summary
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
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
|   |   |   +---action-on-group
|   |   |   |
|   |   |   +---holdoff
|   |   |   |
|   |   |   +---trigger
|   |   |   |
|   |   |   +---wait-to-restore
|   |
|   +---flows
|   |   |
|   |   +---classifier-profile
|   |   |   |
|   |   |   +---match
|   |   |
|   |   +---clear-flow-mac-table
|   |   |
|   |   +---flow
|   |   |   |
|   |   |   +---classifier
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---drop
|   |   |   |
|   |   |   +---egress-port
|   |   |   |
|   |   |   +---ingress-color
|   |   |   |
|   |   |   +---l2cp
|   |   |   |
|   |   |   +---mac-learning
|   |   |   |
|   |   |   +---mark
|   |   |   |   |
|   |   |   |   +---inner-marking-profile
|   |   |   |   |
|   |   |   |   +---inner-p-bit
|   |   |   |   |
|   |   |   |   +---inner-tag-ether-type
|   |   |   |   |
|   |   |   |   +---inner-vlan
|   |   |   |   |
|   |   |   |   +---ip
|   |   |   |   |
|   |   |   |   +---mac
|   |   |   |   |
|   |   |   |   +---marking-profile
|   |   |   |   |
|   |   |   |   +---p-bit
|   |   |   |   |
|   |   |   |   +---tag-ether-type
|   |   |   |   |
|   |   |   |   +---vlan
|   |   |   |
|   |   |   +---marking-profile
|   |   |   |
|   |   |   +---multi-cos-counters
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---policer
|   |   |   |
|   |   |   +---rate-measure
|   |   |   |
|   |   |   +---rate-sampling-window
|   |   |   |
|   |   |   +---reverse-direction
|   |   |   |
|   |   |   +---service-name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---test
|   |   |   |
|   |   |   +---vlan-tag
|   |   |   |
|   |   |   +---show rate
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |   |
|   |   |   +---show test
|   |   |
|   |   +---rate-sampling-window
|   |   |
|   |   +---rename
|   |   |
|   |   +---service-ping
|   |   |
|   |   +---service-ping-response
|   |   |
|   |   +---statistics-count-oam
|   |   |
|   |   +---show service-ping-status
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
|   |   |   +---command-authorization
|   |   |   |
|   |   |   +---sftp
|   |   |   |
|   |   |   +---sftp-server
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
|   |   |   +---ssh-server
|   |   |   |   |
|   |   |   |   +---trusted-ca
|   |   |   |
|   |   |   +---telnet
|   |   |   |
|   |   |   +---tftp
|   |   |   |
|   |   |   +---ztc-xml-generate-encrypted-password
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
|   |   |   +---inactivity-timeout
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
|   |   +---netconf
|   |   |   |
|   |   |   +---inactivity-timeout
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---radius
|   |   |   |
|   |   |   +---clear-statistics
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
|   |   |   |   |
|   |   |   |   +---show credentials
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
|   |   |   |   |
|   |   |   |   +---single-server-accounting
|   |   |   |
|   |   |   +---privilege-level
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
|   |   |   |   +---priority
|   |   |   |   |
|   |   |   |   +---retry
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---timeout
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |
|   |   |   +---server-selection
|   |   |   |
|   |   |   +---wait-to-restore-server
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---user
|   |   |
|   |   +---show failed-login-attempts
|   |   |
|   |   +---show ssh-server
|   |   |
|   |   +---show users-details
|   |   |
|   |   +---show users
|   |
|   +---mirroring-session
|   |   |
|   |   +---destination
|   |   |
|   |   +---shutdown
|   |   |
|   |   +---source
|   |
|   +---oam
|   |   |
|   |   +---cfm
|   |   |   |
|   |   |   +---alarm-type
|   |   |   |
|   |   |   +---availability
|   |   |   |
|   |   |   +---ltr
|   |   |   |
|   |   |   +---maintenance-domain
|   |   |   |   |
|   |   |   |   +---maintenance-association
|   |   |   |   |   |
|   |   |   |   |   +---ccm-interval
|   |   |   |   |   |
|   |   |   |   |   +---classification
|   |   |   |   |   |
|   |   |   |   |   +---interface-status-tlv
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
|   |   |   |   |   |   +---clear-dynamic-rmep
|   |   |   |   |   |   |
|   |   |   |   |   |   +---clear-statistics
|   |   |   |   |   |   |
|   |   |   |   |   |   +---client-md-level
|   |   |   |   |   |   |
|   |   |   |   |   |   +---continuity-verification
|   |   |   |   |   |   |
|   |   |   |   |   |   +---customer-tags-excluded
|   |   |   |   |   |   |
|   |   |   |   |   |   +---dest-addr-type
|   |   |   |   |   |   |
|   |   |   |   |   |   +---dest-mac-addr
|   |   |   |   |   |   |
|   |   |   |   |   |   +---direction
|   |   |   |   |   |   |
|   |   |   |   |   |   +---flow
|   |   |   |   |   |   |
|   |   |   |   |   |   +---forwarding-method
|   |   |   |   |   |   |
|   |   |   |   |   |   +---lbm
|   |   |   |   |   |   |
|   |   |   |   |   |   +---linktrace
|   |   |   |   |   |   |
|   |   |   |   |   |   +---mef46-ll
|   |   |   |   |   |   |
|   |   |   |   |   |   +---queue
|   |   |   |   |   |   |
|   |   |   |   |   |   +---remote-mep
|   |   |   |   |   |   |
|   |   |   |   |   |   +---rmep-learning
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
|   |   |   |   |   |   |   |   +---bck-delay-var-bin
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---clear-statistics
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---delay
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---delay-measurement-bin
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---delay-var-measurement-bin
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---description
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---fwd-delay-var-bin
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---loss
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---on-demand-test
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---activate
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---dmm-data-tlv-length
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---duration
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---message-interval
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---slm-data-tlv-length
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---slm-test-id
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---type
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   +---show report
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---pm-collection
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---remote
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---show statistics
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   +---show statistics
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---dmm-interval
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---lmm-interval
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---pbit-agnostic
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---pm-collection
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---shutdown
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---show statistics
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   +---show statistics
|   |   |   |   |   |   |
|   |   |   |   |   |   +---shutdown
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show lbm-results
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show linktrace-results
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show mef46-ll-status
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show remote-mep-status
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show statistics
|   |   |   |   |   |   |
|   |   |   |   |   |   +---show status
|   |   |   |   |   |
|   |   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---md-level
|   |   |   |   |
|   |   |   |   +---mip
|   |   |   |   |   |
|   |   |   |   |   +---bind
|   |   |   |   |   |
|   |   |   |   |   +---flow
|   |   |   |   |   |
|   |   |   |   |   +---shutdown
|   |   |   |   |   |
|   |   |   |   |   +---show status
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
|   |   |   +---mip-assign
|   |   |   |
|   |   |   +---multicast-addr
|   |   |   |
|   |   |   +---multi-mep-per-evc
|   |   |   |
|   |   |   +---show mips
|   |   |   |
|   |   |   +---show on-demand-tests
|   |   |   |
|   |   |   +---show summary
|   |   |
|   |   +---efm
|   |   |   |
|   |   |   +---descriptor
|   |   |
|   |   +---twamp
|   |   |   |
|   |   |   +---controller
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---local-ip-address
|   |   |   |   |
|   |   |   |   +---peer
|   |   |   |   |   |
|   |   |   |   |   +---activate
|   |   |   |   |   |
|   |   |   |   |   +---show report
|   |   |   |   |   |
|   |   |   |   |   +---show report-all
|   |   |   |   |   |
|   |   |   |   |   +---show status
|   |   |   |   |   |
|   |   |   |   |   +---show summary-report
|   |   |   |   |
|   |   |   |   +---router-entity
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---vlan-tag
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---profile
|   |   |   |   |
|   |   |   |   +---delay-threshold
|   |   |   |   |
|   |   |   |   +---delay-variation-event-type
|   |   |   |   |
|   |   |   |   +---delay-variation-threshold
|   |   |   |   |
|   |   |   |   +---loss-ratio-threshold
|   |   |   |   |
|   |   |   |   +---loss-timeout
|   |   |   |   |
|   |   |   |   +---payload-length
|   |   |   |   |
|   |   |   |   +---transmit-rate
|   |   |   |
|   |   |   +---responder
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---local-ip-address
|   |   |   |   |
|   |   |   |   +---pbit-copy
|   |   |   |   |
|   |   |   |   +---router-entity
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---test-session
|   |   |   |   |
|   |   |   |   +---tx-extended-info
|   |   |   |   |
|   |   |   |   +---tx-seq-num
|   |   |   |   |
|   |   |   |   +---vlan-tag
|   |   |   |   |
|   |   |   |   +---show status
|   |
|   +---peer
|   |
|   +---port
|   |   |
|   |   +---cellular
|   |   |   |
|   |   |   +---apn-name
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---dialer-number
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pin
|   |   |   |
|   |   |   +---radio-access-technology
|   |   |   |
|   |   |   +---rssi-threshold
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---clear-statistics
|   |   |
|   |   +---ds1
|   |   |   |
|   |   |   +---frame-type
|   |   |
|   |   +---ethernet
|   |   |   |
|   |   |   +---auto-fec-policy
|   |   |   |
|   |   |   +---auto-negotiation
|   |   |   |
|   |   |   +---classification-key
|   |   |   |
|   |   |   +---classifier
|   |   |   |   |
|   |   |   |   +---comment
|   |   |   |   |
|   |   |   |   +---delete
|   |   |   |   |
|   |   |   |   +---drop
|   |   |   |   |
|   |   |   |   +---match
|   |   |   |   |
|   |   |   |   +---resequence
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---clear-efm-statistics
|   |   |   |
|   |   |   +---clear-l2cp-statistics
|   |   |   |
|   |   |   +---clear-queue-statistics
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---dhcp-trust
|   |   |   |
|   |   |   +---dot1x
|   |   |   |   |
|   |   |   |   +---authenticator
|   |   |   |   |   |
|   |   |   |   |   +---authentication
|   |   |   |   |   |
|   |   |   |   |   +---reauthentication
|   |   |   |   |   |
|   |   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---clear-statistics
|   |   |   |   |
|   |   |   |   +---initialize
|   |   |   |   |
|   |   |   |   +---show message-log
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---efm
|   |   |   |   |
|   |   |   |   +---loopback
|   |   |   |   |
|   |   |   |   +---snmp-tunneling
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---fec
|   |   |   |
|   |   |   +---l2cp
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---max-capability
|   |   |   |
|   |   |   +---max-ql
|   |   |   |
|   |   |   +---multi-policer
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---policer
|   |   |   |
|   |   |   +---queue-group
|   |   |   |
|   |   |   +---rate-measure
|   |   |   |
|   |   |   +---self-tuning
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tag-ethernet-type
|   |   |   |
|   |   |   +---tx-ssm
|   |   |   |
|   |   |   +---show l2cp-statistics
|   |   |   |
|   |   |   +---show loopback
|   |   |   |
|   |   |   +---show oam-efm
|   |   |   |
|   |   |   +---show oam-efm-statistics
|   |   |   |
|   |   |   +---show queue-statistics
|   |   |   |
|   |   |   +---show rate
|   |   |   |
|   |   |   +---show sfp-extended-information
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
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
|   |   |   +---vcat-header
|   |   |   |
|   |   |   +---show bind
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---hdlc
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---show bind
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---int-ethernet
|   |   |   |
|   |   |   +---classification-key
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---dhcp-trust
|   |   |   |
|   |   |   +---name
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
|   |   |   +---anchor-port
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
|   |   |   +---minimum-link-number
|   |   |   |
|   |   |   +---mode
|   |   |   |
|   |   |   +---name
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
|   |   |   +---classification-key
|   |   |   |
|   |   |   +---classifier
|   |   |   |   |
|   |   |   |   +---comment
|   |   |   |   |
|   |   |   |   +---delete
|   |   |   |   |
|   |   |   |   +---drop
|   |   |   |   |
|   |   |   |   +---match
|   |   |   |   |
|   |   |   |   +---resequence
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---clear-efm-statistics
|   |   |   |
|   |   |   +---clear-l2cp-statistics
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---dhcp-trust
|   |   |   |
|   |   |   +---efm
|   |   |   |   |
|   |   |   |   +---loopback
|   |   |   |   |
|   |   |   |   +---snmp-tunneling
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---l2cp
|   |   |   |
|   |   |   +---l2pt-network
|   |   |   |
|   |   |   +---lldp
|   |   |   |   |
|   |   |   |   +---802.1-protocol-identity
|   |   |   |   |
|   |   |   |   +---clear-statistics
|   |   |   |   |
|   |   |   |   +---nearest-bridge-802.3
|   |   |   |   |
|   |   |   |   +---nearest-bridge-basic-management
|   |   |   |   |
|   |   |   |   +---nearest-bridge-mode
|   |   |   |   |
|   |   |   |   +---show neighbors-details
|   |   |   |   |
|   |   |   |   +---show neighbors-summary
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |
|   |   |   +---loopback
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
|   |   |   |
|   |   |   +---show l2cp-statistics
|   |   |   |
|   |   |   +---show loopback
|   |   |   |
|   |   |   +---show oam-efm
|   |   |   |
|   |   |   +---show oam-efm-statistics
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---mng-ethernet
|   |   |   |
|   |   |   +---pm-collection
|   |   |
|   |   +---ppp
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---chap-hostname
|   |   |   |
|   |   |   +---chap-password
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pap-username
|   |   |   |
|   |   |   +---pppoe
|   |   |   |   |
|   |   |   |   +---service-name
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---refuse-chap
|   |   |   |
|   |   |   +---refuse-no-auth
|   |   |   |
|   |   |   +---refuse-pap
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---queue-statistics
|   |   |
|   |   +---rate-sampling-window
|   |   |
|   |   +---sdh-sonet
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---frame-type
|   |   |   |
|   |   |   +---loopback
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pm-enable
|   |   |   |
|   |   |   +---threshold
|   |   |   |
|   |   |   +---tx-clock-source
|   |   |   |
|   |   |   +---show bind
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---smart-sfp
|   |   |   |
|   |   |   +---reset
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---type
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---svi
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---tag-ether-type
|   |   |
|   |   +---vdsl2
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---xml-export
|   |   |
|   |   +---show statistics
|   |   |
|   |   +---show summary-full-name
|   |   |
|   |   +---show summary
|   |
|   +---protection
|   |   |
|   |   +---erp
|   |   |   |
|   |   |   +---backward-compatibility
|   |   |   |
|   |   |   +---bridge
|   |   |   |
|   |   |   +---clear
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---color-mapping
|   |   |   |
|   |   |   +---cos-mapping
|   |   |   |
|   |   |   +---description
|   |   |   |
|   |   |   +---east-port
|   |   |   |
|   |   |   +---force-switch
|   |   |   |
|   |   |   +---interconnection-node
|   |   |   |
|   |   |   +---manual-switch
|   |   |   |
|   |   |   +---passthrough-vlan
|   |   |   |
|   |   |   +---port-description
|   |   |   |
|   |   |   +---port-type
|   |   |   |
|   |   |   +---r-aps
|   |   |   |
|   |   |   +---revertive
|   |   |   |
|   |   |   +---ring-id
|   |   |   |
|   |   |   +---sf-trigger
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---sub-ring
|   |   |   |
|   |   |   +---timers
|   |   |   |
|   |   |   +---topology-change-propagation
|   |   |   |
|   |   |   +---vlan
|   |   |   |   |
|   |   |   |   +---queue-block
|   |   |   |   |
|   |   |   |   +---service-name
|   |   |   |   |
|   |   |   |   +---shutdown
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
|   |   |   +---force-active-port
|   |   |   |
|   |   |   +---oper-mode
|   |   |   |
|   |   |   +---revertive
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tx-down-duration-upon-flip
|   |   |   |
|   |   |   +---wait-to-restore
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show erp-summary
|   |
|   +---pwe
|   |   |
|   |   +---pw
|   |   |   |
|   |   |   +---cas-frames-per-packet
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---description
|   |   |   |
|   |   |   +---dscp
|   |   |   |
|   |   |   +---egress-port
|   |   |   |
|   |   |   +---exp-bits
|   |   |   |
|   |   |   +---ip-priority-type
|   |   |   |
|   |   |   +---jitter-buffer
|   |   |   |
|   |   |   +---label
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---oam
|   |   |   |
|   |   |   +---peer
|   |   |   |
|   |   |   +---pm-enable
|   |   |   |
|   |   |   +---psn-oos
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tdm-payload
|   |   |   |
|   |   |   +---tos
|   |   |   |
|   |   |   +---udp-mux-method
|   |   |   |
|   |   |   +---show connectivity-statistics
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show summary
|   |
|   +---qos
|   |   |
|   |   +---bandwidth-round-up
|   |   |
|   |   +---color-map-profile
|   |   |   |
|   |   |   +---map
|   |   |
|   |   +---cos-map-profile
|   |   |   |
|   |   |   +---map
|   |   |   |
|   |   |   +---non-ip-map
|   |   |   |
|   |   |   +---untagged-map
|   |   |
|   |   +---envelope-profile
|   |   |   |
|   |   |   +---cf-policy
|   |   |   |
|   |   |   +---color-aware
|   |   |   |
|   |   |   +---compensation
|   |   |   |
|   |   |   +---cos
|   |   |   |   |
|   |   |   |   +---bandwidth
|   |   |   |
|   |   |   +---coupling-flag-0
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---envelope-ranks
|   |   |
|   |   +---marking-profile
|   |   |   |
|   |   |   +---mark
|   |   |   |
|   |   |   +---mark-dscp-code
|   |   |   |
|   |   |   +---mark
|   |   |
|   |   +---policer-aggregate
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---policer
|   |   |   |
|   |   |   +---rate-sampling-window
|   |   |   |
|   |   |   +---show flows
|   |   |   |
|   |   |   +---show statistics
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
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---queue-block-profile
|   |   |   |
|   |   |   +---queue
|   |   |   |   |
|   |   |   |   +---congestion-avoidance
|   |   |   |   |
|   |   |   |   +---depth
|   |   |   |   |
|   |   |   |   +---frame-buffers
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
|   |   |   |
|   |   |   +---show status
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
|   |   +---alarm-source-attribute
|   |   |
|   |   +---alarm-source-type-attribute
|   |   |
|   |   +---clear-accounting-log
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
|   |   +---pm-csv
|   |   |
|   |   +---pm-file-push
|   |   |
|   |   +---soaking-time
|   |   |
|   |   +---show accounting-log
|   |   |
|   |   +---show active-alarms
|   |   |
|   |   +---show active-alarms-details
|   |   |
|   |   +---show alarm-information
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
|   |   +---bfd-neighbor
|   |   |
|   |   +---bgp
|   |   |   |
|   |   |   +---clear-neighbor
|   |   |   |
|   |   |   +---ipv4-unicast-af
|   |   |   |   |
|   |   |   |   +---external-preference
|   |   |   |   |
|   |   |   |   +---internal-preference
|   |   |   |   |
|   |   |   |   +---neighbor
|   |   |   |   |   |
|   |   |   |   |   +---active
|   |   |   |   |   |
|   |   |   |   |   +---prefix-list-bind
|   |   |   |   |   |
|   |   |   |   |   +---route-map-bind
|   |   |   |   |   |
|   |   |   |   |   +---show advertised-route
|   |   |   |   |   |
|   |   |   |   |   +---show prefix-list
|   |   |   |   |   |
|   |   |   |   |   +---show received-route
|   |   |   |   |   |
|   |   |   |   |   +---show route-map
|   |   |   |   |
|   |   |   |   +---network
|   |   |   |   |
|   |   |   |   +---redistribute
|   |   |   |
|   |   |   +---ipv6-unicast-af
|   |   |   |   |
|   |   |   |   +---external-preference
|   |   |   |   |
|   |   |   |   +---internal-preference
|   |   |   |   |
|   |   |   |   +---neighbor
|   |   |   |   |   |
|   |   |   |   |   +---active
|   |   |   |   |   |
|   |   |   |   |   +---prefix-list-bind
|   |   |   |   |   |
|   |   |   |   |   +---route-map-bind
|   |   |   |   |   |
|   |   |   |   |   +---show advertised-route
|   |   |   |   |   |
|   |   |   |   |   +---show prefix-list
|   |   |   |   |   |
|   |   |   |   |   +---show received-route
|   |   |   |   |   |
|   |   |   |   |   +---show route-map
|   |   |   |   |
|   |   |   |   +---network
|   |   |   |   |
|   |   |   |   +---redistribute
|   |   |   |
|   |   |   +---neighbor
|   |   |   |   |
|   |   |   |   +---local-address
|   |   |   |   |
|   |   |   |   +---max-prefixes
|   |   |   |   |
|   |   |   |   +---password
|   |   |   |   |
|   |   |   |   +---remote-as
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---timers
|   |   |   |   |
|   |   |   |   +---show neighbor-connection
|   |   |   |
|   |   |   +---router-id
|   |   |   |
|   |   |   +---shutdown

|   |   |   |
|   |   |   +---show community
|   |   |   |
|   |   |   +---show rib
|   |   |   |
|   |   |   +---show summary
|   |   |
|   |   +---clear-arp-table
|   |   |
|   |   +---clear-bfd-statistics
|   |   |
|   |   +---clear-dns-proxy-cache
|   |   |
|   |   +---clear-neighbor-table
|   |   |
|   |   +---clear-statistics
|   |   |
|   |   +---dhcp-client
|   |   |   |
|   |   |   +---dhcpv6-option-request
|   |   |   |
|   |   |   +---host-name
|   |   |   |
|   |   |   +---vendor-class-id
|   |   |
|   |   +---dhcp-relay-server
|   |   |
|   |   +---dscp
|   |   |
|   |   +---interface
|   |   |   |
|   |   |   +---access-group
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---bfd
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---crypto-map
|   |   |   |
|   |   |   +---dhcp
|   |   |   |
|   |   |   +---dhcp-client
|   |   |   |   |
|   |   |   |   +---client-id
|   |   |   |   |
|   |   |   |   +---release
|   |   |   |   |
|   |   |   |   +---renew
|   |   |   |
|   |   |   +---dhcp-relay
|   |   |   |
|   |   |   +---dhcpv6-client
|   |   |   |
|   |   |   +---dhcpv6-server
|   |   |   |
|   |   |   +---ip-forwarding
|   |   |   |
|   |   |   +---ipv6-address-prefix
|   |   |   |
|   |   |   +---ipv6-autoconfig
|   |   |   |
|   |   |   +---management-access
|   |   |   |
|   |   |   +---mtu
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---ntp-multicast-client
|   |   |   |
|   |   |   +---ospf
|   |   |   |   |
|   |   |   |   +---area
|   |   |   |   |
|   |   |   |   +---authentication-key
|   |   |   |   |
|   |   |   |   +---authentication-type
|   |   |   |   |
|   |   |   |   +---dead-interval
|   |   |   |   |
|   |   |   |   +---hello-interval
|   |   |   |   |
|   |   |   |   +---metric
|   |   |   |   |
|   |   |   |   +---passive
|   |   |   |   |
|   |   |   |   +---priority
|   |   |   |   |
|   |   |   |   +---retransmit-interval
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---transit-delay
|   |   |   |
|   |   |   +---pim
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---unreachables
|   |   |   |
|   |   |   +---vlan
|   |   |   |
|   |   |   +---vrrp
|   |   |   |   |
|   |   |   |   +---description
|   |   |   |   |
|   |   |   |   +---ip
|   |   |   |   |
|   |   |   |   +---preempt
|   |   |   |   |
|   |   |   |   +---priority
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---timer-advertise
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---show access-list
|   |   |   |
|   |   |   +---show crypto-maps-status
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |   |
|   |   |   +---show summary-vrrp
|   |   |
|   |   +---name
|   |   |
|   |   +---nat
|   |   |   |
|   |   |   +---clear-nat-statistics
|   |   |   |
|   |   |   +---clear-nat-translations
|   |   |   |
|   |   |   +---nat-inside-overload
|   |   |   |
|   |   |   +---nat-inside-source-static
|   |   |   |
|   |   |   +---nat-inside-source-static-port
|   |   |   |
|   |   |   +---nat-timeout
|   |   |   |
|   |   |   +---show nat-statistics
|   |   |   |
|   |   |   +---show nat-translations
|   |   |
|   |   +---nslookup
|   |   |
|   |   +---ospf
|   |   |   |
|   |   |   +---area
|   |   |   |   |
|   |   |   |   +---default-cost
|   |   |   |   |
|   |   |   |   +---nssa
|   |   |   |   |
|   |   |   |   +---range
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---stub
|   |   |   |
|   |   |   +---asbr
|   |   |   |
|   |   |   +---external-preference
|   |   |   |
|   |   |   +---graceful-restart
|   |   |   |
|   |   |   +---internal-preference
|   |   |   |
|   |   |   +---redistribute
|   |   |   |
|   |   |   +---restart-interval
|   |   |   |
|   |   |   +---router-id
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---strict-lsa-checking
|   |   |   |
|   |   |   +---show database
|   |   |   |
|   |   |   +---show interface-table
|   |   |   |
|   |   |   +---show neighbor-table
|   |   |   |
|   |   |   +---show statistics
|   |   |
|   |   +---prefix-list
|   |   |   |
|   |   |   +---delete
|   |   |   |
|   |   |   +---deny
|   |   |   |
|   |   |   +---permit
|   |   |   |
|   |   |   +---remark
|   |   |
|   |   +---resequence
|   |   |
|   |   +---route-map
|   |   |   |
|   |   |   +---delete
|   |   |   |
|   |   |   +---deny
|   |   |   |
|   |   |   +---permit
|   |   |   |
|   |   |   +---remark
|   |   |
|   |   +---static-preference
|   |   |
|   |   +---static-route
|   |   |
|   |   +---tunnel-interface
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---dscp
|   |   |   |
|   |   |   +---ip-address
|   |   |   |
|   |   |   +---key
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---nhrp-map
|   |   |   |
|   |   |   +---nhrp-nhs
|   |   |   |
|   |   |   +---nhrp-registration-timeout
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tunnel-destination
|   |   |   |
|   |   |   +---tunnel-source
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show access-list
|   |   |
|   |   +---show arp-table
|   |   |
|   |   +---show bfd-neighbors
|   |   |
|   |   +---show bfd-neighbors-details
|   |   |
|   |   +---show dns-proxy-cache
|   |   |
|   |   +---show multicast-route
|   |   |
|   |   +---show neighbor-table
|   |   |
|   |   +---show rib
|   |   |
|   |   +---show routing-table
|   |   |
|   |   +---show statistics
|   |   |
|   |   +---show summary-interface
|   |   |
|   |   +---show vrrp-summary
|   |
|   +---service
|   |   |
|   |   +---show status
|   |
|   +---system
|   |   |
|   |   +---announcement
|   |   |
|   |   +---clear-cpu-utilization
|   |   |
|   |   +---contact
|   |   |
|   |   +---date-and-time
|   |   |   |
|   |   |   +---date-format
|   |   |   |
|   |   |   +---ntp
|   |   |   |   |
|   |   |   |   +---authenticate
|   |   |   |   |
|   |   |   |   +---authentication-key
|   |   |   |   |
|   |   |   |   +---multicast-client
|   |   |   |   |
|   |   |   |   +---polling-interval
|   |   |   |   |
|   |   |   |   +---server
|   |   |   |   |   |
|   |   |   |   |   +---address
|   |   |   |   |   |
|   |   |   |   |   +---key
|   |   |   |   |   |
|   |   |   |   |   +---prefer
|   |   |   |   |   |
|   |   |   |   |   +---query-server
|   |   |   |   |   |
|   |   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---trusted-key
|   |   |   |   |
|   |   |   |   +---show status
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
|   |   |   |   |   +---shutdown
|   |   |   |   |   |
|   |   |   |   |   +---udp
|   |   |   |
|   |   |   +---summer-time
|   |   |   |
|   |   |   +---zone
|   |   |   |
|   |   |   +---show summer-time
|   |   |
|   |   +---dhcp-relay
|   |   |   |
|   |   |   +---dhcp-option-82
|   |   |   |
|   |   |   +---dhcp-snooping
|   |   |   |
|   |   |   +---source-port
|   |   |
|   |   +---dhcp-server
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear
|   |   |   |
|   |   |   +---exclude-address
|   |   |   |
|   |   |   +---pool
|   |   |   |   |
|   |   |   |   +---address-range
|   |   |   |   |
|   |   |   |   +---client-identifier
|   |   |   |   |
|   |   |   |   +---default-router
|   |   |   |   |
|   |   |   |   +---dns-server
|   |   |   |   |
|   |   |   |   +---domain-name
|   |   |   |   |
|   |   |   |   +---hardware-address
|   |   |   |   |
|   |   |   |   +---host
|   |   |   |   |
|   |   |   |   +---lease-default
|   |   |   |   |
|   |   |   |   +---netbios-name-server
|   |   |   |   |
|   |   |   |   +---netbios-node-type
|   |   |   |   |
|   |   |   |   +---network
|   |   |   |   |
|   |   |   |   +---relay-information
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show binding
|   |   |   |
|   |   |   +---show conflict
|   |   |   |
|   |   |   +---show statistics
|   |   |
|   |   +---interval-duration
|   |   |
|   |   +---inventory
|   |   |   |
|   |   |   +---alias
|   |   |   |
|   |   |   +---asset-id
|   |   |   |
|   |   |   +---serial-number
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---lldp
|   |   |   |
|   |   |   +---bridge-type
|   |   |   |
|   |   |   +---hold-multiplier
|   |   |   |
|   |   |   +---hold-time
|   |   |   |
|   |   |   +---port-description
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tx-interval
|   |   |
|   |   +---location
|   |   |
|   |   +---login-message
|   |   |
|   |   +---name
|   |   |
|   |   +---router
|   |   |   |
|   |   |   +---vrrp-ipv4-checksum-without-pseudoheader
|   |   |   |
|   |   |   +---vrrp-version
|   |   |   |
|   |   |   +---show vrrp-summary
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
|   |   |   +---hostname
|   |   |   |
|   |   |   +---port
|   |   |   |
|   |   |   +---severity-level
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show statistics
|   |   |
|   |   +---tftp
|   |   |
|   |   +---xml-export
|   |   |
|   |   +---show buffers
|   |   |
|   |   +---show copyright
|   |   |
|   |   +---show cpu-utilization
|   |   |
|   |   +---show device-information
|   |   |
|   |   +---show memory
|   |   |
|   |   +---show memory-details
|   |   |
|   |   +---show summary-inventory
|   |   |
|   |   +---show system-date
|   |   |
|   |   +---show tech-support
|   |
|   +---terminal
|   |   |
|   |   +---baud-rate
|   |   |
|   |   +---console-timeout
|   |   |
|   |   +---length
|   |   |
|   |   +---serial-port-disable
|   |   |
|   |   +---timeout
|   |
|   +---test
|   |   |
|   |   +---l3sat
|   |   |   |
|   |   |   +---generator
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---local-ip-address
|   |   |   |   |
|   |   |   |   +---peer
|   |   |   |   |   |
|   |   |   |   |   +---activate
|   |   |   |   |   |
|   |   |   |   |   +---peer-profile
|   |   |   |   |   |
|   |   |   |   |   +---test-session
|   |   |   |   |   |
|   |   |   |   |   +---show status
|   |   |   |   |
|   |   |   |   +---router-entity
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---vlan-tag
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---peer-profile
|   |   |   |   |
|   |   |   |   +---bw-steps
|   |   |   |   |
|   |   |   |   +---configuration-duration
|   |   |   |   |
|   |   |   |   +---performance-duration
|   |   |   |   |
|   |   |   |   +---policing-test
|   |   |   |   |
|   |   |   |   +---report-type
|   |   |   |   |
|   |   |   |   +---scope
|   |   |   |   |
|   |   |   |   +---udp-port
|   |   |   |
|   |   |   +---responder
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---loaned-address
|   |   |   |   |
|   |   |   |   +---local-ip-address
|   |   |   |   |
|   |   |   |   +---router-entity
|   |   |   |   |
|   |   |   |   +---service-policer
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---udp-port
|   |   |   |   |
|   |   |   |   +---vlan-tag
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---session-profile
|   |   |   |   |
|   |   |   |   +---availability-threshold
|   |   |   |   |
|   |   |   |   +---delay-threshold
|   |   |   |   |
|   |   |   |   +---delay-variation-threshold
|   |   |   |   |
|   |   |   |   +---ip-size
|   |   |   |   |
|   |   |   |   +---l2-rate
|   |   |   |   |
|   |   |   |   +---loss-ratio-threshold
|   |   |
|   |   +---rfc2544
|   |   |   |
|   |   |   +---profile-name
|   |   |   |   |
|   |   |   |   +---eth-lck
|   |   |   |   |
|   |   |   |   +---frame-loss-tolerance
|   |   |   |   |
|   |   |   |   +---frame-size
|   |   |   |   |
|   |   |   |   +---frames-number-in-attempt
|   |   |   |   |
|   |   |   |   +---learning-frames
|   |   |   |   |
|   |   |   |   +---number-of-trials
|   |   |   |   |
|   |   |   |   +---pattern
|   |   |   |   |
|   |   |   |   +---test-direction
|   |   |   |   |
|   |   |   |   +---throughput-measurement-accuracy
|   |   |   |   |
|   |   |   |   +---tlv-type
|   |   |   |
|   |   |   +---test
|   |   |   |   |
|   |   |   |   +---activate
|   |   |   |   |
|   |   |   |   +---associated-flow
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---clear-reports
|   |   |   |   |
|   |   |   |   +---max-test-duration
|   |   |   |   |
|   |   |   |   +---test-profile
|   |   |   |   |
|   |   |   |   +---type
|   |   |   |   |
|   |   |   |   +---show attempt-lost-frames
|   |   |   |   |
|   |   |   |   +---show report
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |   |
|   |   |   |   +---show summary
|   |   |
|   |   +---y1564
|   |   |   |
|   |   |   +---generator
|   |   |   |   |
|   |   |   |   +---activate
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---destination
|   |   |   |   |
|   |   |   |   +---policer
|   |   |   |   |
|   |   |   |   +---test-profile
|   |   |   |   |
|   |   |   |   +---show mef46-ll-status
|   |   |   |   |
|   |   |   |   +---show report
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---profile
|   |   |   |   |
|   |   |   |   +---auto-cos-completion
|   |   |   |   |
|   |   |   |   +---bandwidth-round-up
|   |   |   |   |
|   |   |   |   +---burst-test
|   |   |   |   |
|   |   |   |   +---cir-steps
|   |   |   |   |
|   |   |   |   +---color-aware
|   |   |   |   |
|   |   |   |   +---configuration-duration
|   |   |   |   |
|   |   |   |   +---direction
|   |   |   |   |
|   |   |   |   +---ethernet-type
|   |   |   |   |
|   |   |   |   +---multi-frame-size
|   |   |   |   |
|   |   |   |   +---multiple-sa-mac
|   |   |   |   |
|   |   |   |   +---one-way-thresholds
|   |   |   |   |
|   |   |   |   +---p-bit
|   |   |   |   |   |
|   |   |   |   |   +---one-way-thresholds
|   |   |   |   |   |
|   |   |   |   |   +---round-trip-thresholds
|   |   |   |   |
|   |   |   |   +---performance-duration
|   |   |   |   |
|   |   |   |   +---rate-convention
|   |   |   |   |
|   |   |   |   +---responder-type
|   |   |   |   |
|   |   |   |   +---round-trip-thresholds
|   |   |   |   |
|   |   |   |   +---scope
|   |   |   |   |
|   |   |   |   +---traffic-policing
|   |   |   |   |
|   |   |   |   +---user-traffic-blocked
|   |   |   |
|   |   |   +---responder
|   |   |   |   |
|   |   |   |   +---activate
|   |   |   |   |
|   |   |   |   +---bind
|   |   |   |   |
|   |   |   |   +---destination
|   |   |   |   |
|   |   |   |   +---local-mac
|   |   |   |   |
|   |   |   |   +---test-profile
|   |   |   |   |
|   |   |   |   +---show status
|   |
|   +---show cards-summary
|   |
|   +---show peer-summary
|   |
|   +---show service-summary
|
+---file
|   |
|   +---delete
|   |
|   +---delete-user
|   |
|   +---description
|   |
|   +---dir
|   |
|   +---user-file-dir
|   |
|   +---show banner-text
|   |
|   +---show configuration-files
|   |
|   +---show copy
|   |
|   +---show factory-default-config
|   |
|   +---show file-details
|   |
|   +---show rollback-config
|   |
|   +---show schedule-log
|   |
|   +---show startup-config
|   |
|   +---show sw-pack
|   |
|   +---show user-default-config
|   |
|   +---show user-dir
|
+---logon
|
+---on-configuration-error

Global commands:
|
+---copy
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
