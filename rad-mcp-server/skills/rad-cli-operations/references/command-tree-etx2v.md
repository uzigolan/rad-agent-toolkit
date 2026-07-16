# etx2v command tree (family: etx2v)

Captured live from etx2v-1 (ETX-2V (uCPE-OS chassis platform, prompt uCPE-OS#); verified live - shared context CLI, standard SSH; distinctive virtualization/VNF context; CLI reference + hardware manual harvested) via the root `tree` command on 2026-07-15
by scripts/harvest_cli.py — re-run `harvest` after firmware upgrades; the
tree is re-captured fresh each run. Use it to locate which context holds a
feature, then cli-reference-etx2v.md / the cli_help tool for exact,
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
|   +---force-reboot
|   |
|   +---license
|   |   |
|   |   +---license-enable
|   |   |
|   |   +---show summary
|   |   |
|   |   +---show vcpe-os-id
|   |
|   +---login
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
|   |   +---resequence
|   |
|   +---bridge
|   |   |
|   |   +---aging-time
|   |   |
|   |   +---clear-mac-table
|   |   |
|   |   +---filtering
|   |   |
|   |   +---name
|   |   |
|   |   +---port
|   |   |   |
|   |   |   +---accept-frame-type
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---ingress-filtering
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pvid
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---static-mac
|   |   |
|   |   +---vlan
|   |   |   |
|   |   |   +---tagged-port
|   |   |   |
|   |   |   +---untagged-port
|   |   |
|   |   +---vlan-aware
|   |   |
|   |   +---show mac-address-table
|   |   |
|   |   +---show mac-address-table
|   |   |
|   |   +---show summary
|   |   |
|   |   +---show vlans
|   |
|   +---crypto
|   |   |
|   |   +---ca
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---certificate-auto-renew
|   |   |   |
|   |   |   +---crl-auto-renew
|   |   |   |
|   |   |   +---protocol
|   |   |
|   |   +---crypto-map
|   |   |   |
|   |   |   +---ike-authentication
|   |   |   |
|   |   |   +---ike-identity-local
|   |   |   |
|   |   |   +---ike-identity-local-x509
|   |   |   |
|   |   |   +---ike-identity-remote
|   |   |   |
|   |   |   +---ike-identity-remote-x509
|   |   |   |
|   |   |   +---ike-sa-lifetime
|   |   |   |
|   |   |   +---ike-sa-negotiation
|   |   |   |
|   |   |   +---ike-version
|   |   |   |
|   |   |   +---match-address
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
|   |   +---isakmp-key
|   |   |
|   |   +---isakmp-policy
|   |   |   |
|   |   |   +---encryption
|   |   |   |
|   |   |   +---group
|   |   |   |
|   |   |   +---hash
|   |   |
|   |   +---key
|   |   |   |
|   |   |   +---delete-rsa
|   |   |   |
|   |   |   +---generate-rsa
|   |   |   |
|   |   |   +---import-rsa
|   |   |   |
|   |   |   +---show public-key-rsa
|   |   |
|   |   +---pki
|   |   |   |
|   |   |   +---authenticate
|   |   |   |
|   |   |   +---delete-certificate
|   |   |   |
|   |   |   +---delete-crl
|   |   |   |
|   |   |   +---enroll
|   |   |   |
|   |   |   +---export-crl
|   |   |   |
|   |   |   +---import-certificate
|   |   |   |
|   |   |   +---import-crl
|   |   |   |
|   |   |   +---self-sign-certificate
|   |   |   |
|   |   |   +---show certificate
|   |   |   |
|   |   |   +---show certificate-summary
|   |   |   |
|   |   |   +---show crl-summary
|   |
|   +---fault
|   |   |
|   |   +---fault-propagation
|   |
|   +---management
|   |   |
|   |   +---access
|   |   |   |
|   |   |   +---access-group
|   |   |   |
|   |   |   +---auth-policy
|   |   |   |
|   |   |   +---auth-policy-virtualization
|   |   |   |
|   |   |   +---ban-default-login-password
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---ftps
|   |   |   |
|   |   |   +---login-password-black-list
|   |   |   |
|   |   |   +---login-password-properties
|   |   |   |
|   |   |   +---rest-get
|   |   |   |
|   |   |   +---scp-client
|   |   |   |
|   |   |   +---sftp
|   |   |   |
|   |   |   +---snmp
|   |   |   |
|   |   |   +---ssh-encryption
|   |   |   |
|   |   |   +---ssh
|   |   |   |
|   |   |   +---telnet
|   |   |   |
|   |   |   +---tftp
|   |   |   |
|   |   |   +---virtualization-rest
|   |   |   |
|   |   |   +---web
|   |   |   |
|   |   |   +---ztc-after-reboot
|   |   |   |
|   |   |   +---ztc-bootstrap
|   |   |   |
|   |   |   +---ztc-tftp-disable
|   |   |   |
|   |   |   +---show access-list
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---dscp
|   |   |
|   |   +---ldap
|   |   |   |
|   |   |   +---base-dn
|   |   |   |
|   |   |   +---search-dn
|   |   |   |
|   |   |   +---search-user
|   |   |   |
|   |   |   +---server
|   |   |   |   |
|   |   |   |   +---ip-address
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
|   |   |   |   +---retry
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---timeout
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |
|   |   +---show failed-login-attempts
|   |   |
|   |   +---show ssh-server
|   |   |
|   |   +---show users-details
|   |   |
|   |   +---show users
|   |
|   +---oam
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
|   |   |   |   |   +---calculation-mode
|   |   |   |   |   |
|   |   |   |   |   +---compatibility-mode
|   |   |   |   |   |
|   |   |   |   |   +---responder-seq-num
|   |   |   |   |   |
|   |   |   |   |   +---test-session
|   |   |   |   |   |
|   |   |   |   |   +---show report
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
|   |   |   |   +---fragment-mark
|   |   |   |   |
|   |   |   |   +---local-ip-address
|   |   |   |   |
|   |   |   |   +---reflector-timeout
|   |   |   |   |
|   |   |   |   +---router-entity
|   |   |   |   |
|   |   |   |   +---server-timeout
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---tcp-port
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
|   +---port
|   |   |
|   |   +---cellular
|   |   |   |
|   |   |   +---apn-name
|   |   |   |
|   |   |   +---classifier
|   |   |   |   |
|   |   |   |   +---comment
|   |   |   |   |
|   |   |   |   +---delete
|   |   |   |   |
|   |   |   |   +---match
|   |   |   |   |
|   |   |   |   +---resequence
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---dialer-number
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pin
|   |   |   |
|   |   |   +---policy-based-route
|   |   |   |
|   |   |   +---queue-group
|   |   |   |
|   |   |   +---radio-access-technology
|   |   |   |
|   |   |   +---rssi-threshold
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---traffic-class
|   |   |   |   |
|   |   |   |   +---cos
|   |   |   |   |
|   |   |   |   +---mark
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ethernet
|   |   |   |
|   |   |   +---access-group
|   |   |   |
|   |   |   +---classifier
|   |   |   |   |
|   |   |   |   +---comment
|   |   |   |   |
|   |   |   |   +---delete
|   |   |   |   |
|   |   |   |   +---match
|   |   |   |   |
|   |   |   |   +---resequence
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---policy-based-route
|   |   |   |
|   |   |   +---queue-group
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---traffic-class
|   |   |   |   |
|   |   |   |   +---cos
|   |   |   |   |
|   |   |   |   +---mark
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---vlan
|   |   |   |   |
|   |   |   |   +---access-group
|   |   |   |   |
|   |   |   |   +---clear-statistics
|   |   |   |   |
|   |   |   |   +---egress-mtu
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---policy-based-route
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---show access-list-summary
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---show access-list-summary
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---jumbo-frames
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
|   |   +---virtual
|   |   |   |
|   |   |   +---access-group
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---policy-based-route
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---vlan
|   |   |   |   |
|   |   |   |   +---egress-mtu
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---wifi-country-code
|   |   |
|   |   +---wlan
|   |   |   |
|   |   |   +---access-point
|   |   |   |   |
|   |   |   |   +---authentication
|   |   |   |   |
|   |   |   |   +---broadcast-ssid
|   |   |   |   |
|   |   |   |   +---encryption
|   |   |   |   |
|   |   |   |   +---mac-filter
|   |   |   |   |
|   |   |   |   +---mac-filter-enable
|   |   |   |   |
|   |   |   |   +---max-clients
|   |   |   |   |
|   |   |   |   +---password
|   |   |   |   |
|   |   |   |   +---policy-based-route
|   |   |   |   |
|   |   |   |   +---security
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---ssid
|   |   |   |   |
|   |   |   |   +---wlan-partition
|   |   |   |   |
|   |   |   |   +---wps
|   |   |   |   |
|   |   |   |   +---show connected-devices
|   |   |   |
|   |   |   +---channel
|   |   |   |
|   |   |   +---radio-mode
|   |   |
|   |   +---show summary
|   |   |
|   |   +---show wifi
|   |
|   +---qos
|   |   |
|   |   +---queue-block-profile
|   |   |   |
|   |   |   +---queue
|   |   |   |   |
|   |   |   |   +---bandwidth
|   |   |   |   |
|   |   |   |   +---scheduling
|   |   |
|   |   +---queue-group-profile
|   |   |   |
|   |   |   +---queue-block
|   |   |   |   |
|   |   |   |   +---profile
|   |   |   |   |
|   |   |   |   +---shaper
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
|   |   +---clear-accounting-log
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
|   |   |
|   |   +---show log-summary
|   |
|   +---router
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
|   |   +---clear-neighbor-table
|   |   |
|   |   +---dhcp-client
|   |   |   |
|   |   |   +---dhcpv6-option-request
|   |   |   |
|   |   |   +---duid-type
|   |   |   |
|   |   |   +---host-name
|   |   |   |
|   |   |   +---vendor-class-id
|   |   |
|   |   +---interface
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---crypto-map
|   |   |   |
|   |   |   +---dhcp
|   |   |   |
|   |   |   +---dhcp-client
|   |   |   |   |
|   |   |   |   +---client-id
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
|   |   |   +---name
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
|   |   |   +---router-advertisement
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---unreachables
|   |   |   |
|   |   |   +---show crypto-map-status
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---name
|   |   |
|   |   +---nat
|   |   |   |
|   |   |   +---clear-nat-statistics
|   |   |   |
|   |   |   +---clear-nat-translations
|   |   |   |
|   |   |   +---nat-exclude-source-ip
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
|   |   |   +---external-preference
|   |   |   |
|   |   |   +---internal-preference
|   |   |   |
|   |   |   +---redistribute
|   |   |   |
|   |   |   +---router-id
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show database
|   |   |   |
|   |   |   +---show interface-table
|   |   |   |
|   |   |   +---show neighbor-table
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
|   |   +---static-route
|   |   |
|   |   +---tunnel-interface
|   |   |   |
|   |   |   +---backup
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---crypto-map
|   |   |   |
|   |   |   +---dscp
|   |   |   |
|   |   |   +---ip-address
|   |   |   |
|   |   |   +---ip-mtu
|   |   |   |
|   |   |   +---key
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---tunnel-destination
|   |   |   |
|   |   |   +---tunnel-source
|   |   |   |
|   |   |   +---show crypto-map-status
|   |   |   |
|   |   |   +---show crypto-map-status
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show arp-table
|   |   |
|   |   +---show dns-resolver
|   |   |
|   |   +---show neighbor-table
|   |   |
|   |   +---show rib
|   |   |
|   |   +---show routing-table
|   |   |
|   |   +---show summary-interface
|   |
|   +---system
|   |   |
|   |   +---announcement
|   |   |
|   |   +---contact
|   |   |
|   |   +---date-and-time
|   |   |   |
|   |   |   +---date-format
|   |   |   |
|   |   |   +---date
|   |   |   |
|   |   |   +---ntp
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
|   |   |   |   +---learn-from-dhcp-client
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
|   |   |   |   |
|   |   |   |   +---tftp-server-name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---show binding
|   |   |   |
|   |   |   +---show conflict
|   |   |   |
|   |   |   +---show statistics
|   |   |
|   |   +---dhcpv6-server
|   |   |   |
|   |   |   +---clear
|   |   |   |
|   |   |   +---pool
|   |   |   |   |
|   |   |   |   +---address-prefix
|   |   |   |   |
|   |   |   |   +---dns-server
|   |   |   |   |
|   |   |   |   +---domain-search-list
|   |   |   |   |
|   |   |   |   +---learn-from-dhcpv6-client
|   |   |   |
|   |   |   +---show binding
|   |   |   |
|   |   |   +---show conflict
|   |   |
|   |   +---hostname
|   |   |
|   |   +---inventory
|   |   |
|   |   +---ip-domain-name
|   |   |
|   |   +---ip-host
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
|   +---virtualization
|   |   |
|   |   +---add-ons
|   |   |   |
|   |   |   +---add-on
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---clear-cpu-utilization
|   |   |
|   |   +---instance
|   |   |   |
|   |   |   +---clear
|   |   |   |
|   |   |   +---core-pinning
|   |   |   |
|   |   |   +---create-snapshot
|   |   |   |
|   |   |   +---description
|   |   |   |
|   |   |   +---flavor
|   |   |   |
|   |   |   +---image
|   |   |   |
|   |   |   +---init-config
|   |   |   |
|   |   |   +---monitor
|   |   |   |
|   |   |   +---network
|   |   |   |
|   |   |   +---pause
|   |   |   |
|   |   |   +---reboot
|   |   |   |
|   |   |   +---remote-terminal
|   |   |   |
|   |   |   +---replace-network
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---stop
|   |   |   |
|   |   |   +---vnc
|   |   |   |
|   |   |   +---show resources
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---interface
|   |   |   |
|   |   |   +---access-group
|   |   |   |
|   |   |   +---address
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---description
|   |   |   |
|   |   |   +---dhcp
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---virtualization-label
|   |   |
|   |   +---management-mode
|   |   |
|   |   +---networking-mode
|   |   |
|   |   +---repository
|   |   |   |
|   |   |   +---export-image
|   |   |   |
|   |   |   +---flavor
|   |   |   |
|   |   |   +---image
|   |   |   |
|   |   |   +---network
|   |   |   |   |
|   |   |   |   +---admin-state
|   |   |   |   |
|   |   |   |   +---description
|   |   |   |   |
|   |   |   |   +---subnet
|   |   |   |   |
|   |   |   |   +---type
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---show flavors
|   |   |   |
|   |   |   +---show images
|   |   |
|   |   +---virtualization-dns-server
|   |   |
|   |   +---virtualization-gateway
|   |   |
|   |   +---virtualization-ip
|   |   |
|   |   +---show core-mapping
|   |   |
|   |   +---show resources
|   |   |
|   |   +---show summary-instance
|   |   |
|   |   +---show system
|   |   |
|   |   +---show system-detail
|
+---file
|   |
|   +---copy
|   |
|   +---delete
|   |
|   +---delete-from-folder
|   |
|   +---delete-user
|   |
|   +---description
|   |
|   +---dir
|   |
|   +---folder-dir
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
