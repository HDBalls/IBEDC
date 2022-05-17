# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details...
{
    'name': 'Ibedc Customers',
    'category': 'Sales/CRM',
    'sequence': -100,
    'summary': 'Centralize your address book',
    'description': 
                    """
                    This module gives you a quick view of your contacts directory, accessible from your home page.
                    You can track your vendors, customers and other contacts.
                    """,
    'depends': ['base', 'mail','web','website'],
    "qweb":[
            'static/src/xml/hidemenu.xml',
            'static/src/xml/loginpage.xml'
            ],
    'data': [
            #'security/ir.model.access.csv',
            # 'data/database_selector.xml',
            
            'data/add_states.xml',
            'views/contact_views.xml',
            'views/billing_history.xml',
            'views/complaints_history.xml',
            'views/payment_history.xml',
            'views/modify_fields.xml',
            'views/customer_profile.xml',
            'views/customer_assets.xml',
            'views/geolocation.xml',
            'security/security.xml',
            'views/js_css_loader.xml',
            'views/dashboard_ui.xml',
            'views/customers_ui.xml',
            'views/customer_details_ui.xml',
            'views/billing_history_ui.xml',
            'views/payment_history_ui.xml',
            'views/404notfound_ui.xml',
            # 'views/footer.xml'
            ],
    'application': True,
}
