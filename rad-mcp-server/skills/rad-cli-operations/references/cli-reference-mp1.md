# mp1 CLI reference (harvested `?` help)

Captured live from mp-one (MP-1 lab unit (provisional mp1 family - shared context-CLI assumed, NOT verified live)) on 2026-07-16 by scripts/harvest_cli.py
(re-run `harvest` after firmware upgrades — it diffs and updates in place).
Every section is a CLI context: first the level `?` listing (commands +
descriptions), then per-command argument help (`<command> ?`). Sections
ending in NAME are parameterized contexts harvested through one instance
(an existing one, or a temp object created and rolled back) — NAME stands
for any instance. Entries marked *(not entered)* could not be harvested
safely — their inner structure is in command-tree-mp1.md; use
cli_help with a real index for inner argument syntax.

## <root>

Level help (`?`):
```text
admin                          + Adminstrative commands
      configure                      + Configure device
      file                           + File commands
      logon                          - Allows to logon to debug level
      on-configuration-error         - Determines the device behavior when 
                                       encountering an error in configuration 
                                       file

Global commands:
      commit                         - Update the candidate database to the 
                                       running database
      copy                           - Copy file
      discard-changes                - Resets to last-saved parameter profile
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
      ping                           - Ping request to verify reachability of 
                                       remote host
 [no] popup-suspend                  - Suspends popup messages
      sanity-check                   - Initiates a self test of the device
      save                           - Save current settings
 [no] schedule                       - Schedule a command to run in a future 
                                       time
      telnet                         - Open telnet client session
      trace-route                    - Checks the path connectivity to a remote 
                                       device
      tree                           - Displays the command levels from the 
                                       current context downwards
```

### commit
```text
<CR>

MP-1# commit
```

### copy
```text
<source-file-url>    : <file-url> = <url-prefix> <file>
<url-prefix> = 
      tftp://<ipv4-address>/
      sftp://<username>:<password>@<ipv4-address>:<port>/
      xmodem:
<file> = 
      startup-config
      restore-point-config
      rollback-config
      running-config
      user-default-config
      factory-default-config
      log
      candidate-config
      sw-pack-1
      sw-pack-2
      zero-touch-config-xml
      banner-text
      pm-0
      db-schema
      mac-table
      db-config
      ltm_1
      ltm_2
      schedule-log
      sniffer-file
      user-script
      script-result
The maximum allowed length/range is:
      <username> [1..60 chars]
      <password> [1..60 chars]
      <file>     [1..96 chars]
      <port>     [1..65535]



MP-1# copy
```

### discard-changes
```text
<CR>

MP-1# discard-changes
```

### echo
```text
<CR>
 <text-to-echo>       : Text to display on screen [string]


MP-1# echo
```

### exec
```text
<user-script>        : 


MP-1# exec
```

### exit
```text
<CR>
 <all>                : Returns to Device context


MP-1# exit
```

### help
```text
<CR>
 <command-name>       : Command for which help is requested [string]


MP-1# help
```

### history
```text
<CR>

MP-1# history
```

### info
```text
<CR>
 <running>            : Displays data of currently active parameters
 <detail>             : Adds information to every conf. parameter


MP-1# info
```

### level-info
```text
<CR>
 <running>            : Displays data of currently active parameters
 <detail>             : Device configuration, including defaults


MP-1# level-info
```

### logon
```text
<debug>              : 


MP-1# logon
```

### logout
```text
<CR>

MP-1# logout
```

### on-configuration-error
```text
<ignore>             : Device continues running the file regardless of errors 
                        it may contain
 <stop>               : Device  stops upon first error in the file
 <reject>             : Device rejects the file completely and reboots


MP-1# on-configuration-error
```

### ping
```text
<ip-address>         : Specifies the IP address of the remote device [0.0.0.0|
                        0:0:0:0::0]


MP-1# ping
```

### popup-suspend
```text
<CR>

MP-1# popup-suspend
```

### sanity-check
```text
<CR>

MP-1# sanity-check
```

### save
```text
<CR>

MP-1# save
```

### schedule
```text
<name>               : Schedule name [string]


MP-1# schedule
```

### telnet
```text
<ip-address>         : Telnet destination IP address [0.0.0.0|0:0:0:0::0]


MP-1# telnet
```

### trace-route
```text
<ip-address>         : Specifies the IP address of the remote device [0.0.0.0|
                        0:0:0:0::0]


MP-1# trace-route
```

### tree
```text
<CR>
 <detail>             : Available commands, current context and downwards


MP-1# tree
```

## admin

Level help (`?`):
```text
factory-default-all            - Return to factory default and reboot
      factory-default                - Return to factory default configuration 
                                       and reboot
      reboot                         - Reboot device
      scheduler                      + Scheduler control commands
      software                       + Software installation
      user-default                   - Return to user default configuration and 
                                       reboot

 show reboot                         - Display scheduled reboot details
```

### factory-default
```text
<CR>

MP-1>admin# factory-default
```

### factory-default-all
```text
<CR>

MP-1>admin# factory-default-all
```

### reboot
```text
<CR>
 <in>                 : 
 <at>                 : 
 <cancel>             : 


MP-1>admin# reboot
```

### show reboot
```text
<CR>

MP-1>admin# show reboot
```

### user-default
```text
<CR>

MP-1>admin# user-default
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

MP-1>admin>scheduler# clear-finished-schedules
```

### clear-schedule-log
```text
<CR>

MP-1>admin>scheduler# clear-schedule-log
```

### show scheduler
```text
<CR>

MP-1>admin>scheduler# show scheduler
```

### show scheduler-details
```text
<CR>

MP-1>admin>scheduler# show scheduler-details
```

## admin software

Level help (`?`):
```text
install                        - Install software and reboot
      undo-install                   - Return to restore point

 show status                         - Show installation process
```

### install
```text
<sw-pack-1>          : sw-pack-1
 <sw-pack-2>          : sw-pack-2


MP-1>admin>software# install
```

### show status
```text
<CR>

MP-1>admin>software# show status
```

### undo-install
```text
<CR>

MP-1>admin>software# undo-install
```

## configure

Level help (`?`):
```text
access-control                 + Configure access control
      bridge                         + Configure bridge
      chassis                        + Configure chassis
      cross-connect                  + Cross connect of ATM, PW, or TDM 
                                       (DS0,DS1,DS3,SDH/SONET)
      crypto                         + Cryptography level
      flows                          + 
      management                     + Device management commands
 [no] peer                           - Create/delete peer
      port                           + Configure port
      protection                     + Defines protection mechanisms
      pwe                            + Create/delete Psaudo-wire
      qos                            + Quality of service
      reporting                      + 
 [no] router                         + Configure router 
      system                         + Defines system parameters
      terminal                       + Configure terminal

 show peer-summary
```

### bridge *(parameterized — inner help harvested under "configure bridge NAME")*
```text
<number>             : Bridge number [number]


MP-1>config# bridge
```

### peer
```text
<number>             : Number of configured peer [number] [1..16]


MP-1>config# peer
```

### router *(parameterized — inner help harvested under "configure router NAME")*
```text
<number>             : Router number [number] [1..1]


MP-1>config# router
```

### show peer-summary
```text
<CR>

MP-1>config# show peer-summary
```

## configure access-control

Level help (`?`):
```text
[no] access-list                    + Configure access control list 
 [no] logging                        - Set ACL logging interval
      resequence                     - Resequence ACL
```

### access-list *(not entered — parameterized context)*
```text
<ipv4>               : IPv4
 <acl-name>           : Access list name [1..80 chars]


MP-1>config>access-control# access-list
```

### logging
```text
access-list

MP-1>config>access-control# logging
```

### resequence
```text
access-list

MP-1>config>access-control# resequence
```

## configure bridge NAME

Level help (`?`):
```text
aging-time                     - Configure MAC aging time
      clear-mac-table                - Clear MAC address table
 [no] name                           - Configure bridge name
 [no] port                           + Configure bridge port
 [no] vlan                           + Configure VLAN

 show mac-table                      - Display MAC address table
 show vlans                          - Display VLAN membership
```

### aging-time
```text
<seconds>            : MAC aging time (seconds) [number, default 300] 
                        [60..3000]


MP-1>config>bridge(1)# aging-time
```

### clear-mac-table
```text
<CR>

MP-1>config>bridge(1)# clear-mac-table
```

### name
```text
<bridge-name>        : Bridge name [1..32 chars]


MP-1>config>bridge(1)# name
```

### port *(not entered — parameterized context)*
```text
<port-number>        : Bridge port number [number] [1..18]


MP-1>config>bridge(1)# port
```

### show mac-table
```text
<CR>
 vlan

MP-1>config>bridge(1)# show mac-table
```

### show vlans
```text
<CR>

MP-1>config>bridge(1)# show vlans
```

### vlan *(not entered — parameterized context)*
```text
<vlan-id>            : VLAN ID [1..4094]


MP-1>config>bridge(1)# vlan
```

## configure chassis

Level help (`?`):
```text
inventory                      + Specifies device inventory parameters
      temperature-threshold          - Configure temprature thresholds

 show environment                    - Display hardware status
 show summary-inventory              - Display inventory (physical entities)
```

### inventory *(parameterized — inner help harvested under "configure chassis inventory NAME")*
```text
<entity-index>       : Specify entity index [number]


MP-1>config>chassis# inventory
```

### show environment
```text
<CR>
 temperature

MP-1>config>chassis# show environment
```

### show summary-inventory
```text
<CR>

MP-1>config>chassis# show summary-inventory
```

### temperature-threshold
```text
<celsius>            : 
 <fahrenheit>         : 


MP-1>config>chassis# temperature-threshold
```

## configure chassis inventory NAME

