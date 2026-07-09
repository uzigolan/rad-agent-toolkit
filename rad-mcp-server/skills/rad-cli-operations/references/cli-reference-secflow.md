# secflow CLI reference (harvested `?` help)

Captured live from lab-sf1p (SF-1p-187 (SecFlow-1p, Sw 6.5.0.35) - pilot lab unit, safe for guarded write tests) on 2026-07-09 by scripts/harvest_cli.py
(re-run `harvest` after firmware upgrades — it diffs and updates in place).
Every section is a CLI context: first the level `?` listing (commands +
descriptions), then per-command argument help (`<command> ?`). Sections
ending in NAME are parameterized contexts harvested through one instance
(an existing one, or a temp object created and rolled back) — NAME stands
for any instance. Entries marked *(not entered)* could not be harvested
safely — their inner structure is in command-tree-secflow.md; use
cli_help with a real index for inner argument syntax.

## <root>

Level help (`?`):
```text
admin                          + Adminstrative commands
      configure                      + Configure device
      file                           + File commands
      logon                          - Logon as Debug user
      on-configuration-error         - Behavior for configuration error
      quick-setup                    + Quick Setup

Global commands:
      copy                           - Copy file
      echo                           - Displays a line of text (command) on the 
                                       screen
      exec                           - Execute script of CLI commands
      exit                           - Returns to the next higher command level 
                                       (context)
      help                           - Displays information regarding commands 
                                       in the current level
      history                        - Displays the history of commands issued 
                                       since the last restart
      info                           - Displays the current device configuration
      level-info                     - Displays the current device configuration
                                        - commands from the current level only
      logout                         - Logs the device off
      ping                           - Ping
 [no] popup-suspend                  - Suspends popup messages
      save                           - Save current settings
 [no] schedule                       - Schedule a command to run in a future 
                                       time
      telnet                         - Open telnet client session
      trace-route                    - Traceroute
      tree                           - Displays the command levels from the 
                                       current context downwards
```

### copy
```text
<source-file-url>    : <file-url> = <url-prefix> <file>
<url-prefix> = 
      tftp://<ipv4-address>/
      tftp://[<ipv6-address>]/
      sftp://<username>:<password>@<ipv4-address>:<port>/
      sftp://<username>:<password>@[<ipv6-address>]:<port>/
      scp://<username>:<password>@<ipv4-address>:<port>/
      scp://<username>:<password>@[<ipv6-address>]:<port>/
      ftp://<username>:<password>@<ipv4-address>:<port>/
      ftp://<username>:<password>@[<ipv6-address>]:<port>/
      ftps://<username>:<password>@<ipv4-address>:<port>/
      ftps://<username>:<password>@[<ipv6-address>]:<port>/
      xmodem:
      xmodem:
      flash-<flash-number>:
<file> = 
      startup-config
      restore-point-config
      rollback-config
      running-config
      user-default-config
      factory-default-config
      log
      sw-pack-1
      sw-pack-2
      zero-touch-config-xml
      banner-text
      pm-0
      db-schema
      db-config
      ltm_1
      ltm_9
      schedule-log
      accounting-log
      sniffer-file
      user-script
      script-result
      sw-update-1
      sw-update-2
The maximum allowed length/range is:
      <username> [1..32 chars]
      <password> [1..32 chars]
      <file>     [1..96 chars]
      <port>     [1..65535]



SF-1p-187# copy
```

### echo
```text
<CR>
 <text-to-echo>       : Text to display on screen [string]


SF-1p-187# echo
```

### exec
```text
<user-script>        : 


SF-1p-187# exec
```

### exit
```text
<CR>
 <all>                : Returns to Device context


SF-1p-187# exit
```

### help
```text
<CR>
 <command-name>       : Command for which help is requested [string]


SF-1p-187# help
```

### history
```text
<CR>

SF-1p-187# history
```

### info
```text
<CR>
 <detail>             : Adds information to every conf. parameter


SF-1p-187# info
```

### level-info
```text
<CR>
 <detail>             : Device configuration, including defaults


SF-1p-187# level-info
```

### logon
```text
<debug>              : Debug


SF-1p-187# logon
```

### logout
```text
<CR>

SF-1p-187# logout
```

### on-configuration-error
```text
<ignore>             : Ignore configuration error
 <stop>               : Stop at first error
 <reject>             : Reject, reboot and  load alternate configuration


SF-1p-187# on-configuration-error
```

### ping
```text
<ip-address>         : Destination IP [0.0.0.0|0:0:0:0::0|host-name]


SF-1p-187# ping
```

### popup-suspend
```text
<CR>

SF-1p-187# popup-suspend
```

### save
```text
<CR>

SF-1p-187# save
```

### schedule
```text
<name>               : Schedule name [string]


SF-1p-187# schedule
```

### telnet
```text
<ip-address>         : Telnet destination IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187# telnet
```

### trace-route
```text
<ip-address>         : Destination IP [0.0.0.0|0:0:0:0::0|host-name]


SF-1p-187# trace-route
```

### tree
```text
<CR>
 <detail>             : Available commands, current context and downwards


SF-1p-187# tree
```

## admin

Level help (`?`):
```text
factory-default-all            - Return to factory default and reboot
      factory-default                - Return to factory default configuration 
                                       and reboot
      force-reboot                   - Reboot the device unconditionally
 [no] login                          - Login as a different user
      reboot                         - Reboot device
      scheduler                      + Scheduler control commands
      send                           - Send message to all connected CLI users
      software                       + Software installation
 [no] startup-confirm-required       - Require user confirmation after reboot
      user-default                   - Return to user default configuration and 
                                       reboot

 show reboot                         - Display scheduled reboot details
```

### factory-default
```text
<CR>

SF-1p-187>admin# factory-default
```

### factory-default-all
```text
<CR>

SF-1p-187>admin# factory-default-all
```

### force-reboot
```text
<CR>

SF-1p-187>admin# force-reboot
```

### login
```text
<CR>

SF-1p-187>admin# login
```

### reboot
```text
<CR>
 <in>                 : 
 <at>                 : 
 <cancel>             : 


SF-1p-187>admin# reboot
```

### send
```text
<message>            : 


SF-1p-187>admin# send
```

### show reboot
```text
<CR>

SF-1p-187>admin# show reboot
```

### startup-confirm-required
```text
<CR>
 time-to-confirm
 rollback

SF-1p-187>admin# startup-confirm-required
```

### user-default
```text
<CR>

SF-1p-187>admin# user-default
```

## admin scheduler

Level help (`?`):
```text
clear-finished-schedules       - Delete all finished schedules from the 
                                       database
      clear-schedule-log             - Clear schedule log file

 show scheduler                      - Show all schedules
 show scheduler-details              - Show all schedules with details
```

### clear-finished-schedules
```text
<CR>

SF-1p-187>admin>scheduler# clear-finished-schedules
```

### clear-schedule-log
```text
<CR>

SF-1p-187>admin>scheduler# clear-schedule-log
```

### show scheduler
```text
<CR>

SF-1p-187>admin>scheduler# show scheduler
```

### show scheduler-details
```text
<CR>

SF-1p-187>admin>scheduler# show scheduler-details
```

## admin software

Level help (`?`):
```text
install                        - Install software and reboot
 [no] software-confirm-required      - Require user confirmation of software 
                                       after reboot
      undo-install                   - Return to restore point

 show status                         - Show installation process
```

### install
```text
<sw-pack-1>          : sw-pack-1
 <sw-pack-2>          : sw-pack-2
 <sw-update-1>        : sw-update-1
 <sw-update-2>        : sw-update-2


SF-1p-187>admin>software# install
```

### show status
```text
<CR>

SF-1p-187>admin>software# show status
```

### software-confirm-required
```text
<CR>
 time-to-confirm

SF-1p-187>admin>software# software-confirm-required
```

### undo-install
```text
<CR>

SF-1p-187>admin>software# undo-install
```

## configure

Level help (`?`):
```text
access-control                 + Configure access control
 [no] bridge                         + Configure bridge
      crypto                         + Cryptography level
      fault                          + 
      management                     + Device management commands
      monitor                        + 
      oam                            + Configure OAM
      port                           + Configure port
      protection                     + Protection level
      qos                            + Quality of service
      reporting                      + 
 [no] router                         + Configure router
 [no] sd-iot                         + Configure sd-iot entity
      system                         + Defines system parameters
      terminal                       + Configure terminal
```

### bridge *(parameterized — inner help harvested under "configure bridge NAME")*
```text
<number>             : Bridge number [number]


SF-1p-187>config# bridge
```

### router *(parameterized — inner help harvested under "configure router NAME")*
```text
<number>             : Router number [number] [1..10]


SF-1p-187>config# router
```

## configure access-control

Level help (`?`):
```text
[no] access-list                    + Configure ACL
      firewall                       + Configure firewall
 [no] logging                        - Set ACL logging interval
      resequence                     - Resequence ACL
```

### access-list *(not entered — parameterized context)*
```text
<ipv4>               : IPv4
 <ipv6>               : IPv6
 <acl-name>           : Access list name [1..79 chars]


SF-1p-187>config>access-control# access-list
```

### logging
```text
access-list

SF-1p-187>config>access-control# logging
```

### resequence
```text
access-list

SF-1p-187>config>access-control# resequence
```

## configure access-control firewall

Level help (`?`):
```text
[no] blacklist                      - Blacklist an IP address
      blacklist-clear                - Clear blacklist
 [no] interzone                      + Interzone level
 [no] ip-sweep-defend                - Defend from IP sweep DoS attack
 [no] zone                           + Zone level

 show blacklist-summary
```

### blacklist
```text
<ip-address>         : Blacklisted IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>access-control>firewall# blacklist
```

### blacklist-clear
```text
<CR>
 <configured>         : 
 <learned>            : 
 <all>                : 


SF-1p-187>config>access-control>firewall# blacklist-clear
```

### interzone *(not entered — parameterized context)*
```text
in-zone

SF-1p-187>config>access-control>firewall# interzone
```

### ip-sweep-defend
```text
<CR>
 blacklist-time
 max-rate

SF-1p-187>config>access-control>firewall# ip-sweep-defend
```

### show blacklist-summary
```text
<CR>
 <configured>         : 
 <learned>            : 
 address

SF-1p-187>config>access-control>firewall# show blacklist-summary
```

### zone *(parameterized — inner help harvested under "configure access-control firewall zone NAME")*
```text
<zone-name>          : Zone name [1..79 chars]


SF-1p-187>config>access-control>firewall# zone
```

## configure access-control firewall zone NAME

Level help (`?`):
```text
[no] member                         - Bind entity to zone


SF-1p-187>config>access-control>firewall>zone(zzz-hrvst)$
```

### member
```text
<cellular>           : 
 <ethernet>           : 
 <ppp>                : 
 <tunnel-interface>   : 
 <wifi-client>        : 
 <wlan>               : 


SF-1p-187>config>access-control>firewall>zone(zzz-hrvst)$ member
```

## configure bridge NAME

Level help (`?`):
```text
aging-time                     - Configure MAC aging time
      clear-mac-table                - Clear MAC address table
 [no] filtering                      - Enable filtering forwarding mode
 [no] name                           - Configure bridge name
 [no] port                           + Configure bridge port
 [no] vlan-aware                     - Enable VLAN aware mode

 show mac-address-table              - Display MAC address table
 show summary                        - Display bridge ports list

SF-1p-187>config>bridge(1)$
```

### aging-time
```text
<seconds>            : MAC aging time (seconds) [number, default 300] [60..956]


SF-1p-187>config>bridge(1)$ aging-time
```

### clear-mac-table
```text
<CR>

SF-1p-187>config>bridge(1)$ clear-mac-table
```

### filtering
```text
<CR>

SF-1p-187>config>bridge(1)$ filtering
```

### name
```text
<bridge-name>        : Bridge name [1..32 chars]


SF-1p-187>config>bridge(1)$ name
```

### show mac-address-table
```text
<CR>

SF-1p-187>config>bridge(1)# show mac-address-table
```

### show summary
```text
<CR>

SF-1p-187>config>bridge(1)# show summary
```

### show vlans
```text
<CR>
 vlan

SF-1p-187>config>bridge(1)# show vlans
```

### static-mac
```text
# cli error: Invalid Command
SF-1p-187>config>bridge(1)# static-mac
```

### vlan-aware
```text
<CR>

SF-1p-187>config>bridge(1)# vlan-aware
```

## configure bridge NAME port

Level help (`?`):
```text
aging-time                     - Configure MAC aging time
      clear-mac-table                - Clear MAC address table
 [no] filtering                      - Enable filtering forwarding mode
 [no] name                           - Configure bridge name
 [no] port                           + Configure bridge port
 [no] vlan-aware                     - Enable VLAN aware mode

 show mac-address-table              - Display MAC address table
 show summary                        - Display bridge ports list
```

### accept-frame-type
```text
# cli error: Invalid Command
SF-1p-187>config>bridge(1)# accept-frame-type
```

### bind
```text
# cli error: Invalid Command
SF-1p-187>config>bridge(1)# bind
```

### name
```text
<bridge-name>        : Bridge name [1..32 chars]


SF-1p-187>config>bridge(1)# name
```

### pvid
```text
# cli error: Invalid Command
SF-1p-187>config>bridge(1)# pvid
```

### shutdown
```text
# cli error: Invalid Command
SF-1p-187>config>bridge(1)# shutdown
```

## configure bridge NAME vlan

Level help (`?`):
```text
aging-time                     - Configure MAC aging time
      clear-mac-table                - Clear MAC address table
 [no] filtering                      - Enable filtering forwarding mode
 [no] name                           - Configure bridge name
 [no] port                           + Configure bridge port
 [no] static-mac                     - Configure static MAC
 [no] vlan                           + Configure bridge VLAN
 [no] vlan-aware                     - Enable VLAN aware mode

 show mac-address-table              - Display MAC address table
 show summary                        - Display bridge ports list
 show vlans                          - Display VLAN membership
```

### tagged-port
```text
# cli error: Invalid Command
SF-1p-187>config>bridge(1)# tagged-port
```

### untagged-port
```text
# cli error: Invalid Command
SF-1p-187>config>bridge(1)# untagged-port
```

## configure crypto

Level help (`?`):
```text
[no] ca                             + Add or remove a CA
 [no] crypto-map                     + Configure crypto map
 [no] ipsec-transform-set            + Configure IPsec phase 2 policy
 [no] isakmp-key                     - Configure IKE pre-shared key
 [no] isakmp-policy                  + Configure IPsec phase 1 policy
      key                            + RSA key management level
      pki                            + PKI (public key infrastructure) level
```

### ca *(parameterized — inner help harvested under "configure crypto ca NAME")*
```text
<ca-name>            : CA name [1..20 chars]


SF-1p-187>config>crypto# ca
```

### crypto-map *(parameterized — inner help harvested under "configure crypto crypto-map NAME")*
```text
<name>               : [1..80 chars]


SF-1p-187>config>crypto# crypto-map
```

### ipsec-transform-set *(parameterized — inner help harvested under "configure crypto ipsec-transform-set NAME")*
```text
<name>               : [1..80 chars]


SF-1p-187>config>crypto# ipsec-transform-set
```

### isakmp-key
```text
<pre-shared-key>     : IKE pre-shared key [1..80 chars]


SF-1p-187>config>crypto# isakmp-key
```

### isakmp-policy *(parameterized — inner help harvested under "configure crypto isakmp-policy NAME")*
```text
<sequence>           : [number]


SF-1p-187>config>crypto# isakmp-policy
```

## configure crypto ca NAME

Level help (`?`):
```text
[no] address                        - Configure CA address
 [no] certificate-auto-renew         - Enable certificate auto renewal
 [no] crl-auto-renew                 - Enable CRL auto renewal
 [no] protocol                       - Configure protocol to communicate with 
                                       the CA
```

### address
```text
<ip>                 : 
 <url>                : 


SF-1p-187>config>crypto>ca(CA-cert)# address
```

### certificate-auto-renew
```text
<CR>

SF-1p-187>config>crypto>ca(CA-cert)# certificate-auto-renew
```

### crl-auto-renew
```text
<CR>

SF-1p-187>config>crypto>ca(CA-cert)# crl-auto-renew
```

### protocol
```text
<scep>               : SCEP protocol
 <est>                : EST protocol


SF-1p-187>config>crypto>ca(CA-cert)# protocol
```

## configure crypto crypto-map NAME

Level help (`?`):
```text
ike-authentication             - Configure authentication method
      ike-identity-local             - Local IKE identity
      ike-identity-local-x509        - Configure local IKE identity with X.509 
                                       certificate
      ike-identity-remote            - Remote IKE identity
      ike-identity-remote-x509       - Configure remote IKE identity with X.509 
                                       certificate
      ike-sa-lifetime                - Configure SA lifetime
      ike-sa-negotiation             - Configure SA negotiation mode
      ike-version                    - IKE version
 [no] match-address                  - Assign ACL
 [no] peer-address                   - Configure IPsec peer IP address
 [no] pfs-group                      - Configure PFS group
 [no] responder-only                 - Whether or not to initiate connection
 [no] sa-lifetime                    - Configure SA lifetime
 [no] sequence-number                - Configure crypto map priority
 [no] transform-set                  - Assign IPsec phase 2 policy


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$
```

### ike-authentication
```text
<pre-share>          : 
 <rsa-signature>      : 


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ ike-authentication
```

