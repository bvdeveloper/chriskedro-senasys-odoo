from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    p_contact = fields.Text(string='Portal contact')
    p_company = fields.Text(string='Portal company')