Level help (`?`):
```text
[no] alias                          - Configure alias
 [no] asset-id                       - Configure asset identifier
 [no] serial-number                  - Configure serial number

 show status                         - Display entity details
```

### alias
```text
<string>             : Entity alias [1..32 chars]


MP-1>config>chassis>inventory(1001)# alias
```

### show status
```text
<CR>

MP-1>config>chassis>inventory(1001)# show status
```

## configure cross-connect

Level help (`?`):
```text
[no] ds0                            - DS0 (TimeSlot Assignment) Cross Connect 
                                       Command
 [no] pw-tdm                         - TDM virtual circuit cross connect
 [no] tdm                            - TDM (DS1) Cross Connect Command

 show summary
```

### ds0
```text
<e1>                 : 
 <ds1>                : 


MP-1>config>xc# ds0
```

### pw-tdm
```text
pw

MP-1>config>xc# pw-tdm
```

### show summary
```text
<all>                : 
 <ds0>                : 
 <pw>                 : 
 <tdm>                : 


MP-1>config>xc# show summary
```

### tdm
```text
<e1>                 : 
 <ds1>                : 


MP-1>config>xc# tdm
```

## configure crypto

Level help (`?`):
```text
key                            + RSA key management level
```

## configure crypto key

Level help (`?`):
```text
generate-rsa                   - Generate RSA key pair

 show my-public-key-rsa              - Display self RSA public key
```

### generate-rsa
```text
<CR>
 label
 size
 application

MP-1>config>crypto>key# generate-rsa
```

### show my-public-key-rsa
```text
<CR>

MP-1>config>crypto>key# show my-public-key-rsa
```

## configure flows

Level help (`?`):
```text
[no] classifier-profile             + 
 [no] flow                           + 

 show summary
```

### classifier-profile *(not entered — parameterized context)*
```text
<classification-n*>  : [1..32 chars]


MP-1>config>flows# classifier-profile

auto-create tried [classifier-profile zzz-hrvst, classifier-profile hrvst, classifier-profile z], all refused.
last device response ('classifier-profile z'): classifier-profile z
#                                       ^
# cli error: parameter or keyword missing or wrong
 - classifier-profile <classification-name> match-any
 - no classifier-profile <classification-name>
 <classification-n*>  : [1..32 chars]

MP-1>config>flows#
```

### flow *(parameterized — inner help harvested under "configure flows flow NAME")*
```text
<flow-name>          : [1..32 chars]


MP-1>config>flows# flow
```

### show summary
```text
<details>            : 


MP-1>config>flows# show summary
```

## configure flows flow NAME

Level help (`?`):
```text
[no] classifier                     - 
 [no] egress-port                    - 
 [no] ingress-port                   - 
 [no] reverse-direction              - 
 [no] shutdown                       - Enable/disable the flow
 [no] vlan-tag                       - 

 show status
```

### classifier
```text
<classification-n*>  : [1..32 chars]


MP-1>config>flows>flow(mng_access_defau)# classifier
```

### egress-port
```text
<svi>                : 
 <bridge-port>        : 


MP-1>config>flows>flow(mng_access_defau)# egress-port
```

### ingress-port
```text
<ethernet>           : 
 <svi>                : 
 <mng-ethernet>       : 


MP-1>config>flows>flow(mng_access_defau)# ingress-port
```

### reverse-direction
```text
<CR>

MP-1>config>flows>flow(mng_access_defau)# reverse-direction
```

### show status
```text
<CR>

MP-1>config>flows>flow(mng_access_defau)# show status
```

### shutdown
```text
<CR>

MP-1>config>flows>flow(mng_access_defau)# shutdown
```

### vlan-tag
```text
<push>               : 
 <pop>                : 


MP-1>config>flows>flow(mng_access_defau)# vlan-tag
```

## configure management

Level help (`?`):
```text
access                         + Specifies access paths and rights
      dscp                           - Configure DSCP value
 [no] login-user                     + Create user
 [no] management-address             - Configure management protocols source IP
      radius                         + Configure RADIUS client
      snmp                           + Defines SNMP settings
      tacacsplus                     + Configure TACACS+ client
 [no] user                           - Create user

 show ssh-server
 show users-details                  - Display connected users
 show users                          - Show users
```

### dscp
```text
<value>              : DSCP value [0..63, default 0]


MP-1>config>mngmnt# dscp
```

### login-user *(not entered — parameterized context)*
```text
<name>               : User name [1..20 chars]


MP-1>config>mngmnt# login-user
```

### management-address
```text
<ip-address>         : Management protocols source IP [0.0.0.0|0:0:0:0::0]


MP-1>config>mngmnt# management-address
```

### show ssh-server
```text
<fingerprint>        : 


MP-1>config>mngmnt# show ssh-server
```

### show users
```text
<CR>

MP-1>config>mngmnt# show users
```

### show users-details
```text
<CR>

MP-1>config>mngmnt# show users-details
```

### user
```text
<name>               : User name [1..20 chars]


MP-1>config>mngmnt# user
```

## configure management access

Level help (`?`):
```text
[no] access-group                   - Apply ACL to device management
      auth-policy                    - Set authentication sequence
      clear-statistics               - Clear ACL statistics
 [no] sftp                           - Enable SFTP
 [no] sftp-server                    - Enable SFTP Server
 [no] snmp                           - Enable SNMP 
      ssh-encryption                 - 
      ssh-key-exchange               - 
      ssh-mac                        - 
 [no] ssh                            - Enable SSH
 [no] telnet                         - Enable Telnet 
 [no] tftp                           - Enable TFTP

 show access-list                    - ACL Information 
 show statistics                     - Show ACL statistics
```

### access-group
```text
<acl-name>           : ACL name [string]


MP-1>config>mngmnt>access# access-group
```

### auth-policy
```text
<1st-level>          : First method


MP-1>config>mngmnt>access# auth-policy
```

### clear-statistics
```text
<ipv4>               : IPv4


MP-1>config>mngmnt>access# clear-statistics
```

### sftp
```text
<CR>

MP-1>config>mngmnt>access# sftp
```

### sftp-server
```text
<CR>

MP-1>config>mngmnt>access# sftp-server
```

### show access-list
```text
<summary>            : ACL summary


MP-1>config>mngmnt>access# show access-list
```

### show statistics
```text
<ipv4>               : IPv4


MP-1>config>mngmnt>access# show statistics
```

### snmp
```text
<CR>

MP-1>config>mngmnt>access# snmp
```

### ssh
```text
<CR>

MP-1>config>mngmnt>access# ssh
```

### ssh-encryption
```text
<all>                : 
 <algorithm>          : 


MP-1>config>mngmnt>access# ssh-encryption
```

### ssh-key-exchange
```text
<all>                : 
 <algorithm>          : 


MP-1>config>mngmnt>access# ssh-key-exchange
```

### ssh-mac
```text
<all>                : 
 <algorithm>          : 


MP-1>config>mngmnt>access# ssh-mac
```

### telnet
```text
<CR>

MP-1>config>mngmnt>access# telnet
```

### tftp
```text
<CR>

MP-1>config>mngmnt>access# tftp
```

## configure management radius

Level help (`?`):
```text
[no] attribute-send                 - Send RADIUS request with/without 
                                       atributes
      clear-statistics               - Clear RADIUS statistics
 [no] map-service-type               - Send service-type 
      server                         + Connect to RADIUS server

 show statistics                     - RADIUS  statistics
```

### attribute-send
```text
<nas-ip-address>     : 


MP-1>config>mngmnt>radius# attribute-send
```

### clear-statistics
```text
<CR>

MP-1>config>mngmnt>radius# clear-statistics
```

### map-service-type
```text
<unknown>            : 


MP-1>config>mngmnt>radius# map-service-type
```

### server *(not entered — parameterized context)*
```text
<server-id>          : Specify  RADIUS server  [1..4]


MP-1>config>mngmnt>radius# server
```

### show statistics
```text
<CR>

MP-1>config>mngmnt>radius# show statistics
```

## configure management snmp

Level help (`?`):
```text
[no] access-group                   + Configure access group
 [no] bootstrap-notification         - Enable/disable bootstrap notification 
                                       sending
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


MP-1>config>mngmnt>snmp# access-group

auto-create tried [access-group zzz-hrvst, access-group hrvst, access-group z], all refused.
last device response ('access-group z'): access-group z
#                                       ^
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

MP-1>config>mngmnt>snmp#
```

### bootstrap-notification
```text
<CR>

MP-1>config>mngmnt>snmp# bootstrap-notification
```

### community *(not entered — parameterized context)*
```text
<community-index>    : Community index [string]


MP-1>config>mngmnt>snmp# community
```

### config-change-notification
```text
<CR>

MP-1>config>mngmnt>snmp# config-change-notification
```

### notify *(parameterized — inner help harvested under "configure management snmp notify NAME")*
```text
<notify-name>        : Notification group name [string]


MP-1>config>mngmnt>snmp# notify
```

### notify-filter *(not entered — parameterized context)*
```text
<name>               : Notification group name [string]


MP-1>config>mngmnt>snmp# notify-filter

auto-create tried [notify-filter zzz-hrvst, notify-filter hrvst, notify-filter z], all refused.
last device response ('notify-filter z'): notify-filter z
#                                        ^
# cli error: parameter or keyword missing or wrong
 - notify-filter <name> <sub-tree-oid>
 - no notify-filter <name> <sub-tree-oid>
 <name>               : Notification group name [string]
 <sub-tree-oid>       : Sub-tree OID [1.3.6.1...]

MP-1>config>mngmnt>snmp#
```