### ike-identity-local
```text
<default-address>    : 
 <address>            : 
 <default-hostname>   : 
 <hostname>           : 


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-local
```

### ike-identity-local-x509
```text
<distinguished-name> : 
 <string>             : 


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-local-x509
```

### ike-identity-remote
```text
<default-address>    : 
 <address>            : 
 <hostname>           : 


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-remote
```

### ike-identity-remote-x509
```text
<any>                : 
 <string>             : 


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-remote-x509
```

### ike-sa-lifetime
```text
<seconds>            : [60..86400, default 86400]


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ ike-sa-lifetime
```

### ike-sa-negotiation
```text
<main>               : 
 <aggressive>         : 


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ ike-sa-negotiation
```

### ike-version
```text
<1>                  : 
 <2>                  : 


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ ike-version
```

### match-address
```text
<name>               : [1..80 chars]


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ match-address
```

### peer-address
```text
<ip-address>         : [0.0.0.0|0:0:0:0::0, default 0.0.0.0]


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ peer-address
```

### pfs-group
```text
<1>                  : 
 <2>                  : 
 <5>                  : 
 <14>                 : 
 <19>                 : 
 <20>                 : 


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ pfs-group
```

### responder-only
```text
<CR>

SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ responder-only
```

### sa-lifetime
```text
<CR>
 seconds
 kilobytes

SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ sa-lifetime
```

### sequence-number
```text
<number>             : [1..1000, default 10]


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ sequence-number
```

### transform-set
```text
<name-1>             : [1..80 chars]


SF-1p-187>config>crypto>crypto-map(zzz-hrvst)$ transform-set
```

## configure crypto ipsec-transform-set NAME

Level help (`?`):
```text
algorithms                     - Configure IPsec phase 2 algorithms
      mode                           - Tunnel or transport mode


SF-1p-187>config>crypto>ipsec-transform-set(zzz-hrvst)$
```

### algorithms
```text
<esp-aes-cbc-128>    : 
 <esp-aes-cbc-256>    : 
 <esp-aes-gcm-128>    : 
 <esp-aes-gcm-256>    : 
 <esp-null>           : 
 <esp-aes-gmac-128>   : 
 <esp-aes-gmac-256>   : 


SF-1p-187>config>crypto>ipsec-transform-set(zzz-hrvst)$ algorithms
```

### mode
```text
<tunnel>             : 
 <transport>          : 


SF-1p-187>config>crypto>ipsec-transform-set(zzz-hrvst)$ mode
```

## configure crypto isakmp-policy NAME

Level help (`?`):
```text
encryption                     - Configure encryption algorithm
      group                          - Configure Diffie Hellman group
      hash                           - Configure hashing algorithm


SF-1p-187>config>crypto>isakmp-policy(1)$
```

### encryption
```text
<aes-cbc-128>        : 
 <aes-cbc-256>        : 
 <aes-128-gcm-64>     : 
 <aes-128-gcm-96>     : 
 <aes-128-gcm-128>    : 
 <aes-256-gcm-64>     : 
 <aes-256-gcm-96>     : 
 <aes-256-gcm-128>    : 


SF-1p-187>config>crypto>isakmp-policy(1)$ encryption
```

### group
```text
<1>                  : 
 <2>                  : 
 <5>                  : 
 <14>                 : 
 <19>                 : 
 <20>                 : 


SF-1p-187>config>crypto>isakmp-policy(1)$ group
```

### hash
```text
<sha1>               : 
 <sha2-256>           : 
 <sha2-512>           : 


SF-1p-187>config>crypto>isakmp-policy(1)$ hash
```

## configure crypto key

Level help (`?`):
```text
delete                         - Delete key pair
      generate                       - Generate key pair
      import                         - Import key pair

 show public-key                     - Display public key
```

### delete
```text
key-name

SF-1p-187>config>crypto>key# delete
```

### generate
```text
key-name

SF-1p-187>config>crypto>key# generate
```

### import
```text
key-name

SF-1p-187>config>crypto>key# import
```

### show public-key
```text
<CR>

SF-1p-187>config>crypto>key# show public-key
```

## configure crypto pki

Level help (`?`):
```text
authenticate                   - Authenticate CA by importing its 
                                       certificate
      delete-certificate             - Delete certificate
      delete-crl                     - Delete CRL
 [no] enroll-attributes              + Add or remove a enroll attributes
      enroll-from-configuration      - Create CSR for enrollment by a CA using 
                                       predefined enroll attributes
      enroll                         - Create CSR for enrollment by a CA
      export-crl                     - Export CRL
      import-certificate             - Import signed CSR certificate
      import-crl                     - Import CRL from CA
      self-sign-certificate          - Create permanent self-signed certificate

 show certificate                    - Print certificate contents
 show certificate-summary            - Display summary of certificates stored 
                                        in the device
 show crl-summary                    - Display list of CRL files stored in the 
                                        device
```

### authenticate
```text
certificate-name

SF-1p-187>config>crypto>pki# authenticate
```

### delete-certificate
```text
certificate-name

SF-1p-187>config>crypto>pki# delete-certificate
```

### delete-crl
```text
crl-name

SF-1p-187>config>crypto>pki# delete-crl
```

### enroll
```text
<CR>
 certificate-url
 certificate-name
 common-name
 locality
 state
 email
 organization
 organizational-unit
 country
 challenge-password
 <serial-number>      : 


SF-1p-187>config>crypto>pki# enroll
```

### enroll-attributes *(parameterized — inner help harvested under "configure crypto pki enroll-attributes NAME")*
```text
<name>               : Enroll attributes name [1..32 chars]


SF-1p-187>config>crypto>pki# enroll-attributes
```

### enroll-from-configuration
```text
attribute-set

SF-1p-187>config>crypto>pki# enroll-from-configuration
```

### export-crl
```text
crl-name

SF-1p-187>config>crypto>pki# export-crl
```

### import-certificate
```text
certificate-name

SF-1p-187>config>crypto>pki# import-certificate
```

### import-crl
```text
crl-name

SF-1p-187>config>crypto>pki# import-crl
```

### self-sign-certificate
```text
certificate-name

SF-1p-187>config>crypto>pki# self-sign-certificate
```

### show certificate
```text
certificate-name

SF-1p-187>config>crypto>pki# show certificate
```

### show certificate-summary
```text
<CR>
 owner
 <valid-only>         : 
 <invalid-only>       : 


SF-1p-187>config>crypto>pki# show certificate-summary
```

### show crl-summary
```text
<CR>

SF-1p-187>config>crypto>pki# show crl-summary
```

## configure crypto pki enroll-attributes NAME

Level help (`?`):
```text
[no] ca-url                         - Configure CA URL to send the CSR to
 [no] challenge-password             - Configure challenge password to present 
                                       to the CA
 [no] common-name                    - Configure certificate subject common name
 [no] country                        - Configure certificate subject country
 [no] locality                       - Configure certificate subject locality
 [no] organization                   - Configure certificate subject 
                                       organization
 [no] organizational-unit            - Configure certificate subject 
                                       organizational unit
 [no] san-dns-name                   - Configure certificate SAN DNS name
 [no] san-email                      - Configure certificate SAN email
 [no] san-ip-address                 - Configure certificate SAN IP address
 [no] san-uri                        - Configure certificate SAN URI
 [no] serial-number                  - Configure certificate subject 
                                       serial-number
 [no] state                          - Configure certificate subject state
```

### ca-url
```text
<string>             : [1..255 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# ca-url
```

### challenge-password
```text
<string>             : Challenge password to present to the CA [1..80 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# challenge-password
```

### common-name
```text
<string>             : Certificate subject common name [1..64 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# common-name
```

### country
```text
<string>             : Certificate subject country (ISO 3166 two-letter code) 
                        [2..2 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# country
```

### locality
```text
<string>             : Certificate subject locality [1..128 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# locality
```

### organization
```text
<string>             : Certificate subject organization [1..64 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# organization
```

### organizational-unit
```text
<string>             : Certificate subject organizational unit [1..32 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# organizational-unit
```

### san-dns-name
```text
<dns-name>           : [1..255 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# san-dns-name
```

### san-email
```text
<email>              : Certificate SAN email (rfc822Name) [3..255 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# san-email
```

### san-ip-address
```text
<ip-address>         : Certificate SAN IP address (iPAddress) [0.0.0.0|
                        0:0:0:0::0]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# san-ip-address
```

### san-uri
```text
<uri>                : Certificate SAN URI (uniformResourceIdentifier) [1..255 
                        chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# san-uri
```

### serial-number
```text
<dmi>                : 
 <value>              : 


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# serial-number
```

### state
```text
<string>             : Certificate subject state [1..128 chars]


SF-1p-187>config>crypto>pki>enroll-attributes(AAA)# state
```

## configure fault

Level help (`?`):
```text
[no] fault-propagation              + Fault propagation configuration
 [no] group                          + Create group
```

### fault-propagation
```text
<router-interface>   : 
 <ip-monitor-group>   : 
 <tunnel>             : 


SF-1p-187>config>fault# fault-propagation
```

### group *(not entered — parameterized context)*
```text
ip-monitor

SF-1p-187>config>fault# group
```

## configure management

Level help (`?`):
```text
access                         + Access commands
      dscp                           - Configure DSCP value
 [no] login-user                     + Create user
 [no] management-address             - Configure management protocols source IP
      netconf                        + Netconf commands
      radius                         + Configure RADIUS client
      snmp                           + Defines SNMP settings
      tacacsplus                     + Configure TACACS+ client

 show failed-login-attempts
 show ssh-server
 show users-details                  - Display connected users
 show users                          - Show users
```

### dscp
```text
<value>              : DSCP value [0..63, default 0]


SF-1p-187>config>mngmnt# dscp
```

### login-user *(parameterized — inner help harvested under "configure management login-user NAME")*
```text
<name>               : User name [1..20 chars]


SF-1p-187>config>mngmnt# login-user
```

### management-address
```text
<ipv4>               : ipv4
 <ipv6>               : ipv6
 <ip-address>         : Management protocols source IP [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>mngmnt# management-address
```

### show failed-login-attempts
```text
<CR>

SF-1p-187>config>mngmnt# show failed-login-attempts
```

### show ssh-server
```text
<fingerprint>        : 


SF-1p-187>config>mngmnt# show ssh-server
```

### show users
```text
<CR>

SF-1p-187>config>mngmnt# show users
```

### show users-details
```text
<CR>

SF-1p-187>config>mngmnt# show users-details
```

## configure management access

Level help (`?`):
```text
[no] access-group                   - Apply ACL to device management
      auth-policy                    - Configure authentication methods
 [no] ban-default-login-password     - Disallow default login password
      clear-statistics               - Clear ACL statistics
      command-authorization          - Configure command authorization
 [no] enrollment-notification-nms    + NMS enrollment notification configuration
      ftps                           - Configure FTPS
 [no] known-host                     - Configure host fingerprint to trust it
 [no] login-password-black-list      - Configure string not allowed in login 
                                       password
 [no] login-password-properties      - Configure login password strength 
                                       requirement
      opcua-authentification-policy  - Configure opcua authentication methods
 [no] rest-get                       - Enable REST get interface
 [no] scp-client                     - Enable SCP client
 [no] sftp                           - Enable SFTP
      sms                            + SMS configuration
 [no] snmp                           - Enable SNMP
      ssh-encryption                 - Configure acceptable SSH encryption 
                                       algorithms
      ssh-key-exchange               - Configure acceptable SSH key exchange 
                                       algorithms
      ssh-mac                        - Configure acceptable SSH MAC algorithms
 [no] ssh                            - Enable SSH
      ssh-server-host-key            - Configure acceptable SSH server host key 
                                       algorithms
 [no] telnet                         - Enable Telnet
 [no] tftp                           - Enable TFTP
 [no] virtualization-rest            - Enable REST management for virtualization
 [no] web                            - Enable Web
 [no] ztc-after-reboot               - Start ZTC process after next reboot
 [no] ztc-bootstrap                  - Enable ZTC bootstrap provisioning
 [no] ztc-tftp-disable               - 

 show access-list                    - ACL Information
 show enrollment-status              - Show enrollment notification NMS status
 show statistics                     - Show ACL statistics
 show status
```

### access-group
```text
<acl-name>           : ACL name [string]


SF-1p-187>config>mngmnt>access# access-group
```

### auth-policy
```text
<1st-level>          : First method


SF-1p-187>config>mngmnt>access# auth-policy
```

### ban-default-login-password
```text
<CR>

SF-1p-187>config>mngmnt>access# ban-default-login-password
```

### clear-statistics
```text
<ipv4>               : IPv4
 <ipv6>               : IPv6


SF-1p-187>config>mngmnt>access# clear-statistics
```

### command-authorization
```text
<1st-method>         : First method


SF-1p-187>config>mngmnt>access# command-authorization
```

### enrollment-notification-nms *(not entered — parameterized context)*
```text
<ip-address>         : IP address or NMS name to send notifications to [0.0.0.0
                        |0:0:0:0::0]


SF-1p-187>config>mngmnt>access# enrollment-notification-nms
```

### ftps
```text
<CR>
 certificate

SF-1p-187>config>mngmnt>access# ftps
```

### known-host
```text
<ip-address>         : 
 <host-name>          : 


SF-1p-187>config>mngmnt>access# known-host
```

### login-password-black-list
```text
<banned-string>      : String not allowed in login password [4..20 chars]


SF-1p-187>config>mngmnt>access# login-password-black-list
```

### login-password-properties
```text
<CR>
 min-characters
 min-digits
 min-symbols
 min-lowercase
 min-uppercase
 max-consecutive
 <lifetime>           : 


SF-1p-187>config>mngmnt>access# login-password-properties
```

### opcua-authentification-policy
```text
<1st-level>          : First method


SF-1p-187>config>mngmnt>access# opcua-authentification-policy
```

### rest-get
```text
<CR>
 certificate

SF-1p-187>config>mngmnt>access# rest-get
```

### scp-client
```text
<CR>

SF-1p-187>config>mngmnt>access# scp-client
```

### sftp
```text
<CR>

SF-1p-187>config>mngmnt>access# sftp
```

### show access-list
```text
<summary>            : ACL summary


SF-1p-187>config>mngmnt>access# show access-list
```

### show enrollment-status
```text
<CR>

SF-1p-187>config>mngmnt>access# show enrollment-status
```

### show statistics
```text
<ipv4>               : IPv4
 <ipv6>               : IPv6


SF-1p-187>config>mngmnt>access# show statistics
```

### show status
```text
<CR>

SF-1p-187>config>mngmnt>access# show status
```

### snmp
```text
<CR>

SF-1p-187>config>mngmnt>access# snmp
```

### ssh
```text
<CR>
 port

SF-1p-187>config>mngmnt>access# ssh
```

### ssh-encryption
```text
<all>                : 
 <algorithm>          : 


SF-1p-187>config>mngmnt>access# ssh-encryption
```

### ssh-key-exchange
```text
<all>                : 
 <algorithm>          : 


SF-1p-187>config>mngmnt>access# ssh-key-exchange
```

### ssh-mac
```text
<all>                : 
 <algorithm>          : 


SF-1p-187>config>mngmnt>access# ssh-mac
```

### ssh-server-host-key
```text
<all>                : 
 <algorithm>          : 


SF-1p-187>config>mngmnt>access# ssh-server-host-key
```

### telnet
```text
<CR>

SF-1p-187>config>mngmnt>access# telnet
```

### tftp
```text
<CR>

SF-1p-187>config>mngmnt>access# tftp
```

### virtualization-rest
```text
<CR>
 certificate

SF-1p-187>config>mngmnt>access# virtualization-rest
```

### web
```text
<CR>
 certificate

SF-1p-187>config>mngmnt>access# web
```

### ztc-after-reboot
```text
<CR>

SF-1p-187>config>mngmnt>access# ztc-after-reboot
```

### ztc-bootstrap
```text
<CR>
 url
 <no-revertive>       : 
 <password>           : 


SF-1p-187>config>mngmnt>access# ztc-bootstrap
```

### ztc-tftp-disable
```text
<CR>

SF-1p-187>config>mngmnt>access# ztc-tftp-disable
```

## configure management access sms

Level help (`?`):
```text
[no] authentication                 - Configure SMS management authentication 
                                       mode
 [no] caller-id                      - Configure SMS management authorized 
                                       caller
```

### authentication
```text
<otp>                : One-time password authentication


SF-1p-187>config>mngmnt>access>sms# authentication
```

### caller-id
```text
<phone-number>       : Authorized caller number [1..15 chars]


SF-1p-187>config>mngmnt>access>sms# caller-id
```

## configure management login-user NAME

Level help (`?`):
```text
authentication-method          - Login user authentication method
      level                          - Login user level
 [no] otp-authentication             - Enable OTP authentication
      password                       - Password: hashed password [40 chars]; 
                                       non-hashed
 [no] public-key                     - User public key
 [no] shutdown                       - Disable user
```

### authentication-method
```text
<password>           : Password
 <public-key>         : Public key


SF-1p-187>config>mngmnt>login-user(su)# authentication-method
```

### level
```text
<su>                 : Super user
 <oper>               : Operator
 <tech>               : Technician
 <user>               : Read-Only
 <linux-user>         : Linux User
 <virt>               : Virt
 <netconf-su>         : Netconf Super User
 <linux-net-admin>    : Linux Network and Virtualization
 <linux-tech>         : Linux Network, Virtualization and Processes


SF-1p-187>config>mngmnt>login-user(su)# level
```

