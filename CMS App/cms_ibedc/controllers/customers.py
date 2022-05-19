import json
from odoo import http
from odoo.http import request, Response
from ..utilitymethods.utility import Encryption, Serializables
from ..models.customer_profile import BaseDeclarative
from ..utilitymethods.utility  import QuerySelectors
from ..utilitymethods.utility import Encryption, User

class Customers(http.Controller):
    
    @staticmethod
    def getCustomers(queryParam='',limit=0):
        Customers = http.request.env['res.partner']
        if queryParam == '':
            #The below query is to get a particular customer and all his  meter details
            # query = f"""SELECT {QuerySelectors.queryselectors_cust} 
            #             FROM
                        
	        #                 res_partner
	
            #             JOIN meter_model ON res_partner.meter_number = meter_model.meter_number
            #             order by name
            #             ;"""
            total_customers = http.request.env['res.partner'].search_count([])  
            print("\n\n\nTotal customers ",total_customers) 
            query = f"""SELECT 
                                {QuerySelectors.queryselectors_cust} 
                        FROM

                            res_partner
                            
                        LEFT OUTER JOIN res_country_state on res_partner.state_id = res_country_state.id
                        LEFT OUTER JOIN meter_model ON res_partner.meter_number = meter_model.meter_number
                        LEFT OUTER JOIN gis_distribution_substation_all on res_partner.dss_id = gis_distribution_substation_all.assetid
                        ORDER BY name;
                        
                        ;"""
            http.request.cr.execute(query)
            customers_list = request.cr.dictfetchall()
            megalist = []
            if customers_list:
                for single_dict in customers_list:
                    # print(single_dict,type(single_dict))
                
    
                    url = json.dumps([{'name':single_dict['name'],'mobile':single_dict['mobile'],'email':single_dict['email'],'city':single_dict['city'],'address1':single_dict['address1'],
                                        'account_no':single_dict['account_no'],'account_type':single_dict['account_type'],'outstanding_amnt':single_dict['bal_cash'],'address2':single_dict['address2'],
                                        'meter_model':single_dict['meter_model'],'meter_model':single_dict['meter_model'],'meter_type':single_dict['meter_type'],'meter_number':single_dict['meter_number'],
                                        'meter_manufacturer':single_dict['meter_manufacturer'],'manufacture_year':single_dict['manufacture_year'],'meter_rating':single_dict['meter_rating'],
                                        
                                        'applicationdate':single_dict['applicationdate'],'giscoordinate':single_dict['giscoordinate'],'guarantorname':single_dict['guarantorname'],'guarantoraddress':single_dict['guarantoraddress'],
                                        
                                        'v_rating':single_dict['v_rating'],'meter_classification':single_dict['meter_classification'],'meter_category':single_dict['meter_category'],'state':single_dict['state'],
                                        'meter_type_id':single_dict['meter_type_id'],'meter_type_id':single_dict['meter_type_id'],'meter_type_id':single_dict['meter_type_id'],'statuscode':single_dict['statuscode'],
                                        'audit_validated_by':single_dict['audit_validated_by'],'audit_validated_date':single_dict['audit_validated_date'],'billing_validated_by':single_dict['billing_validated_by'],
                                        'billing_validated_date':single_dict['billing_validated_date'],'rev_validated_by':single_dict['rev_validated_by'],'rev_validated_date':single_dict['rev_validated_date'],
                                        'assetid':single_dict['assetid'],'staffid':single_dict['staffid'],'assettype':single_dict['assettype'],'latitude':single_dict['latitude'],'longtitude':single_dict['longtitude'],
                                        'dss_11kv_415v_parent':single_dict['dss_11kv_415v_parent'],'dss_11kv_415v_owner':single_dict['dss_11kv_415v_owner'],'dss_11kv_415v_name':single_dict['dss_11kv_415v_name'],
                                        'dss_11kv_415v_address':single_dict['dss_11kv_415v_address'],'dss_11kv_415v_rating':single_dict['dss_11kv_415v_rating'],'dss_11kv_415v_upriser_number':single_dict['dss_11kv_415v_upriser_number'],
                                        }])

                    single_dict['query_url'] = Encryption.encryptMessage(url)
                    # print('\n\n\n\n\n\nsingle_dict type after addition',type(single_dict))
                    megalist.append(single_dict)
                    # print("\n\n\n\nMegalist ", megalist)
                    Customers += http.request.env['res.partner'].browse(single_dict['id'])

            return Customers,megalist,total_customers
        else:
            customers_list = Customers.search([])
            return 'with_param' ,customers_list
    
    @http.route('/cms/customers/',website=True,auth='public')
    def customers(self,view,id,user,**kw):
        uid = Encryption.decryptMessage(id)
        login = Encryption.decryptMessage(user)
        if User.isUserExist(uid,login):
            this,customers_list,total_customers = Customers.getCustomers()
            if this == 'with_param':
                return request.render("cms_ibedc.customers",{"customers":customers_list})
            # print("\n\n\n\nReturned ",{"self":this,"customers":customers_list})
            return request.render("cms_ibedc.customers",{"self":this,"customers":customers_list,"component":{'url':'personal_info'},"total_customers":total_customers})
        else:
            return request.render("cms_ibedc.404notfound",{})
        

