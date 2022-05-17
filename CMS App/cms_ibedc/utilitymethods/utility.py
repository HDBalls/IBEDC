
import time
import os, uuid,base64, json
from ..cryptography.fernet import Fernet
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
            print("===============================================================",message, type(message))
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
    
    