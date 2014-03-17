(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.NetappAggrePanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NetappAggre',
            autoExpandColumn: 'aggrFlexvollist',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'aggrState'},
                {name: 'aggrOwners'},
                {name: 'aggrFlexvollist'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 180,
            },{
                id: 'aggrFlexvollist',
                dataIndex: 'aggrFlexvollist',
                header: _t('Member Volumes'),
                sortable: true,
            },{

                id: 'aggrOwners',
                dataIndex: 'aggrOwners',
                header: _t('Owner'),
                sortable: true,
            },{
            	 id: 'aggrState',
                 dataIndex: 'aggrState',
                 header: _t('Status'),
                 sortable: true,
                 width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.NetappAggrePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NetappAggrePanel', ZC.NetappAggrePanel);
ZC.registerName('NetappAggre', _t('Aggregate'), _t('Aggregates'));
})();