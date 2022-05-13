import json
from odoo import http
from odoo.http import request, Response

class BillingHistory(http.Controller):
    
    def __init__(self):
        
        self.cache = None
        
    def getBillingHistory(self,queryParam='',limit=0):
        db_name = http.request.session._db
        if queryParam == '':
            BillingHistory = http.request.env['billing.history']
            billing_list = BillingHistory.search([])
            return billing_list
        else:
            filter_domain=[('account_no', '=', queryParam)]
            BillingHistory = http.request.env['billing.history']
            # billing_list = BillingHistory.sudo().search(filter_domain)
            query = f""" 
                        SELECT
                            bill_id,
                            tarrif_name,
                            period,
                            total_usage,
                            total_amount,
                            billing_purpose
                        FROM
                            billing_history
                        INNER JOIN res_partner 
                            ON res_partner.id = billing_history.bill_root_id

                        WHERE billing_history.bill_root_id=(select id from res_partner where account_no='{queryParam}')
                        ;
                    """
            http.request.cr.execute(query)
            billing_list = request.cr.fetchall() 
            
            if billing_list:
                return {'status':True,'data':billing_list ,'message': f'Billing history for {queryParam} fetched succesfully'}
            else:
                return {'status':False,'message': f'No record found for {queryParam}'}
    
    @http.route('/cms/billing_history/',website=True,auth='public')
    def billingHistory(self,**kw):
        billing_list = self.getBillingHistory()
        return request.render("cms_ibedc.billing_history",{"billinghistory":billing_list})
    
    @http.route('/cms/lazybilling_history/', csrf=False, auth="public")
    def lazyBillingHistory(self,account_no,**kw):
        response = self.getBillingHistory(account_no)
        return Response(json.dumps(response),content_type='text/json;charset=utf-8',status=200)