### notify-filter-profile *(parameterized — inner help harvested under "configure management snmp notify-filter-profile NAME")*
```text
<params-name>        : Parameter name [string]


MP-1>config>mngmnt>snmp# notify-filter-profile
```

### security-to-group *(not entered — parameterized context)*
```text
<snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <usm>                : USM


MP-1>config>mngmnt>snmp# security-to-group

auto-create tried [security-to-group zzz-hrvst, security-to-group hrvst, security-to-group z], all refused.
last device response ('security-to-group z'): security-to-group z
#                                          ^
# cli error: invalid parameter value
 - security-to-group {snmpv1|snmpv2c|usm} sec-name <security-name>
 - no security-to-group {snmpv1|snmpv2c|usm} sec-name <security-name>
 <snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <usm>                : USM
 <security-name>      : Security name [string]

MP-1>config>mngmnt>snmp#
```

### show snmpv3
```text
information

MP-1>config>mngmnt>snmp# show snmpv3
```

### show trap-sync
```text
<CR>

MP-1>config>mngmnt>snmp# show trap-sync
```

### snmp-engine-id
```text
<mac>                : MAC
 <ipv4>               : IPv4
 <text>               : Free text


MP-1>config>mngmnt>snmp# snmp-engine-id
```

### target *(not entered — parameterized context)*
```text
<name>               : Target name [1..32 chars]


MP-1>config>mngmnt>snmp# target

auto-create tried [target zzz-hrvst, target hrvst, target z], all refused.
last device response ('target z'): target z
# cli error: Entry instance already exists
MP-1>config>mngmnt>snmp#
```

### target-params *(parameterized — inner help harvested under "configure management snmp target-params NAME")*
```text
<name>               : Target parameters name [1..32 chars]


MP-1>config>mngmnt>snmp# target-params
```

### trap-sync-group *(not entered — parameterized context)*
```text
<group-id>           : Group ID [number] [1..10]


MP-1>config>mngmnt>snmp# trap-sync-group
```

### user *(not entered — parameterized context)*
```text
<security-name>      : Security name [string]


MP-1>config>mngmnt>snmp# user
```

### view *(not entered — parameterized context)*
```text
<view-name>          : View name [string]


MP-1>config>mngmnt>snmp# view

auto-create tried [view zzz-hrvst, view hrvst, view z], all refused.
last device response ('view z'): view z
#                               ^
# cli error: parameter or keyword missing or wrong
 - view <view-name> <sub-tree-oid>
 - no view <view-name> <sub-tree-oid>
 <view-name>          : View name [string]
 <sub-tree-oid>       : Subtree OID [1.3.6.1...]

MP-1>config>mngmnt>snmp#
```

## configure management snmp notify NAME

Level help (`?`):
```text
[no] bind                           - Bind trap
 [no] shutdown                       - Disable notification group
      tag                            - Tag


MP-1>config>mngmnt>snmp>notify(zzz-hrvst)$
```

### bind
```text
<systemTraceMsgPr*>  : 
 <pwConfigMismatch>   : 
 <pwOamFailure>       : 
 <pwRdi>              : 
 <pwRxFailure>        : 
 <pwFeRdi>            : 
 <pwFeRxFailure>      : 
 <pwJitterBufferOv*>  : 
 <pwJitterBufferUn*>  : 
 <pwOamDelayTca>      : 
 <pwOamDelayTcaOff>   : 
 <pwFeDomainClockF*>  : 
 <coldStart>          : 
 <linkDown>           : 
 <linkUp>             : 
 <authenticationFa*>  : 
 <sanityTrap>         : 
 <cnfgFlipTrap>       : 
 <DyingGasp>          : 
 <systemDeviceTemp*>  : 
 <systemSoftwareIn*>  : 
 <systemSoftwareIn*>  : 
 <systemAlternateC*>  : 
 <systemConfigurat*>  : 
 <systemTraceMsgEx*>  : 
 <systemDeviceStar*>  : 
 <systemHardwareFa*>  : 
 <systemSwPackCorr*>  : 
 <systemStartupCon*>  : 
 <fanFailure>         : 
 <systemSuccessful*>  : 
 <systemFailedLogin>  : 
 <systemLogout>       : 
 <powerDeliveryFai*>  : 
 <systemTrapHardSy*>  : 
 <systemTrapHardSy*>  : 
 <systemConfigurat*>  : 
 <systemConfigChan*>  : 
 <systemUserReset>    : 
 <systemActiveSoft*>  : 
 <systemRunningCon*>  : 
 <systemBootstrap>    : 
 <alarmInput>         : 
 <systemAclLogging>   : 
 <systemResourceOv*>  : 
 <systemRemoteTerm*>  : 
 <systemRemoteTerm*>  : 
 <systemNtpAccurac*>  : 
 <systemSummerTime*>  : 
 <systemSummerTime*>  : 
 <systemFileOverflow> : 
 <systemTimeChanged>  : 
 <systemTimeSource*>  : 
 <systemSerialPort*>  : 
 <systemSerialPort*>  : 
 <systemFactoryDef*>  : 
 <systemLowMemory>    : 
 <systemCriticalLo*>  : 
 <systemNewSwFromB*>  : 
 <twampPeerTestSta*>  : 
 <twampPeerTestSto*>  : 
 <twampSessionLoss*>  : 
 <twampSessionDela*>  : 
 <twampSessionDela*>  : 
 <twampSessionUnav*>  : 
 <twampSessionForw*>  : 
 <twampSessionBack*>  : 
 <twampSessionForw*>  : 
 <twampSessionForw*>  : 
 <twampSessionForw*>  : 
 <twampSessionBack*>  : 
 <twampSessionBack*>  : 
 <twampSessionBack*>  : 
 <twampPeerTodAccu*>  : 
 <clockDomainSyste*>  : 
 <clockDomainStati*>  : 
 <sourceClockFailure> : 
 <stationClockAis>    : 
 <stationClockLof>    : 
 <stationClockLos>    : 
 <clockDomainStati*>  : 
 <clockDomainSyste*>  : 
 <clockDomainStati*>  : 
 <clockDomainSyste*>  : 
 <systemPmProcessD*>  : 
 <systemPmSpaceOve*>  : 
 <sfpNoResponse>      : 
 <sfpMismatch>        : 
 <sfpRemoved>         : 
 <sfpTemperatureOra>  : 
 <sfpOprOra>          : 
 <sfpOptOra>          : 
 <sfpOptOraOff>       : 
 <sfpLbcOra>          : 
 <sfpLbcOraOff>       : 
 <ethLos>             : 
 <pcsLinkDown>        : 
 <ethSilentStartNoRx> : 
 <adminDown>          : 
 <e1t1ExcessiveErr*>  : 
 <e1t1Ais>            : 
 <e1t1Lof>            : 
 <e1t1Rai>            : 
 <e1t1Lomf>           : 
 <e1t1Los>            : 
 <e1t1FrameSlip>      : 
 <e1t1Bpv>            : 
 <e1t1CrcError>       : 
 <e1t1Loopback>       : 
 <e1t1LoopbackOff>    : 
 <e1t1PortSwitchover> : 
 <ds1OptOpticalRec*>  : 
 <ds1OptDs1Lof>       : 
 <ds1OptC3794Lof>     : 
 <ds1OptDs1Rai>       : 
 <serialLof>          : 
 <serialRai>          : 
 <serialNoRts>        : 
 <serialLos>          : 
 <systemDownloadEnd>  : 
 <systemSftpServer*>  : 
 <systemSftpServer*>  : 


MP-1>config>mngmnt>snmp>notify(zzz-hrvst)$ bind
```

### shutdown
```text
<CR>

MP-1>config>mngmnt>snmp>notify(zzz-hrvst)$ shutdown
```

### tag
```text
<argument>           : Tag [string]


MP-1>config>mngmnt>snmp>notify(zzz-hrvst)$ tag
```

## configure management snmp notify-filter-profile NAME

Level help (`?`):
```text
profile-name                   - Profile name
 [no] shutdown                       - Disable notification group


MP-1>config>mngmnt>snmp>filter-profile$
```

### profile-name
```text
<argument>           : Profile name [string]


MP-1>config>mngmnt>snmp>filter-profile$ profile-name
```

### shutdown
```text
<CR>

MP-1>config>mngmnt>snmp>filter-profile$ shutdown
```

## configure management snmp target-params NAME

Level help (`?`):
```text
message-processing-model       - Configure message processing model
      security                       - Configure security
 [no] shutdown                       - Disable target parameters
      version                        - Configure SNMP version


MP-1>config>mngmnt>snmp>target(zzz-hrvst)$
```

### message-processing-model
```text
<snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <snmpv3>             : SNMPv3


MP-1>config>mngmnt>snmp>target(zzz-hrvst)$ message-processing-model
```

### security
```text
<CR>
 name
 level

MP-1>config>mngmnt>snmp>target(zzz-hrvst)$ security
```

### shutdown
```text
<CR>

MP-1>config>mngmnt>snmp>target(zzz-hrvst)$ shutdown
```

### version
```text
<snmpv1>             : SNMPv1
 <snmpv2c>            : SNMPv2c
 <usm>                : USM


MP-1>config>mngmnt>snmp>target(zzz-hrvst)$ version
```

## configure management tacacsplus

Level help (`?`):
```text
[no] group                          + TACACS+ server group
 [no] server                         + Add TACACS+ server
```

### group *(parameterized — inner help harvested under "configure management tacacsplus group NAME")*
```text
<group-name>         : TACACS+ server group name [1..32 chars]


MP-1>config>mngmnt>tacacsplus# group
```

### server *(parameterized — inner help harvested under "configure management tacacsplus server NAME")*
```text
<ip>                 : TACACS+ server IP address [0.0.0.0|0:0:0:0::0]


MP-1>config>mngmnt>tacacsplus# server
```

