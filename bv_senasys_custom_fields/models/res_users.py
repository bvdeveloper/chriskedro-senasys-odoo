# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    add_catalog_price_lists = fields.Selection(related='partner_id.add_catalog_price_lists')
    add_relevant_photos_below = fields.Char(related='partner_id.add_relevant_photos_below')
    attncontact = fields.Char(related='partner_id.attncontact')
    catalog_notes_date_etc = fields.Text(related='partner_id.catalog_notes_date_etc')
    cc_email_field = fields.Char(related='partner_id.cc_email_field')
    cust_shipping_preference = fields.Selection(related='partner_id.cust_shipping_preference')
    customer_notes = fields.Text(related='partner_id.customer_notes')
    fax_ = fields.Char(related='partner_id.fax_')
    image_1 = fields.Binary(related="partner_id.image_1")
    image_1_notes = fields.Char(related="partner_id.image_1_notes")
    image_2 = fields.Binary(related="partner_id.image_2")
    image_2_notes = fields.Char(related="partner_id.image_2_notes")
    image_3 = fields.Binary(related="partner_id.image_3")
    image_3_notes = fields.Char(related="partner_id.image_3_notes")
    image_4 = fields.Binary(related="partner_id.image_4")
    image_4_notes = fields.Char(related="partner_id.image_4_notes")
    include_docs = fields.Selection(related="partner_id.include_docs")
    include_photos = fields.Selection(related="partner_id.include_photos")
    internal_report_order_notes = fields.Text(related='partner_id.internal_report_order_notes')
    last_updated_notes = fields.Char(related='partner_id.last_updated_notes')
    last_updated_notes_1 = fields.Char(related='partner_id.last_updated_notes_1')
    last_updated_notes_2 = fields.Char(related='partner_id.last_updated_notes_2')
    notesinstructions = fields.Text(related='partner_id.notesinstructions')
    ordering_rulesinstructions = fields.Text(related='partner_id.ordering_rulesinstructions')
    password = fields.Char(related='partner_id.password')
    portal_url = fields.Text(related='partner_id.portal_url')
    portal_website_url = fields.Char(related='partner_id.portal_website_url')
    price_list_pdf = fields.Binary(related='partner_id.price_list_pdf')
    price_list_pdf_filename = fields.Char(related='partner_id.price_list_pdf_filename')
    record_verified = fields.Selection(related='partner_id.record_verified')
    tech_cad_drawings = fields.Binary(related='partner_id.tech_cad_drawings')
    tech_cad_drawings_filename = fields.Char(related='partner_id.tech_cad_drawings_filename')
    type = fields.Selection(related='partner_id.type')
    typical_item_types_purchased = fields.Text(related='partner_id.typical_item_types_purchased')
    typical_items_types_purchased_for_ecm = fields.Text(related='partner_id.typical_items_types_purchased_for_ecm')
    typical_items_types_purchased_for_ecm_1 = fields.Text(related='partner_id.typical_items_types_purchased_for_ecm_1')
    username = fields.Char(related='partner_id.username')
    vendor_catalog = fields.Binary(related='partner_id.vendor_catalog')
    vendor_catalog_filename = fields.Char(related='partner_id.vendor_catalog_filename')
    vendor_portallogin = fields.Selection(related='partner_id.vendor_portallogin')
    verif_by_namedate = fields.Char(related='partner_id.verif_by_namedate')