### otp-authentication
```text
phone

SF-1p-187>config>mngmnt>login-user(su)# otp-authentication
```

### password
```text
<password>           : Password: non-hashed password [20 chars]; hashed [40 | 
                        144 | 344] [string]


SF-1p-187>config>mngmnt>login-user(su)# password
```

### public-key
```text
<public-key>         : Public key format: <inv comma> ssh-rsa <space> public 
                        key string <space> comment <inv comma> [1..512 chars]


SF-1p-187>config>mngmnt>login-user(su)# public-key
```

### shutdown
```text
<CR>

SF-1p-187>config>mngmnt>login-user(su)# shutdown
```

## configure management netconf

Level help (`?`):
```text
inactivity-timeout             - Configure NETCONF session inactivity 
                                       timeout
 [no] shutdown                       - Disable NETCONF
```

### inactivity-timeout
```text
<time>               : 
 <infinite>           : 


SF-1p-187>config>mngmnt>netconf# inactivity-timeout
```

### shutdown
```text
<CR>

SF-1p-187>config>mngmnt>netconf# shutdown
```

## configure management radius

Level help (`?`):
```text
clear-statistics               - Clear RADIUS statistics
      server                         + Connect to RADIUS server

 show statistics                     - RADIUS  statistics
```

### clear-statistics
```text
<CR>

SF-1p-187>config>mngmnt>radius# clear-statistics
```

### server *(not entered — parameterized context)*
```text
<server-id>          : Specify RADIUS server [1..4]


SF-1p-187>config>mngmnt>radius# server
```

### show statistics
```text
<CR>

SF-1p-187>config>mngmnt>radius# show statistics
```

## configure management snmp

Level help (`?`):
```text
[no] access-group                   + Configure access group
 [no] bootstrap-notification         - Enable bootstrap notification 
 [no] community                      + Configure community
 [no] config-change-notification     - Enable/disable configuration change 
                                       notification sending
 [no] notify                         + Configure notification group
 [no] notify-filter                  + Configure notification group filter
 [no] notify-filter-profile          + Configure notification group profile
 [no] security-to-group              + Assign security to group
      snmp-engine-id                 - Configure SNMP Engine ID
 [no] target                         + Configure SNMP target
 [no] target-params                  + Configure target parameters
      trap-sync-group                + Configure trap synchronization group
 [no] user                           + Configure SNMP user
 [no] view                           + Configure view

 show snmpv3                         - SNMPv3 information
 show trap-sync                      - Show trap synchronization
```

### access-group *(not entered — parameterized context)*
```text
<group-name>         : Group name [string]


SF-1p-187>config>mngmnt>snmp# access-group

auto-create probe 'access-group zzz-hrvst' refused.
device response: access-group zzz-hrvst
#                                                    ^
# cli error: parameter or keyword missing or wrong
 - access-group <group-name> {snmpv1|snmpv2c|usm} {no-auth-no-priv|
   auth-no-priv|auth-priv}
 - no access-group <group-name> {snmpv1|snmpv2c|usm} {no-auth-no-priv|
   auth-no-priv|auth-priv}
 <group-name>         : Group name [string]
 <snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <usm>                : USM
 <no-auth-no-priv>    : No Authentication/No Privacy
 <auth-no-priv>       : Authentication/No Privacy
 <auth-priv>          : Authentication/Privacy

SF-1p-187>config>mngmnt>snmp#
```

### bootstrap-notification
```text
<CR>

SF-1p-187>config>mngmnt>snmp# bootstrap-notification
```

### community *(not entered — parameterized context)*
```text
<community-index>    : Community index [string]


SF-1p-187>config>mngmnt>snmp# community
```

### config-change-notification
```text
<CR>

SF-1p-187>config>mngmnt>snmp# config-change-notification
```

### notify *(parameterized — inner help harvested under "configure management snmp notify NAME")*
```text
<notify-name>        : Notification group name [string]


SF-1p-187>config>mngmnt>snmp# notify
```

### notify-filter *(not entered — parameterized context)*
```text
<name>               : Notification group name [string]


SF-1p-187>config>mngmnt>snmp# notify-filter

auto-create probe 'notify-filter zzz-hrvst' refused.
device response: notify-filter zzz-hrvst
#                                                     ^
# cli error: parameter or keyword missing or wrong
 - notify-filter <name> <sub-tree-oid>
 - no notify-filter <name> <sub-tree-oid>
 <name>               : Notification group name [string]
 <sub-tree-oid>       : Sub-tree OID [1.3.6.1...]

SF-1p-187>config>mngmnt>snmp#
```

### notify-filter-profile *(parameterized — inner help harvested under "configure management snmp notify-filter-profile NAME")*
```text
<params-name>        : Parameter name [string]


SF-1p-187>config>mngmnt>snmp# notify-filter-profile
```

### security-to-group *(not entered — parameterized context)*
```text
<snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <usm>                : USM


SF-1p-187>config>mngmnt>snmp# security-to-group
```

### show snmpv3
```text
information

SF-1p-187>config>mngmnt>snmp# show snmpv3
```

### show trap-sync
```text
<CR>

SF-1p-187>config>mngmnt>snmp# show trap-sync
```

### snmp-engine-id
```text
<mac>                : MAC
 <ipv4>               : IPv4
 <ipv6>               : IPv6
 <text>               : Free text


SF-1p-187>config>mngmnt>snmp# snmp-engine-id
```

### target *(parameterized — inner help harvested under "configure management snmp target NAME")*
```text
<name>               : Target name [1..32 chars]


SF-1p-187>config>mngmnt>snmp# target
```

### target-params *(parameterized — inner help harvested under "configure management snmp target-params NAME")*
```text
<name>               : Target parameters name [1..32 chars]


SF-1p-187>config>mngmnt>snmp# target-params
```

### trap-sync-group *(not entered — parameterized context)*
```text
<group-id>           : Group ID [number] [1..10]


SF-1p-187>config>mngmnt>snmp# trap-sync-group
```

### user *(not entered — parameterized context)*
```text
<security-name>      : Security name [string]


SF-1p-187>config>mngmnt>snmp# user
```

### view *(not entered — parameterized context)*
```text
<view-name>          : View name [string]


SF-1p-187>config>mngmnt>snmp# view

auto-create probe 'view zzz-hrvst' refused.
device response: view zzz-hrvst
#                                            ^
# cli error: parameter or keyword missing or wrong
 - view <view-name> <sub-tree-oid>
 - no view <view-name> <sub-tree-oid>
 <view-name>          : View name [string]
 <sub-tree-oid>       : Subtree OID [1.3.6.1...]

SF-1p-187>config>mngmnt>snmp#
```

## configure management snmp notify NAME

Level help (`?`):
```text
[no] bind                           - Bind trap
 [no] shutdown                       - Disable notification group
      tag                            - Tag


SF-1p-187>config>mngmnt>snmp>notify(zzz-hrvst)$
```

### bind
```text
<systemTraceMsgProtoM: 


SF-1p-187>config>mngmnt>snmp>notify(zzz-hrvst)$ bind
```

### shutdown
```text
<CR>

SF-1p-187>config>mngmnt>snmp>notify(zzz-hrvst)$ shutdown
```

### tag
```text
<argument>           : Tag [string]


SF-1p-187>config>mngmnt>snmp>notify(zzz-hrvst)$ tag
```

## configure management snmp notify-filter-profile NAME

Level help (`?`):
```text
profile-name                   - Profile name
 [no] shutdown                       - Disable notification group


SF-1p-187>config>mngmnt>snmp>filter-profile$
```

### profile-name
```text
<argument>           : Profile name [string]


SF-1p-187>config>mngmnt>snmp>filter-profile$ profile-name
```

### shutdown
```text
<CR>

SF-1p-187>config>mngmnt>snmp>filter-profile$ shutdown
```

## configure management snmp target NAME

Level help (`?`):
```text
address                        - Target address
 [no] tag-list                       - Configure tag list
      target-params                  - Target parameters
 [no] trap-sync-group                - Configure trap synchronization group


SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$
```

### address
```text
<udp-domain>         : UDP
 <oam-domain>         : OAM
 <udp-ipv4-domain>    : UDP over IPv4
 <udp-ipv6-domain>    : UDP over IPv6


SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$ address
```

### shutdown
```text
# cli error: Invalid Command
SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$ shutdown
```

### tag-list
```text
<list>               : Tag list [string]


SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$ tag-list
```

### target-params
```text
<params-name>        : Parameter [string]


SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$ target-params
```

### trap-sync-group
```text
<group-id>           : Group ID [number] [1..10]


SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$ trap-sync-group
```

## configure management snmp target-params NAME

Level help (`?`):
```text
message-processing-model       - Configure message processing model
      security                       - Configure security
      version                        - Configure SNMP version


SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$
```

### message-processing-model
```text
<snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <snmpv3>             : SNMPv3


SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$ message-processing-model
```

### security
```text
<CR>
 name
 level

SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$ security
```

### shutdown
```text
# cli error: Invalid Command
SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$ shutdown
```

### version
```text
<snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <usm>                : USM


SF-1p-187>config>mngmnt>snmp>target(zzz-hrvst)$ version
```

## configure management tacacsplus

Level help (`?`):
```text
[no] group                          + TACACS+ server group
 [no] privilege-level                - Configure mapped between privilege level 
                                       to cli level
 [no] server                         + Add TACACS+ server
```

### group *(parameterized — inner help harvested under "configure management tacacsplus group NAME")*
```text
<group-name>         : TACACS+ server group name [1..80 chars]


SF-1p-187>config>mngmnt>tacacsplus# group
```

### privilege-level
```text
<tacacs-privilege-lev: TACACS+ privilege level [0..15]


SF-1p-187>config>mngmnt>tacacsplus# privilege-level
```

### server *(not entered — parameterized context)*
```text
<ip>                 : TACACS+ server IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>mngmnt>tacacsplus# server
```

## configure management tacacsplus group NAME

Level help (`?`):
```text
[no] accounting                     - Enable TACACS+ accounting


SF-1p-187>config>mngmnt>tacacsplus>group(zzz-hrvst)$
```

### accounting
```text
<CR>
 <shell>              : Shell accounting
 <system>             : System accounting
 <commands>           : Commands accounting


SF-1p-187>config>mngmnt>tacacsplus>group(zzz-hrvst)$ accounting
```

## configure monitor

Level help (`?`):
```text
[no] mirroring-session              + Configure mirroring session
```

### mirroring-session *(parameterized — inner help harvested under "configure monitor mirroring-session NAME")*
```text
<number>             : Mirroring session number [number]


SF-1p-187>config>monitor# mirroring-session
```

## configure monitor mirroring-session NAME

Level help (`?`):
```text
[no] destination                    - Configure mirroring destination. Can not 
                                       be used in more then one mirroring 
                                       session
 [no] shutdown                       - Disable session
 [no] source                         - Configure mirroring source


SF-1p-187>config>monitor>mirroring-session(1)$
```

### destination
```text
<ethernet>           : 


SF-1p-187>config>monitor>mirroring-session(1)$ destination
```

### shutdown
```text
<CR>

SF-1p-187>config>monitor>mirroring-session(1)$ shutdown
```

### source
```text
<port>               : 
 <tunnel-interface>   : 


SF-1p-187>config>monitor>mirroring-session(1)$ source
```

## configure oam

Level help (`?`):
```text
[no] ip-monitoring                  + Define ip-monitoring entity
```

### ip-monitoring *(parameterized — inner help harvested under "configure oam ip-monitoring NAME")*
```text
<name>               : Define ip-monitoring entity name [1..32 chars]


SF-1p-187>config>oam# ip-monitoring
```

## configure oam ip-monitoring NAME

Level help (`?`):
```text
fail-criteria                  - Configure fail criteria
      icmp-timeout                   - Configure monitoring icmp timeout (in 
                                       seconds)
      target                         - Configure monitoring target IP address
      transmit-interval              - Configure monitoring transmit interval 
                                       (in seconds)
      window-size                    - Configure monitoring sliding window-size 
                                       (in seconds)

 show status                         - Display ip-monitoring entity status

SF-1p-187>config>oam>ip-monitoring(zzz-hrvst)$
```

### fail-criteria
```text
<fail-thr-percents>  : The threshold, in percents, over which a monitoring 
                        failure is declared [1..100, default 60]


SF-1p-187>config>oam>ip-monitoring(zzz-hrvst)$ fail-criteria
```

### icmp-timeout
```text
<seconds>            : The timeout to decide on failure after icmp transmission
                         [1..30, default 1]


SF-1p-187>config>oam>ip-monitoring(zzz-hrvst)$ icmp-timeout
```

### show status
```text
<CR>

SF-1p-187>config>oam>ip-monitoring(zzz-hrvst)$ show status
```

### target
```text
<ip-address>         : The IP Address of the ICMP-echo target [0.0.0.0|
                        0:0:0:0::0]


SF-1p-187>config>oam>ip-monitoring(zzz-hrvst)$ target
```

### transmit-interval
```text
<seconds>            : The interval period between monitoring transmissions 
                        [1..30, default 1]


SF-1p-187>config>oam>ip-monitoring(zzz-hrvst)$ transmit-interval
```

### window-size
```text
<seconds>            : The size, in seconds, of the monitor sliding window 
                        [1..30, default 5]


SF-1p-187>config>oam>ip-monitoring(zzz-hrvst)$ window-size
```

## configure port

Level help (`?`):
```text
cellular                       + Cellular interface configuration
      ethernet                       + Specifies Ethernet parameters
 [no] ppp                            + 
      serial                         + Serial port level
      virtual                        + Virtual port level
 [no] wifi-client                    + WiFi client level
 [no] wifi-country-code              - Configure WiFi country code
      wlan                           + Configure wlan interface

 show summary                        - Display port status summary
 show wifi
```

### cellular *(not entered — parameterized context)*
```text
<lte>                : 


SF-1p-187>config>port# cellular
```

### ethernet *(parameterized — inner help harvested under "configure port ethernet NAME")*
```text
<1>                  : 
 <2>                  : 
 <3>                  : 
 <4>                  : 
 <5>                  : 
 <6>                  : 
 <switch1>            : 


SF-1p-187>config>port# ethernet
```

### ppp *(parameterized — inner help harvested under "configure port ppp NAME")*
```text
<port-number>        : PPP Port number [number]


SF-1p-187>config>port# ppp
```

### serial *(parameterized — inner help harvested under "configure port serial NAME")*
```text
<2>                  : 
 <1>                  : 


SF-1p-187>config>port# serial
```

### show summary
```text
<CR>

SF-1p-187>config>port# show summary
```

### show wifi
```text
<CR>

SF-1p-187>config>port# show wifi
```

### virtual *(parameterized — inner help harvested under "configure port virtual NAME")*
```text
<port-number>        : Virtual port level [1..10]


SF-1p-187>config>port# virtual
```

