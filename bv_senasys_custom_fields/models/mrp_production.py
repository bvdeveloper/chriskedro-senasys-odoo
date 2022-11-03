# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    confirmed_completion_date = fields.Date(string="Confirmed Comp. Date")
    mfg_order_notes_for_pdf_report = fields.Text(string="MFG Order Notes (For PDF Report)")
    trevor_notes = fields.Text(string="Notes/Status Updates")
    work_center = fields.Selection(related='bom_id.work_center_note_for_reporting')