## configure management tacacsplus group NAME

Level help (`?`):
```text
[no] accounting                     - Enable TACACS+ accounting


MP-1>config>mngmnt>tacacsplus>group(zzz-hrvst)$
```

### accounting
```text
<shell>              : Shell accounting
 <system>             : System accounting
 <commands>           : Commands accounting


MP-1>config>mngmnt>tacacsplus>group(zzz-hrvst)$ accounting
```

## configure management tacacsplus server NAME

Level help (`?`):
```text
accounting-port                - Set  TACACS+ server accounting TCP port
      authentication-port            - Set  TACACS+ server authentication TCP 
                                       port
      clear-statistics               - Clear TACACS+ statistics
 [no] group                          - Bind TACACS+ server to group
      key                            - TACACS+ server shared secret
      retry                          - Number of authentication retries
 [no] shutdown                       - Disable TACACS+ server
      timeout                        - Timeout

 show statistics                     - Show TACACS+ statistics

MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$
```

### accounting-port
```text
<port-number>        : TCP port [1..65535, default 49]


MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$ accounting-port
```

### authentication-port
```text
<port-number>        : TCP port [1..65535, default 49]


MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$ authentication-port
```

### clear-statistics
```text
<CR>

MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$ clear-statistics
```

### group
```text
<group-name>         : TACACS+ server group name [1..32 chars]


MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$ group
```

### key
```text
<string>             : TACACS+ server shared secret [1..80 chars]


MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$ key
```

### retry
```text
<number-of-retries>  : Number of authentication retries [1..1, default 1]


MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$ retry
```

### show statistics
```text
<CR>

MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$ show statistics
```

### shutdown
```text
<CR>

MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$ shutdown
```

### timeout
```text
<seconds>            : Timeout in seconds [1..30, default 5]


MP-1>config>mngmnt>tacacsplus>server(1.1.1.1)$ timeout
```

## configure port

Level help (`?`):
```text
[no] analog-signaling-profile       + Add/Delete Analog signaling profile
      ds1                            + Configure DS1 port
      e1                             + Configure E1 port
      ethernet                       + Specifies Ethernet parameters
 [no] logical-mac                    + Configure Logical MAC 
      mng-ethernet                   + Specifies Ethernet management parameters
 [no] pcs                            + Configure Physical Coding Sublayer (PCS)
      pdh-frame-type                 - Configure the PDH frame type of E1/T1 
                                       ports on the chassis to be either E1 or 
                                       T1
      serial                         + Define SERIAL port parameters
 [no] svi                            + Create/delete service virtual interface

 show summary                        - Display port status summary
 show svi-summary
```

### analog-signaling-profile *(parameterized — inner help harvested under "configure port analog-signaling-profile NAME")*
```text
<name>               : profile name [1..32 chars]


MP-1>config>port# analog-signaling-profile
```

### ds1 *(parameterized — inner help harvested under "configure port ds1 NAME")*
```text
<port-index>         : Port number [slot/port]


MP-1>config>port# ds1
```

### e1 *(parameterized — inner help harvested under "configure port e1 NAME")*
```text
<port-index>         : Port number [slot/port]


MP-1>config>port# e1
```

### ethernet *(parameterized — inner help harvested under "configure port ethernet NAME")*
```text
<port-index>         : Port number [slot/port]


MP-1>config>port# ethernet
```

### logical-mac
```text
<CR>

MP-1>config>port# logical-mac
```

### mng-ethernet *(parameterized — inner help harvested under "configure port mng-ethernet NAME")*
```text
<port-index>         : Port number [slot/port]


MP-1>config>port# mng-ethernet
```

### pcs
```text
<CR>

MP-1>config>port# pcs
```

### pdh-frame-type
```text
<e1>                 : 
 <t1>                 : 


MP-1>config>port# pdh-frame-type
```

### serial *(parameterized — inner help harvested under "configure port serial NAME")*
```text
<port-number>        : Port number [slot/port]


MP-1>config>port# serial
```

### show summary
```text
<detail>             : 
 <counters>           : 


MP-1>config>port# show summary
```

### show svi-summary
```text
<CR>

MP-1>config>port# show svi-summary
```

### svi *(parameterized — inner help harvested under "configure port svi NAME")*
```text
<port-number>        : SVI port number [number] [1..96]


MP-1>config>port# svi
```

### t1 *(not entered — parameterized context)*
```text
# cli error: Invalid Command
MP-1>config>port# t1
```

## configure port analog-signaling-profile NAME

Level help (`?`):
```text
a-bit-rx                       - Define 'A' bit signaling in the Rx 
                                       direction
      a-bit-tx                       - Define 'A' bit signaling in the Tx 
                                       direction
      b-bit-rx                       - Define 'B' bit signaling in the Rx 
                                       direction
      b-bit-tx                       - Define 'B' bit signaling in the Tx 
                                       direction
      c-bit-rx                       - Define 'C' bit signaling in the Rx 
                                       direction
      c-bit-tx                       - Define 'C' bit signaling in the Tx 
                                       direction
      d-bit-rx                       - Define 'D' bit signaling in the Rx 
                                       direction
      d-bit-tx                       - Define 'D' bit signaling in the Tx 
                                       direction
```

### a-bit-rx
```text
<not-used>           : 
 <signaling>          : 
 <inverse-sig>        : 
 <forward-disconnect> : 
 <inverse-forward-*>  : 


MP-1>config>port>analog-signaling-pro(sig_over_a_bit)# a-bit-rx
```

### a-bit-tx
```text
<1>                  : 
 <0>                  : 
 <signaling>          : 
 <inverse-sig>        : 


MP-1>config>port>analog-signaling-pro(sig_over_a_bit)# a-bit-tx
```

### b-bit-rx
```text
<not-used>           : 
 <signaling>          : 
 <inverse-sig>        : 
 <forward-disconnect> : 
 <inverse-forward-*>  : 
 <wink>               : 


MP-1>config>port>analog-signaling-pro(sig_over_a_bit)# b-bit-rx
```

### b-bit-tx
```text
<1>                  : 
 <0>                  : 
 <signaling>          : 
 <inverse-sig>        : 
 <wink>               : 


MP-1>config>port>analog-signaling-pro(sig_over_a_bit)# b-bit-tx
```

### c-bit-rx
```text
<not-used>           : 
 <forward-disconnect> : 
 <wink>               : 


MP-1>config>port>analog-signaling-pro(sig_over_a_bit)# c-bit-rx
```

### c-bit-tx
```text
<1>                  : 
 <0>                  : 
 <signaling>          : 
 <wink>               : 


MP-1>config>port>analog-signaling-pro(sig_over_a_bit)# c-bit-tx
```

### d-bit-rx
```text
<not-used>           : 
 <signaling>          : 
 <inverse-sig>        : 


MP-1>config>port>analog-signaling-pro(sig_over_a_bit)# d-bit-rx
```

### d-bit-tx
```text
<1>                  : 
 <0>                  : 
 <signaling>          : 
 <inverse-sig>        : 


MP-1>config>port>analog-signaling-pro(sig_over_a_bit)# d-bit-tx
```

## configure port ds1 NAME

Level help (`?`):
```text
idle-code                      - Configure idle code
      line-type                      - Configure line type
 [no] name                           - Configure port name
 [no] shutdown                       - Disable port

 show status                         - Display port status
```

### clear-bert-counters
```text
# cli error: Invalid Command
MP-1>config>port>ds1(1/1)# clear-bert-counters
```

### line-type
```text
<unframed>           : Unframed
 <g732n>              : G.732N without CRC
 <g732s>              : G.732S without CRC


MP-1>config>port>ds1(1/1)# line-type
```

### name
```text
<string>             : Port name [1..64 chars]


MP-1>config>port>ds1(1/1)# name
```

### show status
```text
<CR>

MP-1>config>port>ds1(1/1)# show status
```

### shutdown
```text
<CR>

MP-1>config>port>ds1(1/1)# shutdown
```

## configure port e1 NAME

Level help (`?`):
```text
clear-statistics               - Clear port statistics
      idle-code                      - Configure idle code
      interface-type                 - Configure interface type
      line-type                      - Configure line type
 [no] loopback                       - Activate loopback
 [no] name                           - Configure port name
      out-of-service                 - Configure out of service signaling (OOS)
 [no] pm-collection                  - Enable Performance Management (PM) 
      rx-sensitivity                 - Configure Rx sensitivity
 [no] shutdown                       - Disable port
      tx-clock-source                - Configure Tx clock source

 show statistics                     - Display port statistics
 show status                         - Display port status
```

### clear-bert-counters
```text
# cli error: Invalid Command
MP-1>config>port>e1(1/1)# clear-bert-counters
```

### clear-statistics
```text
<CR>

MP-1>config>port>e1(1/1)# clear-statistics
```

### idle-code
```text
<idle-code-val>      : Idle code [0x00..0xFF]


MP-1>config>port>e1(1/1)# idle-code
```

### interface-type
```text
<balanced>           : Balanced
 <unbalanced>         : Unbalanced


MP-1>config>port>e1(1/1)# interface-type
```

### line-type
```text
<unframed>           : Unframed
 <g732n>              : G.732N without CRC
 <g732n-crc>          : G.732N with CRC
 <g732s>              : G.732S without CRC
 <g732s-crc>          : G.732S with CRC


MP-1>config>port>e1(1/1)# line-type
```

### loopback
```text
<local>              : Local loopback
 <remote>             : Remote loopback


MP-1>config>port>e1(1/1)# loopback
```

### name
```text
<string>             : Port name [1..64 chars]


MP-1>config>port>e1(1/1)# name
```

