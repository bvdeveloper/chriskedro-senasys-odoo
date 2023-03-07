import xmlrpc.client
import time

url = 'https://chriskedro-senasys-odoo.odoo.com'
db = 'chriskedro-senasys-odoo-production-5334020'
username = 'christopher.kedrowski@gmail.com'
password = '0d00123!!!'

# url = 'http://0.0.0.0:8024'
# db = 's_test_7'
# username = 'christopher.kedrowski@gmail.com'
# password = '0d00123!!!'


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

start = time.time()
#=======================res.partner======================================================================
res_partner_studio_field_list = ['x_studio_add_catalogprice_lists', 'x_studio_add_relevant_photos_below',
                                 'x_studio_attncontact', 'x_studio_catalog_notes_date_etc', 'x_studio_cc_email_field',
                                 'x_studio_cust_shipping_preference', 'x_studio_customer_notes', 'x_studio_fax_',
                                 'x_studio_image_1', 'x_studio_image_1_notes', 'x_studio_image_2',
                                 'x_studio_image_2_notes', 'x_studio_image_3', 'x_studio_image_3_notes',
                                 'x_studio_image_4', 'x_studio_image_4_notes', 'x_studio_include_docs',
                                 'x_studio_include_photos', 'x_studio_internal_report_order_notes',
                                 'x_studio_last_updated_notes', 'x_studio_last_updated_notes_1',
                                 'x_studio_last_updated_notes_2', 'x_studio_notesinstructions',
                                 'x_studio_ordering_rulesinstructions', 'x_studio_password', 'x_studio_portal_url',
                                 'x_studio_portal_website_url', 'x_studio_price_list_pdf',
                                 'x_studio_price_list_pdf_filename', 'x_studio_record_verified',
                                 'x_studio_tech_cad_drawings', 'x_studio_tech_cad_drawings_filename', 'x_studio_type',
                                 'x_studio_typical_item_types_purchased',
                                 'x_studio_typical_items_types_purchased_for_ecm',
                                 'x_studio_typical_items_types_purchased_for_ecm_1', 'x_studio_username',
                                 'x_studio_vendor_catalog', 'x_studio_vendor_catalog_filename',
                                 'x_studio_vendor_portallogin', 'x_studio_verif_by_namedate',
                                 'x_studio_binary_field_r07XT_filename', 'x_studio_binary_field_r07XT']

partners_studio_data = models.execute_kw(db, uid, password, 'res.partner', 'search_read',
                                         [[]], {'fields': res_partner_studio_field_list,'order': 'id'})
print("\n\n====Total records for res.partner==", len(partners_studio_data))

