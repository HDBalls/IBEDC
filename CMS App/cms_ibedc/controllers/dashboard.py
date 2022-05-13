
from odoo import http
from odoo.http import request

class Dashboard(http.Controller):
    
    @http.route('/cms/dashboard/',website=True,auth='public')
    def dashboard(self,**kw):
        return request.render("cms_ibedc.dashboard",{})
