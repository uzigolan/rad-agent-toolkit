# etx2 CLI reference (harvested `?` help)

Captured live from etx2i (ETX-2I (Hw 0.2/D, Sw 6.8.5(1.116)) - FIRST live etx2 driver verification; industrial variant of the ETX-2 line) on 2026-07-09 by scripts/harvest_cli.py
(re-run `harvest` after firmware upgrades — it diffs and updates in place).
Every section is a CLI context: first the level `?` listing (commands +
descriptions), then per-command argument help (`<command> ?`). Sections
ending in NAME are parameterized contexts harvested through one instance
(an existing one, or a temp object created and rolled back) — NAME stands
for any instance. Entries marked *(not entered)* could not be harvested
safely — their inner structure is in command-tree-etx2.md; use
cli_help with a real index for inner argument syntax.

## <root>

Level help (`?`):
```text
admin                                   + Adminstrative commands
      clear-statistics                        - Clear all statistics
      configure                               + Configure device
      file                                    + File commands
      logon                                   - Logon as Debug user
      on-configuration-error                  - Behavior for configuration error

Global commands:
      copy                                    - Copy file
      echo                                    - Displays a line of text 
                                                (command) on the screen
      exec                                    - Execute script of CLI commands
      exit                                    - Returns to the next higher 
                                                command level (context)
      help                                    - Displays information regarding 
                                                commands in the current level
      history                                 - Displays the history of commands
                                                 issued since the last restart
      info                                    - Displays the current device 
                                                configuration
      level-info                              - Displays the current device 
                                                configuration - commands from 
                                                the current level only
      logout                                  - Logs the device off
      ping                                    - Ping
 [no] popup-suspend                           - Suspends popup messages
      save                                    - Save current settings
 [no] schedule                                - Schedule a command to run in a 
                                                future time
      telnet                                  - Open telnet client session
      trace-route                             - Traceroute
      tree                                    - Displays the command levels from
                                                 the current context downwards
```

### clear-statistics
```text
<CR>

ETX-2I# clear-statistics
```

### copy
```text
<source-file-url>                          : <file-url> = <url-prefix> <file>
<url-prefix> = 
      tftp://<ipv4-address>/
      tftp://[<ipv6-address>]/
      sftp://<username>:<password>@<ipv4-address>:<port>/
      sftp://<username>:<password>@[<ipv6-address>]:<port>/
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
      sw-pack-3
      sw-pack-4
      zero-touch-config-xml
      banner-text
      pm-0
      pm-csv
      db-schema
      mac-table
      db-config
      ltm_1
      ltm_2
      ltm_9
      schedule-log
      accounting-log
      sniffer-file
      user-script
      script-result
      ps-clei
The maximum allowed length/range is:
      <username> [1..32 chars]
      <password> [1..32 chars]
      <file>     [1..500 chars]
      <port>     [1..65535]



ETX-2I# copy
```

### echo
```text
<CR>
 <text-to-echo>                             : Text to display on screen [string]


ETX-2I# echo
```

### exec
```text
<user-script>                              : 


ETX-2I# exec
```

### exit
```text
<CR>
 <all>                                      : Returns to Device context


ETX-2I# exit
```

### help
```text
<CR>
 <command-name>                             : Command for which help is 
                                              requested [string]


ETX-2I# help
```

### history
```text
<CR>

ETX-2I# history
```

### info
```text
<CR>
 <detail>                                   : Adds information to every conf. 
                                              parameter


ETX-2I# info
```

### level-info
```text
<CR>
 <detail>                                   : Device configuration, including 
                                              defaults


ETX-2I# level-info
```

### logon
```text
<debug>                                    : Debug


ETX-2I# logon
```

### logout
```text
<CR>

ETX-2I# logout
```

### on-configuration-error
```text
<ignore>                                   : Ignore configuration error
 <stop>                                     : Stop at first error
 <reject>                                   : Reject, reboot and  load alternate
                                               configuration


ETX-2I# on-configuration-error
```

### ping
```text
<ip-address>                               : Destination IP [0.0.0.0|0:0:0:0::0
                                              |host-name]


ETX-2I# ping
```

### popup-suspend
```text
<CR>

ETX-2I# popup-suspend
```

### save
```text
<CR>

ETX-2I# save
```

### schedule
```text
<name>                                     : Schedule name [string]


ETX-2I# schedule
```

### telnet
```text
<ip-address>                               : Telnet destination IP address 
                                              [0.0.0.0|0:0:0:0::0]


ETX-2I# telnet
```

### trace-route
```text
<ip-address>                               : Destination IP [0.0.0.0|
                                              0:0:0:0::0]


ETX-2I# trace-route
```

### tree
```text
<CR>
 <detail>                                   : Available commands, current 
                                              context and downwards


ETX-2I# tree
```

## admin

Level help (`?`):
```text
[no] access-level                            - Set Minimum level allowed to 
                                                execute CLI command
 [no] auto-save                               - Enable/disable auto-save mode
      factory-default-all                     - Return to factory default and 
                                                reboot
      factory-default                         - Return to factory default 
                                                configuration and reboot
      force-reboot                            - Reboot the device 
                                                unconditionally
      license                                 + 
      reboot                                  - Reboot device
      scheduler                               + Scheduler control commands
      send                                    - Send message to all connected 
                                                CLI users
      software                                + Software installation
 [no] startup-confirm-required                - Require user confirmation after 
                                                reboot
      user-default                            - Return to user default 
                                                configuration and reboot

 show reboot                                  - Display scheduled reboot 
                                                 details
```

### access-level
```text
command

ETX-2I>admin# access-level
```

### auto-save
```text
<CR>

ETX-2I>admin# auto-save
```

### factory-default
```text
<CR>

ETX-2I>admin# factory-default
```

### factory-default-all
```text
<CR>

ETX-2I>admin# factory-default-all
```

### force-reboot
```text
<CR>

ETX-2I>admin# force-reboot
```

### reboot
```text
<CR>
 <in>                                       : 
 <at>                                       : 
 <cancel>                                   : 


ETX-2I>admin# reboot
```

### send
```text
<message>                                  : 


ETX-2I>admin# send
```

### show reboot
```text
<CR>

ETX-2I>admin# show reboot
```

### startup-confirm-required
```text
<CR>
 time-to-confirm
 rollback

ETX-2I>admin# startup-confirm-required
```

### user-default
```text
<CR>

ETX-2I>admin# user-default
```

## admin license

Level help (`?`):
```text
[no] license-enable                          - 

 show summary                                 - Display license status summary
```

### license-enable
```text
<tmfp>                                     : 
 <twamp>                                    : 


ETX-2I>admin>license# license-enable
```

### show summary
```text
<CR>

ETX-2I>admin>license# show summary
```

## admin scheduler

Level help (`?`):
```text
clear-finished-schedules                - Delete all finished schedules 
                                                from the database
      clear-schedule-log                      - Clear schedule log file

 show scheduler                               - Show all schedules
 show scheduler-details                       - Show all schedules with details
```

### clear-finished-schedules
```text
<CR>

ETX-2I>admin>scheduler# clear-finished-schedules
```

### clear-schedule-log
```text
<CR>

ETX-2I>admin>scheduler# clear-schedule-log
```

### show scheduler
```text
<CR>

ETX-2I>admin>scheduler# show scheduler
```

### show scheduler-details
```text
<CR>

ETX-2I>admin>scheduler# show scheduler-details
```

## admin software

Level help (`?`):
```text
install                                 - Install software and reboot
 [no] software-confirm-required               - Require user confirmation of 
                                                software after reboot
      undo-install                            - Return to restore point

 show status                                  - Show installation process
```

### install
```text
<sw-pack-1>                                : sw-pack-1
 <sw-pack-2>                                : sw-pack-2
 <sw-pack-3>                                : sw-pack-3
 <sw-pack-4>                                : sw-pack-4


ETX-2I>admin>software# install
```

### show status
```text
<CR>

ETX-2I>admin>software# show status
```

### software-confirm-required
```text
<CR>
 time-to-confirm

ETX-2I>admin>software# software-confirm-required
```

### undo-install
```text
<CR>

ETX-2I>admin>software# undo-install
```

## configure

Level help (`?`):
```text
access-control                          + Configure access control
 [no] bridge                                  + Configure bridge
      chassis                                 + Configure chassis
      cross-connect                           + 
      crypto                                  + Cryptography level
      etps                                    + 
      fault                                   + 
      flows                                   + 
      management                              + Device management commands
 [no] mirroring-session                       + 
      oam                                     + Configure OAM
 [no] peer                                    - Create/delete peer
      port                                    + Configure port
      protection                              + Defines protection mechanisms
      pwe                                     + Create/delete Psaudo-wire
      qos                                     + Quality of service
      reporting                               + 
 [no] router                                  + Configure router 
      service                                 + Defines Service parameters
      system                                  + Defines system parameters
      terminal                                + Configure terminal
      test                                    + 

 show cards-summary                           - Display card information
 show peer-summary
 show service-summary                         - Show list of defined services
```

### bridge *(parameterized — inner help harvested under "configure bridge NAME")*
```text
<number>                                   : Bridge number [number]


ETX-2I>config# bridge
```

### mirroring-session *(not entered — parameterized context)*
```text
<number>                                   : [number]


ETX-2I>config# mirroring-session
```

### peer
```text
<number>                                   : Number of configured peer [number]
                                               [1..64]


ETX-2I>config# peer
```

### router *(parameterized — inner help harvested under "configure router NAME")*
```text
<number>                                   : Router number [number] [1..10]


ETX-2I>config# router
```

### service *(not entered — parameterized context)*
```text
<name>                                     : Specifies the name of the service 
                                              [1..32 chars]


ETX-2I>config# service
```

### show cards-summary
```text
<CR>

ETX-2I>config# show cards-summary
```

### show peer-summary
```text
<CR>

ETX-2I>config# show peer-summary
```

### show service-summary
```text
<CR>

ETX-2I>config# show service-summary
```

## configure access-control

Level help (`?`):
```text
[no] access-list                             + Configure ACL
 [no] logging                                 - Set ACL logging interval
      resequence                              - Resequence ACL
```

### access-list *(not entered — parameterized context)*
```text
<ipv4>                                     : IPv4
 <ipv6>                                     : IPv6
 <acl-name>                                 : Access list name [1..80 chars]


ETX-2I>config>access-control# access-list
```

### logging
```text
access-list

ETX-2I>config>access-control# logging
```

### resequence
```text
access-list

ETX-2I>config>access-control# resequence
```

## configure bridge NAME

Level help (`?`):
```text
aging-time                              - Configure MAC aging time
      clear-mac-table                         - Clear MAC address table
 [no] duplicate-mac-rejection                 - Enables duplicate MAC rejection
 [no] filtering                               - Enable filtering forwarding mode
      mld-snooping                            + Configure MLD snooping
 [no] name                                    - Configure bridge name
 [no] port                                    + Configure bridge port
      spanning-tree                           + Spanning tree level
 [no] static-mac                              - Configure static MAC
 [no] vlan                                    + Configure VLAN
 [no] vlan-aware                              - Enable VLAN aware mode

 show mac-address-table                       - Display MAC address table
 show mac-table                               - Display MAC address table
 show vlans                                   - Display VLAN membership
```

### aging-time
```text
<seconds>                                  : MAC aging time (seconds) [number, 
                                              default 300] [60..3000]


ETX-2I>config>bridge(1)# aging-time
```

### clear-mac-table
```text
<CR>

ETX-2I>config>bridge(1)# clear-mac-table
```

### duplicate-mac-rejection
```text
<enable>                                   : 
 <alarm-only>                               : 


ETX-2I>config>bridge(1)# duplicate-mac-rejection
```

### filtering
```text
<CR>

ETX-2I>config>bridge(1)# filtering
```

### mode
```text
# cli error: Invalid Command
ETX-2I>config>bridge(1)# mode
```

### name
```text
<bridge-name>                              : Bridge name [1..32 chars]


ETX-2I>config>bridge(1)# name
```

### port *(not entered — parameterized context)*
```text
<port-number>                              : Bridge port number [number] 
                                              [1..44]


ETX-2I>config>bridge(1)# port
```

### root
```text
# cli error: Invalid Command
ETX-2I>config>bridge(1)# root
```

### show mac-address-table
```text
<static>                                   : Static MAC addresses
 <dynamic>                                  : Dynamic MAC addresses
 <all>                                      : All MAC addresses


ETX-2I>config>bridge(1)# show mac-address-table
```

### show mac-table
```text
<CR>
 vlan
 mac-address

ETX-2I>config>bridge(1)# show mac-table
```

### show vlans
```text
<CR>

ETX-2I>config>bridge(1)# show vlans
```

### static-mac
```text
<vlan-id>                                  : VLAN ID [1..4094]


ETX-2I>config>bridge(1)# static-mac
```

### vlan *(not entered — parameterized context)*
```text
<vlan-id>                                  : VLAN ID [1..4094]


ETX-2I>config>bridge(1)# vlan
```

### vlan-aware
```text
<CR>

ETX-2I>config>bridge(1)# vlan-aware
```

## configure bridge NAME mld-snooping

Level help (`?`):
```text
host-aging-interval                     - Configure host aging interval
      router-aging-interval                   - Configure router aging interval
 [no] shutdown                                - Disable/Enable MLD snooping
 [no] static-group                            - Configure static multicast group
 [no] static-router-port                      - Configure static router ports
 [no] vlan                                    - Configure MLD snooping VLANs

 show status                                  - Display MLD snooping status
```

### host-aging-interval
```text
<seconds>                                  : Host aging interval (seconds) 
                                              [3..11264, default 260]


ETX-2I>config>bridge(1)>mld-snooping# host-aging-interval
```

### router-aging-interval
```text
<seconds>                                  : Router aging interval (seconds) 
                                              [3..11264, default 260]


ETX-2I>config>bridge(1)>mld-snooping# router-aging-interval
```

### show status
```text
<CR>

ETX-2I>config>bridge(1)>mld-snooping# show status
```

### shutdown
```text
<CR>

ETX-2I>config>bridge(1)>mld-snooping# shutdown
```

### static-group
```text
<group-address>                            : Multicast group IP address 
                                              [0:0:0:0::0]


ETX-2I>config>bridge(1)>mld-snooping# static-group
```

### static-router-port
```text
vlan

ETX-2I>config>bridge(1)>mld-snooping# static-router-port
```

### vlan
```text
<vlan-list>                                : MLD snooping VLANs [n1..n2,n3]


ETX-2I>config>bridge(1)>mld-snooping# vlan
```

## configure bridge NAME spanning-tree

Level help (`?`):
```text
forward-time                            - Configure forward delay
      hello-time                              - Configure time between hello 
                                                messages
      max-age                                 - Configure maximum aging
      mode                                    - Select RSTP/MSTP
      priority                                - Configure bridge priority
      tx-hold-count                           - Configure transmission hold 
                                                count

 show status                                  - Display spanning tree status
```

### forward-time
```text
<seconds>                                  : Forward delay (seconds) [4..30, 
                                              default 15]


ETX-2I>config>bridge(1)>spanning-tree# forward-time
```

### hello-time
```text
<seconds>                                  : Time between hello messages 
                                              (seconds) [1..10, default 2]


ETX-2I>config>bridge(1)>spanning-tree# hello-time
```

### max-age
```text
<seconds>                                  : Maximum aging (seconds) [6..40, 
                                              default 20]


ETX-2I>config>bridge(1)>spanning-tree# max-age
```

### max-hops
```text
# cli error: Invalid Command
ETX-2I>config>bridge(1)>spanning-tree# max-hops
```

### mode
```text
<mstp>                                     : MSTP
 <rstp>                                     : RSTP


ETX-2I>config>bridge(1)>spanning-tree# mode
```

### mst *(not entered — parameterized context)*
```text
# cli error: Invalid Command
ETX-2I>config>bridge(1)>spanning-tree# mst
```

### name
```text
# cli error: Invalid Command
ETX-2I>config>bridge(1)>spanning-tree# name
```

### priority
```text
<0>                                        : 0
 <4096>                                     : 4096
 <8192>                                     : 8192
 <12288>                                    : 12288
 <16384>                                    : 16384
 <20480>                                    : 20480
 <24576>                                    : 24576
 <28672>                                    : 28672
 <32768>                                    : 32768
 <36864>                                    : 36864
 <40960>                                    : 40960
 <45056>                                    : 45056
 <49152>                                    : 49152
 <53248>                                    : 53248
 <57344>                                    : 57344
 <61440>                                    : 61440


ETX-2I>config>bridge(1)>spanning-tree# priority
```

### revision-level
```text
# cli error: Invalid Command
ETX-2I>config>bridge(1)>spanning-tree# revision-level
```

### show status
```text
<CR>

ETX-2I>config>bridge(1)>spanning-tree# show status
```

### tx-hold-count
```text
<number>                                   : Tx hold count (BPDUs per second) 
                                              [1..10, default 6]


ETX-2I>config>bridge(1)>spanning-tree# tx-hold-count
```

## configure chassis

Level help (`?`):
```text
[no] overheat-auto-shutdown                  - Enables the overheat auto 
                                                shutdown feature. Shuts down 
                                                I/F's upon device overheating
      temperature-threshold                   - Configure temprature thresholds

 show environment                             - Display hardware status
```

### overheat-auto-shutdown
```text
<CR>

ETX-2I>config>chassis# overheat-auto-shutdown
```

### show environment
```text
<CR>

ETX-2I>config>chassis# show environment
```

### temperature-threshold
```text
<celsius>                                  : 
 <fahrenheit>                               : 


ETX-2I>config>chassis# temperature-threshold
```

## configure cross-connect

Level help (`?`):
```text
[no] pw-tdm                                  - TDM virtual circuit cross 
                                                connect
```

### pw-tdm
```text
pw

ETX-2I>config>cross-connect# pw-tdm
```

## configure crypto

Level help (`?`):
```text
[no] ca                                      + Add or remove a CA
 [no] crypto-map                              + Configure crypto map
 [no] ipsec-transform-set                     + Configure IPsec phase 2 policy
      isakmp-identity                         - Configure IKE identity type
 [no] isakmp-key                              - Configure IKE pre-shared key
 [no] isakmp-policy                           + Configure IPsec phase 1 policy
      key                                     + RSA key management level
      pki                                     + PKI (public key infrastructure) 
                                                level
```

### ca *(parameterized — inner help harvested under "configure crypto ca NAME")*
```text
<ca-name>                                  : CA name [1..20 chars]


ETX-2I>config>crypto# ca
```

### crypto-map *(parameterized — inner help harvested under "configure crypto crypto-map NAME")*
```text
<name>                                     : [1..80 chars]


ETX-2I>config>crypto# crypto-map
```

### ipsec-transform-set *(parameterized — inner help harvested under "configure crypto ipsec-transform-set NAME")*
```text
<name>                                     : [1..80 chars]


ETX-2I>config>crypto# ipsec-transform-set
```

### isakmp-identity
```text
<address>                                  : 
 <hostname>                                 : 


ETX-2I>config>crypto# isakmp-identity
```

### isakmp-key
```text
<pre-shared-key>                           : IKE pre-shared key [1..255 chars]


ETX-2I>config>crypto# isakmp-key
```

### isakmp-policy *(not entered — parameterized context)*
```text
<sequence>                                 : [number]


ETX-2I>config>crypto# isakmp-policy
```

## configure crypto ca NAME

Level help (`?`):
```text
[no] ocsp                                    - 
      revocation-check                        - 


ETX-2I>config>crypto>ca(zzz-hrvst)$
```

### ocsp
```text
<url>                                      : 


ETX-2I>config>crypto>ca(zzz-hrvst)$ ocsp
```

### revocation-check
```text
<crl>                                      : 
 <none>                                     : 
 <ocsp>                                     : 


ETX-2I>config>crypto>ca(zzz-hrvst)$ revocation-check
```

## configure crypto crypto-map NAME

Level help (`?`):
```text
ike-identity-local                      - Local IKE identity
      ike-identity-remote                     - Remote IKE identity
      ike-sa-lifetime                         - Configure SA lifetime
      ike-sa-negotiation                      - Configure SA negotiation mode
 [no] match-address                           - Assign ACL
 [no] match-destination                       - 
 [no] match-source                            - 
 [no] peer-address                            - Configure IPsec peer IP address
 [no] pfs-group                               - Configure PFS group
 [no] sa-lifetime                             - Configure SA lifetime
 [no] sequence-number                         - Configure crypto map priority
 [no] transform-set                           - Assign IPsec phase 2 policy


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$
```

### ike-identity-local
```text
<default-address>                          : 
 <address>                                  : 
 <default-hostname>                         : 
 <hostname>                                 : 


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-local
```

### ike-identity-remote
```text
<default-address>                          : 
 <address>                                  : 
 <hostname>                                 : 


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ ike-identity-remote
```

### ike-sa-lifetime
```text
<seconds>                                  : [60..86400, default 86400]


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ ike-sa-lifetime
```

### ike-sa-negotiation
```text
<main>                                     : 
 <aggressive>                               : 


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ ike-sa-negotiation
```

### match-address
```text
<name>                                     : [1..80 chars]


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ match-address
```

### match-destination
```text
address

ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ match-destination
```

### match-source
```text
<address>                                  : 
 <interface>                                : 


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ match-source
```

### peer-address
```text
<ip-address>                               : [0.0.0.0|0:0:0:0::0, default 
                                              0.0.0.0]


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ peer-address
```

### pfs-group
```text
<1>                                        : 
 <2>                                        : 
 <5>                                        : 
 <14>                                       : 
 <19>                                       : 
 <20>                                       : 


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ pfs-group
```

### sa-lifetime
```text
seconds
 kilobytes

ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ sa-lifetime
```

### sequence-number
```text
<number>                                   : [1..1000, default 10]


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ sequence-number
```

### transform-set
```text
<name-1>                                   : [1..80 chars]


ETX-2I>config>crypto>crypto-map(zzz-hrvst)$ transform-set
```

## configure crypto ipsec-transform-set NAME

Level help (`?`):
```text
algorithms                              - Configure IPsec phase 2 
                                                algorithms
      mode                                    - Tunnel or transport mode


ETX-2I>config>crypto>ipsec-transform-set(zzz-hrvst)$
```

### algorithms
```text
<esp-aes-cbc-128>                          : 
 <esp-aes-cbc-256>                          : 
 <esp-aes-gcm-128>                          : 
 <esp-aes-gcm-256>                          : 
 <esp-null>                                 : 
 <esp-aes-gmac-128>                         : 
 <esp-aes-gmac-256>                         : 


ETX-2I>config>crypto>ipsec-transform-set(zzz-hrvst)$ algorithms
```

