# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    attncontact = fields.Char(related='partner_id.attncontact')
    enter_order_specific_notes_below = fields.Char(string='Order Notes (Visible on Cust PDFs)')
    jobnametag = fields.Char(string='Cust PO# / Ref #')
    lead_time_for_quotes_only = fields.Char(string='Lead Time:')
    order_notes_seen_on_int_reports_only = fields.Char(string='Order Notes (Seen on Int. Reports Only)')
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
    cust_shipping_preference = fields.Selection(related='partner_id.cust_shipping_preference', string='Cust. Shipping Preference',store=True)
    requested_delivery_Date = fields.Date(string="Requested Delivery Date")
    customer_name_name = fields.Char(string="Customer name")
    email_email = fields.Char(string="Email")
    mob_mob = fields.Char(string="Mobile")

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super().onchange_partner_id()
        payment_term = self.partner_invoice_id.property_payment_term_id.id if self.partner_invoice_id.property_payment_term_id else self.partner_id.property_payment_term_id.id
        carrier = self.partner_id.property_delivery_carrier_id.id if self.partner_id.property_delivery_carrier_id else False
        account = self.partner_id.carrier_account_number if self.partner_id.carrier_account_number else False
        values = {
            'payment_term_id': payment_term,
            'carrier_id': carrier,
            'shipping_collect_acct_': account
        }
        self.update(values)

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        picking = self.env['stock.picking'].search([('sale_id.id', '=', self.id)])
        if picking:
            picking.carrier_id = self.carrier_id and self.carrier_id.id or False
            picking.cust_collect_acct = self.shipping_collect_acct_
        return True

    @api.depends('order_line.invoice_lines')
    def _get_invoiced(self):
        super(SaleOrder, self)._get_invoiced()
        for order in self:
            invoices = order.order_line.invoice_lines.move_id.filtered(
                lambda r: r.move_type in ('out_invoice', 'out_refund') and (not r.shipping_method_id or not r.shipping_collect_acct ))
            for inv in invoices:
                inv.shipping_collect_acct = order.shipping_collect_acct_
                inv.shipping_method_id = order.carrier_id.id if order.carrier_id else False
