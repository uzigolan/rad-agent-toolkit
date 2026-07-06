# SecFlow command tree (family: secflow)

Captured live from SF-1p-187 (SecFlow-1p, Sw 6.5.0.35) via the root `tree`
command, July 2026. This is the full navigable command hierarchy — use it to
locate which context holds a feature, then use the `cli_help` tool for exact
argument syntax at that spot (`?` help is always firmware-exact).

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
|   |   +---firewall
|   |   |   |
|   |   |   +---blacklist
|   |   |   |
|   |   |   +---blacklist-clear
|   |   |   |
|   |   |   +---interzone
|   |   |   |   |
|   |   |   |   +---access-group
|   |   |   |   |
|   |   |   |   +---clear-access-list-statistics
|   |   |   |   |
|   |   |   |   +---packet-filter
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---show access-list-statistics
|   |   |   |   |
|   |   |   |   +---show access-list-summary
|   |   |   |
|   |   |   +---ip-sweep-defend
|   |   |   |
|   |   |   +---zone
|   |   |   |   |
|   |   |   |   +---member
|   |   |   |
|   |   |   +---show blacklist-summary
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
|   |   |   +---responder-only
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
|   |   |   +---delete
|   |   |   |
|   |   |   +---generate
|   |   |   |
|   |   |   +---import
|   |   |   |
|   |   |   +---show public-key
|   |   |
|   |   +---pki
|   |   |   |
|   |   |   +---authenticate
|   |   |   |
|   |   |   +---delete-certificate
|   |   |   |
|   |   |   +---delete-crl
|   |   |   |
|   |   |   +---enroll-attributes
|   |   |   |   |
|   |   |   |   +---ca-url
|   |   |   |   |
|   |   |   |   +---challenge-password
|   |   |   |   |
|   |   |   |   +---common-name
|   |   |   |   |
|   |   |   |   +---country
|   |   |   |   |
|   |   |   |   +---locality
|   |   |   |   |
|   |   |   |   +---organization
|   |   |   |   |
|   |   |   |   +---organizational-unit
|   |   |   |   |
|   |   |   |   +---san-dns-name
|   |   |   |   |
|   |   |   |   +---san-email
|   |   |   |   |
|   |   |   |   +---san-ip-address
|   |   |   |   |
|   |   |   |   +---san-uri
|   |   |   |   |
|   |   |   |   +---serial-number
|   |   |   |   |
|   |   |   |   +---state
|   |   |   |
|   |   |   +---enroll-from-configuration
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
|   |   |
|   |   +---group
|   |   |   |
|   |   |   +---member
|   |
|   +---management
|   |   |
|   |   +---access
|   |   |   |
|   |   |   +---access-group
|   |   |   |
|   |   |   +---auth-policy
|   |   |   |
|   |   |   +---ban-default-login-password
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---command-authorization
|   |   |   |
|   |   |   +---enrollment-notification-nms
|   |   |   |   |
|   |   |   |   +---nms-username
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---snmp-profile
|   |   |   |   |
|   |   |   |   +---ssh-username
|   |   |   |
|   |   |   +---ftps
|   |   |   |
|   |   |   +---known-host
|   |   |   |
|   |   |   +---login-password-black-list
|   |   |   |
|   |   |   +---login-password-properties
|   |   |   |
|   |   |   +---opcua-authentification-policy
|   |   |   |
|   |   |   +---rest-get
|   |   |   |
|   |   |   +---scp-client
|   |   |   |
|   |   |   +---sftp
|   |   |   |
|   |   |   +---sms
|   |   |   |   |
|   |   |   |   +---authentication
|   |   |   |   |
|   |   |   |   +---caller-id
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
|   |   |   +---ssh-server-host-key
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
|   |   |   +---show enrollment-status
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---dscp
|   |   |
|   |   +---login-user
|   |   |   |
|   |   |   +---authentication-method
|   |   |   |
|   |   |   +---level
|   |   |   |
|   |   |   +---otp-authentication
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
|   +---monitor
|   |   |
|   |   +---mirroring-session
|   |   |   |
|   |   |   +---destination
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---source
|   |
|   +---oam
|   |   |
|   |   +---ip-monitoring
|   |   |   |
|   |   |   +---fail-criteria
|   |   |   |
|   |   |   +---icmp-timeout
|   |   |   |
|   |   |   +---target
|   |   |   |
|   |   |   +---transmit-interval
|   |   |   |
|   |   |   +---window-size
|   |   |   |
|   |   |   +---show status
|   |
|   +---port
|   |   |
|   |   +---cellular
|   |   |   |
|   |   |   +---access-group
|   |   |   |
|   |   |   +---cellular-protection
|   |   |   |   |
|   |   |   |   +---connect-timeout
|   |   |   |   |
|   |   |   |   +---primary-sim
|   |   |   |   |
|   |   |   |   +---revertive
|   |   |   |   |
|   |   |   |   +---time-to-revert
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
|   |   |   +---clear-access-list-statistics
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---force-next-hop
|   |   |   |
|   |   |   +---mode
|   |   |   |
|   |   |   +---multi-apn
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
|   |   |   +---sim
|   |   |   |   |
|   |   |   |   +---apn
|   |   |   |   |   |
|   |   |   |   |   +---apn-name
|   |   |   |   |   |
|   |   |   |   |   +---chap-hostname
|   |   |   |   |   |
|   |   |   |   |   +---chap-password
|   |   |   |   |   |
|   |   |   |   |   +---pap-username
|   |   |   |   |   |
|   |   |   |   |   +---pdp-type
|   |   |   |   |   |
|   |   |   |   |   +---refuse-chap
|   |   |   |   |   |
|   |   |   |   |   +---refuse-no-auth
|   |   |   |   |   |
|   |   |   |   |   +---refuse-pap
|   |   |   |   |
|   |   |   |   +---apn-name
|   |   |   |   |
|   |   |   |   +---chap-hostname
|   |   |   |   |
|   |   |   |   +---chap-password
|   |   |   |   |
|   |   |   |   +---dialer-number
|   |   |   |   |
|   |   |   |   +---lte-band
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---pap-username
|   |   |   |   |
|   |   |   |   +---pdp-type
|   |   |   |   |
|   |   |   |   +---pin
|   |   |   |   |
|   |   |   |   +---radio-access-technology
|   |   |   |   |
|   |   |   |   +---refuse-chap
|   |   |   |   |
|   |   |   |   +---refuse-no-auth
|   |   |   |   |
|   |   |   |   +---refuse-pap
|   |   |   |   |
|   |   |   |   +---rssi-threshold
|   |   |   |
|   |   |   +---text-me-hello
|   |   |   |
|   |   |   +---traffic-class
|   |   |   |   |
|   |   |   |   +---cos
|   |   |   |   |
|   |   |   |   +---mark
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---show access-list-statistics
|   |   |   |
|   |   |   +---show access-list-summary
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
|   |   |   +---clear-access-list-statistics
|   |   |   |
|   |   |   +---clear-statistics
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
|   |   |   |   +---supplicant
|   |   |   |   |   |
|   |   |   |   |   +---authentication
|   |   |   |   |   |
|   |   |   |   |   +---held-period
|   |   |   |   |   |
|   |   |   |   |   +---max-authentication
|   |   |   |   |   |
|   |   |   |   |   +---shutdown
|   |   |   |   |   |
|   |   |   |   |   +---tx-period
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---force-next-hop
|   |   |   |
|   |   |   +---mac-access-control
|   |   |   |   |
|   |   |   |   +---mac
|   |   |   |   |
|   |   |   |   +---shutdown
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
|   |   |   |   +---clear-access-list-statistics
|   |   |   |   |
|   |   |   |   +---clear-statistics
|   |   |   |   |
|   |   |   |   +---egress-mtu
|   |   |   |   |
|   |   |   |   +---force-next-hop
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---pm-collection
|   |   |   |   |
|   |   |   |   +---policy-based-route
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---show access-list-statistics
|   |   |   |   |
|   |   |   |   +---show access-list-summary
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---show access-list-statistics
|   |   |   |
|   |   |   +---show access-list-summary
|   |   |   |
|   |   |   +---show statistics
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ppp
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---chap-hostname
|   |   |   |
|   |   |   +---chap-password
|   |   |   |
|   |   |   +---ipcp-address
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
|   |   +---serial
|   |   |   |
|   |   |   +---allowed-latency
|   |   |   |
|   |   |   +---baud-rate
|   |   |   |
|   |   |   +---bus-idle
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---data-bits
|   |   |   |
|   |   |   +---parity
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---stop-bits
|   |   |   |
|   |   |   +---terminal-server
|   |   |   |   |
|   |   |   |   +---disconnect
|   |   |   |   |
|   |   |   |   +---local-address
|   |   |   |   |
|   |   |   |   +---telnet-client-tcp
|   |   |   |   |
|   |   |   |   +---telnet-server-tcp
|   |   |   |   |
|   |   |   |   +---telnet-server-udp
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---tunnel
|   |   |   |   |
|   |   |   |   +---address
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---transport-layer
|   |   |   |
|   |   |   +---tx-delay
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---virtual
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---egress-mtu
|   |   |   |
|   |   |   +---force-next-hop
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
|   |   +---wifi-client
|   |   |   |
|   |   |   +---connection-method
|   |   |   |
|   |   |   +---dot1x
|   |   |   |   |
|   |   |   |   +---clear-statistics
|   |   |   |   |
|   |   |   |   +---initialize
|   |   |   |   |
|   |   |   |   +---supplicant
|   |   |   |   |   |
|   |   |   |   |   +---authentication
|   |   |   |   |   |
|   |   |   |   |   +---held-period
|   |   |   |   |   |
|   |   |   |   |   +---max-authentication
|   |   |   |   |   |
|   |   |   |   |   +---shutdown
|   |   |   |   |   |
|   |   |   |   |   +---tx-period
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---ssid
|   |   |   |   |
|   |   |   |   +---password
|   |   |   |   |
|   |   |   |   +---priority
|   |   |   |   |
|   |   |   |   +---security
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---show networks
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---wifi-country-code
|   |   |
|   |   +---wlan
|   |   |   |
|   |   |   +---access-point
|   |   |   |   |
|   |   |   |   +---access-group
|   |   |   |   |
|   |   |   |   +---broadcast-ssid
|   |   |   |   |
|   |   |   |   +---clear-access-list-statistics
|   |   |   |   |
|   |   |   |   +---dot1x
|   |   |   |   |   |
|   |   |   |   |   +---authenticator
|   |   |   |   |   |   |
|   |   |   |   |   |   +---reauthentication
|   |   |   |   |   |   |
|   |   |   |   |   |   +---shutdown
|   |   |   |   |   |
|   |   |   |   |   +---clear-statistics
|   |   |   |   |   |
|   |   |   |   |   +---initialize
|   |   |   |   |   |
|   |   |   |   |   +---show statistics
|   |   |   |   |   |
|   |   |   |   |   +---show status
|   |   |   |   |
|   |   |   |   +---force-next-hop
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
|   |   |   |   +---show access-list-statistics
|   |   |   |   |
|   |   |   |   +---show access-list-summary
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
|   +---protection
|   |   |
|   |   +---erp
|   |   |   |
|   |   |   +---bridge
|   |   |   |
|   |   |   +---data-vlan
|   |   |   |
|   |   |   +---description
|   |   |   |
|   |   |   +---east-port
|   |   |   |
|   |   |   +---port-description
|   |   |   |
|   |   |   +---port-type
|   |   |   |
|   |   |   +---r-aps
|   |   |   |
|   |   |   +---sf-trigger
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---west-port
|   |   |   |
|   |   |   +---show status
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
|   |   +---bfd-neighbor
|   |   |   |
|   |   |   +---detect-multiplier
|   |   |   |
|   |   |   +---receive-interval
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---transmit-interval
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
|   |   |   |   +---allowas-in
|   |   |   |   |
|   |   |   |   +---as-override
|   |   |   |   |
|   |   |   |   +---bfd
|   |   |   |   |
|   |   |   |   +---connect-timer
|   |   |   |   |
|   |   |   |   +---ebgp-multihop
|   |   |   |   |
|   |   |   |   +---local-address
|   |   |   |   |
|   |   |   |   +---max-prefixes
|   |   |   |   |
|   |   |   |   +---next-hop-self
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
|   |   +---dhcp-relay-server
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
|   |   |   +---dhcp-relay
|   |   |   |
|   |   |   +---dhcpv6-client
|   |   |   |
|   |   |   +---dhcpv6-relay
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
|   |   |   +---show crypto-map-status
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
|   |   |   +---access-group
|   |   |   |
|   |   |   +---bind
|   |   |   |
|   |   |   +---clear-access-list-statistics
|   |   |   |
|   |   |   +---clear-nhrp
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
|   |   |   +---multipoint
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---nhrp-map
|   |   |   |
|   |   |   +---nhrp-nhs
|   |   |   |
|   |   |   +---nhrp-registration-timeout
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
|   |   |   +---pm-collection
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---transport-router
|   |   |   |
|   |   |   +---tunnel-destination
|   |   |   |
|   |   |   +---tunnel-source
|   |   |   |
|   |   |   +---show access-list-statistics
|   |   |   |
|   |   |   +---show access-list-summary
|   |   |   |
|   |   |   +---show crypto-map-status
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---show arp-table
|   |   |
|   |   +---show bfd-neighbors
|   |   |
|   |   +---show bfd-neighbors-details
|   |   |
|   |   +---show dns-resolver
|   |   |
|   |   +---show ip-monitoring-summary
|   |   |
|   |   +---show neighbor-table
|   |   |
|   |   +---show rib
|   |   |
|   |   +---show routing-table
|   |   |
|   |   +---show summary-interface
|   |   |
|   |   +---show vrrp-summary
|   |
|   +---sd-iot
|   |   |
|   |   +---authentication-method
|   |   |
|   |   +---certificate
|   |   |
|   |   +---clear-statistics
|   |   |
|   |   +---client-number
|   |   |
|   |   +---duplication
|   |   |
|   |   +---ingress-port
|   |   |
|   |   +---keep-alive
|   |   |
|   |   +---shutdown
|   |   |
|   |   +---tunnel
|   |   |   |
|   |   |   +---peer-address
|   |   |   |
|   |   |   +---priority
|   |   |   |
|   |   |   +---secondary-peer-address
|   |   |   |
|   |   |   +---shutdown
|   |   |
|   |   +---username
|   |   |
|   |   +---show statistics
|   |   |
|   |   +---show status
|   |
|   +---system
|   |   |
|   |   +---announcement
|   |   |
|   |   +---clock
|   |   |   |
|   |   |   +---gnss
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---secondary-system
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
|   |   |   |   +---source-address
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
|   |   +---dhcp-relay
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
|   |   +---generate-log-report
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
|   |   +---modbus-unit
|   |   |   |
|   |   |   +---byte-order
|   |   |   |
|   |   |   +---description
|   |   |   |
|   |   |   +---ip-address
|   |   |   |
|   |   |   +---poll
|   |   |   |   |
|   |   |   |   +---acquisition
|   |   |   |   |
|   |   |   |   +---description
|   |   |   |   |
|   |   |   |   +---map-to-mqtt
|   |   |   |   |
|   |   |   |   +---map-to-opcua
|   |   |   |   |
|   |   |   |   +---modbus-operation
|   |   |   |   |
|   |   |   |   +---scaling
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---start-address
|   |   |   |
|   |   |   +---retries
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---timeout
|   |   |   |
|   |   |   +---unit-id
|   |   |
|   |   +---mqtt
|   |   |   |
|   |   |   +---server
|   |   |   |   |
|   |   |   |   +---address
|   |   |   |   |
|   |   |   |   +---certificate
|   |   |   |   |
|   |   |   |   +---management-channel
|   |   |   |   |
|   |   |   |   +---user
|   |   |   |   |
|   |   |   |   +---show status
|   |   |
|   |   +---name
|   |   |
|   |   +---opcua-server
|   |   |   |
|   |   |   +---application-certificate
|   |   |   |
|   |   |   +---application-name
|   |   |   |
|   |   |   +---application-uri
|   |   |   |
|   |   |   +---endpoint
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---trusted-ca
|   |   |
|   |   +---serial
|   |   |   |
|   |   |   +---terminal-server
|   |   |   |   |
|   |   |   |   +---dead-peer-timeout
|   |   |   |   |
|   |   |   |   +---shutdown
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
|   |   +---show resources
|   |   |
|   |   +---show summary-inventory
|   |   |
|   |   +---show system
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
|   |   +---serial-port-console
|   |   |
|   |   +---timeout
|
+---file
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
|   +---flash-enable
|   |
|   +---flash-temporarily-enable
|   |
|   +---folder-dir
|   |
|   +---media-dir
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
|   +---show file-transfer-status
|   |
|   +---show flash-status
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
|
+---quick-setup
|   |
|   +---port
|   |   |
|   |   +---cellular
|   |   |   |
|   |   |   +---access-group
|   |   |   |
|   |   |   +---cellular-protection
|   |   |   |   |
|   |   |   |   +---connect-timeout
|   |   |   |   |
|   |   |   |   +---primary-sim
|   |   |   |   |
|   |   |   |   +---revertive
|   |   |   |   |
|   |   |   |   +---time-to-revert
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
|   |   |   +---clear-access-list-statistics
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---force-next-hop
|   |   |   |
|   |   |   +---mode
|   |   |   |
|   |   |   +---multi-apn
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
|   |   |   +---sim
|   |   |   |   |
|   |   |   |   +---apn
|   |   |   |   |   |
|   |   |   |   |   +---apn-name
|   |   |   |   |   |
|   |   |   |   |   +---chap-hostname
|   |   |   |   |   |
|   |   |   |   |   +---chap-password
|   |   |   |   |   |
|   |   |   |   |   +---pap-username
|   |   |   |   |   |
|   |   |   |   |   +---pdp-type
|   |   |   |   |   |
|   |   |   |   |   +---refuse-chap
|   |   |   |   |   |
|   |   |   |   |   +---refuse-no-auth
|   |   |   |   |   |
|   |   |   |   |   +---refuse-pap
|   |   |   |   |
|   |   |   |   +---apn-name
|   |   |   |   |
|   |   |   |   +---chap-hostname
|   |   |   |   |
|   |   |   |   +---chap-password
|   |   |   |   |
|   |   |   |   +---dialer-number
|   |   |   |   |
|   |   |   |   +---lte-band
|   |   |   |   |
|   |   |   |   +---name
|   |   |   |   |
|   |   |   |   +---pap-username
|   |   |   |   |
|   |   |   |   +---pdp-type
|   |   |   |   |
|   |   |   |   +---pin
|   |   |   |   |
|   |   |   |   +---radio-access-technology
|   |   |   |   |
|   |   |   |   +---refuse-chap
|   |   |   |   |
|   |   |   |   +---refuse-no-auth
|   |   |   |   |
|   |   |   |   +---refuse-pap
|   |   |   |   |
|   |   |   |   +---rssi-threshold
|   |   |   |
|   |   |   +---text-me-hello
|   |   |   |
|   |   |   +---traffic-class
|   |   |   |   |
|   |   |   |   +---cos
|   |   |   |   |
|   |   |   |   +---mark
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---show access-list-statistics
|   |   |   |
|   |   |   +---show access-list-summary
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---ethernet
|   |   |   |
|   |   |   +---name
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---vlan
|   |   |
|   |   +---serial
|   |   |   |
|   |   |   +---allowed-latency
|   |   |   |
|   |   |   +---baud-rate
|   |   |   |
|   |   |   +---bus-idle
|   |   |   |
|   |   |   +---clear-statistics
|   |   |   |
|   |   |   +---data-bits
|   |   |   |
|   |   |   +---parity
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---stop-bits
|   |   |   |
|   |   |   +---terminal-server
|   |   |   |   |
|   |   |   |   +---disconnect
|   |   |   |   |
|   |   |   |   +---local-address
|   |   |   |   |
|   |   |   |   +---telnet-client-tcp
|   |   |   |   |
|   |   |   |   +---telnet-server-tcp
|   |   |   |   |
|   |   |   |   +---telnet-server-udp
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---tunnel
|   |   |   |   |
|   |   |   |   +---address
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |   |
|   |   |   |   +---transport-layer
|   |   |   |
|   |   |   +---tx-delay
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---virtual
|   |   |
|   |   +---wifi-client
|   |   |   |
|   |   |   +---connection-method
|   |   |   |
|   |   |   +---dot1x
|   |   |   |   |
|   |   |   |   +---clear-statistics
|   |   |   |   |
|   |   |   |   +---initialize
|   |   |   |   |
|   |   |   |   +---supplicant
|   |   |   |   |   |
|   |   |   |   |   +---authentication
|   |   |   |   |   |
|   |   |   |   |   +---held-period
|   |   |   |   |   |
|   |   |   |   |   +---max-authentication
|   |   |   |   |   |
|   |   |   |   |   +---shutdown
|   |   |   |   |   |
|   |   |   |   |   +---tx-period
|   |   |   |   |
|   |   |   |   +---show statistics
|   |   |   |   |
|   |   |   |   +---show status
|   |   |   |
|   |   |   +---shutdown
|   |   |   |
|   |   |   +---ssid
|   |   |   |   |
|   |   |   |   +---password
|   |   |   |   |
|   |   |   |   +---priority
|   |   |   |   |
|   |   |   |   +---security
|   |   |   |   |
|   |   |   |   +---shutdown
|   |   |   |
|   |   |   +---show networks
|   |   |   |
|   |   |   +---show status
|   |   |
|   |   +---wlan
|   |   |   |
|   |   |   +---access-point
|   |   |   |   |
|   |   |   |   +---access-group
|   |   |   |   |
|   |   |   |   +---broadcast-ssid
|   |   |   |   |
|   |   |   |   +---clear-access-list-statistics
|   |   |   |   |
|   |   |   |   +---dot1x
|   |   |   |   |   |
|   |   |   |   |   +---authenticator
|   |   |   |   |   |   |
|   |   |   |   |   |   +---reauthentication
|   |   |   |   |   |   |
|   |   |   |   |   |   +---shutdown
|   |   |   |   |   |
|   |   |   |   |   +---clear-statistics
|   |   |   |   |   |
|   |   |   |   |   +---initialize
|   |   |   |   |   |
|   |   |   |   |   +---show statistics
|   |   |   |   |   |
|   |   |   |   |   +---show status
|   |   |   |   |
|   |   |   |   +---force-next-hop
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
|   |   |   |   +---show access-list-statistics
|   |   |   |   |
|   |   |   |   +---show access-list-summary
|   |   |   |   |
|   |   |   |   +---show connected-devices
|   |   |   |
|   |   |   +---channel
|   |   |   |
|   |   |   +---radio-mode
|   |
|   +---router
|   |   |
|   |   +---default-gateway
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
|   |   |   +---show nat-translations
|   |   |
|   |   +---router
|   |   |   |
|   |   |   +---nat
|   |   |   |   |
|   |   |   |   +---clear-nat-statistics
|   |   |   |   |
|   |   |   |   +---clear-nat-translations
|   |   |   |   |
|   |   |   |   +---nat-exclude-source-ip
|   |   |   |   |
|   |   |   |   +---nat-inside-overload
|   |   |   |   |
|   |   |   |   +---nat-inside-source-static
|   |   |   |   |
|   |   |   |   +---nat-inside-source-static-port
|   |   |   |   |
|   |   |   |   +---nat-timeout
|   |   |   |   |
|   |   |   |   +---show nat-translations
|   |   |   |
|   |   |   +---static-route
|   |
|   +---vpn
|   |   |
|   |   +---ipsec-transform-set
|   |   |   |
|   |   |   +---algorithms
|   |   |   |
|   |   |   +---mode
|   |   |
|   |   +---isakmp-policy
|   |   |   |
|   |   |   +---encryption
|   |   |   |
|   |   |   +---group
|   |   |   |
|   |   |   +---hash

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