### mode
```text
<tunnel>                                   : 
 <transport>                                : 


ETX-2I>config>crypto>ipsec-transform-set(zzz-hrvst)$ mode
```

## configure crypto key

Level help (`?`):
```text
generate-rsa                            - Generate RSA key pair

 show public-key-rsa                          - Display self RSA public key
```

### generate-rsa
```text
<CR>
 label
 size
 application


ETX-2I>config>crypto>key# generate-rsa
```

### show public-key-rsa
```text
<CR>

ETX-2I>config>crypto>key# show public-key-rsa
```

## configure crypto pki

Level help (`?`):
```text
authenticate                            - Authenticate CA by importing its
                                                 certificate
      delete-certificate                      - Delete certificate
      enroll                                  - Create CSR for enrollment by CA
      import-certificate                      - Import certificate

 show certificate                             - Display certificates stored in 
                                                 the device
 show certificate-summary                     - Display the device certificates
```

### authenticate
```text
<CR>
 <tftp>                                     : 


ETX-2I>config>crypto>pki# authenticate
```

### delete-certificate
```text
<self>                                     : 
 <ca>                                       : 


ETX-2I>config>crypto>pki# delete-certificate
```

### enroll
```text
<CR>
 <tftp>                                     : 


ETX-2I>config>crypto>pki# enroll
```

### import-certificate
```text
<CR>
 <tftp>                                     : 


ETX-2I>config>crypto>pki# import-certificate
```

### show certificate
```text
<self>                                     : 
 <ca>                                       : 


ETX-2I>config>crypto>pki# show certificate
```

### show certificate-summary
```text
<self>                                     : 
 <ca>                                       : 
 <all>                                      : 


ETX-2I>config>crypto>pki# show certificate-summary
```

## configure etps

Level help (`?`):
```text
[no] etp                                     + EVC termination point
```

### etp *(parameterized — inner help harvested under "configure etps etp NAME")*
```text
<name>                                     : unique name assigned to the ETP 
                                              [string]


ETX-2I>config>etps# etp
```

## configure etps etp NAME

Level help (`?`):
```text
clear-statistics                        - 
 [no] port                                    + Specifies ETP port parameters
 [no] protection                              + 

 show flows-summary
 show statistics
 show status

ETX-2I>config>etps>etp(zzz-hrvst)$
```

### clear-statistics
```text
<CR>

ETX-2I>config>etps>etp(zzz-hrvst)$ clear-statistics
```

### show flows-summary
```text
<CR>

ETX-2I>config>etps>etp(zzz-hrvst)# show flows-summary
```

### show statistics
```text
<running>                                  : 


ETX-2I>config>etps>etp(zzz-hrvst)# show statistics
```

### show status
```text
<CR>

ETX-2I>config>etps>etp(zzz-hrvst)# show status
```

## configure etps etp NAME port

Level help (`?`):
```text
clear-statistics                        - 
 [no] port                                    + Specifies ETP port parameters
 [no] protection                              + 

 show flows-summary
 show statistics
 show status
```

### loopback
```text
# cli error: Invalid Command
ETX-2I>config>etps>etp(zzz-hrvst)# loopback
```

### name
```text
# cli error: Invalid Command
ETX-2I>config>etps>etp(zzz-hrvst)# name
```

### show loopback
```text
# cli error: Invalid Command
ETX-2I>config>etps>etp(zzz-hrvst)# show loopback
```

### show status
```text
<CR>

ETX-2I>config>etps>etp(zzz-hrvst)# show status
```

### shutdown
```text
# cli error: Invalid Command
ETX-2I>config>etps>etp(zzz-hrvst)# shutdown
```

## configure etps etp NAME protection

Level help (`?`):
```text
[no] aps-protocol                            - 
 [no] bind                                    - Adds/removes working and 
                                                protection ports to/from the APS
      clear                                   - Clears the current command 
                                                (Force Switch or Lockout)
      force-switch                            - Switches traffic from the active
                                                 link to the next one even if it
                                                 is down
      lockout                                 - Prevents a possible switch over 
                                                (in 1+1 Bi-Optimized 
                                                Bidirectional mode) 
      manual-switch                           - Switches traffic from the active
                                                 link to the next one only if it
                                                 is not down
 [no] master-etp                              - 
      mode                                    - Specifies the APS operation mode
 [no] revertive                               - Enables/disables reverting 
                                                working port and protection port
 [no] sf-trigger                              - Signal Fail from different 
                                                sources
 [no] shutdown                                - Enable / Disable the ETP 
                                                Protection
      wait-to-restore                         - Wait to Restore Timer

 show status
```

### bind
```text
<protection>                               : Defines the port as protection 
                                              port
 <working>                                  : Defines the port as working port


ETX-2I>config>etps>etp(zzz-hrvst)>protection# bind
```

### master-etp
```text
<etp-name>                                 : [string]


ETX-2I>config>etps>etp(zzz-hrvst)>protection# master-etp
```

### show status
```text
<CR>

ETX-2I>config>etps>etp(zzz-hrvst)>protection# show status
```

### shutdown
```text
<CR>

ETX-2I>config>etps>etp(zzz-hrvst)>protection# shutdown
```

## configure fault

Level help (`?`):
```text
cfm                                     + 
 [no] fault-propagation                       + Fault propagation configuration
```

### fault-propagation *(not entered — parameterized context)*
```text
<port>                                     : 
 <mep>                                      : 
 <etp>                                      : 
 <router-interface>                         : 
 <bfd>                                      : 
 <twamp-session>                            : 


ETX-2I>config>fault# fault-propagation
```

## configure fault cfm

Level help (`?`):
```text
[no] service                                 +
```

### service *(not entered — parameterized context)*
```text
md

ETX-2I>config>fault>cfm# service
```

## configure flows

Level help (`?`):
```text
[no] classifier-profile                      + 
      clear-flow-mac-table                    - Clears MAC address table
 [no] flow                                    + 
      rate-sampling-window                    - 
      rename                                  - Rename flow or classifier
 [no] service-ping                            - Service Ping Request
 [no] service-ping-response                   - Service Ping Response
 [no] statistics-count-oam                    - 

 show service-ping-status                     - Display the status of the 
                                                 service-ping
 show summary
```

### classifier-profile *(not entered — parameterized context)*
```text
<classification-name>                      : [1..32 chars]


ETX-2I>config>flows# classifier-profile
```

### clear-flow-mac-table
```text
<CR>

ETX-2I>config>flows# clear-flow-mac-table
```

### flow *(parameterized — inner help harvested under "configure flows flow NAME")*
```text
<flow-name>                                : [1..64 chars]


ETX-2I>config>flows# flow
```

### rate-sampling-window
```text
<argument>                                 : Window size for sampling rate 
                                              statistics [Min.] [1..30, default 
                                              15]


ETX-2I>config>flows# rate-sampling-window
```

### rename
```text
<flow>                                     : 
 <classifier>                               : 


ETX-2I>config>flows# rename
```

### service-ping
```text
local-ip

ETX-2I>config>flows# service-ping
```

### service-ping-response
```text
local-ip

ETX-2I>config>flows# service-ping-response
```

### show service-ping-status
```text
<CR>

ETX-2I>config>flows# show service-ping-status
```

### show summary
```text
<details>                                  : 
 <brief>                                    : 


ETX-2I>config>flows# show summary
```

### statistics-count-oam
```text
<CR>

ETX-2I>config>flows# statistics-count-oam
```

## configure flows flow NAME

Level help (`?`):
```text
[no] classifier                              - 
 [no] cos-mapping                             - 
 [no] drop                                    - 
 [no] egress-port                             - 
      ingress-color                           - 
 [no] ingress-port                            - 
 [no] l2cp                                    - 
 [no] mac-learning                            - Invoke MAC address learning for 
                                                specific flow
 [no] mark                                    + 
 [no] marking-profile                         - 
 [no] multi-cos-counters                      - 
 [no] pm-collection                           - Enable Performance Management 
                                                (PM)
 [no] policer                                 - 
 [no] rate-measure                            - Beginning the measurement of the
                                                 port rate
      rate-sampling-window                    - 
 [no] reverse-direction                       - 
 [no] service-name                            - 
 [no] shutdown                                - Enable/disable the flow
 [no] test                                    - This command puts the specified 
                                                port into a loopback mode. The 
                                                no form of the command disables 
                                                the s
 [no] vlan-tag                                - 

 show rate
 show status
 show test
```

### classifier
```text
<classification-name>                      : [1..32 chars]


ETX-2I>config>flows>flow# classifier
```

### clear-statistics
```text
# cli error: Invalid Command
ETX-2I>config>flows>flow# clear-statistics
```

### drop
```text
<CR>

ETX-2I>config>flows>flow# drop
```

### egress-port
```text
<ethernet>                                 : 
 <logical-mac>                              : 
 <pcs>                                      : 
 <svi>                                      : 
 <etp>                                      : 
 <bridge-port>                              : 
 <int-ethernet>                             : 


ETX-2I>config>flows>flow# egress-port
```

### ingress-color
```text
<green>                                    : 
 <yellow>                                   : 
 <profile>                                  : 


ETX-2I>config>flows>flow# ingress-color
```

### l2cp
```text
profile

ETX-2I>config>flows>flow# l2cp
```

### mac-learning
```text
<CR>

ETX-2I>config>flows>flow# mac-learning
```

### marking-profile
```text
<marking-profile-name>                     : [1..32 chars]


ETX-2I>config>flows>flow(mng_access_defa)# marking-profile
```

### multi-cos-counters
```text
<cos-list>                                 : [0..7]


ETX-2I>config>flows>flow(mng_access_defa)# multi-cos-counters
```

### pm-collection
```text
<interval>                                 : PM collection interval
 <on-interval-close>                        : Collect PM only on interval close


ETX-2I>config>flows>flow(mng_access_defa)# pm-collection
```

### policer
```text
<profile>                                  : 
 <aggregate>                                : 
 <envelope>                                 : 


ETX-2I>config>flows>flow(mng_access_defa)# policer
```

### rate-measure
```text
interval

ETX-2I>config>flows>flow(mng_access_defa)# rate-measure
```

### rate-sampling-window
```text
<minutes>                                  : Window size for sampling rate 
                                              statistics [Min.] [number]


ETX-2I>config>flows>flow(mng_access_defa)# rate-sampling-window
```

### reverse-direction
```text
<CR>
 <block>                                    : 


ETX-2I>config>flows>flow(mng_access_defa)# reverse-direction
```

### service-name
```text
<name>                                     : [1..32 chars]


ETX-2I>config>flows>flow(mng_access_defa)# service-name
```

### show rate
```text
<CR>

ETX-2I>config>flows>flow(mng_access_defa)# show rate
```

### show statistics
```text
# cli error: Invalid Command
ETX-2I>config>flows>flow(mng_access_defa)# show statistics
```

### show status
```text
<CR>

ETX-2I>config>flows>flow(mng_access_defa)# show status
```

### show test
```text
<CR>

ETX-2I>config>flows>flow(mng_access_defa)# show test
```

### shutdown
```text
<CR>

ETX-2I>config>flows>flow(mng_access_defa)# shutdown
```

### test
```text
<CR>
 <mac-swap>                                 : 
 <ip-swap>                                  : 
 duration ttl-force

ETX-2I>config>flows>flow(mng_access_defa)# test
```

### vlan-tag
```text
<push>                                     : 
 <pop>                                      : 


ETX-2I>config>flows>flow(mng_access_defa)# vlan-tag
```

## configure flows flow NAME mark

Level help (`?`):
```text
[no] classifier                              - 
 [no] cos-mapping                             - 
 [no] drop                                    - 
 [no] egress-port                             - 
      ingress-color                           - 
 [no] ingress-port                            - 
 [no] l2cp                                    - 
 [no] mac-learning                            - Invoke MAC address learning for 
                                                specific flow
 [no] mark                                    + 
 [no] marking-profile                         - 
 [no] multi-cos-counters                      - 
 [no] pm-collection                           - Enable Performance Management 
                                                (PM)
 [no] policer                                 - 
 [no] rate-measure                            - Beginning the measurement of the
                                                 port rate
      rate-sampling-window                    - 
 [no] reverse-direction                       - 
 [no] service-name                            - 
 [no] shutdown                                - Enable/disable the flow
 [no] test                                    - This command puts the specified 
                                                port into a loopback mode. The 
                                                no form of the command disables 
                                                the s
 [no] vlan-tag                                - 

 show rate
 show status
 show test
```

### inner-marking-profile
```text
# cli error: Invalid Command
ETX-2I>config>flows>flow(mng_access_defa)# inner-marking-profile
```

### inner-p-bit
```text
# cli error: Invalid Command
ETX-2I>config>flows>flow(mng_access_defa)# inner-p-bit
```

### inner-tag-ether-type
```text
# cli error: Invalid Command
ETX-2I>config>flows>flow(mng_access_defa)# inner-tag-ether-type
```

### inner-vlan
```text
# cli error: Invalid Command
ETX-2I>config>flows>flow(mng_access_defa)# inner-vlan
```

### ip
```text
# cli error: Invalid Command
ETX-2I>config>flows>flow(mng_access_defa)# ip
```

### mac
```text
<CR>

ETX-2I>config>flows>flow(mng_access_defa)# mac
```

### marking-profile
```text
<marking-profile-name>                     : [1..32 chars]


ETX-2I>config>flows>flow(mng_access_defa)# marking-profile
```

### p-bit
```text
# cli error: Invalid Command
ETX-2I>config>flows>flow(mng_access_defa)# p-bit
```

### tag-ether-type
```text
# cli error: Invalid Command
ETX-2I>config>flows>flow(mng_access_defa)# tag-ether-type
```

### vlan
```text
<push>                                     : 
 <pop>                                      : 


ETX-2I>config>flows>flow(mng_access_defa)# vlan
```

## configure management

Level help (`?`):
```text
access                                  + Specifies access paths and 
                                                rights
      dscp                                    - Configure DSCP value
 [no] login-user                              + Create user
 [no] management-address                      - Configure management protocols 
                                                source IP
      netconf                                 + Netconf commands
      radius                                  + Configure RADIUS client
      snmp                                    + Defines SNMP settings
      tacacsplus                              + Configure TACACS+ client
 [no] user                                    - Create user

 show failed-login-attempts
 show ssh-server
 show users-details                           - Display connected users
 show users                                   - Show users
```

### dscp
```text
<value>                                    : DSCP value [0..63, default 0]


ETX-2I>config>mngmnt# dscp
```

### login-user *(not entered — parameterized context)*
```text
<name>                                     : User name [1..20 chars]


ETX-2I>config>mngmnt# login-user
```

### management-address
```text
<ipv4>                                     : ipv4
 <ipv6>                                     : ipv6
 <ip-address>                               : Management protocols source IP 
                                              [0.0.0.0|0:0:0:0::0]


ETX-2I>config>mngmnt# management-address
```

### show failed-login-attempts
```text
<CR>

ETX-2I>config>mngmnt# show failed-login-attempts
```

### show ssh-server
```text
<fingerprint>                              : 


ETX-2I>config>mngmnt# show ssh-server
```

### show users
```text
<CR>

ETX-2I>config>mngmnt# show users
```

### show users-details
```text
<CR>

ETX-2I>config>mngmnt# show users-details
```

### user
```text
<name>                                     : User name [1..20 chars]


ETX-2I>config>mngmnt# user
```

## configure management access

Level help (`?`):
```text
[no] access-group                            - Apply ACL to device management
      auth-policy                             - Set authentication sequence
      clear-statistics                        - Clear ACL statistics
      command-authorization                   - Configure command authorization
 [no] sftp                                    - Enable SFTP
 [no] sftp-server                             - Enable SFTP Server
 [no] snmp                                    - Enable SNMP 
      ssh-encryption                          - 
      ssh-key-exchange                        - 
      ssh-mac                                 - 
 [no] ssh                                     - Enable SSH
      ssh-server                              + 
 [no] telnet                                  - Enable Telnet 
 [no] tftp                                    - Enable TFTP
      ztc-xml-generate-encrypted-password     - Encrypted password generator: 
                                                enter clear text password and 
                                                get the encrypted password

 show access-list                             - ACL Information 
 show statistics                              - Show ACL statistics
```

### access-group
```text
<acl-name>                                 : ACL name [string]


ETX-2I>config>mngmnt>access# access-group
```

### auth-policy
```text
<1st-level>                                : First method


ETX-2I>config>mngmnt>access# auth-policy
```

### clear-statistics
```text
<ipv4>                                     : IPv4
 <ipv6>                                     : IPv6


ETX-2I>config>mngmnt>access# clear-statistics
```

### command-authorization
```text
<1st-method>                               : First method


ETX-2I>config>mngmnt>access# command-authorization
```

### sftp
```text
<CR>

ETX-2I>config>mngmnt>access# sftp
```

### sftp-server
```text
<CR>

ETX-2I>config>mngmnt>access# sftp-server
```

### show access-list
```text
<summary>                                  : ACL summary


ETX-2I>config>mngmnt>access# show access-list
```

### show statistics
```text
<ipv4>                                     : IPv4
 <ipv6>                                     : IPv6


ETX-2I>config>mngmnt>access# show statistics
```

### snmp
```text
<CR>

ETX-2I>config>mngmnt>access# snmp
```

### ssh
```text
<CR>

ETX-2I>config>mngmnt>access# ssh
```

### ssh-encryption
```text
<all>                                      : 
 <algorithm>                                : 


ETX-2I>config>mngmnt>access# ssh-encryption
```

### ssh-key-exchange
```text
<all>                                      : 
 <algorithm>                                : 


ETX-2I>config>mngmnt>access# ssh-key-exchange
```

### ssh-mac
```text
<all>                                      : 
 <algorithm>                                : 


ETX-2I>config>mngmnt>access# ssh-mac
```

### telnet
```text
<CR>

ETX-2I>config>mngmnt>access# telnet
```

### tftp
```text
<CR>

ETX-2I>config>mngmnt>access# tftp
```

### ztc-xml-generate-encrypted-password
```text
<clear-password>                           : String with maximum of 60 
                                              characters [0..60 chars]


ETX-2I>config>mngmnt>access# ztc-xml-generate-encrypted-password
```

## configure management access ssh-server

Level help (`?`):
```text
[no] trusted-ca                              - Configure CA to trust for 
                                                authentication
```

### trusted-ca
```text
<ca-name>                                  : [1..20 chars]


ETX-2I>config>mngmnt>access>ssh-server# trusted-ca
```

## configure management netconf

Level help (`?`):
```text
inactivity-timeout                      - Configure NETCONF session 
                                                inactivity timeout
 [no] shutdown                                - Disable NETCONF
```

### inactivity-timeout
```text
<time>                                     : 
 <infinite>                                 : 


ETX-2I>config>mngmnt>netconf# inactivity-timeout
```

### shutdown
```text
<CR>

ETX-2I>config>mngmnt>netconf# shutdown
```

## configure management radius

Level help (`?`):
```text
clear-statistics                        - Clear RADIUS statistics
      server                                  + Connect to RADIUS server

 show statistics                              - RADIUS  statistics
```

### clear-statistics
```text
<CR>

ETX-2I>config>mngmnt>radius# clear-statistics
```

### server *(not entered — parameterized context)*
```text
<server-id>                                : Specify  RADIUS server  [1..4]


ETX-2I>config>mngmnt>radius# server
```

### show statistics
```text
<CR>

ETX-2I>config>mngmnt>radius# show statistics
```

## configure management snmp

Level help (`?`):
```text
[no] access-group                            + Configure access group
 [no] bootstrap-notification                  - Enable bootstrap notification 
 [no] community                               + Configure community
 [no] config-change-notification              - Enable/disable configuration 
                                                change notification sending
 [no] notify                                  + Configure notification group
 [no] notify-filter                           + Configure notification group 
                                                filter
 [no] notify-filter-profile                   + Configure notification group 
                                                profile
 [no] security-to-group                       + Assign security to group
      snmp-engine-id                          - Configure SNMP Engine ID
 [no] target                                  + Configure SNMP target
 [no] target-params                           + Configure target parameters
      trap-sync-group                         + Configure trap synchronization 
                                                group
 [no] user                                    + Configure SNMP user
 [no] view                                    + Configure view

 show snmpv3                                  - SNMPv3 information
 show trap-sync                               - Show trap synchronization
```

### access-group *(not entered — parameterized context)*
```text
<group-name>                               : Group name [string]


ETX-2I>config>mngmnt>snmp# access-group
```

### bootstrap-notification
```text
<CR>

ETX-2I>config>mngmnt>snmp# bootstrap-notification
```

### community *(not entered — parameterized context)*
```text
<community-index>                          : Community index [string]


ETX-2I>config>mngmnt>snmp# community
```

### config-change-notification
```text
<CR>

ETX-2I>config>mngmnt>snmp# config-change-notification
```

### notify *(parameterized — inner help harvested under "configure management snmp notify NAME")*
```text
<notify-name>                              : Notification group name [string]


ETX-2I>config>mngmnt>snmp# notify
```

### notify-filter *(not entered — parameterized context)*
```text
<name>                                     : Notification group name [string]


ETX-2I>config>mngmnt>snmp# notify-filter
```

### notify-filter-profile *(parameterized — inner help harvested under "configure management snmp notify-filter-profile NAME")*
```text
<params-name>                              : Parameter name [string]


ETX-2I>config>mngmnt>snmp# notify-filter-profile
```

### security-to-group *(not entered — parameterized context)*
```text
<snmpv1>                                   : SNMPv1
 <snmpv2c>                                  : SNMPv2c
 <usm>                                      : USM


ETX-2I>config>mngmnt>snmp# security-to-group
```

### show snmpv3
```text
information

ETX-2I>config>mngmnt>snmp# show snmpv3
```

### show trap-sync
```text
<CR>

ETX-2I>config>mngmnt>snmp# show trap-sync
```

### snmp-engine-id
```text
<mac>                                      : MAC
 <ipv4>                                     : IPv4
 <ipv6>                                     : IPv6
 <text>                                     : Free text


ETX-2I>config>mngmnt>snmp# snmp-engine-id
```

### target *(parameterized — inner help harvested under "configure management snmp target NAME")*
```text
<name>                                     : Target name [1..32 chars]


ETX-2I>config>mngmnt>snmp# target
```

### target-params *(not entered — parameterized context)*
```text
<name>                                     : Target parameters name [1..32 
                                              chars]


ETX-2I>config>mngmnt>snmp# target-params
```

