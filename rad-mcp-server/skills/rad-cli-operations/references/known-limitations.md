# Harvest Known Limitations

Generated from current artifacts on 2026-07-16 05:27 UTC.

Scope:
- command-tree-<family>.md
- cli-help-<family>.jsonl

Definitions:
- args-noenter: tree node reached but not entered by harvester.
- missing-contexts: context nodes in tree without a captured level section.
- missing-leaves: leaf nodes in tree without a captured command help record.

## Coverage Summary

| Family | Total JSONL Records | args-noenter | Missing Contexts | Missing Leaves |
|---|---:|---:|---:|---:|
| etx1p | 705 | 27 | 95 | 575 |
| etx2 | 917 | 51 | 125 | 839 |
| etx2v | 537 | 24 | 73 | 423 |
| minid | 387 | 6 | 39 | 198 |
| mp1 | 406 | 19 | 48 | 247 |
| mp4100 | 637 | 55 | 110 | 703 |
| secflow | 778 | 34 | 115 | 688 |

## etx1p Uncovered Tree Nodes

Count: 27

- configure access-control firewall :: interzone
- configure fault :: group
- configure management radius :: server
- configure management snmp :: access-group
- configure management snmp :: community
- configure management snmp :: notify-filter
- configure management snmp :: security-to-group
- configure management snmp :: trap-sync-group
- configure management snmp :: user
- configure management snmp :: view
- configure port :: cellular
- configure port ethernet NAME :: classifier
- configure port ethernet NAME :: vlan
- configure port virtual NAME :: vlan
- configure protection :: erp
- configure router NAME :: bfd-neighbor
- configure router NAME :: prefix-list
- configure router NAME interface NAME :: vrrp
- configure router NAME ospf :: area
- configure system :: dhcp-server
- configure system :: dhcpv6-server
- configure system :: syslog
- quick-setup port :: cellular
- quick-setup port :: ethernet
- quick-setup router :: router
- quick-setup vpn :: ipsec-transform-set
- quick-setup vpn :: isakmp-policy

## etx2 Uncovered Tree Nodes

Count: 51

- configure :: mirroring-session
- configure :: service
- configure access-control :: access-list
- configure bridge NAME :: port
- configure bridge NAME :: vlan
- configure bridge NAME spanning-tree :: mst
- configure crypto :: isakmp-policy
- configure fault :: fault-propagation
- configure fault cfm :: service
- configure flows :: classifier-profile
- configure flows flow NAME :: mark
- configure management :: login-user
- configure management radius :: server
- configure management snmp :: access-group
- configure management snmp :: community
- configure management snmp :: notify-filter
- configure management snmp :: security-to-group
- configure management snmp :: target-params
- configure management snmp :: trap-sync-group
- configure management snmp :: user
- configure management snmp :: view
- configure management tacacsplus :: group
- configure management tacacsplus :: server
- configure oam cfm maintenance-domain NAME :: mip
- configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME :: service
- configure oam twamp :: controller
- configure oam twamp :: profile
- configure oam twamp :: responder
- configure port :: cellular
- configure port :: ds1
- configure port :: gfp
- configure port :: hdlc
- configure port :: int-ethernet
- configure port :: sdh-sonet
- configure port :: smart-sfp
- configure port :: vdsl2
- configure port ethernet NAME :: efm
- configure port logical-mac NAME :: efm
- configure protection :: erp
- configure protection :: ethernet-group
- configure pwe :: pw
- configure qos :: wred-profile
- configure qos queue-block-profile NAME :: queue
- configure router NAME :: prefix-list
- configure router NAME :: tunnel-interface
- configure router NAME interface NAME :: ospf
- configure router NAME interface NAME :: vrrp
- configure router NAME ospf :: area
- configure system :: dhcp-server
- configure system :: inventory
- configure system :: syslog

## etx2v Uncovered Tree Nodes

Count: 24

- configure access-control :: access-list
- configure management radius :: server
- configure management snmp :: access-group
- configure management snmp :: community
- configure management snmp :: notify-filter
- configure management snmp :: security-to-group
- configure management snmp :: trap-sync-group
- configure management snmp :: user
- configure management snmp :: view
- configure port :: cellular
- configure port :: virtual
- configure port :: wlan
- configure port ethernet NAME :: classifier
- configure port ethernet NAME :: vlan
- configure router NAME :: bgp
- configure router NAME :: prefix-list
- configure router NAME interface NAME :: ospf
- configure router NAME ospf :: area
- configure system :: dhcp-server
- configure system :: dhcpv6-server
- configure system :: syslog
- configure system date-and-time ntp :: server
- configure virtualization :: add-ons
- configure virtualization :: interface

