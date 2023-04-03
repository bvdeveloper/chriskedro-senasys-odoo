# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    attncontact = fields.Char(related='partner_id.attncontact')
    enter_order_specific_notes_below = fields.Char(string='Order Notes (Visible on Cust PDFs)')
    jobnametag = fields.Char(string='Cust PO# / Ref #')
    lead_time_for_quotes_only = fields.Char(string='Lead Time:')
    # order_notes_seen_on_int_reports_only = fields.Char(string='Order Notes (Seen on Int. Reports Only)')
    order_promised_ship_date = fields.Date(string='Order Promised Ship Date:')
    portal_cust_contact_method = fields.Selection(
        [('Ariba', 'Ariba - ECM'), ('Email/Phone/Other', 'Email/Phone/Other'),
         ('Ariba - Senasys', 'Ariba - Senasys')],
        string='Portal Cust. Contact Method')
    quote_closed = fields.Boolean(string='Quote Closed')
    shipping_method = fields.Selection(
        [('UPS Ground', 'UPS Ground (Prepay and Add)'),
         ('UPS 2nd Day Air', 'UPS 2nd Day Air UPS Ground (Prepay and Add)'),
         ('UPS Overnight', 'UPS Overnight (Prepay and Add)'),
         ('UPS Overnight (Early AM)', 'UPS Overnight (Early AM) - (Prepay and Add)'),
         ('FedEx Ground', 'FedEx Ground (Prepay and Add)'),
         ('FedEx 2nd Day Air', 'FedEx 2nd Day Air (Prepay and Add)'),
         ('FedEx Overnight', 'FedEx Overnight (Prepay and Add)'),
         ('LTL', 'LTL (Prepay and Add)'),
         ('USPS Economy', 'USPS Economy (Prepay and Add)'),
         ('USPS Priority', 'USPS Priority (Prepay and Add)'),
         ('USPS Overnight (Prepay and Add)', 'USPS Overnight (Prepay and Add)'),
         ('Other (See Notes)', 'Other (See Notes)'),
         ('UPS Ground (Cust. Collect)', 'UPS Ground (Cust. Collect)'),
         ('UPS 2nd Day Air (Cust. Collect)', 'UPS 2nd Day Air (Cust. Collect)'),
         ('UPS Overnight (Cust. Collect)', 'UPS Overnight (Cust. Collect)'),
         ('UPS Overnight (Early AM) - (Cust. Collect)', 'UPS Overnight (Early AM) - (Cust. Collect)'),
         ('FedEx Ground (Cust. Collect)', 'FedEx Ground (Cust. Collect)'),
         ('FedEx 2nd Day Air (Cust. Collect)', 'FedEx 2nd Day Air (Cust. Collect)'),
         ('FedEx Overnight (Cust. Collect)', 'FedEx Overnight (Cust. Collect)'),
         ('LTL (Cust. Collect)', 'LTL (Cust. Collect)'),
         ('USPS Economy (Cust. Collect)', 'USPS Economy (Cust. Collect)'),
         ('USPS Priority (Cust. Collect)', 'USPS Priority (Cust. Collect)'),
         ('USPS Overnight (Cust. Collect)', 'USPS Overnight (Cust. Collect)'), ],
        string='Shipping Method')
    shipping_collect_acct_ = fields.Char(string='Shipping Collect Acct #')
    senasys_division = fields.Char(string="Senasys Division", ondelete={'Empire Corrugated': 'set default'}, default='Empire Corrugated')
    deliv_address_default_customer_contact = fields.Char(related='partner_shipping_id.attncontact', string="Deliv. Address Default Customer Contact")
    delivery_address_for_emailing_quotesorders = fields.Char(related='partner_shipping_id.email', string="Delivery Address for Emailing Quotes/Orders")
    x_delivery_address = fields.Char(related='partner_shipping_id.name', string="Delivery Address")
