from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )
from datetime import datetime
from Products.DataCollector.plugins.DataMaps import RelationshipMap


class BrocadeSWSensor(SnmpPlugin):
    sensortype = {
        1: 'Temperature',
        2: 'Fan',
        3: 'Power Supply',
        }
    sensorstatus = {
        1: 'unknown',
        2: 'faulty',
        3: 'below-min',
        4: 'nominal',
        5: 'above-max',
        6: 'absent',
        }

    snmpGetTableMaps = (
        GetTableMap(
            'SensorTable', '1.3.6.1.4.1.1588.2.1.1.1.1.22.1', {
                '.1': 'swSensorIndex',
                '.2': 'swSensorType',
                '.3': 'swSensorStatus',
                '.5': 'SensorInfo',
                }
            ),
        )

    def process(self, device, results, log):
        sensors = results[1].get('SensorTable', {})

        #rm = self.relMap()
        rez=[]
        temp=[]
        fans=[]
        power=[]
        for snmpindex, row in sensors.items():
            senstype = row.get('swSensorType')
            name = row.get('SensorInfo')
            if not name:
                log.warn('Skipping sensor with no name')
                continue

            if senstype == 1:
                temp.append(self.objectMap({
                    'id': self.prepId(name),
                    'title': name,
                    'snmpindex': snmpindex.strip('.'),
                    'statusdate': datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"),
                    'status': self.sensorstatus[row.get('swSensorStatus')],
                    }))
            elif senstype == 2:
                fans.append(self.objectMap({
                    'id': self.prepId(name),
                    'title': name,
                    'snmpindex': snmpindex.strip('.'),
                    'statusdate': datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"),
                    'status': self.sensorstatus[row.get('swSensorStatus')],
                    }))
            elif senstype == 3:
                power.append(self.objectMap({
                    'id': self.prepId(name),
                    'title': name,
                    'snmpindex': snmpindex.strip('.'),
                    'statusdate': datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"),
                    'status': self.sensorstatus[row.get('swSensorStatus')],
                    }))
        rez.append(RelationshipMap(
            relname='brocadeSWSensorTemperatures',
            modname='ZenPacks.community.BrocadeSW.BrocadeSWSensorTemperature',
            objmaps=temp,
        ))
        #print "--------------relname---"+relname+"---------------------"
        rez.append(RelationshipMap(
            relname='brocadeSWSensorFans',
            modname='ZenPacks.community.BrocadeSW.BrocadeSWSensorFan',
            objmaps=fans,
        ))
        rez.append(RelationshipMap(
            relname='brocadeSWSensorPowers',
            modname='ZenPacks.community.BrocadeSW.BrocadeSWSensorPower',
            objmaps=power,
        ))

        #print "print sensors"
        #print rez
        return rez