### trap-sync-group *(not entered — parameterized context)*
```text
<group-id>                                 : Group ID [number] [1..2]


ETX-2I>config>mngmnt>snmp# trap-sync-group
```

### user *(not entered — parameterized context)*
```text
<security-name>                            : Security name [string]


ETX-2I>config>mngmnt>snmp# user
```

### view *(not entered — parameterized context)*
```text
<view-name>                                : View name [string]


ETX-2I>config>mngmnt>snmp# view
```

## configure management snmp notify NAME

Level help (`?`):
```text
[no] bind                                    - Bind trap
 [no] shutdown                                - Disable notification group
      tag                                     - Tag


ETX-2I>config>mngmnt>snmp>notify(zzz-hrvst)$
```

### bind
```text
<bridgeSpanningTreeNewRoot>                : 
 <bridgeSpanningTreeTopologyChange>         : 
 <bridgeMstpNewRoot>                        : 
 <bridgeMstpTopologyChange>                 : 
 <bridgePortDuplicateMac>                   : 
 <systemTraceMsgProtoMemAllocErr>           : 
 <pwConfigMismatch>                         : 
 <pwOamFailure>                             : 
 <pwRdi>                                    : 
 <pwRxFailure>                              : 
 <pwJitterBufferOverflow>                   : 
 <pwJitterBufferUnderflow>                  : 
 <pwOamDelayTca>                            : 
 <pwOamDelayTcaOff>                         : 
 <coldStart>                                : 
 <linkDown>                                 : 
 <linkUp>                                   : 
 <authenticationFailure>                    : 
 <bridgeMldSnoopingUnsupportedIp>           : 
 <bridgeMldSnoopingDuplicateIp>             : 
 <systemDeviceTemperatureOra>               : 
 <systemSoftwareInstallStart>               : 
 <systemSoftwareInstallEnd>                 : 
 <systemAlternateConfigLoaded>              : 
 <systemConfigurationSanity>                : 
 <systemDyingGasp>                          : 
 <systemDyingGaspRecovery>                  : 
 <systemTraceMsgFatalError>                 : 
 <systemTraceMsgException>                  : 
 <systemDeviceStartup>                      : 
 <systemHardwareFailure>                    : 
 <systemSwPackCorrupted>                    : 
 <systemStartupConfigUnconfirmed>           : 
 <fanFailure>                               : 
 <systemSuccessfulLogin>                    : 
 <systemFailedLogin>                        : 
 <systemLogout>                             : 
 <powerDeliveryFailure>                     : 
 <systemTrapHardSyncStart>                  : 
 <systemTrapHardSyncEnd>                    : 
 <systemConfigurationChange>                : 
 <systemConfigChangeEnableTraps>            : 
 <systemUserReset>                          : 
 <systemActiveSoftwareChanged>              : 
 <systemRunningConfigSaved>                 : 
 <systemBootstrap>                          : 
 <alarmInput>                               : 
 <faultPropagation>                         : 
 <systemAclLogging>                         : 
 <systemResourceOverflow>                   : 
 <systemRemoteTerminalStarted>              : 
 <systemRemoteTerminalEnded>                : 
 <systemNtpAccuracyOutOfLimit>              : 
 <systemSummerTimeStarted>                  : 
 <systemSummerTimeEnded>                    : 
 <systemFileOverflow>                       : 
 <systemTimeChanged>                        : 
 <systemTimeSourceChanged>                  : 
 <systemSerialPortDisabled>                 : 
 <systemSerialPortEnabled>                  : 
 <systemFactoryDefaultButtonPushed>         : 
 <systemLowMemory>                          : 
 <systemCriticalLowMemory>                  : 
 <systemNewSwFromBootMismatch>              : 
 <systemNetconfSessionStarted>              : 
 <systemNetconfSessionEnded>                : 
 <systemConfigurationLocked>                : 
 <systemConfigurationUnlocked>              : 
 <powerSupplyMismatch>                      : 
 <systemAlarmStorm>                         : 
 <systemColdEnvironment>                    : 
 <ospfInterfaceConfigError>                 : 
 <ospfGracefulRestart>                      : 
 <ospfNeighborStateChange>                  : 
 <ospfInterfaceStateChange>                 : 
 <ospfNeighborGracefulRestart>              : 
 <vrrpProtocolStateChange>                  : 
 <smartSfpMismatch>                         : 
 <bgpSessionFailure>                        : 
 <bgpTcpSessionAuthFailure>                 : 
 <bgpSessionPrefixOverflow>                 : 
 <ipBfdDetectionTimeExpired>                : 
 <systemRfc2544TestStart>                   : 
 <systemRfc2544TestEnd>                     : 
 <systemItuSatTestStart>                    : 
 <systemItuSatConfigurationTestEnd>         : 
 <systemItuSatPerformanceTestEnd>           : 
 <systemItuSatResponderActivated>           : 
 <systemItuSatResponderDeactivated>         : 
 <twampPeerTestStarted>                     : 
 <twampPeerTestStopped>                     : 
 <twampSessionLossRatioTca>                 : 
 <twampSessionDelayTca>                     : 
 <twampSessionDelayVarTca>                  : 
 <twampSessionUnavailable>                  : 
 <twampSessionForwardUnavailable>           : 
 <twampSessionBackwardUnavailable>          : 
 <twampSessionForwardLossRatioTca>          : 
 <twampSessionForwardDelayTca>              : 
 <twampSessionForwardDelayVarTca>           : 
 <twampSessionBackwardLossRatioTca>         : 
 <twampSessionBackwardDelayTca>             : 
 <twampSessionBackwardDelayVarTca>          : 
 <twampPeerTodAccuracyOutOfLimit>           : 
 <systemL3SatTestStart>                     : 
 <systemL3SatConfigurationTestEnd>          : 
 <systemL3SatPerformanceTestEnd>            : 
 <systemL3SatResponderActivated>            : 
 <systemL3SatResponderDeactivated>          : 
 <systemL3SatPreliminaryTestFailed>         : 
 <stationClockLos>                          : 
 <lagLacpDown>                              : 
 <lagLacpLoopDetection>                     : 
 <lagLacpChurn>                             : 
 <lagSubGroupSwitchover>                    : 
 <lagFailure>                               : 
 <lagMinimumMembers>                        : 
 <lagFailed>                                : 
 <epsConfigurationMismatch>                 : 
 <etpEpsPortSwitchover>                     : 
 <systemLicenseEnabled>                     : 
 <systemLicenseDisabled>                    : 
 <systemPmProcessDisabled>                  : 
 <systemPmSpaceOverflow>                    : 
 <systemFrameOverflow>                      : 
 <tunnelDown>                               : 
 <tunnelNhrpRegistrationNoReply>            : 
 <tunnelNhrpRegistrationNak>                : 
 <routerInterfaceIpv6Dad>                   : 
 <sfpNoResponse>                            : 
 <sfpMismatch>                              : 
 <sfpRemoved>                               : 
 <sfpTemperatureOra>                        : 
 <sfpOprOra>                                : 
 <sfpOptOra>                                : 
 <sfpOptOraOff>                             : 
 <sfpLbcOra>                                : 
 <sfpLbcOraOff>                             : 
 <sfpVoltageOra>                            : 
 <sfpVoltageOraOff>                         : 
 <ethLos>                                   : 
 <erpStateProtected>                        : 
 <erpPortStateChange>                       : 
 <oamEfmRemoteLoopback>                     : 
 <oamEfmRemoteLoopbackOff>                  : 
 <oamEfmLinkFaultIndication>                : 
 <oamEfmFeLinkFaultIndication>              : 
 <oamEfmCriticalLinkIndication>             : 
 <oamEfmFeCriticalLinkIndication>           : 
 <oamEfmDyingGaspIndication>                : 
 <oamEfmFeDyingGaspIndication>              : 
 <pcsLinkDown>                              : 
 <ethDot1xAuthSuppAuthorized>               : 
 <ethDot1xAuthSuppUnauthorized>             : 
 <ethSilentStartNoRx>                       : 
 <adminDown>                                : 
 <sdhSonetLof>                              : 
 <sdhSonetLos>                              : 
 <sdhSonetAis>                              : 
 <sdhSonetSd>                               : 
 <sdhSonetEed>                              : 
 <e3t3Rai>                                  : 
 <e3t3Ais>                                  : 
 <e3t3Lof>                                  : 
 <e3t3Los>                                  : 
 <e1t1Ais>                                  : 
 <e1t1Lof>                                  : 
 <e1t1Rai>                                  : 
 <e1t1Lomf>                                 : 
 <e1t1Los>                                  : 
 <e1t1Loopback>                             : 
 <e1t1LoopbackOff>                          : 
 <e1t1EsLineTca>                            : 
 <e1t1CvPathTca>                            : 
 <e1t1EsPathTca>                            : 
 <e1t1SesPathTca>                           : 
 <e1t1SefsPathTca>                          : 
 <e1t1CssPathTca>                           : 
 <e1t1UasPathTca>                           : 
 <cellularIfDown>                           : 
 <cellularIfRssiOra>                        : 
 <cardHwFailure>                            : 
 <cardMismatch>                             : 
 <cardProvisionFailure>                     : 
 <cardUnsupportedSw>                        : 
 <cardUnsupportedHw>                        : 
 <cardImproperRemoval>                      : 
 <cardNoResponse>                           : 
 <cardInitFailure>                          : 
 <cardReset>                                : 
 <cardPluggedIn>                            : 
 <cardPluggedOut>                           : 
 <systemTacacsServerWtr>                    : 
 <systemTacacsServerWtrOff>                 : 
 <systemCertificateAboutToExpire>           : 
 <systemCertificateExpired>                 : 
 <systemAbmTestStart>                       : 
 <systemAbmTestEnd>                         : 
 <systemDownloadEnd>                        : 
 <systemUploadEnd>                          : 
 <gnssNotLocked>                            : 
 <gnssHardwareFailure>                      : 
 <mirroringSessionStarted>                  : 
 <mirroringSessionStopped>                  : 
 <routerNatMappingTableFull>                : 
 <routerNatPortRangeExhaustion>             : 
 <oamCfmMepAis>                             : 
 <oamCfmMepLck>                             : 
 <oamCfmMepMismatch>                        : 
 <oamCfmRmepLoc>                            : 
 <oamCfmRmepRdi>                            : 
 <oamCfmDestNeDelayTca>                     : 
 <oamCfmDestNeDelayTcaOff>                  : 
 <oamCfmDestNeDelayVarTca>                  : 
 <oamCfmDestNeDelayVarTcaOff>               : 
 <oamCfmDestNeLossRatioTca>                 : 
 <oamCfmDestNeLossRatioTcaOff>              : 
 <oamCfmDestNeLossRatioTcaFe>               : 
 <oamCfmDestNeLossRatioTcaFeOff>            : 
 <oamCfmDestNeUnavailRatioTca>              : 
 <oamCfmDestNeUnavailRatioTcaOff>           : 
 <oamCfmDestNeUnavailRatioTcaFe>            : 
 <oamCfmDestNeUnavailRatioTcaFeOff>         : 
 <oamCfmMepDefXconCCM>                      : 
 <oamCfmMepDefErrorCCM>                     : 
 <oamCfmRmepDefRemoteCCM>                   : 
 <oamCfmRmepDefRDICCM>                      : 
 <oamCfmRmepDefMACstatus>                   : 
 <systemCfmSoamRxPacketDropped>             : 
 <oamCfmDestNeOnDemandTestStart>            : 
 <oamCfmDestNeOnDemandTestEnd>              : 
 <ethFatPipeRateExceededBwp>                : 
 <flowFatPipeRateExceededBwp>               : 
 <systemSftpServerCopy>                     : 
 <systemSftpServerLoginFailed>              : 
 <oamCfmMepLatchingLoopback>                : 
 <oamCfmMepLatchingLoopbackOff>             : 


ETX-2I>config>mngmnt>snmp>notify(zzz-hrvst)$ bind
```

### shutdown
```text
<CR>

ETX-2I>config>mngmnt>snmp>notify(zzz-hrvst)$ shutdown
```

### tag
```text
<argument>                                 : Tag [string]


ETX-2I>config>mngmnt>snmp>notify(zzz-hrvst)$ tag
```

## configure management snmp notify-filter-profile NAME

Level help (`?`):
```text
profile-name                            - Profile name
 [no] shutdown                                - Disable notification group


ETX-2I>config>mngmnt>snmp>filter-profile$
```

### profile-name
```text
<argument>                                 : Profile name [string]


ETX-2I>config>mngmnt>snmp>filter-profile$ profile-name
```

### shutdown
```text
<CR>

ETX-2I>config>mngmnt>snmp>filter-profile$ shutdown
```

## configure management snmp target NAME

Level help (`?`):
```text
address                                 - Target address
 [no] tag-list                                - Configure tag list
      target-params                           - Target parameters
 [no] trap-sync-group                         - Configure trap synchronization 
                                                group


ETX-2I>config>mngmnt>snmp>target(zzz-hrvst)$
```

### address
```text
<udp-domain>                               : UDP
 <oam-domain>                               : OAM
 <udp-ipv4-domain>                          : UDP over IPv4
 <udp-ipv6-domain>                          : UDP over IPv6
 <udp-dns-domain>                           : UDP-dns


ETX-2I>config>mngmnt>snmp>target(zzz-hrvst)$ address
```

### shutdown
```text
# cli error: Invalid Command
ETX-2I>config>mngmnt>snmp>target(zzz-hrvst)$ shutdown
```

### tag-list
```text
<list>                                     : Tag list [string]


ETX-2I>config>mngmnt>snmp>target(zzz-hrvst)$ tag-list
```

### target-params
```text
<params-name>                              : Parameter [string]


ETX-2I>config>mngmnt>snmp>target(zzz-hrvst)$ target-params
```

### trap-sync-group
```text
<group-id>                                 : Group ID [number] [1..2]


ETX-2I>config>mngmnt>snmp>target(zzz-hrvst)$ trap-sync-group
```

## configure management tacacsplus

Level help (`?`):
```text
[no] group                                   + TACACS+ server group
 [no] privilege-level                         - Configure mapped between 
                                                privilege level to cli level
 [no] server                                  + Add TACACS+ server
      server-selection                        - Order of servers for 
                                                authentication
 [no] wait-to-restore-server                  - Time to restore TACACS+ server

 show status                                  - Display Tacacs+ status
```

### group *(not entered — parameterized context)*
```text
<group-name>                               : TACACS+ server group name [1..80 
                                              chars]


ETX-2I>config>mngmnt>tacacsplus# group
```

### privilege-level
```text
<tacaacs-privilege-level>                  : TACACS+ privilege level [0..15]


ETX-2I>config>mngmnt>tacacsplus# privilege-level
```

### server *(not entered — parameterized context)*
```text
<ip>                                       : TACACS+ server IP address [0.0.0.0
                                              |0:0:0:0::0]


ETX-2I>config>mngmnt>tacacsplus# server
```

### server-selection
```text
<priority>                                 : 
 <cached-first>                             : 


ETX-2I>config>mngmnt>tacacsplus# server-selection
```

### show status
```text
<CR>

ETX-2I>config>mngmnt>tacacsplus# show status
```

### wait-to-restore-server
```text
<seconds>                                  : [1..86400]


ETX-2I>config>mngmnt>tacacsplus# wait-to-restore-server
```

## configure oam

Level help (`?`):
```text
cfm                                     + Configure OAM CFM
      efm                                     + Configure OAM EFM
      twamp                                   + TWAMP
```

## configure oam cfm

Level help (`?`):
```text
alarm-type                              - Alarm legacy report 
      availability                            - 
      ltr                                     - Set LTR parameters 
 [no] maintenance-domain                      + Configure Maintenance Domain 
                                                (MD)
 [no] md-level-mip                            - Define MD level MIP
 [no] measurement-bin-profile                 + Configure measurement bin 
                                                profile
      mip-assign                              - Configure MIP creation mode
      multicast-addr                          - Configure CFM MAC address
 [no] multi-mep-per-evc                       - 

 show mips                                    - Display MIP table
 show on-demand-tests                         - Display CFM on-demand summary
 show summary                                 - Display CFM summary
```

### alarm-type
```text
<legacy>                                   : Alarm name as defined in RAD 
                                              OamCfm-MIB
 <soam>                                     : Alarm name as defined in IEEE 
                                              802.1ag table 20-1


ETX-2I>config>oam>cfm# alarm-type
```

### availability
```text
delta-t
 n
 forward-thr
 backward-thr

ETX-2I>config>oam>cfm# availability
```

### ltr
```text
port-id-subtype
 up-mep-port

ETX-2I>config>oam>cfm# ltr
```

### maintenance-domain *(parameterized — inner help harvested under "configure oam cfm maintenance-domain NAME")*
```text
<mdid>                                     : Maintenance Domain Identifier 
                                              (MDID) [number]


ETX-2I>config>oam>cfm# maintenance-domain
```

### md-level-mip
```text
<md-level-list>                            : MD level list [0..7]


ETX-2I>config>oam>cfm# md-level-mip
```

### measurement-bin-profile *(parameterized — inner help harvested under "configure oam cfm measurement-bin-profile NAME")*
```text
<name>                                     : Measurement bin profile name 
                                              [1..32 chars]


ETX-2I>config>oam>cfm# measurement-bin-profile
```

### mip-assign
```text
<automatic>                                : Automatic MIP creation
 <manual>                                   : Manual MIP creation


ETX-2I>config>oam>cfm# mip-assign
```

### multi-mep-per-evc
```text
<CR>

ETX-2I>config>oam>cfm# multi-mep-per-evc
```

### multicast-addr
```text
<mac-address>                              : CFM MAC address 
                                              [00-00-00-00-00-00, default 
                                              0180C2000000]


ETX-2I>config>oam>cfm# multicast-addr
```

### show mips
```text
<CR>

ETX-2I>config>oam>cfm# show mips
```

### show on-demand-tests
```text
<CR>

ETX-2I>config>oam>cfm# show on-demand-tests
```

### show summary
```text
<CR>

ETX-2I>config>oam>cfm# show summary
```

## configure oam cfm maintenance-domain NAME

Level help (`?`):
```text
[no] maintenance-association                 + Configure Maintenance 
                                                Association (MA)
      md-level                                - Configure MD level
 [no] mip                                     + Configure MIP
 [no] name                                    - Configure MD name
 [no] proprietary-cc                          - Use proprietary CC protocol
```

### maintenance-association *(parameterized — inner help harvested under "configure oam cfm maintenance-domain NAME maintenance-association NAME")*
```text
<maid>                                     : Maintenance Association Identifier
                                               (MAID) [number]


ETX-2I>config>oam>cfm>md(1)# maintenance-association
```

### md-level
```text
<md-level>                                 : MD level [0..7]


ETX-2I>config>oam>cfm>md(1)# md-level
```

### mip *(not entered — parameterized context)*
```text
<mip-id>                                   : MIP ID [number]


ETX-2I>config>oam>cfm>md(1)# mip
```

### name
```text
<string>                                   : String
 <dns>                                      : DNS
 <mac-and-uint>                             : MAC and UINT


ETX-2I>config>oam>cfm>md(1)# name
```

### proprietary-cc
```text
<CR>

ETX-2I>config>oam>cfm>md(1)# proprietary-cc
```

## configure oam cfm maintenance-domain NAME maintenance-association NAME

Level help (`?`):
```text
ccm-interval                            - Configure interval between CC 
                                                messages
      classification                          - Configure classification
 [no] interface-status-tlv                    - Determines if Interface Status 
                                                TLV is added in CCM message
 [no] mep                                     + Configure Maintenance Endpoint 
                                                (MEP)
      name                                    - Configure MA name
```

### ccm-interval
```text
<3.33ms>                                   : 3.33 milliseconds
 <10ms>                                     : 10 milliseconds
 <100ms>                                    : 100 milliseconds
 <1s>                                       : 1 second
 <10s>                                      : 10 seconds
 <1min>                                     : 1 minute
 <10min>                                    : 10 minuntes


ETX-2I>config>oam>cfm>md(1)>ma(1)# ccm-interval
```

### classification
```text
vlan

ETX-2I>config>oam>cfm>md(1)>ma(1)# classification
```

### interface-status-tlv
```text
<CR>

ETX-2I>config>oam>cfm>md(1)>ma(1)# interface-status-tlv
```

### mep *(not entered — parameterized context)*
```text
<mepid>                                    : Maintenance Endpoint Identifier 
                                              (MEP ID) [number]


ETX-2I>config>oam>cfm>md(1)>ma(1)# mep
```

### name
```text
<string>                                   : String
 <primary-vid>                              : Primary VLAN ID
 <uint>                                     : UINT
 <icc>                                      : ICC


ETX-2I>config>oam>cfm>md(1)>ma(1)# name
```

## configure oam cfm measurement-bin-profile NAME

Level help (`?`):
```text
[no] thresholds                              - Configure measurement bin 
                                                thresholds


ETX-2I>config>oam>cfm>measurement-bin-prof(zzz-hrvst)$
```

### thresholds
```text
<thresholds-list>                          : List of measurement bin thresholds
                                               [n1..n2,n3]


ETX-2I>config>oam>cfm>measurement-bin-prof(zzz-hrvst)$ thresholds
```

## configure oam efm

Level help (`?`):
```text
[no] descriptor                              - Configure EFM descriptor
```

### descriptor
```text
<number>                                   : EFM descriptor ID [number]


ETX-2I>config>oam>efm# descriptor
```

## configure oam twamp

Level help (`?`):
```text
[no] controller                              + Create/configure/activate a 
                                                TWAMP controller
 [no] profile                                 + Create/modify/delete a TWAMP 
                                                test profile
 [no] responder                               + Create/configure/activate a 
                                                TWAMP responder
```

### controller *(not entered — parameterized context)*
```text
<name>                                     : Assign a meaningful name to the 
                                              controller [1..32 chars]


ETX-2I>config>oam>twamp# controller
```

### profile *(not entered — parameterized context)*
```text
<name>                                     : [string]


ETX-2I>config>oam>twamp# profile
```

### responder *(not entered — parameterized context)*
```text
<name>                                     : Assign a meaningful name to the 
                                              responder [1..32 chars]


ETX-2I>config>oam>twamp# responder
```

## configure port

