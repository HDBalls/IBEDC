# lst = []
# transient_fields = [
#                         'Name','mobile','email','city','address1','account_no','account_type',
#                         'outstanding_amnt','address2','meter_model','meter_type','meter_number',
#                         'meter_manufacturer','manufacture_year','meter_rating',
#                         'applicationdate','giscoordinate','guarantorname','guarantoraddress',
#                         'v_rating','meter_classification','meter_category','state',
#                         'meter_type_id','meter_type_id','statuscode',
#                         ]  

# for field in transient_fields:
#     lst.append(field.title())

# print(lst)


ListKeys = ['Name', 'Mobile', 'Email', 'Address 1', 'City', 'Account No', 'Account Type', 
                        'Outstanding Amount', 'Address 2', 'Meter Model', 'Meter Type', 'Meter Number', 
                        'Meter Manufacturer', 'Manufacture Year', 'Meter Rating', 'Application Date', 
                        'Giscoordinate', 'Guarantor Name', 'Guarantor Address', 'V Rating', 'Meter Class', 
                        'Meter Category', 'State', 'Meter Type_Id', 'Status Code'
                        ] 

ListValues = ['name', 'mobile', 'email', 'address1', 'city', 'account_no', 'account_type', 
                        'bal_cash', 'address2', 'meter_model', 'meter_type', 'meter_number', 
                        'meter_manufacturer', 'manufacture_year', 'meter_rating', 'applicationdate', 
                        'giscoordinate', 'guarantorname', 'guarantoraddress', 'v_rating', 'meter_classification', 
                        'meter_category', 'state', 'meter_type_Id', 'status_code'
                        ] 
 
#Convert two Lists into Dictionary using zip()
mergeLists = dict(zip(ListKeys, ListValues))
 
#Print new Dictionary
print("Dictionary after conversion is: "+str(mergeLists))



# transient_fields = ['Name', 'Mobile', 'Email', 'Address 1', 'City', 'Account No', 'Account Type', 
#                         'Outstanding Amount', 'Address 2', 'Meter Model', 'Meter Type', 'Meter Number', 
#                         'Meter Manufacturer', 'Manufacture Year', 'Meter Rating', 'Application Date', 
#                         'Giscoordinate', 'Guarantor Name', 'Guarantor Address', 'V Rating', 'Meter Class', 
#                         'Meter Category', 'State', 'Meter Type_Id', 'Status Code'
#                         ] 

#     defaults =          ['Name', 'Mobile', 'Email', 'Address 1', 'Account No', 'Account Type', 
#                         'Outstanding Amount', 'Meter Number', 'State','Status Code'
#                         ] 
    
#     field_names =       ['name', 'mobile', 'email', 'address1', 'city', 'account_no', 'account_type', 
#                         'bal_cash', 'address2', 'meter_model', 'meter_type', 'meter_number', 
#                         'meter_manufacturer', 'manufacture_year', 'meter_rating', 'applicationdate', 
#                         'giscoordinate', 'guarantorname', 'guarantoraddress', 'v_rating', 'meter_classification', 
#                         'meter_category', 'state', 'meter_type_Id', 'status_code'
#                         ] 