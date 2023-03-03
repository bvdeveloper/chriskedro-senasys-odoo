# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    line_item_from_sales_order_entry = fields.Char(string='Line #')
    po_ = fields.Char(string='Cust PO #')

