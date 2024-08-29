{
    'name': 'Price hide for Public User',
    'version': '15.0.1.0.0',
    'category': 'Partner',
    'license': 'LGPL-3',
    'author': 'BV',
    'website': '',
    'summary': 'This module helps to hide the website price for Public User',
    'depends': [
        'website_sale',
    ],
    'data': [
        'views/inherit_web_template.xml',
        'views/unnecessary_field_hide.xml',
        'data/public_user_mail_template.xml',
    ],
    "qweb": ["static/src/xml/website_sale_templates.xml"],
    "installable": True,
    "assets": {
        "web.assets_frontend": [
            "bv_web_price_hide_changes/static/src/js/custom_cart.js",
            "bv_web_price_hide_changes/static/src/js/website_sale_hide_price.js",
            "bv_web_price_hide_changes/static/src/js/website_customise_add_to_cart.js",
        ]
    },
}
