from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Globals import InitializeClass


class NetappAggre(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "NetappAggre"

    aggrname = ''
    aggrState = ''
    aggrRaidType = ''
    aggrOwners = ''
    aggrFlexvollist = ''
    aggrOptions = ''
    
    
    _properties = ManagedEntity._properties + (
        {'id': 'aggrname', 'type': 'string', 'mode': ''},
        {'id': 'aggrState', 'type': 'string', 'mode': ''},
        {'id': 'aggrRaidType', 'type': 'string', 'mode': ''},
        {'id': 'aggrOwners', 'type': 'string', 'mode': ''},
        {'id': 'aggrFlexvollist', 'type': 'string', 'mode': ''},
        {'id': 'aggrOptions', 'type': 'string', 'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('NetappDevAggre', ToOne(ToManyCont,
            'ZenPacks.community.NetappMon.NetappDevice',
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
    def viewName(self):
        """Pretty version human readable version of this object"""
        return self.id

    titleOrId = name = viewName


    def device(self):
        return self.NortelDevPower()

    def manage_deleteComponent(self, REQUEST=None):
        """Delete NetappAggre component takes from Jane Curry"""
        url = None
        if REQUEST is not None:
            url = self.device().NetappAggre.absolute_url()
        self.getPrimaryParent()._delObject(self.id)

        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(url)

    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates
    
InitializeClass(NetappAggre)
