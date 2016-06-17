from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )
from datetime import datetime
from Products.DataCollector.plugins.DataMaps import RelationshipMap
import binascii
from ZenPacks.community.BrocadeSW.oidmapper import extract_oid, GetTableMapHash
#from pprint import pprint

class BrocadeSWFCPort(SnmpPlugin):
    relname='brocadeSWFCPorts'
    modname='ZenPacks.community.BrocadeSW.BrocadeSWFCPort'

    OidMap = {
        'Speed': {
            'connUnitPortEntry': {
                'field': 'connUnitPortSpeed',
                'func': lambda x: x * 8 / 1000000,
                'oid': '.15',
                },
            #Disabled beacos old Switchs answered 'auto-Negotiate' and crash monitoring threshold
            #'swFCPortEntry': {
                #'field': 'swFCPortSpeed',
                #'map':{
                    #1: '1',
                    #2: '2',
                    #3: 'auto-Negotiate',
                    #4: '4',
                    #5: '8',
                    #6: '10',
                    #7: 'unknown',
                    #8: '16',
                #},
                #'oid': '.35',
            #},
        },
        'status': {
            'connUnitPortEntry': {
                'field': 'connUnitPortState',
                'map':{
                    1: 'unknown',
                    2: 'online',
                    3: 'offline',
                    4: 'bypassed',
                    5: 'diagnostics',
                    },
                'oid': '.6',
                },
            'swFCPortEntry': {
                'field': 'swFCPortOpStatus',
                'map':{
                    0: 'unknown',
                    1: 'online',
                    2: 'offline',
                    3: 'testing',
                    4: 'faulty',
                },
                'oid': '.4',
            },
        },
        'TxType': {
            'connUnitPortEntry': {
                'field': 'connUnitPortTransmitterType',
                'map':{
                    1: 'unknown',
                    2: 'other',
                    3: 'unused',
                    4: 'shortwave',
                    5: 'longwave',
                    6: 'copper',
                    7: 'scsi',
                    8: 'longwaveNoOFC',
                    9: 'shortwaveNoOFC',
                    10: 'longwaveLED',
                    11: 'ssa',
                },
                'oid': '.8',
            },
            'swFCPortEntry': {
                'field': 'swFCPortTxType',
                'map':{
                   1: 'unknown',
                   2: 'lw',
                   3: 'sw',
                   4: 'ld',
                   5: 'cu',
                },
                'oid': '.7',
            },
        },
        'PortName': {
            'connUnitPortEntry': {
                'field': 'connUnitPortName',
                'oid': '.17',
            },
            'swFCPortEntry': {
                'field': 'swFCPortName',
                'oid': '.36',
            },
        },
        'PortNumber': {
            'connUnitPortEntry': {
                'field': 'connUnitPortPhysicalNumber',
                'oid': '.18',
                'func': lambda x: int(x),
                },
            'swFCPortEntry': {
                'field': 'swFCPortSpecifier',
                'oid': '.37',
                'func': lambda x: int(x),
            },
        },
        'LocalWWN': {
            'connUnitPortEntry': {
                'field': 'connUnitPortWwn',
                'oid': '.10',
                'func': lambda x: binascii.hexlify(x),
            },
            'swFCPortEntry': {
                'field': 'swFCPortWwn',
                'oid': '.34',
                'func': lambda x: binascii.hexlify(x),
            },
            'swNsLocalEntry': {
                'field': 'LocalWWN',
                'oid': '.13',
            },
        },
        'RemotePortWWPN': {
            'swNsLocalEntry': {
                'field': 'RemotePortWWPN',
                'oid': '.4',
                'func': lambda x: binascii.hexlify(x),
            },
        },
        'RemotePortSymb': {
            'swNsLocalEntry': {
                'field': 'RemotePortSymb',
                'oid': '.5',
            },
        },
        'RemotePortWWNN': {
            'swNsLocalEntry': {
                'field': 'RemotePortWWNN',
                'oid': '.6',
                'func': lambda x: binascii.hexlify(x),
            },
        },
        'RemoteNodeSymb': {
            'swNsLocalEntry': {
                'field': 'RemoteNodeSymb',
                'oid': '.7',
            },
        },
        'PortType': {
            'connUnitPortEntry': {
                'field': 'connUnitPortType',
                'map': {
                    1: 'unknown',
                    2: 'other',
                    3: 'not-present',
                    4: 'hub-port',
                    5: 'n-port',
                    6: 'nl-port',
                    7: 'fl-port',
                    8: 'f-port',
                    9: 'e-port',
                    10: 'g-port',
                    11: 'domain-ctl',
                    12: 'hub-controller',
                    13: 'scsi',
                    14: 'escon',
                    15: 'lan',
                    16: 'wan',
                    17: 'ac',
                    18: 'dc',
                    19: 'ssa',
                    20: 'wdm',
                    21: 'ib',
                    22: 'ipstore',
                },
                'oid': '.3',
            },
            'swFCPortEntry': {
                'field': 'swFCPortBrcdType',
                'map':{
                    1: 'unknown',
                    2: 'other',
                    3: 'fl-port',
                    4: 'f-port',
                    5: 'e-port',
                    6: 'g-port',
                    7: 'ex-port',
                },
                'oid': '.39',
            },
        },
        'PhyState': {
            'swFCPortEntry': {
                'field': 'swFCPortPhyState',
                'map':{
                    1: 'noCard',
                    2: 'noTransceiver',
                    3: 'laserFault',
                    4: 'noLight',
                    5: 'noSync',
                    6: 'inSync',
                    7: 'portFault',
                    8: 'diagFault',
                    9: 'lockRef',
                    10: 'validating',
                    11: 'invalidModule',
                    255: 'unknown',
                },
                'oid': '.3',
            },
            'connUnitPortEntry': {
                'field': 'connUnitPortHWState',
                'map':{
                    1: 'unknown',
                    2: 'failed',
                    3: 'bypassed',
                    4: 'active',
                    5: 'loopback',
                    6: 'txfault',
                    7: 'noMedia',
                    8: 'linkDown',
                },
                'oid': '.23',
            },
        },
        'LinkState': {
            'swFCPortEntry': {
                'field': 'swFCPortLinkState',
                'map':{
                    1: 'enabled',
                    2: 'disabled',
                    3: 'loopback',
                },
                'oid': '.6',
            },
        },
        'connUnitPortStatus': {
            #not used in zenpack
            'connUnitPortEntry': {
                'field': 'connUnitPortStatus',
                'map':{
                    1: 'unknown',
                    2: 'unused',
                    3: 'ready',
                    4: 'warning',
                    5: 'failure',
                    6: 'notparticipating',
                    7: 'initializing',
                    8: 'bypass',
                    9: 'ols',
                    10: 'other',
                },
                'oid': '.7',
            },
        },
        'snmpindex': {
            'swFCPortEntry': {
            },
        },
    }

    #hashmap = GetTableMapHash(OidMap, 'swFCPortEntry')
    #print GetTableMapHash(OidMap, 'swFCPortEntry')
    #print GetTableMapHash(OidMap, 'swNsLocalEntry')
    #print GetTableMapHash(OidMap, 'connUnitPortEntry')

    snmpGetTableMaps = (
      GetTableMap(
           'swFCPortEntry', '1.3.6.1.4.1.1588.2.1.1.1.6.2.1', GetTableMapHash(OidMap, 'swFCPortEntry'),
           ),
      GetTableMap(
           'swNsLocalEntry', '1.3.6.1.4.1.1588.2.1.1.1.7.2.1', GetTableMapHash(OidMap, 'swNsLocalEntry'),
           ),
      GetTableMap(
           'connUnitPortEntry', '1.3.6.1.3.94.1.10.1', GetTableMapHash(OidMap, 'connUnitPortEntry'),
           ),
      )


    def process(self, device, results, log):
        rm = self.relMap()
        #pprint (results)
        ports=extract_oid(self.OidMap, results, ['swFCPortEntry', 'connUnitPortEntry', 'swNsLocalEntry'], 'LocalWWN') #Event Transform used status from swFCPortEntry.
        #ports=extract_oid(self.OidMap, results, ['swFCPortEntry', 'swNsLocalEntry'], 'LocalWWN')

        for port_snmpindex, port_row in ports.items():
            port_row.update ({
                'id': self.prepId(port_row['LocalWWN']),
                'title': 'FC port '+str(port_row['PortNumber']),
                'statusdate': datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"),
            })
            rm.append(self.objectMap(port_row))
        #pprint (rm)
        return rm
