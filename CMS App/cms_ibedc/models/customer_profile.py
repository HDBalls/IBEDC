# -*- coding: utf-8 -*-
# This model Inherits from the Users Model

from email.policy import default

from numpy import full
from odoo import api, models, modules,fields, models, tools
titles = ['.','Mr', 'Mrs', 'Miss', 'Ms', 'Dr', '&', 'Admiral', 'Air', 'Comm', 'Ambassador', 'Baron', 'Baroness', 'Brig', 'Mrs', 'Brig', 'Gen', 'Brigadier', 'Brother', 'Canon', 'Capt', 'Chief', 'Cllr', 'Col', 'Commander', 'Commander', 'Mrs', 'Consul', 'Consul', 'General', 'Count', 'Countess', 'Countess', 'of', 'Cpl', 'Dame', 'Deputy', 'Dr', 'Mrs', 'Drs', 'Duchess', 'Duke', 'Earl', 'Father', 'General', 'Gräfin', 'HE', 'HMA', 'Her', 'Grace', 'His', 'Excellency', 'Ing', 'Judge', 'Justice', 'Lady', 'Lic', 'Llc', 'Lord', 'Lord', 'Lady', 'Lt', 'Lt', 'Col', 'Lt', 'Cpl', 'M', 'Madam', 'Madame', 'Major', 'Major', 'General', 'Marchioness', 'Marquis', 'Minister', 'Mme', 'Mr', 'Dr', 'Mr', 'Mrs', 'Mr', 'Ms', 'Prince', 'Princess', 'Professor', 'Prof', 'Prof', 'Dr', 'Prof', 'Mrs', 'Prof', 'Rev', 'Prof', 'Dame', 'Prof', 'Dr', 'Pvt', 'Rabbi', 'Rear', 'Admiral', 'Rev', 'Rev', 'Mrs', 'Rev', 'Canon', 'Rev', 'Dr', 'Senator', 'Sgt', 'Sir', 'Sir', 'Lady', 'Sister', 'Sqr.', 'Leader', 'The', 'Earl', 'of', 'The', 'Hon', 'The', 'Hon', 'Dr', 'The', 'Hon', 'Lady', 'The', 'Hon', 'Lord', 'The', 'Hon', 'Mrs', 'The', 'Hon', 'Sir', 'The', 'Honourable', 'The', 'Rt', 'Hon', 'The', 'Rt', 'Hon', 'Dr', 'The', 'Rt', 'Hon', 'Lord', 'The', 'Rt', 'Hon', 'Sir', 'The', 'Rt', 'Hon', 'Visc', 'Viscount']

