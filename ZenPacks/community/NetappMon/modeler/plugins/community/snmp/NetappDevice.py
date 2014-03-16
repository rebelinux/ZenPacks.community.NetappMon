from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
import re

class NetappDevice(SnmpPlugin):
    """Map mib elements from Netapp mib to get hw and os products.
    """

    maptype = "NetappDevice"

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.789.1.1.9.0' : 'setHWSerialNumber',
        '.1.3.6.1.4.1.789.1.1.5.0' : 'setHWProductKey',
        '.1.3.6.1.4.1.789.1.1.2.0' : 'setOSProductKey',
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
