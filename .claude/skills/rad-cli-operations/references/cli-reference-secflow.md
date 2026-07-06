# secflow CLI reference (harvested `?` help)

Captured live from lab-sf1p (SF-1p-187 (SecFlow-1p, Sw 6.5.0.35) - pilot lab unit, safe for guarded write tests) on 2026-07-06 by scripts/harvest_cli.py
(re-run `harvest` after firmware upgrades — it diffs and updates in place).
Every section is a CLI context: first the level `?` listing (commands +
descriptions), then per-command argument help (`<command> ?`). Entries
marked *(not entered)* are parameterized contexts — their inner structure
is in command-tree-secflow.md; use cli_help with a real index for
inner argument syntax.

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

### bridge *(not entered — parameterized context)*
```text
<number>             : Bridge number [number]


SF-1p-187>config# bridge
```

### router *(not entered — parameterized context)*
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

### zone *(not entered — parameterized context)*
```text
<zone-name>          : Zone name [1..79 chars]


SF-1p-187>config>access-control>firewall# zone
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

### ca *(not entered — parameterized context)*
```text
<ca-name>            : CA name [1..20 chars]


SF-1p-187>config>crypto# ca
```

### crypto-map *(not entered — parameterized context)*
```text
<name>               : [1..80 chars]


SF-1p-187>config>crypto# crypto-map
```

### ipsec-transform-set *(not entered — parameterized context)*
```text
<name>               : [1..80 chars]


SF-1p-187>config>crypto# ipsec-transform-set
```

### isakmp-key
```text
<pre-shared-key>     : IKE pre-shared key [1..80 chars]


SF-1p-187>config>crypto# isakmp-key
```

### isakmp-policy *(not entered — parameterized context)*
```text
<sequence>           : [number]


SF-1p-187>config>crypto# isakmp-policy
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

### enroll-attributes *(not entered — parameterized context)*
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

### login-user *(not entered — parameterized context)*
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

### notify *(not entered — parameterized context)*
```text
<notify-name>        : Notification group name [string]


SF-1p-187>config>mngmnt>snmp# notify
```

### notify-filter *(not entered — parameterized context)*
```text
<name>               : Notification group name [string]


SF-1p-187>config>mngmnt>snmp# notify-filter
```

### notify-filter-profile *(not entered — parameterized context)*
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

### target *(not entered — parameterized context)*
```text
<name>               : Target name [1..32 chars]


SF-1p-187>config>mngmnt>snmp# target
```

### target-params *(not entered — parameterized context)*
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
```

## configure management tacacsplus

Level help (`?`):
```text
[no] group                          + TACACS+ server group
 [no] privilege-level                - Configure mapped between privilege level 
                                       to cli level
 [no] server                         + Add TACACS+ server
```

### group *(not entered — parameterized context)*
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

## configure monitor

Level help (`?`):
```text
[no] mirroring-session              + Configure mirroring session
```

### mirroring-session *(not entered — parameterized context)*
```text
<number>             : Mirroring session number [number]


SF-1p-187>config>monitor# mirroring-session
```

## configure oam

Level help (`?`):
```text
[no] ip-monitoring                  + Define ip-monitoring entity
```

### ip-monitoring *(not entered — parameterized context)*
```text
<name>               : Define ip-monitoring entity name [1..32 chars]


SF-1p-187>config>oam# ip-monitoring
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

### ethernet *(not entered — parameterized context)*
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

### ppp *(not entered — parameterized context)*
```text
<port-number>        : PPP Port number [number]


SF-1p-187>config>port# ppp
```

### serial *(not entered — parameterized context)*
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

### virtual *(not entered — parameterized context)*
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

### ssid *(not entered — parameterized context)*
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

## configure protection

Level help (`?`):
```text
[no] erp                            + ERP level
```

### erp *(not entered — parameterized context)*
```text
<number>             : Ring ID [1..239, default Index, no default]


SF-1p-187>config>protection# erp
```

## configure qos

Level help (`?`):
```text
[no] queue-block-profile            + Queue block profile configuration
 [no] queue-group-profile            + Queue group profile configuration
 [no] shaper-profile                 + Shaper profile configuration
```

### queue-block-profile *(not entered — parameterized context)*
```text
<profile-name>       : [1..32 chars]


SF-1p-187>config>qos# queue-block-profile
```

### queue-group-profile *(not entered — parameterized context)*
```text
<profile-name>       : [1..32 chars]


SF-1p-187>config>qos# queue-group-profile
```

### shaper-profile *(not entered — parameterized context)*
```text
<profile-name>       : [1..32 chars]


SF-1p-187>config>qos# shaper-profile
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
interval
 clear

SF-1p-187>config>reporting# soaking-time
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

SF-1p-187>config>sd-iot$
```

### authentication-method
```text
<psk>                : Password-based authentication
 <certificate>        : Certificate-based authentication


SF-1p-187>config>sd-iot$ authentication-method
```

### certificate
```text
<certificate-name>   : Sd-iot certificate name [1..64 chars]


SF-1p-187>config>sd-iot$ certificate
```

### clear-statistics
```text
<CR>

SF-1p-187>config>sd-iot$ clear-statistics
```

### client-number
```text
<number>             : Sd-iot client number [1..1000]


SF-1p-187>config>sd-iot$ client-number
```

### duplication
```text
<ethernet>           : Ethernet


SF-1p-187>config>sd-iot$ duplication
```

### ingress-port
```text
<ethernet>           : Ethernet


SF-1p-187>config>sd-iot$ ingress-port
```

### keep-alive
```text
interval
 retries

SF-1p-187>config>sd-iot$ keep-alive
```

### show statistics
```text
<CR>

SF-1p-187>config>sd-iot$ show statistics
```

### show status
```text
<CR>

SF-1p-187>config>sd-iot$ show status
```

### shutdown
```text
<CR>

SF-1p-187>config>sd-iot$ shutdown
```

### tunnel *(not entered — parameterized context)*
```text
<number>             : Sd-iot tunnel number [1..2]


SF-1p-187>config>sd-iot$ tunnel
```

### username
```text
<username-string>    : Sd-iot username [1..80 chars]


SF-1p-187>config>sd-iot$ username
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

### modbus-unit *(not entered — parameterized context)*
```text
<unit-name>          : Modbus unit local name [1..32 chars]


SF-1p-187>config>system# modbus-unit
```

### name
```text
<name-of-device>     : Device name [0..255 chars]


SF-1p-187>config>system# name
```

### opcua-server *(not entered — parameterized context)*
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

### server *(not entered — parameterized context)*
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

## configure system mqtt

Level help (`?`):
```text
[no] server                         + MQTT server level
```

### server *(not entered — parameterized context)*
```text
<name>               : Server name [1..32 chars]


SF-1p-187>config>system>mqtt# server
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