Level help (`?`):
```text
[no] cellular                                + Create/Delete cellular interface
      clear-statistics                        - 
      ds1                                     + Configure DS1 port
      ethernet                                + Specifies Ethernet parameters
 [no] gfp                                     + Specifies GFP port parameters
 [no] hdlc                                    + Specifies HDLC parameters
      int-ethernet                            + Specifies Internal Ethernet 
                                                parameters
 [no] l2cp-profile                            + Defines l2cp profile
 [no] lag                                     + 
 [no] logical-mac                             + Specifies Logical MAC port 
                                                parameters
      mng-ethernet                            + Configure management Ethernet 
                                                port
 [no] ppp                                     + 
 [no] queue-statistics                        - Allocate counters to queue 
                                                blocks
      rate-sampling-window                    - Configure Ethernet statistics 
                                                sampling rate
      sdh-sonet                               + Defines SDH/SONET port 
                                                parameters
 [no] smart-sfp                               + 
 [no] svi                                     + Create/delete service virtual 
                                                interface
 [no] tag-ether-type                          - Configure supported Ethertype
      vdsl2                                   + Defines a VDSL2 interface
      xml-export                              - Export command output to XML 
                                                file

 show statistics                              - Display aggregate counters for 
                                                 all device ports
 show summary-full-name                       - Display port status summary 
                                                 with full name
 show summary                                 - Display port status summary
```

### cellular *(not entered — parameterized context)*
```text
<port-index>                               : Index of cellular interface 
                                              [slot/port]


ETX-2I>config>port# cellular
```

### clear-statistics
```text
<CR>

ETX-2I>config>port# clear-statistics
```

### ds1 *(not entered — parameterized context)*
```text
<port-index>                               : Port number [slot/port]


ETX-2I>config>port# ds1
```

### ethernet *(parameterized — inner help harvested under "configure port ethernet NAME")*
```text
<port-index>                               : Port number [slot/port]


ETX-2I>config>port# ethernet
```

### gfp *(not entered — parameterized context)*
```text
<port-number>                              : GFP port number [number]


ETX-2I>config>port# gfp
```

### hdlc *(not entered — parameterized context)*
```text
<port-number>                              : HDLC port number [number]


ETX-2I>config>port# hdlc
```

### int-ethernet *(not entered — parameterized context)*
```text
<port-index>                               : Port number [slot/port]


ETX-2I>config>port# int-ethernet
```

### l2cp-profile *(parameterized — inner help harvested under "configure port l2cp-profile NAME")*
```text
<l2cp-profile-name>                        : Index of the profile [1..32 chars]


ETX-2I>config>port# l2cp-profile
```

### lag *(not entered — parameterized context)*
```text
<port-number>                              : LAG port number [number] [1..4]


ETX-2I>config>port# lag
```

### logical-mac *(parameterized — inner help harvested under "configure port logical-mac NAME")*
```text
<port-number>                              : Logical MAC port number [number]


ETX-2I>config>port# logical-mac
```

### ppp *(parameterized — inner help harvested under "configure port ppp NAME")*
```text
<port-number>                              : PPP Port number [number]


ETX-2I>config>port# ppp
```

### queue-statistics
```text
<ethernet>                                 : 


ETX-2I>config>port# queue-statistics
```

### rate-sampling-window
```text
<argument>                                 : Duration between statistics 
                                              samplings (minutes) [1..30, 
                                              default 15]


ETX-2I>config>port# rate-sampling-window
```

### sdh-sonet *(not entered — parameterized context)*
```text
<port-index-trib>                          : Port index [slot/port/tributary]


ETX-2I>config>port# sdh-sonet
```

### show statistics
```text
<CR>

ETX-2I>config>port# show statistics
```

### show summary
```text
<CR>

ETX-2I>config>port# show summary
```

### show summary-full-name
```text
<CR>
 <none>                                     : 
 <ethernet>                                 : 
 <giga-ethernet>                            : 
 <fast-ethernet>                            : 
 <lag>                                      : 
 <logical-mac>                              : 
 <e1>                                       : 
 <t1>                                       : 
 <j1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <sdh-sonet>                                : 
 <sdh>                                      : 
 <sonet>                                    : 
 <shdsl>                                    : 
 <adsl>                                     : 
 <vdsl>                                     : 
 <pcs>                                      : 
 <ima-group>                                : 
 <voice>                                    : 
 <serial>                                   : 
 <hdlc>                                     : 
 <ppp>                                      : 
 <mlppp>                                    : 
 <gfp>                                      : 
 <vcg>                                      : 
 <ss7>                                      : 
 <transparent>                              : 
 <svi>                                      : 
 <bridge>                                   : 
 <ethernet-mng>                             : 
 <t1-trib>                                  : 
 <e1-trib>                                  : 
 <mux-eth-tdm>                              : 
 <sag>                                      : 
 <sap>                                      : 
 <station-clock>                            : 
 <ds1>                                      : 
 <repeater>                                 : 
 <fe-mux-eth-tdm>                           : 
 <fe-user-eth>                              : 
 <fe-mng-eth>                               : 
 <e1-i>                                     : 
 <t1-i>                                     : 
 <fe-e1>                                    : 
 <fe-t1>                                    : 
 <tod>                                      : 
 <path>                                     : 
 <vc-vt>                                    : 
 <cmd-in>                                   : 
 <cmd-in-i>                                 : 
 <cmd-out>                                  : 
 <cmd-out-i>                                : 
 <cmd-channel>                              : 
 <bri>                                      : 
 <tdm-bridge>                               : 
 <int-ethernet>                             : 
 <ds0-bundle>                               : 
 <ds0-g703>                                 : 
 <cellular>                                 : 


ETX-2I>config>port# show summary-full-name
```

### smart-sfp *(not entered — parameterized context)*
```text
<port-number>                              : Port number [slot/port]


ETX-2I>config>port# smart-sfp
```

### svi *(parameterized — inner help harvested under "configure port svi NAME")*
```text
<port-number>                              : SVI port number [number] [1..96]


ETX-2I>config>port# svi
```

### tag-ether-type
```text
<ether-tag>                                : Ethertype [00-ffff, default 
                                              0x8100]


ETX-2I>config>port# tag-ether-type
```

### vdsl2 *(not entered — parameterized context)*
```text
<port-index>                               : Specifies the ID of the VDSL2 port
                                               [slot/port]


ETX-2I>config>port# vdsl2
```

### xml-export
```text
<show-summary>                             : 


ETX-2I>config>port# xml-export
```

## configure port ethernet NAME

Level help (`?`):
```text
[no] auto-negotiation                        - Enables/disables automatically 
                                                adjusting the speed
      classification-key                      - 
 [no] classifier                              + Enables/disables classifier at 
                                                the port level (A2CL)
      clear-efm-statistics                    - Clear EFM OAM statistics
      clear-l2cp-statistics                   - Clears the Layer 2 Control 
                                                Protocol statistics
      clear-queue-statistics                  - Clears queue statistics
      clear-statistics                        - Clears all statistics
 [no] dhcp-trust                              - Trust server  DHCP packets from 
                                                port
      dot1x                                   + 802.1X  level
 [no] efm                                     + Enables/disables OAM (EFM) on 
                                                the Ethernet port
      egress-mtu                              - Defines the max frame size to 
                                                transmit
      l2cp                                    - Enables/disables the Layer 2 
                                                Control Protocol
      lldp                                    + 
 [no] loopback                                - Enables/disables the Loopback 
                                                mode
      max-capability                          - Identifies the set of 
                                                capabilities advertised by the 
                                                local autonegotiation entity
      max-ql                                  - QL of the Clock Source
 [no] multi-policer                           - Configure a BUM policer that is 
                                                composed of several separate BW 
                                                profiles
 [no] name                                    - Assigns/removes a port name
 [no] pm-collection                           - Enable Performance Management 
                                                (PM) 
 [no] policer                                 - Activates/deactivates a policer 
                                                profile with single queue
 [no] queue-group                             - Assigns/removes a queue group 
                                                profile
 [no] rate-measure                            - Beginning the measurement of the
                                                 port rate
 [no] self-tuning                             - Enable self tuning if the 
                                                optical module supports it
 [no] shutdown                                - Administratively 
                                                disables/enables the port
 [no] silent-start                            - 
      speed-duplex                            - Specifies speed and duplex mode 
                                                when autonegotiation is disabled
      tag-ethernet-type                       - Determines the tag protocol 
                                                identifier
 [no] tx-ssm                                  - Enables/disables Synchronous 
                                                Status Messages transmission

 show l2cp-statistics                         - Displays Layer 2 Control 
                                                 Protocol statistics
 show loopback
 show oam-efm                                 - Display EFM OAM status
 show oam-efm-statistics                      - Display EFM OAM statistics
 show queue-statistics                        - Display queue statistics
 show rate
 show sfp-extended-information                - Display the vendor and user  
                                                 specific fields of SFP  
 show statistics                              - Displays the Ethernet port 
                                                 statistics
 show status                                  - Displays the Ethernet port 
                                                 status
```

### auto-fec-policy
```text
# cli error: Invalid Command
ETX-2I>config>port>eth(0/1)# auto-fec-policy
```

### auto-negotiation
```text
<CR>
 <sfp>                                      : Enables auto-negotiation for SFP 
                                              interfaces
 <rj45>                                     : Enables auto-negotiation for RJ-45
                                               interfaces


ETX-2I>config>port>eth(0/1)# auto-negotiation
```

### classification-key
```text
<CR>
 <vlan>                                     : 
 <inner-vlan>                               : 
 <legacy>                                   : 


ETX-2I>config>port>eth(0/1)# classification-key
```

### clear-efm-statistics
```text
<CR>

ETX-2I>config>port>eth(0/1)# clear-efm-statistics
```

### clear-l2cp-statistics
```text
<CR>

ETX-2I>config>port>eth(0/1)# clear-l2cp-statistics
```

### clear-queue-statistics
```text
<queue-block>                              : 
 <all>                                      : 


ETX-2I>config>port>eth(0/1)# clear-queue-statistics
```

### clear-statistics
```text
<CR>

ETX-2I>config>port>eth(0/1)# clear-statistics
```

### dhcp-trust
```text
<CR>

ETX-2I>config>port>eth(0/1)# dhcp-trust
```

### efm *(not entered — parameterized context)*
```text
descriptor

ETX-2I>config>port>eth(0/1)# efm
```

### egress-mtu
```text
<size>                                     : Specifies the Max Transition Unit 
                                              size (bytes) [64..12288, default 
                                              1790]


ETX-2I>config>port>eth(0/1)# egress-mtu
```

### fec
```text
# cli error: Invalid Command
ETX-2I>config>port>eth(0/1)# fec
```

### l2cp
```text
profile

ETX-2I>config>port>eth(0/1)# l2cp
```

### loopback
```text
<local>                                    : Closes the loop towards the user 
                                              interface
 <remote>                                   : Closes the loop towards the 
                                              network interface


ETX-2I>config>port>eth(0/1)# loopback
```

### max-capability
```text
<10-full-duplex>                           : Sets Max Capability to 10 BaseT 
                                              Full Duplex
 <100-full-duplex>                          : Sets Max Capability to 100 BaseT 
                                              Full Duplex
 <1000-full-duplex>                         : Sets Max Capability to 1000 BaseT 
                                              Full Duplex
 <1000-x-full-duplex>                       : Sets Max Capability to 1000 BaseX,
                                               -LX, -SX, -CX Full Duplex


ETX-2I>config>port>eth(0/1)# max-capability
```

### max-ql
```text
<eprtc>                                    : Enhanced Primary Reference Time 
                                              Clock
 <prtc>                                     : Primary Reference Time Clock
 <prc>                                      : Primary Reference Clock
 <ssu-a>                                    : Types I or V slave clock that is 
                                              defined in Recommendation G.812
 <ssu-b>                                    : Type VI slave clock that is 
                                              defined in Recommendation G.812.
 <eeec>                                     : Synchronous Equipment Clock
 <sec>                                      : Synchronous Equipment Clock
 <dnu>                                      : This signal should not be used for
                                               synchronization
 <ssm-based>                                : QL is received via Synchronous 
                                              Status Messages
 <prs>                                      : PRS traceable (Recommendation 
                                              G.811).
 <stu>                                      : Synchronized   Traceability 
                                              Unknown
 <st2>                                      : Traceable to Stratum 2 
                                              (Recommendation G.812, Type II).
 <tnc>                                      : Traceable to Transit Node Clock 
                                              (Recommendation G.812, Type V).
 <st3e>                                     : Traceable to Stratum 3E 
                                              (Recommendation G.812, Type III).
 <st3>                                      : Traceable to Stratum 3 
                                              (Recommendation G.812, Type IV).
 <smc>                                      : Traceable to SONET Clock Self 
                                              Timed
 <st4>                                      : Traceable to Stratum 4 Freerun
 <dus>                                      : This signal should not be used for
                                               synchronization
 <prov>                                     : Provisionable by the Network 
                                              Operator
 <unk>                                      : Unknown clock source


ETX-2I>config>port>eth(0/1)# max-ql
```

### multi-policer
```text
<broadcast>                                : 
 <multicast>                                : 
 <unknown-unicast>                          : 
 <broadcast-and-multicast>                  : 
 <broadcast-and-multicast-and-unknown-un*>  : 


ETX-2I>config>port>eth(0/1)# multi-policer
```

### name
```text
<string>                                   : Adds free text to assign a name to
                                               the port [1..254 chars]


ETX-2I>config>port>eth(0/1)# name
```

### pm-collection
```text
<interval>                                 : PM collection interval
 <on-interval-close>                        : Collect PM only on interval close


ETX-2I>config>port>eth(0/1)# pm-collection
```

### policer
```text
profile

ETX-2I>config>port>eth(0/1)# policer
```

### queue-group
```text
profile

ETX-2I>config>port>eth(0/1)# queue-group
```

### rate-measure
```text
interval

ETX-2I>config>port>eth(0/1)# rate-measure
```

### self-tuning
```text
<CR>

ETX-2I>config>port>eth(0/1)# self-tuning
```

### show l2cp-statistics
```text
<CR>

ETX-2I>config>port>eth(0/1)# show l2cp-statistics
```

### show loopback
```text
<CR>

ETX-2I>config>port>eth(0/1)# show loopback
```

### show oam-efm
```text
<CR>

ETX-2I>config>port>eth(0/1)# show oam-efm
```

### show oam-efm-statistics
```text
<CR>

ETX-2I>config>port>eth(0/1)# show oam-efm-statistics
```

### show queue-statistics
```text
<queue-block>                              : 
 <all>                                      : 


ETX-2I>config>port>eth(0/1)# show queue-statistics
```

### show rate
```text
<CR>

ETX-2I>config>port>eth(0/1)# show rate
```

### show sfp-extended-information
```text
<CR>

ETX-2I>config>port>eth(0/1)# show sfp-extended-information
```

### show statistics
```text
<CR>

ETX-2I>config>port>eth(0/1)# show statistics
```

### show status
```text
<CR>

ETX-2I>config>port>eth(0/1)# show status
```

### shutdown
```text
<CR>

ETX-2I>config>port>eth(0/1)# shutdown
```

### tag-ethernet-type
```text
<ether-type>                               : Determines the tag protocol 
                                              identifier (hex numbers) [00-ffff]


ETX-2I>config>port>eth(0/1)# tag-ethernet-type
```

### tx-ssm
```text
<CR>

ETX-2I>config>port>eth(0/1)# tx-ssm
```

## configure port ethernet NAME classifier

Level help (`?`):
```text
comment                                 - Enter a free text among the ACL 
                                                rules
      delete                                  - Delete an ACL rule or comment
      drop                                    - Define an ACL rule for 
                                                discarding frames
      match                                   - Define an ACL rule for 
                                                forwarding frames
      resequence                              - Update the sequence numbers of 
                                                existing ACL actions and 
                                                comments

 show status                                  - Display a sorted list of ACL 
                                                 actions
```

### comment
```text
<description>                              : [1..252 chars]


ETX-2I>config>port>eth(0/1)>classifier# comment
```

### delete
```text
<sequence-number>                          : The sequence number of the 
                                              match/drop/comment to be deleted 
                                              [1..4294967295]


ETX-2I>config>port>eth(0/1)>classifier# delete
```

### drop
```text
dst-mac
 src-mac
 ether-type
 <untagged>                                 : 
 vlan p-bit dei inner-ether-type inner-vlan inner-p-bit ip-dscp ip-precedence tos protocol src-ip dst-ip tcp-src-port tcp-dst-port udp-src-port udp-dst-port <any>                                      : 
 sequence

ETX-2I>config>port>eth(0/1)>classifier# drop
```

### match
```text
dst-mac
 src-mac
 ether-type
 <untagged>                                 : 
 vlan p-bit dei inner-ether-type inner-vlan inner-p-bit ip-dscp ip-precedence tos protocol src-ip dst-ip tcp-src-port tcp-dst-port udp-src-port udp-dst-port <any>                                      : 
 sequence to-flow

ETX-2I>config>port>eth(0/1)>classifier# match
```

### resequence
```text
<CR>
 <step>                                     : The step between sequence numbers 
                                              [1..10000, default 10]


ETX-2I>config>port>eth(0/1)>classifier# resequence
```

### show status
```text
<CR>

ETX-2I>config>port>eth(0/1)>classifier# show status
```

## configure port ethernet NAME dot1x

Level help (`?`):
```text
authenticator                           + Authenticator configuration 
                                                level
      clear-statistics                        - Clears statistic counters
      initialize                              - Reinitialize 802.1X

 show message-log
 show statistics                              - Port dot1x processes statistics
 show status
```

### clear-statistics
```text
<CR>

ETX-2I>config>port>eth(0/1)>dot1x# clear-statistics
```

### initialize
```text
<CR>

ETX-2I>config>port>eth(0/1)>dot1x# initialize
```

### show message-log
```text
<CR>
 <supplicant>                               : 


ETX-2I>config>port>eth(0/1)>dot1x# show message-log
```

### show statistics
```text
<CR>

ETX-2I>config>port>eth(0/1)>dot1x# show statistics
```

### show status
```text
<CR>

ETX-2I>config>port>eth(0/1)>dot1x# show status
```

## configure port ethernet NAME dot1x authenticator

Level help (`?`):
```text
authentication                          - Configure authentication mode
 [no] reauthentication                        - Reauthentication mode
 [no] shutdown                                - Enable/Disable authenticator 
                                                functionality
```

### authentication
```text
<port>                                     : 


ETX-2I>config>port>eth(0/1)>dot1x>authenticator# authentication
```

### reauthentication
```text
<CR>
 period

ETX-2I>config>port>eth(0/1)>dot1x>authenticator# reauthentication
```

### shutdown
```text
<CR>

ETX-2I>config>port>eth(0/1)>dot1x>authenticator# shutdown
```

## configure port l2cp-profile NAME

Level help (`?`):
```text
default                                 - Default action for not defined 
                                                control protocols
 [no] mac                                     - 
 [no] protocol                                - Choose specific protocol
```

### default
```text
<discard>                                  : 
 <tunnel>                                   : 


ETX-2I>config>port>l2cp-profile(mac2peer)# default
```

### mac
```text
<mac-addr>                                 : Last byte of the control protocol 
                                              mac [string, default 0x00]


ETX-2I>config>port>l2cp-profile(mac2peer)# mac
```

### protocol
```text
<lacp>                                     : 
 <stp>                                      : 
 <vtp>                                      : 
 <cdp>                                      : 
 <lldp>                                     : 
 <pvstp>                                    : 
 <pagp>                                     : 
 <udld>                                     : 
 <dtp>                                      : 
 <loopback>                                 : 
 <lamp>                                     : 
 <link-oam>                                 : 
 <e-lmi>                                    : 
 <802.1x>                                   : 
 <gvrp>                                     : 
 <gmrp>                                     : 
 <mmrp>                                     : 
 <mvrp-customer-bridge>                     : 
 <mvrp-provider-bridge>                     : 
 <msrp>                                     : 
 <mirp>                                     : 
 <dldp>                                     : 
 <hgmp>                                     : 
 <ptp>                                      : 
 <esmc>                                     : 


ETX-2I>config>port>l2cp-profile(mac2peer)# protocol
```

## configure port logical-mac NAME

Level help (`?`):
```text
[no] bind                                    - Bind port to lower layer port
      classification-key                      - 
 [no] classifier                              + Enables/disables classifier at 
                                                the port level (A2CL)
      clear-efm-statistics                    - Clear EFM OAM statistics
      clear-l2cp-statistics                   - Clears the Layer 2 Control 
                                                Protocol statistics
      clear-statistics                        - Clears all statistics
 [no] dhcp-trust                              - Trust server  DHCP packets from 
                                                port
 [no] efm                                     + Enables/disables OAM (EFM) on 
                                                the Ethernet port
      egress-mtu                              - Defines the max frame size to 
                                                transmit
      l2cp                                    - Enables/disables the Layer 2 
                                                Control Protocol
 [no] l2pt-network                            - Configures the port for l2pt 
                                                network behavior (translate 
                                                packets with tunnel mac)
      lldp                                    + 
 [no] loopback                                - Enables/disables the Loopback 
                                                mode
 [no] name                                    - Port name
 [no] pm-collection                           - Enable Performance Management 
                                                (PM) 
 [no] queue-group                             - Assigns/removes a queue group 
                                                profile
 [no] shutdown                                - Administratively 
                                                disables/enables the port
      tag-ethernet-type                       - Determines the ethernet tag 
                                                protocol identifier

 show bind                                    - Displays a list of interfaces 
                                                 bound to the port
 show l2cp-statistics                         - Displays Layer 2 Control 
                                                 Protocol statistics
 show loopback
 show statistics                              - Displays port statistics
 show status                                  - Displays the Ethernet port 
                                                 status
```

### bind
```text
<hdlc>                                     : HDLC port
 <gfp>                                      : GFP port


ETX-2I>config>port>log-mac(3)# bind
```

### classification-key
```text
<CR>
 <vlan>                                     : 
 <inner-vlan>                               : 
 <src-ip-addr>                              : 
 <dst-ip-addr>                              : 
 <legacy>                                   : 


ETX-2I>config>port>log-mac(3)# classification-key
```

### clear-efm-statistics
```text
<CR>

ETX-2I>config>port>log-mac(3)# clear-efm-statistics
```

### clear-l2cp-statistics
```text
<CR>

ETX-2I>config>port>log-mac(3)# clear-l2cp-statistics
```

### clear-statistics
```text
<CR>

ETX-2I>config>port>log-mac(3)# clear-statistics
```

### dhcp-trust
```text
<CR>

ETX-2I>config>port>log-mac(3)# dhcp-trust
```

### efm *(not entered — parameterized context)*
```text
descriptor

ETX-2I>config>port>log-mac(3)# efm
```

