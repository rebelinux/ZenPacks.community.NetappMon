/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');


/*
 * Friendly names for the components. First parameter is the meta_type in your
 * custom component class. Second parameter is the singular form of the
 * friendly name to be displayed in the UI. Third parameter is the plural form.
 */
ZC.registerName('NetappAggre', _t('Aggregate'), _t('Aggregates'));


/*
 * Custom component grid panel. This controls the grid that gets displayed for
 * components of the type set in "componenType".
 */
Ext.define('Zenoss.component.NetappAggreGridPanel',{
    extend: 'Zenoss.component.ComponentGridPanel',
    subComponentGridPanel: false,

    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NetappAggre',
            alias:['widget.NetappAggreGridPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'aggrname'},
                {name: 'aggrState'},
                {name: 'aggrRaidType'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                flex: 1,
                dataIndex: 'aggrname',
                header: _t('Name')
            },{
                id: 'aggrState',
                dataIndex: 'aggrState',
                header: _t('Status'),
                sortable: true,
                width: 70
            },{
                id: 'aggrRaidType',
                dataIndex: 'aggrRaidType',
                header: _t('Attribute #2'),
                sortable: true,
                width: 70
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        this.callParent([config]);
    }
});


})();
