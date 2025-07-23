# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductSuppierinfo(models.Model):
    _inherit = "product.supplierinfo"

    vendor_spec_part_notes = fields.Char(string='Vendor Spec. Part# Notes')
    price = fields.Float(
        'Price', default=0.0, digits='Unit Price',
        required=True, help="The price to purchase a product")


