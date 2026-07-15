# etx2v CLI reference (harvested `?` help)

Captured live from etx2v-1 (ETX-2V chassis variant (manual ETX-2V-CA_AC_2CMB_4U_D) - FIRST etx2v-family unit; dialect assumed shared context CLI, NOT verified live - harvest before trusting reads) on 2026-07-15 by scripts/harvest_cli.py
(re-run `harvest` after firmware upgrades — it diffs and updates in place).
Every section is a CLI context: first the level `?` listing (commands +
descriptions), then per-command argument help (`<command> ?`). Sections
ending in NAME are parameterized contexts harvested through one instance
(an existing one, or a temp object created and rolled back) — NAME stands
for any instance. Entries marked *(not entered)* could not be harvested
safely — their inner structure is in command-tree-etx2v.md; use
cli_help with a real index for inner argument syntax.

## <root>

Level help (`?`):
```text
admin                          + Adminstrative commands
      configure                      + Configure device
      file                           + File commands
      logon                          - Logon as Debug user
      on-configuration-error         - Behavior for configuration error

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
      cn-backup-file
      sw-update-1
      sw-update-2
The maximum allowed length/range is:
      <username> [1..60 chars]
      <password> [1..60 chars]
      <file>     [1..96 chars]
      <port>     [1..65535]



uCPE-OS# copy
```

### echo
```text
<CR>
 <text-to-echo>       : Text to display on screen [string]


uCPE-OS# echo
```

### exec
```text
<user-script>        : 


uCPE-OS# exec
```

### exit
```text
<CR>
 <all>                : Returns to Device context


uCPE-OS# exit
```

### help
```text
<CR>
 <command-name>       : Command for which help is requested [string]


uCPE-OS# help
```

### history
```text
<CR>

uCPE-OS# history
```

### info
```text
<CR>
 <detail>             : Adds information to every conf. parameter


uCPE-OS# info
```

### level-info
```text
<CR>
 <detail>             : Device configuration, including defaults


uCPE-OS# level-info
```

### logon
```text
<debug>              : Debug


uCPE-OS# logon
```

### logout
```text
<CR>

uCPE-OS# logout
```

### on-configuration-error
```text
<ignore>             : Ignore configuration error
 <stop>               : Stop at first error
 <reject>             : Reject, reboot and  load alternate configuration


uCPE-OS# on-configuration-error
```

### ping
```text
<ip-address>         : Destination IP [0.0.0.0|0:0:0:0::0]


uCPE-OS# ping
```

### popup-suspend
```text
<CR>

uCPE-OS# popup-suspend
```

### save
```text
<CR>

uCPE-OS# save
```

### schedule
```text
<name>               : Schedule name [string]


uCPE-OS# schedule
```

### telnet
```text
<ip-address>         : Telnet destination IP address [0.0.0.0|0:0:0:0::0]


uCPE-OS# telnet
```

### trace-route
```text
<ip-address>         : Destination IP [0.0.0.0|0:0:0:0::0]


uCPE-OS# trace-route
```

### tree
```text
<CR>
 <detail>             : Available commands, current context and downwards


uCPE-OS# tree
```

## admin

Level help (`?`):
```text
factory-default-all            - Return to factory default and reboot
      factory-default                - Return to factory default configuration 
                                       and reboot
      force-reboot                   - Reboot the device unconditionally
      license                        + 
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

uCPE-OS>admin# factory-default
```

### factory-default-all
```text
<CR>

uCPE-OS>admin# factory-default-all
```

### force-reboot
```text
<CR>

uCPE-OS>admin# force-reboot
```

### login
```text
<CR>

uCPE-OS>admin# login
```

### reboot
```text
<CR>
 <in>                 : 
 <at>                 : 
 <cancel>             : 


uCPE-OS>admin# reboot
```

### send
```text
<message>            : 


uCPE-OS>admin# send
```

### show reboot
```text
<CR>

uCPE-OS>admin# show reboot
```

### startup-confirm-required
```text
<CR>
 time-to-confirm
 rollback

uCPE-OS>admin# startup-confirm-required
```

### user-default
```text
<CR>

uCPE-OS>admin# user-default
```

## admin license

Level help (`?`):
```text
[no] license-enable                 - 

 show summary                        - Display license status summary
 show vcpe-os-id
```

### license-enable
```text
<system>             : 


uCPE-OS>admin>license# license-enable
```

### show summary
```text
<CR>

uCPE-OS>admin>license# show summary
```

### show vcpe-os-id
```text
<CR>

uCPE-OS>admin>license# show vcpe-os-id
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

uCPE-OS>admin>scheduler# clear-finished-schedules
```

### clear-schedule-log
```text
<CR>

uCPE-OS>admin>scheduler# clear-schedule-log
```

### show scheduler
```text
<CR>

uCPE-OS>admin>scheduler# show scheduler
```

### show scheduler-details
```text
<CR>

uCPE-OS>admin>scheduler# show scheduler-details
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


uCPE-OS>admin>software# install
```

### show status
```text
<CR>

uCPE-OS>admin>software# show status
```

### software-confirm-required
```text
<CR>
 time-to-confirm

uCPE-OS>admin>software# software-confirm-required
```

### undo-install
```text
<CR>

uCPE-OS>admin>software# undo-install
```

## configure

Level help (`?`):
```text
access-control                 + Configure access control
 [no] bridge                         + Configure bridge
      crypto                         + Cryptography level
      fault                          + 
      management                     + Device management commands
      oam                            + Configure OAM
      port                           + Configure port
      qos                            + Quality of service
      reporting                      + 
 [no] router                         + Configure router 
      system                         + Defines system parameters
      terminal                       + Configure terminal
      virtualization                 + configure virtualization
```

### bridge *(parameterized — inner help harvested under "configure bridge NAME")*
```text
<number>             : Bridge number [number]


uCPE-OS>config# bridge
```

### router *(parameterized — inner help harvested under "configure router NAME")*
```text
<number>             : Router number [number] [1..10]


uCPE-OS>config# router
```

## configure access-control

Level help (`?`):
```text
[no] access-list                    + Configure ACL
      resequence                     - Resequence ACL
```

### access-list *(not entered — parameterized context)*
```text
<ipv4>               : IPv4
 <ipv6>               : IPv6
 <acl-name>           : Access list name [1..80 chars]


uCPE-OS>config>access-control# access-list
```

### resequence
```text
access-list

uCPE-OS>config>access-control# resequence
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

uCPE-OS>config>bridge(1)$
```

### aging-time
```text
<seconds>            : MAC aging time (seconds) [number, default 300] 
                        [60..15300]


uCPE-OS>config>bridge(1)$ aging-time
```

### clear-mac-table
```text
<CR>

uCPE-OS>config>bridge(1)$ clear-mac-table
```

### filtering
```text
<CR>

uCPE-OS>config>bridge(1)$ filtering
```

### name
```text
<bridge-name>        : Bridge name [1..32 chars]


uCPE-OS>config>bridge(1)$ name
```

### show mac-address-table
```text
<static>             : Static MAC addresses
 <dynamic>            : Dynamic MAC addresses
 <all>                : All MAC addresses


uCPE-OS>config>bridge(1)# show mac-address-table
```

### show summary
```text
<CR>

uCPE-OS>config>bridge(1)# show summary
```

### show vlans
```text
<CR>
 vlan

uCPE-OS>config>bridge(1)# show vlans
```

### static-mac
```text
# cli error: Invalid Command
uCPE-OS>config>bridge(1)# static-mac
```

### vlan-aware
```text
<CR>

uCPE-OS>config>bridge(1)# vlan-aware
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
uCPE-OS>config>bridge(1)# accept-frame-type
```

### bind
```text
# cli error: Invalid Command
uCPE-OS>config>bridge(1)# bind
```

### ingress-filtering
```text
# cli error: Invalid Command
uCPE-OS>config>bridge(1)# ingress-filtering
```

### name
```text
<bridge-name>        : Bridge name [1..32 chars]


uCPE-OS>config>bridge(1)# name
```

### pvid
```text
# cli error: Invalid Command
uCPE-OS>config>bridge(1)# pvid
```

### shutdown
```text
# cli error: Invalid Command
uCPE-OS>config>bridge(1)# shutdown
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
uCPE-OS>config>bridge(1)# tagged-port
```

### untagged-port
```text
# cli error: Invalid Command
uCPE-OS>config>bridge(1)# untagged-port
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


uCPE-OS>config>crypto# ca
```

### crypto-map *(parameterized — inner help harvested under "configure crypto crypto-map NAME")*
```text
<name>               : [1..80 chars]


uCPE-OS>config>crypto# crypto-map
```

### ipsec-transform-set *(parameterized — inner help harvested under "configure crypto ipsec-transform-set NAME")*
```text
<name>               : [1..80 chars]


uCPE-OS>config>crypto# ipsec-transform-set
```

### isakmp-key
```text
<pre-shared-key>     : IKE pre-shared key [1..80 chars]


uCPE-OS>config>crypto# isakmp-key
```

### isakmp-policy *(parameterized — inner help harvested under "configure crypto isakmp-policy NAME")*
```text
<sequence>           : [number]


uCPE-OS>config>crypto# isakmp-policy
```

## configure crypto ca NAME

Level help (`?`):
```text
[no] address                        - Configure CA address
 [no] certificate-auto-renew         - Enable certificate auto renewal
 [no] crl-auto-renew                 - Enable CRL auto renewal
 [no] protocol                       - Configure protocol to communicate with 
                                       the CA


uCPE-OS>config>crypto>ca(zzz-hrvst)$
```

