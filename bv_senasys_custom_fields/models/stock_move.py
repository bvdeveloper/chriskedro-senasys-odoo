# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    inv_location = fields.Selection(string="From", related="product_id.product_tmpl_id.inv_location")