count = 0
for partner in partners_studio_data:
    count = count + 1
    partner_id = partner['id']
    print("\n\n=======count=======", count, "=====partner_id====", partner_id)
    partner_vals = {'add_catalog_price_lists': partner['x_studio_add_catalogprice_lists'],
                    'add_relevant_photos_below': partner['x_studio_add_relevant_photos_below'],
                    'attncontact': partner['x_studio_attncontact'],
                    'catalog_notes_date_etc': partner['x_studio_catalog_notes_date_etc'],
                    'cc_email_field': partner['x_studio_cc_email_field'],
                    'cust_shipping_preference': partner['x_studio_cust_shipping_preference'],
                    'customer_notes': partner['x_studio_customer_notes'],
                    'fax_': partner['x_studio_fax_'],
                    'image_1': partner['x_studio_image_1'],
                    'image_1_notes': partner['x_studio_image_1_notes'],
                    'image_2': partner['x_studio_image_2'],
                    'image_2_notes': partner['x_studio_image_2_notes'],
                    'image_3': partner['x_studio_image_3'],
                    'image_3_notes': partner['x_studio_image_3_notes'],
                    'image_4': partner['x_studio_image_4'],
                    'image_4_notes': partner['x_studio_image_4_notes'],
                    'include_docs': partner['x_studio_include_docs'],
                    'include_photos': partner['x_studio_include_photos'],
                    'internal_report_order_notes': partner['x_studio_internal_report_order_notes'],
                    'last_updated_notes': partner['x_studio_last_updated_notes'],
                    'last_updated_notes_1': partner['x_studio_last_updated_notes_1'],
                    'last_updated_notes_2': partner['x_studio_last_updated_notes_2'],
                    'notesinstructions': partner['x_studio_notesinstructions'],
                    'ordering_rulesinstructions': partner['x_studio_ordering_rulesinstructions'],
                    'x_password': partner['x_studio_password'],
                    'portal_url': partner['x_studio_portal_url'],
                    'portal_website_url': partner['x_studio_portal_website_url'],
                    'price_list_pdf': partner['x_studio_price_list_pdf'],
                    'price_list_pdf_filename': partner['x_studio_price_list_pdf_filename'],
                    'record_verified': partner['x_studio_record_verified'],
                    'tech_cad_drawings': partner['x_studio_tech_cad_drawings'],
                    'tech_cad_drawings_filename': partner['x_studio_tech_cad_drawings_filename'],
                    'type_x': partner['x_studio_type'],
                    'typical_item_types_purchased': partner['x_studio_typical_item_types_purchased'],
                    'typical_items_types_purchased_for_ecm': partner['x_studio_typical_items_types_purchased_for_ecm'],
                    'typical_items_types_purchased_for_ecm_1': partner['x_studio_typical_items_types_purchased_for_ecm_1'],
                    'x_username': partner['x_studio_username'],
                    'vendor_catalog': partner['x_studio_vendor_catalog'],
                    'vendor_catalog_filename': partner['x_studio_vendor_catalog_filename'],
                    'vendor_portallogin': partner['x_studio_vendor_portallogin'],
                    'verif_by_namedate': partner['x_studio_verif_by_namedate'],
                    'catalog_pdf_filename': partner['x_studio_binary_field_r07XT_filename'],
                    'catalog_pdf': partner['x_studio_binary_field_r07XT'],
                    }
    # print("\n\n====partner_vals==", partner_vals)
    models.execute_kw(db, uid, password, 'res.partner', 'write', [[partner_id], partner_vals])

#=================sale.order=================================================================================
sale_order_studio_field_list = ['x_studio_enter_order_specific_notes_below',
                                'x_studio_jobnametag',
                                'x_studio_lead_time_for_quotes_only',
                                'x_studio_order_promised_ship_date',
                                'x_studio_portal_cust_contact_method',
                                'x_studio_quote_closed',
                                'x_studio_shiping_method',
                                'x_studio_shipping_collect_acct_',
                                'x_studio_senasys_division']

sale_order_studio_data = models.execute_kw(db, uid, password, 'sale.order', 'search_read',
                                           [[]], {'fields': sale_order_studio_field_list,'order': 'id'})
print("\n\n====Total records for sale.order==", len(sale_order_studio_data))

count = 0
for order in sale_order_studio_data:
    count = count + 1
    order_id = order['id']
    print("\n\n=======count=======", count, "=====order_id====", order_id)
    order_vals = {'enter_order_specific_notes_below': order['x_studio_enter_order_specific_notes_below'],
                  'jobnametag': order['x_studio_jobnametag'],
                  'lead_time_for_quotes_only': order['x_studio_lead_time_for_quotes_only'],
                  'order_promised_ship_date': order['x_studio_order_promised_ship_date'],
                  'portal_cust_contact_method': order['x_studio_portal_cust_contact_method'],
                  'quote_closed': order['x_studio_quote_closed'],
                  'shipping_method': order['x_studio_shiping_method'],
                  'shipping_collect_acct_': order['x_studio_shipping_collect_acct_'],
                  'senasys_division': order['x_studio_senasys_division']}
    models.execute_kw(db, uid, password, 'sale.order', 'write', [[order_id], order_vals])



