from odoo import api, models, modules,fields, models

class MeterModel(models.Model):
    _name = 'meter.model'
    # _rec_name = "meter_number"
    
    req_type = fields.Char(string='Req type')
    batchid	= fields.Char(string='Batch id')
    oldbatchid	= fields.Char(string='Old batch id')
    meter_number = fields.Char(string='Meter number')
    meter_model	= fields.Char(string='Meter model')
    account_no = fields.Char(string='Account number', related='meter_number', store=True)
    meter_manufacturer	= fields.Char(string='Meter Manufacturer')
    manufacture_year = fields.Char(string='Manufacture year')
    meter_type	= fields.Char(string='Meter type')
    meter_rating= fields.Char(string='Meter rating')
    v_rating = fields.Char(string='Voltage rating')
    meter_classification = fields.Char(string='Classification')
    kct	= fields.Char(string='KCT')
    supplier = fields.Char(string='SUpplier')
    meter_category	= fields.Char(string='Meter category')
    meter_type_id	= fields.Char(string='Meter type id')
    ecmi_exported	= fields.Char(string='Timestamp')
    deployed = fields.Char(string='Deployed')
    addedby	= fields.Char(string='Added by')
    supplierstoreid	= fields.Char(string='Supplier store id')
    supplierstoretype	= fields.Char(string='Supplier store type')
    currentstorelevel	= fields.Char(string='Current store level')
    storeowner	= fields.Char(string='Store owner')
    owner_type	= fields.Char(string='Owner type')
    audit_validated_by	= fields.Char(string='Audit validated  by')
    audit_validated_date	= fields.Char(string='Audit validated date')
    billing_validated_by	= fields.Char(string='Billing validated by')
    billing_validated_date	= fields.Char(string='Billing validated date')
    rev_validated_by = fields.Char(string='Rev validated by')	
    rev_validated_date = fields.Char(string='Rev validated date')
    