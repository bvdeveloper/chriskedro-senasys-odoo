# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    drop_ship_to_vendor = fields.Many2one(comodel_name='res.partner', string='Drop Ship Address (Autofill):')
    po_notes = fields.Text(string='P.O. Notes: (Visible on PO)')
    po_notes_internal_use_only = fields.Char(string='P.O. Notes: (Internal Use Only)')
    purchase_order_closed = fields.Boolean(string='Purchase Order Closed')
    # reconciled_by = fields.Selection(
    #     [('Jess', 'Jess'), ('Kayla', 'Kayla'), ('Chris (credit card)', 'Chris (credit card)')], string='Reconciled By:')
    request_date = fields.Date(
        string='Request Date (Enter based on standard lead time if known, otherwise leave blank and SELECT TBD BELOW)')
    requested_delivery_method = fields.Selection(
        [('Standard / Economy', 'UPS Ground'), ('UPS 2nd Day Air', 'UPS 2nd Day Air'),
         ('Expedited', 'UPS Overnight'), ('UPS Overnight (Early AM)', 'UPS Overnight (Early AM)'), ('LTL', 'LTL')],
        string='Requested Delivery Method:')
    select_ = fields.Selection(
        [('Use Request Date Above', 'Use Request Date Above'), ('TBD (As soon as possible)', 'TBD (As soon as possible)')], string='Select:')
    senasys_buyer = fields.Char(string='Senasys Buyer:')
    vendor_drop_ship_enter_address_below = fields.Selection(
        [('Yes', 'Yes'), ('No', 'No')], string='Vendor Drop Ship?')
    senasys_division = fields.Selection([('Empire Corrugated', 'Empire Corrugated'), ('Wahl', 'Wahl')], string="Senasys Division")



