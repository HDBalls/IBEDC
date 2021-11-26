# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'UContacts',
    'category': 'Sales/CRM',
    'sequence': -100,
    'summary': 'Centralize your address book',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'depends': ['base', 'mail','web'],
    "qweb":['static/src/xml/hidemenu.xml',
            'static/src/xml/loginpage.xml'
            ],
    'data': [
        
        'data/add_states.xml',
        'views/contact_views.xml',
        'views/billing_history.xml',
        'views/complaints_history.xml',
        'views/payment_history.xml',
        'views/modify_fields.xml',
        'security/security.xml'
        
    ],
    
    
    'application': True,
}
