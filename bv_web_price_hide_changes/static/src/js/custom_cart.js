odoo.define('bv_web_price_hide_changes.custom_cart', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    var ajax = require('web.ajax');
    var rpc = require('web.rpc');
    var _t = core._t;

    publicWidget.registry.CustomCartHandler = publicWidget.Widget.extend({
        selector: '.oe_cart',
        events: {
            'click .bv_cart_checkout': '_onCartCheckout',
        },
        _onCartCheckout: function () {
        var carrier_id = $('#carrier_id').val()
        ajax.jsonRpc('/shop/get/carrier', 'call', {'carrier_id':carrier_id}).then(function(data) {
        });
        },
    });

    return publicWidget.registry.CustomCartHandler;
});