class CustomerDetails(http.Controller):
    
    def getSingleCustomer(self,queryParam='',limit=0):
        pass
    
    def toLocale(self,value):
        import locale
        if isinstance(value, int) or isinstance(value, float):
            locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
            return (locale.format_string('%.2f', float(value), True))
        else:
            return (locale.format_string('%.2f', 0.00, True))
        
    @http.route('/cms/customer_details/',website=True,auth='public') 
    def customers_details(self,component,queryParam,**kw):
        print(component,queryParam)
        try:
            import ast
            decrypted_customers_list = Encryption.decryptMessage(queryParam)
            print("\n\n\n\ndecrypted_customers_list",decrypted_customers_list)
            queryParam = decrypted_customers_list
            newqueryParam = queryParam.replace("False", '" "')
            newqueryParam = newqueryParam.replace("None", '" "')
            newqueryParam = newqueryParam.replace("null", '" "')
            newqueryParam = newqueryParam.replace("'", '"')
            # print("\n\nJSON ",newqueryParam, json.dumps(newqueryParam))
            return request.render("cms_ibedc.customer_details",{"ref":{'self':self},"component":{'url':component},"customerdata":ast.literal_eval(newqueryParam)[0]},status=301)
        except Exception as e:
            print('err',e)
            response = {"status":False, "message":"This page was not found..."}
            return request.render("cms_ibedc.404notfound",{"response":response})
            
            # return Response(json.dumps(response, default=Serializables.jsonSerializer),content_type='text/json;charset=utf-8',status=404)

# personal_info gAAAAABigXAT38QLs8cAbY07woKqUCl_mkyeIDlrodYgh7UyCQCY2UsKGunAMlby_386lG237ODiFXbSZahouTeZl4OQfXhq3yAJftkaGsCvB4OSZMK4d2yBDAaLeXflLggAwS9LCgxQaw5gs0jj9PDysUhVoZGQ7hGs9nA_luMpcNH0j8kN4CJV7NB8bdl_yAg9fO7B7Sh1Dn3_ZDhreaKhrx1wiSaZrxQ9qizrIF-P6X-LMFVVcxKDHc3ZcFYSLKQu8sit_dqX6crau9exCAVKB34Lm9_CTIAyWBWoTzkUmM7_0sgOZ7WihJIopXdMmi2OkmjED5AxeCRH4dZms6owmyRIG2PXTg1WOrmba1Ongw5AEzc2EaAFTx63E8LHjIeQ_KWjEDbq8lI-NUF7hHMF1eH23U7xuyDAM4am2XqWl-KXx6wSvirOilsgaBo3mk8bVGPJkrD7AMQtFvNYHKZPjXtku2QznWoEO8Ov1GY3unfPBayRJ6ANWUF2Jo0jnfz5eVKtvB6P_cziw0dnAIHFtu8WAkeoBCzkaYWN9hgIVbM122lNIm1mHGYxLwpQD09CZPx9dsfohhKRL2aXUCD6MsGlf7TZ7ZXgHpBEQjCNh1bXJlAuob1UZtA4aSlXJ4k5Y44qZ1hBIoUXy_V-5mJQXtDWEzixjcudomX03cC7w7bxAOGkT9j_8aotvyK921-dxumPcYK0Row1l7vsgtD0n2yLDRercy-zlXNyHIiRxoGR2fCPHoApVXrEfClsUWn5WXVrd0jYWkmkQ5mrK0Heswf4gS4y6coVTxH86EQCLnUzwtX4_k0=
# personal_info gAAAAABigXAT38QLs8cAbY07woKqUCl_mkyeIDlrodYgh7UyCQCY2UsKGunAMlby_386lG237ODiFXbSZahouTeZl4OQfXhq3yAJftkaGsCvB4OSZMK4d2yBDAaLeXflLggAwS9LCgxQaw5gs0jj9PDysUhVoZGQ7hGs9nA_luMpcNH0j8kN4CJV7NB8bdl_yAg9fO7B7Sh1Dn3_ZDhreaKhrx1wiSaZrxQ9qizrIF-P6X-LMFVVcxKDHc3ZcFYSLKQu8sit_dqX6crau9exCAVKB34Lm9_CTIAyWBWoTzkUmM7_0sgOZ7WihJIopXdMmi2OkmjED5AxeCRH4dZms6owmyRIG2PXTg1WOrmba1Ongw5AEzc2EaAFTx63E8LHjIeQ_KWjEDbq8lI-NUF7hHMF1eH23U7xuyDAM4am2XqWl-KXx6wSvirOilsgaBo3mk8bVGPJkrD7AMQtFvNYHKZPjXtku2QznWoEO8Ov1GY3unfPBayRJ6ANWUF2Jo0jnfz5eVKtvB6P_cziw0dnAIHFtu8WAkeoBCzkaYWN9hgIVbM122lNIm1mHGYxLwpQD09CZPx9dsfohhKRL2aXUCD6MsGlf7TZ7ZXgHpBEQjCNh1bXJlAuob1UZtA4aSlXJ4k5Y44qZ1hBIoUXy_V-5mJQXtDWEzixjcudomX03cC7w7bxAOGkT9j_8aotvyK921-dxumPcYK0Row1l7vsgtD0n2yLDRercy-zlXNyHIiRxoGR2fCPHoApVXrEfClsUWn5WXVrd0jYWkmkQ5mrK0Heswf4gS4y6coVTxH86EQCLnUzwtX4_k0