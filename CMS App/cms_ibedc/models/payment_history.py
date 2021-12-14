
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields, models
    
class PaymentHistory(models.Model):
    _name = 'payment.history'
    payment_root_id = fields.Many2one('res.partner')
    timestamp = fields.Date(string='Timestamp',required=True)
    initiation_date = fields.Date(string='Initiation Date',required=True)
    confirmation_date = fields.Date(string='Confirmation Date',required=True)
    transaction_id = fields.Char(string='Transaction ID',required=True)
    transaction_refr = fields.Char(string='Transaction Ref',required=True)
    tx_message = fields.Text(string='Status Message',required=True)#Char
    gross_amount = fields.Integer(string='Gross Amount',required=True)
    net_amount = fields.Integer(string='Net Amount',required=True)
    units_consumed = fields.Integer(string='Units Consumed',required=True)