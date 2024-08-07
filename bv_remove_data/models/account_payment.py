# -*- coding: utf-8 -*-

from odoo import models, fields, _


class AccountPayment(models.Model):
    _inherit = "account.payment"

    def action_remove_payments(self):
        # payment_ids = self.env['account.payment'].search([('create_uid', 'in', [2, 246, 266, 268])])
        for payment_id in self:
            payment_id.filtered(lambda p: p.state != 'draft').action_draft()
            payment_id.unlink()
            # payment_id.action_cancel()
        # If we are going to delete through query then need to remove journal entries
        # self._cr.execute('delete from account_payment where id in %s', [tuple(self.ids)])
