# -*- coding: utf-8 -*-

import logging
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website.controllers.form import WebsiteForm
from odoo.tools.json import scriptsafe as json_scriptsafe
_logger = logging.getLogger(__name__)
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):
    @http.route(['/shop/get/carrier'], type='json', auth="public", website=True)
    def bv_confirm_order(self, **post):
        order = request.website.sale_get_order()

        # Capture custom field value from the POST request
        carrier_id = post.get('carrier_id')
        _logger.info("Custom Field Value: %s", carrier_id)
        # Save it in the sale order
        if carrier_id:
            web_cust_shipping = request.env['delivery.carrier'].sudo().browse(int(carrier_id))
            if order:
                order.update({
                    'web_cust_shipping':web_cust_shipping.name
                })
                _logger.info("Custom field saved in Sale Order ID: %s", order.id)

        return True


class CustomWebsiteForm(WebsiteForm):
    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        """This route is called when adding a product to cart (no options)."""
        sale_order = request.website.sale_get_order(force_create=True)
        if sale_order.state != 'draft':
            request.session['sale_order_id'] = None
            sale_order = request.website.sale_get_order(force_create=True)
        product_custom_attribute_values = None
        sale_order.customer_name_name = kw.get('customerName')
        sale_order.mob_mob = kw.get('customerMob')
        sale_order.email_email = kw.get('customerEmail')
        if kw.get('customerMob') and  kw.get('customerMob') and kw.get('customerEmail'):
            message_body = _('Customer name: {}\n').format( kw.get('customerName'))
            message_body += _('Mobile: {}\n').format(kw.get('customerMob'))
            message_body += _('Email: {}\n').format(kw.get('customerEmail'))
            sale_order.message_post(body=message_body)
        if kw.get('product_custom_attribute_values'):
            product_custom_attribute_values = json_scriptsafe.loads(kw.get('product_custom_attribute_values'))

        no_variant_attribute_values = None
        if kw.get('no_variant_attribute_values'):
            no_variant_attribute_values = json_scriptsafe.loads(kw.get('no_variant_attribute_values'))

        sale_order._cart_update(
            product_id=int(product_id),
            add_qty=add_qty,
            set_qty=set_qty,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_values=no_variant_attribute_values
        )

        if kw.get('express'):
            return request.redirect("/shop/checkout?express=1")

        return request.redirect("/shop/cart")

    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True, **kw):
        """
        This route is called :
            - When changing quantity from the cart.
            - When adding a product from the wishlist.
            - When adding a product to cart on the same page (without redirection).
        """
        order = request.website.sale_get_order(force_create=1)
        order.customer_name_name = kw.get('customerName')
        order.mob_mob = kw.get('customerMob')
        order.email_email = kw.get('customerEmail')
        if kw.get('customerMob') and  kw.get('customerMob') and kw.get('customerEmail'):
            message_body = _('Customer name: {}\n').format( kw.get('customerName'))
            message_body += _('Mobile: {}\n').format(kw.get('customerMob'))
            message_body += _('Email: {}\n').format(kw.get('customerEmail'))
            order.message_post(body=message_body)
        if order.state != 'draft':
            request.website.sale_reset()
            if kw.get('force_create'):
                order = request.website.sale_get_order(force_create=1)
            else:
                return {}

        pcav = kw.get('product_custom_attribute_values')
        nvav = kw.get('no_variant_attribute_values')
        value = order._cart_update(
            product_id=product_id,
            line_id=line_id,
            add_qty=add_qty,
            set_qty=set_qty,
            product_custom_attribute_values=json_scriptsafe.loads(pcav) if pcav else None,
            no_variant_attribute_values=json_scriptsafe.loads(nvav) if nvav else None
        )

        if not order.cart_quantity:
            request.website.sale_reset()
            return value

        order = request.website.sale_get_order()
        value['cart_quantity'] = order.cart_quantity

        if not display:
            return value

        value['website_sale.cart_lines'] = request.env['ir.ui.view']._render_template("website_sale.cart_lines", {
            'website_sale_order': order,
            'date': fields.Date.today(),
            'suggested_products': order._cart_accessories()
        })
        value['website_sale.short_cart_summary'] = request.env['ir.ui.view']._render_template(
            "website_sale.short_cart_summary", {
                'website_sale_order': order,
            })
        return value
