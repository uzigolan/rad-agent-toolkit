# SNMP capability map — family `minid` (unit minid-1)

Walked live 2026-07-16, read-only GETNEXT (v2c community public); names rendered with the MIBS/+MIBs2/ union map (35,977 objects).
Symbolic names from `snmp-oid-map.json` (compiled from the workspace
MIBS/ set). Row caps are stated per subtree — a capped walk means
MORE data exists beyond the cap, not that the listing is complete.

**Agent caveat (minid SW 2.6.0(0.28)):** this agent's GETNEXT chain is
SPARSE — it skips whole arcs (e.g. jumps from ifTable into the snmp group)
and goes SILENT at end-of-view instead of answering (both also true of its
GETBULK, which additionally mis-orders). So this map is the *walk-reachable*
view; a direct GET of a known OID may still answer even if it never appears
in a walk. Poll minid by explicit OID lists (snmp_get), not discovery walks.

## mib-2 (`1.3.6.1.2.1`) — 53 varbinds — *agent stopped responding after 1.3.6.1.2.1.47.1.1.1.1.11.1001 (known small-agent end-of-view quirk)*

| Object group | Rows | Example |
|---|---|---|
| `IF-MIB::ifIndex` | 3 | `IF-MIB::ifIndex.1` = 1 |
| `IF-MIB::ifDescr` | 3 | `IF-MIB::ifDescr.1` = RAD MiNID SFP Port |
| `IF-MIB::ifPhysAddress` | 3 | `IF-MIB::ifPhysAddress.1` = 0x1806f5cd0653 |
| `IF-MIB::ifType` | 2 | `IF-MIB::ifType.1` = 6 |
| `IF-MIB::ifSpeed` | 2 | `IF-MIB::ifSpeed.1` = 1000000000 |
| `IF-MIB::ifAdminStatus` | 2 | `IF-MIB::ifAdminStatus.1` = 1 |
| `IF-MIB::ifOperStatus` | 2 | `IF-MIB::ifOperStatus.1` = 2 |
| `IF-MIB::ifHCInOctets` | 2 | `IF-MIB::ifHCInOctets.1` = 0 |
| `IF-MIB::ifHCOutOctets` | 2 | `IF-MIB::ifHCOutOctets.1` = 20855107697 |
| `IF-MIB::ifAlias` | 2 | `IF-MIB::ifAlias.1` = SFP |
| `IF-MIB::ifCounterDiscontinuityTime` | 2 | `IF-MIB::ifCounterDiscontinuityTime.1` = 0 |
| `SNMPv2-MIB::sysDescr` | 1 | `SNMPv2-MIB::sysDescr.0` = MiNID Hw: 1.2, Sw: 2.6.0(0.28) |
| `SNMPv2-MIB::sysObjectID` | 1 | `SNMPv2-MIB::sysObjectID.0` = SNMPv2-SMI::enterprises.164.6.1.6.36 |
| `SNMPv2-MIB::sysUpTime` | 1 | `SNMPv2-MIB::sysUpTime.0` = 11212200 |
| `SNMPv2-MIB::sysContact` | 1 | `SNMPv2-MIB::sysContact.0` = RAD |
| `SNMPv2-MIB::sysName` | 1 | `SNMPv2-MIB::sysName.0` = MiNID |
| `SNMPv2-MIB::sysLocation` | 1 | `SNMPv2-MIB::sysLocation.0` = RAD |
| `SNMPv2-MIB::sysServices` | 1 | `SNMPv2-MIB::sysServices.0` = 70 |
| `IF-MIB::ifNumber` | 1 | `IF-MIB::ifNumber.0` = 2 |
| `SNMPv2-MIB::snmpInPkts` | 1 | `SNMPv2-MIB::snmpInPkts.0` = 7754 |
| `SNMPv2-MIB::snmpOutPkts` | 1 | `SNMPv2-MIB::snmpOutPkts.0` = 7682 |
| `SNMPv2-MIB::snmpInBadVersions` | 1 | `SNMPv2-MIB::snmpInBadVersions.0` = 0 |
| `SNMPv2-MIB::snmpInBadCommunityNames` | 1 | `SNMPv2-MIB::snmpInBadCommunityNames.0` = 2 |
| `SNMPv2-MIB::snmpInTooBigs` | 1 | `SNMPv2-MIB::snmpInTooBigs.0` = 0 |
| `SNMPv2-MIB::snmpInTotalReqVars` | 1 | `SNMPv2-MIB::snmpInTotalReqVars.0` = 8647 |
| `SNMPv2-MIB::snmpInTotalSetVars` | 1 | `SNMPv2-MIB::snmpInTotalSetVars.0` = 0 |
| `SNMPv2-MIB::snmpInGetRequests` | 1 | `SNMPv2-MIB::snmpInGetRequests.0` = 6863 |
| `SNMPv2-MIB::snmpInGetNexts` | 1 | `SNMPv2-MIB::snmpInGetNexts.0` = 885 |
| `SNMPv2-MIB::snmpInSetRequests` | 1 | `SNMPv2-MIB::snmpInSetRequests.0` = 0 |
| `SNMPv2-MIB::snmpOutTooBigs` | 1 | `SNMPv2-MIB::snmpOutTooBigs.0` = 0 |
| `SNMPv2-MIB::snmpOutNoSuchNames` | 1 | `SNMPv2-MIB::snmpOutNoSuchNames.0` = 64 |
| `SNMPv2-MIB::snmpOutBadValues` | 1 | `SNMPv2-MIB::snmpOutBadValues.0` = 0 |
| `SNMPv2-MIB::snmpOutGenErrs` | 1 | `SNMPv2-MIB::snmpOutGenErrs.0` = 0 |
| `SNMPv2-MIB::snmpOutTraps` | 1 | `SNMPv2-MIB::snmpOutTraps.0` = 0 |
| `SNMPv2-MIB::snmpEnableAuthenTraps` | 1 | `SNMPv2-MIB::snmpEnableAuthenTraps.0` = enabled |
| `SNMPv2-MIB::snmpSilentDrops` | 1 | `SNMPv2-MIB::snmpSilentDrops.0` = 0 |
| `MAU-MIB::ifMauType` | 1 | `MAU-MIB::ifMauType.0` = 1.3.6.1.4.1.164.3.1.6.1.10.2 |
| `MAU-MIB::ifMauDefaultType` | 1 | `MAU-MIB::ifMauDefaultType.0` = 1.3.6.1.4.1.164.3.1.6.1.10.4 |
| `ENTITY-MIB::entPhysicalSerialNum` | 1 | `ENTITY-MIB::entPhysicalSerialNum.1001` = 18-06-F5-CD-06-53 |