## minid Uncovered Tree Nodes

Count: 6

- configure access-control :: access-list
- configure flows :: in-service-loops-l3-l4
- configure flows :: in-service-loops-mac
- configure management :: host
- configure oam cfm maintenance-domain NAME maintenance-association NAME mep NAME :: remote-mep
- configure test l3sat :: generator

## mp1 Uncovered Tree Nodes

Count: 19

- configure access-control :: access-list
- configure bridge NAME :: port
- configure bridge NAME :: vlan
- configure flows :: classifier-profile
- configure management :: login-user
- configure management radius :: server
- configure management snmp :: access-group
- configure management snmp :: community
- configure management snmp :: notify-filter
- configure management snmp :: security-to-group
- configure management snmp :: target
- configure management snmp :: trap-sync-group
- configure management snmp :: user
- configure management snmp :: view
- configure port :: t1
- configure protection :: tdm-group
- configure system :: syslog
- configure system clock domain NAME :: source
- configure system date-and-time sntp :: server

## mp4100 Uncovered Tree Nodes

Count: 55

- configure access-control :: access-list
- configure fault :: fault-propagation
- configure fault cfm :: service
- configure flows :: classifier-profile
- configure management :: trap-sync-group
- configure management snmp :: access-group
- configure management snmp :: notify
- configure management snmp :: notify-filter
- configure management snmp :: notify-filter-profile
- configure management snmp :: security-to-group
- configure management snmp :: target
- configure management snmp :: target-params
- configure management snmp :: user
- configure management snmp :: view
- configure oam :: efm-descriptor
- configure oam cfm :: measurement-bin-profile
- configure oam cfm maintenance-domain NAME maintenance-association :: mep
- configure port :: bri
- configure port :: cmd-channel
- configure port :: cmd-in
- configure port :: cmd-in-i
- configure port :: cmd-out
- configure port :: cmd-out-i
- configure port :: ds0-bundle
- configure port :: ds0-g703
- configure port :: ds1-opt
- configure port :: e1
- configure port :: e1-i
- configure port :: gfp
- configure port :: hdlc
- configure port :: int-ethernet
- configure port :: logical-mac
- configure port :: lre
- configure port :: mlppp
- configure port :: mux-eth-tdm
- configure port :: pcs
- configure port :: ppp
- configure port :: serial-bundle
- configure port :: shdsl
- configure port :: t1
- configure port :: t3
- configure port :: vcg
- configure port ethernet NAME :: efm
- configure port sdh-sonet NAME :: aug
- configure port sdh-sonet NAME oc3 NAME sts1 NAME :: vt1-5
- configure protection :: ds0-group
- configure protection :: erp
- configure protection :: ethernet-group
- configure protection :: io-group
- configure protection :: tdm-group
- configure protection :: tdm-ring
- configure protection :: vc-path
- configure slot NAME :: ms-module
- configure system clock domain NAME :: source
- configure system date-and-time sntp :: server

## secflow Uncovered Tree Nodes

Count: 34

- configure access-control :: access-list
- configure access-control firewall :: interzone
- configure fault :: group
- configure management radius :: server
- configure management snmp :: access-group
- configure management snmp :: community
- configure management snmp :: notify-filter
- configure management snmp :: security-to-group
- configure management snmp :: trap-sync-group
- configure management snmp :: user
- configure management snmp :: view
- configure port :: cellular
- configure port :: wlan
- configure port ethernet NAME :: classifier
- configure port ethernet NAME :: vlan
- configure port virtual NAME :: vlan
- configure router NAME :: bfd-neighbor
- configure router NAME :: prefix-list
- configure router NAME interface NAME :: vrrp
- configure router NAME ospf :: area
- configure sd-iot :: tunnel
- configure system :: dhcp-server
- configure system :: dhcpv6-server
- configure system :: syslog
- configure system clock :: gnss
- quick-setup port :: cellular
- quick-setup port :: ethernet
- quick-setup port :: serial
- quick-setup port :: wlan
- quick-setup port wifi-client :: dot1x
- quick-setup port wifi-client :: ssid
- quick-setup router :: router
- quick-setup vpn :: ipsec-transform-set
- quick-setup vpn :: isakmp-policy
