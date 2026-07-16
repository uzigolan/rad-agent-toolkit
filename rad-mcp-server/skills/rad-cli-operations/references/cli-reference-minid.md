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

### inventory
```text
MiNID# inventory
```

### logon
```text
MiNID# logon
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

### flow *(parameterized — inner help harvested under "configure flows flow NAME")*
```text
- flow <flow-name>

MiNID>config>flows# flow
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
(no help output captured)
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

### lbm-reflector *(parameterized — inner help harvested under "configure flows lbm-reflector NAME")*
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

## configure flows flow NAME

Level help (`?`):
```text
[no] pm-collection
flow-action
[no] policer
[no] cos-mapping
classifier
[no] service-name
[no] l2cp
[no] shutdown
in-service-loops
in-service-l3-l4-loops
[no] test
clear-statistics
```

### classifier
```text
- cos-mapping profile <cos-mapping-profile-name>

MiNID>config>flows>flow(hrvst)# cos-mapping classifier classifier
```

### clear-statistics
```text
- test {loop-mac-ip-swap|discard}

MiNID>config>flows>flow(hrvst)# test clear-statistics
```

### cos-mapping
```text
- cos-mapping profile <cos-mapping-profile-name>

MiNID>config>flows>flow(hrvst)# cos-mapping
```

### flow-action
```text
(no help output captured)
```

### l2cp
```text
- cos-mapping profile <cos-mapping-profile-name>

MiNID>config>flows>flow(hrvst)# cos-mapping classifier classifier service-name l2cp
```

### pm-collection
```text
(no help output captured)
```

### service-name
```text
- cos-mapping profile <cos-mapping-profile-name>

MiNID>config>flows>flow(hrvst)# cos-mapping classifier classifier service-name
```

### show statistics
```text
- test {loop-mac-ip-swap|discard}

MiNID>config>flows>flow(hrvst)# test clear-statistics show statistics
```

### shutdown
```text
- cos-mapping profile <cos-mapping-profile-name>

MiNID>config>flows>flow(hrvst)# cos-mapping classifier classifier service-name l2cp shutdown
```

### test
```text
- test {loop-mac-ip-swap|discard}

MiNID>config>flows>flow(hrvst)# test
```

## configure flows flow NAME in-service-l3-l4-loops

Level help (`?`):
```text
[no] in-serv-l3-l4
```

### in-serv-l3-l4
```text
(no help output captured)
```

### responder
```text
(no help output captured)
```

## configure flows flow NAME in-service-loops

Level help (`?`):
```text
in-serv-mode
in-serv-action
[no] in-serv-src-mac
[no] in-serv-dst-mac
```

### in-serv-action
```text
(no help output captured)
```

### in-serv-dst-mac
```text
(no help output captured)
```

### in-serv-mode
```text
(no help output captured)
```

### in-serv-src-mac
```text
(no help output captured)
```

## configure flows flow NAME policer

Level help (`?`):
```text
profile
regular-accounting-only
envelope
```

### envelope
```text
(no help output captured)
```

### profile
```text
(no help output captured)
```

### regular-accounting-only
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

## configure flows lbm-reflector NAME

Level help (`?`):
```text
[no] md-level
[no] shutdown
```

### md-level
```text
(no help output captured)
```

### shutdown
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

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

### server *(parameterized — inner help harvested under "configure management tacacsplus server NAME")*
```text
- server <ip>

MiNID>config>mngmnt>tacacsplus# server
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

## configure management tacacsplus server NAME

Level help (`?`):
```text
accounting-port
authentication-port
clear-statistics
[no] group
[no] key
retry
timeout
[no] shutdown
```

### accounting-port
```text
(no help output captured)
```

### authentication-port
```text
(no help output captured)
```

### clear-statistics
```text
(no help output captured)
```

### group
```text
(no help output captured)
```

### key
```text
(no help output captured)
```

### retry
```text

```

### show statistics
```text
(no help output captured)
```

### shutdown
```text
(no help output captured)
```

### timeout
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

### maintenance-domain *(parameterized — inner help harvested under "configure oam cfm maintenance-domain NAME")*
```text
- maintenance-domain <md-index>

MiNID>config>oam>cfm# maintenance-domain
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

## configure oam cfm maintenance-domain NAME

