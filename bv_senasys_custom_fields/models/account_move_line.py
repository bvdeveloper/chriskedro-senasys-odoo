# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    line_item_from_sales_order_entry = fields.Char(string='Line #')
    po_ = fields.Char(string='Cust PO #')
    portal_cust_contact_method_3 = fields.Selection(related='sale_line_ids.portal_cust_pull_to_invoice', string='Portal cust contact method 3')
    name_short = fields.Char(related='sale_line_ids.name_short', string='Part#')
    p_description = fields.Char(related='product_id.default_code', string='Description')