### wifi-country-code
```text
<afghanistan>        : 
 <aland-islands>      : 
 <albania>            : 
 <algeria>            : 
 <american-samoa>     : 
 <andorra>            : 
 <angola>             : 
 <anguilla>           : 
 <antarctica>         : 
 <antigua-barbuda>    : 
 <argentina>          : 
 <armenia>            : 
 <aruba>              : 
 <australia>          : 
 <austria>            : 
 <azerbaijan>         : 
 <bahamas>            : 
 <bahrain>            : 
 <bangladesh>         : 
 <barbados>           : 
 <belarus>            : 
 <belgium>            : 
 <belize>             : 
 <benin>              : 
 <bermuda>            : 
 <bhutan>             : 
 <bolivia>            : 
 <bonaire-sint-eustati: 
 <bosnia-herzegovina> : 
 <botswana>           : 
 <bouvet-island>      : 
 <brazil>             : 
 <british-indian-ocean: 
 <brunei-darussalam>  : 
 <bulgaria>           : 
 <burkina-faso>       : 
 <burundi>            : 
 <cambodia>           : 
 <cameroon>           : 
 <canada>             : 
 <cape-verde>         : 
 <cayman-islands>     : 
 <central-african-repu: 
 <chad>               : 
 <chile>              : 
 <china>              : 
 <christmas-island>   : 
 <cocos-islands>      : 
 <colombia>           : 
 <comoros>            : 
 <congo>              : 
 <congo-democratic-rep: 
 <cook-islands>       : 
 <costa-rica>         : 
 <cote-d-ivoire>      : 
 <croatia>            : 
 <cuba>               : 
 <curacao>            : 
 <cyprus>             : 
 <czech-republic>     : 
 <denmark>            : 
 <djibouti>           : 
 <dominica>           : 
 <dominican-republic> : 
 <ecuador>            : 
 <egypt>              : 
 <el-salvador>        : 
 <equatorial-guinea>  : 
 <eritrea>            : 
 <estonia>            : 
 <ethiopia>           : 
 <falkland-islands>   : 
 <faroe-islands>      : 
 <fiji>               : 
 <finland>            : 
 <france>             : 
 <french-guiana>      : 
 <french-polynesia>   : 
 <french-southern-terr: 
 <gabon>              : 
 <gambia>             : 
 <georgia>            : 
 <germany>            : 
 <ghana>              : 
 <gibraltar>          : 
 <greece>             : 
 <greenland>          : 
 <grenada>            : 
 <guadeloupe>         : 
 <guam>               : 
 <guatemala>          : 
 <guernsey>           : 
 <guinea>             : 
 <guinea-bissau>      : 
 <guyana>             : 
 <haiti>              : 
 <heard-island-mcdonal: 
 <vatican>            : 
 <honduras>           : 
 <hong-kong>          : 
 <hungary>            : 
 <iceland>            : 
 <india>              : 
 <indonesia>          : 
 <iran>               : 
 <iraq>               : 
 <ireland>            : 
 <isle-of-man>        : 
 <israel>             : 
 <italy>              : 
 <jamaica>            : 
 <japan>              : 
 <jersey>             : 
 <jordan>             : 
 <kazakhstan>         : 
 <kenya>              : 
 <kiribati>           : 
 <korea-democratic-peo: 
 <korea-republic>     : 
 <kuwait>             : 
 <kyrgyzstan>         : 
 <lao-people-s-democra: 
 <latvia>             : 
 <lebanon>            : 
 <lesotho>            : 
 <liberia>            : 
 <libya>              : 
 <liechtenstein>      : 
 <lithuania>          : 
 <luxembourg>         : 
 <macao>              : 
 <macedonia>          : 
 <madagascar>         : 
 <malawi>             : 
 <malaysia>           : 
 <maldives>           : 
 <mali>               : 
 <malta>              : 
 <marshall-islands>   : 
 <martinique>         : 
 <mauritania>         : 
 <mauritius>          : 
 <mayotte>            : 
 <mexico>             : 
 <micronesia-federated: 
 <moldova-republic>   : 
 <monaco>             : 
 <mongolia>           : 
 <montenegro>         : 
 <montserrat>         : 
 <morocco>            : 
 <mozambique>         : 
 <myanmar>            : 
 <namibia>            : 
 <nauru>              : 
 <nepal>              : 
 <netherlands>        : 
 <new-caledonia>      : 
 <new-zealand>        : 
 <nicaragua>          : 
 <niger>              : 
 <nigeria>            : 
 <niue>               : 
 <norfolk-island>     : 
 <northern-mariana-isl: 
 <norway>             : 
 <oman>               : 
 <pakistan>           : 
 <palau>              : 
 <palestine-state>    : 
 <panama>             : 
 <papua-new-guinea>   : 
 <paraguay>           : 
 <peru>               : 
 <philippines>        : 
 <pitcairn>           : 
 <poland>             : 
 <portugal>           : 
 <puerto-rico>        : 
 <qatar>              : 
 <reunion>            : 
 <romania>            : 
 <russian-federation> : 
 <rwanda>             : 
 <saint-barthelemy>   : 
 <saint-helena-ascensi: 
 <saint-kitts-nevis>  : 
 <saint-lucia>        : 
 <saint-martin>       : 
 <saint-pierre-miquelo: 
 <saint-vincent-grenad: 
 <samoa>              : 
 <san-marino>         : 
 <sao-tome-principe>  : 
 <saudi-arabia>       : 
 <senegal>            : 
 <serbia>             : 
 <seychelles>         : 
 <sierra-leone>       : 
 <singapore>          : 
 <sint-maarten>       : 
 <slovakia>           : 
 <slovenia>           : 
 <solomon-islands>    : 
 <somalia>            : 
 <south-africa>       : 
 <south-georgia-south-: 
 <south-sudan>        : 
 <spain>              : 
 <sri-lanka>          : 
 <sudan>              : 
 <suriname>           : 
 <svalbard-jan-mayen> : 
 <swaziland>          : 
 <sweden>             : 
 <switzerland>        : 
 <syrian-arab-republic: 
 <taiwan>             : 
 <tajikistan>         : 
 <tanzania-united-repu: 
 <thailand>           : 
 <timor-leste>        : 
 <togo>               : 
 <tokelau>            : 
 <tonga>              : 
 <trinidad-tobago>    : 
 <tunisia>            : 
 <turkey>             : 
 <turkmenistan>       : 
 <turks-caicos-islands: 
 <tuvalu>             : 
 <uganda>             : 
 <ukraine>            : 
 <united-arab-emirates: 
 <united-kingdom>     : 
 <united-states>      : 
 <united-states-minor-: 
 <uruguay>            : 
 <uzbekistan>         : 
 <vanuatu>            : 
 <venezuela>          : 
 <viet-nam>           : 
 <virgin-islands-briti: 
 <virgin-islands-us>  : 
 <wallis-futuna>      : 
 <western-sahara>     : 
 <yemen>              : 
 <zambia>             : 
 <zimbabwe>           : 


SF-1p-187>config>port# wifi-country-code
```

### wlan *(not entered — parameterized context)*
```text
<2.4g>               : 
 <5g>                 : 


SF-1p-187>config>port# wlan
```

## configure port ethernet NAME

Level help (`?`):
```text
[no] access-group                   - Bind ACL to Port Ethernet
 [no] classifier                     + Enables/disables classifier at the port 
                                       level
      clear-access-list-statistics   - Clear ACL statistics
      clear-statistics               - Clears all statistics
      dot1x                          + 802.1X level
      egress-mtu                     - Defines the max frame size to transmit
 [no] force-next-hop                 - Map traffic originated by a router 
                                       interface to its egress port
      mac-access-control             + MAC access control
 [no] name                           - Assigns/removes a port name
 [no] pm-collection                  - Enable Performance Management (PM) 
 [no] policy-based-route             - Bind PBR rule to this entity
 [no] queue-group                    - 
 [no] shutdown                       - Administratively disables/enables the 
                                       port
 [no] traffic-class                  + Define a traffic-class entity
 [no] vlan                           + Configure vlan port

 show access-list-statistics         - Show ACL statistics
 show access-list-summary            - ACL Information
 show statistics                     - Displays the Ethernet port statistics
 show status                         - Displays the Ethernet port status
```

### access-group
```text
<acl-name>           : ACL name [1..80 chars]


SF-1p-187>config>port>eth(1)# access-group
```

### classifier *(not entered — parameterized context)*
```text
<ingress>            : 


SF-1p-187>config>port>eth(1)# classifier
```

### clear-access-list-statistics
```text
<CR>
 <in>                 : In
 <ipv4>               : IPv4
 <ipv6>               : IPv6


SF-1p-187>config>port>eth(1)# clear-access-list-statistics
```

### clear-statistics
```text
<CR>

SF-1p-187>config>port>eth(1)# clear-statistics
```

### egress-mtu
```text
<size>               : Specifies the Max Transition Unit size (bytes) [number, 
                        default 1500] [68..12288]


SF-1p-187>config>port>eth(1)# egress-mtu
```

### force-next-hop
```text
<CR>
 next-hop

SF-1p-187>config>port>eth(1)# force-next-hop
```

### name
```text
<string>             : Adds free text to assign a name to the port [1..64 
                        chars]


SF-1p-187>config>port>eth(1)# name
```

### pm-collection
```text
<interval>           : PM collection interval


SF-1p-187>config>port>eth(1)# pm-collection
```

### policy-based-route
```text
priority

SF-1p-187>config>port>eth(1)# policy-based-route
```

### queue-group
```text
profile

SF-1p-187>config>port>eth(1)# queue-group
```

### show access-list-statistics
```text
<CR>
 <in>                 : In
 <ipv4>               : IPv4
 <ipv6>               : IPv6


SF-1p-187>config>port>eth(1)# show access-list-statistics
```

### show access-list-summary
```text
<CR>

SF-1p-187>config>port>eth(1)# show access-list-summary
```

### show statistics
```text
<CR>

SF-1p-187>config>port>eth(1)# show statistics
```

### show status
```text
<CR>

SF-1p-187>config>port>eth(1)# show status
```

### shutdown
```text
<CR>

SF-1p-187>config>port>eth(1)# shutdown
```

### traffic-class *(parameterized — inner help harvested under "configure port ethernet NAME traffic-class NAME")*
```text
<tc-name>            : Traffic class name [1..32 chars]


SF-1p-187>config>port>eth(1)# traffic-class
```

### vlan *(not entered — parameterized context)*
```text
<vlan-id>            : Vlan id [1..4094]


SF-1p-187>config>port>eth(1)# vlan
```

## configure port ethernet NAME dot1x

Level help (`?`):
```text
authenticator                  + Authenticator level
      clear-statistics               - Clear 802.1X statistics
      initialize                     - Initialize 802.1X
      supplicant                     + Supplicant level

 show statistics                     - Display 802.1X statistics
 show status                         - Display 802.1X statistics
```

### clear-statistics
```text
<CR>

SF-1p-187>config>port>eth(1)>dot1x# clear-statistics
```

### initialize
```text
<CR>

SF-1p-187>config>port>eth(1)>dot1x# initialize
```

### show statistics
```text
<CR>

SF-1p-187>config>port>eth(1)>dot1x# show statistics
```

### show status
```text
<CR>

SF-1p-187>config>port>eth(1)>dot1x# show status
```

## configure port ethernet NAME dot1x authenticator

Level help (`?`):
```text
authentication                 - Configure authentication mode
 [no] reauthentication               - Enable periodic reauthentication
 [no] shutdown                       - Disable authenticator functionality
```

### authentication
```text
mode

SF-1p-187>config>port>eth(1)>dot1x>authenticator# authentication
```

### reauthentication
```text
<CR>
 period

SF-1p-187>config>port>eth(1)>dot1x>authenticator# reauthentication
```

### shutdown
```text
<CR>

SF-1p-187>config>port>eth(1)>dot1x>authenticator# shutdown
```

## configure port ethernet NAME dot1x supplicant

Level help (`?`):
```text
[no] authentication                 - Configure authentication parameters
      held-period                    - Configure held period after 
                                       authentication failure
      max-authentication             - Configure max number of authentication 
                                       attempts
 [no] shutdown                       - Disable supplicant functionality
      tx-period                      - Configure time before retransmitting EAP 
                                       frame
```

### authentication
```text
identity

SF-1p-187>config>port>eth(1)>dot1x>supplicant# authentication
```

### held-period
```text
<seconds>            : [0..65535, default 60]


SF-1p-187>config>port>eth(1)>dot1x>supplicant# held-period
```

### max-authentication
```text
<number>             : Max number of authentication attempts [1..65535, default
                         2]


SF-1p-187>config>port>eth(1)>dot1x>supplicant# max-authentication
```

### shutdown
```text
<CR>

SF-1p-187>config>port>eth(1)>dot1x>supplicant# shutdown
```

### tx-period
```text
<seconds>            : [1..65535, default 30]


SF-1p-187>config>port>eth(1)>dot1x>supplicant# tx-period
```

## configure port ethernet NAME mac-access-control

Level help (`?`):
```text
[no] mac                            - Add static MAC address
 [no] shutdown                       -
```

### mac
```text
<mac-address>        : [00-00-00-00-00-00]


SF-1p-187>config>port>eth(1)>mac-access-control# mac
```

### shutdown
```text
<CR>

SF-1p-187>config>port>eth(1)>mac-access-control# shutdown
```

## configure port ethernet NAME traffic-class NAME

Level help (`?`):
```text
cos                            - Define traffic-class CoS by fixed value 
                                       or by attaching CoS profile
 [no] mark                           - Define traffic-class mark action by fixed
                                        value or by attaching marking profile
 [no] shutdown                       - Enable / disable the traffic-class 
                                       activity


SF-1p-187>config>port>eth(1)>traffic-class(zzz-hrvst)$
```

### cos
```text
<fixed>              : 


SF-1p-187>config>port>eth(1)>traffic-class(zzz-hrvst)$ cos
```

### mark
```text
<dscp-fixed>         : 


SF-1p-187>config>port>eth(1)>traffic-class(zzz-hrvst)$ mark
```

### shutdown
```text
<CR>

SF-1p-187>config>port>eth(1)>traffic-class(zzz-hrvst)$ shutdown
```

## configure port ppp NAME

Level help (`?`):
```text
[no] bind                           - 
 [no] chap-hostname                  - CHAP hostname
 [no] chap-password                  - CHAP password
 [no] ipcp-address                   - PPP ipv4 address
 [no] name                           - Port name
 [no] pap-username                   - Configure PAP credentials
      pppoe                          + 
 [no] refuse-chap                    - Refuse CHAP authentication
 [no] refuse-no-auth                 - Refuse no authentication
 [no] refuse-pap                     - Refuse PAP authentication

 show status

SF-1p-187>config>port>ppp(1)$
```

### bind
```text
<ethernet>           : 


SF-1p-187>config>port>ppp(1)$ bind
```

### chap-hostname
```text
<name>               : [1..80 chars]


SF-1p-187>config>port>ppp(1)$ chap-hostname
```

### chap-password
```text
<password>           : [1..80 chars]


SF-1p-187>config>port>ppp(1)$ chap-password
```

### ipcp-address
```text
<ipv4-unicast-address: IPv4 unicast address [0.0.0.0]


SF-1p-187>config>port>ppp(1)$ ipcp-address
```

### name
```text
<string>             : [1..80 chars]


SF-1p-187>config>port>ppp(1)$ name
```

### pap-username
```text
<name>               : [1..80 chars]


SF-1p-187>config>port>ppp(1)$ pap-username
```

### refuse-chap
```text
<CR>

SF-1p-187>config>port>ppp(1)# refuse-chap
```

### refuse-no-auth
```text
<CR>

SF-1p-187>config>port>ppp(1)# refuse-no-auth
```

### refuse-pap
```text
<CR>

SF-1p-187>config>port>ppp(1)# refuse-pap
```

### show status
```text
<CR>

SF-1p-187>config>port>ppp(1)# show status
```

## configure port ppp NAME pppoe

Level help (`?`):
```text
[no] service-name                   - Configure Service-Name

 show status

SF-1p-187>config>port>ppp(1)>pppoe$
```

### service-name
```text
<string>             : [1..80 chars]


SF-1p-187>config>port>ppp(1)>pppoe$ service-name
```

### show status
```text
<CR>

SF-1p-187>config>port>ppp(1)>pppoe$ show status
```

## configure port serial NAME

Level help (`?`):
```text
allowed-latency                - Configure allowed latency
      baud-rate                      - Configure BAUD rate
      bus-idle                       - Configure idle time in bits
      clear-statistics               - Clear statistics
      data-bits                      - Configure number of data bits
      parity                         - Configure parity type
 [no] shutdown                       - Disable port
      stop-bits                      - Configure number of stop bits
 [no] terminal-server                + Terminal server level
 [no] tunnel                         + Tunnel level
      tx-delay                       - Configure Tx delay

 show status                         - Displays the port's status
```

### allowed-latency
```text
milliseconds

SF-1p-187>config>port>serial(1)# allowed-latency
```

### baud-rate
```text
<300>                : 
 <600>                : 
 <1200>               : 
 <2400>               : 
 <4800>               : 
 <9600>               : 
 <19200>              : 
 <38400>              : 
 <57600>              : 
 <115200>             : 


SF-1p-187>config>port>serial(1)# baud-rate
```

### bus-idle
```text
<auto>               : 
 <bits>               : 


SF-1p-187>config>port>serial(1)# bus-idle
```

### clear-statistics
```text
<CR>

SF-1p-187>config>port>serial(1)# clear-statistics
```

### data-bits
```text
<number-of-bits>     : Number of data bits [5..8, default 8]


SF-1p-187>config>port>serial(1)# data-bits
```

### parity
```text
<none>               : 
 <odd>                : 
 <even>               : 


SF-1p-187>config>port>serial(1)# parity
```

### show status
```text
<CR>

SF-1p-187>config>port>serial(1)# show status
```

### shutdown
```text
<CR>

SF-1p-187>config>port>serial(1)# shutdown
```

### stop-bits
```text
<number-of-bits>     : Number of stop bits [1..2, default 1]


SF-1p-187>config>port>serial(1)# stop-bits
```

### terminal-server *(parameterized — inner help harvested under "configure port serial NAME terminal-server NAME")*
```text
<number>             : Terminal server number [number]


SF-1p-187>config>port>serial(1)# terminal-server
```

### tunnel *(parameterized — inner help harvested under "configure port serial NAME tunnel NAME")*
```text
<service-id>         : Service ID [1..10]


SF-1p-187>config>port>serial(1)# tunnel
```

### tx-delay
```text
<milliseconds>       : Tx delay, in milliseconds [1..10000]


SF-1p-187>config>port>serial(1)# tx-delay
```

## configure port serial NAME terminal-server NAME

Level help (`?`):
```text
disconnect                     - Disconnect session
 [no] local-address                  - Configure device IP address to listen on
 [no] telnet-client-tcp              - Configure telnet client on TCP ports
 [no] telnet-server-tcp              - Configure telnet server on TCP ports
 [no] telnet-server-udp              - Configure telnet server on UDP ports

 show status                         - Display status
```

### disconnect
```text
port

SF-1p-187>config>port>serial(1)>terminal-server(10)# disconnect
```

### local-address
```text
<ipv4-or-ipv6-address: Device IP address to listen on [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>port>serial(1)>terminal-server(10)# local-address
```

### show status
```text
<CR>

SF-1p-187>config>port>serial(1)>terminal-server(10)# show status
```

### telnet-client-tcp
```text
server-address

SF-1p-187>config>port>serial(1)>terminal-server(10)# telnet-client-tcp
```

### telnet-server-tcp
```text
port

SF-1p-187>config>port>serial(1)>terminal-server(10)# telnet-server-tcp
```

### telnet-server-udp
```text
port

SF-1p-187>config>port>serial(1)>terminal-server(10)# telnet-server-udp
```

## configure port serial NAME tunnel NAME

