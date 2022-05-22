from odoo import api, models, modules,fields, models



class EventsTable(models.Model):
    _name = 'respartner.event'
    
    account_no	= fields.Char(string='Tarrif code')
    name	= fields.Char(string='Account type')
    fields_changed	= fields.Char(string='Description')
    timestamp = fields.Char(string='Added date')
    
    