# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockScrap(models.Model):
    _inherit = "stock.scrap"

    general_notes = fields.Text(string="General Notes:")