### address
```text
<ip>                 : 
 <url>                : 


uCPE-OS>config>crypto>ca(zzz-hrvst)$ address
```

### certificate-auto-renew
```text
<CR>

uCPE-OS>config>crypto>ca(zzz-hrvst)$ certificate-auto-renew
```

### crl-auto-renew
```text
<CR>

uCPE-OS>config>crypto>ca(zzz-hrvst)$ crl-auto-renew
```

### protocol
```text
<scep>               : SCEP protocol


uCPE-OS>config>crypto>ca(zzz-hrvst)$ protocol
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
 [no] sa-lifetime                    - Configure SA lifetime
 [no] sequence-number                - Configure crypto map priority
 [no] transform-set                  - Assign IPsec phase 2 policy


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$
```

### ike-authentication
```text
<pre-share>          : 
 <rsa-signature>      : 


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ ike-authentication
```

### ike-identity-local
```text
<default-address>    : 
 <address>            : 
 <default-hostname>   : 
 <hostname>           : 


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-local
```

### ike-identity-local-x509
```text
<distinguished-name> : 
 <string>             : 


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-local-x509
```

### ike-identity-remote
```text
<default-address>    : 
 <address>            : 
 <hostname>           : 


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-remote
```

### ike-identity-remote-x509
```text
<any>                : 
 <string>             : 


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-remote-x509
```

### ike-sa-lifetime
```text
<seconds>            : [60..86400, default 86400]


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ ike-sa-lifetime
```

### ike-sa-negotiation
```text
<main>               : 
 <aggressive>         : 


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ ike-sa-negotiation
```

### ike-version
```text
<1>                  : 
 <2>                  : 


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ ike-version
```

### match-address
```text
<name>               : [1..80 chars]


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ match-address
```

### peer-address
```text
<ip-address>         : [0.0.0.0|0:0:0:0::0, default 0.0.0.0]


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ peer-address
```

### pfs-group
```text
<1>                  : 
 <2>                  : 
 <5>                  : 
 <14>                 : 
 <19>                 : 
 <20>                 : 


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ pfs-group
```

### sa-lifetime
```text
seconds
 kilobytes

uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ sa-lifetime
```

### sequence-number
```text
<number>             : [1..1000, default 10]


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ sequence-number
```

### transform-set
```text
<name-1>             : [1..80 chars]


uCPE-OS>config>crypto>crypto-map(zzz-hrvst)$ transform-set
```

## configure crypto ipsec-transform-set NAME

Level help (`?`):
```text
algorithms                     - Configure IPsec phase 2 algorithms
      mode                           - Tunnel or transport mode


uCPE-OS>config>crypto>ipsec-transform-set(zzz-hrvst)$
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


uCPE-OS>config>crypto>ipsec-transform-set(zzz-hrvst)$ algorithms
```

### mode
```text
<tunnel>             : 
 <transport>          : 


uCPE-OS>config>crypto>ipsec-transform-set(zzz-hrvst)$ mode
```

## configure crypto isakmp-policy NAME

Level help (`?`):
```text
encryption                     - Configure encryption algorithm
      group                          - Configure Diffie Hellman group
      hash                           - Configure hashing algorithm


uCPE-OS>config>crypto>isakmp-policy(1)$
```

### encryption
```text
<aes-cbc-128>        : 
 <aes-cbc-256>        : 


uCPE-OS>config>crypto>isakmp-policy(1)$ encryption
```

### group
```text
<1>                  : 
 <2>                  : 
 <5>                  : 
 <14>                 : 
 <19>                 : 
 <20>                 : 


uCPE-OS>config>crypto>isakmp-policy(1)$ group
```

### hash
```text
<sha1>               : 
 <sha2-256>           : 
 <sha2-512>           : 


uCPE-OS>config>crypto>isakmp-policy(1)$ hash
```

## configure crypto key

Level help (`?`):
```text
delete-rsa                     - Delete device RSA keys
      generate-rsa                   - Generate RSA key pair
      import-rsa                     - Import RSA key pair

 show public-key-rsa                 - Display self RSA public key
```

### delete-rsa
```text
label

uCPE-OS>config>crypto>key# delete-rsa
```

### generate-rsa
```text
label

uCPE-OS>config>crypto>key# generate-rsa
```

### import-rsa
```text
label

uCPE-OS>config>crypto>key# import-rsa
```

### show public-key-rsa
```text
<CR>

uCPE-OS>config>crypto>key# show public-key-rsa
```

## configure crypto pki

Level help (`?`):
```text
authenticate                   - Authenticate CA by importing its 
                                       certificate
      delete-certificate             - Delete certificate
      delete-crl                     - Delete CRL
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

uCPE-OS>config>crypto>pki# authenticate
```

### delete-certificate
```text
certificate-name

uCPE-OS>config>crypto>pki# delete-certificate
```

### delete-crl
```text
crl-name

uCPE-OS>config>crypto>pki# delete-crl
```

### enroll
```text
<CR>
 certificate-folder-url
 certificate-name
 fingerprint
 common-name
 locality
 state
 email
 organization
 organizational-unit
 country
 challenge-password
 <serial-number>      : 


uCPE-OS>config>crypto>pki# enroll
```

### export-crl
```text
crl-name

uCPE-OS>config>crypto>pki# export-crl
```

### import-certificate
```text
certificate-name

uCPE-OS>config>crypto>pki# import-certificate
```

### import-crl
```text
crl-name

uCPE-OS>config>crypto>pki# import-crl
```

### self-sign-certificate
```text
certificate-name

uCPE-OS>config>crypto>pki# self-sign-certificate
```

### show certificate
```text
certificate-name

uCPE-OS>config>crypto>pki# show certificate
```

### show certificate-summary
```text
<CR>
 owner
 <valid-only>         : 
 <invalid-only>       : 


uCPE-OS>config>crypto>pki# show certificate-summary
```

### show crl-summary
```text
<CR>

uCPE-OS>config>crypto>pki# show crl-summary
```

## configure fault

Level help (`?`):
```text
[no] fault-propagation              + Fault propagation configuration
```

### fault-propagation
```text
<port>               : 


uCPE-OS>config>fault# fault-propagation
```

## configure management

Level help (`?`):
```text
access                         + Access commands
      dscp                           - Configure DSCP value
      ldap                           + Configure LDAP client
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


uCPE-OS>config>mngmnt# dscp
```

### login-user *(parameterized — inner help harvested under "configure management login-user NAME")*
```text
<name>               : User name [1..20 chars]


uCPE-OS>config>mngmnt# login-user
```

### management-address
```text
<ipv4>               : ipv4
 <ipv6>               : ipv6
 <ip-address>         : Management protocols source IP [0.0.0.0|0:0:0:0::0]


uCPE-OS>config>mngmnt# management-address
```

### show failed-login-attempts
```text
<CR>

uCPE-OS>config>mngmnt# show failed-login-attempts
```

### show ssh-server
```text
<fingerprint>        : 


uCPE-OS>config>mngmnt# show ssh-server
```

### show users
```text
<CR>

uCPE-OS>config>mngmnt# show users
```

### show users-details
```text
<CR>

uCPE-OS>config>mngmnt# show users-details
```

## configure management access

Level help (`?`):
```text
[no] access-group                   - Apply ACL to device management
      auth-policy                    - Configure authentication methods
      auth-policy-virtualization     - Configure Virtualization authentication 
                                       methods
 [no] ban-default-login-password     - Disallow default login password
      clear-statistics               - Clear ACL statistics
      ftps                           - Configure FTPS
 [no] login-password-black-list      - Configure string not allowed in login 
                                       password
 [no] login-password-properties      - Configure login password strength 
                                       requirement
 [no] rest-get                       - Enable REST get interface
 [no] scp-client                     - Enable SCP client
 [no] sftp                           - Enable SFTP
 [no] snmp                           - Enable SNMP 
      ssh-encryption                 - 
 [no] ssh                            - Enable SSH
 [no] telnet                         - Enable Telnet 
 [no] tftp                           - Enable TFTP
 [no] virtualization-rest            - Enable REST management for virtualization
 [no] web                            - Enable Web
 [no] ztc-after-reboot               - Start ZTC process after next reboot
 [no] ztc-bootstrap                  - Enable ZTC bootstrap provisioning
 [no] ztc-tftp-disable               - 

 show access-list                    - ACL Information 
 show statistics                     - Show ACL statistics
 show status
```

### access-group
```text
<acl-name>           : ACL name [string]


uCPE-OS>config>mngmnt>access# access-group
```

### auth-policy
```text
<1st-level>          : First method


uCPE-OS>config>mngmnt>access# auth-policy
```

### auth-policy-virtualization
```text
<1st-level>          : First method


uCPE-OS>config>mngmnt>access# auth-policy-virtualization
```

### ban-default-login-password
```text
<CR>

uCPE-OS>config>mngmnt>access# ban-default-login-password
```

### clear-statistics
```text
<ipv4>               : IPv4
 <ipv6>               : IPv6


uCPE-OS>config>mngmnt>access# clear-statistics
```

### ftps
```text
<CR>
 certificate

uCPE-OS>config>mngmnt>access# ftps
```

### login-password-black-list
```text
<banned-string>      : String not allowed in login password [4..20 chars]


uCPE-OS>config>mngmnt>access# login-password-black-list
```

### login-password-properties
```text
min-characters

uCPE-OS>config>mngmnt>access# login-password-properties
```

### rest-get
```text
<CR>
 certificate

uCPE-OS>config>mngmnt>access# rest-get
```

### scp-client
```text
<CR>

uCPE-OS>config>mngmnt>access# scp-client
```

