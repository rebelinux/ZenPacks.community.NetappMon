from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

# Classes we'll need for returning proper results from our modeler plugin's
# process method.
from Products.DataCollector.plugins.DataMaps import ObjectMap


class NetappDevice(SnmpPlugin):
    """Map mib elements from Nortel mib to get hw and os products.
    """

    maptype = "NetappDevice"

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.789.1.1.9' : 'setHWSerialNumber',
        '.1.3.6.1.4.1.789.1.1.5' : 'setHWProductKey',
        '.1.3.6.1.4.1.789.1.1.2' : 'setOSProductKey',
        })



    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        if getdata['setHWProductKey'] is None: return None
        if getdata['setOSProductKey'] is None: return None
        om = self.objectMap(getdata)
        om.setOSProductKey = om.setOSProductKey
        om.setHWProductKey = MultiArgs(om.setHWProductKey, "Netapp")
        om.setOSProductKey = MultiArgs(om.setOSProductKey, "Netapp")
        return om
