# -*- coding: utf-8 -*-
from odoo import api, fields, models,_


class ProductProduct(models.Model):
    _inherit = "mrp.bom"

    process_notes = fields.Text(string="Process Notes")
    product_description = fields.Text(string="Product Description")
    work_center_note_for_reporting = fields.Selection([('Senasys Machine Shop', 'Senasys Machine Shop'),
                                                        ('Order Assembly (Kits, Sets, etc)', 'Order Assembly (Kits, Sets, etc)'),
                                                        ('3rd Party - Kreicko, Ed-K, etc', '3rd Party - Kreicko, Ed-K, etc')], string="Work Center Note (For Reporting)")
    description = fields.Char(related="product_tmpl_id.description")
