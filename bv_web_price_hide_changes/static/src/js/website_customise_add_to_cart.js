
odoo.define('bv_web_price_hide_changes.custom_website_sale', function (require) {
    'use strict';
    var core = require('web.core');
    var config = require('web.config');
    var publicWidget = require('web.public.widget');
    var VariantMixin = require('website_sale.VariantMixin');
    var wSaleUtils = require('website_sale.utils');
    const cartHandlerMixin = wSaleUtils.cartHandlerMixin;
    require("web.zoomodoo");
    const {extraMenuUpdateCallbacks} = require('website.content.menu');
    const dom = require('web.dom');
    var _t = core._t;
    publicWidget.registry.WebsiteSale.include({
        _handleAdd: function ($form) {
        var self = this;
        this.$form = $form;
        var customerName = $("#customerName").val();
        var customerEmail = $("#customerEmail").val();
        var customerMob = $("#customerMob").val();
        var productSelector = [
            'input[type="hidden"][name="product_id"]',
            'input[type="radio"][name="product_id"]:checked'
        ];

        if (customerName === '' || customerEmail === '' || customerMob === '') {
            alert(_t("Please fill in your name, email, and mobile number."));
            return $.Deferred().reject();
        }

        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(customerEmail)) {
            alert(_t("Please enter a valid email address."));
            return $.Deferred().reject();
        }

       if (!/^\d{10}$/.test(customerMob)) {
            alert(_t("Mobile number should be 10 digits."));
            return $.Deferred().reject();
        }

        var productReady = this.selectOrCreateProduct(
            $form,
            parseInt($form.find(productSelector.join(', ')).first().val(), 10),
            $form.find('.product_template_id').val(),
            false
        );

        return productReady.then(function (productId) {
            $form.find(productSelector.join(', ')).val(productId);
            self.rootProduct = {
                product_id: productId,
                quantity: parseFloat($form.find('input[name="add_qty"]').val() || 1),
                product_custom_attribute_values: self.getCustomVariantValues($form.find('.js_product')),
                variant_values: self.getSelectedVariantValues($form.find('.js_product')),
                no_variant_attribute_values: self.getNoVariantAttributeValues($form.find('.js_product')),
                customerName: customerName,
                customerEmail:customerEmail,
                customerMob:customerMob
            };
            return self._onProductReady();
        });
    },
});
});

