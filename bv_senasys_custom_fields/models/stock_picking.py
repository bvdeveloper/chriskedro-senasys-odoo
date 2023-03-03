# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    initial_first_shipment = fields.Selection(string='Initial/1st Shipment Method:', related='sale_id.shipping_method')
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
    po_tag_ = fields.Char(string='PO# / Ref#:')
    shipment_delivery_notes = fields.Text(string='Shipment Delivery Notes:')
    senasys_division = fields.Selection(related="sale_id.senasys_division")
    attncontact = fields.Char(related='sale_id.attncontact')