#====================product.template====================================================================
product_template_studio_field_list = ['x_studio_add_ecm_historical_data_below',
                                      'x_studio_add_tech_data_to_print_to_catalog_record', 'x_studio_additional_notes',
                                      'x_studio_additional_notes_1', 'x_studio_additional_notes_2',
                                      'x_studio_additional_notes_3', 'x_studio_additional_notes_4',
                                      'x_studio_additional_notes_filename', 'x_studio_additional_notes_import_export',
                                      'x_studio_brand_name', 'x_studio_by_salesperson', 'x_studio_by_salesperson_1',
                                      'x_studio_by_salesperson_2', 'x_studio_by_salesperson_3',
                                      'x_studio_catalog_section', 'x_studio_country_of_origin',
                                      'x_studio_country_of_purchase', 'x_studio_cust_part_names',
                                      'x_studio_date_of_oem_pricing', 'x_studio_date_verified',
                                      'x_studio_date_verified_1', 'x_studio_dateqtycust_requesting_no_quote_part',
                                      'x_studio_describe_here', 'x_studio_drawing_not_found', 'x_studio_drawing_status',
                                      'x_studio_ecm_on_hand', 'x_studio_ecm_senasys_purchasing_levels',
                                      'x_studio_ecm_vendor', 'x_studio_est_weight_each_lbs',
                                      'x_studio_facility_specific_notes',
                                      'x_studio_faqs_things_to_ask_customer_prior_to_quoting', 'x_studio_function',
                                      'x_studio_function_2', 'x_studio_function_3', 'x_studio_function_4',
                                      'x_studio_georgia_pacific_part_name', 'x_studio_image_for_product_catalog',
                                      'x_studio_inv_location', 'x_studio_invoice_aliases',
                                      'x_studio_is_a_quote_required_for_each_customer_request',
                                      'x_studio_machine_model_s', 'x_studio_machine_model_s_utilizing_part',
                                      'x_studio_machining_required', 'x_studio_material_composition',
                                      'x_studio_material', 'x_studio_mfg_order_notes', 'x_studio_minutes_required',
                                      'x_studio_no_quote_this_item', 'x_studio_notes', 'x_studio_notes_for_order_entry',
                                      'x_studio_notes_for_order_entry_1', 'x_studio_oem_pricing_information',
                                      'x_studio_packing_instructions', 'x_studio_pdf_1', 'x_studio_pdf_1_filename',
                                      'x_studio_pdf_1_1', 'x_studio_pdf_1_1_filename',
                                      'x_studio_pdf_2',
                                      'x_studio_pdf_2_1', 'x_studio_pdf_2_1_filename', 'x_studio_pdf_3',
                                      'x_studio_pdf_3_filename', 'x_studio_pdf_3_1', 'x_studio_pdf_3_1_filename',
                                      'x_studio_preferred_vendors', 'x_studio_prepship_notes',
                                      'x_studio_product_composition_galvanized_stainless_steel_etc',
                                      'x_studio_product_composition_notes', 'x_studio_product_information',
                                      'x_studio_ranked_alternatives', 'x_studio_reason_no_quoting_item',
                                      'x_studio_required_work', 'x_studio_rough_margin_calculation',
                                      'x_studio_senasys_stocking_priority_level',
                                      'x_studio_shipped_record_per_order_line', 'x_studio_spanish_product_desc',
                                      'x_studio_specifications_2', 'x_studio_specifications_3',
                                      'x_studio_specifications_4', 'x_studio_step_1_machining_action',
                                      'x_studio_step_2_machining_action', 'x_studio_step_3_maching_action',
                                      'x_studio_step_4_machining_action', 'x_studio_tariff_code',
                                      'x_studio_uploadmodified_drawing_date', 'x_studio_selection_field_cnIbI',
                                      'x_studio_vendor_2', 'x_studio_vendor_3', 'x_studio_vendor_4',
                                      'x_studio_vendor_aliases', 'x_studio_vendor_noterequirement',
                                      'x_studio_verified_by', 'x_studio_work_process_type', 'x_studio_yesno',
                                      'x_studio_yesno_1', 'x_studio_senasys_division', 'x_studio_description']