### egress-mtu
```text
<size>                                     : Specifies the Max Transition Unit 
                                              size (bytes) [number]


ETX-2I>config>port>log-mac(3)# egress-mtu
```

### l2cp
```text
profile

ETX-2I>config>port>log-mac(3)# l2cp
```

### l2pt-network
```text
<CR>

ETX-2I>config>port>log-mac(3)# l2pt-network
```

### loopback
```text
<local>                                    : 
 <remote>                                   : 


ETX-2I>config>port>log-mac(3)# loopback
```

### name
```text
<string>                                   : Name string [1..64 chars]


ETX-2I>config>port>log-mac(3)# name
```

### pm-collection
```text
<interval>                                 : PM collection interval
 <on-interval-close>                        : Collect PM only on interval close


ETX-2I>config>port>log-mac(3)# pm-collection
```

### queue-group
```text
profile

ETX-2I>config>port>log-mac(3)# queue-group
```

### show bind
```text
<CR>

ETX-2I>config>port>log-mac(3)# show bind
```

### show l2cp-statistics
```text
<CR>

ETX-2I>config>port>log-mac(3)# show l2cp-statistics
```

### show loopback
```text
<CR>

ETX-2I>config>port>log-mac(3)# show loopback
```

### show oam-efm
```text
# cli error: Invalid Command
ETX-2I>config>port>log-mac(3)# show oam-efm
```

### show oam-efm-statistics
```text
# cli error: Invalid Command
ETX-2I>config>port>log-mac(3)# show oam-efm-statistics
```

### show statistics
```text
<CR>

ETX-2I>config>port>log-mac(3)# show statistics
```

### show status
```text
<CR>

ETX-2I>config>port>log-mac(3)# show status
```

### shutdown
```text
<CR>

ETX-2I>config>port>log-mac(3)# shutdown
```

### tag-ethernet-type
```text
<ether-type>                               : Ethernet type value 
                                              [0x0000..0xFFFF]


ETX-2I>config>port>log-mac(3)# tag-ethernet-type
```

## configure port logical-mac NAME classifier

Level help (`?`):
```text
comment                                 - Enter a free text among the ACL 
                                                rules
      delete                                  - Delete an ACL rule or comment
      drop                                    - Define an ACL rule for 
                                                discarding frames
      match                                   - Define an ACL rule for 
                                                forwarding frames
      resequence                              - Update the sequence numbers of 
                                                existing ACL actions and 
                                                comments

 show status                                  - Display a sorted list of ACL 
                                                 actions
```

### comment
```text
<description>                              : [1..252 chars]


ETX-2I>config>port>log-mac(3)>classifier# comment
```

### delete
```text
<sequence-number>                          : The sequence number of the 
                                              match/drop/comment to be deleted 
                                              [1..4294967295]


ETX-2I>config>port>log-mac(3)>classifier# delete
```

### drop
```text
dst-mac
 src-mac
 ether-type
 <untagged>                                 : 
 vlan p-bit dei inner-ether-type inner-vlan inner-p-bit ip-dscp ip-precedence tos protocol src-ip dst-ip tcp-src-port tcp-dst-port udp-src-port udp-dst-port <any>                                      : 
 sequence

ETX-2I>config>port>log-mac(3)>classifier# drop
```

### match
```text
dst-mac
 src-mac
 ether-type
 <untagged>                                 : 
 vlan p-bit dei inner-ether-type inner-vlan inner-p-bit ip-dscp ip-precedence tos protocol src-ip dst-ip tcp-src-port tcp-dst-port udp-src-port udp-dst-port <any>                                      : 
 sequence to-flow

ETX-2I>config>port>log-mac(3)>classifier# match
```

### resequence
```text
<CR>
 <step>                                     : The step between sequence numbers 
                                              [1..10000, default 10]


ETX-2I>config>port>log-mac(3)>classifier# resequence
```

### show status
```text
<CR>

ETX-2I>config>port>log-mac(3)>classifier# show status
```

## configure port logical-mac NAME lldp

Level help (`?`):
```text
[no] 802.1-protocol-identity                 - Enable/disable transmission of 
                                                TLV for the specified protocol
      clear-statistics                        - 
 [no] nearest-bridge-802.3                    - Specifies tlv selection of  
                                                nearest-bridge
 [no] nearest-bridge-basic-management         - Specifies tlv selection of  
                                                nearest-bridge
 [no] nearest-bridge-mode                     - Set mode of operation of 
                                                nearest-bridge 

 show neighbors-details                       - Displays  the identifier of the
                                                  neighbor
 show neighbors-summary
 show statistics
```

### 802.1-protocol-identity
```text
<lldp>                                     : 
 <efm>                                      : 
 <cfm>                                      : 
 <802.1x>                                   : 
 <lag-lacp>                                 : 
 <rstp-mstp>                                : 
 <esmc>                                     : 
 <erp-v1>                                   : 
 <erp-v2>                                   : 
 <etp>                                      : 
 <elmi>                                     : 


ETX-2I>config>port>log-mac(3)>lldp# 802.1-protocol-identity
```

### clear-statistics
```text
<CR>

ETX-2I>config>port>log-mac(3)>lldp# clear-statistics
```

### nearest-bridge-802.3
```text
<mac-phy-configuration>                    : 
 <power-via-mdi>                            : 
 <max-frame-size>                           : 


ETX-2I>config>port>log-mac(3)>lldp# nearest-bridge-802.3
```

### nearest-bridge-basic-management
```text
<port-description>                         : 
 <sys-name>                                 : 
 <sys-description>                          : 
 <sys-capabilities>                         : 
 <management-address>                       : 


ETX-2I>config>port>log-mac(3)>lldp# nearest-bridge-basic-management
```

### nearest-bridge-mode
```text
<tx>                                       : 
 <rx>                                       : 
 <tx-rx>                                    : 


ETX-2I>config>port>log-mac(3)>lldp# nearest-bridge-mode
```

### show neighbors-details
```text
<CR>

ETX-2I>config>port>log-mac(3)>lldp# show neighbors-details
```

### show neighbors-summary
```text
<CR>

ETX-2I>config>port>log-mac(3)>lldp# show neighbors-summary
```

### show statistics
```text
<CR>

ETX-2I>config>port>log-mac(3)>lldp# show statistics
```

## configure port mng-ethernet

Level help (`?`):
```text
[no] pm-collection                           - Enable Performance Management 
                                                (PM)
```

### pm-collection
```text
<interval>                                 : PM collection interval
 <on-interval-close>                        : Collect PM only on interval close


ETX-2I>config>port>mng-eth# pm-collection
```

## configure port ppp NAME

Level help (`?`):
```text
[no] bind                                    - 
 [no] chap-hostname                           - CHAP hostname
 [no] chap-password                           - CHAP password
 [no] name                                    - Port name
 [no] pap-username                            - Configure PAP credentials
      pppoe                                   + 
 [no] refuse-chap                             - Refuse CHAP authentication
 [no] refuse-no-auth                          - Refuse no authentication
 [no] refuse-pap                              - Refuse PAP authentication

 show status
```

### bind
```text
<cellular>                                 : 
 <svi>                                      : 


ETX-2I>config>port>ppp(1)# bind
```

### chap-hostname
```text
<name>                                     : [1..80 chars]


ETX-2I>config>port>ppp(1)# chap-hostname
```

### chap-password
```text
<password>                                 : [1..80 chars]


ETX-2I>config>port>ppp(1)# chap-password
```

### name
```text
<string>                                   : [1..80 chars]


ETX-2I>config>port>ppp(1)# name
```

### pap-username
```text
<name>                                     : [1..80 chars]


ETX-2I>config>port>ppp(1)# pap-username
```

### refuse-chap
```text
<CR>

ETX-2I>config>port>ppp(1)# refuse-chap
```

### refuse-no-auth
```text
<CR>

ETX-2I>config>port>ppp(1)# refuse-no-auth
```

### refuse-pap
```text
<CR>

ETX-2I>config>port>ppp(1)# refuse-pap
```

### show status
```text
<CR>

ETX-2I>config>port>ppp(1)# show status
```

## configure port ppp NAME pppoe

Level help (`?`):
```text
[no] service-name                            - Configure Service-Name

 show status
```

### service-name
```text
<string>                                   : [1..80 chars]


ETX-2I>config>port>ppp(1)>pppoe# service-name
```

### show status
```text
<CR>

ETX-2I>config>port>ppp(1)>pppoe# show status
```

## configure port svi NAME

Level help (`?`):
```text
[no] name                                    - Assign name to the SVI port
 [no] shutdown                                - Administrtavly enable/disable 
                                                the SVI port
```

### name
```text
<string>                                   : SVI port name [1..64 chars]


ETX-2I>config>port>svi(1)# name
```

### shutdown
```text
<CR>

ETX-2I>config>port>svi(1)# shutdown
```

## configure protection

Level help (`?`):
```text
[no] erp                                     + Ethernet Ring Protection
 [no] ethernet-group                          + Enables/disables ethernet port 
                                                protection

 show erp-summary                             - Display list of all erp
```

### erp *(not entered — parameterized context)*
```text
<ring-number>                              : [number] [1..8]


ETX-2I>config>protection# erp
```

### ethernet-group *(not entered — parameterized context)*
```text
<group-id>                                 : Assigns a number for ethernet 
                                              group [number]


ETX-2I>config>protection# ethernet-group
```

### show erp-summary
```text
<CR>

ETX-2I>config>protection# show erp-summary
```

## configure pwe

Level help (`?`):
```text
[no] pw                                      + Create/delete Pseudo-wire

 show summary                                 - Display PWs summary
```

### pw *(not entered — parameterized context)*
```text
<pw-number>                                : A locally unique number which 
                                              represents the PW [number] [1..64]


ETX-2I>config>pwe# pw
```

### show summary
```text
<CR>

ETX-2I>config>pwe# show summary
```

## configure qos

Level help (`?`):
```text
[no] bandwidth-round-up                      - Selects Higher or Lower granular
                                                 rates 
 [no] color-map-profile                       + 
 [no] cos-map-profile                         + 
 [no] envelope-profile                        + 
      envelope-ranks                          - Sets number of ranks in envelope
                                                 profiles
 [no] marking-profile                         + Marking profiles map the Pbit, 
                                                IP precedence, or DSCP 
                                                classifications to user priority
 [no] policer-aggregate                       + 
 [no] policer-profile                         + 
 [no] queue-block-profile                     + 
 [no] queue-group-profile                     + 
 [no] queue-map-profile                       + 
 [no] shaper-profile                          + 
 [no] wred-profile                            +
```

### bandwidth-round-up
```text
<CR>

ETX-2I>config>qos# bandwidth-round-up
```

### color-map-profile *(parameterized — inner help harvested under "configure qos color-map-profile NAME")*
```text
<color-mapping-profile-name>               : [1..32 chars]


ETX-2I>config>qos# color-map-profile
```

### cos-map-profile *(parameterized — inner help harvested under "configure qos cos-map-profile NAME")*
```text
<cos-mapping-profile-name>                 : [1..32 chars]


ETX-2I>config>qos# cos-map-profile
```

### envelope-profile *(parameterized — inner help harvested under "configure qos envelope-profile NAME")*
```text
<envelope-profile-name>                    : [1..32 chars]


ETX-2I>config>qos# envelope-profile
```

### envelope-ranks
```text
<4>                                        : 
 <8>                                        : 


ETX-2I>config>qos# envelope-ranks
```

### marking-profile *(parameterized — inner help harvested under "configure qos marking-profile NAME")*
```text
<marking-profile-name>                     : [1..32 chars]


ETX-2I>config>qos# marking-profile
```

### policer-aggregate *(parameterized — inner help harvested under "configure qos policer-aggregate NAME")*
```text
<name>                                     : [1..32 chars]


ETX-2I>config>qos# policer-aggregate
```

### policer-profile *(parameterized — inner help harvested under "configure qos policer-profile NAME")*
```text
<policer-profile-name>                     : [1..32 chars]


ETX-2I>config>qos# policer-profile
```

### queue-block-profile *(parameterized — inner help harvested under "configure qos queue-block-profile NAME")*
```text
<queue-block-profile-name>                 : [1..32 chars]


ETX-2I>config>qos# queue-block-profile
```

### queue-group-profile *(parameterized — inner help harvested under "configure qos queue-group-profile NAME")*
```text
<queue-group-name>                         : [1..32 chars]


ETX-2I>config>qos# queue-group-profile
```

### queue-map-profile *(parameterized — inner help harvested under "configure qos queue-map-profile NAME")*
```text
<queue-mapping-profile-name>               : [1..32 chars]


ETX-2I>config>qos# queue-map-profile
```

### shaper-profile *(parameterized — inner help harvested under "configure qos shaper-profile NAME")*
```text
<shaper-profile-name>                      : [1..32 chars]


ETX-2I>config>qos# shaper-profile
```

### wred-profile *(not entered — parameterized context)*
```text
<wred-profile-name>                        : [1..32 chars]


ETX-2I>config>qos# wred-profile
```

## configure qos color-map-profile NAME

Level help (`?`):
```text
map                                     - 


ETX-2I>config>qos>color-map-profile(zzz-hrvst)$
```

### map
```text
<class-value>                              : [n1..n2]


ETX-2I>config>qos>color-map-profile(zzz-hrvst)$ map
```

## configure qos cos-map-profile NAME

Level help (`?`):
```text
map                                     - 
      untagged-map                            - 


ETX-2I>config>qos>cos-map-profile(zzz-hrvst)$
```

### map
```text
<class-value>                              : [n1..n2]


ETX-2I>config>qos>cos-map-profile(zzz-hrvst)$ map
```

### non-ip-map
```text
# cli error: Invalid Command
ETX-2I>config>qos>cos-map-profile(zzz-hrvst)$ non-ip-map
```

### untagged-map
```text
to-cos

ETX-2I>config>qos>cos-map-profile(zzz-hrvst)$ untagged-map
```

## configure qos envelope-profile NAME

Level help (`?`):
```text
[no] cf-policy                               - 
 [no] color-aware                             - Defines whether the policing 
                                                function assumes ingress frames 
                                                are already colored and must be 
                                                treated
      compensation                            - Extra bytes to be taken into 
                                                account
 [no] cos                                     + 

 show status                                  - Display Shaper status

ETX-2I>config>qos>envelope-profile(zzz-hrvst)$
```

### cf-policy
```text
<sharing-excess-bw>                        : 
 <uncoupled-bw-sharing>                     : 


ETX-2I>config>qos>envelope-profile(zzz-hrvst)$ cf-policy
```

### color-aware
```text
<CR>

ETX-2I>config>qos>envelope-profile(zzz-hrvst)$ color-aware
```

### compensation
```text
<value>                                    : Defines the layer1 overhead 
                                              (preamble and IFG) and the 
                                              overhead for the added VLAN header
                                               in case of [0..63, default 0]


ETX-2I>config>qos>envelope-profile(zzz-hrvst)$ compensation
```

### coupling-flag-0
```text
# cli error: Invalid Command
ETX-2I>config>qos>envelope-profile(zzz-hrvst)# coupling-flag-0
```

### show status
```text
<CR>

ETX-2I>config>qos>envelope-profile(zzz-hrvst)# show status
```

## configure qos envelope-profile NAME cos

Level help (`?`):
```text
[no] cf-policy                               - 
 [no] color-aware                             - Defines whether the policing 
                                                function assumes ingress frames 
                                                are already colored and must be 
                                                treated
      compensation                            - Extra bytes to be taken into 
                                                account
 [no] cos                                     + 

 show status                                  - Display Shaper status
```

### bandwidth
```text
# cli error: Invalid Command
ETX-2I>config>qos>envelope-profile(zzz-hrvst)# bandwidth
```

## configure qos marking-profile NAME

Level help (`?`):
```text
mark                                    - 


ETX-2I>config>qos>marking-profile(zzz-hrvst)$
```

### mark
```text
<user-priority>                            : [n1..n2]


ETX-2I>config>qos>marking-profile(zzz-hrvst)$ mark
```

### mark-dscp-code
```text
# cli error: Invalid Command
ETX-2I>config>qos>marking-profile(zzz-hrvst)$ mark-dscp-code
```

## configure qos policer-aggregate NAME

Level help (`?`):
```text
clear-statistics                        - 
      policer                                 - 
      rate-sampling-window                    - 

 show flows
 show statistics

ETX-2I>config>qos>policer-aggregate(zzz-hrvst)$
```

### clear-statistics
```text
<CR>

ETX-2I>config>qos>policer-aggregate(zzz-hrvst)$ clear-statistics
```

### policer
```text
<profile>                                  : 
 <envelope>                                 : 


ETX-2I>config>qos>policer-aggregate(zzz-hrvst)$ policer
```

### rate-sampling-window
```text
<minutes>                                  : Window size for sampling rate 
                                              statistics [Min.] [number]


ETX-2I>config>qos>policer-aggregate(zzz-hrvst)$ rate-sampling-window
```

### show flows
```text
<CR>

ETX-2I>config>qos>policer-aggregate(zzz-hrvst)$ show flows
```

### show statistics
```text
<running>                                  : 


ETX-2I>config>qos>policer-aggregate(zzz-hrvst)$ show statistics
```

## configure qos policer-profile NAME

Level help (`?`):
```text
bandwidth                               - 
 [no] color-aware                             - Defines whether the policing 
                                                function assumes ingress frames 
                                                are already colored and must be 
                                                treated
      compensation                            - Extra bytes to be taken into 
                                                account
 [no] coupling-flag                           - Defines the admission options 
                                                for Yellow Colored Frames.
      traffic-type                            - Defines the policed traffic type

 show status                                  - Display Shaper status
```

### bandwidth
```text
cir
 cbs
 eir
 ebs

ETX-2I>config>qos>policer-profile(50M-Policer)# bandwidth
```

### color-aware
```text
<CR>

ETX-2I>config>qos>policer-profile(50M-Policer)# color-aware
```

### compensation
```text
<value>                                    : Defines the layer1 overhead 
                                              (preamble and IFG) and the 
                                              overhead for the added VLAN header
                                               in case of [0..63, default 0]


ETX-2I>config>qos>policer-profile(50M-Policer)# compensation
```

### coupling-flag
```text
<CR>

ETX-2I>config>qos>policer-profile(50M-Policer)# coupling-flag
```

### show status
```text
<CR>

ETX-2I>config>qos>policer-profile(50M-Policer)# show status
```

### traffic-type
```text
<all>                                      : 
 <broadcast>                                : 
 <multicast>                                : 
 <unknown-unicast>                          : 
 <broadcast-and-multicast>                  : 
 <broadcast-and-multicast-and-unknown-un*>  : 


ETX-2I>config>qos>policer-profile(50M-Policer)# traffic-type
```

## configure qos queue-block-profile NAME

Level help (`?`):
```text
[no] queue                                   +
```

### queue *(not entered — parameterized context)*
```text
<queue-id>                                 : [number]


ETX-2I>config>qos>queue-block-profile(Scheduling2)# queue
```

## configure qos queue-group-profile NAME

Level help (`?`):
```text
[no] queue-block                             +
```

### queue-block *(parameterized — inner help harvested under "configure qos queue-group-profile NAME queue-block NAME")*
```text
<id>                                       :  [level_id/queue_id]


ETX-2I>config>qos>queue-group-profile(QGP-NNI)# queue-block
```

## configure qos queue-group-profile NAME queue-block NAME

Level help (`?`):
```text
name                                    - 
      profile                                 - 
 [no] shaper                                  -
```

### bind
```text
# cli error: Invalid Command
ETX-2I>config>qos>queue-group-profile(QGP-NNI)>queue-block(1/1)# bind
```

### name
```text
<block-name>                               : [1..32 chars]


ETX-2I>config>qos>queue-group-profile(QGP-NNI)>queue-block(1/1)# name
```

### profile
```text
<queue-block-profile-name>                 : [1..32 chars]


ETX-2I>config>qos>queue-group-profile(QGP-NNI)>queue-block(1/1)# profile
```

### shaper
```text
profile

ETX-2I>config>qos>queue-group-profile(QGP-NNI)>queue-block(1/1)# shaper
```

## configure qos queue-map-profile NAME

Level help (`?`):
```text
map                                     -
```

### map
```text
<class-value>                              : [n1..n2]


ETX-2I>config>qos>queue-map-profile(Pbit-Queue)# map
```

## configure qos shaper-profile NAME

Level help (`?`):
```text
bandwidth                               - 
      compensation                            - Extra bytes to be taken into 
                                                account

 show status                                  - Display Shaper status
```

### bandwidth
```text
cir
 cbs

ETX-2I>config>qos>shaper-profile(100M-Shaper)# bandwidth
```

### compensation
```text
<value>                                    : Defines the layer1 overhead 
                                              (preamble and IFG) and the 
                                              overhead for the added VLAN header
                                               in case of [number, default 0]


ETX-2I>config>qos>shaper-profile(100M-Shaper)# compensation
```

### show status
```text
<CR>

ETX-2I>config>qos>shaper-profile(100M-Shaper)# show status
```

## configure reporting

Level help (`?`):
```text
acknowledge                             - 
      active-alarm-rebuild                    - 
 [no] alarm-source-attribute                  - 
 [no] alarm-source-type-attribute             - 
      clear-accounting-log                    - Clear Syslog local accounting 
                                                log
      clear-alarm-log                         - 
 [no] led-blink                               - 
      log-file-timestamp-type                 - Configure log file timestamp 
                                                type
 [no] low-memory-alarm                        - Set thresholds for the low 
                                                memory alarms
 [no] mask-minimum-severity                   - 
 [no] pm                                      - Globally enable PM collection
 [no] pm-collection                           - Enable PM collection on entity 
                                                type
      pm-csv                                  - Parameters for CSV format
 [no] pm-file-push                            - Enable PM file push
      soaking-time                            - 

 show accounting-log                          - Dispay Syslog local accounting 
                                                 log
 show active-alarms
 show active-alarms-details
 show alarm-information
 show alarm-list
 show alarm-log
 show brief-alarm-log
 show brief-log
 show event-information
 show event-list
 show led-blink-status
 show log
 show log-summary
```

### acknowledge
```text
<log>                                      : 
 <brief-log>                                : 
 <activity-log>                             : 
 <all-logs>                                 : 


ETX-2I>config>reporting# acknowledge
```

### active-alarm-rebuild
```text
<CR>

 send-traps

ETX-2I>config>reporting# active-alarm-rebuild
```

