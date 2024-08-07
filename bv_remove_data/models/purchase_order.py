# -*- coding: utf-8 -*-

from odoo import models, fields, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_remove_po(self):
        for po_id in self:
            po_id.state = 'purchase'
            pick_ids = po_id.mapped('picking_ids')
            if pick_ids:
                pick_ids.action_remove_transfers()

            bill_ids = po_id.mapped('invoice_ids')  # in case of bills created through odoo-bot.
            if bill_ids:
                bill_ids.action_remove_account_move()
            self._cr.commit()
            po_id.button_cancel()
            po_id.unlink()
