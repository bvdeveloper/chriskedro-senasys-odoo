# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class EcmSalesOrderByLineReporting(models.Model):
    _name = "ecm.sales.order.by.line.reporting"
    _description = "ECM Sales Order by line reporting"

    sequence = fields.Integer(string="Sequence")
    so_line_ids = fields.Many2many(comodel_name='sale.order.line', string="Sales Order Line")
    name = fields.Char(string='Name')