### sftp
```text
<CR>

uCPE-OS>config>mngmnt>access# sftp
```

### show access-list
```text
<summary>            : ACL summary


uCPE-OS>config>mngmnt>access# show access-list
```

### show statistics
```text
<ipv4>               : IPv4
 <ipv6>               : IPv6


uCPE-OS>config>mngmnt>access# show statistics
```

### show status
```text
<CR>

uCPE-OS>config>mngmnt>access# show status
```

### snmp
```text
<CR>

uCPE-OS>config>mngmnt>access# snmp
```

### ssh
```text
<CR>
 port

uCPE-OS>config>mngmnt>access# ssh
```

### ssh-encryption
```text
<all>                : 
 <algorithm>          : 


uCPE-OS>config>mngmnt>access# ssh-encryption
```

### telnet
```text
<CR>

uCPE-OS>config>mngmnt>access# telnet
```

### tftp
```text
<CR>

uCPE-OS>config>mngmnt>access# tftp
```

### virtualization-rest
```text
<CR>
 certificate

uCPE-OS>config>mngmnt>access# virtualization-rest
```

### web
```text
<CR>
 certificate

uCPE-OS>config>mngmnt>access# web
```

### ztc-after-reboot
```text
<CR>

uCPE-OS>config>mngmnt>access# ztc-after-reboot
```

### ztc-bootstrap
```text
<CR>
 url
 <no-revertive>       : 
 <password>           : 


uCPE-OS>config>mngmnt>access# ztc-bootstrap
```

### ztc-tftp-disable
```text
<CR>

uCPE-OS>config>mngmnt>access# ztc-tftp-disable
```

## configure management ldap

Level help (`?`):
```text
[no] base-dn                        - Configure base distinguished name
 [no] search-dn                      - Configure search distinguished name
 [no] search-user                    - Configure search user
 [no] server                         + LDAP server level
```

### base-dn
```text
<string>             : Configure base distinguished name [string]


uCPE-OS>config>mngmnt>ldap# base-dn
```

### search-dn
```text
<string>             : Configure search distinguished name [string]


uCPE-OS>config>mngmnt>ldap# search-dn
```

### search-user
```text
name

uCPE-OS>config>mngmnt>ldap# search-user
```

### server *(parameterized — inner help harvested under "configure management ldap server NAME")*
```text
<name>               : [string]


uCPE-OS>config>mngmnt>ldap# server
```

## configure management ldap server NAME

Level help (`?`):
```text
[no] ip-address                     - Configure server IP address


uCPE-OS>config>mngmnt>ldap>server(zzz-hrvst)$
```

### ip-address
```text
<ip-address>         : LDAP server IP address [0.0.0.0|0:0:0:0::0]


uCPE-OS>config>mngmnt>ldap>server(zzz-hrvst)$ ip-address
```

## configure management login-user NAME

Level help (`?`):
```text
authentication-method          - Login user authentication method
      level                          - Login user level
      password                       - Password: hashed password [40 chars]; 
                                       non-hashed
 [no] public-key                     - User public key
 [no] shutdown                       - Disable user
```

### authentication-method
```text
<password>           : Password
 <public-key>         : Public key


uCPE-OS>config>mngmnt>login-user(netconf-su)# authentication-method
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


uCPE-OS>config>mngmnt>login-user(netconf-su)# level
```

### password
```text
<password>           : Password: non-hashed password [20 chars]; hashed [40 | 
                        144] [string]


uCPE-OS>config>mngmnt>login-user(netconf-su)# password
```

### public-key
```text
<public-key>         : Public key format: <inv comma> ssh-rsa <space> public 
                        key string <space> comment <inv comma> [1..512 chars]


uCPE-OS>config>mngmnt>login-user(netconf-su)# public-key
```

### shutdown
```text
<CR>

uCPE-OS>config>mngmnt>login-user(netconf-su)# shutdown
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


uCPE-OS>config>mngmnt>netconf# inactivity-timeout
```

### shutdown
```text
<CR>

uCPE-OS>config>mngmnt>netconf# shutdown
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

uCPE-OS>config>mngmnt>radius# clear-statistics
```

### server *(not entered — parameterized context)*
```text
<server-id>          : Specify  RADIUS server  [1..4]


uCPE-OS>config>mngmnt>radius# server
```

### show statistics
```text
<CR>

uCPE-OS>config>mngmnt>radius# show statistics
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


uCPE-OS>config>mngmnt>snmp# access-group

auto-create probe 'access-group zzz-hrvst' refused.
device response: access-group zzz-hrvst
#                                                  ^
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

uCPE-OS>config>mngmnt>snmp#
```

### bootstrap-notification
```text
<CR>

uCPE-OS>config>mngmnt>snmp# bootstrap-notification
```

### community *(not entered — parameterized context)*
```text
<community-index>    : Community index [string]


uCPE-OS>config>mngmnt>snmp# community
```

### config-change-notification
```text
<CR>

uCPE-OS>config>mngmnt>snmp# config-change-notification
```

### notify *(parameterized — inner help harvested under "configure management snmp notify NAME")*
```text
<notify-name>        : Notification group name [string]


uCPE-OS>config>mngmnt>snmp# notify
```

### notify-filter *(not entered — parameterized context)*
```text
<name>               : Notification group name [string]


uCPE-OS>config>mngmnt>snmp# notify-filter

auto-create probe 'notify-filter zzz-hrvst' refused.
device response: notify-filter zzz-hrvst
#                                                   ^
# cli error: parameter or keyword missing or wrong
 - notify-filter <name> <sub-tree-oid>
 - no notify-filter <name> <sub-tree-oid>
 <name>               : Notification group name [string]
 <sub-tree-oid>       : Sub-tree OID [1.3.6.1...]

uCPE-OS>config>mngmnt>snmp#
```

### notify-filter-profile *(parameterized — inner help harvested under "configure management snmp notify-filter-profile NAME")*
```text
<params-name>        : Parameter name [string]


uCPE-OS>config>mngmnt>snmp# notify-filter-profile
```

### security-to-group *(not entered — parameterized context)*
```text
<snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <usm>                : USM


uCPE-OS>config>mngmnt>snmp# security-to-group
```

### show snmpv3
```text
information

uCPE-OS>config>mngmnt>snmp# show snmpv3
```

### show trap-sync
```text
<CR>

uCPE-OS>config>mngmnt>snmp# show trap-sync
```

### snmp-engine-id
```text
<mac>                : MAC
 <ipv4>               : IPv4
 <ipv6>               : IPv6
 <text>               : Free text


uCPE-OS>config>mngmnt>snmp# snmp-engine-id
```

### target *(parameterized — inner help harvested under "configure management snmp target NAME")*
```text
<name>               : Target name [1..32 chars]


uCPE-OS>config>mngmnt>snmp# target
```

### target-params *(parameterized — inner help harvested under "configure management snmp target-params NAME")*
```text
<name>               : Target parameters name [1..32 chars]


uCPE-OS>config>mngmnt>snmp# target-params
```

### trap-sync-group *(not entered — parameterized context)*
```text
<group-id>           : Group ID [number] [1..10]


uCPE-OS>config>mngmnt>snmp# trap-sync-group
```

### user *(not entered — parameterized context)*
```text
<security-name>      : Security name [string]


uCPE-OS>config>mngmnt>snmp# user
```

### view *(not entered — parameterized context)*
```text
<view-name>          : View name [string]


uCPE-OS>config>mngmnt>snmp# view

auto-create probe 'view zzz-hrvst' refused.
device response: view zzz-hrvst
#                                          ^
# cli error: parameter or keyword missing or wrong
 - view <view-name> <sub-tree-oid>
 - no view <view-name> <sub-tree-oid>
 <view-name>          : View name [string]
 <sub-tree-oid>       : Subtree OID [1.3.6.1...]

uCPE-OS>config>mngmnt>snmp#
```

## configure management snmp notify NAME

Level help (`?`):
```text
[no] bind                           - Bind trap
 [no] shutdown                       - Disable notification group
      tag                            - Tag


uCPE-OS>config>mngmnt>snmp>notify(zzz-hrvst)$
```

### bind
```text
<systemTraceMsgPr*>  : 


uCPE-OS>config>mngmnt>snmp>notify(zzz-hrvst)$ bind
```

### shutdown
```text
<CR>

uCPE-OS>config>mngmnt>snmp>notify(zzz-hrvst)$ shutdown
```

### tag
```text
<argument>           : Tag [string]


uCPE-OS>config>mngmnt>snmp>notify(zzz-hrvst)$ tag
```

## configure management snmp notify-filter-profile NAME

Level help (`?`):
```text
profile-name                   - Profile name
 [no] shutdown                       - Disable notification group


uCPE-OS>config>mngmnt>snmp>filter-profile$
```

### profile-name
```text
<argument>           : Profile name [string]


uCPE-OS>config>mngmnt>snmp>filter-profile$ profile-name
```

### shutdown
```text
<CR>

uCPE-OS>config>mngmnt>snmp>filter-profile$ shutdown
```

## configure management snmp target NAME

Level help (`?`):
```text
address                        - Target address
 [no] tag-list                       - Configure tag list
      target-params                  - Target parameters
 [no] trap-sync-group                - Configure trap synchronization group


uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$
```

### address
```text
<udp-domain>         : UDP
 <oam-domain>         : OAM
 <udp-ipv4-domain>    : UDP over IPv4
 <udp-ipv6-domain>    : UDP over IPv6


uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$ address
```

### shutdown
```text
# cli error: Invalid Command
uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$ shutdown
```

### tag-list
```text
<list>               : Tag list [string]


uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$ tag-list
```