class BaseDeclarative(models.Model):
    _inherit = 'res.partner'
    # _auto = False
    _rec_name = 'account_no'
    name = fields.Char(string='Fullname',required=False,readonly=False)
    account_no = fields.Char(string='Account Number')
    last_vending = fields.Date(string='Last Vend Date')
    last_vend_amount = fields.Char(string='Last Vend Amount')
    account_type = fields.Char(string='Account Type')
    discoName = fields.Char(string='Disco',default='IBEDC')
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
    # state= fields.Char(compute='_compute_total',store=True)
    
    # meter_db_model = fields.Many2one('meter.model', string='Meter info')
    # meter_type = fields.Char('Meter Type')
    # meter_oem = fields.Char('Meter OEM')
    # meter_model = fields.Char('Meter Model')
    # meter_number = fields.Char('Meter Number')
                             
    # meter_db_model = fields.Many2one('meter.model', string='Meter info')
    meter_db_model = fields.One2many('meter.model','meter_root_id')
    meter_type = fields.Char('Meter Type', related='meter_db_model.meter_type')
    meter_oem = fields.Char('Meter OEM')
    # meter_oem = fields.Char('Meter OEM', related='meter_db_model.meter_oem')
    meter_model = fields.Char('Meter Model', related='meter_db_model.meter_model')
    meter_number = fields.Char('Meter Number', related='meter_db_model.meter_number')
    
    bal_energy = fields.Float(string='Energy Balance')
    bal_cash = fields.Float(string='Outstanding Amount')
    billing_history = fields.One2many('billing.history','bill_root_id')
    payment_history = fields.One2many('payment.history','payment_root_id')
    customer_complaints = fields.One2many('customer.complaints','complaints_root_id')
    
    property_type = fields.Selection([('landlord', 'Landlord'), ('tenant', 'Tenant')], default='landlord')
    geo_coordinates = fields.Char(string='Geolocation Coordinates')
    rowguid = fields.Char(string='Row Guid')
    dummy_asset = fields.Char(string='Dummy Asset')
    
    def abbreviateName(self,fullname):
        abbr = []
        charsSymbol = ['#']
        charsUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        charsLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        titles = ['.','Alj','Alhaji','Alhaja','Mr', 'Mrs', 'Miss', 'Ms', 'Dr', '&', 'Admiral', 'Air', 'Comm', 'Ambassador', 'Baron', 'Baroness', 'Brig', 'Mrs', 'Brig', 'Gen', 'Brigadier', 'Brother', 'Canon', 'Capt', 'Chief', 'Cllr', 'Col', 'Commander', 'Commander', 'Mrs', 'Consul', 'Consul', 'General', 'Count', 'Countess', 'Countess', 'of', 'Cpl', 'Dame', 'Deputy', 'Dr', 'Mrs', 'Drs', 'Duchess', 'Duke', 'Earl', 'Father', 'General', 'Gräfin', 'HE', 'HMA', 'Her', 'Grace', 'His', 'Excellency', 'Ing', 'Judge', 'Justice', 'Lady', 'Lic', 'Llc', 'Lord', 'Lord', 'Lady', 'Lt', 'Lt', 'Col', 'Lt', 'Cpl', 'M', 'Madam', 'Madame', 'Major', 'Major', 'General', 'Marchioness', 'Marquis', 'Minister', 'Mme', 'Mr', 'Dr', 'Mr', 'Mrs', 'Mr', 'Ms', 'Prince', 'Princess', 'Professor', 'Prof', 'Prof', 'Dr', 'Prof', 'Mrs', 'Prof', 'Rev', 'Prof', 'Dame', 'Prof', 'Dr', 'Pvt', 'Rabbi', 'Rear', 'Admiral', 'Rev', 'Rev', 'Mrs', 'Rev', 'Canon', 'Rev', 'Dr', 'Senator', 'Sgt', 'Sir', 'Sir', 'Lady', 'Sister', 'Sqr.', 'Leader', 'The', 'Earl', 'of', 'The', 'Hon', 'The', 'Hon', 'Dr', 'The', 'Hon', 'Lady', 'The', 'Hon', 'Lord', 'The', 'Hon', 'Mrs', 'The', 'Hon', 'Sir', 'The', 'Honourable', 'The', 'Rt', 'Hon', 'The', 'Rt', 'Hon', 'Dr', 'The', 'Rt', 'Hon', 'Lord', 'The', 'Rt', 'Hon', 'Sir', 'The', 'Rt', 'Hon', 'Visc', 'Viscount']
        a = (map(lambda x: x.lower(), titles))
        p_titles = list(a)
        splittednames = fullname.split(' ')
        for name in splittednames:
            if name.lower() not in p_titles:
                if len(abbr) < 2:
                    if name[0] in charsUpper or name[0] in charsLower or name[0] in charsSymbol:
                        abbr.append(name)
                
        try:
            if len(abbr) == 0:
                pass
            
            if len(abbr) == 1:
                firstAbbr = abbr[0][0]
                return str(firstAbbr).upper()
            
            if len(abbr) == 2:
                firstAbbr = abbr[0][0]
                secondAbbr = abbr[1][0]
                return str(firstAbbr)+str(secondAbbr).upper()
            
        except:
            pass

    def _amount_insurance(self):
        self._cr.execute(f"""select name from res_country_state WHERE id={self.state_id}; """)
        result=self._cr.fetchall()
        print('\n\n\The result ',result[0][0])
        self.state = result[0][0]

    def getCustomers(self):
        print("\n\n\nQuerying database for all customers")
        data = self.env['res.partner'].search([])
        print('Transient Model data',data)
        for i in self:
            print(i.name,i.state,i.country,i.account_no)
    # accountno = fields.Char(string='Dummy Asset')
    # booknumber = fields.Char(string='Dummy Asset')
    # oldaccountnumber = fields.Char(string='Dummy Asset')
    # meterno = fields.Char(string='Dummy Asset')
    # title = fields.Char(string='Dummy Asset')
    # surname = fields.Char(string='Dummy Asset')
    # firstname = fields.Char(string='Dummy Asset')
    # othernames = fields.Char(string='Dummy Asset')
    # name = fields.Char(string='Dummy Asset')
    # address1 = fields.Char(string='Dummy Asset')
    # address2 = fields.Char(string='Dummy Asset')
    # city = fields.Char(string='Dummy Asset')
    # state = fields.Char(string='Dummy Asset')
    # email = fields.Char(string='Dummy Asset')
    # serviceaddress1 = fields.Char(string='Dummy Asset')
    # serviceaddress2 = fields.Char(string='Dummy Asset')
    # serviceaddresscity = fields.Char(string='Dummy Asset')
    # serviceaddressstate_formated = fields.Char(string='Dummy Asset')
    # serviceaddressstate = fields.Char(string='Dummy Asset')
    # tariffidarrearsbalance = fields.Char(string='Dummy Asset')
    # mobile = fields.Char(string='Dummy Asset')
    # methodofidentification = fields.Char(string='Dummy Asset')
    # accttypedesc = fields.Char(string='Dummy Asset')
    # schedulebillno = fields.Char(string='Dummy Asset')
    # vat = fields.Char(string='Dummy Asset')
    # applicationdate = fields.Char(string='Dummy Asset')
    # placeofwork = fields.Char(string='Dummy Asset')
    # addressoforganisation = fields.Char(string='Dummy Asset')
    # giscoordinate = fields.Char(string='Dummy Asset')
    # guarantorname
    # guarantoraddress
    # organisationcode
    # institutioncode
    # setupdate
    # connectdate
    # distributionstation
    # injectionstation
    # upriserno
    # utid
    # buid
    # transid
    # operatorname
    # password
    # statuscode
    # adc
    # storedaverage
    # connectiontype
    # useadc
    # isbulk
    # distributionid
    # newsetupdate
    # rowguid
    # iscapmi
    # operatoredits
    # operatoredit
    # cat
    # isconfirmed
    # confirmby
    # dateconfirm
    # nac
    # backbalance
    # gis
    # customerid
    
    # ecmi = field.status

    # atmaccountno
    # tariffid
    # oldaccountno
    # opendate
    # website
    # arrearsbalance
    # operatorname
    # fingerprintrawdata2
    # activated
    # status
    # status1
    # operatormodified
    # lastmodifieddate
    # modifiedcount
