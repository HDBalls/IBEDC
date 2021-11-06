# -*- coding: utf-8 -*-
# This model Inherits from the Users Model

from odoo import api, models, modules,fields, models

class BaseDeclarative(models.Model):
    _inherit = 'res.partner'

    account_no = fields.Char(string='Account Number',size=50)
    # meter_no = fields.Many2one('res.partner',string='bus_terminal_point') related to account_no, not to be used here
    last_vending = fields.Date(string='Last vend date')
    last_vend_amount = fields.Char(string='Last vend amount')
    account_type = fields.Char(string='Account type')
    billing_history = fields.One2many('billing.history','bill_root_id',readonly=True)
    payment_history = fields.One2many('payment.history','payment_root_id',readonly=True)
    customer_complaints = fields.One2many('customer.complaints','complaints_root_id',readonly=True)