Level help (`?`):
```text
md-level
[no] name
[no] maintenance-association
```

### maintenance-association *(parameterized — inner help harvested under "configure oam cfm maintenance-domain NAME maintenance-association NAME")*
```text
- maintenance-association <ma-idx>

MiNID>config>oam>cfm>md(2)# maintenance-association
```

### md-level
```text
(no help output captured)
```

### name
```text
(no help output captured)
```

## configure oam cfm maintenance-domain NAME maintenance-association NAME

Level help (`?`):
```text
ccm-interval
[no] interface-status-tlv
name
tag-mode
[no] service-name
[no] mep
[no] mip
```

### ccm-interval
```text
(no help output captured)
```

### interface-status-tlv
```text
(no help output captured)
```

### mep *(parameterized — inner help harvested under "configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME")*
```text
- mep <mep-id>

MiNID>config>oam>cfm>md(2)>ma(1)# mep
```

### name
```text
(no help output captured)
```

### service-name
```text
(no help output captured)
```

### tag-mode
```text
(no help output captured)
```

## configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME

Level help (`?`):
```text
[no] ais
bind
client-md-level
lbm
linktrace
dest-addr-type
priority
vlan
[no] remote-mep
[no] ccm-initiate
[no] shutdown
[no] service
```

### ais
```text
(no help output captured)
```

### bind
```text
(no help output captured)
```

### ccm-initiate
```text
- remote-mep <remote-mep-id>
show
MiNID>config>oam>cfm>md(2)>ma(1)>mep(1)# remote-mep 6 dest-mac-addr ccm-initiate
```

### client-md-level
```text
(no help output captured)
```

### dest-addr-type
```text
(no help output captured)
```

### dest-mac-addr
```text
- remote-mep <remote-mep-id>
show
MiNID>config>oam>cfm>md(2)>ma(1)>mep(1)# remote-mep 6 dest-mac-addr
```

### inner-priority
```text
(no help output captured)
```

### lbm
```text
(no help output captured)
```

### linktrace
```text
(no help output captured)
```

### outer-priority
```text
(no help output captured)
```

### outer-vlan
```text
(no help output captured)
```

### priority
```text
(no help output captured)
```

### remote-mep *(not entered — parameterized context)*
```text
- remote-mep <remote-mep-id>
show
MiNID>config>oam>cfm>md(2)>ma(1)>mep(1)# remote-mep

auto-create tried indices [1, 2, 3, 4, 5, 6], all refused.
last device response ('remote-mep 6'): remote-mep 6
MiNID>config>oam>cfm>md(2)>ma(1)>mep(1)#
next-arg help: - remote-mep <remote-mep-id>
show
MiNID>config>oam>cfm>md(2)>ma(1)>mep(1)# remote-mep 6
```

### service *(parameterized — inner help harvested under "configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME service NAME")*
```text
- service <service-idx>

MiNID>config>oam>cfm>md(2)>ma(1)>mep(1)# service
```

### show lbm-results
```text
(no help output captured)
```

### show linktrace-results
```text
(no help output captured)
```

### show status
```text
(no help output captured)
```

### shutdown
```text
- remote-mep <remote-mep-id>
show
MiNID>config>oam>cfm>md(2)>ma(1)>mep(1)# remote-mep 6 dest-mac-addr ccm-initiate shutdown
```

### vlan
```text
(no help output captured)
```

## configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME service NAME

Level help (`?`):
```text
delay-threshold
delay-var-threshold
lmm-interval
dmm-interval
loss-threshold
loss-dei-bit-color
priority
[no] shutdown
[no] dest-ne
clear-statistics
```

### clear-statistics
```text
MiNID>config>oam>cfm>md(2)>ma(1)>mep(1)>service(2)# clear-statistics
```

### delay-threshold
```text
(no help output captured)
```

### delay-var-threshold
```text
(no help output captured)
```

### dest-ne *(parameterized — inner help harvested under "configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME service NAME dest-ne NAME")*
```text
- dest-ne <dest-ne-id>

MiNID>config>oam>cfm>md(2)>ma(1)>mep(1)>service(2)# dest-ne
```

### dmm-interval
```text
(no help output captured)
```

### interval
```text
(no help output captured)
```

### lmm-interval
```text
(no help output captured)
```

### loss-dei-bit-color
```text
(no help output captured)
```

