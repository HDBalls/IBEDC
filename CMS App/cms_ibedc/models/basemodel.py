# -*- coding: utf-8 -*-
# This model Inherits from the Users Model

from odoo import api, models, modules,fields, models

class BaseDeclarative(models.Model):
    _inherit = 'res.partner'

    # firstname = fields.Char(string='First name')
    # lastname = fields.Char(string='Last name')
    # other_name = fields.Char(string='Other name')
    
    account_no = fields.Char(string='Account Number')
    meter_number = fields.Char(string='Meter Number')
    last_vending = fields.Date(string='Last vend date')
    last_vend_amount = fields.Char(string='Last vend amount')
    account_type = fields.Char(string='Account type')
    billing_history = fields.One2many('billing.history','bill_root_id')
    payment_history = fields.One2many('payment.history','payment_root_id')
    customer_complaints = fields.One2many('customer.complaints','complaints_root_id')
