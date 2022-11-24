from odoo import fields, models
from odoo.http import request


class Website(models.Model):
    _inherit = "website"

    website_sale_checkout_skip_message = fields.Text(
        string="Website Sale SKip Message",
        required=True,
        default="Our team will check your order and send you payment information soon.",
    )
    checkout_skip_payment = fields.Boolean(default=True)