
from odoo import http
from odoo.http import request

class Customer(http.Controller):

    @http.route('/homepage/',website=True,auth='public')
    def Homepage(self,**kw):
        #return "Hello , Customers"
        return request.render("bus_management.homepage",{})
    