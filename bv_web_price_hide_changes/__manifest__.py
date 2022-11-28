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

    ],
    'installable': True,
    'auto_install': False,
}
