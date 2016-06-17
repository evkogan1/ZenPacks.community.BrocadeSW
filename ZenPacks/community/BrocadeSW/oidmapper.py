#from pprint import pprint
import binascii

def extract_oid (oidmap, results, oidnames, keyoid):
    """
        Merge OIDs from oidnames[] by keyoid in oidmap. Result hash takes found value from oidnames[]
        First oidname has privileged.
        snmpindex used for monitoring in the datasource and must be in oidmap for defined oidname which corresponds snmpindex for datasource.
    """
    oids = {}
    data = {}
    data2 = {}

    for oidname in oidnames :
        temp_r = results[1].get(oidname, {})
        oids[oidname] = {}
        #print oidname
        for snmpindex, item in temp_r.iteritems() :
            #print item
            oids[oidname][item[oidmap[keyoid][oidname]['field']]] = item
            oids[oidname][item[oidmap[keyoid][oidname]['field']]]['snmpindex'] = snmpindex
        for keyname in oidmap.keys() :
            #print keyname
            #print oidname
            #print oidmap
            if oidname in oidmap[keyname] :
                for key, item2 in oids[oidname].items() :
                    if key not in data :
                        data[key]= {}
                    if keyname not in data[key] :
                        if keyname == 'snmpindex':
                            data[key][keyname]=item2['snmpindex'].strip('.')
                        elif item2.get(oidmap[keyname][oidname]['field']) is not None :
                            #print 'keyname='+keyname
                            #print 'oidname='+oidname
                            #print 'oidname_fields='+oidmap[keyname][oidname]['field']
                            data[key][keyname]=item2[oidmap[keyname][oidname]['field']]
                            if 'map' in oidmap[keyname][oidname] :
                                data[key][keyname]=oidmap[keyname][oidname]['map'][data[key][keyname]]
                            if 'func' in oidmap[keyname][oidname] :
                                data[key][keyname]=oidmap[keyname][oidname]['func'](data[key][keyname])
    #pprint (data)
    for item in data.values() :
        data2[item['snmpindex']] = item
    #pprint (data2)
    return data2


def GetTableMapHash(oidmap, oidname):
    #print "-----------Hello---------------"
    maphash = {}
    for key in oidmap.keys():
        #print key
        if oidname in oidmap[key]:
            #print oidname
            #print oidmap[key][oidname]['oid']
            #print oidmap[key][oidname]['field']
            if 'oid' in oidmap[key][oidname] :
                maphash[oidmap[key][oidname]['oid']] = oidmap[key][oidname]['field']
    return maphash
