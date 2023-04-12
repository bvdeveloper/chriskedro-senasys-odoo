# -*- coding: utf-8 -*-

{
    'name': 'Senasys Fields',
    'version': '15.0',
    'category': 'Stock',
    'sequence': 10,
    'summary': 'Senasys Custom Field Install',
    'description': """
            Senasys Custom Field Install
            """,
    'author': 'Brainvire',
    'website': 'https://www.brainvire.com/',
    'depends':['base', 'sale_management', 'purchase', 'account', 'product', 'stock', 'product_expiry', 'purchase_stock', 'delivery'],
    'data': [
        'security/ir.model.access.csv',
        'views/picking_operation_template_inherit.xml',
        'views/res_partner.xml',
        'views/product_template.xml',
        'views/mrp_production.xml',
        'views/stock_picking.xml',
        'views/purchase_order.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/stock_scrap.xml',
        'views/stock_warehouse_orderpoint.xml',
        'views/purchase_order_ecm_reporting_view.xml',
        'views/ecm_sales_order_by_line_reporting_view.xml',
        'views/purchase_ecm_reporting_inherit_view.xml',
        'views/ecm_sales_order_by_line_inherit_view.xml',
        'views/purchase_order_report_inherit.xml',
        'views/purchase_order_rfq_report.xml',
        'views/sale_order_quotation_template_inherit.xml',
        'views/delivery_carrier.xml',
        'report/sale_order_acknowledgement_report.xml',
        'report/sale_order_internal_acknowledgement.xml',
        'report/quote_with_photo_report.xml',
        'report/report_action.xml',
    ],
    'demo': [
    ],
    'images': [

    ],
    'css': [],
    'installable': True,
    'license': 'LGPL-3',
    # 'auto_install': True,
    'application': False,
}
