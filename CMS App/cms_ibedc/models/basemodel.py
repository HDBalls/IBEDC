# -*- coding: utf-8 -*-
# This model Inherits from the Users Model

from odoo import api, models, modules,fields, models

class BaseDeclarative(models.Model):
    _inherit = 'res.partner'

    account_no = fields.Char(string='Account Number')
    last_vending = fields.Date(string='Last Vend Date')
    last_vend_amount = fields.Char(string='Last Vend Amount')
    account_type = fields.Char(string='Account Type')
    discoName = fields.Char(string='Disco')
    accountID = fields.Char(string='Account ID')
    creation_date = fields.Char(string='Creation Date')
    has_tenant = fields.Char(string='Has Tenant')
    tname = fields.Char(string='Tenant Name')
    tphone = fields.Char(string='Tenant Phone')
    lname = fields.Char(string='Landlord Name')
    lphone = fields.Char(string='Landlord Phone')
    tarrif_category = fields.Char(string='Tariff Category')
    tarrif_class = fields.Char(string='Tariff Class')
    tarrif_rate = fields.Float(string='Tariff Rate')
    CIN = fields.Char(string='Nerc Customer Id')
    is_metered = fields.Char(string='Reading Method')
    is_prepaid = fields.Char(string='Billing Method')
    meter_type = fields.Char(string='Meter Type')
    meter_oem = fields.Char(string='Meter OEM')
    meter_model = fields.Char(string='Meter Model')
    meter_number = fields.Char(string='Meter Number')
    bal_energy = fields.Float(string='Energy Balance')
    bal_cash = fields.Float(string='Cash Balance')
    billing_history = fields.One2many('billing.history','bill_root_id')
    payment_history = fields.One2many('payment.history','payment_root_id')
    customer_complaints = fields.One2many('customer.complaints','complaints_root_id')
    property_type = fields.Selection([('landlord', 'Landlord'), ('tenant', 'Tenant')], default='landlord')
    geo_coordinates = fields.Char(string='Geolocation Coordinates')
    dummy_asset = fields.Char(string='Dummy Asset')