### out-of-service
```text
voice
 data
 signaling

MP-1>config>port>e1(1/1)# out-of-service
```

### pm-collection
```text
<interval>           : PM collection interval
 <on-interval-close>  : Collect PM only on interval close


MP-1>config>port>e1(1/1)# pm-collection
```

### rx-sensitivity
```text
<short-haul>         : Low sensitivity (-12dB)
 <long-haul>          : High sensitivity (-43dB)


MP-1>config>port>e1(1/1)# rx-sensitivity
```

### show statistics
```text
<current>            : Current statistics
 <interval>           : Interval statistics
 <total>              : Preceding 24 hours cumulative statistics
 <all-intervals>      : All interval statistics
 <all>                : All statistics


MP-1>config>port>e1(1/1)# show statistics
```

### show status
```text
<CR>

MP-1>config>port>e1(1/1)# show status
```

### shutdown
```text
<CR>

MP-1>config>port>e1(1/1)# shutdown
```

### tx-clock-source
```text
<loopback>           : Recovered Rx clock
 <through-timing>     : Indicates that recovered receive clock
 <domain>             : Clock provided by the system clock domain


MP-1>config>port>e1(1/1)# tx-clock-source
```

## configure port ethernet NAME

Level help (`?`):
```text
[no] auto-negotiation               - Enables/disables automatically adjusting 
                                       the speed
      clear-statistics               - Clears all statistics
      max-capability                 - Identifies the set of capabilities 
                                       advertised by the local autonegotiation 
                                       entity
 [no] name                           - Assigns/removes a port name
 [no] pm-collection                  - Enable Performance Management (PM) 
 [no] policer                        - Activates/deactivates a policer profile 
                                       with single queue
 [no] queue-group                    - Assigns/removes a queue group profile
 [no] queue-mapping                  - Assigns/removes a queue mapping profile
 [no] shutdown                       - Administratively disables/enables the 
                                       port
      speed-duplex                   - Specifies speed and duplex mode when 
                                       autonegotiation is disabled

 show statistics                     - Displays the Ethernet port statistics
 show status                         - Displays the Ethernet port status
```

### auto-negotiation
```text
<CR>

MP-1>config>port>eth(0/1)# auto-negotiation
```

### clear-statistics
```text
<CR>

MP-1>config>port>eth(0/1)# clear-statistics
```

### max-capability
```text
<10-half-duplex>     : Sets Max Capability to 10 BaseT Half Duplex
 <10-full-duplex>     : Sets Max Capability to 10 BaseT Full Duplex
 <100-half-duplex>    : Sets Max Capability to 100 BaseT Half Duplex
 <100-full-duplex>    : Sets Max Capability to 100 BaseT Full Duplex
 <1000-full-duplex>   : Sets Max Capability to 1000 BaseT Full Duplex
 <1000-x-full-duplex> : Sets Max Capability to 1000 BaseX, -LX, -SX, -CX Full 
                        Duplex


MP-1>config>port>eth(0/1)# max-capability
```

### name
```text
<string>             : Adds free text to assign a name to the port [1..64 
                        chars]


MP-1>config>port>eth(0/1)# name
```

### pm-collection
```text
<interval>           : PM collection interval
 <on-interval-close>  : Collect PM only on interval close


MP-1>config>port>eth(0/1)# pm-collection
```

### policer
```text
profile

MP-1>config>port>eth(0/1)# policer
```

### queue-group
```text
profile

MP-1>config>port>eth(0/1)# queue-group
```

### queue-mapping
```text
profile

MP-1>config>port>eth(0/1)# queue-mapping
```

### show sfp-status
```text
# cli error: Invalid Command
MP-1>config>port>eth(0/1)# show sfp-status
```

### show statistics
```text
<running>            : Displays the running statistics


MP-1>config>port>eth(0/1)# show statistics
```

### show status
```text
<CR>

MP-1>config>port>eth(0/1)# show status
```

### shutdown
```text
<CR>

MP-1>config>port>eth(0/1)# shutdown
```

### speed-duplex
```text
<10-half-duplex>     : Sets the interface to 10 BaseT Half Duplex
 <10-full-duplex>     : Sets the interface to 10 BaseT Full Duplex
 <100-half-duplex>    : Sets the interface to 100 BaseT Half Duplex
 <100-full-duplex>    : Sets the interface to 100 BaseT Full Duplex
 <1000-full-duplex>   : Sets the interface to 1000 BaseT Full Duplex
 <1000-x-full-duplex> : Sets the interface to 1000 BaseX, -LX, -SX, -CX Full 
                        Duplex


MP-1>config>port>eth(0/1)# speed-duplex
```

## configure port mng-ethernet NAME

Level help (`?`):
```text
clear-statistics               - Clears all statistics
 [no] name                           - Assigns/removes a port name
 [no] pm-collection                  - Enable Performance Management (PM) 
 [no] shutdown                       - Administratively disables/enables the 
                                       port

 show statistics                     - Displays the Ethernet port statistics
 show status                         - Displays the Ethernet port status
```

### clear-statistics
```text
<CR>

MP-1>config>port>mng-eth(0/0)# clear-statistics
```

### name
```text
<string>             : Adds free text to assign a name to the port [1..64 
                        chars]


MP-1>config>port>mng-eth(0/0)# name
```

### pm-collection
```text
<interval>           : PM collection interval
 <on-interval-close>  : Collect PM only on interval close


MP-1>config>port>mng-eth(0/0)# pm-collection
```

### show statistics
```text
<running>            : Displays the running statistics


MP-1>config>port>mng-eth(0/0)# show statistics
```

### show status
```text
<CR>

MP-1>config>port>mng-eth(0/0)# show status
```

### shutdown
```text
<CR>

MP-1>config>port>mng-eth(0/0)# shutdown
```

## configure port serial NAME

Level help (`?`):
```text
clear-statistics               - Clear the Serial port statistics
 [no] cts-rts                        - Selects the state of the local CTS line
      encapsulation-mode             - Define the data encapsulation mode
 [no] end-to-end-control             - Define the end-to-end transmission of the
                                        local DTR and RTS lines
      interface                      - Define serial interface type
 [no] loopback                       - Enables/disables loopback mode for the 
                                       port
 [no] name                           - Port name
      rate                           - Define the channel data rate (no 
                                       encapsulation)
 [no] shutdown                       - Administratively disables/enables the 
                                       port

 show statistics                     - Displays the Serial port statistics
 show status                         - Displays the Serial port status
```

### clear-statistics
```text
<CR>

MP-1>config>port>serial(1/1)# clear-statistics
```

### cts-rts
```text
<CR>

MP-1>config>port>serial(1/1)# cts-rts
```

### encapsulation-mode
```text
<v110>               : 
 <3-bit-transitional> : 
 <none>               : 


MP-1>config>port>serial(1/1)# encapsulation-mode
```

### end-to-end-control
```text
<CR>
 <rts>                : 


MP-1>config>port>serial(1/1)# end-to-end-control
```

### interface
```text
<v35>                : 
 <rs-422>             : 
 <rs-232>             : 


MP-1>config>port>serial(1/1)# interface
```

### loopback
```text
<local>              : 
 <remote>             : 
 <remote-on-remote>   : 


MP-1>config>port>serial(1/1)# loopback
```

### mode
```text
# cli error: Invalid Command
MP-1>config>port>serial(1/1)# mode
```

### name
```text
<string>             : [1..64 chars]


MP-1>config>port>serial(1/1)# name
```

### rate
```text
<1>                  : 
 <2>                  : 
 <3>                  : 
 <4>                  : 
 <5>                  : 
 <6>                  : 
 <7>                  : 
 <8>                  : 
 <9>                  : 
 <10>                 : 
 <11>                 : 
 <12>                 : 
 <13>                 : 
 <14>                 : 
 <15>                 : 
 <16>                 : 
 <17>                 : 
 <18>                 : 
 <19>                 : 
 <20>                 : 
 <21>                 : 
 <22>                 : 
 <23>                 : 
 <24>                 : 
 <25>                 : 
 <26>                 : 
 <27>                 : 
 <28>                 : 
 <29>                 : 
 <30>                 : 
 <31>                 : 


MP-1>config>port>serial(1/1)# rate
```

### show statistics
```text
<CR>

MP-1>config>port>serial(1/1)# show statistics
```

### show status
```text
<CR>

MP-1>config>port>serial(1/1)# show status
```

### shutdown
```text
<CR>

MP-1>config>port>serial(1/1)# shutdown
```

## configure port svi NAME

Level help (`?`):
```text
[no] name                           - Assign name to the SVI port
 [no] shutdown                       - Administrtavly enable/disable the SVI 
                                       port

 show status
```

### name
```text
<string>             : SVI port name [1..64 chars]


MP-1>config>port>svi(1)# name
```

### show status
```text
<CR>

MP-1>config>port>svi(1)# show status
```

### shutdown
```text
<CR>

MP-1>config>port>svi(1)# shutdown
```

## configure protection

Level help (`?`):
```text
[no] pw                             + Input/Output pw protection group 
                                       configuration
 [no] tdm-group                      + Define tdm protection group
```

### pw *(parameterized — inner help harvested under "configure protection pw NAME")*
```text
<group-id>           : Unique number that should identify the protection group.
                         [number] [1..16]


MP-1>config>protection# pw
```

### show summary-tdm-group
```text
<CR>

MP-1>config>protection# show summary-tdm-group
```

### tdm-group *(not entered — parameterized context)*
```text
<group-id>           : [number] [1..8]


MP-1>config>protection# tdm-group

auto-create tried [tdm-group zzz-hrvst, tdm-group hrvst, tdm-group z], all refused.
last device response ('tdm-group z'): tdm-group z
#                                 ^
# cli error: invalid parameter value
 - tdm-group <group-id>
 - no tdm-group <group-id>
 <group-id>           : [number] [1..8]

MP-1>config>protection#
```

