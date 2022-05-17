# -*- coding: utf-8 -*-
# This model Inherits from the Users Model
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
    bal_energy = fields.Float(string='Energy Balance')
    bal_cash = fields.Float(string='Outstanding Amount')
    billing_history = fields.One2many('billing.history','bill_root_id')
    payment_history = fields.One2many('payment.history','payment_root_id')
    customer_complaints = fields.One2many('customer.complaints','complaints_root_id')
    property_type = fields.Selection([('landlord', 'Landlord'), ('tenant', 'Tenant')], default='landlord')
    geo_coordinates = fields.Char(string='Geolocation Coordinates')
    rowguid = fields.Char(string='Row Guid')
    dummy_asset = fields.Char(string='Dummy Asset')
    booknumber = fields.Char(string='Book Number')
    oldaccountnumber = fields.Char(string='Old Account Number')
    title = fields.Char(string='Title(s)')
    surname = fields.Char(string='Surname')
    firstname = fields.Char(string='Firstname')
    othernames = fields.Char(string='Othernames')
    address1 = fields.Char(string='Address 1')
    address2 = fields.Char(string='Address 2')
    serviceaddress1 = fields.Char(string='Service Address 1')
    serviceaddress2 = fields.Char(string='Service Address 2')
    serviceaddresscity = fields.Char(string='Service Address city')
    serviceaddressstate_formated = fields.Char(string='Service Address State formatted')
    serviceaddressstate = fields.Char(string='Service Address State')
    tariffidarrearsbalance = fields.Char(string='Tariffid Arrears Balance')
    methodofidentification = fields.Char(string='methodofidentification')
    accttypedesc = fields.Char(string='Account Type Description')
    schedulebillno = fields.Char(string='Schedule Bill No')
    vat = fields.Char(string='Vat')
    applicationdate = fields.Char(string='Application Date')
    placeofwork = fields.Char(string='Place Of Work')
    addressoforganisation = fields.Char(string='Address Of Organisation')
    giscoordinate = fields.Char(string='Dummy Asset')
    guarantorname = fields.Char(string='Guarantor name')
    guarantoraddress  = fields.Char(string='Guarantor Address')
    organisationcode = fields.Char(string='Organisation Code')
    institutioncode = fields.Char(string='Institution Code')
    setupdate = fields.Char(string='Setup Date')
    connectdate = fields.Char(string='')
    distributionstation = fields.Char(string='Distribution Station')
    injectionstation = fields.Char(string='Injection Station')
    
    upriserno = fields.Char(string='Upriser NO')
    utid = fields.Char(string='Utid')
    buid = fields.Char(string='Buid')
    transid = fields.Char(string='Transformer ID')
    operatorname = fields.Char(string='Operator Name')
    password = fields.Char(string='Password')
    statuscode = fields.Char(string='Status Code')
    adc = fields.Char(string='ADC')
    storedaverage = fields.Char(string='Stored Average')
    connectiontype = fields.Char(string='Connection Type')
    useadc = fields.Char(string='')
    isbulk = fields.Char(string='')
    distributionid = fields.Char(string='Distribution Id')
    newsetupdate = fields.Char(string='')
    iscapmi = fields.Char(string='')
    operatoredits = fields.Char(string='')
    operatoredit = fields.Char(string='')
    cat = fields.Char(string='')
    isconfirmed = fields.Char(string='')
    confirmby = fields.Char(string='')
    dateconfirm = fields.Char(string='')
    nac = fields.Char(string='')
    backbalance = fields.Char(string='Back Balance')
    gis = fields.Char(string='GIS')
    customerid = fields.Char(string='Customer Id')
    atmaccountno = fields.Char(string='Atm Account No')
    newtariffcode = fields.Char(string='Tarrif Code')
    dss_id = fields.Char(string='Dss ID')
    servicecenter = fields.Char(string='Service Center')
    
    oldaccountno = fields.Char(string='Old Account No')
    opendate = fields.Char(string='Open Date')
    website = fields.Char(string='')
    arrearsbalance = fields.Char(string='Arrears Balance')
    operatorname = fields.Char(string='Operator name')
    fingerprintrawdata2 = fields.Char(string='')
    activated = fields.Char(string='')
    status = fields.Char(string='')
    status1 = fields.Char(string='')
    operatormodified = fields.Char(string='')
    lastmodifieddate = fields.Char(string='')
    modifiedcount = fields.Char(string='')
    
    #MSMS
    meter_model = fields.Char('Meter Model',compute="function_name", store=True)
    meter_type = fields.Char('Meter Type')
    meter_oem = fields.Char('Meter OEM')
    meter_number = fields.Char('Meter Number')
    meter_manufacturer	= fields.Char(string='Meter Manufacturer')
    manufacture_year = fields.Char(string='Manufacture year')
    meter_rating= fields.Char(string='Meter rating')
    v_rating = fields.Char(string='Voltage rating')
    meter_classification = fields.Char(string='Classification')
    kct	= fields.Char(string='KCT')
    supplier = fields.Char(string='SUpplier')
    meter_category	= fields.Char(string='Meter category')
    meter_type_id	= fields.Char(string='Meter type id')
    audit_validated_by	= fields.Char(string='Audit validated  by')
    audit_validated_date	= fields.Char(string='Audit validated date')
    billing_validated_by	= fields.Char(string='Billing validated by')
    billing_validated_date	= fields.Char(string='Billing validated date')
    rev_validated_by = fields.Char(string='Rev validated by')	
    rev_validated_date = fields.Char(string='Rev validated date')
    
    def function_name(self):
        cr = self._cr
        try:
            print("\n\n\n\n\n\n\nAccount no ",self.account_no,self._rec_name)
            if self.meter_number != False:
                query = f"select * from meter_model where meter_number='{self.meter_number}';"
                print(query)
                cr.execute(query)
                temp = cr.dictfetchone()
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nmeter val: ", temp)
                meter_model = temp['meter_model']
                meter_type = temp['meter_type']
                meter_manufacturer = temp['meter_manufacturer']
                manufacture_year = temp['manufacture_year']
                meter_rating= temp['meter_rating']
                v_rating = temp['v_rating']
                meter_classification = temp['meter_classification']
                kct	= temp['kct']
                supplier = temp['supplier']
                meter_category	= temp['meter_category']
                meter_type_id	= temp['meter_type_id']
                audit_validated_by	= temp['audit_validated_by']
                audit_validated_date	= temp['audit_validated_date']
                billing_validated_by	= temp['billing_validated_by']
                billing_validated_date	= temp['billing_validated_date']
                rev_validated_by = temp['rev_validated_by']
                rev_validated_date = temp['merev_validated_dateter_type']
                
                for rec in self:
                    rec.meter_model = meter_model or ''
                    self.meter_type = meter_type or ''
                    self.meter_manufacturer = meter_manufacturer or ''
                    self.manufacture_year = manufacture_year or ''
                    self.meter_rating= meter_rating or ''
                    self.v_rating = v_rating or ''
                    self.meter_classification = meter_classification or ''
                    self.kct	= kct or ''
                    self.supplier = supplier or ''
                    self.meter_category	= meter_category or ''
                    self.meter_type_id	= meter_type_id or ''
                    self.audit_validated_by	= audit_validated_by or ''
                    self.audit_validated_date = audit_validated_date or ''
                    self.billing_validated_by = billing_validated_by or ''
                    self.billing_validated_date	= billing_validated_date or ''
                    self.rev_validated_by = rev_validated_by or ''
                    self.rev_validated_date = rev_validated_date or ''
                    
                return
            
            else:
                for rec in self:
                    rec.meter_model = ''
                    rec.meter_type =  ''
                    self.manufacture_year = ''
                    self.meter_rating= ''
                    self.v_rating = ''
                    self.meter_classification = ''
                    self.kct	= ''
                    self.supplier = ''
                    self.meter_category	= ''
                    self.meter_type_id	= ''
                    self.audit_validated_by	= ''
                    self.audit_validated_date	= ''
                    self.billing_validated_by	= ''
                    self.billing_validated_date	= ''
                    self.rev_validated_by = ''
                    self.rev_validated_date = ''
                return
        except:
            pass
    
    
    
    # ECMI
    
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
        # print("\n\n\nQuerying database for all customers")
        data = self.env['res.partner'].search([])
        for i in self:
            print(i.name,i.state,i.country,i.account_no)


    def ParseFloat(self,value):
        try:
            return int(float(value))
        except Exception as e:
            return value
    