## rad-enterprise(164) (`1.3.6.1.4.1.164`) — 31 varbinds — *agent stopped responding after 1.3.6.1.4.1.164.6.1.14.1.3.1.3.1 (known small-agent end-of-view quirk)*

| Object group | Rows | Example |
|---|---|---|
| `RAD-OamCfm-MIB::ethOamMeasureBinProfileRowStatus` | 1 | `RAD-OamCfm-MIB::ethOamMeasureBinProfileRowStatus.1` = 1 |
| `RAD-OamCfm-MIB::ethOamMeasureBinProfileName` | 1 | `RAD-OamCfm-MIB::ethOamMeasureBinProfileName.1` = 0x15696e666f00745f6e616d653100000000000000000000000000000000 |
| `RAD-OamCfm-MIB::ethOamMeasureBinThresh` | 1 | `RAD-OamCfm-MIB::ethOamMeasureBinThresh.1` =  |
| `RAD-OamCfm-MIB::ethOamConfigAlarmType` | 1 | `RAD-OamCfm-MIB::ethOamConfigAlarmType.1` = 1 |
| `RAD-OamCfm-MIB::ethOamConfigAvailabilityDeltaT` | 1 | `RAD-OamCfm-MIB::ethOamConfigAvailabilityDeltaT.1` = 1 |
| `RAD-OamCfm-MIB::ethOamConfigAvailabilityNumDeltaTs` | 1 | `RAD-OamCfm-MIB::ethOamConfigAvailabilityNumDeltaTs.1` = 10 |
| `RAD-OamCfm-MIB::ethOamConfigAvailabilityFwdFlrThreshold` | 1 | `RAD-OamCfm-MIB::ethOamConfigAvailabilityFwdFlrThreshold.1` = 50 |
| `RAD-OamCfm-MIB::ethOamConfigAvailabilityBckFlrThreshold` | 1 | `RAD-OamCfm-MIB::ethOamConfigAvailabilityBckFlrThreshold.1` = 50 |
| `RAD-Dacs-MIB::sysSDateFormat` | 1 | `RAD-Dacs-MIB::sysSDateFormat.0` = 4 |
| `RAD-TACACS-MIB::tacplusServerAddressType` | 1 | `RAD-TACACS-MIB::tacplusServerAddressType.1.4.1.1.1.1.1` = 1 |
| `RAD-TACACS-MIB::tacplusServerAddress` | 1 | `RAD-TACACS-MIB::tacplusServerAddress.1.4.1.1.1.1.1` = 1.1.1.1 |
| `RAD-TACACS-MIB::tacplusServerPort` | 1 | `RAD-TACACS-MIB::tacplusServerPort.1.4.1.1.1.1.1` = 49 |
| `RAD-TACACS-MIB::tacplusRowStatus` | 1 | `RAD-TACACS-MIB::tacplusRowStatus.1.4.1.1.1.1.1` = 5 |
| `RAD-TACACS-MIB::tacplusSecretKey` | 1 | `RAD-TACACS-MIB::tacplusSecretKey.1.4.1.1.1.1.1` =  |
| `RAD-TACACS-MIB::tacplusRetryCount` | 1 | `RAD-TACACS-MIB::tacplusRetryCount.1.4.1.1.1.1.1` = 3 |
| `RAD-TACACS-MIB::tacplusTimeout` | 1 | `RAD-TACACS-MIB::tacplusTimeout.1.4.1.1.1.1.1` = 5 |
| `RAD-TACACS-MIB::tacplusAccountingPort` | 1 | `RAD-TACACS-MIB::tacplusAccountingPort.1.4.1.1.1.1.1` = 49 |
| `RAD-TACACS-MIB::tacplusServerGroup` | 1 | `RAD-TACACS-MIB::tacplusServerGroup.1.4.1.1.1.1.1` = 0 |
| `RAD-TACACS-MIB::tacplusAuthenticationPort` | 1 | `RAD-TACACS-MIB::tacplusAuthenticationPort.1.4.1.1.1.1.1` = 49 |
| `RAD-TACACS-MIB::tacplusClearStaticsCmd` | 1 | `RAD-TACACS-MIB::tacplusClearStaticsCmd.1.4.1.1.1.1.1` = 2 |
| `RAD-TACACS-MIB::tacplusAuthRequests` | 1 | `RAD-TACACS-MIB::tacplusAuthRequests.1.4.1.1.1.1.1` = 0 |
| `RAD-TACACS-MIB::tacplusAuthenRequestTimeouts` | 1 | `RAD-TACACS-MIB::tacplusAuthenRequestTimeouts.1.4.1.1.1.1.1` = 0 |
| `RAD-TACACS-MIB::tacplusAuthenUnexpectedResponses` | 1 | `RAD-TACACS-MIB::tacplusAuthenUnexpectedResponses.1.4.1.1.1.1.1` = 0 |
| `RAD-TACACS-MIB::tacplusAuthenServerErrorResponses` | 1 | `RAD-TACACS-MIB::tacplusAuthenServerErrorResponses.1.4.1.1.1.1.1` = 0 |
| `RAD-TACACS-MIB::tacplusAuthenIncorrectResponses` | 1 | `RAD-TACACS-MIB::tacplusAuthenIncorrectResponses.1.4.1.1.1.1.1` = 0 |
| `RAD-TACACS-MIB::tacplusAuthenTransactionSuccesses` | 1 | `RAD-TACACS-MIB::tacplusAuthenTransactionSuccesses.1.4.1.1.1.1.1` = 0 |
| `RAD-TACACS-MIB::tacplusAuthenTransactionFailures` | 1 | `RAD-TACACS-MIB::tacplusAuthenTransactionFailures.1.4.1.1.1.1.1` = 0 |
| `RAD-TACACS-MIB::tacplusAuthenPendingRequests` | 1 | `RAD-TACACS-MIB::tacplusAuthenPendingRequests.1.4.1.1.1.1.1` = 0 |
| `RAD-TACACS-MIB::tacplusServerGroupId` | 1 | `RAD-TACACS-MIB::tacplusServerGroupId.1` = 1 |
| `RAD-TACACS-MIB::tacplusServerGroupRowStatus` | 1 | `RAD-TACACS-MIB::tacplusServerGroupRowStatus.1` = 1 |
| `RAD-TACACS-MIB::tacplusServerGroupName` | 1 | `RAD-TACACS-MIB::tacplusServerGroupName.1` = 0x15696e666f |

## ieee802.1 (`1.0.8802`) — 0 varbinds (complete)

*(no response / empty subtree)*
