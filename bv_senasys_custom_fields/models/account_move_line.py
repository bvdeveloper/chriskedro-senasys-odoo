# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    line_item_from_sales_order_entry = fields.Char(string='Line #')
    po_ = fields.Char(string='Cust PO #')
    portal_cust_contact_method_3 = fields.Selection(related='sale_line_ids.portal_cust_pull_to_invoice', string='Portal cust contact method 3')
    name_short = fields.Char(related='sale_line_ids.name_short', string='Part#')
    p_description = fields.Char(related='product_id.default_code', string='Description')
    bill_price_unit = fields.Float(string='Unit Price', digits='Unit Price')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        super()._onchange_product_id()
        for line in self:
            line.bill_price_unit = line._get_computed_price_unit()

    @api.onchange('bill_price_unit')
    def _onchange_bill_price_unit(self):
        for line in self:
            line.price_unit = line.bill_price_unit