Level help (`?`):
```text
[no] address                        - Configure tunnel addresses
 [no] shutdown                       - Disable serial tunnel
      transport-layer                - Configure transport layer
```

### address
```text
local

SF-1p-187>config>port>serial(1)>tunnel(10)# address
```

### shutdown
```text
<CR>

SF-1p-187>config>port>serial(1)>tunnel(10)# shutdown
```

### transport-layer
```text
<tcp>                : TCP
 <udp>                : UDP


SF-1p-187>config>port>serial(1)>tunnel(10)# transport-layer
```

## configure port virtual NAME

Level help (`?`):
```text
clear-statistics               - Clear port statistics
      egress-mtu                     - Defines the max frame size to transmit
 [no] force-next-hop                 - Map traffic originated by a router 
                                       interface to its egress port
 [no] name                           - Assigns/removes a port name
 [no] policy-based-route             - Bind PBR rule to this entity
 [no] shutdown                       - Administratively disables/enables the 
                                       port
 [no] vlan                           + Configure vlan port

 show statistics                     - Displays the Virtual port statistics
 show status                         - Displays the Virtual port status
```

### clear-statistics
```text
<CR>

SF-1p-187>config>port>virtual(1)# clear-statistics
```

### egress-mtu
```text
<size>               : Specifies the Max Transition Unit size (bytes) [number, 
                        default 1500] [68..12288]


SF-1p-187>config>port>virtual(1)# egress-mtu
```

### force-next-hop
```text
<CR>
 next-hop

SF-1p-187>config>port>virtual(1)# force-next-hop
```

### name
```text
<string>             : Adds free text to assign a name to the port [0..64 
                        chars]


SF-1p-187>config>port>virtual(1)# name
```

### policy-based-route
```text
priority

SF-1p-187>config>port>virtual(1)# policy-based-route
```

### show statistics
```text
<CR>

SF-1p-187>config>port>virtual(1)# show statistics
```

### show status
```text
<CR>

SF-1p-187>config>port>virtual(1)# show status
```

### shutdown
```text
<CR>

SF-1p-187>config>port>virtual(1)# shutdown
```

### vlan *(not entered — parameterized context)*
```text
<vlan-id>            : Vlan id [1..4094]


SF-1p-187>config>port>virtual(1)# vlan
```

## configure port wifi-client

Level help (`?`):
```text
connection-method              - Configure first SSID to connect
      dot1x                          + 802.1X level
 [no] shutdown                       - Disable client
 [no] ssid                           + SSID level

 show networks
 show status                         - Display client status
```

### connection-method
```text
<last>               : 
 <best>               : 
 <priority>           : 


SF-1p-187>config>port>wifi-client# connection-method
```

### show networks
```text
<CR>

SF-1p-187>config>port>wifi-client# show networks
```

### show status
```text
<CR>

SF-1p-187>config>port>wifi-client# show status
```

### shutdown
```text
<CR>

SF-1p-187>config>port>wifi-client# shutdown
```

### ssid *(parameterized — inner help harvested under "configure port wifi-client ssid NAME")*
```text
<name>               : SSID [1..32 chars]


SF-1p-187>config>port>wifi-client# ssid
```

## configure port wifi-client dot1x

Level help (`?`):
```text
clear-statistics               - Clear 802.1X statistics
      initialize                     - Initialize 802.1X
      supplicant                     + Supplicant level

 show statistics                     - Display 802.1X statistics
 show status                         - Display 802.1X statistics
```

### clear-statistics
```text
<CR>

SF-1p-187>config>port>wifi-client>dot1x# clear-statistics
```

### initialize
```text
<CR>

SF-1p-187>config>port>wifi-client>dot1x# initialize
```

### show statistics
```text
<CR>

SF-1p-187>config>port>wifi-client>dot1x# show statistics
```

### show status
```text
<CR>

SF-1p-187>config>port>wifi-client>dot1x# show status
```

## configure port wifi-client dot1x supplicant

Level help (`?`):
```text
[no] authentication                 - Configure authentication parameters
      held-period                    - Configure held period after 
                                       authentication failure
      max-authentication             - Configure max number of authentication 
                                       attempts
 [no] shutdown                       - Disable supplicant functionality
      tx-period                      - Configure time before retransmitting EAP 
                                       frame
```

### authentication
```text
identity

SF-1p-187>config>port>wifi-client>dot1x>supplicant# authentication
```

### held-period
```text
<seconds>            : [0..65535, default 60]


SF-1p-187>config>port>wifi-client>dot1x>supplicant# held-period
```

### max-authentication
```text
<number>             : Max number of authentication attempts [1..65535, default
                         2]


SF-1p-187>config>port>wifi-client>dot1x>supplicant# max-authentication
```

### shutdown
```text
<CR>

SF-1p-187>config>port>wifi-client>dot1x>supplicant# shutdown
```

### tx-period
```text
<seconds>            : [1..65535, default 30]


SF-1p-187>config>port>wifi-client>dot1x>supplicant# tx-period
```

## configure port wifi-client ssid NAME

Level help (`?`):
```text
[no] password                       - Configure password
      priority                       - Configure priority, to determine 
                                       connecting order
      security                       - Configure security method
 [no] shutdown                       - Disable SSID


SF-1p-187>config>port>wifi-client>ssid(zzz-hrvst)$
```

### password
```text
<key-string>         : [1..32 chars]


SF-1p-187>config>port>wifi-client>ssid(zzz-hrvst)$ password
```

### priority
```text
<number>             : [1..254, default 100]


SF-1p-187>config>port>wifi-client>ssid(zzz-hrvst)$ priority
```

### security
```text
<none>               : 
 <wpa2-psk>           : 
 <wpa2-dot1x>         : 


SF-1p-187>config>port>wifi-client>ssid(zzz-hrvst)$ security
```

### shutdown
```text
<CR>

SF-1p-187>config>port>wifi-client>ssid(zzz-hrvst)$ shutdown
```

## configure protection

Level help (`?`):
```text
[no] erp                            + ERP level
```

### erp *(parameterized — inner help harvested under "configure protection erp NAME")*
```text
<number>             : Ring ID [1..239, default Index, no default]


SF-1p-187>config>protection# erp
```

## configure protection erp NAME

Level help (`?`):
```text
[no] bridge                         - Associate ring with bridge
 [no] data-vlan                      - Configure data VLANs
 [no] description                    - Configure ring description
 [no] east-port                      - Configure east bridge port
 [no] port-description               - Configure port description
      port-type                      - Configure east or west port role
 [no] r-aps                          - Configure R-APS properties
 [no] sf-trigger                     - Configure SF trigger on east or west port
 [no] shutdown                       - Disable ring
 [no] west-port                      - Configure west bridge port

 show status                         - Display ring status
```

### bridge
```text
<number>             : ID of the bridge the ring is on [1..1]


SF-1p-187>config>protection>erp(1)# bridge
```

### data-vlan
```text
<data-vlan>          : [1..4094]


SF-1p-187>config>protection>erp(1)# data-vlan
```

### description
```text
<string>             : Configure ring description [1..64 chars]


SF-1p-187>config>protection>erp(1)# description
```

### east-port
```text
<bridge-port-number> : Bridge port to be the ring east port [number] [1..64]


SF-1p-187>config>protection>erp(1)# east-port
```

### port-description
```text
<east>               : 
 <west>               : 


SF-1p-187>config>protection>erp(1)# port-description
```

### port-type
```text
<east>               : 
 <west>               : 


SF-1p-187>config>protection>erp(1)# port-type
```

### r-aps
```text
vlan

SF-1p-187>config>protection>erp(1)# r-aps
```

### sf-trigger
```text
<east>               : 
 <west>               : 


SF-1p-187>config>protection>erp(1)# sf-trigger
```

### show status
```text
<CR>

SF-1p-187>config>protection>erp(1)# show status
```

### shutdown
```text
<CR>

SF-1p-187>config>protection>erp(1)# shutdown
```

### west-port
```text
<bridge-port-number> : Bridge port to be the ring west port [number] [1..64]


SF-1p-187>config>protection>erp(1)# west-port
```

## configure qos

Level help (`?`):
```text
[no] queue-block-profile            + Queue block profile configuration
 [no] queue-group-profile            + Queue group profile configuration
 [no] shaper-profile                 + Shaper profile configuration
```

### queue-block-profile *(parameterized — inner help harvested under "configure qos queue-block-profile NAME")*
```text
<profile-name>       : [1..32 chars]


SF-1p-187>config>qos# queue-block-profile
```

### queue-group-profile *(parameterized — inner help harvested under "configure qos queue-group-profile NAME")*
```text
<profile-name>       : [1..32 chars]


SF-1p-187>config>qos# queue-group-profile
```

### shaper-profile *(parameterized — inner help harvested under "configure qos shaper-profile NAME")*
```text
<profile-name>       : [1..32 chars]


SF-1p-187>config>qos# shaper-profile
```

## configure qos queue-block-profile NAME

Level help (`?`):
```text
queue                          + Define queue parameters in queue block


SF-1p-187>config>qos>queue-block-profile(zzz-hrvst)$
```

## configure qos queue-block-profile NAME queue

Level help (`?`):
```text
queue                          + Define queue parameters in queue block
```

### bandwidth
```text
# cli error: Invalid Command
SF-1p-187>config>qos>queue-block-profile(zzz-hrvst)# bandwidth
```

### scheduling
```text
# cli error: Invalid Command
SF-1p-187>config>qos>queue-block-profile(zzz-hrvst)# scheduling
```

## configure qos queue-group-profile NAME

Level help (`?`):
```text
queue-block                    + Define queue blocks in queue group 
                                       structure


SF-1p-187>config>qos>queue-group-profile(zzz-hrvst)$
```

## configure qos queue-group-profile NAME queue-block

Level help (`?`):
```text
queue-block                    + Define queue blocks in queue group 
                                       structure
```

### profile
```text
# cli error: Invalid Command
SF-1p-187>config>qos>queue-group-profile(zzz-hrvst)# profile
```

### shaper
```text
# cli error: Invalid Command
SF-1p-187>config>qos>queue-group-profile(zzz-hrvst)# shaper
```

## configure qos shaper-profile NAME

Level help (`?`):
```text
bandwidth                      - Bandwidth profile configuration


SF-1p-187>config>qos>shaper-profile(zzz-hrvst)$
```

### bandwidth
```text
<CR>
 cir

SF-1p-187>config>qos>shaper-profile(zzz-hrvst)$ bandwidth
```

## configure reporting

Level help (`?`):
```text
acknowledge                    - 
      active-alarm-rebuild           - 
      alarm-cut-off                  - 
      alarm-input                    - 
      alarm-output                   - 
 [no] alarm-source-attribute         - 
 [no] alarm-source-type-attribute    - 
 [no] bind-alarm-source-to-relay     - 
 [no] bind-alarm-to-relay            - 
      clear-accounting-log           - Clear Syslog local accounting log
      clear-alarm-log                - 
      log-file-timestamp-type        - Configure log file timestamp type
 [no] mask-minimum-severity          - 
 [no] pm                             - Globally enable PM collection
 [no] pm-collection                  - Enable PM collection on entity type
      soaking-time                   - 

 show accounting-log                 - Dispay Syslog local accounting log
 show active-alarms
 show active-alarms-details
 show alarm-information
 show alarm-input
 show alarm-list
 show alarm-log
 show alarm-outputs
 show brief-alarm-log
 show brief-log
 show event-information
 show event-list
 show log
 show log-summary
```

### acknowledge
```text
<log>                : 
 <brief-log>          : 
 <activity-log>       : 
 <all-logs>           : 


SF-1p-187>config>reporting# acknowledge
```

### active-alarm-rebuild
```text
<CR>

 send-traps

SF-1p-187>config>reporting# active-alarm-rebuild
```

### alarm-cut-off
```text
<port>               : 


SF-1p-187>config>reporting# alarm-cut-off
```

### alarm-input
```text
<port-number>        : [number]


SF-1p-187>config>reporting# alarm-input
```

### alarm-output
```text
<port>               : 


SF-1p-187>config>reporting# alarm-output
```

### alarm-source-attribute
```text
<system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# alarm-source-attribute
```

### alarm-source-type-attribute
```text
<system>             : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <gnss>               : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# alarm-source-type-attribute
```

### bind-alarm-source-to-relay
```text
<system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# bind-alarm-source-to-relay
```

### bind-alarm-to-relay
```text
<system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# bind-alarm-to-relay
```

### clear-accounting-log
```text
<CR>

SF-1p-187>config>reporting# clear-accounting-log
```

### clear-alarm-log
```text
<log>                : 
 <brief-log>          : 
 <activity-log>       : 
 <all-logs>           : 


SF-1p-187>config>reporting# clear-alarm-log
```

### log-file-timestamp-type
```text
<utc>                : 
 <local>              : 


SF-1p-187>config>reporting# log-file-timestamp-type
```

### mask-minimum-severity
```text
<CR>
 log
 snmp-trap
 led-relay
 popup
 vty-popup
 netconf-notification

SF-1p-187>config>reporting# mask-minimum-severity
```

### pm
```text
<CR>

SF-1p-187>config>reporting# pm
```

### pm-collection
```text
<cellular>           : Cellular
 <eth>                : Ethernet
 <eth-vlan>           : Ethernet Vlan
 <sd-iot-tunnel>      : Sd Iot Tunnel
 <system>             : Memory usage and CPU utilization
 <tunnel-interface>   : Tunnel interface


SF-1p-187>config>reporting# pm-collection
```

### show accounting-log
```text
<CR>

SF-1p-187>config>reporting# show accounting-log
```

### show active-alarms
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <all>                : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# show active-alarms
```

### show active-alarms-details
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <all>                : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# show active-alarms-details
```

### show alarm-information
```text
<system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# show alarm-information
```

### show alarm-input
```text
<CR>

SF-1p-187>config>reporting# show alarm-input
```

### show alarm-list
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 
 <all>                : 


SF-1p-187>config>reporting# show alarm-list
```

### show alarm-log
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <all>                : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# show alarm-log
```

### show alarm-outputs
```text
<CR>

SF-1p-187>config>reporting# show alarm-outputs
```

### show brief-alarm-log
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <all>                : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# show brief-alarm-log
```

### show brief-log
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <all>                : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# show brief-log
```

### show event-information
```text
<system>             : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# show event-information
```

### show event-list
```text
<CR>
 <system>             : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <all>                : 
 <tunnel>             : 


SF-1p-187>config>reporting# show event-list
```

### show log
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <access-point>       : 
 <wifi-client>        : 
 <bridge>             : 
 <bridge-port>        : 
 <erp>                : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <ip-bfd>             : 
 <cellular>           : 
 <alarm-input>        : 
 <all>                : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <vrrp-group>         : 
 <tunnel>             : 


SF-1p-187>config>reporting# show log
```

### show log-summary
```text
<CR>
 <number-records>     : [number, default 10]


SF-1p-187>config>reporting# show log-summary
```

### soaking-time
```text
<CR>
 interval
 clear

SF-1p-187>config>reporting# soaking-time
```

## configure router NAME

Level help (`?`):
```text
[no] bfd-neighbor                   + Configure BFD neighbor
 [no] bgp                            + Configure BGP
      clear-arp-table                - Clear ARP table
      clear-bfd-statistics           - Clear BFD statistics
      clear-neighbor-table           - Clear neighbor table
      dhcp-client                    + Configure DHCP client
 [no] dhcp-relay-server              - DHCP relay server address
 [no] dns-name-server                - 
 [no] interface                      + Configure router interface
 [no] name                           - Configure router name
 [no] nat                            + Enable/disable-delete NAT configuration
 [no] ospf                           + Configure OSPF
 [no] prefix-list                    + create and delete prefix-list policy 
                                       profile entity per router entity
      resequence                     - Resequence policy profile
 [no] route-map                      + Command to create and delete route-map 
                                       policy profile entity per router entity.
 [no] static-route                   - Configure static route
 [no] tunnel-interface               + Configure tunnel interface

 show arp-table                      - Show ARP table
 show bfd-neighbors                  - Display BFD neighbors
 show bfd-neighbors-details          - Display BFD neighbors
 show dns-resolver
 show ip-monitoring-summary          - Display ip-monitoring entities status
 show neighbor-table                 - Show IPv6 neighbor table
 show rib
 show routing-table                  - Show routing table
 show summary-interface              - Show interface table
 show vrrp-summary
```

### bfd-neighbor *(not entered — parameterized context)*
```text
<ip-address>         : Neighbor IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)# bfd-neighbor
```

### bgp *(parameterized — inner help harvested under "configure router NAME bgp NAME")*
```text
<as-number>          : Set local AS [1..4294967295, default 0]


SF-1p-187>config>router(1)# bgp
```

### clear-arp-table
```text
<CR>

SF-1p-187>config>router(1)# clear-arp-table
```

### clear-bfd-statistics
```text
<ip-address>         : Neighbor IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)# clear-bfd-statistics
```

### clear-neighbor-table
```text
<CR>

SF-1p-187>config>router(1)# clear-neighbor-table
```

### dhcp-relay-server
```text
<address>            : DHCP relay server address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)# dhcp-relay-server
```

### interface *(parameterized — inner help harvested under "configure router NAME interface NAME")*
```text
<number>             : Router interface number [number] [1..32]


SF-1p-187>config>router(1)# interface
```

### name
```text
<string>             : Router name [1..32 chars]


