# -*- coding: utf-8 -*-
from odoo import api, models


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    def _merge_purchase_order_attachments(self, attachment_ids_value):
        """Extract list of ids from attachment_ids (ids or command list), merge with PO product attachments."""
        current_ids = []
        if attachment_ids_value and isinstance(attachment_ids_value, list):
            if attachment_ids_value and isinstance(attachment_ids_value[0], (list, tuple)):
                for cmd in attachment_ids_value:
                    if len(cmd) >= 3 and cmd[0] == 6:  # REPLACE
                        current_ids = list(cmd[2]) if cmd[2] else []
                        break
            else:
                current_ids = list(attachment_ids_value)
        return current_ids

    @api.model
    def default_get(self, fields):
        result = super().default_get(fields)
        if 'attachment_ids' not in fields:
            return result
        model = result.get('model') or self._context.get('default_model') or self._context.get('active_model')
        res_id = result.get('res_id') or self._context.get('default_res_id') or self._context.get('active_id')
        if model == 'purchase.order' and res_id:
            order = self.env['purchase.order'].browse(res_id)
            if order.exists():
                extra_ids = order._get_rfq_product_attachments()
                if extra_ids:
                    current_ids = self._merge_purchase_order_attachments(result.get('attachment_ids'))
                    seen = set(current_ids)
                    for aid in extra_ids:
                        if aid not in seen:
                            current_ids.append(aid)
                            seen.add(aid)
                    result['attachment_ids'] = [(6, 0, current_ids)]
        return result

    def _onchange_template_id(self, template_id, composition_mode, model, res_id):
        result = super()._onchange_template_id(template_id, composition_mode, model, res_id)
        if model == 'purchase.order' and res_id and result.get('value'):
            order = self.env['purchase.order'].browse(res_id)
            if order.exists():
                extra_ids = order._get_rfq_product_attachments()
                if extra_ids:
                    value = result['value']
                    current_ids = self._merge_purchase_order_attachments(value.get('attachment_ids'))
                    seen = set(current_ids)
                    for aid in extra_ids:
                        if aid not in seen:
                            current_ids.append(aid)
                            seen.add(aid)
                    value['attachment_ids'] = [(6, 0, current_ids)]
        return result
