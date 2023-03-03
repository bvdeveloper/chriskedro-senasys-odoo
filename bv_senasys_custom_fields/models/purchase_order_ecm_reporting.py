# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PurchaseOrderEcmReporting(models.Model):
    _name = "purchase.order.ecm.reporting"
    _description = "Purchase Order ECM Reporting"

    po_line_ids = fields.Many2many(comodel_name='purchase.order.line', string="Purchase Order Line")
    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string='Name')
