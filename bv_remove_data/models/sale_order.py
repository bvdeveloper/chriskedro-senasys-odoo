# -*- coding: utf-8 -*-

from odoo import fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_remove_so(self):
        for so_id in self:
            # so_id.locked = False
            pick_ids = so_id.mapped('picking_ids')
            if pick_ids:
                pick_ids.action_remove_transfers()

            invoice_ids = so_id.mapped('invoice_ids')  # Auto-generated Invoices
            if invoice_ids:
                invoice_ids.action_remove_account_move()

            po_ids = so_id._get_purchase_orders()
            if po_ids:
                po_ids.action_remove_po()

            if so_id.mrp_production_count > 0:
                manufacturing_orders = self.env['mrp.production'].search([
                    ('origin', '=', self.name)
                ])
                manufacturing_orders.action_remove_mrp_production()

            self._cr.commit()
            so_id._action_cancel()
            so_id.unlink()