### target-params
```text
<params-name>        : Parameter [string]


uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$ target-params
```

### trap-sync-group
```text
<group-id>           : Group ID [number] [1..10]


uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$ trap-sync-group
```

## configure management snmp target-params NAME

Level help (`?`):
```text
message-processing-model       - Configure message processing model
      security                       - Configure security
      version                        - Configure SNMP version


uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$
```

### message-processing-model
```text
<snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <snmpv3>             : SNMPv3


uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$ message-processing-model
```

### security
```text
<CR>
 name
 level

uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$ security
```

### shutdown
```text
# cli error: Invalid Command
uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$ shutdown
```

### version
```text
<snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <usm>                : USM


uCPE-OS>config>mngmnt>snmp>target(zzz-hrvst)$ version
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


uCPE-OS>config>mngmnt>tacacsplus# group
```

### privilege-level
```text
<tacacs-privilege*>  : TACACS+ privilege level [0..15]


uCPE-OS>config>mngmnt>tacacsplus# privilege-level
```

### server *(not entered — parameterized context)*
```text
<ip>                 : TACACS+ server IP address [0.0.0.0|0:0:0:0::0]


uCPE-OS>config>mngmnt>tacacsplus# server
```

## configure management tacacsplus group NAME

Level help (`?`):
```text
[no] accounting                     - Enable TACACS+ accounting


uCPE-OS>config>mngmnt>tacacsplus>group(zzz-hrvst)$
```

### accounting
```text
<shell>              : Shell accounting
 <system>             : System accounting
 <commands>           : Commands accounting


uCPE-OS>config>mngmnt>tacacsplus>group(zzz-hrvst)$ accounting
```

## configure oam

Level help (`?`):
```text
twamp                          + TWAMP
```

## configure oam twamp

Level help (`?`):
```text
[no] controller                     + Create/configure/activate a TWAMP 
                                       controller
 [no] profile                        + Create/modify/delete a TWAMP test profile
 [no] responder                      + Create/configure/activate a TWAMP 
                                       responder
```

### controller *(parameterized — inner help harvested under "configure oam twamp controller NAME")*
```text
<name>               : Assign a meaningful name to the controller [1..32 chars]


uCPE-OS>config>oam>twamp# controller
```

### profile *(parameterized — inner help harvested under "configure oam twamp profile NAME")*
```text
<name>               : [string]


uCPE-OS>config>oam>twamp# profile
```

### responder *(parameterized — inner help harvested under "configure oam twamp responder NAME")*
```text
<name>               : Assign a meaningful name to the responder [1..32 chars]


uCPE-OS>config>oam>twamp# responder
```

## configure oam twamp controller NAME

Level help (`?`):
```text
local-ip-address               - 
 [no] peer                           + 
      router-entity                  - 
 [no] shutdown                       - 

 show status

uCPE-OS>config>oam>twamp>controller(zzz-hrvst)$
```

### bind
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>controller(zzz-hrvst)$ bind
```

### local-ip-address
```text
<ip-address>         : [0.0.0.0|0:0:0:0::0]


uCPE-OS>config>oam>twamp>controller(zzz-hrvst)$ local-ip-address
```

### router-entity
```text
<number>             : [number]


uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# router-entity
```

### show status
```text
<CR>

uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# show status
```

### shutdown
```text
<CR>

uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# shutdown
```

### vlan-tag
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# vlan-tag
```

## configure oam twamp controller NAME peer

Level help (`?`):
```text
local-ip-address               - 
 [no] peer                           + 
      router-entity                  - 
 [no] shutdown                       - 

 show status
```

### activate
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# activate
```

### calculation-mode
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# calculation-mode
```

### compatibility-mode
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# compatibility-mode
```

### responder-seq-num
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# responder-seq-num
```

### show report
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# show report
```

### show status
```text
<CR>

uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# show status
```

### show summary-report
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# show summary-report
```

### test-session
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>controller(zzz-hrvst)# test-session
```

## configure oam twamp profile NAME

Level help (`?`):
```text
delay-threshold                - Delay thresholdloss in micro-sec
      delay-variation-event-type     - Set delay variation event type to define 
                                       on which metric the delay threshold will 
                                       be operated
      delay-variation-threshold      - Delay variation thresholdloss in 
                                       micro-sec
      loss-ratio-threshold           - Loss Ratio Threshold in ppm (Packet Per 
                                       Million)
      loss-timeout                   - Loss timeout in micro-sec
      payload-length                 - Packets payload size in Bytes units
      transmit-rate                  - Packets transmit rate in PPS


uCPE-OS>config>oam>twamp>profile(zzz-hrvst)$
```

### delay-threshold
```text
<msec>               : Delay thresholdloss in micro-sec [1000..1000000, default
                         1000]


uCPE-OS>config>oam>twamp>profile(zzz-hrvst)$ delay-threshold
```

### delay-variation-event-type
```text
<pdv>                : 
 <ipdv>               : 


uCPE-OS>config>oam>twamp>profile(zzz-hrvst)$ delay-variation-event-type
```

### delay-variation-threshold
```text
<msec>               : Delay variation threshold in micro-sec [1000..1000000, 
                        default 1000]


uCPE-OS>config>oam>twamp>profile(zzz-hrvst)$ delay-variation-threshold
```

### loss-ratio-threshold
```text
<ppm>                : Loss Ratio Threshold in ppm (Packet Per Million) 
                        [1000..10000, default 1000]


uCPE-OS>config>oam>twamp>profile(zzz-hrvst)$ loss-ratio-threshold
```

### loss-timeout
```text
<msec>               : Loss timeout in micro-sec [1000000..50000000, default 
                        2000000]


uCPE-OS>config>oam>twamp>profile(zzz-hrvst)$ loss-timeout
```

### payload-length
```text
<bytes>              : Packets payload size in Bytes units [36..1472, default 
                        256]


uCPE-OS>config>oam>twamp>profile(zzz-hrvst)$ payload-length
```

### transmit-rate
```text
<pps>                : Packets transmit rate in PPS [1..10, default 10]


uCPE-OS>config>oam>twamp>profile(zzz-hrvst)$ transmit-rate
```

## configure oam twamp responder NAME

Level help (`?`):
```text
[no] fragment-mark                  - 
      local-ip-address               - 
 [no] reflector-timeout              - TWAMP test session inactivity timer
      router-entity                  - 
 [no] server-timeout                 - TWAMP control session inactivity timer
 [no] shutdown                       - 
      tcp-port                       - Defines TCP port number for the TWAMP 
                                       control session
 [no] tx-extended-info               - 
 [no] tx-seq-num                     - 

 show status

uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$
```

### bind
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ bind
```

### fragment-mark
```text
<CR>

uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ fragment-mark
```

### local-ip-address
```text
<ip-address>         : [0.0.0.0|0:0:0:0::0]


uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ local-ip-address
```

### reflector-timeout
```text
<seconds>            : Defines the TWAMP test session inactivity timeout 
                        [60..3600, default 900]


uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ reflector-timeout
```

### router-entity
```text
<number>             : [number]


uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ router-entity
```

### server-timeout
```text
<seconds>            : Defines the TWAMP control session inactivity timeout 
                        [60..3600, default 900]


uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ server-timeout
```

### show status
```text
<CR>

uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ show status
```

### shutdown
```text
<CR>

uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ shutdown
```

### tcp-port
```text
<number>             : Defines TCP port number for the TWAMP control session 
                        [862,1024..49151, default 862]


uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ tcp-port
```

### test-session
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ test-session
```

### tx-extended-info
```text
<CR>

uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ tx-extended-info
```

### tx-seq-num
```text
<CR>

uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ tx-seq-num
```

### vlan-tag
```text
# cli error: Invalid Command
uCPE-OS>config>oam>twamp>responder(zzz-hrvst)$ vlan-tag
```

## configure port

Level help (`?`):
```text
cellular                       + Create/Delete cellular interface
      ethernet                       + Specifies Ethernet parameters
 [no] jumbo-frames                   - Enable jumbo frames
 [no] ppp                            + 
      virtual                        + Virtual port level
 [no] wifi-country-code              - Configure WiFi country code
      wlan                           + Configure wlan interface

 show summary                        - Display port status summary
 show wifi
```

### cellular *(not entered — parameterized context)*
```text
<port-index>         : Index of cellular interface [port]


uCPE-OS>config>port# cellular
```

### ethernet *(parameterized — inner help harvested under "configure port ethernet NAME")*
```text
<port-index>         : Port number [port]


uCPE-OS>config>port# ethernet
```

### jumbo-frames
```text
<CR>

uCPE-OS>config>port# jumbo-frames
```

### ppp *(parameterized — inner help harvested under "configure port ppp NAME")*
```text
<port-number>        : PPP Port number [number]


uCPE-OS>config>port# ppp
```

### show summary
```text
<CR>

uCPE-OS>config>port# show summary
```

### show wifi
```text
<CR>

uCPE-OS>config>port# show wifi
```

### virtual *(not entered — parameterized context)*
```text
<port-number>        : Virtual port level [1..10]


uCPE-OS>config>port# virtual
```

### wifi-country-code
```text
<alpha-2-country-*>  : ISO 3166 two-letter country code [2..2 chars]


uCPE-OS>config>port# wifi-country-code
```

### wlan *(not entered — parameterized context)*
```text
<port-index>         : Index of wlan interface [port]


