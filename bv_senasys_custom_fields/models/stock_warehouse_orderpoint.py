# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockWarehouseOrderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    forecast_exc_pending = fields.Float(string="F.Cast - Exc. Pending")
    our_cost_non_vendor_specific = fields.Float(string="Our Cost (Non-Vendor Specific)")
    target_po_level = fields.Text(string="Target PO Level")
    total_qty_sold = fields.Float(string="Total Qty Sold")