### loss-threshold
```text
(no help output captured)
```

### priority
```text
(no help output captured)
```

### shutdown
```text
(no help output captured)
```

## configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME service NAME dest-ne NAME

Level help (`?`):
```text
[no] delay
[no] bind-delay-measurement-bin
[no] bind-delay-var-measurement-bin
[no] loss
remote-mep
clear-statistics
[no] shutdown
show-statistics
show-delay-measurement-bins
```

### bind-delay-measurement-bin
```text
(no help output captured)
```

### bind-delay-var-measurement-bin
```text
(no help output captured)
```

### clear-statistics
```text
(no help output captured)
```

### delay
```text
(no help output captured)
```

### loss
```text
(no help output captured)
```

### remote-mep
```text
(no help output captured)
```

### shutdown
```text
(no help output captured)
```

## configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME service NAME dest-ne NAME show-delay-measurement-bins

Level help (`?`):
```text
running
current
interval
all-intervals
total-intervals
```

### all-intervals
```text
(no help output captured)
```

### current
```text
(no help output captured)
```

### interval
```text
(no help output captured)
```

### running
```text
(no help output captured)
```

### total-intervals
```text
(no help output captured)
```

## configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME service NAME dest-ne NAME show-statistics

Level help (`?`):
```text
running
current
interval
total-intervals
all-intervals
```

### all-intervals
```text
(no help output captured)
```

### current
```text
(no help output captured)
```

### interval
```text
(no help output captured)
```

### running
```text
(no help output captured)
```

### total-intervals
```text
(no help output captured)
```

## configure oam cfm maintenance-domain NAME maintenance-association NAME mip

Level help (`?`):
```text
priority
vlan
[no] shutdown
```

### inner-priority
```text
(no help output captured)
```

### outer-priority
```text
(no help output captured)
```

### outer-vlan
```text
(no help output captured)
```

### priority
```text
(no help output captured)
```

### shutdown
```text
(no help output captured)
```

### vlan
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

### controller *(parameterized — inner help harvested under "configure oam twamp controller NAME")*
```text
- controller <controller-name> [<number>]

MiNID>config>oam>twamp# controller
```

### profile *(parameterized — inner help harvested under "configure oam twamp profile NAME")*
```text
- profile <profile-name> [<number>]

MiNID>config>oam>twamp# profile
```

### responder *(parameterized — inner help harvested under "configure oam twamp responder NAME")*
```text
- responder <responder-name>

MiNID>config>oam>twamp# responder
```

## configure oam twamp controller NAME

Level help (`?`):
```text
local-ip-address
[no] shutdown
[no] peer
```

### local-ip-address
```text
(no help output captured)
```

### peer *(parameterized — inner help harvested under "configure oam twamp controller NAME peer NAME")*
```text
- peer <ip-address> [twamp-light]

MiNID>config>oam>twamp>controller(hrvst)# peer
```

### show status
```text
(no help output captured)
```

### shutdown
```text
(no help output captured)
```

## configure oam twamp controller NAME peer NAME

Level help (`?`):
```text
calculation-mode
[no] responder-seq-num
[no] test-session
[no] activate
show-status
show-summary-report
show-report
```

### activate
```text
(no help output captured)
```

### calculation-mode
```text
(no help output captured)
```

### responder-seq-num
```text
(no help output captured)
```

### show-report
```text
(no help output captured)
```

### show-status
```text
(no help output captured)
```

### show-summary-report
```text
(no help output captured)
```

### test-session
```text
(no help output captured)
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

## configure oam twamp responder NAME

Level help (`?`):
```text
ip-address
udp-port
[no] tx-seq-num
[no] ip-loan
[no] shutdown
unbind-all-flows
```

### ip-address
```text
(no help output captured)
```

### ip-loan
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

### tx-seq-num
```text
(no help output captured)
```

### udp-port
```text
(no help output captured)
```

### unbind-all-flows
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

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

### ethernet *(parameterized — inner help harvested under "configure port ethernet NAME")*
```text
- ethernet {sfp|msa}

