


# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields, models

class EmsPaymentTrans(models.Model):
    _name = 'emspayment.trans'
    
    ts_id = fields.Many2one('payment.history', compute='compute_stage', inverse='stage_inverse')
    stage_ids = fields.One2many('payment.history', 'trans_status')

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
    
    @api.depends('stage_ids')
    def compute_stage(self):
        if len(self.stage_ids) > 0:
            self.ts_id = self.stage_ids[0]

    def stage_inverse(self):
        if len(self.stage_ids) > 0:
            # delete previous reference
            stage = self.env['payment.history'].browse(self.stage_ids[0].id)
            # asset.stage_id = False
        # set new reference
        self.ts_id.stage_id = self
    

class PaymentHistory(models.Model):
    _name = 'payment.history'
    payment_root_id = fields.Many2one('res.partner',ondelete='cascade')
    payment_id = fields.Char(string='Payment ID')
    account_no = fields.Char(string='Account No')
    transaction_id = fields.Char(string='Transaction ID')
    timestamp = fields.Char(string='Timestamp')
    initiation_date = fields.Char(string='Initiation Date')
    confirmation_date = fields.Char(string='Confirmation Date') #Should be Date field too, dirty data caused the change...
    transaction_refr = fields.Float(string='Transaction Ref')
    tx_message = fields.Char('Transaction status')
    gross_amount = fields.Float(string='Gross Amount')
    net_amount = fields.Float(string='Net Amount')
    units_consumed = fields.Float(string='Units Consumed')
    trans_status = fields.Many2one('emspayment.trans', string='Transaction status')
    _sql_constraints = [('transaction_id_unique','unique(transaction_id)','Transaction ID already exists')]
    
    def asDict(self,value):
        print("\n\n\n\n\n\nValue : ",value)
        return {'status':self.value}
            
    def ParseFloat(self,value):
        print(int(value))
        return int(value)
    
    