SF-1p-187>config>router(1)# name
```

### prefix-list *(not entered — parameterized context)*
```text
<name>               : Set prefix-list policy profile name. Profile name shall 
                        be unique in the system [1..252 chars]


SF-1p-187>config>router(1)# prefix-list

auto-create probe 'prefix-list zzz-hrvst' refused.
device response: prefix-list zzz-hrvst
#                                                 ^
# cli error: parameter or keyword missing or wrong
 - prefix-list <name> {ipv4|ipv6}
 - no prefix-list <name>
 <name>               : Set prefix-list policy profile name. Profile name shall 
                        be unique in the system [1..252 chars]

SF-1p-187>config>router(1)#
```

### resequence
```text
<name>               : Policy profile to resequence [1..252 chars]


SF-1p-187>config>router(1)# resequence
```

### route-map *(parameterized — inner help harvested under "configure router NAME route-map NAME")*
```text
<name>               : Set route-map policy profile name. Profile name shall be
                         unique in the system. [1..252 chars]


SF-1p-187>config>router(1)# route-map
```

### show arp-table
```text
<CR>
 address

SF-1p-187>config>router(1)# show arp-table
```

### show bfd-neighbors
```text
<CR>

SF-1p-187>config>router(1)# show bfd-neighbors
```

### show bfd-neighbors-details
```text
<CR>

SF-1p-187>config>router(1)# show bfd-neighbors-details
```

### show dns-resolver
```text
<CR>

SF-1p-187>config>router(1)# show dns-resolver
```

### show ip-monitoring-summary
```text
<CR>

SF-1p-187>config>router(1)# show ip-monitoring-summary
```

### show neighbor-table
```text
<CR>
 address

SF-1p-187>config>router(1)# show neighbor-table
```

### show rib
```text
<ipv4>               : 
 <ipv6>               : 


SF-1p-187>config>router(1)# show rib
```

### show routing-table
```text
<CR>
 address
 protocol

SF-1p-187>config>router(1)# show routing-table
```

### show summary-interface
```text
<CR>

SF-1p-187>config>router(1)# show summary-interface
```

### show vrrp-summary
```text
<CR>

SF-1p-187>config>router(1)# show vrrp-summary
```

### static-route
```text
<address-mask>       : IP and mask [0.0.0.0/32|0:0:0:0::0/128]


SF-1p-187>config>router(1)# static-route
```

### tunnel-interface *(parameterized — inner help harvested under "configure router NAME tunnel-interface NAME")*
```text
<number>             : Tunnel number [number] [1..30]


SF-1p-187>config>router(1)# tunnel-interface
```

## configure router NAME bgp NAME

Level help (`?`):
```text
clear-neighbor                 - Restart BGP session
      ipv4-unicast-af                + Configure IPv4 unicast AF
      ipv6-unicast-af                + Configure IPv6 unicast AF
 [no] neighbor                       + Configure BGP neighbor
      router-id                      - Configure router identifier
 [no] shutdown                       - Disable BGP

 show community
 show rib
 show summary
```

### clear-neighbor
```text
<ip-address>         : Neighbor IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)>bgp(65002)# clear-neighbor
```

### neighbor *(parameterized — inner help harvested under "configure router NAME bgp NAME neighbor NAME")*
```text
<ip-address>         : Neighbor IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)>bgp(65002)# neighbor
```

### router-id
```text
<ip-address>         : Router ID (IP address format) [0.0.0.0]


SF-1p-187>config>router(1)>bgp(65002)# router-id
```

### show community
```text
<ipv4>               : 
 <ipv6>               : 


SF-1p-187>config>router(1)>bgp(65002)# show community
```

### show rib
```text
<ipv4>               : 
 <ipv6>               : 


SF-1p-187>config>router(1)>bgp(65002)# show rib
```

### show summary
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)# show summary
```

### shutdown
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)# shutdown
```

## configure router NAME bgp NAME ipv4-unicast-af

Level help (`?`):
```text
external-preference            - Configure external BGP route priority
      internal-preference            - Configure internal BGP route priority
      neighbor                       + Configure BGP neighbor
 [no] network                        - Configure BGP network
 [no] redistribute                   - Redistribute routes
```

### external-preference
```text
<priority>           : BGP route priority [1..255, default 20]


SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af# external-preference
```

### internal-preference
```text
<priority>           : BGP route priority [1..255, default 200]


SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af# internal-preference
```

### neighbor *(parameterized — inner help harvested under "configure router NAME bgp NAME ipv4-unicast-af neighbor NAME")*
```text
<ip-address>         : Neighbor IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af# neighbor
```

### network
```text
<prefix>             : Network prefix length [0.0.0.0/32]


SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af# network
```

### redistribute
```text
<connected>          : Connected
 <static>             : Static
 <ospf>               : OSPF


SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af# redistribute
```

## configure router NAME bgp NAME ipv4-unicast-af neighbor NAME

Level help (`?`):
```text
[no] active                         - Activate neighbor
 [no] prefix-list-bind               - 
 [no] route-map-bind                 - 

 show advertised-route               - Show advertised routes
 show prefix-list
 show received-route                 - Show received routes
 show route-map
```

### active
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af>neighbor(10.10.10.188)# active
```

### prefix-list-bind
```text
<name>               : [1..252 chars]


SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af>neighbor(10.10.10.188)# prefix-list-bind
```

### route-map-bind
```text
<name>               : [1..252 chars]


SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af>neighbor(10.10.10.188)# route-map-bind
```

### show advertised-route
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af>neighbor(10.10.10.188)# show advertised-route
```

### show prefix-list
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af>neighbor(10.10.10.188)# show prefix-list
```

### show received-route
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af>neighbor(10.10.10.188)# show received-route
```

### show route-map
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv4-unicast-af>neighbor(10.10.10.188)# show route-map
```

## configure router NAME bgp NAME ipv6-unicast-af

Level help (`?`):
```text
external-preference            - Configure external BGP route priority
      internal-preference            - Configure internal BGP route priority
      neighbor                       + Configure BGP neighbor
 [no] network                        - Configure BGP network
 [no] redistribute                   - Redistribute routes
```

### external-preference
```text
<priority>           : BGP route priority [1..255, default 20]


SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af# external-preference
```

### internal-preference
```text
<priority>           : BGP route priority [1..255, default 200]


SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af# internal-preference
```

### neighbor *(parameterized — inner help harvested under "configure router NAME bgp NAME ipv6-unicast-af neighbor NAME")*
```text
<ip-address>         : Neighbor IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af# neighbor
```

### network
```text
<prefix>             : Network prefix length [0.0.0.0/32|0:0:0:0::0/128]


SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af# network
```

### redistribute
```text
<connected>          : Connected
 <static>             : Static


SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af# redistribute
```

## configure router NAME bgp NAME ipv6-unicast-af neighbor NAME

Level help (`?`):
```text
[no] active                         - Activate neighbor
 [no] prefix-list-bind               - 
 [no] route-map-bind                 - 

 show advertised-route               - Show advertised routes
 show prefix-list
 show received-route                 - Show received routes
 show route-map
```

### active
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af>neighbor(10.10.10.188)# active
```

### prefix-list-bind
```text
<name>               : [1..252 chars]


SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af>neighbor(10.10.10.188)# prefix-list-bind
```

### route-map-bind
```text
<name>               : [1..252 chars]


SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af>neighbor(10.10.10.188)# route-map-bind
```

### show advertised-route
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af>neighbor(10.10.10.188)# show advertised-route
```

### show prefix-list
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af>neighbor(10.10.10.188)# show prefix-list
```

### show received-route
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af>neighbor(10.10.10.188)# show received-route
```

### show route-map
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>ipv6-unicast-af>neighbor(10.10.10.188)# show route-map
```

## configure router NAME bgp NAME neighbor NAME

Level help (`?`):
```text
[no] allowas-in                     - Accept as-path with my AS present in it
 [no] as-override                    - Override ASNs in outbound updates if 
                                       aspath equals remote-as
 [no] bfd                            - Enable IP-BFD
      connect-timer                  - Configure BGP connect timer
 [no] ebgp-multihop                  - Allow EBGP neighbors not on directly 
                                       connected networks
 [no] local-address                  - Configure local address
      max-prefixes                   - Configure maximum prefixes
 [no] next-hop-self                  - Disable the next hop calculation for this
                                        neighbor
 [no] password                       - Configure password
      remote-as                      - Configure remote AS
 [no] shutdown                       - Disable neighbor
      timers                         - Configure BGP timers

 show neighbor-connection            - Show neighbor connection
```

### allowas-in
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# allowas-in
```

### as-override
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# as-override
```

### bfd
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# bfd
```

### connect-timer
```text
<connect-time>       : BGP connect timer [1..65535, default 120]


SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# connect-timer
```

### ebgp-multihop
```text
<CR>
 <hop-number>         : Hop number [1..255, default 255]


SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# ebgp-multihop
```

### local-address
```text
<ip-address>         : Neighbor local IP address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# local-address
```

### max-prefixes
```text
<number>             : Maximum prefixes [0..2147483647 , default 0]


SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# max-prefixes
```

### next-hop-self
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# next-hop-self
```

### password
```text
<string>             : Password [0..80 chars]


SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# password
```

### remote-as
```text
<as-number>          : Remote AS number [1..4294967295]


SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# remote-as
```

### show neighbor-connection
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# show neighbor-connection
```

### shutdown
```text
<CR>

SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# shutdown
```

### timers
```text
<CR>
 keepalive
 holdtime

SF-1p-187>config>router(1)>bgp(65002)>neighbor(10.10.10.188)# timers
```

## configure router NAME dhcp-client

Level help (`?`):
```text
[no] dhcpv6-option-request          - Configure DHCPv6 option request option
      duid-type                      - 
 [no] host-name                      - Configure DHCP option 12 (host name)
      vendor-class-id                - Configure DHCP option 60 (vendor class 
                                       identifier)
```

### dhcpv6-option-request
```text
<CR>
 <vendor-specific-info: Vendor Specific Information (option 17)


SF-1p-187>config>router(1)>dhcp-client# dhcpv6-option-request
```

### duid-type
```text
<en>                 : 
 <ll>                 : 


SF-1p-187>config>router(1)>dhcp-client# duid-type
```

### host-name
```text
<name>               : User specified name
 <sys-name>           : System defined name


SF-1p-187>config>router(1)>dhcp-client# host-name
```

### vendor-class-id
```text
<name>               : User specified name
 <ent-physical-name>  : System defined name


SF-1p-187>config>router(1)>dhcp-client# vendor-class-id
```

## configure router NAME interface NAME

Level help (`?`):
```text
[no] address                        - Configure router interface IP
 [no] bind                           - Bind router interface
 [no] crypto-map                     - 
 [no] dhcp                           - Enable DHCP client
      dhcp-client                    + Configure DHCP client
 [no] dhcp-relay                     - Enable DHCP relay
 [no] dhcpv6-client                  - Enable DHCPv6 client
 [no] dhcpv6-relay                   - Enable DHCPv6 layer 3 relay
 [no] dhcpv6-server                  - 
 [no] ip-forwarding                  - Enable/disable IP forwarding
 [no] ipv6-address-prefix            - 
 [no] ipv6-autoconfig                - Enable IPv6 autoconfiguration
 [no] management-access              - Configure managment access
 [no] name                           - Configure router interface name
 [no] ospf                           + Configure OSPF
 [no] router-advertisement           - Enables/disables IPv6 Router 
                                       Advertisements
 [no] shutdown                       - Disable router interface
 [no] unreachables                   - Enable ICMP unreachables
 [no] vrrp                           + Define VRRP group

 show crypto-map-status
 show status                         - Show router interface status
 show summary-vrrp
```

### address
```text
<address-mask>       : Router interface IP and mask [0.0.0.0/32|0:0:0:0::0/128]


SF-1p-187>config>router(1)>interface(1)# address
```

### bind
```text
<ppp>                : PPP
 <ethernet>           : Ethernet
 <virtual>            : Virtual
 <cellular>           : Cellular
 <wlan>               : Wlan
 <wifi-client>        : Wifi client


SF-1p-187>config>router(1)>interface(1)# bind
```

### crypto-map
```text
<name>               : [1..80 chars]


SF-1p-187>config>router(1)>interface(1)# crypto-map
```

### dhcp
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# dhcp
```

### dhcp-relay
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# dhcp-relay
```

### dhcpv6-client
```text
<CR>
 pd-name
 <rapid-commit>       : 


SF-1p-187>config>router(1)>interface(1)# dhcpv6-client
```

### dhcpv6-relay
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# dhcpv6-relay
```

### dhcpv6-server
```text
<pool>               : 


SF-1p-187>config>router(1)>interface(1)# dhcpv6-server
```

### ip-forwarding
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# ip-forwarding
```

### ipv6-address-prefix
```text
<prefix-name>        : [1..80 chars]


SF-1p-187>config>router(1)>interface(1)# ipv6-address-prefix
```

### ipv6-autoconfig
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# ipv6-autoconfig
```

### management-access
```text
<allow-all>          : Allow all
 <allow-ping>         : Ping only


SF-1p-187>config>router(1)>interface(1)# management-access
```

### name
```text
<string>             : Router interface name [1..32 chars]


SF-1p-187>config>router(1)>interface(1)# name
```

### router-advertisement
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# router-advertisement
```

### show crypto-map-status
```text
<CR>
 <name>               : [1..80 chars]


SF-1p-187>config>router(1)>interface(1)# show crypto-map-status
```

### show status
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# show status
```

### show summary-vrrp
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# show summary-vrrp
```

### shutdown
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# shutdown
```

### unreachables
```text
<CR>

SF-1p-187>config>router(1)>interface(1)# unreachables
```

### vrrp *(not entered — parameterized context)*
```text
<vrid>               : [1..255]


SF-1p-187>config>router(1)>interface(1)# vrrp
```

## configure router NAME interface NAME dhcp-client

Level help (`?`):
```text
client-id                      - Configure DHCP option 61 (client 
                                       identifier)
```

### client-id
```text
<id>                 : User defined string
 <mac>                : Device MAC address


SF-1p-187>config>router(1)>interface(1)>dhcp-client# client-id
```

## configure router NAME interface NAME ospf

Level help (`?`):
```text
area                           - Set area
      authentication-key             - Configure authentication key
 [no] authentication-type            - Configure authentication type
      dead-interval                  - Configure dead interval
      hello-interval                 - Configure hello interval
      metric                         - Configure metric
 [no] passive                        - Suppress hello packets
      priority                       - Configure interface priority
      retransmit-interval            - Configure retransmit interval
 [no] shutdown                       - Disable OSPF
      transit-delay                  - Configure transit delay
```

### area
```text
<area-id>            : Area ID [0.0.0.0]


SF-1p-187>config>router(1)>interface(1)>ospf# area
```

### authentication-key
```text
<key>                : Key [0..22 chars]


SF-1p-187>config>router(1)>interface(1)>ospf# authentication-key
```

### authentication-type
```text
<simple-password>    : Simple password


SF-1p-187>config>router(1)>interface(1)>ospf# authentication-type
```

### dead-interval
```text
<seconds>            : Dead interval (seconds) [1..2147483647, default 40]


SF-1p-187>config>router(1)>interface(1)>ospf# dead-interval
```

### hello-interval
```text
<seconds>            : Hello interval (seconds) [1..65535, default 10]


SF-1p-187>config>router(1)>interface(1)>ospf# hello-interval
```

### metric
```text
<value>              : Metric [1..65535, default 1]


SF-1p-187>config>router(1)>interface(1)>ospf# metric
```

### passive
```text
<CR>

SF-1p-187>config>router(1)>interface(1)>ospf# passive
```

### priority
```text
<priority>           : Interface priority [0..255, default 1]


SF-1p-187>config>router(1)>interface(1)>ospf# priority
```

### retransmit-interval
```text
<seconds>            : Retransmit interval (seconds) [0..3600, default 5]


SF-1p-187>config>router(1)>interface(1)>ospf# retransmit-interval
```

### shutdown
```text
<CR>

SF-1p-187>config>router(1)>interface(1)>ospf# shutdown
```

### transit-delay
```text
<seconds>            : Transit delay (seconds) [0..3600, default 1]


SF-1p-187>config>router(1)>interface(1)>ospf# transit-delay
```

## configure router NAME nat

Level help (`?`):
```text
clear-nat-statistics           - Clears NAT statistics counters
      clear-nat-translations         - Clears NAT translation table
 [no] nat-exclude-source-ip          - Configure NAT exclude expression
 [no] nat-inside-overload            - Configure a NAPT rule inside to outside
 [no] nat-inside-source-static       - Configure NAT rule inside to outside
 [no] nat-inside-source-static-port  - Configure/modify/delete NAT rule from the
                                        inside to outside
      nat-timeout                    - Configure translation table entries 
                                       timeout

 show nat-translations               - Display NAT translation table
```

### clear-nat-statistics
```text
<CR>

SF-1p-187>config>router(1)>nat# clear-nat-statistics
```

### clear-nat-translations
```text
<CR>

SF-1p-187>config>router(1)>nat# clear-nat-translations
```

### nat-exclude-source-ip
```text
<source-ip>          : IP Address of source IP station [0.0.0.0]


SF-1p-187>config>router(1)>nat# nat-exclude-source-ip
```

### nat-inside-overload
```text
source

SF-1p-187>config>router(1)>nat# nat-inside-overload
```

### nat-inside-source-static
```text
<inside-ip>          : IP Address of Inside IP station [0.0.0.0]


