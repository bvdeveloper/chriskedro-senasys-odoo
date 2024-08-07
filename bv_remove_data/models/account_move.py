# -*- coding: utf-8 -*-

from odoo import models, fields, _


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_remove_account_move(self):
        # invoice_ids = self.env['account.move'].search([('create_uid', 'in', [2, 246, 266, 268])])
        invoice_ids = self.line_ids._reconciled_lines()
        invoice_ids = self.env['account.move.line'].browse(invoice_ids).filtered(
            lambda l: l.matched_debit_ids or l.matched_credit_ids).mapped("move_id")
        invoice_ids |= self
        for invoice_id in invoice_ids:
            if invoice_id.line_ids:
                if invoice_id.line_ids.matched_debit_ids:
                    self._cr.execute('delete from account_partial_reconcile where id in %s',
                                     [tuple(invoice_id.line_ids.matched_debit_ids.ids)])
                if invoice_id.line_ids.matched_credit_ids:
                    self._cr.execute('delete from account_partial_reconcile where id in %s',
                                     [tuple(invoice_id.line_ids.matched_credit_ids.ids)])
                self._cr.execute('delete from account_move_line where id in %s', [tuple(invoice_id.line_ids.ids)])
            self._cr.execute(f'delete from account_move where id = {invoice_id.id}')