## configure protection pw NAME

Level help (`?`):
```text
[no] bind                           - Bind a card to an IO card group.
 [no] name                           - 
      oper-mode                      - Input/output card protection group 
                                       operational mode
 [no] shutdown                       - Enables/disables an IO card protection 
                                       group

 show status                         - Display status of Input/Output card 
                                        protection group.

MP-1>config>protection>pw(1)$
```

### bind
```text
<working>            : 
 <protection>         : 


MP-1>config>protection>pw(1)$ bind
```

### name
```text
<string>             : [1..32 chars]


MP-1>config>protection>pw(1)$ name
```

### oper-mode
```text
<1-plus-1>           : 


MP-1>config>protection>pw(1)$ oper-mode
```

### show status
```text
<CR>

MP-1>config>protection>pw(1)$ show status
```

### shutdown
```text
<CR>

MP-1>config>protection>pw(1)$ shutdown
```

## configure pwe

Level help (`?`):
```text
[no] pw                             + Create/delete Pseudo-wire

 show summary                        - Display PWs summary
```

### pw *(parameterized — inner help harvested under "configure pwe pw NAME")*
```text
<pw-number>          : A locally unique number which represents the PW [number]
                         [1..32]


MP-1>config>pwe# pw
```

### show summary
```text
<CR>

MP-1>config>pwe# show summary
```

## configure pwe pw NAME

Level help (`?`):
```text
[no] arp-table-refresh              - Controls whether the next-hop MAC is 
                                       periodically refreshed according to the 
                                       ARP table.
 [no] description                    - The name given to the specified PW
 [no] domain-failure-indication      - Controls whether the PW carry failure 
                                       indication if local domain clock fails.
      jitter-buffer                  - Jitter buffer size
 [no] jitter-buffer-centering        - Sets the threshold that causes jitter 
                                       buffer flush to re-center it.
      label                          - The PW label used in the inbound 
                                       /outbound direction
 [no] name                           - The name given to the specified PW
 [no] peer                           - The number of the remote peer which 
                                       terminated this PW 
 [no] pm-collection                  - Enable Performance Management (PM) 
 [no] shutdown                       - Administrativly enable/disable the 
                                       current PW
      source-clock-fail              - Conditions when the PW is considered 
                                       failed for the CSM.
      tdm-oos                        - Transmits an out of service signal (oos)
      tdm-payload                    - TDM payload parameters
      tos                            - Configures the value of the IP TOS byte 
                                       in egress packets
      udp-mux-method                 - 

 show statistics                     - Display PW statistics counters
 show status                         - Display PW status parameters

MP-1>config>pwe>pw(1)$
```

### arp-table-refresh
```text
<CR>

MP-1>config>pwe>pw(1)$ arp-table-refresh
```

### clear-statistics
```text
# cli error: Invalid Command
MP-1>config>pwe>pw(1)$ clear-statistics
```

### description
```text
<pw-description>     : The description given to the specified PW  [1..80 chars]


MP-1>config>pwe>pw(1)$ description
```

### domain-failure-indication
```text
<CR>

MP-1>config>pwe>pw(1)$ domain-failure-indication
```

### egress-port
```text
# cli error: Invalid Command
MP-1>config>pwe>pw(1)$ egress-port
```

### exp-bits
```text
# cli error: Invalid Command
MP-1>config>pwe>pw(1)$ exp-bits
```

### jitter-buffer
```text
<jitter-size>        : Jitter buffer size in usec [number]


MP-1>config>pwe>pw(1)$ jitter-buffer
```

### jitter-buffer-centering
```text
deviation

MP-1>config>pwe>pw(1)$ jitter-buffer-centering
```

### label
```text
in
 out

MP-1>config>pwe>pw(1)$ label
```

### name
```text
<pw-name>            : The name given to the specified PW  [1..32 chars]


MP-1>config>pwe>pw(1)$ name
```

### peer
```text
<peer-number>        : Peer number [number]


MP-1>config>pwe>pw(1)$ peer
```

### pm-collection
```text
<interval>           : PM collection interval
 <on-interval-close>  : Collect PM only on interval close


MP-1>config>pwe>pw(1)$ pm-collection
```

### show statistics
```text
# cli error: Invalid Command
MP-1>config>pwe>pw(1)$ show statistics
```

### show status
```text
<CR>

MP-1>config>pwe>pw(1)$ show status
```

### shutdown
```text
<CR>

MP-1>config>pwe>pw(1)$ shutdown
```

### source-clock-fail
```text
<pw-down>            : 
 <remote-domain-down> : 


MP-1>config>pwe>pw(1)$ source-clock-fail
```

### tdm-oos
```text
voice
 data
 signaling

MP-1>config>pwe>pw(1)$ tdm-oos
```

### tdm-payload
```text
size

MP-1>config>pwe>pw(1)$ tdm-payload
```

### tos
```text
<tos>                : The value of the IP TOS byte in egress packets. [0 .. 
                        255]


MP-1>config>pwe>pw(1)$ tos
```

### udp-mux-method
```text
<dst-port>           : 
 <src-port>           : 


MP-1>config>pwe>pw(1)$ udp-mux-method
```

## configure qos

Level help (`?`):
```text
[no] policer-profile                + 
 [no] queue-block-profile            + 
 [no] queue-group-profile            + 
 [no] queue-internal-profile         + 
 [no] queue-map-profile              + 
 [no] shaper-profile                 +
```

### policer-profile *(parameterized — inner help harvested under "configure qos policer-profile NAME")*
```text
<policer-profile-*>  : [1..32 chars]


MP-1>config>qos# policer-profile
```

### queue-block-profile *(parameterized — inner help harvested under "configure qos queue-block-profile NAME")*
```text
<queue-block-prof*>  : [1..32 chars]


MP-1>config>qos# queue-block-profile
```

### queue-group-profile *(parameterized — inner help harvested under "configure qos queue-group-profile NAME")*
```text
<queue-group-name>   : [1..32 chars]


MP-1>config>qos# queue-group-profile
```

### queue-internal-profile *(parameterized — inner help harvested under "configure qos queue-internal-profile NAME")*
```text
<queue-internal-p*>  : [1..32 chars]


MP-1>config>qos# queue-internal-profile
```

### queue-map-profile *(parameterized — inner help harvested under "configure qos queue-map-profile NAME")*
```text
<queue-mapping-pr*>  : [1..32 chars]


MP-1>config>qos# queue-map-profile
```

### shaper-profile *(parameterized — inner help harvested under "configure qos shaper-profile NAME")*
```text
<shaper-profile-n*>  : [1..32 chars]


MP-1>config>qos# shaper-profile
```

## configure qos policer-profile NAME

Level help (`?`):
```text
bandwidth                      -
```

### bandwidth
```text
cir
 cbs

MP-1>config>qos>policer-profile(GbeDefaultPolice)# bandwidth
```

## configure qos queue-block-profile NAME

Level help (`?`):
```text
[no] queue                          +
```

### queue *(parameterized — inner help harvested under "configure qos queue-block-profile NAME queue NAME")*
```text
<queue-id>           : [number]


MP-1>config>qos>queue-block-profile(L0StrictDefaultP)# queue
```

## configure qos queue-block-profile NAME queue NAME

Level help (`?`):
```text
[no] internal-profile               -
```

### internal-profile
```text
profile

MP-1>config>qos>queue-block-profile(L0StrictDefaultP)>queue(0)# internal-profile
```

## configure qos queue-group-profile NAME

Level help (`?`):
```text
[no] queue-block                    +
```

### queue-block *(parameterized — inner help harvested under "configure qos queue-group-profile NAME queue-block NAME")*
```text
<id>                 :  [level_id/queue_id]


MP-1>config>qos>queue-group-profile(FeDefaultQueueGr)# queue-block
```

## configure qos queue-group-profile NAME queue-block NAME

Level help (`?`):
```text
name                           - 
 [no] profile                        - 
 [no] shaper                         -
```

### name
```text
<block-name>         : [1..32 chars]


MP-1>config>qos>queue-group-profile(FeDefaultQueueGr)>queue-block(0/1)# name
```

### profile
```text
<queue-block-prof*>  : [1..32 chars]


MP-1>config>qos>queue-group-profile(FeDefaultQueueGr)>queue-block(0/1)# profile
```

### shaper
```text
profile

MP-1>config>qos>queue-group-profile(FeDefaultQueueGr)>queue-block(0/1)# shaper
```

## configure qos queue-internal-profile NAME

Level help (`?`):
```text
scheduling                     -
```

### scheduling
```text
<strict>             : 
 <wfq>                : 


MP-1>config>qos>queue-internal-profi(QueueDefaultStri)# scheduling
```

## configure qos queue-map-profile NAME

Level help (`?`):
```text
map                            -
```

### map
```text
<class-value>        : [n1..n2]


MP-1>config>qos>queue-map-profile(qmappbit)# map
```

## configure qos shaper-profile NAME

Level help (`?`):
```text
bandwidth                      -
```

### bandwidth
```text
cir
 cbs

MP-1>config>qos>shaper-profile(GbeDefaultShaper)# bandwidth
```

## configure reporting

Level help (`?`):
```text
acknowledge                    - 
      active-alarm-rebuild           - 
      alarm-input                    - 
 [no] alarm-source-attribute         - 
 [no] alarm-source-type-attribute    - 
      clear-alarm-log                - 
      log-file-timestamp-type        - Configure log file timestamp type
 [no] low-memory-alarm               - Set thresholds for the low memory alarms
 [no] mask-minimum-severity          - 
 [no] pm                             - Globally enable PM collection
 [no] pm-collection                  - Enable PM collection on entity type

 show active-alarms
 show active-alarms-details
 show alarm-information
 show alarm-input
 show alarm-list
 show alarm-log
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


MP-1>config>reporting# acknowledge
```

