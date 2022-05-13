import json
from odoo import http
from odoo.http import request
from ..models.customer_profile import BaseDeclarative

class Customers(http.Controller):
    
    @staticmethod
    def getCustomers(queryParam='',limit=0):
        Customers = http.request.env['res.partner']
        customers_list = Customers.search([])
        return customers_list
    
    @http.route('/cms/customers/',website=True,auth='public')
    def customers(self,**kw):
        customers_list = Customers.getCustomers()
        return request.render("cms_ibedc.customers",{"customers":customers_list})
    

class CustomerDetails(http.Controller):
    
    def getSingleCustomer(self,queryParam='',limit=0):
        pass
    
    def toLocale(self,value):
        import locale
        if value:
            locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
            return (locale.format_string('%.2f', float(value), True))
        else:
            return (locale.format_string('%.2f', 0.00, True))
        
    @http.route('/cms/customer_details/',website=True,auth='public') 
    def customers_details(self,queryParam,**kw):
        import ast
        newqueryParam = queryParam.replace("False", '" "')
        newqueryParam = newqueryParam.replace("None", '" "')
        # newqueryParam = newqueryParam.replace("0.0", '"0.0"')
        newqueryParam = newqueryParam.replace("'", '"')
        print("\n\nJSON ",newqueryParam, json.dumps(newqueryParam))
        return request.render("cms_ibedc.customer_details",{"ref":{'self':self},"customerdata":ast.literal_eval(newqueryParam)[0]})
    