# -*- coding: utf-8 -*-
from string import digits

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    line_item_number = fields.Char(string='Line#')
    pull_to_invoice = fields.Char(related='order_id.jobnametag')
    x_studio_related_field_Af1vN = fields.Float(related='product_id.free_qty')
    x_studio_related_field_Rpv4q = fields.Float(related='product_id.qty_available')
    portal_cust_contact_method_2 = fields.Char(string='Portal Cust Contact Method 2')
    portal_cust_pull_to_invoice = fields.Selection(related='order_id.portal_cust_contact_method')
    inv_loc = fields.Selection(related='product_id.inv_location')
    name_short = fields.Char(string="Name Short")
    price_subtotal_rounded = fields.Float(string="Subtotal", compute="_compute_price_subtotal_rounded", store=True)

    @api.depends("price_subtotal")
    def _compute_price_subtotal_rounded(self):
        for line in self:
            line.price_subtotal_rounded = "%.2f" % line.price_subtotal


