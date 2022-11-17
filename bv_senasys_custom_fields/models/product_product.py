# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    add_ecm_historical_data_below = fields.Selection(related='product_tmpl_id.add_ecm_historical_data_below')
    add_tech_data_to_print_to_catalog_record = fields.Text(
        related='product_tmpl_id.add_tech_data_to_print_to_catalog_record')
    additional_notes = fields.Text(related='product_tmpl_id.additional_notes')
    additional_notes_1 = fields.Text(related='product_tmpl_id.additional_notes_1')
    additional_notes_2 = fields.Text(related='product_tmpl_id.additional_notes_2')
    additional_notes_3 = fields.Text(related='product_tmpl_id.additional_notes_3')
    additional_notes_4 = fields.Text(related='product_tmpl_id.additional_notes_4')
    additional_notes_filename = fields.Char(related='product_tmpl_id.additional_notes_filename')
    additional_notes_import_export = fields.Text(related='product_tmpl_id.additional_notes_import_export')
    brand_name = fields.Char(related='product_tmpl_id.brand_name')
    by_salesperson = fields.Char(related='product_tmpl_id.by_salesperson')
    by_salesperson_1 = fields.Char(related='product_tmpl_id.by_salesperson_1')
    by_salesperson_2 = fields.Selection(related='product_tmpl_id.by_salesperson_2')
    by_salesperson_3 = fields.Selection(related='product_tmpl_id.by_salesperson_3')
    catalog_section = fields.Selection(related='product_tmpl_id.catalog_section')
    country_of_origin = fields.Selection(related='product_tmpl_id.country_of_origin')
    country_of_purchase = fields.Selection(related='product_tmpl_id.country_of_purchase')
    cust_part_names = fields.Char(related='product_tmpl_id.cust_part_names')
    date_of_oem_pricing = fields.Date(related='product_tmpl_id.date_of_oem_pricing')
    date_verified = fields.Date(related='product_tmpl_id.date_verified')
    date_verified_1 = fields.Date(related='product_tmpl_id.date_verified_1')
    dateqtycust_requesting_no_quote_part = fields.Text(related='product_tmpl_id.dateqtycust_requesting_no_quote_part')
    describe_here = fields.Text(related='product_tmpl_id.describe_here')
    drawing_not_found = fields.Boolean(related='product_tmpl_id.drawing_not_found')
    drawing_status = fields.Selection(related='product_tmpl_id.drawing_status')
    ecm_on_hand = fields.Char(related='product_tmpl_id.ecm_on_hand')
    ecm_senasys_purchasing_levels = fields.Text(related="product_tmpl_id.ecm_senasys_purchasing_levels")
    ecm_vendor = fields.Char(related='product_tmpl_id.ecm_vendor')
    est_weight_each_lbs = fields.Char(related='product_tmpl_id.est_weight_each_lbs')
    facility_specific_notes = fields.Text(related="product_tmpl_id.facility_specific_notes")
    faqs_things_to_ask_customer_prior_to_quoting = fields.Text(
        related="product_tmpl_id.faqs_things_to_ask_customer_prior_to_quoting")
    function = fields.Selection(related="product_tmpl_id.function")
    function_2 = fields.Selection(related="product_tmpl_id.function_2")
    function_3 = fields.Selection(related="product_tmpl_id.function_3")
    function_4 = fields.Selection(related="product_tmpl_id.function_4")
    georgia_pacific_part_name = fields.Char(related="product_tmpl_id.georgia_pacific_part_name")
    image_for_product_catalog = fields.Binary(related="product_tmpl_id.image_for_product_catalog")
    inv_location = fields.Selection(related="product_tmpl_id.inv_location")
    invoice_aliases = fields.Text(related='product_tmpl_id.invoice_aliases')
    is_a_quote_required_for_each_customer_request = fields.Selection(
        related='product_tmpl_id.is_a_quote_required_for_each_customer_request')
    machine_model_s = fields.Text(related='product_tmpl_id.machine_model_s')
    machine_model_s_utilizing_part = fields.Text(related='product_tmpl_id.machine_model_s_utilizing_part')
    machining_required = fields.Selection(related='product_tmpl_id.machining_required')
    material_composition = fields.Selection(related='product_tmpl_id.material_composition')
    material = fields.Selection(related='product_tmpl_id.material')
    mfg_bom = fields.Binary(related='product_tmpl_id.mfg_bom')
    mfg_order_notes = fields.Text(related='product_tmpl_id.mfg_order_notes')
    min_qty = fields.Float(related='product_tmpl_id.min_qty')
    minutes_required = fields.Char(related='product_tmpl_id.minutes_required')
    no_quote_this_item = fields.Boolean(related='product_tmpl_id.no_quote_this_item')
    notes = fields.Char(related='product_tmpl_id.notes')
    notes_for_order_entry = fields.Char(related='product_tmpl_id.notes_for_order_entry')
    notes_for_order_entry_1 = fields.Selection(related='product_tmpl_id.notes_for_order_entry_1')
    oem_pricing_information = fields.Char(related='product_tmpl_id.oem_pricing_information')
    packing_instructions = fields.Selection(related='product_tmpl_id.packing_instructions')
    pdf_1 = fields.Binary(related='product_tmpl_id.pdf_1')
    pdf_1_filename = fields.Char(related='product_tmpl_id.pdf_1_filename')
    pdf_1_1 = fields.Binary(related='product_tmpl_id.pdf_1_1')
    pdf_1_1_filename = fields.Char(related='product_tmpl_id.pdf_1_1_filename')
    pdf_2 = fields.Binary(related='product_tmpl_id.pdf_2')
    pdf_2_1 = fields.Binary(related='product_tmpl_id.pdf_2_1')
    pdf_2_1_filename = fields.Char(related='product_tmpl_id.pdf_2_1_filename')
    pdf_3 = fields.Binary(related='product_tmpl_id.pdf_3')
    pdf_3_filename = fields.Char(related='product_tmpl_id.pdf_3_filename')
    pdf_3_1 = fields.Binary(related='product_tmpl_id.pdf_3_1')
    pdf_3_1_filename = fields.Char(related='product_tmpl_id.pdf_3_1_filename')
    preferred_vendors = fields.Char(related='product_tmpl_id.preferred_vendors')
    prepship_notes = fields.Selection(related='product_tmpl_id.prepship_notes')
    product_composition_galvanized_stainless_steel_etc = fields.Text(
        related='product_tmpl_id.product_composition_galvanized_stainless_steel_etc')
    product_composition_notes = fields.Text(related='product_tmpl_id.product_composition_notes')
    product_information = fields.Char(related='product_tmpl_id.product_information')
    ranked_alternatives = fields.Char(related='product_tmpl_id.ranked_alternatives')
    reason_no_quoting_item = fields.Text(related='product_tmpl_id.reason_no_quoting_item')
    required_work = fields.Text(related='product_tmpl_id.required_work')
    rough_margin_calculation = fields.Char(related='product_tmpl_id.rough_margin_calculation')
    senasys_stocking_priority_level = fields.Selection(related='product_tmpl_id.senasys_stocking_priority_level')
    spanish_product_desc = fields.Char(related='product_tmpl_id.spanish_product_desc')
    specifications_2 = fields.Text(related='product_tmpl_id.specifications_2')
    specifications_3 = fields.Text(related='product_tmpl_id.specifications_3')
    specifications_4 = fields.Text(related='product_tmpl_id.specifications_4')
    step_1_machining_action = fields.Char(related='product_tmpl_id.step_1_machining_action')
    step_2_machining_action = fields.Char(related='product_tmpl_id.step_2_machining_action')
    step_3_machining_action = fields.Char(related='product_tmpl_id.step_3_machining_action')
    step_4_machining_action = fields.Char(related='product_tmpl_id.step_4_machining_action')
    tariff_code = fields.Char(related='product_tmpl_id.tariff_code')
    uploadmodified_drawing_date = fields.Date(related='product_tmpl_id.uploadmodified_drawing_date')
    used_in_part_s = fields.Char(related='product_tmpl_id.used_in_part_s')
    vendor_1 = fields.Selection(related='product_tmpl_id.vendor_1')
    vendor_2 = fields.Selection(related='product_tmpl_id.vendor_2')
    vendor_3 = fields.Selection(related='product_tmpl_id.vendor_3')
    vendor_4 = fields.Selection(related='product_tmpl_id.vendor_4')
    vendor_aliases = fields.Text(related='product_tmpl_id.vendor_aliases')
    vendor_noterequirement = fields.Char(related='product_tmpl_id.vendor_noterequirement')
    verified_by = fields.Selection(related='product_tmpl_id.verified_by')
    work_process_type = fields.Selection(related='product_tmpl_id.work_process_type')
    yesno = fields.Selection(related='product_tmpl_id.work_process_type')
    yesno_1 = fields.Selection(related='product_tmpl_id.yesno_1')
    senasys_division = fields.Selection(related="product_tmpl_id.senasys_division")
    x_description = fields.Char(related="product_tmpl_id.x_description")
    download_full_res_image = fields.Binary(related="product_tmpl_id.download_full_res_image")
    image_1024_wide = fields.Binary(related="product_tmpl_id.image_1024_wide")






