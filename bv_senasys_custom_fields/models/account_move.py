# -*- coding: utf-8 -*-
from odoo import api, fields, models,_


class AccountMove(models.Model):
    _inherit = "account.move"

    additional_notes = fields.Text(string='Additional Notes For PDF Invoice:')
    enter_tracking_ = fields.Char(string='Enter Tracking #')
    incoterm = fields.Text(string='Custom Incoterm')
    payment_terms = fields.Char(related='partner_id.sale_order_ids.partner_id.property_payment_term_id.name')
    senasys_division = fields.Selection(related="partner_id.sale_order_ids.senasys_division")
    # inv_sent_to_cus = fields.Boolean(string="Inv Sent to Customer?")


