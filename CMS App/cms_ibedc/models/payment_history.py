
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields, models
    
class PaymentHistory(models.Model):
    _name = 'payment.history'
    payment_root_id = fields.Many2one('res.partner',ondelete='cascade')
    payment_id = fields.Char(string='Payment ID')
    transaction_id = fields.Char(string='Transaction ID')
    timestamp = fields.Char(string='Timestamp')
    initiation_date = fields.Char(string='Initiation Date')
    confirmation_date = fields.Char(string='Confirmation Date') #Should be Date field too, dirty data caused the change
    transaction_refr = fields.Char(string='Transaction Ref')
    tx_message = fields.Text(string='Status Message')#Char
    gross_amount = fields.Float(string='Gross Amount')
    net_amount = fields.Float(string='Net Amount')
    units_consumed = fields.Float(string='Units Consumed')
    _sql_constraints = [('transaction_id_unique','unique(transaction_id)','Transaction ID already exists')]