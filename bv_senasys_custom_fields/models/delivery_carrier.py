# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    has_account_number = fields.Boolean("Has Account number")