def copy_product_vals(product_template_studio_data):
    count = 0
    for product in product_template_studio_data:
        count = count + 1
        product_id = product['id']
        print("\n\n=======count=======", count, "=====product_id====", product_id)
        product_vals = {'add_ecm_historical_data_below': product['x_studio_add_ecm_historical_data_below'],
                        'add_tech_data_to_print_to_catalog_record': product[
                            'x_studio_add_tech_data_to_print_to_catalog_record'],
                        'additional_notes': product['x_studio_additional_notes'],
                        'additional_notes_1': product['x_studio_additional_notes_1'],
                        'additional_notes_2': product['x_studio_additional_notes_2'],
                        'additional_notes_3': product['x_studio_additional_notes_3'],
                        'additional_notes_4': product['x_studio_additional_notes_4'],
                        'additional_notes_filename': product['x_studio_additional_notes_filename'],
                        'additional_notes_import_export': product['x_studio_additional_notes_import_export'],
                        'brand_name': product['x_studio_brand_name'],
                        'by_salesperson': product['x_studio_by_salesperson'],
                        'by_salesperson_1': product['x_studio_by_salesperson_1'],
                        'by_salesperson_2': product['x_studio_by_salesperson_2'],
                        'by_salesperson_3': product['x_studio_by_salesperson_3'],
                        'catalog_section': product['x_studio_catalog_section'],
                        'country_of_origin': product['x_studio_country_of_origin'],
                        'country_of_purchase': product['x_studio_country_of_purchase'],
                        'cust_part_names': product['x_studio_cust_part_names'],
                        'date_of_oem_pricing': product['x_studio_date_of_oem_pricing'],
                        'date_verified': product['x_studio_date_verified'],
                        'date_verified_1': product['x_studio_date_verified_1'],
                        'dateqtycust_requesting_no_quote_part': product['x_studio_dateqtycust_requesting_no_quote_part'],
                        'describe_here': product['x_studio_describe_here'],
                        'drawing_not_found': product['x_studio_drawing_not_found'],
                        'drawing_status': product['x_studio_drawing_status'],
                        'ecm_on_hand': product['x_studio_ecm_on_hand'],
                        'ecm_senasys_purchasing_levels': product['x_studio_ecm_senasys_purchasing_levels'],
                        'ecm_vendor': product['x_studio_ecm_vendor'],
                        'est_weight_each_lbs': product['x_studio_est_weight_each_lbs'],
                        'facility_specific_notes': product['x_studio_facility_specific_notes'],
                        'faqs_things_to_ask_customer_prior_to_quoting': product['x_studio_faqs_things_to_ask_customer_prior_to_quoting'],
                        'function': product['x_studio_function'],
                        'function_2': product['x_studio_function_2'],
                        'function_3': product['x_studio_function_3'],
                        'function_4': product['x_studio_function_4'],
                        'georgia_pacific_part_name': product['x_studio_georgia_pacific_part_name'],
                        'image_for_product_catalog': product['x_studio_image_for_product_catalog'],
                        'inv_location': product['x_studio_inv_location'],
                        'invoice_aliases': product['x_studio_invoice_aliases'],
                        'is_a_quote_required_for_each_customer_request': product[
                            'x_studio_is_a_quote_required_for_each_customer_request'],
                        'machine_model_s': product['x_studio_machine_model_s'],
                        'machine_model_s_utilizing_part': product['x_studio_machine_model_s_utilizing_part'],
                        'machining_required': product['x_studio_machining_required'],
                        'material_composition': product['x_studio_material_composition'],
                        'material': product['x_studio_material'],
                        'mfg_order_notes': product['x_studio_mfg_order_notes'],
                        'minutes_required': product['x_studio_minutes_required'],
                        'no_quote_this_item': product['x_studio_no_quote_this_item'],
                        'notes': product['x_studio_notes'],
                        'notes_for_order_entry': product['x_studio_notes_for_order_entry'],
                        'notes_for_order_entry_1': product['x_studio_notes_for_order_entry_1'],
                        'oem_pricing_information': product['x_studio_oem_pricing_information'],
                        'packing_instructions': product['x_studio_packing_instructions'],
                        'pdf_1': product['x_studio_pdf_1'],
                        'pdf_1_filename': product['x_studio_pdf_1_filename'],
                        'pdf_1_1': product['x_studio_pdf_1_1'],
                        'pdf_1_1_filename': product['x_studio_pdf_1_1_filename'],
                        'pdf_2': product['x_studio_pdf_2'],
                        'pdf_2_1': product['x_studio_pdf_2_1'],
                        'pdf_2_1_filename': product['x_studio_pdf_2_1_filename'],
                        'pdf_3': product['x_studio_pdf_3'],
                        'pdf_3_filename': product['x_studio_pdf_3_filename'],
                        'pdf_3_1': product['x_studio_pdf_3_1'],
                        'pdf_3_1_filename': product['x_studio_pdf_3_1_filename'],
                        'preferred_vendors': product['x_studio_preferred_vendors'],
                        'prepship_notes': product['x_studio_prepship_notes'],
                        'product_composition_galvanized_stainless_steel_etc': product[
                            'x_studio_product_composition_galvanized_stainless_steel_etc'],
                        'product_composition_notes': product['x_studio_product_composition_notes'],
                        'product_information': product['x_studio_product_information'],
                        'ranked_alternatives': product['x_studio_ranked_alternatives'],
                        'reason_no_quoting_item': product['x_studio_reason_no_quoting_item'],
                        'required_work': product['x_studio_required_work'],
                        'rough_margin_calculation': product['x_studio_rough_margin_calculation'],
                        'senasys_stocking_priority_level': product['x_studio_senasys_stocking_priority_level'],
                        'shipped_record_per_order_line': product['x_studio_shipped_record_per_order_line'],
                        'spanish_product_desc': product['x_studio_spanish_product_desc'],
                        'specifications_2': product['x_studio_specifications_2'],
                        'specifications_3': product['x_studio_specifications_3'],
                        'specifications_4': product['x_studio_specifications_4'],
                        'step_1_machining_action': product['x_studio_step_1_machining_action'],
                        'step_2_machining_action': product['x_studio_step_2_machining_action'],
                        'step_3_machining_action': product['x_studio_step_3_maching_action'],
                        'step_4_machining_action': product['x_studio_step_4_machining_action'],
                        'tariff_code': product['x_studio_tariff_code'],
                        'uploadmodified_drawing_date': product['x_studio_uploadmodified_drawing_date'],
                        'vendor_1': product['x_studio_selection_field_cnIbI'],
                        'vendor_2': product['x_studio_vendor_2'],
                        'vendor_3': product['x_studio_vendor_3'],
                        'vendor_4': product['x_studio_vendor_4'],
                        'vendor_aliases': product['x_studio_vendor_aliases'],
                        'vendor_noterequirement': product['x_studio_vendor_noterequirement'],
                        'verified_by': product['x_studio_verified_by'],
                        'work_process_type': product['x_studio_work_process_type'],
                        'yesno': product['x_studio_yesno'],
                        'yesno_1': product['x_studio_yesno_1'],
                        'senasys_division': product['x_studio_senasys_division'],
                        'x_description': product['x_studio_description'],
                        }

        # print("\n\n====product_vals==", product_vals)
        models.execute_kw(db, uid, password, 'product.template', 'write', [[product_id], product_vals])


