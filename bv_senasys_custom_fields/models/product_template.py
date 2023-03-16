# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    add_ecm_historical_data_below = fields.Selection([('Yes', 'Yes'), ('No', 'No')],
                                                     string='Add ECM Historical Data Below?')
    add_tech_data_to_print_to_catalog_record = fields.Text(string='Add Tech. Data to Print to Catalog Record')
    additional_notes = fields.Binary(string='Additional Notes')
    additional_notes_1 = fields.Text(string='Additional Notes 1:')
    additional_notes_2 = fields.Text(string='Additional Notes 2:')
    additional_notes_3 = fields.Text(string='Additional Notes 3:')
    additional_notes_4 = fields.Text(string='Additional Notes 4:')
    additional_notes_5 = fields.Text(string='Additional Notes 5:')
    additional_notes_filename = fields.Char(string='Additional Notes For Filename:')
    additional_notes_import_export = fields.Text(string='Additional Notes Import Export:')
    brand = fields.Char(string='Brand')
    brand_name = fields.Char(string='Brand Name')
    by_salesperson = fields.Char(string='By Salesperson:')
    by_salesperson_1 = fields.Char(string='By Salesperson 1:')
    by_salesperson_2 = fields.Selection(
        [('Alyssa', 'Alyssa'), ('Chris', 'Chris'), ('ECM/Don (Initial Pricing)', 'ECM/Don (Initial Pricing)'),
         ('Jeremy', 'Jeremy'), ('Kayla', 'Kayla'), ('Lana', 'Lana'), ('Sara', 'Sara'), ('Victoria', 'Victoria')], string='By Salesperson 2:')
    by_salesperson_3 = fields.Selection(
        [('Alyssa', 'Alyssa'), ('Chris', 'Chris'), ('ECM/Don (Initial Pricing)', 'ECM/Don (Initial Pricing)'),
         ('Jeremy', 'Jeremy'), ('Kayla', 'Kayla'), ('Lana', 'Lana'), ('Sara', 'Sara'), ('Victoria', 'Victoria')], string='By Salesperson 3:')
    catalog_section = fields.Selection(
        [('Actuators', 'Actuators'), ('Bearings', 'Bearings'), ('Bearing Housings', 'Bearing Housings'),
         ('Connectors/Wires', 'Connectors/Wires'), ('Encoders', 'Encoders'), ('Glue Pans', 'Glue Pans'),
         ('Glue Pan - Accessories', 'Glue Pan - Accessories'), ('Machine Parts', 'Machine Parts'), ('Motors', 'Motors'),
         ('Rods', 'Rods'),
         ('Screws/Nuts/Bolts/Washers', 'Screws/Nuts/Bolts/Washers')], string='Catalog Section')
    country_of_origin = fields.Selection(
        [('Canada', 'Canada'), ('China', 'China'), ('Mexico', 'Mexico'),
         ('USA', 'USA')], string='Country of Origin')
    country_of_purchase = fields.Selection(
        [('Canada', 'Canada'), ('China', 'China'), ('Mexico', 'Mexico'),
         ('USA', 'USA')], string='Country of Purchase')
    cust_part_names = fields.Char(string="Cust. Part Name/#'s")
    date_of_oem_pricing = fields.Date(string="Date of OEM Pricing:")
    date_verified = fields.Date(string="Date Verified:")
    date_verified_1 = fields.Date(string="Date Verified 1:")
    dateqtycust_requesting_no_quote_part = fields.Text(string="Date/Qty/Cust Requesting 'No Quote' Part:")
    describe_here = fields.Text(string='Describe Here:')
    drawing_not_found = fields.Boolean(string='Drawing Not Found')
    drawing_status = fields.Selection([('Unverified', 'Unverified'), ('Verified', 'Verified'),
                                       ('Produced & Accepted By Customer', 'Produced & Accepted By Customer')],
                                      string='Drawing Status:')
    ecm_on_hand = fields.Char(string="ECM On Hand:")
    ecm_senasys_purchasing_levels = fields.Text(string="ECM Senasys Purchasing Levels")
    ecm_vendor = fields.Char(string="ECM Vendor")
    est_weight_each_lbs = fields.Char(string="Est Weight/Dim (Each)")
    facility_specific_notes = fields.Text(string="Facility Specific Notes")
    faqs_things_to_ask_customer_prior_to_quoting = fields.Text(string="FAQs / Things to Ask Customer Prior to Quoting:")
    function = fields.Selection(
        [('Cylindrical Grinding', 'Cylindrical Grinding'), ('General Machining', 'General Machining'),
         ('Heat Treating', 'Heat Treating'),
         ('Lathe Work', 'Lathe Work')], string='Function')
    function_2 = fields.Selection(
        [('Cylindrical Grinding', 'Cylindrical Grinding'), ('General Machining', 'General Machining'),
         ('Heat Treating', 'Heat Treating'),
         ('Lathe Work', 'Lathe Work')], string='Function 2')
    function_3 = fields.Selection(
        [('Cylindrical Grinding', 'Cylindrical Grinding'), ('General Machining', 'General Machining'),
         ('Heat Treating', 'Heat Treating'),
         ('Lathe Work', 'Lathe Work')], string='Function 3')
    function_4 = fields.Selection(
        [('Cylindrical Grinding', 'Cylindrical Grinding'), ('General Machining', 'General Machining'),
         ('Heat Treating', 'Heat Treating'),
         ('Lathe Work', 'Lathe Work')], string='Function 4')
    georgia_pacific_part_name = fields.Char(string="Georgia Pacific Part Name/#:")
    image_for_product_catalog = fields.Binary(string="Image for Product Catalog")
    inv_location = fields.Selection(
        [('TBD', 'TBD'), ('1A', '1A'), ('1B', '1B'), ('1C', '1C'), ('1D', '1D'), ('1E', '1E'), ('2A', '2A'),
         ('2B', '2B'), ('2C', '2C'), ('2D', '2D'), ('2E', '2E'), ('3A', '3A'), ('3B', '3B'), ('3C', '3C'), ('3D', '3D'),
         ('3E', '3E'), ('4A', '4A'), ('4B', '4B'), ('4C', '4C'), ('4D', '4D'), ('4E', '4E'), ('5A', '5A'), ('5B', '5B'),
         ('5C', '5C'), ('5D', '5D'), ('5E', '5E'), ('6A', '6A'), ('6B', '6B'), ('6C', '6C'), ('6D', '6D'), ('6E', '6E'),
         ('7A', '7A'), ('7B', '7B'), ('7C', '7C'), ('7D', '7D'), ('7E', '7E'), ('8A', '8A'), ('8B', '8B'), ('8C', '8C'),
         ('8D', '8D'), ('8E', '8E'), ('9A', '9A'), ('9B', '9B'), ('9C', '9C'), ('9D', '9D'), ('9E', '9E'),
         ('10A', '10A'), ('10B', '10B'), ('10C', '10C'), ('10D', '10D'), ('10E', '10E'), ('11A', '11A'), ('11B', '11B'),
         ('11C', '11C'), ('11D', '11D'), ('11E', '11E'), ('12A', '12A'), ('12B', '12B'), ('12C', '12C'), ('12D', '12D'),
         ('12E', '12E'), ('13A', '13A'), ('13B', '13B'), ('13C', '13C'), ('13D', '13D'), ('13E', '13E'), ('14A', '14A'),
         ('14B', '14B'), ('14C', '14C'), ('14D', '14D'), ('14E', '14E'), ('15A', '15A'), ('15B', '15B'), ('15C', '15C'),
         ('15D', '15D'), ('15E', '15E'), ('16A', '16A'), ('16B', '16B'), ('16C', '16C'), ('16D', '16D'), ('16E', '16E'),
         ('17A', '17A'), ('17B', '17B'), ('17C', '17C'), ('17D', '17D'), ('17E', '17E'), ('18A', '18A'), ('18B', '18B'),
         ('18C', '18C'), ('18D', '18D'), ('18E', '18E'), ('19A', '19A'), ('19B', '19B'), ('19C', '19C'), ('19D', '19D'),
         ('19E', '19E'), ('20A', '20A'), ('20B', '20B'), ('20C', '20C'), ('20D', '20D'), ('20E', '20E'), ('21A', '21A'),
         ('21B', '21B'), ('21C', '21C'), ('21D', '21D'), ('21E', '21E'), ('22A', '22A'), ('22B', '22B'), ('22C', '22C'),
         ('22D', '22D'), ('22E', '22E'), ('23A', '23A'), ('23B', '23B'), ('23C', '23C'), ('23D', '23D'), ('23E', '23E'),
         ('MACHINE SHOP', 'M. SHOP'), ('M.SHOP-2', 'M.SHOP-2'), ('OTHER', 'OTHER'), ('Zero', 'Zero'),
         ('GLUE-B', 'GLUE-B'), ('GLUE-R', 'GLUE-R'), ('GLUE-Y', 'GLUE-Y'), ('GLUE-?', 'GLUE-?'), ('Rack 1A', 'Rack 1'),
         ('Rack 1B', 'Rack 2'), ('Rack 1C', 'Rack 3'), ('Rack 1D', 'Rack 4'), ('Rack 5', 'Rack 5'),
         ('Rack 6', 'Rack 6')]
        , string='Inv Location:')
    invoice_aliases = fields.Text(string='Invoice Aliases')
    is_a_quote_required_for_each_customer_request = fields.Selection([('Yes', 'Yes'), ('No', 'No'), ('TBD', 'TBD')],
                                                                     string='Is a quote required for each customer request?')
    machine_model_s = fields.Text(string='Machine Model #s:')
    machine_model_s_utilizing_part = fields.Text(string='Machine Model S Utilizing Part')
    machining_required = fields.Selection([('TBD', 'TBD'), ('No Machining Required', 'No Machining Required'),
                                           ('Submachining - In House', 'Submachining - In House'),
                                           ('Full Fabrication In-House', 'Full Fabrication In-House'),
                                           ('3rd Party Rework/Machining', '3rd Party Rework/Machining')],
                                          string='Machining Required:')
    material_composition = fields.Selection([('Electronics', 'Electronics'), ('Gasket Material', 'Gasket Material'),
                                             ('Glass', 'Glass'),
                                             ('Metal', 'Metal'),
                                             ('Nylon', 'Nylon'),
                                             ('Plastic', 'Plastic')], string='Material Composition')
    material = fields.Selection([('TBD', 'TBD'), ('CRS (Cold Rolled Steel)', 'CRS (Cold Rolled Steel)'),
                                 ('304 Stainless', '304 Stainless'),
                                 ('440 Stainless', '440 Stainless'),
                                 ('Brass', 'Brass'), ('Bronze', 'Bronze'), ('Copper', 'Copper'),
                                 ('Aluminum', 'Aluminum')], string='Material:')
    # mfg_bom = fields.Binary(string='MFG BOM')
    mfg_order_notes = fields.Text(string='MFG Order Notes:')
    min_qty = fields.Float(related='product_variant_id.orderpoint_ids.product_min_qty')
    minutes_required = fields.Char(string='Senasys Minutes Required (for pricing/billing)')
    no_quote_this_item = fields.Boolean(string='No Quote This Item')
    notes = fields.Char(string='Notes')
    notes_for_order_entry = fields.Char(string='Notes for Order Entry')
    notes_for_order_entry_1 = fields.Selection([('Alt Vendors/Prices', 'Alt Vendors/Prices'),
                                                ('Long Lead Time','Long Lead Time'),
                                                ('Obsolete', 'Obsolete'),
                                                ('Obsolete: See Alt', 'Obsolete: See Alt'),
                                                ('Part # Variant is Cust. Specific','Part # Variant is Cust. Specific'),
                                                ('Price Check Req!', 'Price Check Req!'),
                                                ('See Tech Notes', 'See Tech Notes'),
                                                ('Upsell Available', 'Upsell Available'),
                                                ('NA', 'NA')], string='Notes for Order Entry')
    oem_pricing_information = fields.Char(string='OEM Pricing Information')
    packing_instructions = fields.Selection(
        [('Bagged With Qty/Label', 'Bagged With Qty/Label'), ('Boxed (Loose in Box)', 'Boxed (Loose in Box)'),
         ('Boxed (Bubble Wrapped)', 'Boxed (Bubble Wrapped)'),
         ('Boxed (Remove MFG Packaging)', 'Boxed (Remove MFG Packaging)'),
         ('Crated', 'Crated (UPS or LTL TBD)'),
         ('Crated (LTL Required)', 'Crated (LTL Required)'),
         ('Custom: See Below', 'Custom: See Below'),
         ('Double Boxed if Mult. Items in Shipment', 'Double Boxed if Mult. Items in Shipment'),
         ], string='Packing Instructions')
    pdf_1 = fields.Binary(string='PDF 1')
    pdf_1_filename = fields.Char(string='PDF 1 filename')
    pdf_1_1 = fields.Binary(string='PDF 1_1')
    pdf_1_1_filename = fields.Char(string='PDF 1_1 filename')
    pdf_2 = fields.Binary(string='PDF 2')
    pdf_2_1 = fields.Binary(string='PDF 2_1')
    pdf_2_1_filename = fields.Char(string='PDF 2_1 filename')
    pdf_3 = fields.Binary(string='PDF 3')
    pdf_3_filename = fields.Char(string='PDF 3 filename')
    pdf_3_1 = fields.Binary(string='PDF 3_1')
    pdf_3_1_filename = fields.Char(string='PDF 3_1 filename')
    preferred_vendors = fields.Char(string='1st Choice:')
    prepship_notes = fields.Selection([('☐ Date:____/____ /____  Notes: _____________ _____________________',
                                        '☐ Date:____/____ /____ Notes: _____________ _____________________'),
                                       ('a☐ Prepped___ Date:____/____ /____  Notes: _____________ _____________________',
                                        '☐ Prepped___ Date:____/____ /____ Notes: _____________ _____________________')],
                                      string='Prep/Ship Notes')
    product_composition_galvanized_stainless_steel_etc = fields.Text(
        string='Product Composition (Galvanized, Stainless Steel, Brass, etc)')
    product_composition_notes = fields.Text(string='Product Composition Notes:')
    product_information = fields.Char(string="Product Information")
    ranked_alternatives = fields.Char(string="Ranked Alternatives")
    reason_no_quoting_item = fields.Text(string="Reason No Quoting Item:")
    required_work = fields.Text(string="Specifications 1:")
    rough_margin_calculation = fields.Char(string="Rough Margin Calculation")
    senasys_stocking_priority_level = fields.Selection([('AA', 'AA'), ('A', 'A'),
                                                        ('B', 'B'), ('C', 'C (Order on Demand, No Min Stock Rule)'),
                                                        ('TBD', 'TBD')], string="A, B, C Class")
    shipped_record_per_order_line = fields.Char(string="Shipped Record:")
    spanish_product_desc = fields.Char(string="Spanish Product Desc.")
    specifications_2 = fields.Text(string="Specifications 2:")
    specifications_3 = fields.Text(string="Specifications 3:")
    specifications_4 = fields.Text(string="Specifications 4:")
    step_1_machining_action = fields.Char(string="Step 1 Machining Action")
    step_2_machining_action = fields.Char(string="Step 2 Machining Action")
    step_3_machining_action = fields.Char(string="Step 3 Machining Action")
    step_4_machining_action = fields.Char(string="Step 4 Machining Action")
    tariff_code = fields.Char(string="Tariff Code")
    uploadmodified_drawing_date = fields.Date(string="Upload/Modified Drawing Date:")
    # used_in_part_s = fields.Char(string="Used in Part #(s)")
    vendor_1 = fields.Selection([('ED-K Machining', 'ED-K Machining'), ('Indianhead Plating', 'Indianhead Plating'),
                                 ('Metal Treaters', 'Metal Treaters'), ('Senasys Machining', 'Senasys Machining'),
                                 ('Coulson Precision Tooling Inc', 'Coulson Precision Tooling Inc')],
                                string="Vendor 1:")
    vendor_2 = fields.Selection([('ED-K Machining', 'ED-K Machining'), ('Indianhead Plating', 'Indianhead Plating'),
                                 ('Metal Treaters', 'Metal Treaters'), ('Senasys Machining', 'Senasys Machining'),
                                 ('Coulson Precision Tooling Inc', 'Coulson Precision Tooling Inc')],
                                string="Vendor 2:")
    vendor_3 = fields.Selection([('ED-K Machining', 'ED-K Machining'), ('Indianhead Plating', 'Indianhead Plating'),
                                 ('Metal Treaters', 'Metal Treaters'), ('Senasys Machining', 'Senasys Machining'),
                                 ('Coulson Precision Tooling Inc', 'Coulson Precision Tooling Inc')],
                                string="Vendor 3:")
    vendor_4 = fields.Selection([('ED-K Machining', 'ED-K Machining'), ('Indianhead Plating', 'Indianhead Plating'),
                                 ('Metal Treaters', 'Metal Treaters'), ('Senasys Machining', 'Senasys Machining'),
                                 ('Coulson Precision Tooling Inc', 'Coulson Precision Tooling Inc')],
                                string="Vendor 4:")
    vendor_aliases = fields.Text(string="Vendor Aliases")
    vendor_noterequirement = fields.Char(string="Vendor Note/Requirement")
    verified_by = fields.Selection([('Jeremy', 'Jeremy'), ('Chris', 'Chris'),
                                    ('Steve', 'Steve'), ('Other', 'Other'),
                                    ('End User', 'End User'), ('TBD', 'TBD')], string="Verified By")
    work_process_type = fields.Selection([('Skilled Labor/Assembly Required', 'Skilled Labor/Assembly Required'), (
    'Simple Assembly from Sub-Component Parts', 'Simple Assembly from Sub-Component Parts')], string="Work Process Type")
    yesno = fields.Selection([('Yes', 'Yes'), ('No', 'No')], string="Add Technical Product Info Below?")
    yesno_1 = fields.Selection([('Yes', 'Yes'), ('No', 'No'), ('TBD', 'TBD')], string="Yes/No")
    senasys_division = fields.Selection([('Empire Corrugated', 'Empire Corrugated'), ('Wahl', 'Wahl')], string="Senasys Division")
    x_description = fields.Char(string="Vendor PO / Mfg Description")
    download_full_res_image = fields.Binary(related="product_variant_id.image_1920")
    image_1024_wide = fields.Binary(related="product_variant_id.image_1024")
    website_lead_time = fields.Text(string="Website lead Time")
    customer_part_name = fields.Char(string="Customer Part Name/#:")
    inv_loc = fields.Selection(related='product_variant_id.inv_location')
    product_composition = fields.Char(string="Product Composition")
    shipped_record = fields.Char(string="Shipped Record:")
    tariff = fields.Char(string="Tariff")
    x_studio_binary_field_4CqW2 = fields.Binary(string="New File")
    x_studio_binary_field_4CqW2_filename = fields.Char(string="Filename for x_studio_binary_field_4CqW2")
    x_studio_binary_field_4yovM = fields.Binary(string="New Image")
    x_studio_binary_field_cQquS = fields.Binary(string="New Image")
    x_studio_binary_field_EhQ1a = fields.Binary(string="New Image")
    x_studio_binary_field_f1ABS = fields.Binary(string="New Image")
    x_studio_binary_field_FExVC = fields.Binary(string="New File")
    x_studio_binary_field_FExVC_filename = fields.Char(string="Filename for x_studio_binary_field_FExVC")
    x_studio_binary_field_fzAlF = fields.Binary(string="New File")
    x_studio_binary_field_fzAlF_filename = fields.Char(string="Filename for x_studio_binary_field_fzAlF")
    x_studio_binary_field_Nm5jY = fields.Binary(string="New File")
    x_studio_binary_field_Nm5jY_filename = fields.Char(string="Filename for x_studio_binary_field_Nm5jY")
    x_studio_binary_field_qeHlf = fields.Binary(string="New Image")
    x_studio_binary_field_QWeIs = fields.Binary(string="New Image")
    x_studio_binary_field_RM4Bo = fields.Binary(string="New File")
    x_studio_binary_field_RM4Bo_filename = fields.Char(string="Filename for x_studio_binary_field_RM4Bo")
    x_studio_binary_field_t79IE = fields.Binary(string="New File")
    x_studio_binary_field_t79IE_filename = fields.Char(string="Filename for x_studio_binary_field_t79IE")
    x_studio_boolean_field_br5KV = fields.Boolean(string="New Checkbox")
    x_studio_boolean_field_VE9xk = fields.Boolean(string="New Checkbox")
    x_studio_related_field_inBxC = fields.Binary(related="product_variant_id.image_1920", string='Download (Full Res) Image')
    x_studio_related_field_sL8RZ = fields.Binary(related="product_variant_id.image_1024", string='Image (1024 wide)')


