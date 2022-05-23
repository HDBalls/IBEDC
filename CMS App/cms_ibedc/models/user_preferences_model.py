from odoo import api, models, modules,fields, models

class UserPreferences(models.Model): #This table stores the columns and fields a user wants visible in his workspace
    _name = 'user.preferences'
    
    user_id = fields.Many2one('res.users',ondelete='cascade')
    
    customerstransientviews	= fields.Char(string='',default='null')
    billing_main_page	= fields.Char(string='',default='null')
    payments_main_page	= fields.Char(string='',default='null')
    personal_info_page = fields.Char(string='',default='null')
    cust_billing_page = fields.Char(string='',default='null')
    cust_payment_page = fields.Char(string='',default='null')
    cust_metering_page	= fields.Char(string='',default='null')
    cust_assets_page	= fields.Char(string='',default='null')