MiNID>config>port# ethernet
```

## configure port ethernet NAME

Level help (`?`):
```text
[no] auto-negotiation
mtu
clear-statistics
```

### auto-negotiation
```text
(no help output captured)
```

### clear-statistics
```text
(no help output captured)
```

### force-direct-i2c
```text
(no help output captured)
```

### force-speed
```text
(no help output captured)
```

### i2c-stretching-clock
```text
(no help output captured)
```

### mtu
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

## configure qos

Level help (`?`):
```text
[no] policer-profile
[no] envelope-profile
[no] cos-map-profile
```

### cos-map-profile *(parameterized — inner help harvested under "configure qos cos-map-profile NAME")*
```text
- cos-map-profile <profile-name> classification {p-bit|ip-dscp}

MiNID>config>qos# cos-map-profile
```

### envelope-profile *(parameterized — inner help harvested under "configure qos envelope-profile NAME")*
```text
- envelope-profile <profile-name>

MiNID>config>qos# envelope-profile
```

### policer-profile *(parameterized — inner help harvested under "configure qos policer-profile NAME")*
```text
- policer-profile <profile-name>

MiNID>config>qos# policer-profile
```

## configure qos cos-map-profile NAME

Level help (`?`):
```text
map
```

### map
```text
(no help output captured)
```

## configure qos envelope-profile NAME

Level help (`?`):
```text
[no] cf-policy
[no] color_aware
compensation
[no] cos
```

### cf-policy
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

### cos *(parameterized — inner help harvested under "configure qos envelope-profile NAME cos NAME")*
```text
- cos [<value>]

MiNID>config>qos>envelope-profile(hrvst)# cos
```

### coupling-flag-0
```text
(no help output captured)
```

## configure qos envelope-profile NAME cos NAME

Level help (`?`):
```text
bandwidth
```

### bandwidth
```text
(no help output captured)
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

### interface *(parameterized — inner help harvested under "configure router interface NAME")*
```text
- interface <number>

MiNID>config>router# interface
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

## configure router interface NAME

Level help (`?`):
```text
[no] ipv6-autoconfig
[no] address
[no] vlan
bind
[no] dhcp
[no] loaned-ip
[no] dhcpv6-client
```

### address
```text
(no help output captured)
```

### bind
```text
(no help output captured)
```

### dhcp
```text
(no help output captured)
```

### dhcpv6-client
```text
(no help output captured)
```

### ipv6-autoconfig
```text
(no help output captured)
```

### loaned-ip
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

### vlan
```text
(no help output captured)
```

### vlan-tpid
```text
(no help output captured)
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

### syslog *(parameterized — inner help harvested under "configure system syslog NAME")*
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

### server *(parameterized — inner help harvested under "configure system date-and-time ntp server NAME")*
```text
- server <server-id>

MiNID>config>system>date-time>ntp# server
```

### show status
```text
(no help output captured)
```

## configure system date-and-time ntp server NAME

Level help (`?`):
```text
address
query-server
[no] shutdown
udp
```

### address
```text
(no help output captured)
```

### query-server
```text
(no help output captured)
```

### shutdown
```text
(no help output captured)
```

### udp
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

## configure system syslog NAME

Level help (`?`):
```text
facility
port
severity-level
[no] shutdown
clear-statistics
show-statistics
```

### accounting
```text
(no help output captured)
```

### address
```text
(no help output captured)
```

### clear-statistics
```text
(no help output captured)
```

### facility
```text
(no help output captured)
```

### port
```text
(no help output captured)
```

### severity-level
```text
(no help output captured)
```

### show-statistics
```text
(no help output captured)
```

### shutdown
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

auto-create tried [generator zzz-hrvst, generator hrvst, generator z], all refused.
last device response ('generator z'): generator z
#CLI Error, Maximum Number Of Generator Profile Reached
MiNID>config>test>l3sat#
```

### peer-profile *(parameterized — inner help harvested under "configure test l3sat peer-profile NAME")*
```text
- peer-profile <name>

MiNID>config>test>l3sat# peer-profile
```

### session-profile *(parameterized — inner help harvested under "configure test l3sat session-profile NAME")*
```text
- session-profile <name>

MiNID>config>test>l3sat# session-profile
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

## configure test l3sat session-profile NAME

Level help (`?`):
```text
loss-ratio-threshold
delay-threshold
delay-variation-threshold
[no] packet-size
[no] L1-rate
```

### L1-rate
```text
(no help output captured)
```

### delay-threshold
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

### packet-size
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
