# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockWarehouseOrderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    # forecast_exc_pending = fields.Float(string="F.Cast - Exc. Pending")
    forecast_exc_pending = fields.Float(related='product_id.virtual_available', string="F.Cast - Exc. Pending")
    # our_cost_non_vendor_specific = fields.Float(string="Our Cost (Non-Vendor Specific)")
    our_cost_non_vendor_specific = fields.Float(related='product_id.standard_price',
                                                string="Our Cost (Non-Vendor Specific)")
    # target_po_level = fields.Text(string="Target PO Level")
    target_po_level = fields.Text(related='product_id.ecm_senasys_purchasing_levels', string="Target PO Level")
    # total_qty_sold = fields.Float(string="Total Qty Sold")
    total_qty_sold = fields.Float(related='product_id.sales_count', string="Total Qty Sold")
    x_studio_related_field_hlaBp = fields.Char(related="product_tmpl_id.seller_ids.name.name")
    ecm_hist_vendor = fields.Char(related="product_id.ecm_vendor", string="ECM Hist Vendor")
    x_studio_related_field_34lVd = fields.Selection(related="product_tmpl_id.inv_location", string="Location")
