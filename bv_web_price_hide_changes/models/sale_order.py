# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        # Check if shopify_instance_id is in vals
        if 'web_cust_shipping' in vals and not self.web_cust_mail_sent:
            view_context = {}
            view_context.update({
                'sale': self.name,
                'cus_name': self.customer_name_name,
                'cus_mob': self.mob_mob,
                'cus_email': self.email_email
            })
            # Send email using template
            template = self.env.ref('bv_web_price_hide_changes.email_template_public_user_quotation')
            template.with_context(**view_context).sudo().send_mail(self.id, force_send=True)
            self.web_cust_mail_sent = True
        return res