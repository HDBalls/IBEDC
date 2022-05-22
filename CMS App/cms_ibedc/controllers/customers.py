from email.policy import default
import json
from odoo import http
from odoo.http import request, Response
from ..utilitymethods.utility import Encryption, Serializables
from ..models.customer_profile import BaseDeclarative
from ..utilitymethods.utility  import QuerySelectors, TransientFields 
from ..utilitymethods.utility import Encryption, User

class CustomersView(http.Controller):
    
    @staticmethod
    def getCustomers(queryParam='',limit=0):
        Customers = http.request.env['res.partner']
        customers_onchange = Customers.sudo().onchange_name()
        print("Onchange name controller", customers_onchange,queryParam)
        if queryParam == '' or queryParam == None:
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
            return CustomersView.makeUrl(Customers,customers_list)
        
        else:
            customers_list = Customers.search([])
            return 'with_param' ,customers_list
    
    @staticmethod
    def deepSearchCustomers(Customers,searchparam=None,browse=''):
        query = f"""         
                    SELECT 
                            {QuerySelectors.queryselectors_cust} 
                    FROM

                        res_partner

                    LEFT OUTER JOIN res_country_state on res_partner.state_id = res_country_state.id
                    LEFT OUTER JOIN meter_model ON res_partner.meter_number = meter_model.meter_number
                    LEFT OUTER JOIN gis_distribution_substation_all on res_partner.dss_id = gis_distribution_substation_all.assetid
                    WHERE UPPER(res_partner.name) LIKE UPPER('%{searchparam}%') OR
                    UPPER(res_partner.email) LIKE UPPER('%{searchparam}%') OR
                    UPPER(res_partner.account_no) LIKE UPPER('%{searchparam}%') OR
                    UPPER(res_partner.mobile) LIKE UPPER('%{searchparam}%')
                    ORDER BY res_partner.name;
                    
                    ;"""
                    
        http.request.cr.execute(query)
        customers_list = request.cr.dictfetchall()
        return CustomersView.makeUrl(Customers,customers_list,browse)
    
    @staticmethod 
    def makeUrl(Customers,customers_list,browse=True):
        total_customers = http.request.env['res.partner'].search_count([])  
        megalist = []
        if customers_list:
            for single_dict in customers_list:

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
                megalist.append(single_dict)
                if browse == True:
                    Customers += http.request.env['res.partner'].browse(single_dict['id'])
                else:
                    pass
        
        if browse == True:
            return Customers,megalist,len(customers_list)
        else:
            return megalist,len(customers_list)
    
    @http.route('/cms/customers/search/page/<int:page>', website=True,auth='public')
    def deepsearchcustomers(self,view,id,user,page,searchparam,**kw):
        
        try:
            # print("\n\n\n\ndeep searcjig customers")
            Customers = http.request.env['res.partner']
            this,customers_list,total_searchresults = CustomersView.deepSearchCustomers(Customers ,searchparam,True)
            print("\n\n\nTotal search no ",total_searchresults)
            # pager = request.website.pager( 
            #                             url=f'/cms/customers/search',
            #                             total=total_searchresults,
            #                             page=0,
            #                             step=10
            #                             )
            # # print("after pager")
            # offset = pager['offset']
            # customers_list = customers_list[offset: offset + 50]
            
            # response = {"status":True,"data":customers_list,"pager":pager,"total_searchresults":total_searchresults}
            # # print('\n\n\n\nSearch customers ',json.dumps(response, default=Serializables.jsonSerializer))
            # # return Response(json.dumps(response),content_type='text/json;charset=utf-8',status=200)
            # return request.render("cms_ibedc.deep_search_customers",{})
            pager = request.website.pager( 
                                        url=f'/cms/customers/search',
                                        total=total_searchresults,
                                        page=page,
                                        step=50,
                                        url_args= {'view':view, 'id':id, 'user':user,'searchparam':searchparam}
                                        )
            offset = (page - 1) * 50
            customers_list = customers_list[offset: offset + 50]
            return request.render("cms_ibedc.deep_search_customers",{"self":this,"customers":customers_list,"component":{'url':'personal_info'},"total_customers":total_searchresults,'pager': pager})

        except Exception as e:
            print("catching error ", e)
            return request.render("cms_ibedc.404notfound",{})
        
    @http.route('/cms/customers/page/<int:page>', website=True,auth='public')
    def customers(self,view,id,user,page,**kw):
        
        uid = Encryption.decryptMessage(id)
        login = Encryption.decryptMessage(user)
        if User.isUserExist(uid,login):
            this,customers_list,total_customers = CustomersView.getCustomers()
            if isinstance(this,str):
                if this == 'with_param':
                    return request.render("cms_ibedc.customers",{"customers":customers_list})
        
            pager = request.website.pager( 
                                        url=f'/cms/customers',
                                        total=total_customers,
                                        page=page,
                                        step=10,
                                        url_args= {'view':view, 'id':id, 'user':user}
                                        )
            offset = pager['offset']
            customers_list = customers_list[offset: offset + 50]
            transients = TransientFields.transient_fields
            defaults = TransientFields.defaults
            field_names = TransientFields.field_names
            defaults = TransientFields.loadUserTransientFields('customerstransientviews') or defaults
            return request.render("cms_ibedc.customers",{"self":this,"customers":customers_list,"component":{'url':'personal_info'},
                                                         "total_customers":total_customers,'pager': pager,'transients':transients,
                                                         "defaults":defaults,"field_names":field_names})
        else:
            
            return request.render("cms_ibedc.404notfound",{})
        

