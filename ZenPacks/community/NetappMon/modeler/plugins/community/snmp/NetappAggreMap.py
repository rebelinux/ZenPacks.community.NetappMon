from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
import binascii, re
class NetappAggreMap(SnmpPlugin):
    """Map class NetappAggreMap to model."""
    maptype = "NetappAggreMap"
    modname = "ZenPacks.community.NetappMon.NetappAggreMap"
    relname = "NetappAggreMap"
    

    snmpGetTableMaps = (
        GetTableMap('aggre',
        '.1.3.6.1',
                    {
                        '.4.1.789.1.5.11.1.1.0': 'aggreindex',
                        '.4.1.789.1.5.11.1.2': 'aggrname',
                        '.4.1.789.1.5.11.1.5': 'aggrState',
                        '.4.1.789.1.5.11.1.10': 'aggrRaidType',
                        '.4.1.789.1.5.11.1.13': 'aggrOwners',
                        '.4.1.789.1.5.11.1.9' : 'aggrFlexvollist',
                        '.4.1.789.1.5.11.1.7': 'aggrOptions',
                        }
                    ),
    )
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        aggres = tabledata.get("aggre")
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not aggres:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        for oid, data in aggres.iteritems():
            try:
                om = self.objectMap(data)
                om.id = self.prepId(om.aggrname)
                om.snmpindex = om.aggreindex
            except AttributeError:
                continue
            rm.append(om)
        return rm
