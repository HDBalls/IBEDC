from odoo import api, fields, models,tools
import csv,os
import datetime
my_path = os.path.abspath(os.path.dirname(__file__))
my_path = my_path.replace("\\", "/")
my_path = my_path.rsplit('/', 1)[0]

class BillingHistory(models.Model):
    _name = 'billing.history'
    
    bill_root_id = fields.Many2one('res.partner',ondelete='cascade')
    bill_id = fields.Char(string='Bill ID')
    tarrif_name = fields.Char(string='Tarrif Name')
    period = fields.Char(string='Billing date')
    total_usage = fields.Char(string='Total Usage')
    total_amount = fields.Char(string='Total Amount')
    billing_purpose = fields.Text(string='Billing Purpose')
    _sql_constraints = [('bill_id_unique','unique(bill_id)','Bill id already exists')]
    
    
    