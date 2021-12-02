
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields, models
    
class PaymentHistory(models.Model):
    _name = 'payment.history'
    payment_root_id = fields.Many2one('res.partner')
    initiation_date = fields.Date(string='Initiation date',required=True)
    confirmation_date = fields.Date(string='Confirmation date',required=True)
    transaction_id = fields.Char(string='Transaction ID',required=True)
    transaction_refr = fields.Char(string='Transaction ref',required=True)#Char
    amount = fields.Integer(string='Amount',required=True)
    units_consumed = fields.Integer(string='Units consumed',required=True)