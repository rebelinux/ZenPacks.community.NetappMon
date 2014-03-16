from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class NetappAggre(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "NetappAggre"

    name = ''

    _properties = ManagedEntity._properties + (
        {'id': 'name', 'type': 'string', 'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('NetappDevice', ToOne(ToManyCont,
            'ZenPacks.community.NetappMon.NetappAggre',
            'NetappAggre',
            ),
        ),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'NetappAggre',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
        },),
    },)

    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    def device(self):
        return self.NetappDevice()