product_template_studio_data = models.execute_kw(db, uid, password, 'product.template', 'search_read',
                                                 [[('id','>=',1),('id','<=',5000)]], {'fields': product_template_studio_field_list, 'order': 'id'})
print("\n\n====B1 Total records for product.templater==", len(product_template_studio_data))
copy_product_vals(product_template_studio_data)

product_template_studio_data = models.execute_kw(db, uid, password, 'product.template', 'search_read',
                                                 [[('id','>',5000),('id','<=',5500)]], {'fields': product_template_studio_field_list, 'order': 'id'})
print("\n\n====B2 Total records for product.templater==", len(product_template_studio_data))
copy_product_vals(product_template_studio_data)


product_template_studio_data = models.execute_kw(db, uid, password, 'product.template', 'search_read',
                                                 [[('id','>',5500),('id','<=',6000)]], {'fields': product_template_studio_field_list, 'order': 'id'})
print("\n\n====B3 Total records for product.templater==", len(product_template_studio_data))
copy_product_vals(product_template_studio_data)


product_template_studio_data = models.execute_kw(db, uid, password, 'product.template', 'search_read',
                                                 [[('id','>',6000),('id','<=',6500)]], {'fields': product_template_studio_field_list, 'order': 'id'})
print("\n\n====B4 Total records for product.templater==", len(product_template_studio_data))
copy_product_vals(product_template_studio_data)


