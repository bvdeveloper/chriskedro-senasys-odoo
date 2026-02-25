# -*- coding: utf-8 -*-
import base64
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    drop_ship_to_vendor = fields.Many2many(comodel_name='res.partner', string='Drop Ship Address (Autofill):')
    po_notes = fields.Text(string='P.O. Notes: (Visible on PO)')
    po_notes_internal_use_only = fields.Char(string='P.O. Notes: (Internal Use Only)')
    purchase_order_closed = fields.Boolean(string='Purchase Order Closed')
    # reconciled_by = fields.Selection(
    #     [('Jess', 'Jess'), ('Kayla', 'Kayla'), ('Chris (credit card)', 'Chris (credit card)')], string='Reconciled By:')
    request_date = fields.Date(
        string='Requested Ship Date (Enter based on standard lead time if known, otherwise leave blank and SELECT TBD BELOW)')
    requested_delivery_method = fields.Selection(
        [('Standard / Economy', 'UPS Ground'), ('UPS 2nd Day Air', 'UPS 2nd Day Air'),
         ('Expedited', 'UPS Overnight'), ('UPS Overnight (Early AM)', 'UPS Overnight (Early AM)'), ('LTL', 'LTL')],
        string='Requested Delivery Method:')
    select_ = fields.Selection(
        [('Use Request Date Above', 'Use Request Date Above'), ('TBD (As soon as possible)', 'TBD (As soon as possible)')], string='Select:')
    senasys_buyer = fields.Char(string='Senasys Buyer:')
    vendor_drop_ship_enter_address_below = fields.Selection(
        [('Yes', 'Yes'), ('No', 'No')], string='Vendor Drop Ship?')
    senasys_division = fields.Char(string="Senasys Division", ondelete={'Empire Corrugated': 'set default'}, default='Empire Corrugated')
    dedicated_ecm_contact = fields.Char(related='partner_id.attncontact', string='Dedicated ECM Contact:')
    po_drawing_attach = fields.Binary(string='Attach Drawing')
    show_mail_po_warning = fields.Boolean(string='Mail Warning',related='partner_id.show_mail_po_warning')
    
    @api.depends('order_line.date_planned')
    def _compute_date_planned(self):
        """
        Override
        """
        for order in self:
            if not order.date_planned:
                order.date_planned = False

    def _get_rfq_product_attachments(self):
        """
        Build attachments for RFQ email: per product on order lines,
        create a revision note TXT (drawing_revision value) and attach pdf_1_1.
        Returns list of ir.attachment ids (temporary, res_model=mail.compose.message, res_id=0).
        """
        self.ensure_one()
        Attachment = self.env['ir.attachment']
        attachment_ids = []
        seen_products = set()
        for line in self.order_line:
            if line.display_type or not line.product_id:
                continue
            product = line.product_id
            if product.id in seen_products:
                continue
            seen_products.add(product.id)
            # Safe filename base from product
            part_name = (product.default_code or product.name or 'product').replace('/', '-').replace('\\', '-')[:50]
            # 1. Revision note TXT per product
            revision_text = (product.drawing_revision or '').strip()
            if revision_text:
                revision_content = revision_text.encode('utf-8')
                revision_attach = Attachment.create({
                    'name': 'revision_note_%s.txt' % part_name,
                    'datas': base64.b64encode(revision_content),
                    'res_model': 'mail.compose.message',
                    'res_id': 0,
                    'type': 'binary',
                })
                attachment_ids.append(revision_attach.id)
            # 2. PDF pdf_1_1 per product if present
            if product.pdf_1_1:
                pdf_name = product.pdf_1_1_filename or ('drawing_%s.pdf' % part_name)
                if not pdf_name.lower().endswith('.pdf'):
                    pdf_name += '.pdf'
                pdf_attach = Attachment.create({
                    'name': pdf_name,
                    'datas': product.pdf_1_1,
                    'res_model': 'mail.compose.message',
                    'res_id': 0,
                    'type': 'binary',
                })
                attachment_ids.append(pdf_attach.id)
        return attachment_ids

    def action_rfq_send(self):
        """Override to attach product pdf_1_1 and revision note TXT per product (RFQ and PO email)."""
        self.ensure_one()
        extra_attachment_ids = self._get_rfq_product_attachments()
        if extra_attachment_ids:
            ctx = dict(self.env.context)
            ctx['default_attachment_ids'] = extra_attachment_ids
            self = self.with_context(ctx)
        return super(PurchaseOrder, self).action_rfq_send()


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    inv_loc = fields.Selection(related='product_id.inv_location')
    price_unit = fields.Float(digits='Unit Price')

    def _prepare_account_move_line(self, move=False):
        """Override to ensure bill_price_unit is properly set when creating vendor bills"""
        res = super()._prepare_account_move_line(move)
        
        # Set the bill_price_unit to the same value as price_unit from purchase order
        if res.get('price_unit'):
            res['bill_price_unit'] = res['price_unit']
        
        return res

