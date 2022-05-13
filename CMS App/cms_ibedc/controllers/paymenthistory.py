import json
from odoo import http
from odoo.http import request, Response

class objectview(object):
    def __init__(self, d):
        self.__dict__ = d


class PaymentHistory(http.Controller):
    
    

    def jsonSerializer(self,obj):
        from datetime import date, datetime
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        pass
        
    def getPaymentsHistory(self,queryParam='',limit=0):
        db_name = http.request.session._db
        if queryParam == '':
            Paymenthistory = http.request.env['payment.history']
            payment_list_search = Paymenthistory.search([])
            query = f"""SELECT 
                            payment_history.id,
                            payment_history.payment_root_id,
                            payment_history.transaction_id,
                            payment_history.transaction_refr,
                            payment_history.payment_id,
                            payment_history.account_no,
                            payment_history.timestamp,
                            payment_history.initiation_date,
                            payment_history.confirmation_date,
                            payment_history.tx_message,
                            payment_history.gross_amount,
                            payment_history.net_amount,
                            payment_history.units_consumed,
                            emspayment_trans.trans_status
                        FROM
                            payment_history
                        LEFT OUTER JOIN emspayment_trans ON payment_history.transaction_id = emspayment_trans.transaction_id
                        order by payment_history.id desc;
 

                        ;
                    """
            http.request.cr.execute(query)
            payment_list = request.cr.dictfetchall()
            megalist = []
            if payment_list:
                for single_dict in payment_list:
                    
                    single_dict['trans_status'] = str(single_dict['trans_status'])
                    if single_dict['trans_status'] == 'None':
                        single_dict['trans_status'] = ''
                    print("\n\n\n\nsingle_dict ",single_dict)
                    megalist.append(single_dict)
                    Paymenthistory += http.request.env['payment.history'].browse(single_dict['id'])
            print("pay ",payment_list_search,Paymenthistory[0].trans_status,(payment_list_search==Paymenthistory))
            return Paymenthistory,megalist
        
        else:
            filter_domain=[('account_no', '=', queryParam)]
            Payment_history = http.request.env['payment.history']
            # billing_list = Payment_history.sudo().search(filter_domain)
            query = f""" 
                        SELECT * FROM payment_history, emspayment_trans 
                        WHERE payment_history.transaction_id = emspayment_trans.transaction_id 
                        AND payment_history.account_no = '{queryParam}';
                    """
            http.request.cr.execute(query)
            payment_list = request.cr.dictfetchall() 
            
            if payment_list:
                return {'status':True,'data':payment_list ,'message': f'Payment history for {queryParam} fetched succesfully'}
            else:
                return {'status':False,'message': f'No record found for {queryParam}'}
    
    @http.route('/cms/payment_history/',website=True,auth='public')
    def paymentHistory(self,queryParam='',limit='',**kw):
        this,payment_list = self.getPaymentsHistory()
        
        return request.render("cms_ibedc.payment_history",{'this':this,'paymentshistory':payment_list})

    @http.route('/cms/lazypayment_history/', csrf=False, auth="public")
    def lazyPaymentHistory(self,account_no,**kw):
        response = self.getPaymentsHistory(account_no)
        print('\n\n\n\nDumper ',json.dumps(response, default=self.jsonSerializer))
        return Response(json.dumps(response, default=self.jsonSerializer),content_type='text/json;charset=utf-8')
    
# WHERE payment_history.payment_root_id=(select id from res_partner where account_no='{queryParam}')
# class CustomerDetails(http.Controller):
    
#     @http.route('/cms/customer_details',website=True,auth='public') 
#     def customers_details(self,**kw):
#         return request.render("cms_ibedc.customer_details",{})
    