product_template_studio_data = models.execute_kw(db, uid, password, 'product.template', 'search_read',
                                                 [[('id','>',6500),('id','<=',7000)]], {'fields': product_template_studio_field_list, 'order': 'id'})
print("\n\n====B5 Total records for product.templater==", len(product_template_studio_data))
copy_product_vals(product_template_studio_data)

product_template_studio_data = models.execute_kw(db, uid, password, 'product.template', 'search_read',
                                                 [[('id','>',7000),('id','<=',8000)]], {'fields': product_template_studio_field_list, 'order': 'id'})
print("\n\n====B6 Total records for product.templater==", len(product_template_studio_data))
copy_product_vals(product_template_studio_data)


product_template_studio_data = models.execute_kw(db, uid, password, 'product.template', 'search_read',
                                                 [[('id','>',8000),('id','<=',9000)]], {'fields': product_template_studio_field_list, 'order': 'id'})
print("\n\n====B7 Total records for product.templater==", len(product_template_studio_data))
copy_product_vals(product_template_studio_data)

product_template_studio_data = models.execute_kw(db, uid, password, 'product.template', 'search_read',
                                                 [[('id','>',9000),('id','<=',10000)]], {'fields': product_template_studio_field_list, 'order': 'id'})
print("\n\n====B8 Total records for product.templater==", len(product_template_studio_data))
copy_product_vals(product_template_studio_data)

product_template_studio_data = models.execute_kw(db, uid, password, 'product.template', 'search_read',
                                                 [[('id','>',10000),('id','<=',12000)]], {'fields': product_template_studio_field_list, 'order': 'id'})
print("\n\n====B9 Total records for product.templater==", len(product_template_studio_data))
copy_product_vals(product_template_studio_data)

#==============================sale.order.line====================================================
sale_order_line_studio_field_list = ['x_studio_line_item_number', 'x_studio_po_pull_to_invoice']

sale_order_studio_data = models.execute_kw(db, uid, password, 'sale.order.line', 'search_read',
                                           [[]], {'fields': sale_order_line_studio_field_list, 'order': 'id'})
print("\n\n====Total records for sale.order.line==", len(sale_order_studio_data))


count = 0
for order_line in sale_order_studio_data:
    count = count + 1
    order_line_id = order_line['id']
    print("\n\n=======count=======", count, "=====order_line_id====", order_line_id)
    order_line_vals = {'line_item_number': order_line['x_studio_line_item_number'],
                       'pull_to_invoice': order_line['x_studio_po_pull_to_invoice'],
                    }
    models.execute_kw(db, uid, password, 'sale.order.line', 'write', [[order_line_id], order_line_vals])


#=============================account.move==========================================================
move_studio_field_list = ['x_studio_additional_notes', 'x_studio_enter_tracking_', 'x_studio_incoterm']

move_studio_data = models.execute_kw(db, uid, password, 'account.move', 'search_read',
                                     [[]], {'fields': move_studio_field_list, 'order': 'id'})
print("\n\n====Total records for account.move==", len(move_studio_data))


count = 0
for move in move_studio_data:
    count = count + 1
    move_id = move['id']
    print("\n\n=======count=======", count, "=====move_id====", move_id)
    move_vals = {'additional_notes': move['x_studio_additional_notes'],
                 'enter_tracking_': move['x_studio_enter_tracking_'],
                 'incoterm': move['x_studio_incoterm']}
    models.execute_kw(db, uid, password, 'account.move', 'write', [[move_id], move_vals])

#=================================account.move.line============================================
move_line_studio_field_list = ['x_studio_line_item_from_sales_order_entry', 'x_studio_po_','journal_id']

move_line_studio_data = models.execute_kw(db, uid, password, 'account.move.line', 'search_read',
                                          [[]], {'fields': move_line_studio_field_list, 'order': 'id'})
print("\n\n====Total records for account.move.line ==", len(move_line_studio_data))

bank_journals =  models.execute_kw(db, uid, password, 'account.journal', 'search_read',
                                          [[('type','=','bank')]], {'fields':['id'], 'order': 'id'})
cash_journals =  models.execute_kw(db, uid, password, 'account.journal', 'search_read',
                                          [[('type','=','cash')]], {'fields':['id'], 'order': 'id'})