SF-1p-187>config>router(1)>nat# nat-inside-source-static
```

### nat-inside-source-static-port
```text
<tcp>                : Indicate that the configured port number is associated 
                        with TCP
 <udp>                : Indicate that the configured port number is associated 
                        with UDP


SF-1p-187>config>router(1)>nat# nat-inside-source-static-port
```

### nat-timeout
```text
<CR>
 tcp
 udp
 others

SF-1p-187>config>router(1)>nat# nat-timeout
```

### show nat-translations
```text
<CR>

SF-1p-187>config>router(1)>nat# show nat-translations
```

## configure router NAME ospf

Level help (`?`):
```text
[no] area                           + Configure OSPF area 
      external-preference            - Set OSPF external route priority 
      internal-preference            - Set OSPF internal route priority 
 [no] redistribute                   - Redistribute external routes
      router-id                      - Configure router ID
 [no] shutdown                       - Disable OSPF 

 show database                       - Show database
 show interface-table                - Show interface table
 show neighbor-table                 - Show neighbor table
```

### area *(not entered — parameterized context)*
```text
<area-id>            : Area ID [0.0.0.0]


SF-1p-187>config>router(1)>ospf# area
```

### external-preference
```text
<priority>           : Priority [1..255, default 110]


SF-1p-187>config>router(1)>ospf# external-preference
```

### internal-preference
```text
<priority>           : Priority [1..255, default 30]


SF-1p-187>config>router(1)>ospf# internal-preference
```

### redistribute
```text
<connected>          : Connected
 <static>             : Static
 <bgp>                : BGP


SF-1p-187>config>router(1)>ospf# redistribute
```

### router-id
```text
<ip>                 : Router ID (IP address format) [0.0.0.0]


SF-1p-187>config>router(1)>ospf# router-id
```

### show database
```text
<CR>

SF-1p-187>config>router(1)>ospf# show database
```

### show interface-table
```text
<CR>

SF-1p-187>config>router(1)>ospf# show interface-table
```

### show neighbor-table
```text
<CR>

SF-1p-187>config>router(1)>ospf# show neighbor-table
```

### shutdown
```text
<CR>

SF-1p-187>config>router(1)>ospf# shutdown
```

## configure router NAME route-map NAME

Level help (`?`):
```text
delete                         - Remove statement from policy profile
      deny                           - Add deny statement to policy profile
      permit                         - Add permit statement to policy profile
      remark                         - Add remark statement to policy profile


SF-1p-187>config>router(1)>route-map(zzz-hrvst)$
```

### delete
```text
<sequence>           : [number] [1..65535]


SF-1p-187>config>router(1)>route-map(zzz-hrvst)$ delete
```

### deny
```text
<CR>
 <match>              : 
 <sequence>           : 


SF-1p-187>config>router(1)>route-map(zzz-hrvst)$ deny
```

### permit
```text
<CR>
 <match>              : 
 <set>                : 
 <sequence>           : 


SF-1p-187>config>router(1)>route-map(zzz-hrvst)$ permit
```

### remark
```text
<description>        : [1..252 chars]


SF-1p-187>config>router(1)>route-map(zzz-hrvst)$ remark
```

## configure router NAME tunnel-interface NAME

Level help (`?`):
```text
[no] access-group                   - Bind ACL to Tunnel Interface
      clear-access-list-statistics   - Clear ACL statistics
      clear-statistics               - Clears Tunnel statistics counters
 [no] crypto-map                     - 
 [no] ip-address                     - Configure tunnel IP address
 [no] ip-mtu                         - Configure tunnel IP MTU
 [no] multipoint                     - Configure tunnel as multipoint
 [no] name                           - Configure Tunnel name
 [no] nhrp-map                       - Configure NHRP mapping
 [no] nhrp-nhs                       - Configure NHRP server
 [no] nhrp-registration-timeout      - Configure NHRP registration timeout
 [no] ospf                           + Configure OSPF
 [no] pm-collection                  - Enable Performance Management (PM)
 [no] shutdown                       - 
 [no] tunnel-destination             - Configure tunnel destination
 [no] tunnel-source                  - Configure tunnel source
 [no] tunnel-underlay-destination    - Configure GREoIPsec underlay destination 
                                       (for tunnel mode only)
 [no] tunnel-underlay-source         - Configure GREoIPsec underlay source (for 
                                       tunnel mode only)

 show access-list-statistics         - Show ACL statistics
 show access-list-summary            - ACL Information
 show crypto-map-status
 show status                         - Show tunnel status
```

### access-group
```text
<acl-name>           : ACL name [1..80 chars]


SF-1p-187>config>router(1)>tunnel-interface(1)# access-group
```

### bind
```text
# cli error: Invalid Command
SF-1p-187>config>router(1)>tunnel-interface(1)# bind
```

### clear-access-list-statistics
```text
<CR>
 <in>                 : In
 <ipv4>               : IPv4
 <ipv6>               : IPv6


SF-1p-187>config>router(1)>tunnel-interface(1)# clear-access-list-statistics
```

### clear-nhrp
```text
# cli error: Invalid Command
SF-1p-187>config>router(1)>tunnel-interface(1)# clear-nhrp
```

### clear-statistics
```text
<CR>

SF-1p-187>config>router(1)>tunnel-interface(1)# clear-statistics
```

### crypto-map
```text
<name>               : [1..80 chars]


SF-1p-187>config>router(1)>tunnel-interface(1)# crypto-map
```

### dscp
```text
# cli error: Invalid Command
SF-1p-187>config>router(1)>tunnel-interface(1)# dscp
```

### ip-address
```text
<address-mask>       : Tunnel address [0.0.0.0/32|0:0:0:0::0/128]


SF-1p-187>config>router(1)>tunnel-interface(1)# ip-address
```

### ip-mtu
```text
<bytes>              : MTU in bytes [number] [128..65535]


SF-1p-187>config>router(1)>tunnel-interface(1)# ip-mtu
```

### key
```text
# cli error: Invalid Command
SF-1p-187>config>router(1)>tunnel-interface(1)# key
```

### multipoint
```text
<CR>

SF-1p-187>config>router(1)>tunnel-interface(1)# multipoint
```

### name
```text
<string>             : [1..64 chars]


SF-1p-187>config>router(1)>tunnel-interface(1)# name
```

### nhrp-map
```text
<logical-ip-address> : Element to map to NBMA address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)>tunnel-interface(1)# nhrp-map
```

### nhrp-nhs
```text
<ip-address>         : NHRP server [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)>tunnel-interface(1)# nhrp-nhs
```

### nhrp-registration-timeout
```text
<seconds>            : NHRP registration timeout (in seconds) [number, default 
                        2400] [1..65535]


SF-1p-187>config>router(1)>tunnel-interface(1)# nhrp-registration-timeout
```

### pm-collection
```text
<interval>           : PM collection interval


SF-1p-187>config>router(1)>tunnel-interface(1)# pm-collection
```

### show access-list-statistics
```text
<CR>
 <in>                 : In
 <ipv4>               : IPv4
 <ipv6>               : IPv6


SF-1p-187>config>router(1)>tunnel-interface(1)# show access-list-statistics
```

### show access-list-summary
```text
<CR>

SF-1p-187>config>router(1)>tunnel-interface(1)# show access-list-summary
```

### show crypto-map-status
```text
<CR>
 <name>               : [1..80 chars]


SF-1p-187>config>router(1)>tunnel-interface(1)# show crypto-map-status
```

### show status
```text
<CR>
 <all>                : 
 <nhrp>               : 
 <dmvpn>              : 


SF-1p-187>config>router(1)>tunnel-interface(1)# show status
```

### shutdown
```text
<CR>

