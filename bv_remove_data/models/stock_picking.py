# -*- coding: utf-8 -*-

from odoo import models, fields, _


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def action_remove_transfers(self):
        for pick_id in self:
            # move_line_ids = self.env['stock.move.line'].search([('picking_id', '=', pick_id.id)])
            if pick_id.move_line_ids:
                self._cr.execute('delete from stock_move_line where id in %s', [tuple(pick_id.move_line_ids.ids)])
            # move_lines = self.env['stock.move'].search([('picking_id', '=', pick_id.id)])
            if pick_id.move_lines:
                if pick_id.move_lines.stock_valuation_layer_ids:
                    self._cr.execute('delete from stock_valuation_layer where id in %s',
                                     [tuple(pick_id.move_lines.stock_valuation_layer_ids.ids)])
                self._cr.execute('delete from stock_move where id in %s', [tuple(pick_id.move_lines.ids)])
            if pick_id.id:
                self._cr.execute(f'delete from stock_picking where id = {pick_id.id}')
