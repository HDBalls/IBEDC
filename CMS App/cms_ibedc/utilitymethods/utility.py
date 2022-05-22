
import time
import os, uuid,base64, json
from cryptography.fernet import Fernet
from odoo import http
from odoo.http import request
key = "5CWvxbkxPI2e0W2KRc1l4ZXMXRn7WJzdGP9NZhbbVgA="


class User:
    
    def isUserExist(uid,login):
        
        request.env['res.users']
        query = f"""SELECT id, login from res_users WHERE id = '{uid}';"""
        http.request.cr.execute(query)
        user = request.cr.dictfetchone()
        print('User login check',user['login'], login)
        if user['login'] == login:
            print("\n\n\nPass:==> Checked if user exists in the database ", user)
            return True
        
        return False
    
class Encryption(object):
    
    def Bytes(string):
        return string.encode('utf-8')
    
    def encryptMessage(message):
        
        fernet = Fernet(key)
        encMessage = fernet.encrypt(message.encode('utf-8'))
        # print("original string: ", message)
        # print("encrypted string: ", encMessage)
        # _ = str(encMessage.decode('utf-8')).count("=")
        __ = str(encMessage.decode('utf-8')).replace("=",'@')
        return __

    def decryptMessage(message):
        
        try:
            bytekey = Encryption.Bytes(key)
            fernet = Fernet(bytekey)
            message = message.replace("@",'=')
            message = message.encode('utf-8')
            # print("===============================================================",message, type(message))
            decMessage = fernet.decrypt(message)
            decMessage = decMessage.decode('utf-8')
            # print("----------------------",decMessage)
            return decMessage
        except Exception as e:
            print("\n\n\nException occured during decryption ", e)
    
    

class Serializables(object):
    
    def jsonSerializer(obj):
        from datetime import date, datetime
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        pass
    
class TransientFields(object):
    #THESE FIELDS ARE THE FIELDS TO APPEAR IN TRANSIENTS DROPDOWN
    def loadUserTransientFields(view):
        http.request.env['res.users']
        current_user = request.env['res.users'].browse(request.session.uid)
        # http.request.env['user.preferences']
        print(f"\n\n\nGetting current user preferences from DB ",current_user.name, current_user.id)
        try:    
            http.request._cr.execute(f"""select {view} from user_preferences where user_id = '{current_user.id}';""")
            data =  http.request._cr.fetchone()
            if data is not None:
                print("User preferences from Database",data)
                preferences = json.loads(data[0])
                return [k for k,v in preferences.items() if v ==True]
            
        except Exception as e:
            print(e)

    transient_fields = ['Name', 'Mobile', 'Email', 'Address 1', 'City', 'Account No', 'Account Type', 
                        'Outstanding Amount', 'Address 2', 'Meter Model', 'Meter Type', 'Meter Number', 
                        'Meter Manufacturer', 'Manufacture Year', 'Meter Rating', 'Application Date', 
                        'Giscoordinate', 'Guarantor Name', 'Guarantor Address', 'V Rating', 'Meter Class', 
                        'Meter Category', 'State', 'Meter Type_Id', 'Status Code'
                        ] 

    defaults =           ['Name', 'Mobile', 'Email', 'Address 1', 'Account No', 'Account Type', 
                        'Outstanding Amount', 'Meter Number', 'State','Status Code'
                        ] 
    
    field_names =       {'Mobile': 'mobile', 'Email': 'email', 'Address 1': 'address1', 'City': 'city', 
                         'Account No': 'account_no', 'Account Type': 'account_type', 'Outstanding Amount': 'bal_cash', 
                         'Address 2': 'address2', 'Meter Model': 'meter_model', 'Meter Type': 'meter_type', 'Meter Number': 'meter_number',
                         'Meter Manufacturer': 'meter_manufacturer', 'Manufacture Year': 'manufacture_year', 'Meter Rating': 'meter_rating', 
                         'Application Date': 'applicationdate', 'Giscoordinate': 'giscoordinate', 'Guarantor Name': 'guarantorname', 'Guarantor Address': 'guarantoraddress',
                         'V Rating': 'v_rating', 'Meter Class': 'meter_classification', 'Meter Category': 'meter_category', 'State': 'state', 'Meter Type_Id': 'meter_type_id', 
                         'Status Code': 'statuscode'
                         }
    
    
class QuerySelectors(object):
    

    queryselectors_cust = ("""
                            
                            DISTINCT res_partner.id,
                            res_partner.name,
                            res_partner.mobile,
                            res_partner.email,
                            res_partner.city,
                            res_partner.account_no,
                            res_partner.statuscode,
                            res_partner.account_type,
                            res_partner.bal_cash,
                            res_partner.address1,
                            res_partner.address2,
                            res_partner.applicationdate,
                            res_partner.giscoordinate,
                            res_partner.guarantorname,
                            res_partner.guarantoraddress,
                            res_country_state.name as state,
                            
                            meter_model.meter_model,
                            meter_model.meter_type,
                            meter_model.meter_number,
                            meter_model.meter_manufacturer,
                            meter_model.manufacture_year,
                            meter_model.meter_rating,
                            meter_model.v_rating,
                            meter_model.meter_classification,
                            meter_model.meter_category,
                            meter_model.meter_type_id,
                            meter_model.audit_validated_by,
                            meter_model.audit_validated_date,
                            meter_model.billing_validated_by,
                            meter_model.billing_validated_date,
                            meter_model.rev_validated_by,
                            meter_model.rev_validated_date,
                            
                            gis_distribution_substation_all.assetid,
                            gis_distribution_substation_all.staffid,
                            gis_distribution_substation_all.assettype,
                            gis_distribution_substation_all.latitude,
                            gis_distribution_substation_all.longtitude,
                            gis_distribution_substation_all.dss_11kv_415v_parent,
                            gis_distribution_substation_all.dss_11kv_415v_owner,
                            gis_distribution_substation_all.dss_11kv_415v_name,
                            gis_distribution_substation_all.dss_11kv_415v_address,
                            gis_distribution_substation_all.dss_11kv_415v_rating,
                            gis_distribution_substation_all.dss_11kv_415v_upriser_number

                           """)
    
    