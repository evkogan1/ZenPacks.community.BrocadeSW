from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class BrocadeSW(SnmpPlugin):
    snmpGetTableMaps = (
        GetTableMap(
            'swSystemTable', '1.3.6.1.4.1.1588.2.1.1.1.1', {
                '.10': 'swSsn',
                #'.7': 'swOperStatus',
                '.6': 'swFirmwareVersion',
                #'.20': 'swDiagResult',
                }
            ),
        GetTableMap(
            'swCpuOrMemoryUsage', '1.3.6.1.4.1.1588.2.1.1.1.26', {
                '.3': 'swCpuUsageLimit',
                '.11': 'swMemUsageLimit1',
                '.8': 'swMemUsageLimit',
                '.12': 'swMemUsageLimit3',
                }
            ),
        )


    def process(self, device, results, log):
        #print 'swCpuOrMemoryUsage:swMemUsageLimit3='
        #print results[1].get('swCpuOrMemoryUsage', {})['.0']['swMemUsageLimit3']
        #thresholdmap=results[1].get('swCpuOrMemoryUsage', {}).values()[0]
        #print thresholdmap['swMemUsageLimit3']
        
        data = {
            'firmwareversion': 'None',
            'threshold_mem': 70,
            'threshold_cpu': 75,
            'setHWSerialNumber': 'None',
	    }
	    
        swSystemTable = results[1].get('swSystemTable')
        if swSystemTable :
	    if swSystemTable['.0'].get('swFirmwareVersion'):
		data['firmwareversion']= swSystemTable['.0'].get('swFirmwareVersion')
	    if swSystemTable['.0'].get('swSsn'):
		data['setHWSerialNumber']= swSystemTable['.0'].get('swSsn')
        swCpuOrMemoryUsage = results[1].get('swCpuOrMemoryUsage')
        if swCpuOrMemoryUsage :
	    if swCpuOrMemoryUsage['.0'].get('swMemUsageLimit3'):
		data['threshold_mem']= swCpuOrMemoryUsage['.0'].get('swMemUsageLimit3')
	    if swCpuOrMemoryUsage['.0'].get('swCpuUsageLimit'):
		data['threshold_cpu']= swCpuOrMemoryUsage['.0'].get('swCpuUsageLimit')


	om=self.objectMap(data)
        #om.setHWSerialNumber=str(results[1].get('swSystemTable', {})['.0']['swSsn'],)
        #print "----------BrocadeSW------------"
        #print om
        return om