count = 0
for move_line in move_line_studio_data:
    count = count + 1
    move_line_id = move_line['id']
    print("\n\n=======count=======", count, "=====move_line_id====", move_line_id)
    move_line_vals = {'line_item_from_sales_order_entry': move_line['x_studio_line_item_from_sales_order_entry'],
                      'po_': move_line['x_studio_po_']}

    if move_line['journal_id'][0] not in [bank_journals[0]['id'],cash_journals[0]['id']] :
        models.execute_kw(db, uid, password, 'account.move.line', 'write', [[move_line_id], move_line_vals])

#===========================product.supllierinfo=======================================================
product_supplierinfo_studio_field_list = ['x_studio_vendor_spec_part_notes']

product_supplierinfo_studio_data = models.execute_kw(db, uid, password, 'product.supplierinfo', 'search_read',
                                                     [[]],
                                                     {'fields': product_supplierinfo_studio_field_list, 'order': 'id'})
print("\n\n====Total records for product.supplierinfo ==", len(product_supplierinfo_studio_data))

count = 0
for supplierinfo in product_supplierinfo_studio_data:
    count = count + 1
    supplierinfo_id = supplierinfo['id']
    print("\n\n=======count=======", count, "=====supplierinfo_id====", supplierinfo_id)
    supplierinfo_vals =  {'vendor_spec_part_notes': supplierinfo['x_studio_vendor_spec_part_notes']}

    models.execute_kw(db, uid, password, 'product.supplierinfo', 'write', [[supplierinfo_id], supplierinfo_vals])



#==============================================mrp.bom=================================================
mrp_bom_studio_field_list = ['x_studio_process_notes', 'x_studio_product_description',
                             'x_studio_work_center_note_for_reporting']

mrp_bom_studio_data = models.execute_kw(db, uid, password, 'mrp.bom', 'search_read',
                                        [[]],
                                        {'fields': mrp_bom_studio_field_list, 'order': 'id'})
print("\n\n====Total records for mrp.bom ==", len(mrp_bom_studio_data))

count = 0
for bom in mrp_bom_studio_data:
    count = count + 1
    bom_id = bom['id']
    print("\n\n=======count=======", count, "=====bom_id====", bom_id)
    bom_vals = {'process_notes': bom['x_studio_process_notes'],
                'product_description': bom['x_studio_product_description'],
                'work_center_note_for_reporting': bom['x_studio_work_center_note_for_reporting']
                }
    models.execute_kw(db, uid, password, 'mrp.bom', 'write', [[bom_id], bom_vals])

#============================mrp.production==============================================================
mrp_production_studio_field_list = ['x_studio_confirmed_completion_date',
                                    'x_studio_mfg_order_notes_for_pdf_report',
                                    'x_studio_trevor_notes',
                                    'x_studio_senasys_division']

mrp_production_studio_data = models.execute_kw(db, uid, password, 'mrp.production', 'search_read',
                                               [[]],
                                               {'fields': mrp_production_studio_field_list, 'order': 'id'})
print("\n\n====Total records for mrp.production ==", len(mrp_production_studio_data))

count = 0
for production in mrp_production_studio_data:
    count = count + 1
    production_id = production['id']
    print("\n\n=======count=======", count, "=====production_id====", production_id)
    production_vals = {'confirmed_completion_date': production['x_studio_confirmed_completion_date'],
                       'mfg_order_notes_for_pdf_report': production['x_studio_mfg_order_notes_for_pdf_report'],
                       'trevor_notes': production['x_studio_trevor_notes'],
                       'senasys_division': production['x_studio_senasys_division']}
    models.execute_kw(db, uid, password, 'mrp.production', 'write', [[production_id], production_vals])

#==================================purchase.order============================================

# update purchase order x_studio_select
studio_data = models.execute_kw(db, uid, password, 'purchase.order', 'search_read',
                                               [[('x_studio_select','=',' ')]],
                                               {'fields': ['x_studio_select'], 'order': 'id'})
