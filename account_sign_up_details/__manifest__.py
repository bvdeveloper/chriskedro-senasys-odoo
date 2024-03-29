{
    "name": "Website Signup Form Extend",
    "summary": """Add a mandatory field for users to share their contact and company during the sign up.""",
    "category": "Website",
    "version": "1.0.0",
    "sequence": 1,
    "author": "Brainvire Infotech Pvt. Ltd.",
    "depends": ['auth_signup'],
    "data": [
        'views/res_partner_view.xml',
        'views/account_details_template.xml',
    ],
    'license': 'LGPL-3',
    "application": False,
    "installable": True,
    "auto_install": False,
}