SF-1p-187>config>router(1)>tunnel-interface(1)# shutdown
```

### transport-router
```text
# cli error: Invalid Command
SF-1p-187>config>router(1)>tunnel-interface(1)# transport-router
```

### tunnel-destination
```text
<address>            : Destination address [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>router(1)>tunnel-interface(1)# tunnel-destination
```

### tunnel-source
```text
<CR>
 <address>            : Source address [0.0.0.0|0:0:0:0::0]
 router-interface

SF-1p-187>config>router(1)>tunnel-interface(1)# tunnel-source
```

## configure router NAME tunnel-interface NAME ospf

Level help (`?`):
```text
area                           - Set area
      authentication-key             - Configure authentication key
 [no] authentication-type            - Configure authentication type
      dead-interval                  - Configure dead interval
      hello-interval                 - Configure hello interval
      metric                         - Configure metric
 [no] passive                        - Suppress hello packets
      priority                       - Configure interface priority
      retransmit-interval            - Configure retransmit interval
 [no] shutdown                       - Disable OSPF
      transit-delay                  - Configure transit delay
```

### area
```text
<area-id>            : Area ID [0.0.0.0]


SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# area
```

### authentication-key
```text
<key>                : Key [0..22 chars]


SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# authentication-key
```

### authentication-type
```text
<simple-password>    : Simple password


SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# authentication-type
```

### dead-interval
```text
<seconds>            : Dead interval (seconds) [1..2147483647, default 40]


SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# dead-interval
```

### hello-interval
```text
<seconds>            : Hello interval (seconds) [1..65535, default 10]


SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# hello-interval
```

### metric
```text
<value>              : Metric [1..65535, default 1]


SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# metric
```

### passive
```text
<CR>

SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# passive
```

### priority
```text
<priority>           : Interface priority [0..255, default 1]


SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# priority
```

### retransmit-interval
```text
<seconds>            : Retransmit interval (seconds) [0..3600, default 5]


SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# retransmit-interval
```

### shutdown
```text
<CR>

SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# shutdown
```

### transit-delay
```text
<seconds>            : Transit delay (seconds) [0..3600, default 1]


SF-1p-187>config>router(1)>tunnel-interface(1)>ospf# transit-delay
```

## configure sd-iot

Level help (`?`):
```text
authentication-method          - Configure sd-iot authentication-method
 [no] certificate                    - Configure sd-iot certification
      clear-statistics               - Clear sd-iot statistics
 [no] client-number                  - Configure sd-iot client number
 [no] duplication                    - Configure sd-iot duplication function
 [no] ingress-port                   - Configure sd-iot ingress port
      keep-alive                     - Configure sd-iot tunnels keep alive 
                                       interval and retries
 [no] shutdown                       - Configure sd-iot entity activity
 [no] tunnel                         + Configure sd-iot tunnel
 [no] username                       - Configure sd-iot username and password

 show statistics                     - Display sd-iot entity statistics
 show status                         - Display sd-iot entity status
```

### authentication-method
```text
<psk>                : Password-based authentication
 <certificate>        : Certificate-based authentication


SF-1p-187>config>sd-iot# authentication-method
```

### certificate
```text
<certificate-name>   : Sd-iot certificate name [1..64 chars]


SF-1p-187>config>sd-iot# certificate
```

### clear-statistics
```text
<CR>

SF-1p-187>config>sd-iot# clear-statistics
```

### client-number
```text
<number>             : Sd-iot client number [1..1000]


SF-1p-187>config>sd-iot# client-number
```

### duplication
```text
<ethernet>           : Ethernet


SF-1p-187>config>sd-iot# duplication
```

### ingress-port
```text
<ethernet>           : Ethernet


SF-1p-187>config>sd-iot# ingress-port
```

### keep-alive
```text
<CR>
 interval
 retries

SF-1p-187>config>sd-iot# keep-alive
```

### show statistics
```text
<CR>

SF-1p-187>config>sd-iot# show statistics
```

### show status
```text
<CR>

SF-1p-187>config>sd-iot# show status
```

### shutdown
```text
<CR>

SF-1p-187>config>sd-iot# shutdown
```

### tunnel *(not entered — parameterized context)*
```text
<number>             : Sd-iot tunnel number [1..2]


SF-1p-187>config>sd-iot# tunnel
```

### username
```text
<username-string>    : Sd-iot username [1..80 chars]


SF-1p-187>config>sd-iot# username
```

## configure system

Level help (`?`):
```text
[no] announcement                   - Post-login banner text
      clock                          + Clock configuration
 [no] contact                        - Contact name
      date-and-time                  + Configure date and time
      dhcp-relay                     + Enable DHCP Relay
 [no] dhcp-server                    + DHCP server level state
 [no] dhcpv6-server                  + DHCPv6 server level
      generate-log-report            - Command to generate log report file to be
                                        exported by copy command
      hostname                       - Hostname type
      inventory                      - Specifies device inventory parameters
 [no] ip-domain-name                 - 
 [no] ip-host                        - 
 [no] location                       - Device location
 [no] login-message                  - Pre-login banner text
 [no] modbus-unit                    + Configure Modbus unit
      mqtt                           + MQTT level
 [no] name                           - Device name
 [no] opcua-server                   + OPC UA server level
      serial                         + Serial port global configuration level
      syslog                         + Configure Syslog

 show copyright                      - Display copyright message
 show device-information             - Display device information
 show resources                      - Display system metrics for CPU, RAM and 
                                        disk
 show summary-inventory              - Displays a list with installed hardware 
                                        and software
 show system                         - Display system information
 show system-date                    - Display date and time
 show tech-support                   - Executes a predefined series of commands
```

### announcement
```text
<message>            : 


SF-1p-187>config>system# announcement
```

### contact
```text
<contact-person>     : Contact name [0..255 chars, default contact person]


SF-1p-187>config>system# contact
```

### dhcp-server *(not entered — parameterized context)*
```text
<number>             : [1..1, default 1]


SF-1p-187>config>system# dhcp-server
```

### dhcpv6-server *(not entered — parameterized context)*
```text
<number>             : [1..1, default 1]


SF-1p-187>config>system# dhcpv6-server
```

### generate-log-report
```text
<CR>

SF-1p-187>config>system# generate-log-report
```

### hostname
```text
<mac>                : 
 <string>             : 


SF-1p-187>config>system# hostname
```

### inventory
```text
<entity-index>       : Unique identifier for device inventory [number]


SF-1p-187>config>system# inventory
```

### ip-domain-name
```text
<name>               : [1..255 chars]


SF-1p-187>config>system# ip-domain-name
```

### ip-host
```text
<fqdn>               : FQDN [1..255 chars]


SF-1p-187>config>system# ip-host
```

### location
```text
<location-of-device> : Device location [0..255 chars, default the location of 
                        this device]


SF-1p-187>config>system# location
```

### login-message
```text
<message>            : 


SF-1p-187>config>system# login-message
```

### modbus-unit *(parameterized — inner help harvested under "configure system modbus-unit NAME")*
```text
<unit-name>          : Modbus unit local name [1..32 chars]


SF-1p-187>config>system# modbus-unit
```

### name
```text
<name-of-device>     : Device name [0..255 chars]


SF-1p-187>config>system# name
```

### opcua-server *(parameterized — inner help harvested under "configure system opcua-server NAME")*
```text
<name>               : OPC UA local server name [1..32 chars]


SF-1p-187>config>system# opcua-server
```

### show copyright
```text
<CR>

SF-1p-187>config>system# show copyright
```

### show device-information
```text
<CR>

SF-1p-187>config>system# show device-information
```

### show resources
```text
<CR>

SF-1p-187>config>system# show resources
```

### show summary-inventory
```text
<CR>

SF-1p-187>config>system# show summary-inventory
```

### show system
```text
<CR>

SF-1p-187>config>system# show system
```

### show system-date
```text
<CR>

SF-1p-187>config>system# show system-date
```

### show tech-support
```text
<CR>
 <file>               : 
 <terminal>           : Commands output is printed to terminal screen


SF-1p-187>config>system# show tech-support
```

### syslog *(not entered — parameterized context)*
```text
<device>             : Device
 <server>             : Server


SF-1p-187>config>system# syslog
```

## configure system clock

Level help (`?`):
```text
gnss                           + Create/delete GNSS
```

### gnss *(not entered — parameterized context)*
```text
<1>                  : 


SF-1p-187>config>system>clock# gnss
```

## configure system date-and-time

Level help (`?`):
```text
date-format                    - Date format
      date                           - Set  date (yyyy-mm-dd) 
      ntp                            + Configure NTP client
 [no] summer-time                    - Configure summer time begin and end
      time                           - Set time
      zone                           - Time zone

 show summer-time                    - Show summer time details
```

### date
```text
<date>               : Set  date (yyyy-mm-dd) [yyyy-mm-dd]


SF-1p-187>config>system>date-time# date
```

### date-format
```text
<yyyy-mm-dd>         : yyyy-mm-dd
 <dd-mm-yyyy>         : dd-mm-yyyy
 <mm-dd-yyyy>         : mm-dd-yyyy 
 <yyyy-dd-mm>         : yyyy-dd-mm


SF-1p-187>config>system>date-time# date-format
```

### show summer-time
```text
<CR>

SF-1p-187>config>system>date-time# show summer-time
```

### summer-time
```text
<recurring>          : 
 <date>               : 


SF-1p-187>config>system>date-time# summer-time
```

### time
```text
<time>               : Set time [hh:mm[:ss]]


SF-1p-187>config>system>date-time# time
```

### zone
```text
<utc>                : Universal Time Coordinated


SF-1p-187>config>system>date-time# zone
```

## configure system date-and-time ntp

Level help (`?`):
```text
[no] server                         + NTP server level
 [no] source-address                 - Configure source IP address of NTP 
                                       packets

 show status                         - NTP status
```

### server *(parameterized — inner help harvested under "configure system date-and-time ntp server NAME")*
```text
<server-id>          : NTP server number [1..10]


SF-1p-187>config>system>date-time>ntp# server
```

### show status
```text
<CR>

SF-1p-187>config>system>date-time>ntp# show status
```

### source-address
```text
<outbound-interface-a: 


SF-1p-187>config>system>date-time>ntp# source-address
```

## configure system date-and-time ntp server NAME

Level help (`?`):
```text
address                        - Configure NTP server IP address
 [no] prefer                         - Preferred server
      query-server                   - Send server an NTP polling request
 [no] shutdown                       - Enable SNTP server connection
```

### address
```text
<ip-address>         : NTP server IP address [0.0.0.0|0:0:0:0::0|host-name]


SF-1p-187>config>system>date-time>ntp>server(1)# address
```

### prefer
```text
<CR>

SF-1p-187>config>system>date-time>ntp>server(1)# prefer
```

### query-server
```text
<CR>

SF-1p-187>config>system>date-time>ntp>server(1)# query-server
```

### shutdown
```text
<CR>

SF-1p-187>config>system>date-time>ntp>server(1)# shutdown
```

## configure system dhcp-relay

Level help (`?`):
```text
source-port                    - Configure DHCP relay source port
```

### source-port
```text
<default>            : 
 <udp>                : 


SF-1p-187>config>system>dhcp-relay# source-port
```

## configure system modbus-unit NAME

Level help (`?`):
```text
byte-order                     - Byte order
 [no] description                    - Unit description
 [no] ip-address                     - Modbus unit IP address
 [no] poll                           + Poll local name
 [no] retries                        - Number of retries
 [no] shutdown                       - 
 [no] timeout                        - 
 [no] unit-id                        - Slave unit ID
```

### byte-order
```text
<big-endian>         : 
 <little-endian>      : 
 <big-endian-swapped> : 
 <little-endian-swappe: 


SF-1p-187>config>system>modbus-unit(AAA)# byte-order
```

### description
```text
<string>             : [1..255 chars]


SF-1p-187>config>system>modbus-unit(AAA)# description
```

### ip-address
```text
<ip-address>         : [0.0.0.0|0:0:0:0::0]


SF-1p-187>config>system>modbus-unit(AAA)# ip-address
```

### poll *(parameterized — inner help harvested under "configure system modbus-unit NAME poll NAME")*
```text
<poll-name>          : Poll local name [1..32 chars]


SF-1p-187>config>system>modbus-unit(AAA)# poll
```

### retries
```text
<number>             : [1..10, default 3]


SF-1p-187>config>system>modbus-unit(AAA)# retries
```

### shutdown
```text
<CR>

SF-1p-187>config>system>modbus-unit(AAA)# shutdown
```

### timeout
```text
<milliseconds>       : [100..10000, default 3000]


SF-1p-187>config>system>modbus-unit(AAA)# timeout
```

### unit-id
```text
<number>             : Slave unit ID [1..247, default 1]


SF-1p-187>config>system>modbus-unit(AAA)# unit-id
```

## configure system modbus-unit NAME poll NAME

Level help (`?`):
```text
acquisition                    - Data acquisition mode (poll interval or 
                                       interrupt)
 [no] description                    - Poll description
 [no] map-to-mqtt                    - 
 [no] map-to-opcua                   - Source of the MQTT server name
 [no] modbus-operation               - Modbus function
 [no] scaling                        - Configure data scaling
 [no] shutdown                       - 
 [no] start-address                  - Holding register start address
```

### acquisition
```text
poll-interval

SF-1p-187>config>system>modbus-unit(AAA)>poll(PPP)# acquisition
```

### description
```text
<desc>               : [1..128 chars]


SF-1p-187>config>system>modbus-unit(AAA)>poll(PPP)# description
```

### map-to-mqtt
```text
<mqtt-server-name>   : MQTT server (broker) name
 <opcua-server-name>  : OPC UA server in which the MQTT server (broker) IP 
                        address is stored


SF-1p-187>config>system>modbus-unit(AAA)>poll(PPP)# map-to-mqtt
```

### map-to-opcua
```text
<server-name>        : [1..32 chars]


SF-1p-187>config>system>modbus-unit(AAA)>poll(PPP)# map-to-opcua
```

### modbus-operation
```text
function

SF-1p-187>config>system>modbus-unit(AAA)>poll(PPP)# modbus-operation
```

### scaling
```text
<CR>
 factor
 offset

SF-1p-187>config>system>modbus-unit(AAA)>poll(PPP)# scaling
```

### shutdown
```text
<CR>

SF-1p-187>config>system>modbus-unit(AAA)>poll(PPP)# shutdown
```

### start-address
```text
<number>             : [0..65535, default 40001]


SF-1p-187>config>system>modbus-unit(AAA)>poll(PPP)# start-address
```

## configure system mqtt

Level help (`?`):
```text
[no] server                         + MQTT server level
```

### server *(parameterized — inner help harvested under "configure system mqtt server NAME")*
```text
<name>               : Server name [1..32 chars]


SF-1p-187>config>system>mqtt# server
```

## configure system mqtt server NAME

Level help (`?`):
```text
[no] address                        - Configure server IP parameters
 [no] certificate                    - Configure X.509 certificate for MQTTS 
                                       authentication
 [no] management-channel             - Open management channel with server
 [no] user                           - Configure user credential for 
                                       authentication

 show status                         - Display MQTT connection status
```

### address
```text
<ip>                 : 
 <url>                : 


SF-1p-187>config>system>mqtt>server(MY-BROKER)# address
```

### certificate
```text
<certificate-name>   : MQTTS certificate [1..64 chars]


SF-1p-187>config>system>mqtt>server(MY-BROKER)# certificate
```

### management-channel
```text
<CR>

SF-1p-187>config>system>mqtt>server(MY-BROKER)# management-channel
```

### show status
```text
<CR>

SF-1p-187>config>system>mqtt>server(MY-BROKER)# show status
```

### user
```text
name

SF-1p-187>config>system>mqtt>server(MY-BROKER)# user
```

## configure system opcua-server NAME

Level help (`?`):
```text
[no] application-certificate        - Assign X.509 certificate as application 
                                       certificate
 [no] application-name               - Configure application name
 [no] application-uri                - Configure application URI
 [no] endpoint                       - Configure endpoint
 [no] shutdown                       - Disable server
 [no] trusted-ca                     - Configure CA trusted for OPC UA
```

### application-certificate
```text
<certificate-name>   : OPC UA application name [1..64 chars]


SF-1p-187>config>system>opcua-server(AAA)# application-certificate
```

### application-name
```text
<default>            : 
 <custom>             : 


SF-1p-187>config>system>opcua-server(AAA)# application-name
```

### application-uri
```text
<default>            : 
 <custom>             : 


SF-1p-187>config>system>opcua-server(AAA)# application-uri
```

### endpoint
```text
<default>            : 
 <custom>             : 


SF-1p-187>config>system>opcua-server(AAA)# endpoint
```

### shutdown
```text
<CR>

SF-1p-187>config>system>opcua-server(AAA)# shutdown
```

### trusted-ca
```text
<name>               : Trusted CA name [1..20 chars]


SF-1p-187>config>system>opcua-server(AAA)# trusted-ca
```

## configure system serial

Level help (`?`):
```text
terminal-server                + Terminal server global configuration 
                                       level
```

## configure system serial terminal-server

Level help (`?`):
```text
[no] dead-peer-timeout              - Configure dead peer detection
 [no] shutdown                       - Disable terminal server
```

### dead-peer-timeout
```text
<minutes>            : [1..1440, default 10]


SF-1p-187>config>system>serial>terminal-server# dead-peer-timeout
```

### shutdown
```text
<CR>

SF-1p-187>config>system>serial>terminal-server# shutdown
```

## configure terminal

Level help (`?`):
```text
baud-rate                      - Terminal baud rate
      console-timeout                - Specifies the time of inactivity after 
                                       which the device disconnects
      length                         - Configure terminal screen size (number of
                                        rows)
 [no] serial-port-console            - Use serial port as console
      timeout                        - Terminal timeout
```

### baud-rate
```text
<300bps>             : 300 bps
 <1200bps>            : 1200 bps
 <2400bps>            : 2400 bps
 <4800bps>            : 4800 bps
 <9600bps>            : 9600 bps
 <19200bps>           : 19200 bps
 <38400bps>           : 38400 bps
 <57600bps>           : 57600 bps
 <115200bps>          : 115200 bps


SF-1p-187>config>terminal# baud-rate
```

### console-timeout
```text
<forever>            : Disables disconnecting the device in case of inactivity
 <limited>            : Enables disconnecting the device in case of inactivity 
                        after a specified time period


SF-1p-187>config>terminal# console-timeout
```

### length
```text
<number-of-rows>     : Number of rows to print before pausing (or 0 for no 
                        pausing). [0..255, default 20]


SF-1p-187>config>terminal# length
```

### serial-port-console
```text
<CR>

SF-1p-187>config>terminal# serial-port-console
```

### timeout
```text
<forever>            : No timeout
 <limited>            : Enable timeout


SF-1p-187>config>terminal# timeout
```

## file

Level help (`?`):
```text
delete                         - Delete file
      delete-from-folder             - Deletes a user file
      delete-user                    - Deletes a file from the device
 [no] description                    - Description of the file
      dir                            - Display file directory
 [no] flash-enable                   - Enable flash (SD card)
      flash-temporarily-enable       - Enable flash until inactivity time is 
                                       reached
      folder-dir                     - List of all user files
      media-dir                      - Execute media dir
      user-file-dir                  - List of all user files in the device

 show banner-text                    - Display banner
 show configuration-files            - Displays configuration files properties
 show copy                           - Display Copy progress
 show factory-default-config         - Display factory-default-config
 show file-details                   - Displays the details of the file
 show file-transfer-status           - Display Copy progress
 show flash-status
 show rollback-config                - Display rollback-config
 show schedule-log                   - Display schedule-log  
 show startup-config                 - Display startup-config
 show sw-pack                        - Display SW packs
 show user-default-config            - Display user-default-config
 show user-dir
```

### delete
```text
<sw-pack-2>          : 
 <startup-config>     : 
 <zero-touch-config-xm: 
 <restore-point-config: 
 <user-script>        : 
 <script-result>      : 


SF-1p-187>file# delete
```

### delete-from-folder
```text
<filename>           : [string]


SF-1p-187>file# delete-from-folder
```

### delete-user
```text
<filename>           : [string]


SF-1p-187>file# delete-user
```

### description
```text
<file-name>          : The name of the file [1..37 chars]


SF-1p-187>file# description
```

### dir
```text
<CR>

SF-1p-187>file# dir
```

### flash-enable
```text
<CR>

SF-1p-187>file# flash-enable
```

### flash-temporarily-enable
```text
inactivity-timeout

SF-1p-187>file# flash-temporarily-enable
```

### folder-dir
```text
<CR>

SF-1p-187>file# folder-dir
```

### media-dir
```text
media

SF-1p-187>file# media-dir
```

### show banner-text
```text
<CR>

SF-1p-187>file# show banner-text
```

### show configuration-files
```text
<CR>

SF-1p-187>file# show configuration-files
```

### show copy
```text
<CR>
 <summary>            : 


SF-1p-187>file# show copy
```

### show factory-default-config
```text
<CR>

SF-1p-187>file# show factory-default-config
```

### show file-details
```text
<filename>           : [string]


SF-1p-187>file# show file-details
```

### show file-transfer-status
```text
<CR>

SF-1p-187>file# show file-transfer-status
```

### show flash-status
```text
<CR>

SF-1p-187>file# show flash-status
```

### show rollback-config
```text
<CR>

SF-1p-187>file# show rollback-config
```

### show schedule-log
```text
<CR>

SF-1p-187>file# show schedule-log
```

### show startup-config
```text
<CR>

SF-1p-187>file# show startup-config
```

### show sw-pack
```text
<CR>

SF-1p-187>file# show sw-pack
```

### show user-default-config
```text
<CR>

SF-1p-187>file# show user-default-config
```

### show user-dir
```text
<filename>           : [string]


SF-1p-187>file# show user-dir
```

### user-file-dir
```text
<CR>

SF-1p-187>file# user-file-dir
```

## quick-setup

Level help (`?`):
```text
port                           + Configure port
      router                         + 
      vpn                            +
```

## quick-setup port

Level help (`?`):
```text
cellular                       + Cellular interface configuration
      ethernet                       + 
      serial                         + Serial port level
 [no] virtual                        - 
 [no] wifi-client                    + WiFi client level
      wlan                           + Configure wlan interface

 show summary                        - Display ports status summary
```

### cellular *(not entered — parameterized context)*
```text
<lte>                : 


SF-1p-187>quick-setup>port# cellular
```

### ethernet *(not entered — parameterized context)*
```text
<1>                  : 
 <2>                  : 
 <3>                  : 
 <4>                  : 
 <5>                  : 
 <6>                  : 
 <switch1>            : 


SF-1p-187>quick-setup>port# ethernet
```

### serial *(not entered — parameterized context)*
```text
<2>                  : 
 <1>                  : 


SF-1p-187>quick-setup>port# serial
```

### virtual
```text
<number>             : [1..10]


SF-1p-187>quick-setup>port# virtual
```

### wlan *(not entered — parameterized context)*
```text
<2.4g>               : 
 <5g>                 : 


SF-1p-187>quick-setup>port# wlan
```

## quick-setup port wifi-client

Level help (`?`):
```text
[no] address                        - Configure interface IP
      connection-method              - Configure first SSID to connect
 [no] dhcp                           - Enable DHCP client
 [no] dhcpv6-client                  - Enable DHCPv6 client
 [no] ipv6-autoconfig                - Enable IPv6 autoconfiguration
 [no] nat                            - Enable NAT
 [no] shutdown                       - Disable client
 [no] ssid                           + SSID level

 show summary                        - Display ports status summary
```

### connection-method
```text
<last>               : 
 <best>               : 
 <priority>           : 


SF-1p-187>quick-setup>port>wifi-client# connection-method
```

### dot1x *(not entered — parameterized context)*
```text
# cli error: Invalid Command
SF-1p-187>quick-setup>port>wifi-client# dot1x
```

### show networks
```text
# cli error: Invalid Command
SF-1p-187>quick-setup>port>wifi-client# show networks
```

### show status
```text
# cli error: Invalid Command
SF-1p-187>quick-setup>port>wifi-client# show status
```

### shutdown
```text
<CR>

SF-1p-187>quick-setup>port>wifi-client# shutdown
```

### ssid *(not entered — parameterized context)*
```text
<name>               : SSID [1..32 chars]


SF-1p-187>quick-setup>port>wifi-client# ssid
```

## quick-setup router

Level help (`?`):
```text
[no] default-gateway                - Configure default gateway
 [no] nat                            + Enable/disable-delete NAT configuration
 [no] router                         + Configure router
```

### default-gateway
```text
<address>            : Default gateway IP address [0.0.0.0]


SF-1p-187>quick-setup>router# default-gateway
```

### router *(not entered — parameterized context)*
```text
<number>             : Router number [number] [1..10]


SF-1p-187>quick-setup>router# router
```

## quick-setup router nat

Level help (`?`):
```text
[no] nat-exclude-source-ip          - Configure NAT exclude expression
 [no] nat-inside-overload            - Configure a NAPT rule inside to outside
 [no] nat-inside-source-static       - Configure NAT rule inside to outside
 [no] nat-inside-source-static-port  - Configure/modify/delete NAT rule from the
                                        inside to outside
      nat-timeout                    - Configure translation table entries 
                                       timeout
```

### clear-nat-statistics
```text
# cli error: Invalid Command
SF-1p-187>quick-setup>router>nat# clear-nat-statistics
```

### clear-nat-translations
```text
# cli error: Invalid Command
SF-1p-187>quick-setup>router>nat# clear-nat-translations
```

### nat-exclude-source-ip
```text
<source-ip>          : IP Address of source IP station [0.0.0.0]


SF-1p-187>quick-setup>router>nat# nat-exclude-source-ip
```

### nat-inside-overload
```text
source

SF-1p-187>quick-setup>router>nat# nat-inside-overload
```

### nat-inside-source-static
```text
<inside-ip>          : IP Address of Inside IP station [0.0.0.0]


SF-1p-187>quick-setup>router>nat# nat-inside-source-static
```

### nat-inside-source-static-port
```text
<tcp>                : Indicate that the configured port number is associated 
                        with TCP
 <udp>                : Indicate that the configured port number is associated 
                        with UDP


SF-1p-187>quick-setup>router>nat# nat-inside-source-static-port
```

### nat-timeout
```text
<CR>
 tcp
 udp
 others

SF-1p-187>quick-setup>router>nat# nat-timeout
```

### show nat-translations
```text
# cli error: Invalid Command
SF-1p-187>quick-setup>router>nat# show nat-translations
```

## quick-setup vpn

Level help (`?`):
```text
[no] ipsec-transform-set            + Configure IPsec phase 2 policy
 [no] isakmp-policy                  + Configure IPsec phase 1 policy
      submit                         - 
 [no] tunnel                         + Configure tunnel interface
```

### ipsec-transform-set *(not entered — parameterized context)*
```text
<name>               : [1..80 chars]


SF-1p-187>quick-setup>vpn# ipsec-transform-set
```

### isakmp-policy *(not entered — parameterized context)*
```text
<sequence>           : [number]


SF-1p-187>quick-setup>vpn# isakmp-policy
```