uCPE-OS>config>port# wlan
```

## configure port ethernet NAME

Level help (`?`):
```text
[no] access-group                   - Apply ACL to device management
 [no] classifier                     + Enables/disables classifier at the port 
                                       level
      clear-statistics               - Clears all statistics
      egress-mtu                     - Defines the max frame size to transmit
 [no] name                           - Assigns/removes a port name
 [no] pm-collection                  - Enable Performance Management (PM) 
 [no] policy-based-route             - Bind PBR rule to this entity
 [no] queue-group                    - 
 [no] shutdown                       - Administratively disables/enables the 
                                       port
 [no] traffic-class                  + Define a traffic-class entity
 [no] vlan                           + Configure vlan port

 show access-list-summary            - ACL Information
 show statistics                     - Displays the Ethernet port statistics
 show status                         - Displays the Ethernet port status
```

### access-group
```text
<acl-name>           : ACL to bind to the entity [1..80 chars]


uCPE-OS>config>port>eth(6)# access-group
```

### classifier *(not entered — parameterized context)*
```text
<ingress>            : 


uCPE-OS>config>port>eth(6)# classifier
```

### clear-statistics
```text
<CR>

uCPE-OS>config>port>eth(6)# clear-statistics
```

### egress-mtu
```text
<size>               : Specifies the Max Transition Unit size (bytes) 
                        [68..12288, default 1500]


uCPE-OS>config>port>eth(6)# egress-mtu
```

### name
```text
<string>             : Adds free text to assign a name to the port [1..64 
                        chars]


uCPE-OS>config>port>eth(6)# name
```

### pm-collection
```text
<interval>           : PM collection interval
 <on-interval-close>  : Collect PM only on interval close


uCPE-OS>config>port>eth(6)# pm-collection
```

### policy-based-route
```text
priority

uCPE-OS>config>port>eth(6)# policy-based-route
```

### queue-group
```text
profile

uCPE-OS>config>port>eth(6)# queue-group
```

### show access-list-summary
```text
<CR>

uCPE-OS>config>port>eth(6)# show access-list-summary
```

### show statistics
```text
<CR>

uCPE-OS>config>port>eth(6)# show statistics
```

### show status
```text
<CR>

uCPE-OS>config>port>eth(6)# show status
```

### shutdown
```text
<CR>

uCPE-OS>config>port>eth(6)# shutdown
```

### traffic-class *(parameterized — inner help harvested under "configure port ethernet NAME traffic-class NAME")*
```text
<tc-name>            : Traffic class name [1..32 chars]


uCPE-OS>config>port>eth(6)# traffic-class
```

### vlan *(not entered — parameterized context)*
```text
<vlan-id>            : Vlan id [1..4094]


uCPE-OS>config>port>eth(6)# vlan
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


uCPE-OS>config>port>eth(6)>traffic-class(zzz-hrvst)$
```

### cos
```text
<fixed>              : 


uCPE-OS>config>port>eth(6)>traffic-class(zzz-hrvst)$ cos
```

### mark
```text
<dscp-fixed>         : 


uCPE-OS>config>port>eth(6)>traffic-class(zzz-hrvst)$ mark
```

### shutdown
```text
<CR>

uCPE-OS>config>port>eth(6)>traffic-class(zzz-hrvst)$ shutdown
```

## configure port ppp NAME

Level help (`?`):
```text
[no] bind                           - 
 [no] chap-hostname                  - CHAP hostname
 [no] chap-password                  - CHAP password
 [no] name                           - Port name
 [no] pap-username                   - Configure PAP credentials
      pppoe                          + 
 [no] refuse-chap                    - Refuse CHAP authentication
 [no] refuse-no-auth                 - Refuse no authentication
 [no] refuse-pap                     - Refuse PAP authentication

 show status

uCPE-OS>config>port>ppp(1)$
```

### bind
```text
<cellular>           : 
 <ethernet>           : 


uCPE-OS>config>port>ppp(1)$ bind
```

### chap-hostname
```text
<name>               : [1..80 chars]


uCPE-OS>config>port>ppp(1)$ chap-hostname
```

### chap-password
```text
<password>           : [1..80 chars]


uCPE-OS>config>port>ppp(1)$ chap-password
```

### name
```text
<string>             : [1..80 chars]


uCPE-OS>config>port>ppp(1)$ name
```

### pap-username
```text
<name>               : [1..80 chars]


uCPE-OS>config>port>ppp(1)$ pap-username
```

### refuse-chap
```text
<CR>

uCPE-OS>config>port>ppp(1)# refuse-chap
```

### refuse-no-auth
```text
<CR>

uCPE-OS>config>port>ppp(1)# refuse-no-auth
```

### refuse-pap
```text
<CR>

uCPE-OS>config>port>ppp(1)# refuse-pap
```

### show status
```text
<CR>

uCPE-OS>config>port>ppp(1)# show status
```

## configure port ppp NAME pppoe

Level help (`?`):
```text
show status

uCPE-OS>config>port>ppp(1)>pppoe$
```

### show status
```text
<CR>

uCPE-OS>config>port>ppp(1)>pppoe$ show status
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


uCPE-OS>config>qos# queue-block-profile
```

### queue-group-profile *(parameterized — inner help harvested under "configure qos queue-group-profile NAME")*
```text
<profile-name>       : [1..32 chars]


uCPE-OS>config>qos# queue-group-profile
```

### shaper-profile *(parameterized — inner help harvested under "configure qos shaper-profile NAME")*
```text
<profile-name>       : [1..32 chars]


uCPE-OS>config>qos# shaper-profile
```

## configure qos queue-block-profile NAME

Level help (`?`):
```text
queue                          + Define queue parameters in queue block


uCPE-OS>config>qos>queue-block-profile(zzz-hrvst)$
```

## configure qos queue-block-profile NAME queue

Level help (`?`):
```text
queue                          + Define queue parameters in queue block
```

### bandwidth
```text
# cli error: Invalid Command
uCPE-OS>config>qos>queue-block-profile(zzz-hrvst)# bandwidth
```

### scheduling
```text
# cli error: Invalid Command
uCPE-OS>config>qos>queue-block-profile(zzz-hrvst)# scheduling
```

## configure qos queue-group-profile NAME

Level help (`?`):
```text
queue-block                    + Define queue blocks in queue group 
                                       structure


uCPE-OS>config>qos>queue-group-profile(zzz-hrvst)$
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
uCPE-OS>config>qos>queue-group-profile(zzz-hrvst)# profile
```

### shaper
```text
# cli error: Invalid Command
uCPE-OS>config>qos>queue-group-profile(zzz-hrvst)# shaper
```

## configure qos shaper-profile NAME

Level help (`?`):
```text
bandwidth                      - Bandwidth profile configuration


uCPE-OS>config>qos>shaper-profile(zzz-hrvst)$
```

### bandwidth
```text
cir

uCPE-OS>config>qos>shaper-profile(zzz-hrvst)$ bandwidth
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


uCPE-OS>config>reporting# acknowledge
```

### active-alarm-rebuild
```text
<CR>

 send-traps

uCPE-OS>config>reporting# active-alarm-rebuild
```

### alarm-cut-off
```text
<port>               : 


uCPE-OS>config>reporting# alarm-cut-off
```

### alarm-input
```text
<port-number>        : [number]


uCPE-OS>config>reporting# alarm-input
```

### alarm-output
```text
<port>               : 


uCPE-OS>config>reporting# alarm-output
```

### alarm-source-attribute
```text
<system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# alarm-source-attribute
```

### alarm-source-type-attribute
```text
<system>             : 
 <ethernet>           : 
 <gnss>               : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# alarm-source-type-attribute
```

### bind-alarm-source-to-relay
```text
<system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# bind-alarm-source-to-relay
```

### bind-alarm-to-relay
```text
<system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# bind-alarm-to-relay
```

### clear-accounting-log
```text
<CR>

uCPE-OS>config>reporting# clear-accounting-log
```

### clear-alarm-log
```text
<log>                : 
 <brief-log>          : 
 <activity-log>       : 
 <all-logs>           : 


uCPE-OS>config>reporting# clear-alarm-log
```

### log-file-timestamp-type
```text
<utc>                : 
 <local>              : 


uCPE-OS>config>reporting# log-file-timestamp-type
```

### mask-minimum-severity
```text
log
 snmp-trap
 led-relay
 popup
 vty-popup
 netconf-notification

uCPE-OS>config>reporting# mask-minimum-severity
```

### pm
```text
<CR>

uCPE-OS>config>reporting# pm
```

### pm-collection
```text
<eth>                : Ethernet
 <twamp>              : TWAMP sessions
 <system>             : Memory usage and CPU utilization


uCPE-OS>config>reporting# pm-collection
```

### show accounting-log
```text
<CR>

uCPE-OS>config>reporting# show accounting-log
```

### show active-alarms
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <all>                : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# show active-alarms
```

### show active-alarms-details
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <all>                : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# show active-alarms-details
```

### show alarm-information
```text
<system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# show alarm-information
```

### show alarm-input
```text
<CR>

uCPE-OS>config>reporting# show alarm-input
```

### show alarm-list
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 
 <all>                : 


uCPE-OS>config>reporting# show alarm-list
```

### show alarm-log
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <all>                : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# show alarm-log
```

### show alarm-outputs
```text
<CR>

uCPE-OS>config>reporting# show alarm-outputs
```

### show brief-alarm-log
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <all>                : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# show brief-alarm-log
```

### show brief-log
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <all>                : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# show brief-log
```

### show event-information
```text
<system>             : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# show event-information
```

### show event-list
```text
<CR>
 <system>             : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <all>                : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# show event-list
