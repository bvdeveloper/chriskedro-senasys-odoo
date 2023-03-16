# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PurchaseOrderEcmReporting(models.Model):
    _name = "x_purchase_order_ecm_r"
    _description = "Purchase Order ECM Reporting"

    po_line_ids = fields.Many2many(comodel_name='purchase.order.line', string="Purchase Order Line")
    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string='Name')
    x_studio_many2many_field_5Tw9Y = fields.Many2many(comodel_name='purchase.order',
                                                      relation='x_purchase_order_x_purchase_order_ecm_r_rel',
                                                      column1='x_purchase_order_ecm_r_id', column2='purchase_order_id')
    x_studio_many2many_field_m02vO = fields.Many2many(comodel_name='purchase.order.line',
                                                      relation='x_purchase_order_line_x_purchase_order_ecm_r_rel',
                                                      column1='x_purchase_order_ecm_r_id',
                                                      column2='purchase_order_line_id')
    x_studio_many2many_field_mmlUu = fields.Many2many(comodel_name='x_purchase_order_ecm_r',
                                                      relation='x_x_purchase_order_ecm_r_x_purchase_order_ecm_r_rel',
                                                      column1='id1', column2='id2')
    x_studio_many2many_field_SLsTW = fields.Many2many(comodel_name='purchase.order.line',
                                                      relation='x_purchase_order_line_x_purchase_order_ecm_r_rel_1',
                                                      column1='x_purchase_order_ecm_r_id',
                                                      column2='purchase_order_line_id')