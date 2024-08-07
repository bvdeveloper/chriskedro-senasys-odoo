# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class MRPProduction(models.Model):
    _inherit = "mrp.production"

    def action_remove_mrp_production(self):
        for mrp in self:
            if mrp.picking_ids:
                mrp.picking_ids.action_remove_transfers()

            move_lines = set()
            move_line_ids = set()
            stock_valuation_layer_ids = set()
            for move_type in ['move_raw_ids', 'move_dest_ids', 'move_finished_ids']:
                mrp_records = getattr(mrp, move_type)
                if mrp_records:
                    move_lines.update(mrp_records.ids)
                    move_line_ids.update(mrp_records.mapped('move_line_ids').ids)
                    stock_valuation_layer_ids.update(mrp_records.mapped('stock_valuation_layer_ids').ids)
                if move_type in ['move_raw_ids', 'move_finished_ids'] and mrp.workorder_ids:
                    wo_records = getattr(mrp.workorder_ids, move_type)
                    move_lines.update(wo_records.ids)
                    move_line_ids.update(wo_records.mapped('move_line_ids').ids)
                    stock_valuation_layer_ids.update(wo_records.mapped('stock_valuation_layer_ids').ids)

            for field_name in ['finished_move_line_ids', 'move_raw_line_ids', 'move_byproduct_line_ids']:
                move_line_records = getattr(mrp, field_name)
                if move_line_records:
                    move_line_ids.update(move_line_records.ids)

            move_lines = list(move_lines)
            move_line_ids = list(move_line_ids)
            stock_valuation_layer_ids = list(stock_valuation_layer_ids)
            if move_line_ids:
                self._cr.execute('delete from stock_move_line where id in %s', [tuple(move_line_ids)])
            if stock_valuation_layer_ids:
                self._cr.execute('delete from stock_valuation_layer where id in %s', [tuple(stock_valuation_layer_ids)])
            if move_lines:
                self._cr.execute('delete from stock_move where id in %s', [tuple(move_lines)])

            if mrp.workorder_ids:
                if mrp.workorder_ids.check_ids:
                    self._cr.execute('delete from quality_check where id in %s',
                                     [tuple(mrp.workorder_ids.mapped("check_ids").ids)])
                if mrp.workorder_ids.time_ids:
                    self._cr.execute('delete from mrp_workcenter_productivity where id in %s',
                                     [tuple(mrp.workorder_ids.mapped("time_ids").ids)])
                mrp.workorder_ids.state = 'cancel'
                self._cr.execute('delete from mrp_workorder where id in %s',
                                 [tuple(mrp.mapped("workorder_ids").ids)])
            self._cr.execute(f'delete from mrp_production where id = {mrp.id}')
