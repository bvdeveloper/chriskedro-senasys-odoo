# -*- coding: utf-8 -*-
from odoo import api, fields, models,_


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    additional_notes = fields.Text(related="move_id.additional_notes")
    incoterm = fields.Text(related="move_id.incoterm")
    payment_terms = fields.Char(related='move_id.payment_terms')
    senasys_division = fields.Selection(related="move_id.senasys_division")
    inv_sent_to_cus = fields.Boolean(related="move_id.inv_sent_to_cus")




