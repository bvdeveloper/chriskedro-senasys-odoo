# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    order = fields.Char(related='picking_id.origin')

