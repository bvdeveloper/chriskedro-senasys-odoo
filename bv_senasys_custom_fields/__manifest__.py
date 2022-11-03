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
    # 'depends': ['base', 'product'],
    'depends': ['base', 'sale_management', 'purchase', 'account', 'product', 'stock', 'product_expiry', 'website', 'purchase_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/product_template.xml',
        'views/mrp_production.xml',
        'views/stock_picking.xml',
        'views/purchase_order.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/stock_scrap.xml',
        'views/product_supplierinfo.xml',
    ],
    'demo': [
    ],
    'images': [

    ],
    'css': [],
    'installable': True,
    'auto_install': True,
    'application': True,
}