### alarm-source-attribute
```text
<system>                                   : 
 <fan>                                      : 
 <power-supply>                             : 
 <mirroring>                                : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <domain-clock>                             : 
 <gnss>                                     : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <shdsl-fe>                                 : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <e1>                                       : 
 <t1>                                       : 
 <t3>                                       : 
 <e3>                                       : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# alarm-source-attribute
```

### alarm-source-type-attribute
```text
<system>                                   : 
 <fan>                                      : 
 <power-supply>                             : 
 <mirroring>                                : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <domain-clock>                             : 
 <card>                                     : 
 <ethernet>                                 : 
 <gnss>                                     : 
 <shdsl>                                    : 
 <shdsl-fe>                                 : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# alarm-source-type-attribute
```

### clear-accounting-log
```text
<CR>

ETX-2I>config>reporting# clear-accounting-log
```

### clear-alarm-log
```text
<log>                                      : 
 <brief-log>                                : 
 <activity-log>                             : 
 <all-logs>                                 : 


ETX-2I>config>reporting# clear-alarm-log
```

### led-blink
```text
<red>                                      : 
 <yellow>                                   : 


ETX-2I>config>reporting# led-blink
```

### log-file-timestamp-type
```text
<utc>                                      : 
 <local>                                    : 


ETX-2I>config>reporting# log-file-timestamp-type
```

### low-memory-alarm
```text
clear-threshold
 raise-threshold
 critical-raise-threshold

ETX-2I>config>reporting# low-memory-alarm
```

### mask-minimum-severity
```text
log
 snmp-trap
 led
 popup
 vty-popup

ETX-2I>config>reporting# mask-minimum-severity
```

### pm
```text
<CR>

ETX-2I>config>reporting# pm
```

### pm-collection
```text
<eth>                                      : Ethernet
 <flow>                                     : Flows
 <oam-cfm-service>                          : OAM CFM services
 <dest-ne>                                  : DEST-NE entities
 <twamp>                                    : TWAMP sessions
 <system>                                   : Memory usage and CPU utilization


ETX-2I>config>reporting# pm-collection
```

### pm-csv
```text
<CR>
 delimiter
 newline

ETX-2I>config>reporting# pm-csv
```

### pm-file-push
```text
server

ETX-2I>config>reporting# pm-file-push
```

### show accounting-log
```text
<CR>

ETX-2I>config>reporting# show accounting-log
```

### show active-alarms
```text
<CR>
 <system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <gnss>                                     : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <all>                                      : 
 <domain-clock>                             : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# show active-alarms
```

### show active-alarms-details
```text
<CR>
 <system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <gnss>                                     : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <all>                                      : 
 <domain-clock>                             : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# show active-alarms-details
```

### show alarm-information
```text
<system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <domain-clock>                             : 
 <gnss>                                     : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# show alarm-information
```

### show alarm-list
```text
<CR>
 <system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <domain-clock>                             : 
 <gnss>                                     : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 
 <all>                                      : 


ETX-2I>config>reporting# show alarm-list
```

### show alarm-log
```text
<CR>
 <system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <gnss>                                     : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <all>                                      : 
 <domain-clock>                             : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# show alarm-log
```

### show brief-alarm-log
```text
<CR>
 <system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <gnss>                                     : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <all>                                      : 
 <domain-clock>                             : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# show brief-alarm-log
```

### show brief-log
```text
<CR>
 <system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <gnss>                                     : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <all>                                      : 
 <domain-clock>                             : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# show brief-log
```

### show event-information
```text
<system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <domain-clock>                             : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# show event-information
```

### show event-list
```text
<CR>
 <system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <domain-clock>                             : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <all>                                      : 
 <tunnel>                                   : 


ETX-2I>config>reporting# show event-list
```

### show led-blink-status
```text
<CR>

ETX-2I>config>reporting# show led-blink-status
```

### show log
```text
<CR>
 <system>                                   : 
 <mirroring>                                : 
 <fan>                                      : 
 <power-supply>                             : 
 <station-clock>                            : 
 <recovered-clock>                          : 
 <g82751-recovered-clock>                   : 
 <g82751-master-clock>                      : 
 <g82752-recovered-clock>                   : 
 <g82752-master-clock>                      : 
 <g82752-recovered-master-clock>            : 
 <gnss>                                     : 
 <card>                                     : 
 <ethernet>                                 : 
 <shdsl>                                    : 
 <vdsl2>                                    : 
 <pcs>                                      : 
 <sdh-sonet>                                : 
 <e1>                                       : 
 <t1>                                       : 
 <e3>                                       : 
 <t3>                                       : 
 <vcg>                                      : 
 <bridge>                                   : 
 <bridge-port>                              : 
 <logical-mac>                              : 
 <etp>                                      : 
 <flow>                                     : 
 <gfp>                                      : 
 <lag>                                      : 
 <oam-efm>                                  : 
 <oam-cfm-mep>                              : 
 <oam-cfm-destne>                           : 
 <eps>                                      : 
 <erp>                                      : 
 <eth-protection>                           : 
 <router>                                   : 
 <router-interface>                         : 
 <pw>                                       : 
 <bgp>                                      : 
 <cellular>                                 : 
 <all>                                      : 
 <domain-clock>                             : 
 <recovered-clock-master>                   : 
 <domain-clock-source>                      : 
 <master-clock>                             : 
 <smart-sfp>                                : 
 <oam-cfm-r-mep>                            : 
 <erp-port>                                 : 
 <ospf>                                     : 
 <ospf-neighbor>                            : 
 <ospf-interface>                           : 
 <twamp-session>                            : 
 <twamp-peer>                               : 
 <twamp-responder>                          : 
 <tunnel>                                   : 


ETX-2I>config>reporting# show log
```

### show log-summary
```text
<CR>
 <number-records>                           : [number, default 10]


ETX-2I>config>reporting# show log-summary
```

### soaking-time
```text
interval
 clear

ETX-2I>config>reporting# soaking-time
```

## configure router NAME

Level help (`?`):
```text
[no] bfd-neighbor                            - Configure BFD neighbor
 [no] bgp                                     + Configure BGP
      clear-arp-table                         - Clear ARP table
      clear-bfd-statistics                    - Clear BFD statistics
      clear-dns-proxy-cache                   - Clear DNS proxy cache
      clear-neighbor-table                    - Clear neighbor table
      clear-statistics                        - Clear statistics (traffic, 
                                                access lists)
      dhcp-client                             + Configure DHCP client 
 [no] dhcp-relay-server                       - DHCP relay server address
      dscp                                    - Configure DSCP value
 [no] interface                               + Configure router interface
 [no] name                                    - Configure router name
 [no] nat                                     + Enable/disable-delete NAT 
                                                configuration
      nslookup                                - nslookup
 [no] ospf                                    + Configure OSPF
 [no] prefix-list                             + create and delete prefix-list 
                                                policy profile entity per router
                                                 entity
      resequence                              - Resequence policy profile
 [no] route-map                               + Command to create and delete 
                                                route-map policy profile entity 
                                                per router entity.
      static-preference                       - Set static route priority 
 [no] static-route                            - Configure static route 
 [no] tunnel-interface                        + Configure tunnel interface

 show access-list                             - ACL Information 
 show arp-table                               - Show ARP table
 show bfd-neighbors                           - Display BFD neighbors
 show bfd-neighbors-details                   - Display BFD neighbors
 show dns-proxy-cache
 show multicast-route
 show neighbor-table                          - Show IPv6 neighbor table
 show rib
 show routing-table                           - Show routing table
 show statistics                              - Show statistics
 show summary-interface                       - Show interface table
 show vrrp-summary
```

### bfd-neighbor
```text
<ip-address>                               : Neighbor IP address [0.0.0.0|
                                              0:0:0:0::0]


ETX-2I>config>router(1)# bfd-neighbor
```

### bgp *(parameterized — inner help harvested under "configure router NAME bgp NAME")*
```text
<as-number>                                : Set local AS [1..4294967295, 
                                              default 0]


ETX-2I>config>router(1)# bgp
```

### clear-arp-table
```text
<CR>

ETX-2I>config>router(1)# clear-arp-table
```

### clear-bfd-statistics
```text
<ip-address>                               : Neighbor IP address [0.0.0.0|
                                              0:0:0:0::0]


ETX-2I>config>router(1)# clear-bfd-statistics
```

### clear-dns-proxy-cache
```text
<CR>

ETX-2I>config>router(1)# clear-dns-proxy-cache
```

### clear-neighbor-table
```text
<CR>

ETX-2I>config>router(1)# clear-neighbor-table
```

### clear-statistics
```text
<all>                                      : Clear all statistics
 <ipv4>                                     : Clear IPv4 statistics
 <ipv6>                                     : Clear IPv6 statistics


ETX-2I>config>router(1)# clear-statistics
```

### dhcp-relay-server
```text
<address>                                  : DHCP relay server address [0.0.0.0
                                              |0:0:0:0::0]


ETX-2I>config>router(1)# dhcp-relay-server
```

### dscp
```text
<value>                                    : DSCP value  [0..63, default 0]


ETX-2I>config>router(1)# dscp
```

### interface *(parameterized — inner help harvested under "configure router NAME interface NAME")*
```text
<number>                                   : Router interface number [number] 
                                              [1..31]


ETX-2I>config>router(1)# interface
```

### name
```text
<string>                                   : Router name [1..32 chars]


ETX-2I>config>router(1)# name
```

### nslookup
```text
<ip-address>                               : ip-address or hostname [0.0.0.0|
                                              0:0:0:0::0|host-name]


ETX-2I>config>router(1)# nslookup
```

### prefix-list *(not entered — parameterized context)*
```text
<name>                                     : Set prefix-list policy profile 
                                              name. Profile name shall be unique
                                               in the system [1..252 chars]


ETX-2I>config>router(1)# prefix-list
```

### resequence
```text
<name>                                     : Policy profile to resequence 
                                              [1..252 chars]


ETX-2I>config>router(1)# resequence
```

### route-map *(parameterized — inner help harvested under "configure router NAME route-map NAME")*
```text
<name>                                     : Set route-map policy profile name.
                                               Profile name shall be unique in 
                                              the system. [1..252 chars]


ETX-2I>config>router(1)# route-map
```

### show access-list
```text
<summary>                                  : ACL summary


ETX-2I>config>router(1)# show access-list
```

### show arp-table
```text
<CR>
 address

ETX-2I>config>router(1)# show arp-table
```

### show bfd-neighbors
```text
<CR>

ETX-2I>config>router(1)# show bfd-neighbors
```

### show bfd-neighbors-details
```text
<CR>

ETX-2I>config>router(1)# show bfd-neighbors-details
```

### show dns-proxy-cache
```text
<CR>

ETX-2I>config>router(1)# show dns-proxy-cache
```

### show multicast-route
```text
<CR>

ETX-2I>config>router(1)# show multicast-route
```

### show neighbor-table
```text
<CR>
 address

ETX-2I>config>router(1)# show neighbor-table
```

### show rib
```text
<ipv4>                                     : 
 <ipv6>                                     : 


ETX-2I>config>router(1)# show rib
```

### show routing-table
```text
<CR>
 address
 protocol

ETX-2I>config>router(1)# show routing-table
```

### show statistics
```text
<ipv4>                                     : ipv4
 <ipv6>                                     : IPv6


ETX-2I>config>router(1)# show statistics
```

### show summary-interface
```text
<CR>

ETX-2I>config>router(1)# show summary-interface
```

### show vrrp-summary
```text
<CR>

ETX-2I>config>router(1)# show vrrp-summary
```

### static-preference
```text
<ipv4>                                     : IPv4
 <ipv6>                                     : IPv6


ETX-2I>config>router(1)# static-preference
```

### static-route
```text
<address-mask>                             : IP and mask [0.0.0.0/32|
                                              0:0:0:0::0/128]


ETX-2I>config>router(1)# static-route
```

### tunnel-interface *(not entered — parameterized context)*
```text
<number>                                   : Tunnel number [number] [1..32]


ETX-2I>config>router(1)# tunnel-interface
```

## configure router NAME bgp NAME

Level help (`?`):
```text
clear-neighbor                          - Restart BGP session 
      ipv4-unicast-af                         + Configure IPv4 unicast AF
      ipv6-unicast-af                         + Configure IPv6 unicast AF
 [no] neighbor                                + Configure BGP neighbor
      router-id                               - Configure router identifier
 [no] shutdown                                - Disable BGP 

 show community
 show rib
 show summary
```

### clear-neighbor
```text
<ip-address>                               : Neighbor IP address [0.0.0.0|
                                              0:0:0:0::0]


ETX-2I>config>router(1)>bgp(64515)# clear-neighbor
```

### neighbor *(parameterized — inner help harvested under "configure router NAME bgp NAME neighbor NAME")*
```text
<ip-address>                               : Neighbor IP address [0.0.0.0|
                                              0:0:0:0::0]


ETX-2I>config>router(1)>bgp(64515)# neighbor
```

### router-id
```text
<ip-address>                               : Router ID (IP address format) 
                                              [0.0.0.0]


ETX-2I>config>router(1)>bgp(64515)# router-id
```

### show community
```text
<ipv4>                                     : 
 <ipv6>                                     : 


ETX-2I>config>router(1)>bgp(64515)# show community
```

### show rib
```text
<ipv4>                                     : 
 <ipv6>                                     : 


ETX-2I>config>router(1)>bgp(64515)# show rib
```

### show summary
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)# show summary
```

### shutdown
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)# shutdown
```

## configure router NAME bgp NAME ipv4-unicast-af

Level help (`?`):
```text
external-preference                     - Configure external BGP route 
                                                priority
      internal-preference                     - Configure internal BGP route 
                                                priority
      neighbor                                + Configure BGP neighbor
 [no] network                                 - Configure BGP network
 [no] redistribute                            - Redistribute routes
```

### external-preference
```text
<priority>                                 : BGP route priority [0..255, 
                                              default 20]


ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af# external-preference
```

### internal-preference
```text
<priority>                                 : BGP route priority [0..255, 
                                              default 200]


ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af# internal-preference
```

### neighbor *(parameterized — inner help harvested under "configure router NAME bgp NAME ipv4-unicast-af neighbor NAME")*
```text
<ip-address>                               : Neighbor IP address [0.0.0.0|
                                              0:0:0:0::0]


ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af# neighbor
```

### network
```text
<prefix>                                   : Network prefix length [0.0.0.0/32]


ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af# network
```

### redistribute
```text
<static>                                   : Static
 <ospf>                                     : OSPF


ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af# redistribute
```

## configure router NAME bgp NAME ipv4-unicast-af neighbor NAME

Level help (`?`):
```text
[no] active                                  - Activate neighbor
 [no] prefix-list-bind                        - 
 [no] route-map-bind                          - 

 show advertised-route                        - Show advertised routes
 show prefix-list
 show received-route                          - Show received routes
 show route-map
```

### active
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(10.10.10.1)# active
```

### prefix-list-bind
```text
<name>                                     : [1..252 chars]


ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(10.10.10.1)# prefix-list-bind
```

### route-map-bind
```text
<name>                                     : [1..252 chars]


ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(10.10.10.1)# route-map-bind
```

### show advertised-route
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(10.10.10.1)# show advertised-route
```

### show prefix-list
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(10.10.10.1)# show prefix-list
```

### show received-route
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(10.10.10.1)# show received-route
```

### show route-map
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv4-unicast-af>neighbor(10.10.10.1)# show route-map
```

## configure router NAME bgp NAME ipv6-unicast-af

Level help (`?`):
```text
external-preference                     - Configure external BGP route 
                                                priority
      internal-preference                     - Configure internal BGP route 
                                                priority
      neighbor                                + Configure BGP neighbor
 [no] network                                 - Configure BGP network
 [no] redistribute                            - Redistribute routes
```

### external-preference
```text
<priority>                                 : BGP route priority [0..255, 
                                              default 20]


ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af# external-preference
```

### internal-preference
```text
<priority>                                 : BGP route priority [0..255, 
                                              default 200]


ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af# internal-preference
```

### neighbor *(parameterized — inner help harvested under "configure router NAME bgp NAME ipv6-unicast-af neighbor NAME")*
```text
<ip-address>                               : Neighbor IP address [0.0.0.0|
                                              0:0:0:0::0]


ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af# neighbor
```

### network
```text
<prefix>                                   : Network prefix length [0.0.0.0/32|
                                              0:0:0:0::0/128]


ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af# network
```

### redistribute
```text
<static>                                   : Static


ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af# redistribute
```

## configure router NAME bgp NAME ipv6-unicast-af neighbor NAME

Level help (`?`):
```text
[no] active                                  - Activate neighbor
 [no] prefix-list-bind                        - 
 [no] route-map-bind                          - 

 show advertised-route                        - Show advertised routes
 show prefix-list
 show received-route                          - Show received routes
 show route-map
```

### active
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10.10.10.1)# active
```

### prefix-list-bind
```text
<name>                                     : [1..252 chars]


ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10.10.10.1)# prefix-list-bind
```

### route-map-bind
```text
<name>                                     : [1..252 chars]


ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10.10.10.1)# route-map-bind
```

### show advertised-route
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10.10.10.1)# show advertised-route
```

### show prefix-list
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10.10.10.1)# show prefix-list
```

### show received-route
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10.10.10.1)# show received-route
```

### show route-map
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>ipv6-unicast-af>neighbor(10.10.10.1)# show route-map
```

## configure router NAME bgp NAME neighbor NAME

Level help (`?`):
```text
[no] local-address                           - Configure local address
      max-prefixes                            - Configure maximum prefixes
 [no] password                                - Configure password
      remote-as                               - Configure remote AS
 [no] shutdown                                - Disable neighbor
      timers                                  - Configure BGP timers

 show neighbor-connection                     - Show neighbor connection
```

### local-address
```text
<ip-address>                               : Neighbor local IP address [0.0.0.0
                                              |0:0:0:0::0]


ETX-2I>config>router(1)>bgp(64515)>neighbor(10.10.10.1)# local-address
```

### max-prefixes
```text
<number>                                   : Maximum prefixes [0..2147483647 , 
                                              default 0]


ETX-2I>config>router(1)>bgp(64515)>neighbor(10.10.10.1)# max-prefixes
```

### password
```text
<string>                                   : Password [0..80 chars]


ETX-2I>config>router(1)>bgp(64515)>neighbor(10.10.10.1)# password
```

### remote-as
```text
<as-number>                                : Remote AS number [1..4294967295]


ETX-2I>config>router(1)>bgp(64515)>neighbor(10.10.10.1)# remote-as
```

### show neighbor-connection
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>neighbor(10.10.10.1)# show neighbor-connection
```

### shutdown
```text
<CR>

ETX-2I>config>router(1)>bgp(64515)>neighbor(10.10.10.1)# shutdown
```

### timers
```text
keepalive
 holdtime

ETX-2I>config>router(1)>bgp(64515)>neighbor(10.10.10.1)# timers
```

## configure router NAME dhcp-client

Level help (`?`):
```text
[no] dhcpv6-option-request                   - Configure DHCPv6 option request 
                                                option
 [no] host-name                               - Configure DHCP option 12 (host 
                                                name) 
      vendor-class-id                         - Configure DHCP option 60 (vendor
                                                 class identifier)
```

### dhcpv6-option-request
```text
<CR>
 <vendor-specific-information-17>           : Vendor Specific Information 
                                              (option 17)


ETX-2I>config>router(1)>dhcp-client# dhcpv6-option-request
```

### host-name
```text
<name>                                     : User specified name
 <sys-name>                                 : System defined name


ETX-2I>config>router(1)>dhcp-client# host-name
```

### vendor-class-id
```text
<name>                                     : User specified name
 <ent-physical-name>                        : System defined name


ETX-2I>config>router(1)>dhcp-client# vendor-class-id
```

## configure router NAME interface NAME

Level help (`?`):
```text
[no] access-group                            - Apply ACL to device management
 [no] address                                 - Configure router interface IP
      bfd                                     - Assign BFD periodic control 
                                                packets
 [no] bind                                    - Bind router interface
      clear-statistics                        - Clear statistics (traffic, 
                                                access lists)
 [no] crypto-map                              - 
 [no] dhcp                                    - Enable DHCP client
      dhcp-client                             + Configure DHCP client 
 [no] dhcp-relay                              - Enable DHCP relay
 [no] dhcpv6-client                           - Enable DHCPv6 client
 [no] dhcpv6-server                           - 
 [no] ip-forwarding                           - Enable/disable IP forwarding
 [no] ipv6-address-prefix                     - 
 [no] ipv6-autoconfig                         - Enable IPv6 autoconfiguration
 [no] management-access                       - Configure managment access
      mtu                                     - Configure MTU
 [no] name                                    - Configure router interface name
 [no] ntp-multicast-client                    - Enable or disable NTP multicast
 [no] ospf                                    + Configure OSPF
 [no] pim                                     - Enable PIM sparse mode
 [no] shutdown                                - Disable router interface
 [no] unreachables                            - Enable ICMP unreachables 
 [no] vlan                                    - Configure router interface VLAN 
 [no] vrrp                                    + Define VRRP group

 show access-list                             - ACL Information 
 show crypto-maps-status
 show statistics                              - Show router interface 
                                                 statistics 
 show status                                  - Show router interface status
 show summary-vrrp
```

### access-group
```text
<acl-name>                                 : Access list to bind to router 
                                              interface [string]


ETX-2I>config>router(1)>interface(1)# access-group
```

### address
```text
<address-mask>                             : Router interface IP and mask 
                                              [0.0.0.0/32|0:0:0:0::0/128]


ETX-2I>config>router(1)>interface(1)# address
```

### bfd
```text
min-tx

ETX-2I>config>router(1)>interface(1)# bfd
```

### bind
```text
<ppp>                                      : PPP 
 <svi>                                      : SVI 
 <cellular>                                 : Cellular


ETX-2I>config>router(1)>interface(1)# bind
```

### clear-statistics
```text
<all>                                      : Clear all statistics
 <ipv4>                                     : IPv4 statistics
 <ipv6>                                     : IPv6 statistics


ETX-2I>config>router(1)>interface(1)# clear-statistics
```

### crypto-map
```text
<name>                                     : [1..80 chars]


ETX-2I>config>router(1)>interface(1)# crypto-map
```

### dhcp
```text
<CR>

ETX-2I>config>router(1)>interface(1)# dhcp
```

### dhcp-relay
```text
<CR>

ETX-2I>config>router(1)>interface(1)# dhcp-relay
```

### dhcpv6-client
```text
<CR>
 pd-name
 <rapid-commit>                             : 


ETX-2I>config>router(1)>interface(1)# dhcpv6-client
```

### dhcpv6-server
```text
<automatic>                                : 
 <pool>                                     : 