```

### show log
```text
<CR>
 <system>             : 
 <gnss>               : 
 <ethernet>           : 
 <bridge>             : 
 <bridge-port>        : 
 <router>             : 
 <router-interface>   : 
 <bgp>                : 
 <cellular>           : 
 <all>                : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <twamp-session>      : 
 <twamp-peer>         : 
 <tunnel>             : 
 <virt-image>         : 
 <virt-network>       : 
 <virt-instance>      : 
 <virt-volume>        : 


uCPE-OS>config>reporting# show log
```

### show log-summary
```text
<CR>
 <number-records>     : [number, default 10]


uCPE-OS>config>reporting# show log-summary
```

### soaking-time
```text
interval
 clear

uCPE-OS>config>reporting# soaking-time
```

## configure router NAME

Level help (`?`):
```text
[no] bgp                            + Configure BGP
      clear-arp-table                - Clear ARP table
      clear-neighbor-table           - Clear neighbor table
      dhcp-client                    + Configure DHCP client 
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
 show dns-resolver
 show neighbor-table                 - Show IPv6 neighbor table
 show rib
 show routing-table                  - Show routing table
 show summary-interface              - Show interface table
```

### bgp *(not entered — parameterized context)*
```text
<as-number>          : Set local AS [1..4294967295, default 0]


uCPE-OS>config>router(1)# bgp
```

### clear-arp-table
```text
<CR>

uCPE-OS>config>router(1)# clear-arp-table
```

### clear-neighbor-table
```text
<CR>

uCPE-OS>config>router(1)# clear-neighbor-table
```

### interface *(parameterized — inner help harvested under "configure router NAME interface NAME")*
```text
<number>             : Router interface number [number] [1..32]


uCPE-OS>config>router(1)# interface
```

### name
```text
<string>             : Router name [1..32 chars]


uCPE-OS>config>router(1)# name
```

### prefix-list *(not entered — parameterized context)*
```text
<name>               : Set prefix-list policy profile name. Profile name shall 
                        be unique in the system [1..252 chars]


uCPE-OS>config>router(1)# prefix-list

auto-create probe 'prefix-list zzz-hrvst' refused.
device response: prefix-list zzz-hrvst
#                                               ^
# cli error: parameter or keyword missing or wrong
 - prefix-list <name> {ipv4|ipv6}
 - no prefix-list <name>
 <name>               : Set prefix-list policy profile name. Profile name shall 
                        be unique in the system [1..252 chars]

uCPE-OS>config>router(1)#
```

### resequence
```text
<name>               : Policy profile to resequence [1..252 chars]


uCPE-OS>config>router(1)# resequence
```

### route-map *(parameterized — inner help harvested under "configure router NAME route-map NAME")*
```text
<name>               : Set route-map policy profile name. Profile name shall be
                         unique in the system. [1..252 chars]


uCPE-OS>config>router(1)# route-map
```

### show arp-table
```text
<CR>
 address

uCPE-OS>config>router(1)# show arp-table
```

### show dns-resolver
```text
<CR>

uCPE-OS>config>router(1)# show dns-resolver
```

### show neighbor-table
```text
<CR>
 address

uCPE-OS>config>router(1)# show neighbor-table
```

### show rib
```text
<ipv4>               : 
 <ipv6>               : 


uCPE-OS>config>router(1)# show rib
```

### show routing-table
```text
<CR>
 address
 protocol

uCPE-OS>config>router(1)# show routing-table
```

### show summary-interface
```text
<CR>

uCPE-OS>config>router(1)# show summary-interface
```

### static-route
```text
<address-mask>       : IP and mask [0.0.0.0/32|0:0:0:0::0/128]


uCPE-OS>config>router(1)# static-route
```

### tunnel-interface *(parameterized — inner help harvested under "configure router NAME tunnel-interface NAME")*
```text
<number>             : Tunnel number [number] [1..10]


uCPE-OS>config>router(1)# tunnel-interface
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
 <vendor-specific-*>  : Vendor Specific Information (option 17)


uCPE-OS>config>router(1)>dhcp-client# dhcpv6-option-request
```

### duid-type
```text
<en>                 : 
 <ll>                 : 


uCPE-OS>config>router(1)>dhcp-client# duid-type
```

### host-name
```text
<name>               : User specified name
 <sys-name>           : System defined name


uCPE-OS>config>router(1)>dhcp-client# host-name
```

### vendor-class-id
```text
<name>               : User specified name
 <ent-physical-name>  : System defined name


uCPE-OS>config>router(1)>dhcp-client# vendor-class-id
```

## configure router NAME interface NAME

Level help (`?`):
```text
[no] address                        - Configure router interface IP
 [no] bind                           - Bind router interface
 [no] crypto-map                     - 
 [no] dhcp                           - Enable DHCP client
      dhcp-client                    + Configure DHCP client 
 [no] dhcpv6-client                  - Enable DHCPv6 client
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

 show crypto-map-status
 show status                         - Show router interface status
```

### address
```text
<address-mask>       : Router interface IP and mask [0.0.0.0/32|0:0:0:0::0/128]


uCPE-OS>config>router(1)>interface(32)# address
```

### bind
```text
<ppp>                : PPP 
 <pcs>                : PCS 
 <ethernet>           : Ethernet 
 <virtual>            : Virtual
 <cellular>           : Cellular
 <wlan>               : Wlan


uCPE-OS>config>router(1)>interface(32)# bind
```

### crypto-map
```text
<name>               : [1..80 chars]


uCPE-OS>config>router(1)>interface(32)# crypto-map
```

### dhcp
```text
<CR>

uCPE-OS>config>router(1)>interface(32)# dhcp
```

### dhcpv6-client
```text
<CR>
 pd-name
 <rapid-commit>       : 


uCPE-OS>config>router(1)>interface(32)# dhcpv6-client
```

### dhcpv6-server
```text
<pool>               : 


uCPE-OS>config>router(1)>interface(32)# dhcpv6-server
```

### ip-forwarding
```text
<CR>

uCPE-OS>config>router(1)>interface(32)# ip-forwarding
```

### ipv6-address-prefix
```text
<prefix-name>        : [1..80 chars]


uCPE-OS>config>router(1)>interface(32)# ipv6-address-prefix
```

### ipv6-autoconfig
```text
<CR>

uCPE-OS>config>router(1)>interface(32)# ipv6-autoconfig
```

### management-access
```text
<allow-all>          : Allow all
 <allow-ping>         : Ping only


uCPE-OS>config>router(1)>interface(32)# management-access
```

### name
```text
<string>             : Router interface name [1..32 chars]


uCPE-OS>config>router(1)>interface(32)# name
```

### ospf *(not entered — parameterized context)*
```text
<CR>

uCPE-OS>config>router(1)>interface(32)# ospf
```

### router-advertisement
```text
<CR>

uCPE-OS>config>router(1)>interface(32)# router-advertisement
```

### show crypto-map-status
```text
<name>               : [1..80 chars]


uCPE-OS>config>router(1)>interface(32)# show crypto-map-status
```

### show status
```text
<CR>

uCPE-OS>config>router(1)>interface(32)# show status
```

### shutdown
```text
<CR>

uCPE-OS>config>router(1)>interface(32)# shutdown
```

### unreachables
```text
<CR>

uCPE-OS>config>router(1)>interface(32)# unreachables
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


uCPE-OS>config>router(1)>interface(32)>dhcp-client# client-id
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

uCPE-OS>config>router(1)>nat# clear-nat-statistics
```

### clear-nat-translations
```text
<CR>

uCPE-OS>config>router(1)>nat# clear-nat-translations
```

### nat-exclude-source-ip
```text
<source-ip>          : IP Address of source IP station [0.0.0.0]


uCPE-OS>config>router(1)>nat# nat-exclude-source-ip
```

### nat-inside-overload
```text
source

uCPE-OS>config>router(1)>nat# nat-inside-overload
```

### nat-inside-source-static
```text
<inside-ip>          : IP Address of Inside IP station [0.0.0.0]


uCPE-OS>config>router(1)>nat# nat-inside-source-static
```

### nat-inside-source-static-port
```text
<tcp>                : Indicate that the configured port number is associated 
                        with TCP 
 <udp>                : Indicate that the configured port number is associated 
                        with UDP 


uCPE-OS>config>router(1)>nat# nat-inside-source-static-port
```

### nat-timeout
```text
tcp
 udp
 others

uCPE-OS>config>router(1)>nat# nat-timeout
```

### show nat-statistics
```text
# cli error: Invalid Command
uCPE-OS>config>router(1)>nat# show nat-statistics
```

### show nat-translations
```text
<CR>

uCPE-OS>config>router(1)>nat# show nat-translations
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


uCPE-OS>config>router(1)>ospf# area
```

### external-preference
```text
<priority>           : Priority [1..255, default 110]


uCPE-OS>config>router(1)>ospf# external-preference
```

### internal-preference
```text
<priority>           : Priority [1..255, default 30]


uCPE-OS>config>router(1)>ospf# internal-preference
```

### redistribute
```text
<connected>          : Connected
 <static>             : Static
 <bgp>                : BGP


uCPE-OS>config>router(1)>ospf# redistribute
```

### router-id
```text
<ip>                 : Router ID (IP address format) [0.0.0.0]


uCPE-OS>config>router(1)>ospf# router-id
```

### show database
```text
<CR>

uCPE-OS>config>router(1)>ospf# show database
```

### show interface-table
```text
<CR>

uCPE-OS>config>router(1)>ospf# show interface-table
```

### show neighbor-table
```text
<CR>

uCPE-OS>config>router(1)>ospf# show neighbor-table
```

### shutdown
```text
<CR>

