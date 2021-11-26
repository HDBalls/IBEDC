# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, modules,fields, models

class BillingHistory(models.Model):
    _name = 'billing.history'
    bill_root_id = fields.Many2one('res.partner')
    bill_id = fields.Char(string='Bill ID',required=True)
    tarrif_name = fields.Char(string='Tarrif name',required=True)
    period = fields.Char(string='Period',required=True)
    total_usage = fields.Char(string='Total Usage',required=True)
    total_amount = fields.Char(string='Total amount',required=True)
    _sql_constraints = [('bill_id_unique','unique(bill_id)','Bill id already exists')]
