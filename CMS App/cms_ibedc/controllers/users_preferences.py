   
import json
from odoo import http
from odoo.http import request, Response
import datetime
from ..utilitymethods.utility import Serializables

class UserPreferences(http.Controller):

    @http.route('/cms/preferences/', csrf=False, auth="public")
    def Preferences(self,field,preferences,**kw):
        current_user = request.env['res.users'].browse(request.session.uid)
        try:    
            http.request._cr.execute(f"""select id from user_preferences where user_id = '{current_user.id}';""")
            data =  http.request._cr.fetchone()
            if data is not None:
                if len(data) > 0:
                    query = f"""update user_preferences set {field} = '{preferences}' where user_id = '{current_user.id}';"""
                    http.request._cr.execute(query)
                    response = {"status":True,"message":"Preferences were saved"}
                    return Response(json.dumps(response, default=Serializables.jsonSerializer),content_type='text/json;charset=utf-8',status=200)
                    
            else:
                timestamp = datetime.datetime.now()
                preferences = json.dumps(preferences)
                query = """INSERT INTO user_preferences (user_id,customersTransientViews,billing_main_page,payments_main_page,
                            personal_info_page,cust_billing_page,cust_payment_page,cust_metering_page,cust_assets_page,create_uid,
                            create_date,write_uid,write_date) VALUES ('%d','%s','%s','%s','%s','%s','%s','%s','%s','%d','%s','%d','%s')
                            """%(current_user.id,preferences,'null','null','null','null','null','null','null',1,timestamp,1,timestamp)

                http.request._cr.execute(query)
                response = {"status":True,"message":"Preferences were saved"}
                return Response(json.dumps(response, default=Serializables.jsonSerializer),content_type='text/json;charset=utf-8',status=200)
        except Exception as e:
                response = {"status":False,"message":"Preferences were not saved"}
                return Response(json.dumps(response, default=Serializables.jsonSerializer),content_type='text/json;charset=utf-8',status=200)

    