uCPE-OS>config>router(1)>ospf# shutdown
```

## configure router NAME route-map NAME

Level help (`?`):
```text
delete                         - Remove statement from policy profile
      deny                           - Add deny statement to policy profile
      permit                         - Add permit statement to policy profile
      remark                         - Add remark statement to policy profile


uCPE-OS>config>router(1)>route-map(zzz-hrvst)$
```

### delete
```text
<sequence>           : [number] [1..65535]


uCPE-OS>config>router(1)>route-map(zzz-hrvst)$ delete
```

### deny
```text
<CR>
 <match>              : 
 <sequence>           : 


uCPE-OS>config>router(1)>route-map(zzz-hrvst)$ deny
```

### permit
```text
<CR>
 <match>              : 
 <set>                : 
 <sequence>           : 


uCPE-OS>config>router(1)>route-map(zzz-hrvst)$ permit
```

### remark
```text
<description>        : [1..252 chars]


uCPE-OS>config>router(1)>route-map(zzz-hrvst)$ remark
```

## configure router NAME tunnel-interface NAME

Level help (`?`):
```text
clear-statistics               - Clears Tunnel statistics counters
 [no] crypto-map                     - 
 [no] ip-address                     - Configure tunnel IP address
 [no] ip-mtu                         - Configure tunnel IP MTU
 [no] name                           - Configure Tunnel name
 [no] shutdown                       - 
 [no] tunnel-destination             - Configure tunnel destination
 [no] tunnel-source                  - Configure tunnel source
 [no] tunnel-underlay-destination    - Configure GREoIPsec underlay destination
 [no] tunnel-underlay-source         - Configure GREoIPsec underlay source

 show crypto-map-status
 show status                         - Show tunnel status

uCPE-OS>config>router(1)>tunnel-interface(1)$
```

### backup
```text
# cli error: Invalid Command
uCPE-OS>config>router(1)>tunnel-interface(1)$ backup
```

### bind
```text
# cli error: Invalid Command
uCPE-OS>config>router(1)>tunnel-interface(1)$ bind
```

### clear-statistics
```text
<CR>

uCPE-OS>config>router(1)>tunnel-interface(1)$ clear-statistics
```

### crypto-map
```text
<name>               : [1..80 chars]


uCPE-OS>config>router(1)>tunnel-interface(1)$ crypto-map
```

### dscp
```text
# cli error: Invalid Command
uCPE-OS>config>router(1)>tunnel-interface(1)$ dscp
```

### ip-address
```text
<address-mask>       : Tunnel address [0.0.0.0/32|0:0:0:0::0/128]


uCPE-OS>config>router(1)>tunnel-interface(1)$ ip-address
```

### ip-mtu
```text
<bytes>              : MTU in bytes [number] [128..65535]


uCPE-OS>config>router(1)>tunnel-interface(1)$ ip-mtu
```

### key
```text
# cli error: Invalid Command
uCPE-OS>config>router(1)>tunnel-interface(1)$ key
```

### name
```text
<string>             : [1..64 chars]


uCPE-OS>config>router(1)>tunnel-interface(1)$ name
```

### show crypto-map-status
```text
<CR>
 <name>               : [1..80 chars]


uCPE-OS>config>router(1)>tunnel-interface(1)$ show crypto-map-status
```

### show status
```text
<CR>

uCPE-OS>config>router(1)>tunnel-interface(1)$ show status
```

### shutdown
```text
<CR>

uCPE-OS>config>router(1)>tunnel-interface(1)$ shutdown
```

### tunnel-destination
```text
<address>            : Destination address [0.0.0.0|0:0:0:0::0]


uCPE-OS>config>router(1)>tunnel-interface(1)$ tunnel-destination
```

### tunnel-source
```text
<address>            : Source address [0.0.0.0|0:0:0:0::0]
 router-interface

uCPE-OS>config>router(1)>tunnel-interface(1)$ tunnel-source
```

## configure system

Level help (`?`):
```text
[no] announcement                   - Post-login banner text
 [no] contact                        - Contact name
      date-and-time                  + Configure date and time
 [no] dhcp-server                    + DHCP server level state
 [no] dhcpv6-server                  + DHCPv6 server level
      hostname                       - Hostname type
      inventory                      - Specifies device inventory parameters
 [no] ip-domain-name                 - 
 [no] ip-host                        - 
 [no] location                       - Device location
 [no] login-message                  - Pre-login banner text
 [no] name                           - Device name
      syslog                         + Configure Syslog

 show copyright                      - Display copyright message
 show device-information             - Display device information
 show summary-inventory              - Displays a list with installed hardware 
                                        and software
 show system-date                    - Display date and time
 show tech-support                   - Executes a predefined series of commands
```

### announcement
```text
<message>            : 


uCPE-OS>config>system# announcement
```

### contact
```text
<contact-person>     : Contact name [0..255 chars, default contact person]


uCPE-OS>config>system# contact
```

### dhcp-server *(not entered — parameterized context)*
```text
<number>             : [1..1, default 1]


uCPE-OS>config>system# dhcp-server
```

### dhcpv6-server *(not entered — parameterized context)*
```text
<number>             : [1..1, default 1]


uCPE-OS>config>system# dhcpv6-server
```

### hostname
```text
<mac>                : 
 <string>             : 


uCPE-OS>config>system# hostname
```

### inventory
```text
<entity-index>       : Unique identifier for device inventory [number]


uCPE-OS>config>system# inventory
```

### ip-domain-name
```text
<name>               : [1..255 chars]


uCPE-OS>config>system# ip-domain-name
```

### ip-host
```text
<fqdn>               : [1..255 chars]


uCPE-OS>config>system# ip-host
```

### location
```text
<location-of-device> : Device location [0..255 chars, default the location of 
                        this device]


uCPE-OS>config>system# location
```

### login-message
```text
<message>            : 


uCPE-OS>config>system# login-message
```

### name
```text
<name-of-device>     : Device name [0..255 chars]


uCPE-OS>config>system# name
```

### show copyright
```text
<CR>

uCPE-OS>config>system# show copyright
```

### show device-information
```text
<CR>

uCPE-OS>config>system# show device-information
```

### show summary-inventory
```text
<CR>

uCPE-OS>config>system# show summary-inventory
```

### show system-date
```text
<CR>

uCPE-OS>config>system# show system-date
```

### show tech-support
```text
<CR>
 <file>               : 
 <terminal>           : Commands output is printed to terminal screen


uCPE-OS>config>system# show tech-support
```

### syslog *(not entered — parameterized context)*
```text
<device>             : Device
 <server>             : Server


uCPE-OS>config>system# syslog
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


uCPE-OS>config>system>date-time# date
```

### date-format
```text
<yyyy-mm-dd>         : yyyy-mm-dd
 <dd-mm-yyyy>         : dd-mm-yyyy
 <mm-dd-yyyy>         : mm-dd-yyyy 
 <yyyy-dd-mm>         : yyyy-dd-mm


uCPE-OS>config>system>date-time# date-format
```

### show summer-time
```text
<CR>

uCPE-OS>config>system>date-time# show summer-time
```

### summer-time
```text
<recurring>          : 
 <date>               : 


uCPE-OS>config>system>date-time# summer-time
```

### time
```text
<time>               : Set time [hh:mm[:ss]]


uCPE-OS>config>system>date-time# time
```

### zone
```text
<utc>                : Universal Time Coordinated


uCPE-OS>config>system>date-time# zone
```

## configure system date-and-time ntp

Level help (`?`):
```text
[no] server                         + NTP server level

 show status                         - NTP status
```

### server *(not entered — parameterized context)*
```text
<server-id>          : NTP server number [1..10]


uCPE-OS>config>system>date-time>ntp# server
```

### show status
```text
<CR>

uCPE-OS>config>system>date-time>ntp# show status
```

## configure terminal

Level help (`?`):
```text
baud-rate                      - Terminal baud rate
      console-timeout                - Specifies the time of inactivity after 
                                       which the device disconnects
      length                         - Configure terminal screen size (number of
                                        rows)
 [no] serial-port-disable            - Disable serial port
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


uCPE-OS>config>terminal# baud-rate
```

### console-timeout
```text
<forever>            : Disables disconnecting the device in case of inactivity
 <limited>            : Enables disconnecting the device in case of inactivity 
                        after a specified time period


uCPE-OS>config>terminal# console-timeout
```

### length
```text
<number-of-rows>     : Number of rows to print before pausing (or 0 for no 
                        pausing). [0..255, default 20]


uCPE-OS>config>terminal# length
```

### serial-port-disable
```text
<CR>

uCPE-OS>config>terminal# serial-port-disable
```

### timeout
```text
<forever>            : No timeout
 <limited>            : Enable timeout


uCPE-OS>config>terminal# timeout
```

## configure virtualization

Level help (`?`):
```text
clear-cpu-utilization          - Reset the CPU utilization counters
 [no] instance                       + Create/modify/delete a VNF
      management-mode                - Virtualization management mode
      repository                     + Manage virtualization re-usable 
                                       repositories
 [no] virtualization-dns-server      - 
 [no] virtualization-ip              - Virtualization component ip address

 show core-mapping                   - Display process mapping per physical 
                                        core or per thread
 show resources                      - Display system metrics for CPU, RAM and 
                                        disk 
 show summary-instance               - Display summary information for all 
                                        instances
 show system                         - Display system information
 show system-detail
```

### add-ons *(not entered — parameterized context)*
```text
# cli error: Invalid Command
uCPE-OS>config>virt# add-ons
```

### clear-cpu-utilization
```text
<CR>

uCPE-OS>config>virt# clear-cpu-utilization
```

### instance *(parameterized — inner help harvested under "configure virtualization instance NAME")*
```text
<name>               : [string]


