# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    line_item_number = fields.Char(string='Line#')
    pull_to_invoice = fields.Char(string='PO#_Pull_To_Invoice')
    free_2_sell = fields.Float(related='product_id.free_qty')
    on_hand = fields.Float(related='product_id.qty_available')