ETX-2I>config>router(1)>interface(1)# dhcpv6-server
```

### ip-forwarding
```text
<CR>

ETX-2I>config>router(1)>interface(1)# ip-forwarding
```

### ipv6-address-prefix
```text
<prefix-name>                              : [1..80 chars]


ETX-2I>config>router(1)>interface(1)# ipv6-address-prefix
```

### ipv6-autoconfig
```text
<CR>

ETX-2I>config>router(1)>interface(1)# ipv6-autoconfig
```

### management-access
```text
<allow-all>                                : Allow all
 <allow-ping>                               : Ping only


ETX-2I>config>router(1)>interface(1)# management-access
```

### mtu
```text
<bytes>                                    : MTU in bytes [1280..12288, default
                                               1500]


ETX-2I>config>router(1)>interface(1)# mtu
```

### name
```text
<string>                                   : Router interface name [1..32 
                                              chars]


ETX-2I>config>router(1)>interface(1)# name
```

### ntp-multicast-client
```text
<CR>

ETX-2I>config>router(1)>interface(1)# ntp-multicast-client
```

### ospf *(not entered — parameterized context)*
```text
<CR>

ETX-2I>config>router(1)>interface(1)# ospf
```

### pim
```text
<sparse-mode>                              : 


ETX-2I>config>router(1)>interface(1)# pim
```

### show access-list
```text
<summary>                                  : ACL summary


ETX-2I>config>router(1)>interface(1)# show access-list
```

### show crypto-maps-status
```text
<name>                                     : [1..80 chars]


ETX-2I>config>router(1)>interface(1)# show crypto-maps-status
```

### show statistics
```text
<ipv4>                                     : IPv4
 <ipv6>                                     : IPv6


ETX-2I>config>router(1)>interface(1)# show statistics
```

### show status
```text
<CR>

ETX-2I>config>router(1)>interface(1)# show status
```

### show summary-vrrp
```text
<CR>

ETX-2I>config>router(1)>interface(1)# show summary-vrrp
```

### shutdown
```text
<CR>

ETX-2I>config>router(1)>interface(1)# shutdown
```

### unreachables
```text
<CR>

ETX-2I>config>router(1)>interface(1)# unreachables
```

### vlan
```text
<id>                                       : VLAN ID [1..4094]


ETX-2I>config>router(1)>interface(1)# vlan
```

### vrrp *(not entered — parameterized context)*
```text
<vrid>                                     : [1..255]


ETX-2I>config>router(1)>interface(1)# vrrp
```

## configure router NAME interface NAME dhcp-client

Level help (`?`):
```text
client-id                               - Configure DHCP option 61 (client
                                                 identifier) 
      release                                 - Release a DHCP lease
      renew                                   - Renew a DHCP lease
```

### client-id
```text
<id>                                       : User defined string
 <mac>                                      : Device MAC address


ETX-2I>config>router(1)>interface(1)>dhcp-client# client-id
```

### release
```text
<CR>

ETX-2I>config>router(1)>interface(1)>dhcp-client# release
```

### renew
```text
<CR>

ETX-2I>config>router(1)>interface(1)>dhcp-client# renew
```

## configure router NAME nat

Level help (`?`):
```text
clear-nat-statistics                    - Clears NAT statistics counters
      clear-nat-translations                  - Clears NAT translation table
 [no] nat-inside-overload                     - Configure a NAPT rule inside to 
                                                outside
 [no] nat-inside-source-static                - Configure NAT rule inside to 
                                                outside
 [no] nat-inside-source-static-port           - Configure/modify/delete NAT rule
                                                 from the inside to outside 
      nat-timeout                             - Configure translation table 
                                                entries timeout

 show nat-statistics
 show nat-translations                        - Display NAT translation table
```

### clear-nat-statistics
```text
<CR>

ETX-2I>config>router(1)>nat# clear-nat-statistics
```

### clear-nat-translations
```text
<CR>

ETX-2I>config>router(1)>nat# clear-nat-translations
```

### nat-inside-overload
```text
source

ETX-2I>config>router(1)>nat# nat-inside-overload
```

### nat-inside-source-static
```text
<inside-ip>                                : IP Address of Inside IP station 
                                              [0.0.0.0]


ETX-2I>config>router(1)>nat# nat-inside-source-static
```

### nat-inside-source-static-port
```text
<tcp>                                      : Indicate that the configured port 
                                              number is associated with TCP 
 <udp>                                      : Indicate that the configured port 
                                              number is associated with UDP 


ETX-2I>config>router(1)>nat# nat-inside-source-static-port
```

### nat-timeout
```text
tcp
 udp
 others

ETX-2I>config>router(1)>nat# nat-timeout
```

### show nat-statistics
```text
<CR>

ETX-2I>config>router(1)>nat# show nat-statistics
```

### show nat-translations
```text
<CR>

ETX-2I>config>router(1)>nat# show nat-translations
```

## configure router NAME ospf

Level help (`?`):
```text
[no] area                                    + Configure OSPF area 
 [no] asbr                                    - Set router as ASBR
      external-preference                     - Set OSPF external route priority
                                                 
 [no] graceful-restart                        - Configure graceful restart 
      internal-preference                     - Set OSPF internal route priority
                                                 
 [no] redistribute                            - Redistribute external routes
      restart-interval                        - Configure graceful restart 
                                                interval
      router-id                               - Configure router ID
 [no] shutdown                                - Disable OSPF 
 [no] strict-lsa-checking                     - Configure strict LSA checking

 show database                                - Show database
 show interface-table                         - Show interface table
 show neighbor-table                          - Show neighbor table
 show statistics                              - Show statistics
```

### area *(not entered — parameterized context)*
```text
<area-id>                                  : Area ID [0.0.0.0]


ETX-2I>config>router(1)>ospf# area
```

### asbr
```text
<CR>

ETX-2I>config>router(1)>ospf# asbr
```

### external-preference
```text
<priority>                                 : Priority [0..255, default 110]


ETX-2I>config>router(1)>ospf# external-preference
```

### graceful-restart
```text
<CR>

ETX-2I>config>router(1)>ospf# graceful-restart
```

### internal-preference
```text
<priority>                                 : Priority [0..255, default 30]


ETX-2I>config>router(1)>ospf# internal-preference
```

### redistribute
```text
<static>                                   : Static
 <bgp>                                      : BGP


ETX-2I>config>router(1)>ospf# redistribute
```

### restart-interval
```text
<interval>                                 : Interval [0..1800, default 120]


ETX-2I>config>router(1)>ospf# restart-interval
```

### router-id
```text
<ip>                                       : Router ID (IP address format) 
                                              [0.0.0.0]


ETX-2I>config>router(1)>ospf# router-id
```

### show database
```text
<CR>

ETX-2I>config>router(1)>ospf# show database
```

### show interface-table
```text
<CR>

ETX-2I>config>router(1)>ospf# show interface-table
```

### show neighbor-table
```text
<CR>

ETX-2I>config>router(1)>ospf# show neighbor-table
```

### show statistics
```text
<CR>

ETX-2I>config>router(1)>ospf# show statistics
```

### shutdown
```text
<CR>

ETX-2I>config>router(1)>ospf# shutdown
```

### strict-lsa-checking
```text
<CR>

ETX-2I>config>router(1)>ospf# strict-lsa-checking
```

## configure router NAME route-map NAME

Level help (`?`):
```text
delete                                  - Remove statement from policy 
                                                profile
      deny                                    - Add deny statement to policy 
                                                profile
      permit                                  - Add permit statement to policy 
                                                profile
      remark                                  - Add remark statement to policy 
                                                profile


ETX-2I>config>router(1)>route-map(zzz-hrvst)$
```

### delete
```text
<sequence>                                 : [1..2147483648]


ETX-2I>config>router(1)>route-map(zzz-hrvst)$ delete
```

### deny
```text
<CR>
 <match>                                    : 
 <sequence>                                 : 


ETX-2I>config>router(1)>route-map(zzz-hrvst)$ deny
```

### permit
```text
<CR>
 <match>                                    : 
 <set>                                      : 
 <sequence>                                 : 


ETX-2I>config>router(1)>route-map(zzz-hrvst)$ permit
```

### remark
```text
<description>                              : [1..252 chars]


ETX-2I>config>router(1)>route-map(zzz-hrvst)$ remark
```

## configure system

Level help (`?`):
```text
[no] announcement                            - Post-login banner text
      clear-cpu-utilization                   - 
 [no] contact                                 - Contact name
      date-and-time                           + Configure date and time
      dhcp-relay                              + Enable DHCP Relay
 [no] dhcp-server                             + DHCP server level state
      interval-duration                       - 
      inventory                               + Specifies device inventory 
                                                parameters
      lldp                                    + Configures LLDP parameters on 
                                                all interfaces
 [no] location                                - Device location
 [no] login-message                           - Pre-login banner text
 [no] name                                    - Device name
      router                                  + Router global configuration
      syslog                                  + Configure Syslog
      tftp                                    - 
      xml-export                              - Export command output to XML 
                                                file

 show buffers
 show copyright                               - Display copyright message
 show cpu-utilization                         - Shows the CPU utilization
 show device-information                      - Display device information
 show memory                                  - Display memory usage
 show memory-details                          - Display memory usage in detail
 show summary-inventory                       - Displays a list with installed 
                                                 hardware and software
 show system-date                             - Display date and time
 show tech-support                            - Executes a predefined series of
                                                  commands
```

### announcement
```text
<message>                                  : 


ETX-2I>config>system# announcement
```

### clear-cpu-utilization
```text
<CR>

ETX-2I>config>system# clear-cpu-utilization
```

### contact
```text
<contact-person>                           : Contact name [0..255 chars, 
                                              default contact person]


ETX-2I>config>system# contact
```

### dhcp-server *(not entered — parameterized context)*
```text
<number>                                   : [1..1, default 1]


ETX-2I>config>system# dhcp-server
```

### interval-duration
```text
<5>                                        : 
 <10>                                       : 
 <15>                                       : 


ETX-2I>config>system# interval-duration
```

### inventory *(not entered — parameterized context)*
```text
<entity-index>                             : Unique identifier for device 
                                              inventory [number]


ETX-2I>config>system# inventory
```

### location
```text
<location-of-device>                       : Device location [0..255 chars, 
                                              default the location of this 
                                              device]


ETX-2I>config>system# location
```

### login-message
```text
<message>                                  : 


ETX-2I>config>system# login-message
```

### name
```text
<name-of-device>                           : Device name [0..255 chars]


ETX-2I>config>system# name
```

### show buffers
```text
<CR>

ETX-2I>config>system# show buffers
```

### show copyright
```text
<CR>

ETX-2I>config>system# show copyright
```

### show cpu-utilization
```text
<CR>

ETX-2I>config>system# show cpu-utilization
```

### show device-information
```text
<CR>

ETX-2I>config>system# show device-information
```

### show memory
```text
<CR>

ETX-2I>config>system# show memory
```

### show memory-details
```text
<CR>

ETX-2I>config>system# show memory-details
```

### show summary-inventory
```text
<CR>

ETX-2I>config>system# show summary-inventory
```

### show system-date
```text
<CR>

ETX-2I>config>system# show system-date
```

### show tech-support
```text
<CR>
 <file>                                     : 
 <terminal>                                 : Commands output is printed to 
                                              terminal screen


ETX-2I>config>system# show tech-support
```

### syslog *(not entered — parameterized context)*
```text
<device>                                   : Device
 <server>                                   : Server


ETX-2I>config>system# syslog
```

### tftp
```text
timeout

ETX-2I>config>system# tftp
```

### xml-export
```text
<show-summary-inventory>                   : 


ETX-2I>config>system# xml-export
```

## configure system date-and-time

Level help (`?`):
```text
date-format                             - Date format
      ntp                                     + Configure NTP client
      sntp                                    + Configure SNTP client
 [no] summer-time                             - Configure summer time begin and 
                                                end
      zone                                    - Time zone

 show summer-time                             - Show summer time details
```

### date-format
```text
<yyyy-mm-dd>                               : yyyy-mm-dd
 <dd-mm-yyyy>                               : dd-mm-yyyy
 <mm-dd-yyyy>                               : mm-dd-yyyy 
 <yyyy-dd-mm>                               : yyyy-dd-mm


ETX-2I>config>system>date-time# date-format
```

### show summer-time
```text
<CR>

ETX-2I>config>system>date-time# show summer-time
```

### summer-time
```text
<recurring>                                : 
 <date>                                     : 


ETX-2I>config>system>date-time# summer-time
```

### zone
```text
<utc>                                      : Universal Time Coordinated


ETX-2I>config>system>date-time# zone
```

## configure system date-and-time ntp

Level help (`?`):
```text
[no] authenticate                            - Enable NTP authentication
 [no] authentication-key                      - Configure NTP authentication key
 [no] multicast-client                        - Enable or disable NTP multicast 
                                                mode
      polling-interval                        - 
 [no] server                                  + NTP server level
 [no] trusted-key                             - 

 show status                                  - NTP status
```

### authenticate
```text
<CR>

ETX-2I>config>system>date-time>ntp# authenticate
```

### authentication-key
```text
<number>                                   : NTP authentication key number 
                                              [number]


ETX-2I>config>system>date-time>ntp# authentication-key
```

### multicast-client
```text
<CR>
 <multicast-ip-address>                     : IP multicast address to listen on 
                                              for NTP messages [0.0.0.0|
                                              0:0:0:0::0]


ETX-2I>config>system>date-time>ntp# multicast-client
```

### polling-interval
```text
min

ETX-2I>config>system>date-time>ntp# polling-interval
```

### server *(parameterized — inner help harvested under "configure system date-and-time ntp server NAME")*
```text
<server-id>                                : NTP server number [1..10]


ETX-2I>config>system>date-time>ntp# server
```

### show status
```text
<CR>

ETX-2I>config>system>date-time>ntp# show status
```

### trusted-key
```text
<number>                                   : [number]


ETX-2I>config>system>date-time>ntp# trusted-key
```

## configure system date-and-time ntp server NAME

Level help (`?`):
```text
address                                 - Configure NTP server IP address
 [no] key                                     - Configure NTP server 
                                                authentication key
 [no] prefer                                  - Preferred server
      query-server                            - Send server an NTP polling 
                                                request
 [no] shutdown                                - Enable SNTP server connection
```

### address
```text
<ip-address>                               : NTP server IP address [0.0.0.0|
                                              0:0:0:0::0|host-name]


ETX-2I>config>system>date-time>ntp>server(1)# address
```

### key
```text
<key-number>                               : [number]


ETX-2I>config>system>date-time>ntp>server(1)# key
```

### prefer
```text
<CR>

ETX-2I>config>system>date-time>ntp>server(1)# prefer
```

### query-server
```text
<CR>

ETX-2I>config>system>date-time>ntp>server(1)# query-server
```

### shutdown
```text
<CR>

ETX-2I>config>system>date-time>ntp>server(1)# shutdown
```

## configure system date-and-time sntp

Level help (`?`):
```text
[no] broadcast                               - Enable SNTP broadcast 
      poll-interval                           - Period of polling SNTP Server
 [no] server                                  + Specify SNTP Server
```

### broadcast
```text
<CR>

ETX-2I>config>system>date-time>sntp# broadcast
```

### poll-interval
```text
<minutes>                                  : Polling interval [1..1440, default
                                               15]


ETX-2I>config>system>date-time>sntp# poll-interval
```

### server *(parameterized — inner help harvested under "configure system date-and-time sntp server NAME")*
```text
<server-id>                                : SNTP server address [1..10]


ETX-2I>config>system>date-time>sntp# server
```

## configure system date-and-time sntp server NAME

Level help (`?`):
```text
address                                 - SNTP Server IP Address
 [no] prefer                                  - Preferred server
 [no] shutdown                                - Enable SNTP server connection
      udp                                     - UDP port
```

### address
```text
<ip-address>                               : SNTP Server IP Address [0.0.0.0|
                                              0:0:0:0::0|host-name]


ETX-2I>config>system>date-time>sntp>server(1)# address
```

### prefer
```text
<CR>

ETX-2I>config>system>date-time>sntp>server(1)# prefer
```

### shutdown
```text
<CR>

ETX-2I>config>system>date-time>sntp>server(1)# shutdown
```

### udp
```text
<default>                                  : Default Value for SNTP Server UDP 
                                              Port
 <port>                                     : 


ETX-2I>config>system>date-time>sntp>server(1)# udp
```

## configure system dhcp-relay

Level help (`?`):
```text
[no] dhcp-option-82                          - Enable DHCP option 82
 [no] dhcp-snooping                           - Enable DHCP snooping
      source-port                             - Configure DHCP relay source port
```

### dhcp-option-82
```text
<all>                                      : 
 <service>                                  : 


ETX-2I>config>system>dhcp-relay# dhcp-option-82
```

### dhcp-snooping
```text
<all>                                      : 
 <service>                                  : 


ETX-2I>config>system>dhcp-relay# dhcp-snooping
```

### source-port
```text
<default>                                  : 
 <udp>                                      : 


ETX-2I>config>system>dhcp-relay# source-port
```

## configure system lldp

Level help (`?`):
```text
bridge-type                             - Set device bridge type
      hold-multiplier                         - Assigns hold multiplier for lldp
      hold-time                               - Assigns hold-time for lldp
      port-description                        - Port description TLV source
 [no] shutdown                                - Administrtavly enable/disable 
                                                lldp on all interfaces
      tx-interval                             - Set transmit interval
```

### bridge-type
```text
<nearest-bridge>                           : 
 <customer-bridge>                          : 
 <non-tpmr-bridge>                          : 


ETX-2I>config>system>lldp# bridge-type
```

### hold-multiplier
```text
<seconds>                                  : Assigns hold multiplier in seconds
                                               for lldp transmission [1..100, 
                                              default 4]


ETX-2I>config>system>lldp# hold-multiplier
```

### hold-time
```text
<seconds>                                  : Assigns hold time in seconds for 
                                              lldp transmission [1..100, default
                                               4]


ETX-2I>config>system>lldp# hold-time
```

### port-description
```text
source

ETX-2I>config>system>lldp# port-description
```

### shutdown
```text
<CR>

ETX-2I>config>system>lldp# shutdown
```

### tx-interval
```text
<seconds>                                  : Assigns an interval number in 
                                              seconds for lldp transmission 
                                              [1..3600, default 30]


ETX-2I>config>system>lldp# tx-interval
```

## configure system router

Level help (`?`):
```text
[no] vrrp-ipv4-checksum-without-pseudoheade* - Whether or not VRRP checksum is 
                                                calculated with pseudoheader
      vrrp-version                            - Configure VRRP version

 show vrrp-summary
```

### show vrrp-summary
```text
<CR>

ETX-2I>config>system>router# show vrrp-summary
```

### vrrp-ipv4-checksum-without-pseudoheader
```text
<CR>

ETX-2I>config>system>router# vrrp-ipv4-checksum-without-pseudoheader
```

### vrrp-version
```text
<version>                                  : Can be one of: 2 or 3 [2..3, 
                                              default 2]


ETX-2I>config>system>router# vrrp-version
```

## configure terminal

Level help (`?`):
```text
baud-rate                               - Terminal baud rate
      console-timeout                         - Specifies the time of inactivity
                                                 after which the device 
                                                disconnects
      length                                  - Configure terminal screen size 
                                                (number of rows)
 [no] serial-port-disable                     - Disable serial port
      timeout                                 - Terminal timeout
```

### baud-rate
```text
<300bps>                                   : 300 bps
 <1200bps>                                  : 1200 bps
 <2400bps>                                  : 2400 bps
 <4800bps>                                  : 4800 bps
 <9600bps>                                  : 9600 bps
 <19200bps>                                 : 19200 bps
 <38400bps>                                 : 38400 bps
 <57600bps>                                 : 57600 bps
 <115200bps>                                : 115200 bps


ETX-2I>config>terminal# baud-rate
```

### console-timeout
```text
<forever>                                  : Disables disconnecting the device 
                                              in case of inactivity
 <limited>                                  : Enables disconnecting the device 
                                              in case of inactivity after a 
                                              specified time period


ETX-2I>config>terminal# console-timeout
```

### length
```text
<number-of-rows>                           : Number of rows to print before 
                                              pausing (or 0 for no pausing). 
                                              [0..255, default 20]


ETX-2I>config>terminal# length
```

### serial-port-disable
```text
<CR>

ETX-2I>config>terminal# serial-port-disable
```

### timeout
```text
<forever>                                  : No timeout
 <limited>                                  : Enable timeout


ETX-2I>config>terminal# timeout
```

## configure test

Level help (`?`):
```text
l3sat                                   + L3 service activation test
      rfc2544                                 + 
      y1564                                   + Ethernet service test per ITU-T 
                                                Y.1564
```

## configure test l3sat

Level help (`?`):
```text
[no] generator                               + Create/configure/activate a L3Sa
                                                 generaor
 [no] peer-profile                            + Create/modify/delete a L3Sat 
                                                peer profile
 [no] responder                               + Create/configure/activate a L3Sa
                                                 responder
 [no] session-profile                         + Create/modify/delete a L3Sat 
                                                session profile
```

### generator *(parameterized — inner help harvested under "configure test l3sat generator NAME")*
```text
<name>                                     : Assign a meaningful name to the 
                                              controller [1..32 chars]


ETX-2I>config>test>l3sat# generator
```

### peer-profile *(parameterized — inner help harvested under "configure test l3sat peer-profile NAME")*
```text
<name>                                     : [string]


ETX-2I>config>test>l3sat# peer-profile
```

### responder *(parameterized — inner help harvested under "configure test l3sat responder NAME")*
```text
<name>                                     : Assign a meaningful name to the 
                                              responder [1..32 chars]


ETX-2I>config>test>l3sat# responder
```

### session-profile *(parameterized — inner help harvested under "configure test l3sat session-profile NAME")*
```text
<name>                                     : [1..32 chars]


ETX-2I>config>test>l3sat# session-profile
```

## configure test l3sat generator NAME

Level help (`?`):
```text
local-ip-address                        - 
 [no] peer                                    + 
      router-entity                           - 
 [no] shutdown                                - 

 show status
```

### bind
```text
# cli error: Invalid Command
ETX-2I>config>test>l3sat>generator(2)# bind
```

### local-ip-address
```text
<ip-address>                               : [0.0.0.0|0:0:0:0::0]


