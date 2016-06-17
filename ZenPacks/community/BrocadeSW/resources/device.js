Ext.onReady(function() {
    var DEVICE_OVERVIEW_ID = 'deviceoverviewpanel_summary';
    Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_ID, function(){
        var overview = Ext.getCmp(DEVICE_OVERVIEW_ID);
        overview.removeField('memory');

        overview.addField({
            name: 'firmwareversion',
            fieldLabel: _t('FirmwareVersion')
        });
    });

});

Ext.apply(Zenoss.render, {
    FCPort_OpStatus: function(n) {
        var status = n,
            tpl = new Ext.Template(
                '<font color={color}>{text}</font>'
            ),
        result = '';
        tpl.compile();
        switch (status) {
            case 'online':
                result += tpl.apply({color:"green",text:status});
                break;
            case 'offline':
                result += tpl.apply({color:'grey',text:status});
                break;
            default:
                result += tpl.apply({color:'red',text:status});
        }
        return result;
    },
    FCPort_Speed: function(n) {
        return n+' Gbps';
    }
});
