import json
from odoo import http
from odoo.http import request, Response
from ..utilitymethods.utility import Encryption, Serializables, User

class objectview(object):
    def __init__(self, d):
        self.__dict__ = d


class PaymentHistory(http.Controller):
        
    def getPaymentsHistory(self,queryParam=None,limit=0):
        db_name = http.request.session._db
        print("Account Number ",queryParam)
        if queryParam == None:
            Paymenthistory = http.request.env['payment.history']
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
                    megalist.append(single_dict)
                    Paymenthistory += http.request.env['payment.history'].browse(single_dict['id'])
            return Paymenthistory,megalist,len(payment_list)
        
        else:

            print("Account Number ",queryParam)
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
                if queryParam == '':
                    return {'status':False,'message': f'This customer does not have an Account Number'}
                else:
                    return {'status':False,'message': f'No record found for {queryParam}'}
                
    @http.route('/cms/payment_history/page/<int:page>',website=True,auth='public')
    def paymentHistory(self,view,id,user,page,limit='',**kw):
        try:
            uid = Encryption.decryptMessage(id)
            login = Encryption.decryptMessage(user)
            if User.isUserExist(uid,login):
                this,payment_list,total_payments = self.getPaymentsHistory()
                pager = request.website.pager( 
                                        url=f'/cms/payment_history',
                                        total=total_payments,
                                        page=page,
                                        step=10,
                                        url_args= {'view':view, 'id':id, 'user':user}
                                        )
                offset = (page - 1) * 10
                payment_list = payment_list[offset: offset + 10]
                return request.render("cms_ibedc.payment_history",{'this':this,'paymentshistory':payment_list,"total_payments":total_payments,"pager":pager})
            else:
                return request.render("cms_ibedc.404notfound",{})   
        except Exception as e:
            print("An error occured ",e)
        

    @http.route('/cms/lazypayment_history/', csrf=False, auth="public")
    def lazyPaymentHistory(self,account_no,**kw):
        try:
            response = self.getPaymentsHistory(account_no)
            return Response(json.dumps(response),content_type='text/json;charset=utf-8')
        except Exception as e:
            print("An error occured ",e)
    