class CustomerDetails(http.Controller):
    
    def processData(data):
        specialChars = ["!","#","$","%","^","&","*","(",")","False","None","None","null","'"]
        for specialChar in specialChars:
            data = data.replace(specialChar, " ")
            if specialChar == "'":
                data = data.replace(specialChar, '"')
        return data
    
    def toLocale(self,value):
        import locale
        if isinstance(value, int) or isinstance(value, float):
            locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
            return (locale.format_string('%.2f', float(value), True))
        else:
            return (locale.format_string('%.2f', 0.00, True))
        
    @http.route('/cms/customer_details/',website=True,auth='public') 
    def customers_details(self,component,queryParam,**kw):
        try:
            import ast
            decrypted_customers_list = Encryption.decryptMessage(queryParam)
            queryParam = decrypted_customers_list
            # newqueryParam = CustomerDetails.processData(queryParam)
            newqueryParam = queryParam.replace("False", '" "')
            newqueryParam = newqueryParam.replace("None", '" "')
            newqueryParam = newqueryParam.replace("null", '" "')
            newqueryParam = newqueryParam.replace("'", '"')
            http.request.cr.execute(f"""select * from respartner_event where account_no = '{json.loads(newqueryParam)[0]['account_no']}';""")
            print("\n\n\n\ndecrypted_customers_list",type(newqueryParam),json.loads(newqueryParam)[0])
            data = http.request.cr.dictfetchone()
            if data is not None:
                newqueryParam_e = json.loads(newqueryParam)[0]
                print("data ",data)
                edited_fields = data['fields_changed']
                edited_fields = json.loads(edited_fields)
                print("\n\nGot new edited fields ", edited_fields)
                keys = edited_fields.keys()
                for key in keys:
                    newqueryParam_e[key] = edited_fields[key]
                print("New data ", type(newqueryParam_e))
                http.request.cr.execute(f"""delete from respartner_event where account_no = '{json.loads(newqueryParam)[0]['account_no']}';""")
                return request.render("cms_ibedc.customer_details",{"ref":{'self':self},"component":{'url':component},"customerdata":newqueryParam_e},status=301)
                
            
            else:
                return request.render("cms_ibedc.customer_details",{"ref":{'self':self},"component":{'url':component},"customerdata":ast.literal_eval(newqueryParam)[0]},status=301)
        
        except Exception as e:
            print('err',e)
            response = {"status":False, "message":"This page was not found..."}
            return request.render("cms_ibedc.404notfound",{"response":response})
            
            # return Response(json.dumps(response, default=Serializables.jsonSerializer),content_type='text/json;charset=utf-8',status=404)