from odoo import api, models, modules,fields, models

class TarrifModel(models.Model):
    _name = 'tarrif.model'
    tarrif_root_id = fields.Many2one('res.partner',ondelete='cascade')
    
    tariffCode	= fields.Char(string='Tarrif code')
    accountType	= fields.Char(string='Account type')
    description	= fields.Char(string='Description')
    addedDate = fields.Char(string='Added date')
    storedAverage = fields.Char(string='Stored average')
    isMD = fields.Char(string='Is MD')
    usageratio	= fields.Char(string='Usage ratio')
    rowguid	= fields.Char(string='Row guid')
    newTariffCode = fields.Char(string='New tarrif code')