print("\n\n=====studio_data===",len(studio_data))
if studio_data:
    for s_data in studio_data:
        print("\n\n====s_data['id']====",s_data['id'])
        models.execute_kw(db, uid, password, 'purchase.order', 'write', [[s_data['id']], {'x_studio_select':''}])

purchase_order_studio_field_list = ['x_studio_drop_ship_to_vendor',
                                    'x_studio_po_notes',
                                    'x_studio_po_notes_internal_use_only',
                                    'x_studio_purchase_order_closed',
                                    'x_studio_request_date',
                                    'x_studio_requested_delivery_method',
                                    'x_studio_select',
                                    'x_studio_senasys_buyer',
                                    'x_studio_vendor_drop_ship_enter_address_below',
                                    'x_studio_senasys_division']

purchase_order_studio_data = models.execute_kw(db, uid, password, 'purchase.order', 'search_read',
                                               [[]],
                                               {'fields': purchase_order_studio_field_list, 'order': 'id'})
print("\n\n====Total records for purchase.order ==", len(purchase_order_studio_data))


count = 0
for order in purchase_order_studio_data:
    count = count + 1
    order_id = order['id']
    print("\n\n=======count=======", count, "=====order_id====", order_id)
    order_vals = {'drop_ship_to_vendor': order['x_studio_drop_ship_to_vendor'][0] if order['x_studio_drop_ship_to_vendor'] else False,
                  'po_notes': order['x_studio_po_notes'],
                  'po_notes_internal_use_only': order['x_studio_po_notes_internal_use_only'],
                  'purchase_order_closed': order['x_studio_purchase_order_closed'],
                  'request_date': order['x_studio_request_date'],
                  'requested_delivery_method': order['x_studio_requested_delivery_method'],
                  'select_': order['x_studio_select'],
                  'senasys_buyer': order['x_studio_senasys_buyer'],
                  'vendor_drop_ship_enter_address_below': order['x_studio_vendor_drop_ship_enter_address_below'],
                  'senasys_division': order['x_studio_senasys_division']
                  }
    models.execute_kw(db, uid, password, 'purchase.order', 'write', [[order_id], order_vals])


#=================================stock.picking==============================================
stock_picking_studio_field_list = ['x_studio_override_shipment_method',
                                   'x_studio_ship_method_for_this_delivery',
                                   'x_studio_cust_collect_acct',
                                   'x_studio_po_tag_',
                                   'x_studio_shipment_delivery_notes']

stock_picking_studio_data = models.execute_kw(db, uid, password, 'stock.picking', 'search_read',
                                              [[]],
                                              {'fields': stock_picking_studio_field_list, 'order': 'id'})
print("\n\n====Total records for stock.picking ==", len(stock_picking_studio_data))

count = 0
for picking in stock_picking_studio_data:
    count = count + 1
    picking_id = picking['id']
    print("\n\n=======count=======", count, "=====picking_id====", picking_id)
    picking_vals = {'override_shipment_method': picking['x_studio_override_shipment_method'],
                    'ship_method_for_this_delivery': picking['x_studio_ship_method_for_this_delivery'],
                    'cust_collect_acct': picking['x_studio_cust_collect_acct'],
                    'po_tag_': picking['x_studio_po_tag_'],
                    'shipment_delivery_notes': picking['x_studio_shipment_delivery_notes']
                    }
    models.execute_kw(db, uid, password, 'stock.picking', 'write', [[picking_id], picking_vals])

#===================================stock.scrap=================================================
stock_scrap_studio_field_list = ['x_studio_general_notes']

stock_scrap_studio_data = models.execute_kw(db, uid, password, 'stock.scrap', 'search_read',
                                            [[]],
                                            {'fields': stock_scrap_studio_field_list, 'order': 'id'})
print("\n\n====Total records for stock.scrap ==", len(stock_scrap_studio_data))

count = 0
for stock in stock_scrap_studio_data:
    count = count + 1
    stock_id = stock['id']
    print("\n\n=======count=======", count, "=====stock_id====", stock_id)
    stock_vals = {'general_notes': stock['x_studio_general_notes']}
    models.execute_kw(db, uid, password, 'stock.scrap', 'write', [[stock_id], stock_vals])


#============================================================================================================

end = time.time()
print("\n\n====Total execution time=====", end - start)

