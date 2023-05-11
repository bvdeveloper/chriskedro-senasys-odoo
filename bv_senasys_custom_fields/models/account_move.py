# -*- coding: utf-8 -*-
from odoo import api, fields, models,_


class AccountMove(models.Model):
    _inherit = "account.move"

    additional_notes = fields.Text(string='Additional Notes For PDF Invoice:')
    enter_tracking_ = fields.Char(string='Enter Tracking #')
    incoterm = fields.Text(string='Custom Incoterm')
    payment_terms = fields.Char(related='partner_id.property_payment_term_id.name')
    senasys_division = fields.Char(related="invoice_line_ids.sale_line_ids.order_id.senasys_division")
    # inv_sent_to_cus = fields.Boolean(string="Inv Sent to Customer?")
    cust_po_submission_invoice_form = fields.Selection(related="invoice_line_ids.portal_cust_contact_method_3")
    pull_to_invoice = fields.Char(related="invoice_line_ids.sale_line_ids.pull_to_invoice", string="Customer_PO#:")
    x_studio_boolean_field_YoU4G = fields.Boolean(string="Inv Sent to Customer?")
    shipping_method_id = fields.Many2one("delivery.carrier", string="Shipping method")
    shipping_collect_acct = fields.Char(string='Shipping Collect Acct')
