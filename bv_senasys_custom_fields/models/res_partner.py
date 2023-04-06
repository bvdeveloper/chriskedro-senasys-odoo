# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    add_catalog_price_lists = fields.Selection([('Yes', 'Yes'), ('No', 'No')], string='Add Catalog/Price Lists?')
    add_relevant_photos_below = fields.Char(string='Add Relevant Photos Below')
    attncontact = fields.Char(string='Attn/Contact:')
    catalog_notes_date_etc = fields.Text(string='Catalog Notes, Date, Etc:')
    cc_email_field = fields.Char(string='CC Email Field')
    cust_shipping_preference = fields.Selection(
        [('Ship Items as They Become Available', 'Ship Items as They Become Available'),
         ('Ship Orders Complete', 'Ship Orders Complete'), ('TBD', 'TBD')], string='Cust. Shipping Preference')
    customer_notes = fields.Text(string='Customer Notes:')
    fax_ = fields.Char(string='Fax #')
    image_1 = fields.Binary(string="Image #1")
    image_1_notes = fields.Char(string="Image 1 Notes")
    image_2 = fields.Binary(string="Image #2")
    image_2_notes = fields.Char(string="Image 2 Notes")
    image_3 = fields.Binary(string="Image #3")
    image_3_notes = fields.Char(string="Image 3 Notes")
    image_4 = fields.Binary(string="Image #4")
    image_4_notes = fields.Char(string="Image 4 Notes")
    include_docs = fields.Selection([('Yes', 'Yes'), ('No', 'No')], string="Include Docs?")
    include_photos = fields.Selection([('Yes', 'Yes'), ('No', 'No')], string="Include Photos?")
    internal_report_order_notes = fields.Text(string='Internal Report Order Notes:')
    last_updated_notes = fields.Char(string='Last Updated / Notes')
    last_updated_notes_1 = fields.Char(string='Last Updated / Notes 1')
    last_updated_notes_2 = fields.Char(string='Last Updated / Notes 2')
    notesinstructions = fields.Text(string='Notes/Instructions:')
    ordering_rulesinstructions = fields.Text(string='Ordering Rules/Instructions')
    x_password = fields.Char(string='Password')
    portal_url = fields.Text(string='Portal URL:')
    portal_website_url = fields.Char(string='Portal Website URL:')
    price_list_pdf = fields.Binary(string='Price List (PDF)')
    price_list_pdf_filename = fields.Char(string='Price List (PDF) Filename')
    record_verified = fields.Selection([('Verified', 'Verified'), ('Not Verified', 'Not Verified')], string="Record Verified?")
    tech_cad_drawings = fields.Binary(string='Tech. / CAD Drawings')
    tech_cad_drawings_filename = fields.Char(string='Tech. / CAD Drawings Filename')
    type_x = fields.Selection([('Vendor', 'Vendor'), ('Customer', 'Customer')], string="Type:")
    typical_item_types_purchased = fields.Text(string='Typical Item Type(s) Purchased')
    typical_items_types_purchased_for_ecm = fields.Text(string='Typical Items Types Purchased for ECM')
    typical_items_types_purchased_for_ecm_1 = fields.Text(string='Typical Items Types Purchased for ECM 1')
    x_username = fields.Char(string="Username")
    vendor_catalog = fields.Binary(string='Vendor Catalog:')
    vendor_catalog_filename = fields.Char(string='Vendor Catalog Filename:')
    vendor_portallogin = fields.Selection([('Yes', 'Yes'), ('No', 'No')], string="Add Vendor Portal/Login?")
    verif_by_namedate = fields.Char(string='Verif. By Name/Date')
    catalog_pdf_filename = fields.Char(string='Catalog (PDF) Filename')
    catalog_pdf = fields.Binary(string='Catalog (PDF)')
    add_rel_ref_photos_description = fields.Char(string='Add Relevant Reference Photos Below and Provide Description')
    portal_url_1 = fields.Char(string='Portal URL:')
    x_studio_binary_field_3V0L2 = fields.Binary(string='New Image')
    x_studio_binary_field_KsP2R_filename = fields.Char(string="Filename for x_studio_binary_field_KsP2R")
    x_studio_binary_field_NjvGx_filename = fields.Char(string="Filename for x_studio_binary_field_NjvGx")
    x_studio_binary_field_ruCRS_filename = fields.Char(string="Filename for x_studio_binary_field_ruCRS")

    carrier_account_number = fields.Char(String='Carrier Account no.')
    carried_has_acc_number = fields.Boolean("Carrier has acc no?", related='property_delivery_carrier_id.has_account_number')