uCPE-OS>config>virt# instance
```

### interface *(not entered — parameterized context)*
```text
# cli error: Invalid Command
uCPE-OS>config>virt# interface
```

### management-mode
```text
<or-vi-cli-netconf>  : 
 <or-vi-rest>         : 


uCPE-OS>config>virt# management-mode
```

### networking-mode
```text
# cli error: Invalid Command
uCPE-OS>config>virt# networking-mode
```

### show core-mapping
```text
<CR>

uCPE-OS>config>virt# show core-mapping
```

### show resources
```text
<CR>

uCPE-OS>config>virt# show resources
```

### show summary-instance
```text
<CR>

uCPE-OS>config>virt# show summary-instance
```

### show system
```text
<CR>

uCPE-OS>config>virt# show system
```

### show system-detail
```text
<CR>

uCPE-OS>config>virt# show system-detail
```

### virtualization-dns-server
```text
<ip-address>         : [0.0.0.0|0:0:0:0::0]


uCPE-OS>config>virt# virtualization-dns-server
```

### virtualization-gateway
```text
# cli error: Invalid Command
uCPE-OS>config>virt# virtualization-gateway
```

### virtualization-ip
```text
<address>            : 
 <interface>          : 


uCPE-OS>config>virt# virtualization-ip
```

## configure virtualization instance NAME

Level help (`?`):
```text
[no] core-pinning                   - Map a vCPU to physical core and thread
      description                    - Set a meaningful description for the VNF
 [no] flavor                         - Associate a previously defined flavor to 
                                       the VNF
 [no] image                          - Associate a previously defined image to 
                                       the VNF
 [no] init-config                    - Set initial configuration for the VNF
 [no] monitor                        - Configure VNF monitoring
 [no] network                        - Associate a previously defined network to
                                        the VNF
      remote-terminal                - Open a session to the VNF console
 [no] shutdown                       - Enable/disable the VNF
 [no] vnc                            - Enable / disable VNC

 show status                         - Display the status of the VNF

uCPE-OS>config>virt>instance(zzz-hrvst)$
```

### clear
```text
# cli error: Invalid Command
uCPE-OS>config>virt>instance(zzz-hrvst)$ clear
```

### core-pinning
```text
vcpu

uCPE-OS>config>virt>instance(zzz-hrvst)$ core-pinning
```

### create-snapshot
```text
# cli error: Invalid Command
uCPE-OS>config>virt>instance(zzz-hrvst)$ create-snapshot
```

### description
```text
<string>             : A textual description of the instance [string]


uCPE-OS>config>virt>instance(zzz-hrvst)$ description
```

### flavor
```text
<flavor-ref>         : The name of a previously defined flavor [1..32 chars]


uCPE-OS>config>virt>instance(zzz-hrvst)$ flavor
```

### image
```text
<image-ref>          : The name of a previously defined image [1..32 chars]


uCPE-OS>config>virt>instance(zzz-hrvst)$ image
```

### init-config
```text
sequence
 <user-data-file>     : 
 <user-data-text>     : 
 <inject-file>        : 
 <property>           : 
 <iso-file>           : 


uCPE-OS>config>virt>instance(zzz-hrvst)$ init-config
```

### monitor
```text
method

uCPE-OS>config>virt>instance(zzz-hrvst)$ monitor
```

### network
```text
<name>               : The name of a previously defined Network [string]


uCPE-OS>config>virt>instance(zzz-hrvst)$ network
```

### pause
```text
# cli error: Invalid Command
uCPE-OS>config>virt>instance(zzz-hrvst)$ pause
```

### reboot
```text
# cli error: Invalid Command
uCPE-OS>config>virt>instance(zzz-hrvst)$ reboot
```

### remote-terminal
```text
<CR>
 port

uCPE-OS>config>virt>instance(zzz-hrvst)$ remote-terminal
```

### replace-network
```text
# cli error: Invalid Command
uCPE-OS>config>virt>instance(zzz-hrvst)$ replace-network
```

### show resources
```text
# cli error: Invalid Command
uCPE-OS>config>virt>instance(zzz-hrvst)$ show resources
```

### show status
```text
<CR>

uCPE-OS>config>virt>instance(zzz-hrvst)$ show status
```

### shutdown
```text
<CR>

uCPE-OS>config>virt>instance(zzz-hrvst)$ shutdown
```

### stop
```text
# cli error: Invalid Command
uCPE-OS>config>virt>instance(zzz-hrvst)$ stop
```

### vnc
```text
password

uCPE-OS>config>virt>instance(zzz-hrvst)$ vnc
```

## configure virtualization repository

Level help (`?`):
```text
export-image                   - 
 [no] flavor                         - Create/modify/delete a VNF flavor
 [no] image                          - Create/delete a VNF image
 [no] network                        + Create/modify/delete a VL

 show flavors                        - Display status of all VIM flavors
 show images                         - Display status of all VIM images
```

### export-image
```text
<image-name>         : The name of the image which should be exported [string]


uCPE-OS>config>virt>repository# export-image
```

### flavor
```text
<name>               : Assign a meaningful name to the flavor [1..32 chars]


uCPE-OS>config>virt>repository# flavor
```

### image
```text
<name>               : Assign a meaningful name to the image [1..32 chars]


uCPE-OS>config>virt>repository# image
```

### network *(parameterized — inner help harvested under "configure virtualization repository network NAME")*
```text
<name>               : Assign a meaningful name to the network [1..32 chars]


uCPE-OS>config>virt>repository# network
```

### show flavors
```text
<CR>

uCPE-OS>config>virt>repository# show flavors
```

### show images
```text
<CR>

uCPE-OS>config>virt>repository# show images
```

## configure virtualization repository network NAME

Level help (`?`):
```text
admin-state                    - Enable/disable the network
      description                    - Set a meaningful description for the 
                                       network
 [no] subnet                         - Define a network subnet in CIDR notation
      type                           - Set the network type

 show status                         - Display the status of the network and 
                                        its components

uCPE-OS>config>virt>repository>network(zzz-hrvst)$
```

### admin-state
```text
<up>                 : 
 <down>               : 


uCPE-OS>config>virt>repository>network(zzz-hrvst)$ admin-state
```

### description
```text
<string>             : A textual description of the network [string]


uCPE-OS>config>virt>repository>network(zzz-hrvst)$ description
```

### show status
```text
<CR>

uCPE-OS>config>virt>repository>network(zzz-hrvst)$ show status
```

### subnet
```text
<name>               : A meaningful subnet name [1..32 chars]


uCPE-OS>config>virt>repository>network(zzz-hrvst)$ subnet
```

### type
```text
<local>              : 
 <flat>               : 
 <vlan>               : 


uCPE-OS>config>virt>repository>network(zzz-hrvst)$ type
```

## file

Level help (`?`):
```text
copy                           - Copy file
      delete                         - Delete file
      delete-from-folder             - Deletes a user file
      delete-user                    - Deletes a file from the device
 [no] description                    - Description of the file
      dir                            - Display file directory
      folder-dir                     - List of all user files
      user-file-dir                  - List of all user files in the device

 show banner-text                    - Display banner  
 show configuration-files            - Displays configuration files properties
 show copy                           - Display Copy progress
 show factory-default-config         - Display factory-default-config
 show file-details                   - Displays the details of the file
 show rollback-config                - Display rollback-config 
 show schedule-log                   - Display schedule-log  
 show startup-config                 - Display startup-config 
 show sw-pack                        - Display SW packs 
 show user-default-config            - Display user-default-config 
 show user-dir
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
      cn-backup-file
      sw-update-1
      sw-update-2
The maximum allowed length/range is:
      <username> [1..60 chars]
      <password> [1..60 chars]
      <file>     [1..96 chars]
      <port>     [1..65535]



uCPE-OS>file# copy
```

### delete
```text
<sw-pack-1>          : 
 <startup-config>     : 
 <user-default-con*>  : 
 <zero-touch-confi*>  : 
 <restore-point-co*>  : 
 <user-script>        : 
 <script-result>      : 


uCPE-OS>file# delete
```

### delete-from-folder
```text
<filename>           : [string]


uCPE-OS>file# delete-from-folder
```

### delete-user
```text
<filename>           : [string]


uCPE-OS>file# delete-user
```

### description
```text
<file-name>          : The name of the file [1..37 chars]


uCPE-OS>file# description
```

### dir
```text
<CR>

uCPE-OS>file# dir
```

### folder-dir
```text
<CR>

uCPE-OS>file# folder-dir
```

### show banner-text
```text
<CR>

uCPE-OS>file# show banner-text
```

### show configuration-files
```text
<CR>

uCPE-OS>file# show configuration-files
```

### show copy
```text
<CR>
 <summary>            : 


uCPE-OS>file# show copy
```

### show factory-default-config
```text
<CR>

uCPE-OS>file# show factory-default-config
```

### show file-details
```text
<filename>           : [string]


uCPE-OS>file# show file-details
```

### show rollback-config
```text
<CR>

uCPE-OS>file# show rollback-config
```

### show schedule-log
```text
<CR>

uCPE-OS>file# show schedule-log
```

### show startup-config
```text
<CR>

uCPE-OS>file# show startup-config
```

### show sw-pack
```text
<CR>

uCPE-OS>file# show sw-pack
```

### show user-default-config
```text
<CR>

uCPE-OS>file# show user-default-config
```

### show user-dir
```text
<filename>           : [string]


uCPE-OS>file# show user-dir
```

### user-file-dir
```text
<CR>

uCPE-OS>file# user-file-dir
```
