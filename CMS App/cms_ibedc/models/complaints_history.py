# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, modules, fields, models

class Complaints(models.Model):
    _name = 'customer.complaints'
    
    complaints_root_id = fields.Many2one('res.partner',ondelete='cascade')
    ticket_id = fields.Char(string='Ticket ID')
    category = fields.Char(string='Category',required=True)
    sub_category = fields.Char(string='Sub Category',required=True)
    summary = fields.Char(string='Summary',required=True)
    description = fields.Text(string='Description',required=True)
    address = fields.Char(string='Address',required=True)
    status = fields.Char(string='Status',required=True)
    date_created = fields.Date(string='Date Created',required=True)

    