### active-alarm-rebuild
```text
<CR>

 send-traps

MP-1>config>reporting# active-alarm-rebuild
```

### alarm-input
```text
<port-number>        : [number]


MP-1>config>reporting# alarm-input
```

### alarm-source-attribute
```text
<system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <domain-clock>       : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <serial>             : 
 <serial-fe>          : 
 <router-interface>   : 
 <pw>                 : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <alarm-input>        : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# alarm-source-attribute
```

### alarm-source-type-attribute
```text
<system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <domain-clock>       : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <ds1-opt>            : 
 <e1>                 : 
 <t1>                 : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# alarm-source-type-attribute
```

### clear-alarm-log
```text
<log>                : 
 <brief-log>          : 
 <activity-log>       : 
 <all-logs>           : 


MP-1>config>reporting# clear-alarm-log
```

### led-blink
```text
# cli error: Invalid Command
MP-1>config>reporting# led-blink
```

### log-file-timestamp-type
```text
<utc>                : 
 <local>              : 


MP-1>config>reporting# log-file-timestamp-type
```

### low-memory-alarm
```text
clear-threshold
 raise-threshold
 critical-raise-threshold

MP-1>config>reporting# low-memory-alarm
```

### mask-minimum-severity
```text
log
 snmp-trap
 led-relay
 popup
 vty-popup

MP-1>config>reporting# mask-minimum-severity
```

### pm
```text
<CR>

MP-1>config>reporting# pm
```

### pm-collection
```text
<eth>                : Ethernet
 <twamp>              : TWAMP sessions
 <e1>                 : E1 Ports
 <t1>                 : T1 Ports
 <pw>                 : PW


MP-1>config>reporting# pm-collection
```

### show active-alarms
```text
<CR>
 <system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <all>                : 
 <domain-clock>       : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# show active-alarms
```

### show active-alarms-details
```text
<CR>
 <system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <all>                : 
 <domain-clock>       : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# show active-alarms-details
```

### show alarm-information
```text
<system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <domain-clock>       : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# show alarm-information
```

### show alarm-input
```text
<CR>

MP-1>config>reporting# show alarm-input
```

### show alarm-list
```text
<CR>
 <system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <domain-clock>       : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 
 <all>                : 


MP-1>config>reporting# show alarm-list
```

### show alarm-log
```text
<CR>
 <system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <all>                : 
 <domain-clock>       : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# show alarm-log
```

### show brief-alarm-log
```text
<CR>
 <system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <all>                : 
 <domain-clock>       : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# show brief-alarm-log
```

### show brief-log
```text
<CR>
 <system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <all>                : 
 <domain-clock>       : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# show brief-log
```

### show event-information
```text
<system>             : 
 <power-supply>       : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <domain-clock>       : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# show event-information
```

### show event-list
```text
<CR>
 <system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <domain-clock>       : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 
 <all>                : 


MP-1>config>reporting# show event-list
```

### show led-blink-status
```text
# cli error: Invalid Command
MP-1>config>reporting# show led-blink-status
```

### show log
```text
<CR>
 <system>             : 
 <power-supply>       : 
 <station-clock>      : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <voice>              : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <ds1-opt>            : 
 <serial>             : 
 <router-interface>   : 
 <pw>                 : 
 <alarm-input>        : 
 <all>                : 
 <domain-clock>       : 
 <domain-clock-sou*>  : 
 <twamp-responder>    : 


MP-1>config>reporting# show log
```

### show log-summary
```text
<CR>
 <number-records>     : [number, default 10]


MP-1>config>reporting# show log-summary
```

## configure router NAME

Level help (`?`):
```text
arp-timeout                    - Aging time for the ARP entries
      clear-arp-table                - Clear ARP table
      clear-statistics               - Clear statistics (traffic, access lists)
 [no] interface                      + Configure router interface
 [no] name                           - Configure router name
 [no] static-route                   - Configure static route 

 show arp-table                      - Show ARP table
 show routing-table                  - Show routing table
 show statistics                     - Show statistics
 show summary-interface              - Show interface table
```

### arp-timeout
```text
<seconds>            : Aging time seconds [10..1000000]


MP-1>config>router(1)# arp-timeout
```

### clear-arp-table
```text
<CR>

MP-1>config>router(1)# clear-arp-table
```

### clear-statistics
```text
<ipv4>               : Clear IPv4 statistics


MP-1>config>router(1)# clear-statistics
```

### interface *(parameterized — inner help harvested under "configure router NAME interface NAME")*
```text
<number>             : Router interface number [number] [1..8]


MP-1>config>router(1)# interface
```

### name
```text
<string>             : Router name [1..32 chars]


MP-1>config>router(1)# name
```

### show arp-table
```text
<CR>
 address

MP-1>config>router(1)# show arp-table
```

### show routing-table
```text
<CR>
 address
 protocol

MP-1>config>router(1)# show routing-table
```

### show statistics
```text
<ipv4>               : ipv4


MP-1>config>router(1)# show statistics
```

### show summary-interface
```text
<CR>

MP-1>config>router(1)# show summary-interface
```

### static-route
```text
<address-mask>       : IP and mask [0.0.0.0/32|0:0:0:0::0/128]


MP-1>config>router(1)# static-route
```

## configure router NAME interface NAME

Level help (`?`):
```text
[no] address                        - Configure router interface IP
 [no] bind                           - Bind router interface
      clear-statistics               - Clear statistics (traffic, access lists)
 [no] ip-forwarding                  - Enable/disable IP forwarding
      management-access              - Configure managment access
 [no] name                           - Configure router interface name
 [no] shutdown                       - Disable router interface

 show statistics                     - Show router interface statistics 
 show status                         - Show router interface status
```

### address
```text
<address-mask>       : Router interface IP and mask [0.0.0.0/32|0:0:0:0::0/128]


MP-1>config>router(1)>interface(1)# address
```

### bind
```text
<svi>                : SVI 


MP-1>config>router(1)>interface(1)# bind
```

### clear-statistics
```text
<ipv4>               : IPv4 statistics


MP-1>config>router(1)>interface(1)# clear-statistics
```

### management-access
```text
<allow-all>          : Allow all
 <allow-ping>         : Ping only


MP-1>config>router(1)>interface(1)# management-access
```

### name
```text
<string>             : Router interface name [1..32 chars]


MP-1>config>router(1)>interface(1)# name
```

### show statistics
```text
<ipv4>               : IPv4


MP-1>config>router(1)>interface(1)# show statistics
```

### show status
```text
<CR>

MP-1>config>router(1)>interface(1)# show status
```

### shutdown
```text
<CR>

MP-1>config>router(1)>interface(1)# shutdown
```

## configure system

Level help (`?`):
```text
[no] announcement                   - Post-login banner text
      clock                          + Clock configuration
 [no] contact                        - Contact name
      date-and-time                  + Configure date and time
 [no] location                       - Device location
 [no] login-message                  - Pre-login banner text
 [no] name                           - Device name
      syslog                         + Configure Syslog

 show copyright                      - Display copyright message
 show device-information             - Display device information
 show memory                         - Display memory usage
 show memory-details                 - Display memory usage in detail
 show system-date                    - Display date and time
 show tech-support                   - Executes a predefined series of commands
```

### announcement
```text
<message>            : 


MP-1>config>system# announcement
```

### contact
```text
<contact-person>     : Contact name [0..255 chars, default contact person]


MP-1>config>system# contact
```

### location
```text
<location-of-device> : Device location [0..255 chars, default the location of 
                        this device]


MP-1>config>system# location
```

### login-message
```text
<message>            : 


MP-1>config>system# login-message
```

### name
```text
<name-of-device>     : Device name [0..255 chars]


MP-1>config>system# name
```

### show copyright
```text
<CR>

MP-1>config>system# show copyright
```

### show device-information
```text
<CR>

MP-1>config>system# show device-information
```

### show memory
```text
<CR>

MP-1>config>system# show memory
```

### show memory-details
```text
<CR>

MP-1>config>system# show memory-details
```

### show system-date
```text
<CR>

MP-1>config>system# show system-date
```

### show tech-support
```text
<CR>
 <file>               : 
 <terminal>           : Commands output is printed to terminal screen


MP-1>config>system# show tech-support
```

### syslog *(not entered — parameterized context)*
```text
<device>             : Device
 <server>             : Server


MP-1>config>system# syslog
```

## configure system clock

Level help (`?`):
```text
[no] domain                         + Clock domain number
      station                        + Enable/disable station clock
```

### domain *(parameterized — inner help harvested under "configure system clock domain NAME")*
```text
<id>                 : Domain Number [number] [1..1]


MP-1>config>system>clock# domain
```

### station *(parameterized — inner help harvested under "configure system clock station NAME")*
```text
<id>                 : Station clock identifier number [slot/port]


MP-1>config>system>clock# station
```

## configure system clock domain NAME

Level help (`?`):
```text
clear                          - Clear the Forced or Manual selection
      force                          - Forced selection of any configured Clock 
                                       Source
      manual                         - Manual selection of any configured Clock 
                                       Source
      mode                           - Mode of Clock Selection
 [no] quality                        - Clock Quality Level (QL)
 [no] source                         + Clock Source parameters
      sync-network-type              - The synchronous digital hierarchy type

 show status                         - Display status parameters
```

### clear
```text
<CR>

MP-1>config>system>clock>domain(1)# clear
```

