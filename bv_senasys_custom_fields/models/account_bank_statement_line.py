# -*- coding: utf-8 -*-
from odoo import api, fields, models,_


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    additional_notes = fields.Text(related="move_id.additional_notes")
    incoterm = fields.Text(related="move_id.incoterm")
    payment_terms = fields.Char(related='move_id.payment_terms')
    senasys_division = fields.Char(related="move_id.senasys_division")
    # inv_sent_to_cus = fields.Boolean(related="move_id.inv_sent_to_cus")
    x_studio_boolean_field_YoU4G = fields.Boolean(related="move_id.x_studio_boolean_field_YoU4G")
    cust_po_submission_invoice_form = fields.Selection(related="move_id.cust_po_submission_invoice_form")
    pull_to_invoice = fields.Char(related="move_id.pull_to_invoice")




