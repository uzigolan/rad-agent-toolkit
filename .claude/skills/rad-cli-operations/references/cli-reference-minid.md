# minid CLI reference (harvested `?` help)

Captured live from minid-1 (MiNID (Miniature NID / sleeve device) SW 2.6, prompt MiNID#; verified live - shared context CLI, direct-write save; fragile/unique SSH (patient profile); CLI reference + manual harvested) on 2026-07-15 by scripts/harvest_cli.py
(re-run `harvest` after firmware upgrades — it diffs and updates in place).
Every section is a CLI context: first the level `?` listing (commands +
descriptions), then per-command argument help (`<command> ?`). Sections
ending in NAME are parameterized contexts harvested through one instance
(an existing one, or a temp object created and rolled back) — NAME stands
for any instance. Entries marked *(not entered)* could not be harvested
safely — their inner structure is in command-tree-minid.md; use
cli_help with a real index for inner argument syntax.

## <root>

Level help (`?`):
```text
admin
configure
inventory
factory
logon
file

-- Global Commands --
exit
info
logout
help
tree
ping
save
```

## admin

Level help (`?`):
```text
factory-default
user-default
reboot
software
```

### factory-default
```text
(no help output captured)
```

### reboot
```text
(no help output captured)
```

### user-default
```text
(no help output captured)
```

## admin software

Level help (`?`):
```text
install
```

### install
```text
(no help output captured)
```

## configure

Level help (`?`):
```text
access-control
management
router
oam
qos
flows
port
reporting
service
system
test
packet-capture
```

## configure access-control

Level help (`?`):
```text
[no] access-list
```

### access-list *(not entered — parameterized context)*
```text
- access-list <acl-name>

MiNID>config>access-control# access-list
```

## configure flows

Level help (`?`):
```text
classification
dscp-marking
fallback-action
in-service-mac
in-service-l3-l4
inner-vlan-marking
port-mode-action
[no] l2cp-mac
l2cp-protocol
[no] l2cp-profile
[no] fallback-l2cp
[no] tpid-outer-vlan
[no] tpid-inner-vlan
[no] flow
rename-flow
lbm-reflector
clear-statistics
[no] fallback-policer
[no] fallback-pm-collection
[no] port-mode-policer
[no] port-mode-pm-collection
```

### classification
```text
(no help output captured)
```

### clear-statistics
```text
(no help output captured)
```

### dscp-marking
```text
(no help output captured)
```

### fallback-action
```text
(no help output captured)
```

### fallback-l2cp
```text
(no help output captured)
```

### fallback-pm-collection
```text
(no help output captured)
```

### fallback-policer
```text
(no help output captured)
```

### flow *(not entered — parameterized context)*
```text
- flow <flow-name>

MiNID>config>flows# flow

auto-create probe 'flow zzz-hrvst' refused.
device response: flow zzz-hrvst
#CLI Error, Unknown Command
MiNID>config>flows#
```

### in-service-loops-l3-l4 *(not entered — parameterized context)*
```text
(no help output captured)
```

### in-service-loops-mac *(not entered — parameterized context)*
```text
(no help output captured)
```

### in-service-mac
```text
(no help output captured)
```

### inner-vlan-marking
```text
- inner-vlan-marking c-pbit <p-bit> s-pbit <p-bit>

MiNID>config>flows# inner-vlan-marking
```

### ip-agnostic-loop
```text
- lbm-reflector {sfp|msa}

MiNID>config>flows# lbm-reflector ip-agnostic-loop
```

### l2cp-mac
```text
- inner-vlan-marking c-pbit <p-bit> s-pbit <p-bit>

MiNID>config>flows# inner-vlan-marking port-mode-action l2cp-mac
```

### l2cp-profile *(parameterized — inner help harvested under "configure flows l2cp-profile NAME")*
```text
- l2cp-profile <profile-name>

MiNID>config>flows# l2cp-profile
```

### l2cp-protocol
```text
- inner-vlan-marking c-pbit <p-bit> s-pbit <p-bit>

MiNID>config>flows# inner-vlan-marking port-mode-action l2cp-mac l2cp-protocol
```

### lbm-reflector *(not entered — parameterized context)*
```text
- lbm-reflector {sfp|msa}

MiNID>config>flows# lbm-reflector
```

### port-l2cp
```text
(no help output captured)
```

### port-mode-action
```text
- inner-vlan-marking c-pbit <p-bit> s-pbit <p-bit>

MiNID>config>flows# inner-vlan-marking port-mode-action
```

### port-mode-pm-collection
```text
(no help output captured)
```

### port-mode-policer
```text
(no help output captured)
```

### rename-flow
```text
- rename-flow <current-flow-name> <new-flow-name>

MiNID>config>flows# rename-flow
```

### show port-mode-statistics
```text
(no help output captured)
```

### show summary
```text
(no help output captured)
```

### show unclassified-statistics
```text
(no help output captured)
```

### tpid-inner-vlan
```text
(no help output captured)
```

### tpid-outer-vlan
```text
(no help output captured)
```

### tpid-pushed-replaced-vlan
```text
(no help output captured)
```

## configure flows in-service-l3-l4

Level help (`?`):
```text
ip-loop
udp-loop
udp-echo
```

## configure flows in-service-l3-l4 ip-loop

Level help (`?`):
```text
ip-address
```

### ip-address
```text
(no help output captured)
```

## configure flows in-service-l3-l4 udp-echo

Level help (`?`):
```text
ip-address
udp-port
```

### ip-address
```text
(no help output captured)
```

### udp-port
```text
(no help output captured)
```

## configure flows in-service-l3-l4 udp-loop

Level help (`?`):
```text
ip-address
udp-port
```

### ip-address
```text
(no help output captured)
```

### udp-port
```text
(no help output captured)
```

## configure flows l2cp-profile NAME

Level help (`?`):
```text
mac
protocol
```

### mac
```text
(no help output captured)
```

### protocol
```text
(no help output captured)
```

## configure management

Level help (`?`):
```text
timeout
user
[no] manager
[no] zero-touch
access
snmp
tacacsplus
```

### host *(not entered — parameterized context)*
```text
(no help output captured)
```

### manager
```text
(no help output captured)
```

### show access
```text
(no help output captured)
```

### show users
```text
(no help output captured)
```

### snmp
```text
- snmp {community} {rw|ronly|trap} <name>

MiNID>config>mngmnt# snmp
```

### timeout
```text
(no help output captured)
```

### user
```text
(no help output captured)
```

### zero-touch
```text
(no help output captured)
```

## configure management access

Level help (`?`):
```text
auth-policy
[no] wait-to-restore-auth-method
[no] sfp
[no] msa
[no] snmp-read-only
static-ip-access
loaned-ip-access
[no] access-group
```

### access-group
```text
- access-group <acl-name>

MiNID>config>mngmnt>access# access-group
```

### auth-policy
```text
(no help output captured)
```

### msa
```text
(no help output captured)
```

### sfp
```text
(no help output captured)
```

### snmp-read-only
```text
(no help output captured)
```

### wait-to-restore-auth-method
```text
(no help output captured)
```

## configure management access loaned-ip-access

Level help (`?`):
```text
[no] snmp
[no] tftp/sftp
[no] ssh
[no] telnet
[no] http
[no] rpcap
```

### http
```text
(no help output captured)
```

### rpcap
```text
(no help output captured)
```

### snmp
```text
(no help output captured)
```

### ssh
```text
(no help output captured)
```

### telnet
```text
(no help output captured)
```

### tftp/sftp
```text
(no help output captured)
```

## configure management access static-ip-access

Level help (`?`):
```text
[no] snmp
[no] tftp/sftp
[no] ssh
[no] telnet
[no] http
```

### http
```text
(no help output captured)
```

### snmp
```text
(no help output captured)
```

### ssh
```text
(no help output captured)
```

### telnet
```text
(no help output captured)
```

### tftp/sftp
```text
(no help output captured)
```

## configure management tacacsplus

Level help (`?`):
```text
[no] privilege-level
[no] group
[no] server
[no] wait-to-restore-server
```

### group *(parameterized — inner help harvested under "configure management tacacsplus group NAME")*
```text
- group <group-name>

MiNID>config>mngmnt>tacacsplus# group
```

### privilege-level
```text
(no help output captured)
```

### server *(not entered — parameterized context)*
```text
- server <ip>

MiNID>config>mngmnt>tacacsplus# server

auto-create probe 'server zzz-hrvst' refused.
device response: server zzz-hrvst
#CLI Error, Unneeded Parameter
MiNID>config>mngmnt>tacacsplus#
```

### wait-to-restore-server
```text
- wait-to-restore-server <seconds>

MiNID>config>mngmnt>tacacsplus# wait-to-restore-server
```

## configure management tacacsplus group NAME

Level help (`?`):
```text
[no] accounting
```

### accounting
```text
(no help output captured)
```

## configure oam

Level help (`?`):
```text
cfm
efm
twamp
```

## configure oam cfm

Level help (`?`):
```text
alarm-type
availability
[no] measurement-bin-profile
[no] maintenance-domain
```

### alarm-type
```text
(no help output captured)
```

### availability
```text
(no help output captured)
```

### maintenance-domain *(not entered — parameterized context)*
```text
- maintenance-domain <md-index>

MiNID>config>oam>cfm# maintenance-domain

auto-create probe 'maintenance-domain zzz-hrvst' refused.
device response: maintenance-domain zzz-hrvst
#CLI Error, MD Index Exceeds Range [1-8]
MiNID>config>oam>cfm#
```

### measurement-bin-profile *(parameterized — inner help harvested under "configure oam cfm measurement-bin-profile NAME")*
```text
- measurement-bin-profile <name>

MiNID>config>oam>cfm# measurement-bin-profile
```

### show mips
```text
(no help output captured)
```

### show summary
```text
(no help output captured)
```

## configure oam cfm measurement-bin-profile NAME

Level help (`?`):
```text
[no] thresholds
```

### thresholds
```text
(no help output captured)
```

## configure oam efm

Level help (`?`):
```text
mode
bind
[no] shutdown
clear-statistics
```

### bind
```text
(no help output captured)
```

### clear-statistics
```text
(no help output captured)
```

### loopback
```text
(no help output captured)
```

### mode
```text
(no help output captured)
```

### show statistics
```text
(no help output captured)
```

### show status
```text
(no help output captured)
```

### shutdown
```text
(no help output captured)
```

## configure oam twamp

Level help (`?`):
```text
[no] profile
[no] responder
[no] controller
```

### controller *(not entered — parameterized context)*
```text
- controller <controller-name> [<number>]

MiNID>config>oam>twamp# controller

auto-create probe 'controller zzz-hrvst' refused.
device response: controller zzz-hrvst
#CLI Error, Invalid Parameter
MiNID>config>oam>twamp#
```

### profile *(parameterized — inner help harvested under "configure oam twamp profile NAME")*
```text
- profile <profile-name> [<number>]

MiNID>config>oam>twamp# profile
```

### responder *(not entered — parameterized context)*
```text
- responder <responder-name>

MiNID>config>oam>twamp# responder

auto-create probe 'responder zzz-hrvst' refused.
device response: responder zzz-hrvst
#CLI Error, Unneeded Parameter
MiNID>config>oam>twamp#
```

## configure oam twamp profile NAME

Level help (`?`):
```text
payload-length
transmit-rate
loss-timeout
loss-ratio-threshold
delay-variation-threshold
delay-threshold
delay-variation-event-type
```

### delay-threshold
```text
(no help output captured)
```

### delay-variation-event-type
```text
(no help output captured)
```

### delay-variation-threshold
```text
(no help output captured)
```

### loss-ratio-threshold
```text
(no help output captured)
```

### loss-timeout
```text
(no help output captured)
```

### payload-length
```text
(no help output captured)
```

### transmit-rate
```text
(no help output captured)
```

## configure packet-capture

Level help (`?`):
```text
capture-dscp
local-ip-address
rpcap-tcp-port
[no] inactive-timeout
timestamp-source
[no] capture
```

### capture
```text
(no help output captured)
```

### capture-dscp
```text
(no help output captured)
```

### inactive-timeout
```text
(no help output captured)
```

### local-ip-address
```text
(no help output captured)
```

### rpcap-tcp-port
```text
(no help output captured)
```

### show status
```text
(no help output captured)
```

### timestamp-source
```text
(no help output captured)
```

## configure port

Level help (`?`):
```text
ethernet
```

### ethernet *(not entered — parameterized context)*
```text
- ethernet {sfp|msa}

MiNID>config>port# ethernet
```

## configure qos

Level help (`?`):
```text
[no] policer-profile
[no] envelope-profile
[no] cos-map-profile
```

### cos-map-profile *(not entered — parameterized context)*
```text
- cos-map-profile <profile-name> classification {p-bit|ip-dscp}

MiNID>config>qos# cos-map-profile

auto-create probe 'cos-map-profile zzz-hrvst' refused.
device response: cos-map-profile zzz-hrvst
#CLI Error, Profile Name Too Long, Max Name Length Is 10 Chars
MiNID>config>qos#
```

### envelope-profile *(not entered — parameterized context)*
```text
- envelope-profile <profile-name>

MiNID>config>qos# envelope-profile

auto-create probe 'envelope-profile zzz-hrvst' refused.
device response: envelope-profile zzz-hrvst
#CLI Error, Profile Name Too Long, Max Name Length Is 10 Chars
MiNID>config>qos#
```

### policer-profile *(parameterized — inner help harvested under "configure qos policer-profile NAME")*
```text
- policer-profile <profile-name>

MiNID>config>qos# policer-profile
```

## configure qos policer-profile NAME

Level help (`?`):
```text
bandwidth
[no] color_aware
compensation
[no] coupling-flag
```

### bandwidth
```text
(no help output captured)
```

### color_aware
```text
(no help output captured)
```

### compensation
```text
(no help output captured)
```

### coupling-flag
```text
(no help output captured)
```

## configure reporting

Level help (`?`):
```text
[no] pm
clear-log
file-interval-duration
interval-duration
```

### clear-log
```text
(no help output captured)
```

### file-interval-duration
```text
(no help output captured)
```

### interval-duration
```text
(no help output captured)
```

### pm
```text
(no help output captured)
```

### show log
```text
(no help output captured)
```

## configure router

Level help (`?`):
```text
[no] interface
[no] static-route
management-cfg
```

### interface *(not entered — parameterized context)*
```text
- interface <number>

MiNID>config>router# interface

auto-create probe 'interface zzz-hrvst' refused.
device response: interface zzz-hrvst
#CLI Error, Invalid Parameter
MiNID>config>router#
```

### management-cfg
```text
- static-route <ip-address/mask> address <next-hop-ip-address>

MiNID>config>router# static-route management-cfg
```

### static-route
```text
- static-route <ip-address/mask> address <next-hop-ip-address>

MiNID>config>router# static-route
```

## configure service

Level help (`?`):
```text
(no help output captured)
```

### show summary
```text
(no help output captured)
```

## configure system

Level help (`?`):
```text
[no] device-name
[no] location
[no] contact
date-and-time
clock
fault-propagation
syslog
```

### contact
```text
(no help output captured)
```

### device-name
```text
(no help output captured)
```

### location
```text
(no help output captured)
```

### show status
```text
(no help output captured)
```

### syslog *(not entered — parameterized context)*
```text
- syslog {device|server}  <server number>

MiNID>config>system# syslog
```

## configure system clock

Level help (`?`):
```text
sync-e-src
```

### sync-e-src
```text
(no help output captured)
```

## configure system date-and-time

Level help (`?`):
```text
date-format
date
ntp
[no] summer-time
time
zone
```

### date
```text
(no help output captured)
```

### date-format
```text
(no help output captured)
```

### show summer-time
```text
- time time [hh:mm[:ss]]

MiNID>config>system>date-time# time zone show summer-time
```

### time
```text
- time time [hh:mm[:ss]]

MiNID>config>system>date-time# time
```

### zone
```text
- time time [hh:mm[:ss]]

MiNID>config>system>date-time# time zone
```

## configure system date-and-time ntp

Level help (`?`):
```text
poll-interval
[no] server
```

### poll-interval
```text
(no help output captured)
```

### server *(not entered — parameterized context)*
```text
- server <server-id>

MiNID>config>system>date-time>ntp# server

auto-create probe 'server zzz-hrvst' refused.
device response: server zzz-hrvst
#CLI Error, Invalid Parameter
MiNID>config>system>date-time>ntp#
```

### show status
```text
(no help output captured)
```

## configure system date-and-time summer-time

Level help (`?`):
```text
recurring
date
```

### date
```text
(no help output captured)
```

### recurring
```text
(no help output captured)
```

## configure system fault-propagation

Level help (`?`):
```text
[no] ais
[no] phy-disable
[no] los-propagation
[no] tx-disable
[no] tx-fault
[no] cfm-fault
[no] if-status-tlv
```

### ais
```text
(no help output captured)
```

### cfm-fault
```text
(no help output captured)
```

### if-status-tlv
```text
(no help output captured)
```

### los-propagation
```text
(no help output captured)
```

### phy-disable
```text
(no help output captured)
```

### tx-disable
```text
(no help output captured)
```

### tx-fault
```text
(no help output captured)
```

## configure test

Level help (`?`):
```text
l3sat
```

## configure test l3sat

Level help (`?`):
```text
[no] peer-profile
[no] session-profile
[no] generator
```

### generator *(not entered — parameterized context)*
```text
- generator <name>

MiNID>config>test>l3sat# generator

auto-create probe 'generator zzz-hrvst' refused.
device response: generator zzz-hrvst
#CLI Error, Unneeded Parameter
MiNID>config>test>l3sat#
```

### peer-profile *(parameterized — inner help harvested under "configure test l3sat peer-profile NAME")*
```text
- peer-profile <name>

MiNID>config>test>l3sat# peer-profile
```

### session-profile *(not entered — parameterized context)*
```text
- session-profile <name>

MiNID>config>test>l3sat# session-profile

auto-create probe 'session-profile zzz-hrvst' refused.
device response: session-profile zzz-hrvst
#CLI Error, Unneeded Parameter
MiNID>config>test>l3sat#
```

## configure test l3sat peer-profile NAME

Level help (`?`):
```text
performance-duration
udp-port
responder-type
```

### performance-duration
```text
(no help output captured)
```

### responder-type
```text
(no help output captured)
```

### udp-port
```text
(no help output captured)
```

## factory

Level help (`?`):
```text
eprom_ins
eprom_set
cfg_set
erase
cfg_ins
fpga
print-arp-table
```

### cfg_ins
```text
(no help output captured)
```

### cfg_set
```text
(no help output captured)
```

### eprom_ins
```text
(no help output captured)
```

### eprom_set
```text
(no help output captured)
```

### erase
```text
(no help output captured)
```

### print-arp-table
```text
MiNID>factory# print-arp-table
```

### show cfg
```text
MiNID>factory# print-arp-table show eprom show cfg
```

### show eprom
```text
MiNID>factory# print-arp-table show eprom
```

## factory fpga

Level help (`?`):
```text
read
write
show-statistics
clear-statistics
read_l2cp_table
read_flows_table
```

### clear-statistics
```text
(no help output captured)
```

### read
```text
(no help output captured)
```

### read_flows_table
```text
(no help output captured)
```

### read_l2cp_table
```text
(no help output captured)
```

### show-statistics
```text
(no help output captured)
```

### write
```text
(no help output captured)
```

## file

Level help (`?`):
```text
copy
delete
```

### copy
```text
(no help output captured)
```

### delete
```text
(no help output captured)
```

### show startup-config
```text
(no help output captured)
```

### show sw-pack
```text
(no help output captured)
```

### show user-default-config
```text
(no help output captured)
```