### force
```text
<source-id>          : Clock Source Id [number]


MP-1>config>system>clock>domain(1)# force
```

### manual
```text
<source-id>          : Clock Source Id [number]


MP-1>config>system>clock>domain(1)# manual
```

### mode
```text
<auto>               : Performs Automatic Clock Selection.
 <free-run>           : No Clock Selection


MP-1>config>system>clock>domain(1)# mode
```

### quality
```text
min-level-station
 min-level-system

MP-1>config>system>clock>domain(1)# quality
```

### show status
```text
<CR>

MP-1>config>system>clock>domain(1)# show status
```

### source *(not entered — parameterized context)*
```text
<src-id>             : Unique Clock Source Id [number] [1..4]


MP-1>config>system>clock>domain(1)# source

auto-create tried [source zzz-hrvst, source hrvst, source z], all refused.
last device response ('source z'): source z
#                                          ^
# cli error: invalid parameter value
 - source <src-id> [rx-port ethernet  <port-index>]
 - source <src-id> [rx-port fast-ethernet  <port-index>]
 - source <src-id> [rx-port giga-ethernet  <port-index>]
 - source <src-id> [rx-port e1  <port-index>]
 - source <src-id> [rx-port t1  <port-index>]
 - source <src-id> [rx-port j1  <port-index>]
 - source <src-id> [rx-port sdh-sonet  <port-index>]
 - source <src-id> [rx-port shdsl  <port-index>]
 - source <src-id> [rx-port ima  <group-index>]
 - source <src-id> [rx-port serial  <port-index>]
 - source <src-id> [rx-port serial-bundle  <port-index-trib>]
 - source <src-id> [rx-port e1  <port-index-trib>]
 - source <src-id> [rx-port t1  <port-index-trib>]
 - source <src-id> [rx-port t3  <port-index>]
 - source <src-id> [rx-port ds1-opt  <port-index>]
 - source <src-id> [rx-port e1-i  <port-index>]
 - source <src-id> [station <station-id>]
 - source <src-id> [recovered <recovered-id>]
 - source <src-id> [recovered <recovered-id>]
 - source <src-id> [domain <domain-id>]
 - source <src-id> [internal-gps <port-index>]
 - source <src-id> [pw <pw-num>]
 - no source <src-id>

 <src-id>             : Unique Clock Source Id [number] [1..4]
 <ethernet>           : Ethernet speed of 10/100/1000 Mbit/s.
 <port-index>         : Rx-Port IfIndex [slot/port]
 <fast-ethernet>      : Ethernet at the nominal rate of 100 Mbit/s
 <giga-ethernet>      : Ethernet frames at a rate of a gigabit per second
 <e1>                 : Fundamental Rate of European Carriers
 <t1>                 : Fundamental Rate of Noth American Carriers
 <j1>                 : Fundamental  Rate of Japanese Carriers
 <sdh-sonet>          : Synchronous optical networking/Synchronous Digital 
                        Hierarchy
 <shdsl>              : Single-Pair High-speed Digital Subscriber Line
 <ima>                : ATM Inverse Multiplexing group
 <group-index>        : IMA Group Number [number]
 <serial-bundle>      : Serial bundle
 <port-index-trib>    : Rx Port IfIndex [slot/port[/tributary]]
 <t3>                 : Fundamental Rate of North American Carriers
 <e1-i>               : Fundamental Rate of European Carriers
 <station-id>         : Station Clock Source Number [slot/port]
 <recovered-id>       : Recovered Clock Source Number [slot/port]
 <domain-id>          : Domain where this Clock Source is defined [number]
 <pw-num>             : Pw where this Clock Source is defined [number] [1..32]

MP-1>config>system>clock>domain(1)#
```

### sync-network-type
```text
<1>                  : Type 1 = Europe
 <2>                  : Type 2 = North America


MP-1>config>system>clock>domain(1)# sync-network-type
```

## configure system clock station NAME

Level help (`?`):
```text
interface-type                 - Assign station clock interface type
      line-code                      - Assign station clock line code
      line-type                      - Set interface line-type
      rx-sensitivity                 - Station clock received sensitivity
 [no] shutdown                       - Administratively enable/disable station 
                                       clock

 show status                         - Display station clock status
```

### impedance
```text
# cli error: Invalid Command
MP-1>config>system>clock>station(0/1)# impedance
```

### interface-type
```text
<e1>                 : E1
 <t1>                 : T1


MP-1>config>system>clock>station(0/1)# interface-type
```

### line-code
```text
<b8zs>               : B8ZS
 <ami>                : AMI
 <hdb3>               : HDB3


MP-1>config>system>clock>station(0/1)# line-code
```

### line-type
```text
<unframed>           : Sets the T1 line type to Unframed
 <esf>                : Selects Extended Super Frame (24 T1 frames)
 <sf>                 : Selects Super Frame (12 T1 frames)


MP-1>config>system>clock>station(0/1)# line-type
```

### rx-sensitivity
```text
<short-haul>         : Short haul
 <long-haul>          : Long haul


MP-1>config>system>clock>station(0/1)# rx-sensitivity
```

### show status
```text
<CR>

MP-1>config>system>clock>station(0/1)# show status
```

### shutdown
```text
<CR>

MP-1>config>system>clock>station(0/1)# shutdown
```

## configure system date-and-time

Level help (`?`):
```text
date-format                    - Date format
      date                           - Set  date (yyyy-mm-dd) 
      sntp                           + Configure SNTP client
 [no] summer-time                    - Configure summer time begin and end
      time                           - Set time
      zone                           - Time zone

 show summer-time                    - Show summer time details
```

### date
```text
<date>               : Set  date (yyyy-mm-dd) [yyyy-mm-dd]


MP-1>config>system>date-time# date
```

### date-format
```text
<yyyy-mm-dd>         : yyyy-mm-dd
 <dd-mm-yyyy>         : dd-mm-yyyy
 <mm-dd-yyyy>         : mm-dd-yyyy 
 <yyyy-dd-mm>         : yyyy-dd-mm


MP-1>config>system>date-time# date-format
```

### show summer-time
```text
<CR>

MP-1>config>system>date-time# show summer-time
```

### summer-time
```text
<recurring>          : 
 <date>               : 


MP-1>config>system>date-time# summer-time
```

### time
```text
<time>               : Set time [hh:mm[:ss]]


MP-1>config>system>date-time# time
```

### zone
```text
<utc>                : Universal Time Coordinated


MP-1>config>system>date-time# zone
```

## configure system date-and-time sntp

Level help (`?`):
```text
[no] broadcast                      - Enable SNTP broadcast 
      poll-interval                  - Period of polling SNTP Server
 [no] server                         + Specify SNTP Server

 show status                         - SNTP status
```

### broadcast
```text
<CR>

MP-1>config>system>date-time>sntp# broadcast
```

### poll-interval
```text
<CR>
 <interval>           : 
 <fast-mode>          : 
 <minutes>            : Polling interval [1..1440]


MP-1>config>system>date-time>sntp# poll-interval
```

### server *(not entered — parameterized context)*
```text
<server-id>          : SNTP server address [1..10]


MP-1>config>system>date-time>sntp# server

auto-create tried [server zzz-hrvst, server hrvst, server z], all refused.
last device response ('server z'): server z
#                                         ^
# cli error: invalid parameter value
 - server <server-id>
 - no server <server-id>
 <server-id>          : SNTP server address [1..10]

MP-1>config>system>date-time>sntp#
```

### show status
```text
<CR>

MP-1>config>system>date-time>sntp# show status
```

## configure terminal

Level help (`?`):
```text
baud-rate                      - Terminal baud rate
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


MP-1>config>terminal# baud-rate
```

### length
```text
<number-of-rows>     : Number of rows to print before pausing (or 0 for no 
                        pausing). [0..255, default 20]


MP-1>config>terminal# length
```

### serial-port-disable
```text
<CR>

MP-1>config>terminal# serial-port-disable
```

### timeout
```text
<forever>            : No timeout
 <limited>            : Enable timeout


MP-1>config>terminal# timeout
```

## file

Level help (`?`):
```text
delete                         - Delete file
      dir                            - Display file directory

 show banner-text                    - Display banner  
 show configuration-files            - Displays configuration files properties
 show copy                           - Display Copy progress
 show factory-default-config         - Display factory-default-config
 show schedule-log                   - Display schedule-log  
 show startup-config                 - Display startup-config 
 show sw-pack                        - Display SW packs 
 show user-default-config            - Display user-default-config
```

### delete
```text
<sw-pack-1>          : 
 <sw-pack-2>          : 
 <startup-config>     : 
 <rollback-config>    : 
 <user-default-con*>  : 
 <candidate-config>   : 
 <alarm-event-log>    : 
 <banner-text>        : 
 <sniffer-file>       : 
 <user-script>        : 
 <script-result>      : 


MP-1>file# delete
```

### dir
```text
<CR>

MP-1>file# dir
```

### show banner-text
```text
<CR>

MP-1>file# show banner-text
```

### show configuration-files
```text
<CR>

MP-1>file# show configuration-files
```

### show copy
```text
<CR>
 <summary>            : 


MP-1>file# show copy
```

### show factory-default-config
```text
<CR>

MP-1>file# show factory-default-config
```

### show schedule-log
```text
<CR>

MP-1>file# show schedule-log
```

### show script-result
```text
# cli error: Invalid Command
MP-1>file# show script-result
```

### show startup-config
```text
<CR>

MP-1>file# show startup-config
```

### show sw-pack
```text
<CR>

MP-1>file# show sw-pack
```

### show user-default-config
```text
<CR>

MP-1>file# show user-default-config
```

### show user-script
```text
# cli error: Invalid Command
MP-1>file# show user-script
```
