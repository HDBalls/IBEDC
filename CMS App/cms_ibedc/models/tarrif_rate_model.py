from odoo import api, models, modules,fields, models

class TarrifRateModel(models.Model):
    _name = 'tarrifrate.model'
    tarrif_rate_root_id = fields.Many2one('res.partner',ondelete='cascade')
    
    tariffid = fields.Char(string='Tarrif code')
    versionno = fields.Char(string='Tarrif code')
    rate = fields.Char(string='Tarrif code')
    mmf = fields.Char(string='Tarrif code')
    fc = fields.Char(string='Tarrif code')
    vat = fields.Char(string='Tarrif code')
    effectivedate = fields.Char(string='Tarrif code')
    status = fields.Char(string='Tarrif code')
    demandchg = fields.Char(string='Tarrif code')
    minimumchg = fields.Char(string='Tarrif code')
    rowguid = fields.Char(string='Tarrif code')
    serviceid = fields.Char(string='Tarrif code')