# mp4100 CLI reference (harvested `?` help)

Captured live from marks-mp4 (Mark's Megaplex-4100 (prompt mp4100#, Mn 4.91) - FIRST mp4100-family unit; candidate-DB CLI (commit/discard-changes)) on 2026-07-12 by scripts/harvest_cli.py
(re-run `harvest` after firmware upgrades — it diffs and updates in place).
Every section is a CLI context: first the level `?` listing (commands +
descriptions), then per-command argument help (`<command> ?`). Sections
ending in NAME are parameterized contexts harvested through one instance
(an existing one, or a temp object created and rolled back) — NAME stands
for any instance. Entries marked *(not entered)* could not be harvested
safely — their inner structure is in command-tree-mp4100.md; use
cli_help with a real index for inner argument syntax.

## <root>

Level help (`?`):
```text
admin                 + Adminstrative commands
      clear-statistics      - Clear all statistics
      configure             + Configure device
      file                  + File commands
      logon                 - Allows to logon to debug level

Global commands:
      commit                - Update the candidate database to the running 
                              database
      discard-changes       - Resets to last-saved parameter profile
      echo                  - Displays a line of text (command) on the screen
      exec                  - Executes a file.
      exit                  - Returns to the next higher command level (context)
      help                  - Displays information regarding commands in the 
                              current level
      history               - Displays the history of commands issued since the 
                              last restart
      info                  - Displays the current device configuration
      level-info            - Displays the current device configuration - 
                              commands from the current level only
      logout                - Logs the device off
      ping                  - Ping request to verify reachability of remote host
      sanity-check          - Initiates a self test of the device
      save                  - Saves current settings
      startup-config-confi* - Confirm configuration
      tree                  - Displays the command levels from the current 
                              context downwards
      virtual-terminal      -
```

### clear-statistics
```text
<CR>

mp4100# clear-statistics
```

### commit
```text
<CR>

mp4100# commit
```

### discard-changes
```text
<CR>

mp4100# discard-changes
```

### echo
```text
<CR>
 <text-to-echo>       : Text to display on screen [string]


mp4100# echo
```

### exec
```text
<file-name>          : Specifies name of the file to be executed [string]


mp4100# exec
```

### exit
```text
<CR>
 <all>                : Returns to Device context


mp4100# exit
```

### help
```text
<CR>
 <hotkeys>            : Hotkeys related to global commands
 <globals>            : Displays commands available from all levels


mp4100# help
```

### history
```text
<CR>

mp4100# history
```

### info
```text
<CR>
 <running>            : Displays data of currently active parameters
 <detail>             : Adds information to every conf. parameter


mp4100# info
```

### level-info
```text
<CR>
 <running>            : Displays data of currently active parameters
 <detail>             : Device configuration, including defaults


mp4100# level-info
```

### logon
```text
<debug>              : 


mp4100# logon
```

### logout
```text
<CR>

mp4100# logout
```

### ping
```text
<ip-address>         : Destination IP [0.0.0.0]


mp4100# ping
```

### sanity-check
```text
<CR>

mp4100# sanity-check
```

### save
```text
<CR>

mp4100# save
```

### startup-config-confirm
```text
<CR>

mp4100# startup-config-confirm
```

### tree
```text
<CR>
 <detail>             : Available commands, current context and downwards


mp4100# tree
```

### virtual-terminal
```text
<shdsl>              : 


mp4100# virtual-terminal
```

## admin

Level help (`?`):
```text
factory-default       - Return to factory default configuration
      license               + 
      reboot                - Reboot device
      software              + Software installation
 [no] startup-confirm-requ* - Require user confirmation after reboot
      user-default          - Return to user default configuration
```

### factory-default
```text
<CR>

mp4100>admin# factory-default
```

### reboot
```text
<CR>

mp4100>admin# reboot
```

### startup-confirm-required
```text
<CR>
 time-to-confirm
 rollback

mp4100>admin# startup-confirm-required
```

### user-default
```text
<CR>

mp4100>admin# user-default
```

## admin license

Level help (`?`):
```text
[no] license-enable        - 

 show summary               - Display license status summary
```

### license-enable
```text
<macsec>             : 


mp4100>admin>license# license-enable
```

### show summary
```text
<CR>

mp4100>admin>license# show summary
```

## admin software

Level help (`?`):
```text
install               - Install SW

 show status                - Show installation process
```

### install
```text
<sw-pack-1>          : sw-pack-1
 <sw-pack-2>          : sw-pack-2
 <sw-pack-3>          : sw-pack-3
 <sw-pack-4>          : sw-pack-4


mp4100>admin>software# install
```

### show status
```text
<CR>

mp4100>admin>software# show status
```

### undo-install
```text
# cli error: Invalid Command
mp4100>admin>software# undo-install
```

## configure

Level help (`?`):
```text
access-control        + Configure access control
 [no] bridge                + Configure bridge
      chassis               + Configure chassis
      cross-connect         + Cross connect of ATM, PW, or TDM 
                              (DS0,DS1,DS3,SDH/SONET)
      crypto                + Cryptography level
      fault                 + 
      flows                 + 
      management            + Device management commands
      oam                   + Configure OAM
 [no] peer                  - Create/delete peer
      port                  + Configure port
      protection            + Defines protection mechanisms
      pwe                   + Create/delete Psaudo-wire
      qos                   + Quality of service
      reporting             + 
      router                + Configures router parameters
      slot                  + Configure card
      system                + Defines system parameters
      terminal              + Configure terminal
      test                  + 

 show cards-summary         - Display card information
 show peer-summary
```

### bridge *(parameterized — inner help harvested under "configure bridge NAME")*
```text
<number>             : Bridge number [number]


mp4100>config# bridge
```

### peer
```text
<number>             : Number of configured peer [number] [1..640]


mp4100>config# peer
```

### router *(parameterized — inner help harvested under "configure router NAME")*
```text
<number>             : Router number [number]


mp4100>config# router
```

### show cards-summary
```text
<CR>

mp4100>config# show cards-summary
```

### show peer-summary
```text
<CR>

mp4100>config# show peer-summary
```

### slot *(parameterized — inner help harvested under "configure slot NAME")*
```text
<slot>               : 


mp4100>config# slot
```

## configure access-control

Level help (`?`):
```text
[no] access-list           + Configure access control list
```

### access-list *(not entered — parameterized context)*
```text
<ipv4>               : IPv4
 <acl-name>           : Access list name [1..252 chars]


mp4100>config>access-control# access-list
```

## configure bridge NAME

Level help (`?`):
```text
aging-time            - Configure MAC aging time
      clear-mac-table       - Clear MAC address table
 [no] filtering             - Enable filtering forwarding mode
 [no] port                  + Configure bridge port
      spanning-tree         + Configure spanning tree
 [no] vlan                  + Configure VLAN
 [no] vlan-aware            - Enable VLAN aware mode

 show mac-address-table     - Display MAC address table

mp4100>config>bridge(1)$
```

### aging-time
```text
<seconds>            : MAC aging time (seconds) [number, default 300] 
                        [60..3000]


mp4100>config>bridge(1)$ aging-time
```

### clear-mac-table
```text
<CR>

mp4100>config>bridge(1)$ clear-mac-table
```

### filtering
```text
<CR>

mp4100>config>bridge(1)$ filtering
```

### mode
```text
# cli error: Invalid Command
mp4100>config>bridge(1)$ mode
```

### root
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# root
```

### show mac-address-table
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# show mac-address-table
```

### vlan-aware
```text
<CR>

mp4100>config>bridge(1)# vlan-aware
```

## configure bridge NAME port

Level help (`?`):
```text
aging-time            - Configure MAC aging time
      clear-mac-table       - Clear MAC address table
 [no] filtering             - Enable filtering forwarding mode
 [no] port                  + Configure bridge port
      spanning-tree         + Configure spanning tree
 [no] vlan                  + Configure VLAN
 [no] vlan-aware            - Enable VLAN aware mode

 show mac-address-table     - Display MAC address table
```

### bind
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# bind
```

### name
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# name
```

### pvid
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# pvid
```

### show bind
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# show bind
```

### shutdown
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# shutdown
```

## configure bridge NAME vlan

Level help (`?`):
```text
aging-time            - Configure MAC aging time
      clear-mac-table       - Clear MAC address table
 [no] filtering             - Enable filtering forwarding mode
 [no] port                  + Configure bridge port
      spanning-tree         + Configure spanning tree
 [no] vlan                  + Configure VLAN
 [no] vlan-aware            - Enable VLAN aware mode

 show mac-address-table     - Display MAC address table
```

### maximum-mac-addresses
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# maximum-mac-addresses
```

### mode
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# mode
```

### name
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# name
```

### root
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# root
```

### tagged-egress
```text
# cli error: Invalid Command
mp4100>config>bridge(1)# tagged-egress
```

## configure chassis

Level help (`?`):
```text
inventory             + Specifies device inventory parameters

 show environment           - Display hardware status
 show manufacture-info      - Display chassis and card information
 show summary-inventory     - Display inventory (physical entities)
```

### inventory *(parameterized — inner help harvested under "configure chassis inventory NAME")*
```text
<entity-index>       : Specify entity index [number]


mp4100>config>chassis# inventory
```

### show environment
```text
<CR>
 temperature

mp4100>config>chassis# show environment
```

### show manufacture-info
```text
<slot>               : Slot
 <all>                : Entire device


mp4100>config>chassis# show manufacture-info
```

### show summary-inventory
```text
<CR>

mp4100>config>chassis# show summary-inventory
```

## configure chassis inventory NAME

Level help (`?`):
```text
[no] alias                 - Configure alias
 [no] asset-id              - Configure asset identifier
 [no] serial-number         - Configure serial number

 show status                - Display entity details
```

### show status
```text
<CR>

mp4100>config>chassis>inventory(2)# show status
```

## configure cross-connect

Level help (`?`):
```text
[no] ds0                   - DS0 (TimeSlot Assignment) Cross Connect Command
 [no] pw-tdm                - TDM virtual circuit cross connect
 [no] sdh-sonet             - SDH/Sonet Cross Connect Command
 [no] split-ts              - DS0 (TimeSlot Assignment) Cross Connect Command
 [no] tdm                   - TDM (DS1) Cross Connect Command

 show summary
```

### ds0
```text
<e1>                 : 
 <t1>                 : 
 <e1-i>               : 
 <t1-i>               : 
 <ds1>                : 
 <ds1-opt>            : 


mp4100>config>xc# ds0
```

### pw-tdm
```text
pw

mp4100>config>xc# pw-tdm
```

### sdh-sonet
```text
<vc12-vt2>           : 
 <vc11-vt1.5>         : 
 <vc3-sts1>           : 
 <vc4-sts3c>          : 


mp4100>config>xc# sdh-sonet
```

### show summary
```text
<all>                : 
 <ds0>                : 
 <sdh-sonet>          : 
 <pw>                 : 
 <tdm>                : 


mp4100>config>xc# show summary
```

### split-ts
```text
<e1>                 : 
 <t1>                 : 
 <e1-i>               : 
 <t1-i>               : 
 <ds1>                : 


mp4100>config>xc# split-ts
```

### tdm
```text
<e1>                 : 
 <t1>                 : 
 <e1-i>               : 
 <t1-i>               : 
 <ds1>                : 
 <ds1-opt>            : 


mp4100>config>xc# tdm
```

## configure crypto

Level help (`?`):
```text
key                   + RSA key management level
```

## configure crypto key

Level help (`?`):
```text
generate-rsa          - Generate RSA key pair

 show my-public-key-rsa     - Display self RSA public key
```

### generate-rsa
```text
<CR>
 label
 size
 application

mp4100>config>crypto>key# generate-rsa
```

### show my-public-key-rsa
```text
<CR>

mp4100>config>crypto>key# show my-public-key-rsa
```

## configure fault

Level help (`?`):
```text
cfm                   + 
 [no] fault-propagation     + Fault propagation configuration
```

### fault-propagation *(not entered — parameterized context)*
```text
<port>               : 


mp4100>config>fault# fault-propagation
```

## configure fault cfm

Level help (`?`):
```text
[no] service               +
```

### service *(not entered — parameterized context)*
```text
md

mp4100>config>fault>cfm# service
```

## configure flows

Level help (`?`):
```text
[no] classifier-profile    + 
 [no] flow                  + 
      rate-sampling-window  - 
 [no] service-ping          - Service Ping Request
 [no] service-ping-respons* - Service Ping Response

 show summary
```

### classifier-profile *(not entered — parameterized context)*
```text
<classification-n*>  : [1..32 chars]


mp4100>config>flows# classifier-profile

auto-create probe 'classifier-profile zzz-hrvst' refused.
device response: classifier-profile zzz-hrvst
#                                                 ^
# cli error: parameter or keyword missing or wrong
 - classifier-profile <classification-name> {match-all|match-any}
 - no classifier-profile <classification-name>
 <classification-n*>  : [1..32 chars]

mp4100>config>flows#
```

### flow *(parameterized — inner help harvested under "configure flows flow NAME")*
```text
<flow-name>          : [1..32 chars]


mp4100>config>flows# flow
```

### rate-sampling-window
```text
<argument>           : Window size for sampling rate statistics [Min.] [1..30, 
                        default 15]


mp4100>config>flows# rate-sampling-window
```

### service-ping
```text
local-ip

mp4100>config>flows# service-ping
```

### service-ping-response
```text
local-ip

mp4100>config>flows# service-ping-response
```

### show summary
```text
<details>            : 
 <brief>              : 


mp4100>config>flows# show summary
```

## configure flows flow NAME

Level help (`?`):
```text
[no] classifier            - 
 [no] drop                  - 
 [no] egress-port           - 
 [no] ingress-port          - 
 [no] mark                  + 
 [no] pm-collection         - Enable Performance Management (PM)
 [no] policer               - 
 [no] reverse-direction     - 
 [no] shutdown              - Enable/disable the flow
 [no] vlan-tag              - 

 show statistics
 show test

mp4100>config>flows>flow(zzz-hrvst)$
```

### classifier
```text
<classification-n*>  : [1..32 chars]


mp4100>config>flows>flow(zzz-hrvst)$ classifier
```

### drop
```text
<CR>

mp4100>config>flows>flow(zzz-hrvst)$ drop
```

### egress-port
```text
<ethernet>           : 
 <lag>                : 
 <lre>                : 
 <logical-mac>        : 
 <pcs>                : 
 <svi>                : 
 <mng-ethernet>       : 
 <bridge-port>        : 
 <int-ethernet>       : 


mp4100>config>flows>flow(zzz-hrvst)$ egress-port
```

### ingress-port
```text
<ethernet>           : 
 <lag>                : 
 <lre>                : 
 <logical-mac>        : 
 <pcs>                : 
 <svi>                : 
 <mng-ethernet>       : 
 <bridge-port>        : 
 <int-ethernet>       : 


mp4100>config>flows>flow(zzz-hrvst)$ ingress-port
```

### pm-collection
```text
interval

mp4100>config>flows>flow(zzz-hrvst)# pm-collection
```

### policer
```text
<profile>            : 
 <aggregate>          : 


mp4100>config>flows>flow(zzz-hrvst)# policer
```

### reverse-direction
```text
<CR>
 <queue>              : 
 <queue-map-profile>  : 


mp4100>config>flows>flow(zzz-hrvst)# reverse-direction
```

### show statistics
```text
<running>            : 


mp4100>config>flows>flow(zzz-hrvst)# show statistics
```

### show test
```text
<CR>

mp4100>config>flows>flow(zzz-hrvst)# show test
```

### shutdown
```text
<CR>

mp4100>config>flows>flow(zzz-hrvst)# shutdown
```

### test
```text
# cli error: Invalid Command
mp4100>config>flows>flow(zzz-hrvst)# test
```

### vlan-tag
```text
<push>               : 
 <pop>                : 


mp4100>config>flows>flow(zzz-hrvst)# vlan-tag
```

## configure flows flow NAME mark

Level help (`?`):
```text
[no] classifier            - 
 [no] drop                  - 
 [no] egress-port           - 
 [no] ingress-port          - 
 [no] mark                  + 
 [no] pm-collection         - Enable Performance Management (PM)
 [no] policer               - 
 [no] reverse-direction     - 
 [no] shutdown              - Enable/disable the flow
 [no] vlan-tag              - 

 show statistics
 show test
```

### inner-marking-profile
```text
# cli error: Invalid Command
mp4100>config>flows>flow(zzz-hrvst)# inner-marking-profile
```

### inner-p-bit
```text
# cli error: Invalid Command
mp4100>config>flows>flow(zzz-hrvst)# inner-p-bit
```

### inner-vlan
```text
# cli error: Invalid Command
mp4100>config>flows>flow(zzz-hrvst)# inner-vlan
```

### marking-profile
```text
# cli error: Invalid Command
mp4100>config>flows>flow(zzz-hrvst)# marking-profile
```

### p-bit
```text
# cli error: Invalid Command
mp4100>config>flows>flow(zzz-hrvst)# p-bit
```

### vlan
```text
<push>               : 
 <pop>                : 


mp4100>config>flows>flow(zzz-hrvst)# vlan
```

## configure management

Level help (`?`):
```text
access                + Specifies access paths and rights
 [no] enable-mng-ethernet-* - Enable/Disable traffic forwarding between 
                              mng-ethernet and the management cloud including 
                              local host
 [no] manager               + Configure manager
      radius                + Configure RADIUS client
      snmp                  + Defines SNMP settings
      tacacsplus            + Configure TACACS+ client
      trap-sync-group       + Create trap sync group
 [no] user                  - Create user

 show trap-sync             - Display trap sync group
 show users                 - Show users
```

### enable-mng-ethernet-traffic
```text
<CR>

mp4100>config>mngmnt# enable-mng-ethernet-traffic
```

### manager *(not entered — parameterized context)*
```text
<ip-address>         : Manager IP address [0.0.0.0]


mp4100>config>mngmnt# manager
```

### show trap-sync
```text
<CR>

mp4100>config>mngmnt# show trap-sync
```

### show users
```text
<CR>

mp4100>config>mngmnt# show users
```

### trap-sync-group *(not entered — parameterized context)*
```text
<group-id>           : Trap sync group [number]


mp4100>config>mngmnt# trap-sync-group
```

### user
```text
<name>               : User name [1..20 chars]


mp4100>config>mngmnt# user
```

## configure management access

Level help (`?`):
```text
[no] access-group          - Apply ACL to device management
      auth-policy           - Set authentication sequence
      clear-statistics      - Clear ACL statistics
 [no] sftp                  - Enable SFTP
 [no] snmp                  - Enables/disables SNMP access
      ssh-encryption        - 
      ssh-key-exchange      - 
      ssh-mac               - 
 [no] ssh                   - Enables/disables Secure Shell (SSH) access
 [no] telnet                - Enables/disables Telnet access
 [no] tftp                  - Enable TFTP

 show access-list           - ACL information
```

### access-group
```text
<acl-name>           : ACL name [string]


mp4100>config>mngmnt>access# access-group
```

### auth-policy
```text
<1st-level>          : First method


mp4100>config>mngmnt>access# auth-policy
```

### clear-statistics
```text
<access-list>        : ACL


mp4100>config>mngmnt>access# clear-statistics
```

### sftp
```text
<CR>

mp4100>config>mngmnt>access# sftp
```

### show access-list
```text
<statistics>         : ACL statistics
 <summary>            : ACL summary


mp4100>config>mngmnt>access# show access-list
```

### snmp
```text
<CR>
 <managers-only>      : Allows access to listed managers only


mp4100>config>mngmnt>access# snmp
```

### ssh
```text
<CR>
 <managers-only>      : Allows access to listed managers only


mp4100>config>mngmnt>access# ssh
```

### ssh-encryption
```text
<all>                : 
 <algorithm>          : 


mp4100>config>mngmnt>access# ssh-encryption
```

### ssh-key-exchange
```text
<all>                : 
 <algorithm>          : 


mp4100>config>mngmnt>access# ssh-key-exchange
```

### ssh-mac
```text
<all>                : 
 <algorithm>          : 


mp4100>config>mngmnt>access# ssh-mac
```

### telnet
```text
<CR>
 <managers-only>      : Allows access to listed managers only


mp4100>config>mngmnt>access# telnet
```

### tftp
```text
<CR>

mp4100>config>mngmnt>access# tftp
```

## configure management radius

Level help (`?`):
```text
[no] attribute-send        - Send RADIUS request with/without atributes
      clear-statistics      - Clear RADIUS statistics
 [no] map-service-type      - Send service-type 
      server                + Connect to RADIUS server

 show statistics            - RADIUS statistics
 show status                - RADIUS status
```

### attribute-send
```text
<nas-ip-address>     : 


mp4100>config>mngmnt>radius# attribute-send
```

### clear-statistics
```text
<CR>

mp4100>config>mngmnt>radius# clear-statistics
```

### map-service-type
```text
<unknown>            : 


mp4100>config>mngmnt>radius# map-service-type
```

### server *(parameterized — inner help harvested under "configure management radius server NAME")*
```text
<server-id>          : Specify  RADIUS server  [1..4]


mp4100>config>mngmnt>radius# server
```

### show statistics
```text
<CR>

mp4100>config>mngmnt>radius# show statistics
```

### show status
```text
<CR>

mp4100>config>mngmnt>radius# show status
```

## configure management radius server NAME

Level help (`?`):
```text
address               - RADIUS server IP address
      auth-port             - RADIUS UDP port
      key                   - Shared secret 
      retry                 - Authentication attempts 
      timeout               - Timeout
```

### address
```text
<ip-address>         : IP address [0.0.0.0]


mp4100>config>mngmnt>radius>server(1)# address
```

### auth-port
```text
<udp-port-number>    : UDP port number [1..65535, default 1812]


mp4100>config>mngmnt>radius>server(1)# auth-port
```

### key
```text
<string>             : Shared secret [1..80 chars]


mp4100>config>mngmnt>radius>server(1)# key
```

### retry
```text
<number-of-retries>  : Retries [0..10]


mp4100>config>mngmnt>radius>server(1)# retry
```

### shutdown
```text
# cli error: Invalid Command
mp4100>config>mngmnt>radius>server(1)# shutdown
```

### timeout
```text
<seconds>            : Duration [1..5]


mp4100>config>mngmnt>radius>server(1)# timeout
```

## configure management snmp

Level help (`?`):
```text
community             - Specifies SNMP communities
      server                + 
      snmp-engine-id        - Configure SNMP Engine ID
 [no] snmpv3                - SNMPv3 commands
```

### access-group *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>mngmnt>snmp# access-group
```

### community
```text
read
 write
 trap

mp4100>config>mngmnt>snmp# community
```

### notify *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>mngmnt>snmp# notify
```

### notify-filter *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>mngmnt>snmp# notify-filter
```

### notify-filter-profile *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>mngmnt>snmp# notify-filter-profile
```

### security-to-group *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>mngmnt>snmp# security-to-group
```

### snmp-engine-id
```text
<mac>                : MAC
 <ipv4>               : IPv4
 <text>               : Free text


mp4100>config>mngmnt>snmp# snmp-engine-id
```

### snmpv3
```text
<CR>

mp4100>config>mngmnt>snmp# snmpv3
```

### target *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>mngmnt>snmp# target
```

### target-params *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>mngmnt>snmp# target-params
```

### user *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>mngmnt>snmp# user
```

### view *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>mngmnt>snmp# view
```

## configure management snmp server

Level help (`?`):
```text
[no] trap-source-address   -
```

### trap-source-address
```text
<address>            : [0.0.0.0]


mp4100>config>mngmnt>snmp>server# trap-source-address
```

## configure management tacacsplus

Level help (`?`):
```text
[no] group                 + TACACS+ server group
 [no] server                + Add TACACS+ server
```

### group *(parameterized — inner help harvested under "configure management tacacsplus group NAME")*
```text
<group-name>         : TACACS+ server group name [1..32 chars]


mp4100>config>mngmnt>tacacsplus# group
```

### server *(not entered — parameterized context)*
```text
<ip>                 : TACACS+ server IP address [0.0.0.0]


mp4100>config>mngmnt>tacacsplus# server
```

## configure management tacacsplus group NAME

Level help (`?`):
```text
[no] accounting            - Enable TACACS+ accounting


mp4100>config>mngmnt>tacacsplus>group(zzz-hrvst)$
```

### accounting
```text
<shell>              : Shell accounting
 <system>             : System accounting
 <commands>           : Commands accounting


mp4100>config>mngmnt>tacacsplus>group(zzz-hrvst)$ accounting
```

## configure oam

Level help (`?`):
```text
cfm                   + OAM CFM configurarion
 [no] efm-descriptor        + Configure EFM descriptor
```

### efm-descriptor *(not entered — parameterized context)*
```text
<number>             : EFM descriptor ID [1..2]


mp4100>config>oam# efm-descriptor
```

## configure oam cfm

Level help (`?`):
```text
ethertype             - Standard EtherType in an OAM message
 [no] maintenance-domain    + Creates/deletes a maintenance domain
 [no] md-level-mip          - Define MD level MIP
 [no] measurement-bin-prof* + measurement-bin-profile
      multicast-addr        - Standard MAC address in an OAM message

 show mips
 show summary
```

### ethertype
```text
<ethertype>          : Standard Ether Type in an OAM message [00-ffff]


mp4100>config>oam>cfm# ethertype
```

### maintenance-domain *(not entered — parameterized context)*
```text
<mdid>               : Index of the maintenance domain [number]


mp4100>config>oam>cfm# maintenance-domain
```

### md-level-mip
```text
<md-level-list>      : MD level list [0..7]


mp4100>config>oam>cfm# md-level-mip
```

### measurement-bin-profile *(not entered — parameterized context)*
```text
<name>               : [1..32 chars]


mp4100>config>oam>cfm# measurement-bin-profile
```

### multicast-addr
```text
<mac-address>        : Standard MAC address in an OAM message. 
                        [00-00-00-00-00-00, default 0180C2000000]


mp4100>config>oam>cfm# multicast-addr
```

### show mips
```text
<CR>

mp4100>config>oam>cfm# show mips
```

### show summary
```text
<CR>

mp4100>config>oam>cfm# show summary
```

## configure port

Level help (`?`):
```text
[no] analog-signaling-pro* + Add/Delete Analog signaling profile
      bri                   + Configure BRI port
      clear-cmd-led         - Clear teleprotection latched leds
      cmd-channel           + Configure cmd-channel port
      cmd-in                + Configure cmd-in port
      cmd-in-i              + Configure cmd-in-i (internal) port
      cmd-out               + Configure cmd-out port
      cmd-out-i             + Configure cmd-out-i (internal) port
 [no] ds0-bundle            + Create/delete ds0-bundle
      ds0-g703              + Define DS0 G703 port parameters
      ds1                   + Configure DS1 port
      ds1-opt               + Configure DS1 optical port
      e1                    + Configure E1 port
      e1-i                  + Configure E1-i (internal) port
      ethernet              + Specifies Ethernet parameters
 [no] gfp                   + Specifies GFP port parameters
 [no] hdlc                  + Specifies HDLC parameters
      int-ethernet          + Specifies Internal Ethernet parameters
 [no] l2cp-profile          + Defines l2cp profile
 [no] lag                   + 
 [no] logical-mac           + Specifies Logical MAC port parameters
 [no] lre                   + Add/Remove LRE port
 [no] mlppp                 + Specifies MLPPP parameters
      mng-ethernet          + Specifies Ethernet management parameters
      mux-eth-tdm           + Link use to transport  TDM/ETH services
 [no] pcs                   + Specifies physical coding sublayer parameters
 [no] ppp                   + 
      sdh-sonet             + Defines SDH/SONET port parameters
      serial                + Define SERIAL port parameters
      serial-bundle         + Define SERIAL BUNDLE port parameters
      shdsl                 + Defines an SHDSL port
 [no] signaling-profile     + Defines Signaling profile
 [no] svi                   + Create/delete service virtual interface
      t1                    + Configure T1 port
      t1-i                  + Configure T1-i (internal) port
      t3                    + Configure T3 port
      tdm-bridge            + Link use to transport  TDM/Bridge services
 [no] vcg                   + Specifies VCG parameters
 [no] vc-profile            + Defines SDH/Sonet VC profile
      voice                 + Define VOICE port parameters

 show lag-summary
 show summary               - Display port status summary
 show svi-summary
```

### analog-signaling-profile *(parameterized — inner help harvested under "configure port analog-signaling-profile NAME")*
```text
<name>               : profile name [1..32 chars]


mp4100>config>port# analog-signaling-profile
```

### bri *(not entered — parameterized context)*
```text
<port-number>        : Port number [slot/port[/tributary]]


mp4100>config>port# bri
```

### clear-cmd-led
```text
<all>                : All teleprotection latched leds
 <cmd-in>             : Cmd-in latched leds
 <cmd-out>            : Cmd-out latched leds


mp4100>config>port# clear-cmd-led
```

### cmd-channel *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port]


mp4100>config>port# cmd-channel
```

### cmd-in *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port[/tributary]]


mp4100>config>port# cmd-in
```

### cmd-in-i *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port/tributary]


mp4100>config>port# cmd-in-i
```

### cmd-out *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port[/tributary]]


mp4100>config>port# cmd-out
```

### cmd-out-i *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port/tributary]


mp4100>config>port# cmd-out-i
```

### ds0-bundle *(not entered — parameterized context)*
```text
<port-index>         : DS0 Bundle port index [slot/port]


mp4100>config>port# ds0-bundle
```

### ds0-g703 *(not entered — parameterized context)*
```text
<port-index>         : Port index [slot/port]


mp4100>config>port# ds0-g703
```

### ds1 *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port]


mp4100>config>port# ds1
```

### ds1-opt *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port]


mp4100>config>port# ds1-opt
```

### e1 *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port[/tributary]]


mp4100>config>port# e1
```

### e1-i *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port]


mp4100>config>port# e1-i
```

### ethernet *(parameterized — inner help harvested under "configure port ethernet NAME")*
```text
<port-index>         : Port number [slot/port[/tributary]]


mp4100>config>port# ethernet
```

### gfp *(not entered — parameterized context)*
```text
<port-index>         : GFP port index [slot/port]


mp4100>config>port# gfp
```

### hdlc *(not entered — parameterized context)*
```text
<port-index>         : HDLC port index [slot/port]


mp4100>config>port# hdlc
```

### int-ethernet *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port]


mp4100>config>port# int-ethernet
```

### l2cp-profile *(parameterized — inner help harvested under "configure port l2cp-profile NAME")*
```text
<l2cp-profile-name>  : Index of the profile [1..32 chars]


mp4100>config>port# l2cp-profile
```

### lag *(parameterized — inner help harvested under "configure port lag NAME")*
```text
<port-number>        : LAG port number [number]


mp4100>config>port# lag
```

### logical-mac *(not entered — parameterized context)*
```text
<port-index>         : Logical MAC port index [slot/port]


mp4100>config>port# logical-mac
```

### lre *(not entered — parameterized context)*
```text
<port-number>        : LRE port number [number]


mp4100>config>port# lre
```

### mlppp *(not entered — parameterized context)*
```text
<port-index>         : MLPPP port index [slot/port]


mp4100>config>port# mlppp
```

### mng-ethernet *(parameterized — inner help harvested under "configure port mng-ethernet NAME")*
```text
<port-index>         : Port number [slot/port]


mp4100>config>port# mng-ethernet
```

### mux-eth-tdm *(not entered — parameterized context)*
```text
<port-number>        : logical Port number [slot/port]


mp4100>config>port# mux-eth-tdm
```

### pcs *(not entered — parameterized context)*
```text
<port-index>         : Physical coding sublayer port number 
                        [slot/port[/tributary]]


mp4100>config>port# pcs
```

### ppp *(not entered — parameterized context)*
```text
<port-index>         : PPP Port index [slot/port]


mp4100>config>port# ppp
```

### sdh-sonet *(parameterized — inner help harvested under "configure port sdh-sonet NAME")*
```text
<port-index>         : Port number [slot/port]


mp4100>config>port# sdh-sonet
```

### serial *(not entered — parameterized context)*
```text
<port-number>        : Port number [slot/port]


mp4100>config>port# serial
```

### serial-bundle *(not entered — parameterized context)*
```text
<port-number>        : Port number [slot/port]


mp4100>config>port# serial-bundle
```

### shdsl *(not entered — parameterized context)*
```text
<port-number>        : Port number [slot/port]


mp4100>config>port# shdsl
```

### show lag-summary
```text
<CR>

mp4100>config>port# show lag-summary
```

### show summary
```text
<detail>             : 
 <counters>           : 


mp4100>config>port# show summary
```

### show svi-summary
```text
<CR>

mp4100>config>port# show svi-summary
```

### signaling-profile *(parameterized — inner help harvested under "configure port signaling-profile NAME")*
```text
<signaling-profil*>  : Index of the profile [string]


mp4100>config>port# signaling-profile
```

### svi *(parameterized — inner help harvested under "configure port svi NAME")*
```text
<port-number>        : SVI port number [number]


mp4100>config>port# svi
```

### t1 *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port[/tributary]]


mp4100>config>port# t1
```

### t1-i *(parameterized — inner help harvested under "configure port t1-i NAME")*
```text
<port-index>         : Port number [slot/port]


mp4100>config>port# t1-i
```

### t3 *(not entered — parameterized context)*
```text
<port-index>         : Port number [slot/port]


mp4100>config>port# t3
```

### tdm-bridge *(not entered — parameterized context)*
```text
<port-number>        : logical Port number [slot/port]


mp4100>config>port# tdm-bridge
```

### vc-profile *(parameterized — inner help harvested under "configure port vc-profile NAME")*
```text
<vc-profile-name>    : Index of the profile [1..32 chars]


mp4100>config>port# vc-profile
```

### vcg *(not entered — parameterized context)*
```text
<port-index>         : VCG port index [slot/port]


mp4100>config>port# vcg
```

### voice *(not entered — parameterized context)*
```text
<port-number>        : Port number [slot/port[/tributary]]


mp4100>config>port# voice
```

## configure port analog-signaling-profile NAME

Level help (`?`):
```text
a-bit-rx              - Define 'A' bit signaling in the Rx direction
      a-bit-tx              - Define 'A' bit signaling in the Tx direction
      b-bit-rx              - Define 'B' bit signaling in the Rx direction
      b-bit-tx              - Define 'B' bit signaling in the Tx direction
      c-bit-rx              - Define 'C' bit signaling in the Rx direction
      c-bit-tx              - Define 'C' bit signaling in the Tx direction
      d-bit-rx              - Define 'D' bit signaling in the Rx direction
      d-bit-tx              - Define 'D' bit signaling in the Tx direction
```

### a-bit-rx
```text
<not-used>           : 
 <signaling>          : 
 <inverse-sig>        : 
 <forward-disconnect> : 
 <inverse-forward-*>  : 


mp4100>config>port>analog-signaling-pro(sig_over_a_bit)# a-bit-rx
```

### a-bit-tx
```text
<1>                  : 
 <0>                  : 
 <signaling>          : 
 <inverse-sig>        : 
 <loop-disconnect>    : 


mp4100>config>port>analog-signaling-pro(sig_over_a_bit)# a-bit-tx
```

### b-bit-rx
```text
<not-used>           : 
 <signaling>          : 
 <inverse-sig>        : 
 <forward-disconnect> : 
 <inverse-forward-*>  : 
 <wink>               : 


mp4100>config>port>analog-signaling-pro(sig_over_a_bit)# b-bit-rx
```

### b-bit-tx
```text
<1>                  : 
 <0>                  : 
 <signaling>          : 
 <inverse-sig>        : 
 <loop-disconnect>    : 
 <inverse-loop-dis*>  : 
 <wink>               : 


mp4100>config>port>analog-signaling-pro(sig_over_a_bit)# b-bit-tx
```

### c-bit-rx
```text
<not-used>           : 
 <forward-disconnect> : 
 <wink>               : 


mp4100>config>port>analog-signaling-pro(sig_over_a_bit)# c-bit-rx
```

### c-bit-tx
```text
<1>                  : 
 <0>                  : 
 <signaling>          : 
 <loop-disconnect>    : 
 <wink>               : 


mp4100>config>port>analog-signaling-pro(sig_over_a_bit)# c-bit-tx
```

### d-bit-rx
```text
<not-used>           : 
 <signaling>          : 
 <inverse-sig>        : 


mp4100>config>port>analog-signaling-pro(sig_over_a_bit)# d-bit-rx
```

### d-bit-tx
```text
<1>                  : 
 <0>                  : 
 <signaling>          : 
 <inverse-sig>        : 


mp4100>config>port>analog-signaling-pro(sig_over_a_bit)# d-bit-tx
```

## configure port ethernet NAME

Level help (`?`):
```text
[no] auto-negotiation      - Enables/disables automatically adjusting the speed
      clear-efm-statistics  - 
      clear-statistics      - Clears all statistics
      dot1x                 + 802.1X  level
 [no] efm                   + Enables/disables OAM (EFM) on the Ethernet port
      egress-mtu            - Defines the max frame size to transmit
 [no] l2cp                  - Enables/disables the Layer 2 Control Protocol
      macsec                + MACsec  level
      max-capability        - Identifies the set of capabilities advertised by 
                              the local autonegotiation entity
      min-tagged-frame-len* - Defines the minimum frame length in bytes. 
 [no] name                  - Assigns/removes a port name
 [no] pm-collection         - Enable Performance Management (PM) 
 [no] queue-group           - Assigns/removes a queue group profile
 [no] shaper                - Activates/deactivates a shaper profile
 [no] shutdown              - Administratively disables/enables the port
      speed-duplex          - Specifies speed and duplex mode when 
                              autonegotiation is disabled
      tag-ethernet-type     - Determines the tag protocol identifier
 [no] tx-ssm                - Enables/disables Synchronous Status Messages 
                              transmission

 show status                - Displays the Ethernet port status
```

### auto-negotiation
```text
<CR>

mp4100>config>port>eth(cl-a/1)# auto-negotiation
```

### clear-efm-statistics
```text
<CR>

mp4100>config>port>eth(cl-a/1)# clear-efm-statistics
```

### clear-statistics
```text
<CR>

mp4100>config>port>eth(cl-a/1)# clear-statistics
```

### efm *(not entered — parameterized context)*
```text
descriptor

mp4100>config>port>eth(cl-a/1)# efm
```

### egress-mtu
```text
<size>               : Specifies the Max Transition Unit size (bytes) 
                        [64..13312, default 1790]


mp4100>config>port>eth(cl-a/1)# egress-mtu
```

### flow-control
```text
# cli error: Invalid Command
mp4100>config>port>eth(cl-a/1)# flow-control
```

### l2cp
```text
profile

mp4100>config>port>eth(cl-a/1)# l2cp
```

### max-capability
```text
<10-half-duplex>     : Sets Max Capability to 10 BaseT Half Duplex
 <10-full-duplex>     : Sets Max Capability to 10 BaseT Full Duplex
 <100-half-duplex>    : Sets Max Capability to 100 BaseT Half Duplex
 <100-full-duplex>    : Sets Max Capability to 100 BaseT Full Duplex
 <1000-half-duplex>   : Sets Max Capability to 1000 BaseT Half Duplex.
 <1000-full-duplex>   : Sets Max Capability to 1000 BaseT Full Duplex
 <1000-x-full-duplex> : Sets Max Capability to 1000 BaseX, -LX, -SX, -CX Full 
                        Duplex


mp4100>config>port>eth(cl-a/1)# max-capability
```

### name
```text
<string>             : Adds free text to assign a name to the port [1..64 
                        chars]


mp4100>config>port>eth(cl-a/1)# name
```

### pm-collection
```text
interval

mp4100>config>port>eth(cl-a/1)# pm-collection
```

### policer
```text
# cli error: Invalid Command
mp4100>config>port>eth(cl-a/1)# policer
```

### queue-group
```text
profile

mp4100>config>port>eth(cl-a/1)# queue-group
```

### show oam-efm
```text
# cli error: Invalid Command
mp4100>config>port>eth(cl-a/1)# show oam-efm
```

### show oam-efm-statistics
```text
# cli error: Invalid Command
mp4100>config>port>eth(cl-a/1)# show oam-efm-statistics
```

### show sfp-status
```text
# cli error: Invalid Command
mp4100>config>port>eth(cl-a/1)# show sfp-status
```

### show statistics
```text
# cli error: Invalid Command
mp4100>config>port>eth(cl-a/1)# show statistics
```

### shutdown
```text
<CR>

mp4100>config>port>eth(cl-a/1)# shutdown
```

### speed-duplex
```text
<10-half-duplex>     : Sets the interface to 10 BaseT Half Duplex
 <10-full-duplex>     : Sets the interface to 10 BaseT Full Duplex
 <100-half-duplex>    : Sets the interface to 100 BaseT Half Duplex
 <100-full-duplex>    : Sets the interface to 100 BaseT Full Duplex
 <1000-half-duplex>   : Sets the interface to 1000 BaseT Half Duplex
 <1000-full-duplex>   : Sets the interface to 1000 BaseT Full Duplex
 <1000-x-full-duplex> : Sets the interface to 1000 BaseX, -LX, -SX, -CX Full 
                        Duplex
 <10g-sr>             : Sets the interface to 10G Base SR
 <10g-lr>             : Sets the interface to 10G Base LR
 <10g-er>             : Sets the interface to 10G Base ER
 <10g-x-full-duplex>  : Sets the interface to 10g BaseX, -LX, -SX, -CX Full 
                        Duplex


mp4100>config>port>eth(cl-a/1)# speed-duplex
```

### tag-ethernet-type
```text
<ether-type>         : Determines the tag protocol identifier (hex numbers) 
                        [00-ffff, default 0x8100]


mp4100>config>port>eth(cl-a/1)# tag-ethernet-type
```

## configure port l2cp-profile NAME

Level help (`?`):
```text
default               - Default action for not defined control protocols
 [no] mac                   - 
 [no] protocol              - Choose specific protocol
 [no] protocol              - Choose specific protocol
 [no] protocol              - Choose specific protocol
 [no] protocol              - Choose specific protocol
```

### default
```text
<discard>            : 
 <tunnel>             : 


mp4100>config>port>l2cp-profile(L2cpDefaultProf)# default
```

### mac
```text
<mac-addr>           : Control protocol MAC [00-00-00-00-00-00]


mp4100>config>port>l2cp-profile(L2cpDefaultProf)# mac
```

### protocol
```text
<efm-oam>            : 
 <port-authenticat*>  : 
 <lacp>               : 
 <garp>               : 
 <stp>                : 
 <vtp>                : 
 <cdp>                : 
 <lldp>               : 
 <pvstp>              : 
 <pagp>               : 
 <udld>               : 
 <dtp>                : 


mp4100>config>port>l2cp-profile(L2cpDefaultProf)# protocol
```

## configure port lag NAME

Level help (`?`):
```text
admin-key             - Defines LAG capability
 [no] bind                  - 
      distribution-method   - Defines load sharing between LAG ports
 [no] lacp                  - Enable the lacp protocol on the  LAG
 [no] name                  - Name of the LAG
 [no] queue-group           - Assigns/removes a queue group profile
 [no] shutdown              - shutdown the LAG

 show bind
 show lacp-statistics       - Displays the LAG members statistics
 show lacp-status           - Displays LAG members status
 show statistics
 show status

mp4100>config>port>lag(1)$
```

### admin-key
```text
<fast-ethernet>      : Defines Fast Ethernet capability for the LAG
 <giga-ethernet>      : Defines Giga Ethernet capability for the LAG
 <ten-giga-ethernet>  : Defines 10 Giga Ethernet capability for the LAG


mp4100>config>port>lag(1)$ admin-key
```

### bind
```text
<ethernet>           : 


mp4100>config>port>lag(1)$ bind
```

### clear-lacp-statistics
```text
# cli error: Invalid Command
mp4100>config>port>lag(1)$ clear-lacp-statistics
```

### clear-statistics
```text
# cli error: Invalid Command
mp4100>config>port>lag(1)$ clear-statistics
```

### distribution-method
```text
<dest-mac>           : Distribution according to dest mac address


mp4100>config>port>lag(1)$ distribution-method
```

### lacp
```text
<CR>
 tx-activity
 tx-speed
 sys-priority

mp4100>config>port>lag(1)$ lacp
```

### name
```text
<string>             : [1..64 chars]


mp4100>config>port>lag(1)$ name
```

### queue-group
```text
profile

mp4100>config>port>lag(1)$ queue-group
```

### show bind
```text
<CR>

mp4100>config>port>lag(1)$ show bind
```

### show lacp-statistics
```text
<ethernet>           : 


mp4100>config>port>lag(1)$ show lacp-statistics
```

### show lacp-status
```text
<ethernet>           : 


mp4100>config>port>lag(1)$ show lacp-status
```

### show statistics
```text
<CR>

mp4100>config>port>lag(1)$ show statistics
```

### show status
```text
<CR>

mp4100>config>port>lag(1)$ show status
```

### shutdown
```text
<CR>

mp4100>config>port>lag(1)$ shutdown
```

## configure port mng-ethernet NAME

Level help (`?`):
```text
[no] auto-negotiation      - Enables/disables automatically adjusting the speed
 [no] flow-control          - Enables/disables the flow control
      max-capability        - Identifies the set of capabilities advertised by 
                              the local autonegotiation entity
 [no] name                  - Assigns/removes a port name
 [no] shutdown              - Administratively disables/enables the port

 show bind                  - Displays a list of interfaces bound to the bridge
 show status                - Displays the Ethernet port status
```

### auto-negotiation
```text
<CR>

mp4100>config>port>mng-eth(cl-a/1)# auto-negotiation
```

### flow-control
```text
<CR>

mp4100>config>port>mng-eth(cl-a/1)# flow-control
```

### max-capability
```text
<10-half-duplex>     : Sets Max Capability to 10 BaseT Half Duplex
 <10-full-duplex>     : Sets Max Capability to 10 BaseT Full Duplex
 <100-half-duplex>    : Sets Max Capability to 100 BaseT Half Duplex
 <100-full-duplex>    : Sets Max Capability to 100 BaseT Full Duplex


mp4100>config>port>mng-eth(cl-a/1)# max-capability
```

### name
```text
<string>             : Adds free text to assign a name to the port [1..64 
                        chars]


mp4100>config>port>mng-eth(cl-a/1)# name
```

### show bind
```text
<CR>

mp4100>config>port>mng-eth(cl-a/1)# show bind
```

### show status
```text
<CR>

mp4100>config>port>mng-eth(cl-a/1)# show status
```

### shutdown
```text
<CR>

mp4100>config>port>mng-eth(cl-a/1)# shutdown
```

### speed-duplex
```text
# cli error: Invalid Command
mp4100>config>port>mng-eth(cl-a/1)# speed-duplex
```

## configure port sdh-sonet NAME

Level help (`?`):
```text
[no] automatic-laser-shut* - Enable/disable automatic laser shutdown
      clear-statistics      - Clears the statistics
 [no] dcc                   - Enables/disables DCC inband management
      frame-type            - Specifies the cell frame type
      j0-pathtrace          - Sets section trace bytes in the section header
 [no] loopback              - Enables/disables loopback mode for the port
 [no] name                  - Assigns/removes a port name
      oc3                   + Defines an OC-3 (STM-1) connection
 [no] pm-collection         - Enable Performance Management (PM) 
 [no] rdi-on-failure        - Enables/disables triggering RDI on failure
 [no] shutdown              - Administratively disables/enables the port
      speed                 - Selects the port speed
      threshold             - Bit error rate above which an alarm is triggered
 [no] tim-response          - Enables/disables triggering AIS & RDI on path 
                              trace error
 [no] tx-ssm                - Force/Unforce DNU/DUS transmit

 show sfp-status            - Displays the SDH/SONET port SFP status
 show statistics            - Displays the specified SDH/SONET statistics
 show status                - Displays the SDH-SONET status of the port
```

### aug *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>port>sdh-sonet(cl-a/1)# aug
```

### automatic-laser-shutdown
```text
<CR>

mp4100>config>port>sdh-sonet(cl-a/1)# automatic-laser-shutdown
```

### clear-statistics
```text
<current-interval>   : 
 <current-all>        : 


mp4100>config>port>sdh-sonet(cl-a/1)# clear-statistics
```

### dcc
```text
encapsulation
 mode
 routing-protocol
 deviation

mp4100>config>port>sdh-sonet(cl-a/1)# dcc
```

### frame-type
```text
<sdh>                : Sets the cell frame type to SDH
 <sonet>              : Sets the cell frame type to SONET


mp4100>config>port>sdh-sonet(cl-a/1)# frame-type
```

### j0-pathtrace
```text
direction
 string
 padding

mp4100>config>port>sdh-sonet(cl-a/1)# j0-pathtrace
```

### loopback
```text
<remote>             : 


mp4100>config>port>sdh-sonet(cl-a/1)# loopback
```

### name
```text
<string>             : Adds free text to assign a name to the port [1..64 
                        chars]


mp4100>config>port>sdh-sonet(cl-a/1)# name
```

### oc3 *(parameterized — inner help harvested under "configure port sdh-sonet NAME oc3 NAME")*
```text
<oc3-num>            : Assigns an ID to the OC-3 connection [number]


mp4100>config>port>sdh-sonet(cl-a/1)# oc3
```

### pm-collection
```text
interval

mp4100>config>port>sdh-sonet(cl-a/1)# pm-collection
```

### rdi-on-failure
```text
<CR>

mp4100>config>port>sdh-sonet(cl-a/1)# rdi-on-failure
```

### show sfp-status
```text
<CR>

mp4100>config>port>sdh-sonet(cl-a/1)# show sfp-status
```

### show statistics
```text
<current>            : Displays the current statistics
 <interval>           : Displays statistics of a specified interval
 <all>                : Displays all statistics


mp4100>config>port>sdh-sonet(cl-a/1)# show statistics
```

### show status
```text
<CR>

mp4100>config>port>sdh-sonet(cl-a/1)# show status
```

### shutdown
```text
<CR>

mp4100>config>port>sdh-sonet(cl-a/1)# shutdown
```

### speed
```text
<155mbps>            : Sets the port speed to 155 Mbps
 <622mbps>            : Sets the port speed to 622 Mbps


mp4100>config>port>sdh-sonet(cl-a/1)# speed
```

### threshold
```text
eed
 sd

mp4100>config>port>sdh-sonet(cl-a/1)# threshold
```

### tim-response
```text
<CR>

mp4100>config>port>sdh-sonet(cl-a/1)# tim-response
```

### tx-ssm
```text
<CR>

mp4100>config>port>sdh-sonet(cl-a/1)# tx-ssm
```

## configure port sdh-sonet NAME oc3 NAME

Level help (`?`):
```text
[no] name                  - Assigns/removes a port name
      sts1                  + Number in the range from 1 to 3.
```

### name
```text
<string>             : Adds free text to assign a name to the port [1..64 
                        chars]


mp4100>config>port>sdh-sonet(cl-a/1)>oc3(1)# name
```

### pm-collection
```text
# cli error: Invalid Command
mp4100>config>port>sdh-sonet(cl-a/1)>oc3(1)# pm-collection
```

### sts1 *(parameterized — inner help harvested under "configure port sdh-sonet NAME oc3 NAME sts1 NAME")*
```text
<sts1-num>           : sts1 number [1..3]


mp4100>config>port>sdh-sonet(cl-a/1)>oc3(1)# sts1
```

### vc
```text
# cli error: Invalid Command
mp4100>config>port>sdh-sonet(cl-a/1)>oc3(1)# vc
```

## configure port sdh-sonet NAME oc3 NAME sts1 NAME

Level help (`?`):
```text
[no] loopback              - Enables/disables loopback mode
 [no] pm-collection         - Enable Performance Management (PM) 
      vc                    - 
      vt1-5                 + Specifies VT-1.5 as Sonet Channelized format
```

### loopback
```text
<local>              : 
 <remote>             : 


mp4100>config>port>sdh-sonet(cl-a/1)>oc3(1)>sts1(1)# loopback
```

### pm-collection
```text
interval

mp4100>config>port>sdh-sonet(cl-a/1)>oc3(1)>sts1(1)# pm-collection
```

### vc
```text
profile

mp4100>config>port>sdh-sonet(cl-a/1)>oc3(1)>sts1(1)# vc
```

### vt1-5 *(not entered — parameterized context)*
```text
<vtg-num>            : vtg number [1..7]


mp4100>config>port>sdh-sonet(cl-a/1)>oc3(1)>sts1(1)# vt1-5
```

## configure port signaling-profile NAME

Level help (`?`):
```text
a-bit-code            - 
      b-bit-code            - 
      busy-code             - 
      c-bit-code            - 
      d-bit-code            - 
      idle-code             -
```

### a-bit-code
```text
tx

mp4100>config>port>signaling-profile(profile1)# a-bit-code
```

### b-bit-code
```text
tx

mp4100>config>port>signaling-profile(profile1)# b-bit-code
```

### busy-code
```text
<code-type>          : Select the incoming pattern to be interpreted internally
                         as the busy state [0x00..0x0F]


mp4100>config>port>signaling-profile(profile1)# busy-code
```

### c-bit-code
```text
tx

mp4100>config>port>signaling-profile(profile1)# c-bit-code
```

### d-bit-code
```text
tx

mp4100>config>port>signaling-profile(profile1)# d-bit-code
```

### idle-code
```text
<code-type>          : Select the incoming pattern to be interpreted internally
                         as the busy state [0x00..0x0F]


mp4100>config>port>signaling-profile(profile1)# idle-code
```

## configure port svi NAME

Level help (`?`):
```text
[no] name                  - Assign name to the SVI port
 [no] shutdown              - Administrtavly enable/disable the SVI port
```

### name
```text
<string>             : SVI port name [1..64 chars]


mp4100>config>port>svi(1)# name
```

### shutdown
```text
<CR>

mp4100>config>port>svi(1)# shutdown
```

## configure port t1-i NAME

Level help (`?`):
```text
[no] bert                  - Activate BERT
      clear-statistics      - Clear port statistics
      idle-code             - Configure idle code
 [no] inband-management     - Configure inband management
      line-type             - Configure line type
 [no] name                  - Configure port name
      out-of-service        - Configure out of service signaling (OOS)
 [no] pm-collection         - Enable Performance Management (PM) 
      restoration-time      - Configure time to restore after LOF
 [no] shutdown              - Disable port
      vc                    - Associate SDH/SONET VC profile with port

 show statistics            - Display port statistics
 show status                - Display port status
```

### bert
```text
<CR>
 pattern
 duration
 ts
 inject-error

mp4100>config>port>t1-i(cl-a/1)# bert
```

### idle-code
```text
<idle-code-val>      : Idle code [0x00..0xFF]


mp4100>config>port>t1-i(cl-a/1)# idle-code
```

### inband-management
```text
<timeslot>           : Inband management timeslot [1..24]


mp4100>config>port>t1-i(cl-a/1)# inband-management
```

### line-type
```text
<unframed>           : Unframed
 <esf>                : Extended Super Frame (ESF)
 <sf>                 : Super Frame (SF)


mp4100>config>port>t1-i(cl-a/1)# line-type
```

### name
```text
<string>             : Port name [1..64 chars]


mp4100>config>port>t1-i(cl-a/1)# name
```

### out-of-service
```text
voice
 data
 signaling

mp4100>config>port>t1-i(cl-a/1)# out-of-service
```

### restoration-time
```text
<1sec>               : 1 second (fast)
 <10sec>              : 10 seconds (TR-6211)


mp4100>config>port>t1-i(cl-a/1)# restoration-time
```

### show status
```text
<CR>

mp4100>config>port>t1-i(cl-a/1)# show status
```

### shutdown
```text
<CR>

mp4100>config>port>t1-i(cl-a/1)# shutdown
```

## configure port vc-profile NAME

Level help (`?`):
```text
day-threshold         - Setting CV,ES,SES and/or UAS counter value during 
                              a 24-hour interval starting with a trap sent.
      interval-threshold    - Setting CV, ES, SES and/or UAS counter value 
                              during a 15-min interval starting with a trap 
                              sent.
 [no] pathtrace             - Enabling checking of the receive/transmit path 
                              trace label by port and conf. optional path trace 
                              dir
      payload-label         - Specifies the expected signal label
 [no] plm-response          - Enables/diables sending AIS and RDI upon signal 
                              label mismatch.
      rate-threshold        - Selecting EED (error rate degradation) and SD 
                              (signal degrade) thresholds
 [no] tim-response          - Enables/disables triggering AIS & RDI on path 
                              trace error.
```

### day-threshold
```text
cv
 es
 ses
 uas

mp4100>config>port>vc-profile(tug-structure)# day-threshold
```

### interval-threshold
```text
cv
 es
 ses
 uas

mp4100>config>port>vc-profile(tug-structure)# interval-threshold
```

### pathtrace
```text
direction
 length
 string
 padding

mp4100>config>port>vc-profile(tug-structure)# pathtrace
```

### payload-label
```text
<label-val>          : Specifies the The payload label of the VC [0x00..0xFF]


mp4100>config>port>vc-profile(tug-structure)# payload-label
```

### plm-response
```text
<rdi>                : 


mp4100>config>port>vc-profile(tug-structure)# plm-response
```

### rate-threshold
```text
eed
 sd

mp4100>config>port>vc-profile(tug-structure)# rate-threshold
```

### tim-response
```text
<rdi>                : 


mp4100>config>port>vc-profile(tug-structure)# tim-response
```

## configure protection

Level help (`?`):
```text
[no] accelerated-eth-hw-s* - Accelerated  HW redundancy between CL.2 modules
 [no] aps                   + Enables/disables port protection
 [no] ds0-group             + Define ds0 bundle protection group
 [no] erp                   + Ethernet Ring Protection
 [no] ethernet-group        + Enables/disables ethernet port protection
 [no] io-group              + Input/Output card protection group configuration
 [no] pw                    + Input/Output pw protection group configuration
 [no] tdm-group             + Define tdm protection group
 [no] tdm-ring              + Define tdm protection ring
 [no] vc-path               + Input/Output card protection group configuration

 show summary-ds0-group
 show summary-tdm-group     - Display the tdm protection group status
 show summary-vc-path       - Display status of Input/Output card protection 
                               group.
```

### accelerated-eth-hw-switchover
```text
<CR>

mp4100>config>protection# accelerated-eth-hw-switchover
```

### aps *(not entered — parameterized context)*
```text
<group-name>         : Assigns a name to the newly created APS group [1..32 
                        chars]


mp4100>config>protection# aps
```

### ds0-group *(not entered — parameterized context)*
```text
<group-id>           : Unique number that should identify the protection group.
                         [1..140]


mp4100>config>protection# ds0-group
```

### erp *(not entered — parameterized context)*
```text
<ring-number>        : [number] [1..5]


mp4100>config>protection# erp
```

### ethernet-group *(not entered — parameterized context)*
```text
<group-id>           : Assigns a number for ethernet group [number] [1..32]


mp4100>config>protection# ethernet-group
```

### io-group *(not entered — parameterized context)*
```text
<group-id>           : Unique number that should identify the protection group.
                         [number]


mp4100>config>protection# io-group
```

### pw *(parameterized — inner help harvested under "configure protection pw NAME")*
```text
<group-id>           : Unique number that should identify the protection group.
                         [number]


mp4100>config>protection# pw
```

### show summary-ds0-group
```text
<CR>

mp4100>config>protection# show summary-ds0-group
```

### show summary-tdm-group
```text
<CR>

mp4100>config>protection# show summary-tdm-group
```

### show summary-vc-path
```text
<CR>

mp4100>config>protection# show summary-vc-path
```

### tdm-group *(not entered — parameterized context)*
```text
<group-id>           : [1..144]


mp4100>config>protection# tdm-group
```

### tdm-ring *(not entered — parameterized context)*
```text
<ring-id>            : [1..16]


mp4100>config>protection# tdm-ring
```

### vc-path *(not entered — parameterized context)*
```text
<group-id>           : Unique number that should identify the protection group.
                         [1..255]


mp4100>config>protection# vc-path
```

## configure protection pw NAME

Level help (`?`):
```text
[no] bind                  - Bind a card to an IO card group.
 [no] name                  - 
      oper-mode             - Input/output card protection group operational 
                              mode
 [no] shutdown              - Enables/disables an IO card protection group

 show status                - Display status of Input/Output card protection 
                               group.

mp4100>config>protection>pw(1)$
```

### bind
```text
<working>            : 
 <protection>         : 


mp4100>config>protection>pw(1)$ bind
```

### name
```text
<string>             : [1..32 chars]


mp4100>config>protection>pw(1)$ name
```

### oper-mode
```text
<1-plus-1>           : 


mp4100>config>protection>pw(1)$ oper-mode
```

### show status
```text
<CR>

mp4100>config>protection>pw(1)$ show status
```

### shutdown
```text
<CR>

mp4100>config>protection>pw(1)$ shutdown
```

## configure pwe

Level help (`?`):
```text
[no] pw                    + Create/delete Pseudo-wire

 show summary               - Display PWs summary
```

### pw *(parameterized — inner help harvested under "configure pwe pw NAME")*
```text
<pw-number>          : A locally unique number which represents the PW [number]
                         [1..640]


mp4100>config>pwe# pw
```

### show summary
```text
<CR>

mp4100>config>pwe# show summary
```

## configure pwe pw NAME

Level help (`?`):
```text
[no] arp-table-refresh     - Controls whether the next-hop MAC is periodically 
                              refreshed according to the ARP table.
 [no] domain-failure-indic* - Controls whether the PW carry failure indication 
                              if local domain clock fails.
      far-end-type          - Define far end type of the connected device
      jitter-buffer         - Jitter buffer size
 [no] jitter-buffer-center* - Sets the threshold that causes jitter buffer flush
                               to re-center it.
      label                 - The PW label used in the inbound /outbound 
                              direction
 [no] name                  - The name given to the specified PW
 [no] oam                   - Enable/disable OAM protocol for this PW
 [no] peer                  - The number of the remote peer which terminated 
                              this PW 
 [no] sensitivity           - Constant delay
      source-clock-fail     - Conditions when the PW is considered failed for 
                              the CSM.
      tdm-oos               - Transmits an out of service signal (oos)
      tdm-payload           - TDM payload configuration
      tos                   - Configures the value of the IP TOS byte in egress 
                              packets
      udp-mux-method        - 
 [no] vlan                  - Enable/disable VLAN tag on every transmitted 
                              packet for this PW

 show status                - Display PW status parameters

mp4100>config>pwe>pw(1)$
```

### arp-table-refresh
```text
<CR>

mp4100>config>pwe>pw(1)$ arp-table-refresh
```

### domain-failure-indication
```text
<CR>

mp4100>config>pwe>pw(1)$ domain-failure-indication
```

### egress-port
```text
# cli error: Invalid Command
mp4100>config>pwe>pw(1)$ egress-port
```

### exp-bits
```text
# cli error: Invalid Command
mp4100>config>pwe>pw(1)$ exp-bits
```

### far-end-type
```text
<e1>                 : E1
 <t1-esf>             : T1 (ESF)
 <t1-sf>              : T1 (SF)
 <unframed>           : Serial
 <fxs-e1>             : FXS - E1
 <fxs-t1>             : FXS - T1


mp4100>config>pwe>pw(1)$ far-end-type
```

### jitter-buffer
```text
<jitter-size>        : Jitter buffer size in usec [number]


mp4100>config>pwe>pw(1)$ jitter-buffer
```

### jitter-buffer-centering
```text
deviation

mp4100>config>pwe>pw(1)$ jitter-buffer-centering
```

### label
```text
in
 out

mp4100>config>pwe>pw(1)$ label
```

### name
```text
<pw-name>            : The name given to the specified PW  [1..32 chars]


mp4100>config>pwe>pw(1)$ name
```

### oam
```text
<CR>

mp4100>config>pwe>pw(1)$ oam
```

### peer
```text
<peer-number>        : Peer number [number]


mp4100>config>pwe>pw(1)$ peer
```

### sensitivity
```text
<CR>

mp4100>config>pwe>pw(1)$ sensitivity
```

### show status
```text
<CR>

mp4100>config>pwe>pw(1)$ show status
```

### source-clock-fail
```text
<pw-down>            : 
 <remote-domain-down> : 


mp4100>config>pwe>pw(1)$ source-clock-fail
```

### tdm-oos
```text
voice
 data
 signaling

mp4100>config>pwe>pw(1)$ tdm-oos
```

### tdm-payload
```text
size

mp4100>config>pwe>pw(1)$ tdm-payload
```

### tos
```text
<tos>                : The value of the IP TOS byte in egress packets. [0 .. 
                        255]


mp4100>config>pwe>pw(1)$ tos
```

### udp-mux-method
```text
<dst-port>           : 
 <src-port>           : 


mp4100>config>pwe>pw(1)$ udp-mux-method
```

### vlan
```text
priority

mp4100>config>pwe>pw(1)$ vlan
```

## configure qos

Level help (`?`):
```text
[no] marking-profile       + Marking profiles map the Pbit, IP precedence, or 
                              DSCP classifications to user priority
 [no] policer-profile       + 
 [no] queue-block-profile   + 
 [no] queue-group-profile   + 
 [no] queue-map-profile     + 
 [no] shaper-profile        + 
 [no] wred-profile          +
```

### marking-profile *(parameterized — inner help harvested under "configure qos marking-profile NAME")*
```text
<marking-profile-*>  : [1..32 chars]


mp4100>config>qos# marking-profile
```

### policer-profile *(parameterized — inner help harvested under "configure qos policer-profile NAME")*
```text
<policer-profile-*>  : [1..32 chars]


mp4100>config>qos# policer-profile
```

### queue-block-profile *(parameterized — inner help harvested under "configure qos queue-block-profile NAME")*
```text
<queue-block-prof*>  : [1..32 chars]


mp4100>config>qos# queue-block-profile
```

### queue-group-profile *(parameterized — inner help harvested under "configure qos queue-group-profile NAME")*
```text
<queue-group-name>   : [1..32 chars]


mp4100>config>qos# queue-group-profile
```

### queue-map-profile *(parameterized — inner help harvested under "configure qos queue-map-profile NAME")*
```text
<queue-mapping-pr*>  : [1..32 chars]


mp4100>config>qos# queue-map-profile
```

### shaper-profile *(parameterized — inner help harvested under "configure qos shaper-profile NAME")*
```text
<shaper-profile-n*>  : [1..32 chars]


mp4100>config>qos# shaper-profile
```

### wred-profile *(parameterized — inner help harvested under "configure qos wred-profile NAME")*
```text
<wred-profile-name>  : [1..32 chars]


mp4100>config>qos# wred-profile
```

## configure qos marking-profile NAME

Level help (`?`):
```text
mark                  - 


mp4100>config>qos>marking-profile(zzz-hrvst)$
```

### mark
```text
<user-priority>      : [n1..n2]


mp4100>config>qos>marking-profile(zzz-hrvst)$ mark
```

## configure qos policer-profile NAME

Level help (`?`):
```text
bandwidth             - 
 [no] color-aware           - Defines whether the policing function assumes 
                              ingress frames are already colored and must be 
                              treated
      compensation          - Extra bytes to be taken into account
 [no] coupling-flag         - Defines the admission options for Yellow Colored 
                              Frames.
      traffic-type          - Defines the policed traffic type
```

### bandwidth
```text
cir
 cbs
 eir
 ebs

mp4100>config>qos>policer-profile(Policer1)# bandwidth
```

### color-aware
```text
<CR>

mp4100>config>qos>policer-profile(Policer1)# color-aware
```

### compensation
```text
<value>              : Defines the layer1 overhead (preamble and IFG) and the 
                        overhead for the added VLAN header in case of [0..63, 
                        default 0]


mp4100>config>qos>policer-profile(Policer1)# compensation
```

### coupling-flag
```text
<CR>

mp4100>config>qos>policer-profile(Policer1)# coupling-flag
```

### traffic-type
```text
<all>                : 
 <broadcast>          : 
 <multicast>          : 
 <unknown-unicast>    : 


mp4100>config>qos>policer-profile(Policer1)# traffic-type
```

## configure qos queue-block-profile NAME

Level help (`?`):
```text
[no] queue                 +
```

### queue *(parameterized — inner help harvested under "configure qos queue-block-profile NAME queue NAME")*
```text
<queue-id>           : [number]


mp4100>config>qos>queue-block-profile(DefaultQueue1)# queue
```

## configure qos queue-block-profile NAME queue NAME

Level help (`?`):
```text
[no] congestion-avoidance  - 
      depth                 - The queue length, max value is 1,048,576
      scheduling            -
```

### congestion-avoidance
```text
<wred>               : 
 <tail-drop>          : 


mp4100>config>qos>queue-block-profile(DefaultQueue1)>queue(0)# congestion-avoidance
```

### depth
```text
<value>              : [number, default 10000]


mp4100>config>qos>queue-block-profile(DefaultQueue1)>queue(0)# depth
```

### scheduling
```text
<strict>             : 
 <wfq>                : 


mp4100>config>qos>queue-block-profile(DefaultQueue1)>queue(0)# scheduling
```

## configure qos queue-group-profile NAME

Level help (`?`):
```text
[no] queue-block           +
```

### queue-block *(parameterized — inner help harvested under "configure qos queue-group-profile NAME queue-block NAME")*
```text
<id>                 :  [level_id/queue_id]


mp4100>config>qos>queue-group-profile(FeDefaultQueueG)# queue-block
```

## configure qos queue-group-profile NAME queue-block NAME

Level help (`?`):
```text
name                  - 
 [no] profile               -
```

### bind
```text
# cli error: Invalid Command
mp4100>config>qos>queue-group-profile(FeDefaultQueueG)>queue-block(1/1)# bind
```

### name
```text
<block-name>         : [1..32 chars]


mp4100>config>qos>queue-group-profile(FeDefaultQueueG)>queue-block(1/1)# name
```

### profile
```text
<queue-block-prof*>  : [1..32 chars]


mp4100>config>qos>queue-group-profile(FeDefaultQueueG)>queue-block(1/1)# profile
```

### shaper
```text
# cli error: Invalid Command
mp4100>config>qos>queue-group-profile(FeDefaultQueueG)>queue-block(1/1)# shaper
```

## configure qos queue-map-profile NAME

Level help (`?`):
```text
map                   -
```

### map
```text
<class-value>        : [n1..n2]


mp4100>config>qos>queue-map-profile(CosProfile1)# map
```

## configure qos shaper-profile NAME

Level help (`?`):
```text
bandwidth             - 
      compensation          - Extra bytes to be taken into account
```

### bandwidth
```text
cir
 cbs

mp4100>config>qos>shaper-profile(GbeShaper)# bandwidth
```

### compensation
```text
<value>              : Defines the layer1 overhead (preamble and IFG) and the 
                        overhead for the added VLAN header in case of [number, 
                        default 0]


mp4100>config>qos>shaper-profile(GbeShaper)# compensation
```

## configure qos wred-profile NAME

Level help (`?`):
```text
[no] color                 -
```

### color
```text
<green>              : 
 <yellow>             : 
 <red>                : 


mp4100>config>qos>wred-profile(WREDProfile0)# color
```

## configure reporting

Level help (`?`):
```text
acknowledge           - 
      active-alarm-rebuild  - 
      alarm-cut-off         - 
      alarm-input           - 
      alarm-output          - 
 [no] alarm-source-attribu* - 
 [no] alarm-source-type-at* - 
 [no] bind-alarm-source-to* - 
 [no] bind-alarm-to-relay   - 
      clear-alarm-log       - 
      log-file-timestamp-t* - Configure log file timestamp type
 [no] mask-minimum-severit* - 
 [no] pm                    - Globally enable PM collection
 [no] pm-collection         - Enable PM collection on entity type

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
```

### acknowledge
```text
<log>                : 
 <brief-log>          : 
 <activity-log>       : 
 <all-logs>           : 


mp4100>config>reporting# acknowledge
```

### active-alarm-rebuild
```text
<CR>

 send-traps

mp4100>config>reporting# active-alarm-rebuild
```

### alarm-cut-off
```text
<port>               : 


mp4100>config>reporting# alarm-cut-off
```

### alarm-input
```text
<port-index>         :  [slot/port[/tributary]]


mp4100>config>reporting# alarm-input
```

### alarm-output
```text
<port>               : 


mp4100>config>reporting# alarm-output
```

### alarm-source-attribute
```text
<system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <domain-clock>       : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <mux-eth-tdm-fe>     : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <shdsl-fe>           : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <bri-fe>             : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <ds3>                : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <serial-fe>          : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <ds1-opt>            : 
 <t3>                 : 
 <e3>                 : 
 <alarm-input-on-s*>  : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# alarm-source-attribute
```

### alarm-source-type-attribute
```text
<system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <domain-clock>       : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <mux-eth-tdm-fe>     : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <shdsl-fe>           : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <bri-fe>             : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <ds1-opt>            : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input>        : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# alarm-source-type-attribute
```

### bind-alarm-source-to-relay
```text
<system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <domain-clock>       : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <ds3>                : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <e3>                 : 
 <t3>                 : 
 <alarm-input>        : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# bind-alarm-source-to-relay
```

### bind-alarm-to-relay
```text
<system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <domain-clock>       : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <serial-fe>          : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input>        : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# bind-alarm-to-relay
```

### clear-alarm-log
```text
<log>                : 
 <brief-log>          : 
 <activity-log>       : 
 <all-logs>           : 


mp4100>config>reporting# clear-alarm-log
```

### log-file-timestamp-type
```text
<utc>                : 
 <local>              : 


mp4100>config>reporting# log-file-timestamp-type
```

### mask-minimum-severity
```text
log
 snmp-trap
 led-relay
 popup
 vty-popup

mp4100>config>reporting# mask-minimum-severity
```

### pm
```text
<CR>

mp4100>config>reporting# pm
```

### pm-collection
```text
<eth>                : Ethernet
 <flow>               : Flows
 <oam-cfm-service>    : OAM CFM services
 <e1>                 : E1 Ports
 <t1>                 : T1 Ports
 <e1-i>               : E1 Internal Ports
 <t1-i>               : T1 Internal Ports
 <sdh-sonet>          : SDH/Sonet Ports
 <path>               : SDH/Sonet Path Level
 <vc-vt>              : SDH/Sonet VC/VT Level


mp4100>config>reporting# pm-collection
```

### show active-alarms
```text
<CR>
 <system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input-on-s*>  : 
 <all>                : 
 <domain-clock>       : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# show active-alarms
```

### show active-alarms-details
```text
<CR>
 <system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input-on-s*>  : 
 <all>                : 
 <domain-clock>       : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# show active-alarms-details
```

### show alarm-information
```text
<system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <domain-clock>       : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <bri-fe>             : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input>        : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# show alarm-information
```

### show alarm-input
```text
<slot>               : 
 <all>                : 


mp4100>config>reporting# show alarm-input
```

### show alarm-list
```text
<CR>
 <system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <domain-clock>       : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <bri-fe>             : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <all>                : 


mp4100>config>reporting# show alarm-list
```

### show alarm-log
```text
<CR>
 <system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input-on-s*>  : 
 <all>                : 
 <domain-clock>       : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# show alarm-log
```

### show alarm-outputs
```text
<slot>               : 
 <all>                : 


mp4100>config>reporting# show alarm-outputs
```

### show brief-alarm-log
```text
<CR>
 <system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input-on-s*>  : 
 <all>                : 
 <domain-clock>       : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# show brief-alarm-log
```

### show brief-log
```text
<CR>
 <system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input-on-s*>  : 
 <all>                : 
 <domain-clock>       : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# show brief-log
```

### show event-information
```text
<system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <recovered-clock>    : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <bri-fe>             : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <domain-clock>       : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# show event-information
```

### show event-list
```text
<CR>
 <system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <domain-clock>       : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input>        : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 
 <all>                : 


mp4100>config>reporting# show event-list
```

### show log
```text
<CR>
 <system>             : 
 <fan>                : 
 <power-supply>       : 
 <clock>              : 
 <station-clock>      : 
 <recovered-clock>    : 
 <card>               : 
 <ethernet>           : 
 <mng-ethernet>       : 
 <mux-eth-tdm>        : 
 <dsl>                : 
 <vdsl>               : 
 <shdsl>              : 
 <adsl>               : 
 <pcs>                : 
 <bri>                : 
 <voice>              : 
 <sdh-sonet>          : 
 <vc-vt>              : 
 <path>               : 
 <ds1>                : 
 <e1>                 : 
 <t1>                 : 
 <j1>                 : 
 <ds1-opt>            : 
 <ds3>                : 
 <e3>                 : 
 <t3>                 : 
 <ds0-bundle>         : 
 <ds0-g703>           : 
 <vcg>                : 
 <serial>             : 
 <serial-bundle>      : 
 <bridge>             : 
 <logical-mac>        : 
 <flow>               : 
 <gfp>                : 
 <hdlc>               : 
 <lag>                : 
 <oam-efm>            : 
 <oam-cfm-mep>        : 
 <oam-cfm-service>    : 
 <oam-cfm-destne>     : 
 <ppp>                : 
 <mlppp>              : 
 <aps>                : 
 <eps>                : 
 <erp>                : 
 <router-interface>   : 
 <pw>                 : 
 <cmd-channel>        : 
 <cmd-in>             : 
 <cmd-out>            : 
 <e1-i>               : 
 <t1-i>               : 
 <j1-i>               : 
 <alarm-input-on-s*>  : 
 <all>                : 
 <domain-clock>       : 
 <recovered-clock-*>  : 
 <domain-clock-sou*>  : 
 <master-clock>       : 
 <smart-sfp>          : 
 <oam-cfm-r-mep>      : 
 <erp-port>           : 
 <ospf>               : 
 <ospf-neighbor>      : 
 <ospf-interface>     : 


mp4100>config>reporting# show log
```

## configure router NAME

Level help (`?`):
```text
[no] arp-timeout           - Enable/disable address aging function
 [no] interface             + Create/delete router interface
 [no] static-route          - Create/delete static route entities

 show arp-table             - Displays the router ARP table
 show routing-table         - Displays the routing table
```

### arp-timeout
```text
<seconds>            : Aging time for the ARP entries [300..1000000]


mp4100>config>router(1)# arp-timeout
```

### interface *(parameterized — inner help harvested under "configure router NAME interface NAME")*
```text
<number>             : Unique number which represents the router interface 
                        [1..132]


mp4100>config>router(1)# interface
```

### show routing-table
```text
<CR>
 address
 protocol

mp4100>config>router(1)# show routing-table
```

### static-route
```text
<address-mask>       : IP address and IP mask of static route [0.0.0.0/0 .. 
                        255.255.255.255/32]


mp4100>config>router(1)# static-route
```

## configure router NAME interface NAME

Level help (`?`):
```text
address               - Router interface IP and mask
      bind                  - Binds router interface to physical/logical port
 [no] ip-forwarding         - Enable/disable IP forwarding
      mtu                   - Configure MTU
 [no] name                  - Router interface name
 [no] rip                   - Enable / Disable RIP routing protocol
 [no] shutdown              - Administrtavly enable/disable the router interface
```

### address
```text
<address-mask>       : Router interface IP and mask [0.0.0.0/32]


mp4100>config>router(1)>interface(1)# address
```

### bind
```text
<ethernet>           : Ethernet port
 <svi>                : SVI port
 <e1>                 : E1 port
 <t1>                 : T1
 <sdh-sonet>          : SDH/SONET port
 <e1-i>               : E1 internal port
 <t1-i>               : T1 internal port
 <logical-mac>        : Logical MAC port
 <ds1-opt>            : DS1 Opt port


mp4100>config>router(1)>interface(1)# bind
```

### ip-forwarding
```text
<CR>

mp4100>config>router(1)>interface(1)# ip-forwarding
```

### mtu
```text
<bytes>              : MTU in bytes [200,1280..1500]


mp4100>config>router(1)>interface(1)# mtu
```

### name
```text
<string>             : Name of the router interface [string]


mp4100>config>router(1)>interface(1)# name
```

### rip
```text
<v2>                 : 


mp4100>config>router(1)>interface(1)# rip
```

### shutdown
```text
<CR>

mp4100>config>router(1)>interface(1)# shutdown
```

## configure slot NAME

Level help (`?`):
```text
[no] card-type             - Configure card type
      reset                 - Reset card

 show card-type             - Display card type and version
 show power-inline-status   - Display PoE Status
```

### card-type
```text
<power-supply>       : Power supply
 <cl>                 : Common logic
 <e1-t1>              : Main link (E1/T1)
 <e3-t3>              : Main link (E3/T3)
 <high-speed>         : High speed
 <isdn>               : ISDN
 <low-speed>          : Low speed
 <voice>              : Voice
 <versatile>          : Versatile
 <optimux>            : Optimux
 <dsl>                : DSL (ASMi)
 <pw>                 : PW
 <alarm-relay>        : Alarm relay
 <eth>                : Ethernet
 <virtual-engine>     : VE
 <multi-service>      : MS


mp4100>config>slot(ps-a)# card-type
```

### ms-module *(not entered — parameterized context)*
```text
# cli error: Invalid Command
mp4100>config>slot(ps-a)# ms-module
```

### reset
```text
<CR>

mp4100>config>slot(ps-a)# reset
```

### show card-type
```text
<CR>

mp4100>config>slot(ps-a)# show card-type
```

### show power-inline-status
```text
<CR>

mp4100>config>slot(ps-a)# show power-inline-status
```

## configure system

Level help (`?`):
```text
clear-cpu-utilizatio* - Clears the CPU utilization
      clock                 + Clock configuration
 [no] contact               - Contact name
      date-and-time         + Date and time parameters
      dot1x                 + Enable 802.1X announcements
 [no] location              - Device location
      macsec                + MACsec level
 [no] name                  - Device name
      syslog                + Configure Syslog

 show cpu-utilization       - Shows the CPU utilization
 show date-and-time         - Displays current system data and time
 show device-information    - Display device information
 show license               - Displays the profile supported by the license
 show memory                - Display memory usage
```

### clear-cpu-utilization
```text
<CR>

mp4100>config>system# clear-cpu-utilization
```

### contact
```text
<contact-person>     : Contact name [0..255 chars, default contact person]


mp4100>config>system# contact
```

### location
```text
<location-of-device> : Device location [0..255 chars, default the location of 
                        this device]


mp4100>config>system# location
```

### name
```text
<name-of-device>     : Device name [0..255 chars]


mp4100>config>system# name
```

### show cpu-utilization
```text
<CR>

mp4100>config>system# show cpu-utilization
```

### show date-and-time
```text
<CR>

mp4100>config>system# show date-and-time
```

### show device-information
```text
<CR>

mp4100>config>system# show device-information
```

### show license
```text
<CR>

mp4100>config>system# show license
```

### show memory
```text
<CR>

mp4100>config>system# show memory
```

### syslog *(parameterized — inner help harvested under "configure system syslog NAME")*
```text
<device>             : Device
 <server>             : Server


mp4100>config>system# syslog
```

## configure system clock

Level help (`?`):
```text
[no] domain                + Clock domain number
 [no] recovered             + Create/delete recovered clock
      station               + Enable/disable station clock
```

### domain *(parameterized — inner help harvested under "configure system clock domain NAME")*
```text
<id>                 : Domain Number [number] [1..1]


mp4100>config>system>clock# domain
```

### recovered *(parameterized — inner help harvested under "configure system clock recovered NAME")*
```text
<id>                 : Recovered clock identifier number [1..99]


mp4100>config>system>clock# recovered
```

### station *(parameterized — inner help harvested under "configure system clock station NAME")*
```text
<id>                 : Station clock identifier number [slot/port]


mp4100>config>system>clock# station
```

## configure system clock domain NAME

Level help (`?`):
```text
clear                 - Clear the Forced or Manual selection
      force                 - Forced selection of any configured Clock Source
      manual                - Manual selection of any configured Clock Source
      mode                  - Mode of Clock Selection
 [no] quality               - Clock Quality Level (QL)
 [no] source                + Clock Source parameters
      sync-network-type     - The synchronous digital hierarchy type

 show status                - Display status parameters
```

### clear
```text
<CR>

mp4100>config>system>clock>domain(1)# clear
```

### force
```text
<source-id>          : Clock Source Id [number]


mp4100>config>system>clock>domain(1)# force
```

### manual
```text
<source-id>          : Clock Source Id [number]


mp4100>config>system>clock>domain(1)# manual
```

### mode
```text
<auto>               : Performs Automatic Clock Selection.
 <free-run>           : No Clock Selection


mp4100>config>system>clock>domain(1)# mode
```

### quality
```text
min-level-station
 min-level-system

mp4100>config>system>clock>domain(1)# quality
```

### show status
```text
<CR>

mp4100>config>system>clock>domain(1)# show status
```

### source *(not entered — parameterized context)*
```text
<src-id>             : Unique Clock Source Id [number] [1..10]


mp4100>config>system>clock>domain(1)# source
```

### sync-network-type
```text
<1>                  : Type 1 = Europe
 <2>                  : Type 2 = North America


mp4100>config>system>clock>domain(1)# sync-network-type
```

## configure system clock recovered NAME

Level help (`?`):
```text
network-type          - Network type of the recovered clock
      pw                    - Associate PW number to recovered clock
 [no] shutdown              - Enable/disable recovered clock
```

### network-type
```text
<type-a>             : Type-A
 <type-b>             : Type-B


mp4100>config>system>clock>recovered(1)# network-type
```

### pw
```text
<pw-number>          : PW number [number]


mp4100>config>system>clock>recovered(1)# pw
```

### show status
```text
# cli error: Invalid Command
mp4100>config>system>clock>recovered(1)# show status
```

### shutdown
```text
<CR>

mp4100>config>system>clock>recovered(1)# shutdown
```

## configure system clock station NAME

Level help (`?`):
```text
impedance             - Set station clock impedance
      interface-type        - Assign station clock interface type
      line-code             - Assign station clock line code
      line-type             - Set interface line-type
 [no] name                  - Assign a name to station clock interface
      rx-sensitivity        - Station clock received sensitivity
 [no] shutdown              - Administratively enable/disable station clock
      ssm-channel           - Define E1 G.732-CRC bits to carry SSM information
      tx-clock-source       - Assign station transmitted clock source 
 [no] tx-ssm                - Enable SSM transmission 

 show status                - Display station clock status
```

### impedance
```text
<balanced>           : 
 <unbalanced>         : 


mp4100>config>system>clock>station(cl-a/1)# impedance
```

### interface-type
```text
<e1>                 : E1
 <t1>                 : T1
 <2mhz>               : 2 MHz square-wave


mp4100>config>system>clock>station(cl-a/1)# interface-type
```

### line-code
```text
<b8zs>               : B8ZS
 <ami>                : AMI
 <hdb3>               : HDB3


mp4100>config>system>clock>station(cl-a/1)# line-code
```

### line-type
```text
<unframed>           : Sets the E1 line type to Unframed
 <g732n>              : Selects G.732.N, CRC disabled
 <g732n-crc>          : Selects G.732.N, CRC enabled


mp4100>config>system>clock>station(cl-a/1)# line-type
```

### name
```text
<string>             : [1..32 chars]


mp4100>config>system>clock>station(cl-a/1)# name
```

### rx-sensitivity
```text
<short-haul>         : Short haul
 <long-haul>          : Long haul


mp4100>config>system>clock>station(cl-a/1)# rx-sensitivity
```

### show status
```text
<CR>

mp4100>config>system>clock>station(cl-a/1)# show status
```

### shutdown
```text
<CR>

mp4100>config>system>clock>station(cl-a/1)# shutdown
```

### tx-clock-source
```text
<system>             : System clock
 <station-rclk-plu*>  : Station receive clock + jitter attenuator


mp4100>config>system>clock>station(cl-a/1)# tx-clock-source
```

## configure system date-and-time

Level help (`?`):
```text
date-format           - System date format
      date                  - System date in European format.
      sntp                  + Configure SNTP client
      time                  - System time
      zone                  - Time zone and offset
```

### date
```text
<date>               : System date in European format [dd-mm-yyyy]


mp4100>config>system>date-and-time# date
```

### date-format
```text
<yyyy-mm-dd>         : ISO format
 <dd-mm-yyyy>         : European format
 <mm-dd-yyyy>         : USA format
 <yyyy-dd-mm>         : Japanese date format


mp4100>config>system>date-and-time# date-format
```

### time
```text
<time>               : System time [hh:mm[:ss]]


mp4100>config>system>date-and-time# time
```

### zone
```text
<utc>                : Universal Time Coordinated
 <gmt>                : GMT
 <user-defined>       : User-defined time zone


mp4100>config>system>date-and-time# zone
```

## configure system date-and-time sntp

Level help (`?`):
```text
[no] broadcast             - Enable SNTP broadcast 
      poll-interval         - Period of polling SNTP Server
 [no] server                + Specify SNTP Server

 show status                - SNTP status
```

### broadcast
```text
<CR>

mp4100>config>system>date-and-time>sntp# broadcast
```

### poll-interval
```text
<minutes>            : Polling interval [1..1440, default 15]


mp4100>config>system>date-and-time>sntp# poll-interval
```

### server *(not entered — parameterized context)*
```text
<server-id>          : SNTP server address [1..10]


mp4100>config>system>date-and-time>sntp# server
```

### show status
```text
<CR>

mp4100>config>system>date-and-time>sntp# show status
```

## configure system dot1x

Level help (`?`):
```text
[no] access-control        - Enable or disable 802.1X

 show version-information   - Show EAPoL and MKA protocolversion
```

### access-control
```text
<CR>

mp4100>config>system>dot1x# access-control
```

### show version-information
```text
<CR>

mp4100>config>system>dot1x# show version-information
```

## configure system macsec

Level help (`?`):
```text
gcm-aes-128           - gcm-aes-128 protection type
      gcm-aes-256           - gcm-aes-256 protection type
```

### gcm-aes-128
```text
<integrity-only>     : 
 <confidentiality>    : 


mp4100>config>system>macsec# gcm-aes-128
```

### gcm-aes-256
```text
<integrity-only>     : 
 <confidentiality>    : 


mp4100>config>system>macsec# gcm-aes-256
```

## configure system syslog NAME

Level help (`?`):
```text
clear-statistics      - Clear Syslog statistics
      facility              - Syslog facility
      port                  - Syslog UDP port
      severity-level        - Syslog severity level 
 [no] shutdown              - Enable Syslog 

 show statistics            - Display Syslog statistics
```

### address
```text
# cli error: Invalid Command
mp4100>config>system>syslog(device)# address
```

### clear-statistics
```text
<CR>

mp4100>config>system>syslog(device)# clear-statistics
```

### facility
```text
<local1>             : Local 1
 <local2>             : Local 2
 <local3>             : Local 3
 <local4>             : Local 4
 <local5>             : Local 5
 <local6>             : Local 6
 <local7>             : Local 7


mp4100>config>system>syslog(device)# facility
```

### port
```text
<udp-port-number>    : UDP port  [1..65535]


mp4100>config>system>syslog(device)# port
```

### severity-level
```text
<emergency>          : Emergency messages
 <alert>              : Critical alarms
 <critical>           : Major alarms
 <error>              : Minor alarms
 <warning>            : Events
 <notice>             : Cleared alarms, accounting messages
 <informational>      : Informational messages
 <debug>              : Debug messages


mp4100>config>system>syslog(device)# severity-level
```

### show statistics
```text
<CR>

mp4100>config>system>syslog(device)# show statistics
```

### shutdown
```text
<CR>

mp4100>config>system>syslog(device)# shutdown
```

## configure terminal

Level help (`?`):
```text
baud-rate             - Baud rate
      length                - Terminal length (rows)
      timeout               - Terminal timeout
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
 <auto>               : Auto baud rate


mp4100>config>terminal# baud-rate
```

### length
```text
<number-of-rows>     : Number of rows  [number, default 20]


mp4100>config>terminal# length
```

### timeout
```text
<forever>            : No timeout
 <limited>            : Enable timeout


mp4100>config>terminal# timeout
```

## configure test

Level help (`?`):
```text
rfc2544               +
```

## configure test rfc2544

Level help (`?`):
```text
[no] profile-name          + 
 [no] test                  +
```

### profile-name *(parameterized — inner help harvested under "configure test rfc2544 profile-name NAME")*
```text
<name>               : [string]


mp4100>config>test>rfc2544# profile-name
```

### test *(parameterized — inner help harvested under "configure test rfc2544 test NAME")*
```text
<id>                 : [number]


mp4100>config>test>rfc2544# test
```

## configure test rfc2544 profile-name NAME

Level help (`?`):
```text
frame-size            - 
      pattern               - 


mp4100>config>test>rfc2544>profile-nam(zzz-hrvst)$
```

### frame-size
```text
<64>                 : 
 <128>                : 
 <256>                : 
 <512>                : 
 <1024>               : 
 <1280>               : 
 <1518>               : 
 <1700>               : 
 <1900>               : 
 <2000>               : 
 custom

mp4100>config>test>rfc2544>profile-nam(zzz-hrvst)$ frame-size
```

### pattern
```text
<all-ones>           : 
 <all-zeroes-witho*>  : 
 <alternate>          : 
 <prbs-without-crc>   : 


mp4100>config>test>rfc2544>profile-nam(zzz-hrvst)$ pattern
```

## configure test rfc2544 test NAME

Level help (`?`):
```text
[no] activate              - 
 [no] associated-flow       - Associate flow with test
      clear-reports         - 
      max-rate              - 
 [no] max-test-duration     - Maximum duration of test
      test-profile          - 
      type                  - 

 show report
 show status
 show summary

mp4100>config>test>rfc2544>test(1)$
```

### activate
```text
<CR>
 <date>               : 
 <recurring>          : 


mp4100>config>test>rfc2544>test(1)$ activate
```

### associated-flow
```text
<name>               : [string]


mp4100>config>test>rfc2544>test(1)$ associated-flow
```

### clear-reports
```text
<CR>

mp4100>config>test>rfc2544>test(1)$ clear-reports
```

### max-rate
```text
<bps>                : [1..1000000000]


mp4100>config>test>rfc2544>test(1)$ max-rate
```

### max-test-duration
```text
<minutes>            : [2..2880]


mp4100>config>test>rfc2544>test(1)$ max-test-duration
```

### show report
```text
<all>                : 
 <iteration>          : 


mp4100>config>test>rfc2544>test(1)$ show report
```

### show status
```text
<CR>

mp4100>config>test>rfc2544>test(1)$ show status
```

### show summary
```text
<CR>

mp4100>config>test>rfc2544>test(1)$ show summary
```

### test-profile
```text
<name>               : [string]


mp4100>config>test>rfc2544>test(1)$ test-profile
```

### type
```text
<frame-loss>         : 


mp4100>config>test>rfc2544>test(1)$ type
```

## file

Level help (`?`):
```text
copy                  - 
      delete                - Delete file
      dir                   - Display file directory

 show copy                  - Display Copy progress
 show sw-pack               - Display SW packs
```

### copy
```text
<source-file-url>    : <file-url> = <url-prefix> <file>
<url-prefix> = 
      tftp://<ipv4-address>/
      tftp://[<ipv6-address>]/
      sftp://<username>:<password>@<ipv4-address>:<port>/
      sftp://<username>:<password>@[<ipv6-address>]:<port>/
      xmodem:
<file> = 
      startup-config
      rollback-config
      running-config
      user-default-config
      factory-default-config
      log
      candidate-config
      trace-log
      sw-pack-1
      sw-pack-2
      sw-pack-3
      sw-pack-4
      license-1
      license-2
      license-3
      license-4
      hidden_config
      mac-table
      ltm_1
      ltm_2
      ltm_3
      ltm_4
      ltm_5
      ltm_6
      ltm_7
      ltm_8
      ltm_9
      ltm_10
      ltm_11
      ltm_12
      ltmedr_1
      ltmedr_2
      ltmedr_3
      ltmedr_4
      ltmedr_5
      ltmedr_6
      ltmedr_7
      ltmedr_8
      ltmedr_9
      ltmedr_10
      ltmedr_11
      ltmedr_12
The maximum allowed length/range is:
      <username> [1..100 chars]
      <password> [1..100 chars]
      <file>     [1..96 chars]
      <port>     [1..65535]



mp4100>file# copy
```

### delete
```text
<sw-pack-1>          : 
 <sw-pack-2>          : 
 <sw-pack-3>          : 
 <sw-pack-4>          : 
 <startup-config>     : 
 <rollback-config>    : 
 <user-default-con*>  : 
 <candidate-config>   : 
 <license-1>          : 
 <license-2>          : 
 <license-3>          : 
 <license-4>          : 
 <alarm-event-log>    : 
 <monitoring-log>     : 


mp4100>file# delete
```

### dir
```text
<CR>

mp4100>file# dir
```

### show copy
```text
<CR>
 <summary>            : 


mp4100>file# show copy
```

### show sw-pack
```text
<CR>

mp4100>file# show sw-pack
```
