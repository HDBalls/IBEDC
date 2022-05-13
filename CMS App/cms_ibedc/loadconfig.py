import json,os
my_path = os.path.abspath(os.path.dirname(__file__))
my_path = my_path.replace("\\", "/")

try:
    def configload(args):
        with open(my_path+'/config.json') as json_file:
            data = json.load(json_file)
            json_file.close()
            results = list()
            for parameter in args:
                results.append(data[''+parameter])
            return results
        
except Exception as e:
    print("\n===> Error occured while loading config.json ",e)
    



#Payment history for all for users that have ever made payment
# SELECT
#     payment_history.payment_root_id,
#     payment_history.account_no,
#     payment_history.payment_id,
#     emspayment_trans.trans_status
	
# FROM
#     payment_history
# LEFT OUTER JOIN emspayment_trans ON payment_history.transaction_id = emspayment_trans.transaction_id;
 
 
 
 
 
# All payment history that have corresponding payment trans?
# SELECT * FROM payment_history, emspayment_trans 
#     where payment_history.transaction_id = emspayment_trans.transaction_id 
#     and payment_history.account_no = emspayment_trans.account_no;





#single user payment history

# SELECT * FROM payment_history, emspayment_trans 
# where payment_history.transaction_id = emspayment_trans.transaction_id 
# and payment_history.account_no = '11/12/64/0036-01';