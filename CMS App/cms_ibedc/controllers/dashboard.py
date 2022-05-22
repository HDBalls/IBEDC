
from odoo import http
from odoo.http import request
from ..utilitymethods.utility import Encryption, User

class Dashboard(http.Controller):
    
    @http.route('/cms/dashboard/',website=True,auth='public')
    def dashboard(self,view,id,user,**kw):
        uid = Encryption.decryptMessage(id)
        login = Encryption.decryptMessage(user)
        if User.isUserExist(uid,login):
            return request.render("cms_ibedc.dashboard",{})
        
        return request.render("cms_ibedc.404notfound",{})
