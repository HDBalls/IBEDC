
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields, models

class EmsPaymentTrans(models.Model):
    _name = 'emspayment.trans'

    
    # payment_trans_root_id = fields.Many2one('payment.history',ondelete='cascade',domain="[('payment_history.account_no','=', account_no)]")
    payment_trans_root_id = fields.Many2one('payment.history',ondelete='cascade')
    account_no = fields.Char(string='Account No')
    transaction_id = fields.Char(string='Transaction ID')
    transaction_refr = fields.Char(string='Transaction Ref')
    enteredby = fields.Char(string='Entered_by')#Char
    trans_date = fields.Char(string='Transaction Date')
    trans_amount = fields.Char(string='Transaction Amount')
    trans_status = fields.Char(string='Transaction Status',default='None')
    trans_response = fields.Char(string='Transaction Response')
    payment_type = fields.Char(string='Payment type')
    trans_business_unit = fields.Char(string='Transaction Business Unit')
    rowguid = fields.Char(string='Row guid')
