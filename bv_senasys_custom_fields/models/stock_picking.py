# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    x_studio_related_field_He86r = fields.Selection(string='Initial/1st Shipment Method:', related='sale_id.shipping_method')
    override_shipment_method = fields.Selection([('Yes', 'Yes'), ('No', 'No')], string='Override Shipment Method')
    ship_method_for_this_delivery = fields.Selection([('UPS Ground (Prepay and Add)', 'UPS Ground (Prepay and Add)'),
                                                      ('UPS 2nd Day Air UPS Ground (Prepay and Add)',
                                                       'UPS 2nd Day Air UPS Ground (Prepay and Add)'),
                                                      ('UPS Overnight (Prepay and Add)',
                                                      'UPS Overnight (Prepay and Add)'),
                                                      ('UPS Overnight (Early AM) - (Prepay and Add)',
                                                      'UPS Overnight (Early AM) - (Prepay and Add)'),
                                                      ('FedEx Ground (Prepay and Add)', 'FedEx Ground (Prepay and Add)'),
                                                      ('FedEx 2nd Day Air (Prepay and Add)', 'FedEx 2nd Day Air (Prepay and Add)')],
                                                     string='Ship. Method For this Delivery')
    cust_collect_acct = fields.Char(string='Cust. Collect Acct:')
    po_tag_ = fields.Char(string='PO# / Ref#:', related="sale_id.jobnametag")
    shipment_delivery_notes = fields.Text(string='Shipment Delivery Notes:')
    x_studio_related_field_lWIty = fields.Selection(string='Senasys Division', related="sale_id.senasys_division")
    x_studio_related_field_Pl4hB = fields.Char(related='sale_id.attncontact', string='Attn/Contact')
    order_promised_ship_date = fields.Date(string='Order Promised Ship Date:', related="sale_id.order_promised_ship_date")



