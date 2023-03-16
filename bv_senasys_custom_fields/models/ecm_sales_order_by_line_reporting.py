# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class EcmSalesOrderByLineReporting(models.Model):
    _name = "x_ecm_sales_order_by_l"
    _description = "ECM Sales Order by line reporting"

    sequence = fields.Integer(string="Sequence")
    so_line_ids = fields.Many2many(comodel_name='sale.order.line', string="Sales Order Line")
    name = fields.Char(string='Name')
    x_studio_many2many_field_mbdK2 = fields.Many2many(comodel_name='sale.order.line',
                                                      relation='x_sale_order_line_x_ecm_sales_order_by_l_rel',
                                                      column1='x_ecm_sales_order_by_l_id', column2='sale_order_line_id')


class InvoiceLinesExport(models.Model):
    _name = "invoice.lines.export"
    _description = "Invoice Lines Export (Comm)"

    sequence = fields.Integer(string="Sequence")


class TestCommExport(models.Model):
    _name = "test.comm.export"
    _description = "Test - Comm Export"

    sequence = fields.Integer(string="Sequence")