ETX-2I>config>test>l3sat>generator(2)# local-ip-address
```

### peer *(parameterized — inner help harvested under "configure test l3sat generator NAME peer NAME")*
```text
<ip-address>                               : [0.0.0.0|0:0:0:0::0]


ETX-2I>config>test>l3sat>generator(2)# peer
```

### router-entity
```text
<number>                                   : [number]


ETX-2I>config>test>l3sat>generator(2)# router-entity
```

### show status
```text
<CR>

ETX-2I>config>test>l3sat>generator(2)# show status
```

### shutdown
```text
<CR>

ETX-2I>config>test>l3sat>generator(2)# shutdown
```

### vlan-tag
```text
# cli error: Invalid Command
ETX-2I>config>test>l3sat>generator(2)# vlan-tag
```

## configure test l3sat generator NAME peer NAME

Level help (`?`):
```text
[no] activate                                - Start/stop a L3SAT test at the 
                                                controller side
 [no] peer-profile                            - Assign the profile used in the 
                                                test
 [no] test-session                            - Assign the profile used in the 
                                                test

 show status                                  - Display the status of the peer
```

### activate
```text
<CR>

ETX-2I>config>test>l3sat>generator(2)>peer(192.168.30.31)# activate
```

### peer-profile
```text
<name>                                     : The profile used in the test 
                                              [1..32 chars]


ETX-2I>config>test>l3sat>generator(2)>peer(192.168.30.31)# peer-profile
```

### show status
```text
<CR>

ETX-2I>config>test>l3sat>generator(2)>peer(192.168.30.31)# show status
```

### test-session
```text
<name>                                     : The profile used in the test 
                                              [1..32 chars]


ETX-2I>config>test>l3sat>generator(2)>peer(192.168.30.31)# test-session
```

## configure test l3sat peer-profile NAME

Level help (`?`):
```text
bw-steps                                - Set the number of steps and 
                                                their transmission rate in the 
                                                CIR sub-test
      configuration-duration                  - Set the duration of the 
                                                configuration test
      performance-duration                    - Set the duration of the 
                                                performance test
 [no] policing-test                           - Set the policing test
      report-type                             - Indicates which metrics are 
                                                included in the report
 [no] scope                                   - Set the scope of the test: 
                                                configuration test, performance 
                                                test, or both phases
      udp-port                                - The start of the range of UDP 
                                                ports that are used in the tests
```

### bw-steps
```text
s1

ETX-2I>config>test>l3sat>peer-profile(1)# bw-steps
```

### configuration-duration
```text
<seconds>                                  : The duration, in seconds, of the 
                                              configuration test. This duration 
                                              is used for each tested P bit 
                                              [60..360, default 100]


ETX-2I>config>test>l3sat>peer-profile(1)# configuration-duration
```

### performance-duration
```text
<15m>                                      : 
 <2h>                                       : 
 <24h>                                      : 
 <custom>                                   : 


ETX-2I>config>test>l3sat>peer-profile(1)# performance-duration
```

### policing-test
```text
<CR>

ETX-2I>config>test>l3sat>peer-profile(1)# policing-test
```

### report-type
```text
<clock-sync>                               : 
 <no-clock-sync>                            : 


ETX-2I>config>test>l3sat>peer-profile(1)# report-type
```

### scope
```text
<configuration>                            : 
 <performance>                              : 


ETX-2I>config>test>l3sat>peer-profile(1)# scope
```

### udp-port
```text
<port-number>                              : Packets payload size in Bytes 
                                              units [number, default 256]


ETX-2I>config>test>l3sat>peer-profile(1)# udp-port
```

## configure test l3sat responder NAME

Level help (`?`):
```text
local-ip-address                        - 
      router-entity                           - 
 [no] shutdown                                - 
 [no] udp-port                                - The start of the range of UDP 
                                                ports that are used in the tests

 show status

ETX-2I>config>test>l3sat>responder(zzz-hrvst)$
```

### bind
```text
# cli error: Invalid Command
ETX-2I>config>test>l3sat>responder(zzz-hrvst)$ bind
```

### loaned-address
```text
# cli error: Invalid Command
ETX-2I>config>test>l3sat>responder(zzz-hrvst)$ loaned-address
```

### local-ip-address
```text
<ip-address>                               : [0.0.0.0|0:0:0:0::0]


ETX-2I>config>test>l3sat>responder(zzz-hrvst)$ local-ip-address
```

### router-entity
```text
<number>                                   : [number]


ETX-2I>config>test>l3sat>responder(zzz-hrvst)$ router-entity
```

### service-policer
```text
# cli error: Invalid Command
ETX-2I>config>test>l3sat>responder(zzz-hrvst)$ service-policer
```

### show status
```text
<CR>

ETX-2I>config>test>l3sat>responder(zzz-hrvst)$ show status
```

### shutdown
```text
<CR>

ETX-2I>config>test>l3sat>responder(zzz-hrvst)$ shutdown
```

### udp-port
```text
<port-number>                              : The start of the range of UDP 
                                              ports that are used in the tests 
                                              [number] [0..65504, default 53248]


ETX-2I>config>test>l3sat>responder(zzz-hrvst)$ udp-port
```

### vlan-tag
```text
# cli error: Invalid Command
ETX-2I>config>test>l3sat>responder(zzz-hrvst)$ vlan-tag
```

## configure test l3sat session-profile NAME

Level help (`?`):
```text
availability-threshold                  - Set the Availability service 
                                                acceptance criteria
      delay-threshold                         - Delay thresholdloss in micro-sec
      delay-variation-threshold               - Delay variation thresholdloss in
                                                 micro-sec
      ip-size                                 - Set the size of the test frames
 [no] l2-rate                                 - Set the calculation of test in 
                                                l2 rate
      loss-ratio-threshold                    - Loss Ratio Threshold in ppm 
                                                (Packet Per Million)


ETX-2I>config>test>l3sat>session-profile(zzz-hrvst)$
```

### availability-threshold
```text
<hundret-precent>                          : Set the Availability service 
                                              acceptance criteria [number, 
                                              default 9990]


ETX-2I>config>test>l3sat>session-profile(zzz-hrvst)$ availability-threshold
```

### delay-threshold
```text
<usec>                                     : Delay thresholdloss in micro-sec 
                                              [1000..1000000, default 200000]


ETX-2I>config>test>l3sat>session-profile(zzz-hrvst)$ delay-threshold
```

### delay-variation-threshold
```text
<usec>                                     : Delay variation threshold in 
                                              micro-sec [1000..1000000, default 
                                              100000]


ETX-2I>config>test>l3sat>session-profile(zzz-hrvst)$ delay-variation-threshold
```

### ip-size
```text
<CR>
 <64>                                       : 
 <128>                                      : 
 <256>                                      : 
 <512>                                      : 
 <1024>                                     : 
 <1280>                                     : 
 <1500>                                     : 
 <mtu>                                      : 
 <custom>                                   : 


ETX-2I>config>test>l3sat>session-profile(zzz-hrvst)$ ip-size
```

### l2-rate
```text
<CR>

ETX-2I>config>test>l3sat>session-profile(zzz-hrvst)$ l2-rate
```

### loss-ratio-threshold
```text
<ppm>                                      : Loss Ratio Threshold in ppm 
                                              (Packet Per Million) [1000..10000,
                                               default 1000]


ETX-2I>config>test>l3sat>session-profile(zzz-hrvst)$ loss-ratio-threshold
```

## configure test rfc2544

Level help (`?`):
```text
[no] profile-name                            + 
 [no] test                                    +
```

### profile-name *(parameterized — inner help harvested under "configure test rfc2544 profile-name NAME")*
```text
<name>                                     : [string]


ETX-2I>config>test>rfc2544# profile-name
```

### test *(not entered — parameterized context)*
```text
<id>                                       : [number]


ETX-2I>config>test>rfc2544# test
```

## configure test rfc2544 profile-name NAME

Level help (`?`):
```text
[no] eth-lck                                 - Enable/Disable the LCK
      frame-loss-tolerance                    - 
      frame-size                              - 
      frames-number-in-attempt                - 
 [no] learning-frames                         - 
      number-of-trials                        - 
      pattern                                 - 
      test-direction                          - 
      throughput-measurement-accuracy         - 
      tlv-type                                - 


ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$
```

### eth-lck
```text
<CR>

ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ eth-lck
```

### frame-loss-tolerance
```text
<frames>                                   : [number]


ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ frame-loss-tolerance
```

### frame-size
```text
<64>                                       : 
 <128>                                      : 
 <256>                                      : 
 <512>                                      : 
 <1024>                                     : 
 <1280>                                     : 
 <1518>                                     : 
 <1700>                                     : 
 <1900>                                     : 
 <2000>                                     : 
 custom

ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ frame-size
```

### frames-number-in-attempt
```text
<frames>                                   : [number]


ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ frames-number-in-attempt
```

### learning-frames
```text
<CR>
 number
 frequency

ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ learning-frames
```

### number-of-trials
```text
<value>                                    : [number]


ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ number-of-trials
```

### pattern
```text
<all-ones>                                 : 
 <all-zeroes-without-crc>                   : 
 <all-zeroes-with-crc>                      : 
 <alternate>                                : 
 <prbs-with-crc>                            : 
 <prbs-without-crc>                         : 


ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ pattern
```

### test-direction
```text
<unidirectional>                           : 
 <bidirectional>                            : 


ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ test-direction
```

### throughput-measurement-accuracy
```text
<bps>                                      : [number]


ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ throughput-measurement-accuracy
```

### tlv-type
```text
<test>                                     : 
 <data>                                     : 


ETX-2I>config>test>rfc2544>profile-name(zzz-hrvst)$ tlv-type
```

## configure test y1564

Level help (`?`):
```text
[no] generator                               + Create/configure/activate a 
                                                Y.1564 test session
 [no] profile                                 + Create/modify/delete a Y.1564 
                                                test profile
 [no] responder                               + Create/configure/enable a Y.1564
                                                 responder
```

### generator *(parameterized — inner help harvested under "configure test y1564 generator NAME")*
```text
<name>                                     : Assign a meaningful name to the 
                                              Y.1564 generator [1..32 chars]


ETX-2I>config>test>y1564# generator
```

### profile *(parameterized — inner help harvested under "configure test y1564 profile NAME")*
```text
<name>                                     : [1..32 chars]


ETX-2I>config>test>y1564# profile
```

### responder *(parameterized — inner help harvested under "configure test y1564 responder NAME")*
```text
<name>                                     : Assign a meaningful name to the 
                                              Y.1564 responder [1..32 chars]


ETX-2I>config>test>y1564# responder
```

## configure test y1564 generator NAME

Level help (`?`):
```text
[no] activate                                - Start/stop a Y.1564 test at the 
                                                generator side
 [no] bind                                    - Set the service to be tested
 [no] destination                             - Set the destination address
 [no] policer                                 - Optional set of a bandwidth 
                                                profile to be used during the 
                                                test
 [no] test-profile                            - Assign the profile used in the 
                                                test

 show status                                  - Display the status of the test
```

### activate
```text
<CR>

ETX-2I>config>test>y1564>generator(1)# activate
```

### bind
```text
<md>                                       : 
 <flow>                                     : 
 <service>                                  : 


ETX-2I>config>test>y1564>generator(1)# bind
```

### destination
```text
remote-mep

ETX-2I>config>test>y1564>generator(1)# destination
```

### policer
```text
<p-bit>                                    : The CoS to which the configuration
                                               applies [0..7]


ETX-2I>config>test>y1564>generator(1)# policer
```

### show mef46-ll-status
```text
# cli error: Invalid Command
ETX-2I>config>test>y1564>generator(1)# show mef46-ll-status
```

### show report
```text
# cli error: Invalid Command
ETX-2I>config>test>y1564>generator(1)# show report
```

### show status
```text
<CR>

ETX-2I>config>test>y1564>generator(1)# show status
```

### test-profile
```text
<name>                                     : The profile used in the test 
                                              [1..32 chars]


ETX-2I>config>test>y1564>generator(1)# test-profile
```

## configure test y1564 profile NAME

Level help (`?`):
```text
[no] auto-cos-completion                     - Set automatic creation of OAM 
                                                CFM services for tested P-bit 
                                                values
 [no] bandwidth-round-up                      - Set the rounding of transmit 
                                                rate of test frames
 [no] burst-test                              - Include or exclude the CBS and 
                                                EBS sub-tests from the 
                                                configuration phase
      cir-steps                               - Set the number of steps and 
                                                their transmission rate in the 
                                                CIR sub-test
 [no] color-aware                             - Set the color mode that is used 
                                                for the test
      configuration-duration                  - Set the duration of the 
                                                configuration test
      direction                               - Set the direction in which the 
                                                test is performed
      ethernet-type                           - Set the Ethertype of the test 
                                                frames
      frame-size                              - Set the size of the test frames
 [no] multi-frame-size                        - 
 [no] multiple-sa-mac                         - Set the source MAC address in 
                                                test frames
      one-way-thresholds                      - Set the one-way service 
                                                acceptance criteria
 [no] p-bit                                   + Create/modify/delete a Y.1564 
                                                test P-bit profile
      performance-duration                    - Set the duration of the 
                                                performance test
      rate-convention                         - Select whether rate measurements
                                                 are shown as 'data-rate' (IR) 
                                                or converted to 'line rate' 
                                                (ULR)
      responder-type                          - Select whether rate measurements
                                                 are shown as 'data-rate' (IR) 
                                                or converted to 'line rate' 
                                                (ULR)
      round-trip-thresholds                   - Set the round-trip service 
                                                acceptance criteria
      scope                                   - Set the scope of the test: 
                                                configuration test, performance 
                                                test, or both phases
 [no] traffic-policing                        - Include or exclude the traffic 
                                                policing sub-test from the 
                                                configuration phase
 [no] user-traffic-blocked                    - Set how user traffic is handled


ETX-2I>config>test>y1564>profile(zzz-hrvst)$
```

### auto-cos-completion
```text
<CR>

ETX-2I>config>test>y1564>profile(zzz-hrvst)$ auto-cos-completion
```

### bandwidth-round-up
```text
<CR>

ETX-2I>config>test>y1564>profile(zzz-hrvst)$ bandwidth-round-up
```

### burst-test
```text
<cbs>                                      : 
 <ebs>                                      : 


ETX-2I>config>test>y1564>profile(zzz-hrvst)$ burst-test
```

### cir-steps
```text
<CR>
 s1
 s2
 s3
 s4

ETX-2I>config>test>y1564>profile(zzz-hrvst)$ cir-steps
```

### color-aware
```text
<CR>

ETX-2I>config>test>y1564>profile(zzz-hrvst)$ color-aware
```

### configuration-duration
```text
<seconds>                                  : The duration, in seconds, of the 
                                              configuration test. This duration 
                                              is used for each tested P bit 
                                              [18..360, default 60]


ETX-2I>config>test>y1564>profile(zzz-hrvst)$ configuration-duration
```

### direction
```text
<unidirectional>                           : 
 <bidirectional>                            : 


ETX-2I>config>test>y1564>profile(zzz-hrvst)$ direction
```

### ethernet-type
```text
<value>                                    : [0x0000..0xFFFF, default 0x22E8]


ETX-2I>config>test>y1564>profile(zzz-hrvst)$ ethernet-type
```

### multi-frame-size
```text
<CR>

ETX-2I>config>test>y1564>profile(zzz-hrvst)$ multi-frame-size
```

### multiple-sa-mac
```text
<CR>
 base

ETX-2I>config>test>y1564>profile(zzz-hrvst)$ multiple-sa-mac
```

### one-way-thresholds
```text
<CR>
 flr
 ftd
 fdv
 availability

ETX-2I>config>test>y1564>profile(zzz-hrvst)$ one-way-thresholds
```

### performance-duration
```text
<15m>                                      : 
 <2h>                                       : 
 <24h>                                      : 
 <custom>                                   : 


ETX-2I>config>test>y1564>profile(zzz-hrvst)# performance-duration
```

### rate-convention
```text
<data-rate>                                : 
 <line-rate>                                : 


ETX-2I>config>test>y1564>profile(zzz-hrvst)# rate-convention
```

### responder-type
```text
<y1564>                                    : 
 <mac-swap>                                 : 
 <mef46-ll>                                 : 


ETX-2I>config>test>y1564>profile(zzz-hrvst)# responder-type
```

### round-trip-thresholds
```text
<CR>
 flr
 ftd
 fdv
 availability

ETX-2I>config>test>y1564>profile(zzz-hrvst)# round-trip-thresholds
```

### scope
```text
<configuration>                            : 
 <performance>                              : 


ETX-2I>config>test>y1564>profile(zzz-hrvst)# scope
```

### traffic-policing
```text
<CR>
 <no-bandwidth-roundup>                     : 
 <service>                                  : 


ETX-2I>config>test>y1564>profile(zzz-hrvst)# traffic-policing
```

### user-traffic-blocked
```text
<CR>

ETX-2I>config>test>y1564>profile(zzz-hrvst)# user-traffic-blocked
```

## configure test y1564 profile NAME p-bit

Level help (`?`):
```text
[no] auto-cos-completion                     - Set automatic creation of OAM 
                                                CFM services for tested P-bit 
                                                values
 [no] bandwidth-round-up                      - Set the rounding of transmit 
                                                rate of test frames
 [no] burst-test                              - Include or exclude the CBS and 
                                                EBS sub-tests from the 
                                                configuration phase
      cir-steps                               - Set the number of steps and 
                                                their transmission rate in the 
                                                CIR sub-test
 [no] color-aware                             - Set the color mode that is used 
                                                for the test
      configuration-duration                  - Set the duration of the 
                                                configuration test
      direction                               - Set the direction in which the 
                                                test is performed
      ethernet-type                           - Set the Ethertype of the test 
                                                frames
      frame-size                              - Set the size of the test frames
 [no] multi-frame-size                        - 
 [no] multiple-sa-mac                         - Set the source MAC address in 
                                                test frames
      one-way-thresholds                      - Set the one-way service 
                                                acceptance criteria
 [no] p-bit                                   + Create/modify/delete a Y.1564 
                                                test P-bit profile
      performance-duration                    - Set the duration of the 
                                                performance test
      rate-convention                         - Select whether rate measurements
                                                 are shown as 'data-rate' (IR) 
                                                or converted to 'line rate' 
                                                (ULR)
      responder-type                          - Select whether rate measurements
                                                 are shown as 'data-rate' (IR) 
                                                or converted to 'line rate' 
                                                (ULR)
      round-trip-thresholds                   - Set the round-trip service 
                                                acceptance criteria
      scope                                   - Set the scope of the test: 
                                                configuration test, performance 
                                                test, or both phases
 [no] traffic-policing                        - Include or exclude the traffic 
                                                policing sub-test from the 
                                                configuration phase
 [no] user-traffic-blocked                    - Set how user traffic is handled
```

### one-way-thresholds
```text
<CR>
 flr
 ftd
 fdv
 availability

ETX-2I>config>test>y1564>profile(zzz-hrvst)# one-way-thresholds
```

### round-trip-thresholds
```text
<CR>
 flr
 ftd
 fdv
 availability

ETX-2I>config>test>y1564>profile(zzz-hrvst)# round-trip-thresholds
```

## configure test y1564 responder NAME

Level help (`?`):
```text
[no] activate                                - Start/stop a Y.1564 test at the 
                                                respoder side
 [no] bind                                    - Set the service to be tested
 [no] destination                             - 
 [no] test-profile                            - Assign the profile used in the 
                                                test

 show status                                  - Display the status of the test

ETX-2I>config>test>y1564>responder(zzz-hrvst)$
```

### activate
```text
<CR>

ETX-2I>config>test>y1564>responder(zzz-hrvst)$ activate
```

### bind
```text
<md>                                       : 
 <flow>                                     : 
 <service>                                  : 


ETX-2I>config>test>y1564>responder(zzz-hrvst)$ bind
```

### destination
```text
<mac-address>                              : 
 <remote-mep>                               : 


ETX-2I>config>test>y1564>responder(zzz-hrvst)$ destination
```

### local-mac
```text
# cli error: Invalid Command
ETX-2I>config>test>y1564>responder(zzz-hrvst)$ local-mac
```

### show status
```text
<CR>

ETX-2I>config>test>y1564>responder(zzz-hrvst)$ show status
```

### test-profile
```text
<name>                                     : The profile used in the test 
                                              [1..32 chars]


ETX-2I>config>test>y1564>responder(zzz-hrvst)$ test-profile
```

## file

Level help (`?`):
```text
delete                                  - Delete file
      delete-user                             - Deletes a file from the device
 [no] description                             - Description of the file
      dir                                     - Display file directory
      user-file-dir                           - List of all user files in the 
                                                device

 show banner-text                             - Display banner  
 show configuration-files                     - Displays configuration files 
                                                 properties
 show copy                                    - Display Copy progress
 show factory-default-config                  - Display factory-default-config
 show file-details                            - Displays the details of the 
                                                 file
 show rollback-config                         - Display rollback-config 
 show schedule-log                            - Display schedule-log  
 show startup-config                          - Display startup-config 
 show sw-pack                                 - Display SW packs 
 show user-default-config                     - Display user-default-config 
 show user-dir
```

### delete
```text
<startup-config>                           : 
 <zero-touch-config-xml>                    : 
 <restore-point-config>                     : 
 <user-script>                              : 
 <script-result>                            : 


ETX-2I>file# delete
```

### delete-user
```text
<filename>                                 : [string]


ETX-2I>file# delete-user
```

### description
```text
<file-name>                                : The name of the file [1..37 chars]


ETX-2I>file# description
```

### dir
```text
<CR>

ETX-2I>file# dir
```

### show banner-text
```text
<CR>

ETX-2I>file# show banner-text
```

### show configuration-files
```text
<CR>

ETX-2I>file# show configuration-files
```

### show copy
```text
<CR>
 <summary>                                  : 


ETX-2I>file# show copy
```

### show factory-default-config
```text
<CR>

ETX-2I>file# show factory-default-config
```

### show file-details
```text
<filename>                                 : [string]


ETX-2I>file# show file-details
```

### show rollback-config
```text
<CR>

ETX-2I>file# show rollback-config
```

### show schedule-log
```text
<CR>

ETX-2I>file# show schedule-log
```

### show startup-config
```text
<CR>

ETX-2I>file# show startup-config
```

### show sw-pack
```text
<CR>

ETX-2I>file# show sw-pack
```

### show user-default-config
```text
<CR>

ETX-2I>file# show user-default-config
```

### show user-dir
```text
<filename>                                 : [string]


ETX-2I>file# show user-dir
```

### user-file-dir
```text
<CR>

ETX-2I>file# user-file-dir
```
