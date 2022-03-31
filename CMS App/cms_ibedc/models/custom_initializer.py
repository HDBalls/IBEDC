from odoo import api, fields, models,tools
import collections, csv,os
from .. import loadconfig
import datetime
from lxml import etree
my_path = os.path.abspath(os.path.dirname(__file__))
my_path = my_path.replace("\\", "/")
my_path = my_path.rsplit('/', 1)[0]
config = list()

try:
        config = loadconfig.configload(["states_csv_path","local"])
except Exception as e:
        print("An error occured while loading config file ",e)
        
path = my_path + config[0]
country = config[1]


class product(models.Model):
        _inherit = "res.country.state"

        @api.model
        def addStates(self):
                
                try: # Check database if states are already added 
                        data = self.readcsv(path)
                        self._cr.execute("""select id from res_country where code='NG';""")
                        countryid = self._cr.fetchall()
                        query = """select * from res_country_state where country_id=%d;"""%(countryid[0][0])
                        print("=====> ",countryid[0][0])
                        self._cr.execute(query)
                        result=self._cr.fetchall()
                        if (len(result) == len(data)):
                                print("States are complete")
                        else:
                                print("Incomplete or no Nigerian state found ",len(result), result)
                                for i in range(0,len(data)):
                                        timestamp = datetime.datetime.now()
                                        # Add the states from the states csv file to the database
                                        self._cr.execute("""INSERT INTO res_country_state (country_id,name, code,create_uid,create_date,write_uid,write_date) VALUES ('%d','%s','%s','%d','%s','%d','%s')"""%(countryid[0][0],data[i][2],data[i][3],1,timestamp,1,timestamp))
                                print("Nigerian states were added")
                except Exception as e:
                        print("===>>> AN ERROR OCCURED WHILE ADDING STATES TO RES.COUNTRY.STATES ",e)
        
        def readcsv(self,args):

                try:
                        print(args)
                        rows = []
                        with open(""+args, 'r') as file:
                                csvreader = csv.reader(file)
                                header = next(csvreader)
                                for row in csvreader:
                                        rows.append(row)
                        
                        print(rows)
                        return rows
                except Exception as e:
                        print("Exception occured while reading file ",e)

class RestrictDropdown(models.Model):
        
        _inherit = 'res.partner'
        
        @api.model
        def _default_country_domain(self): # set domain to restrict the countries in country dropdown to only Nigeria
                domain =[('id', '=', -1)]
                country_list=[]
                country_model = self.env['res.partner'].search([('country_id','=',''+country)])
                
                for each in country_model:
                        country_list.append(each.country_id.id)
                if country_list:
                        domain =[('id', 'in',country_list)]
                        return domain

                return domain

        def _default_country(self):
                        return self.env['res.country'].search([('name', '=', ''+country)], limit=1).id
                        # Apply returned domain to the country dropdown to restrict the countries to only Nigeria
        country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',domain=_default_country_domain,default=_default_country)
        
        
        @api.model
        def fields_view_get(self, view_id=None, view_type='form',
                                                toolbar=False, submenu=False):
                res = super(RestrictDropdown, self).fields_view_get(
                        view_id=view_id, view_type=view_type,
                        toolbar=toolbar, submenu=submenu)
                if view_type != 'search' and self.env.uid != 1:
                        # Check if user is in group that allow creation of contacts
                        has_my_group = self.env.user.has_group('cms_ibedc.developers_group')
                        print("======> ", view_type, self.env.uid,has_my_group,self.env.user)

                        if has_my_group==False: # Hide contacts creation button for users not in developers group
                                
                                root = etree.fromstring(res['arch'])
                                root.set('create', 'false')
                                res['arch'] = etree.tostring(root)
                return res


class RenamePartnerAssignment(models.Model):
        
        _inherit = 'res.partner'
 
        @api.model
        def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
                result = super(RenamePartnerAssignment, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
                # if view_type == 'form':
                #         doc = etree.XML(result['arch'])
                #         PartnerAssignment = doc.xpath("//page[@string='Sales & Purchase']") #geo_location Test tab name replacement (development only)
                #         # PartnerAssignment = doc.xpath("//page[@string='Partner Assignment']") #geo_location Partner Assignment (Live only)
                #         print("Swapping ", PartnerAssignment[0].text)
                #         if PartnerAssignment:
                #                 PartnerAssignment[0].set("string", "Geolocation")
                #                 result['arch'] = etree.tostring(doc, encoding='unicode')
                                

                if view_type == 'tree':
                        doc = etree.XML(result['arch'])
                        Customerheader = doc.xpath("//tree[@string='Contacts']") 
                        
                        if Customerheader:
                                print("Swapping contacts header ", Customerheader[0].text)
                                Customerheader[0].set("string", "Customers")
                                result['arch'] = etree.tostring(doc, encoding='unicode')
                return result



class NonAdminHideSettings(models.Model):
        has_my_group = None
        hide_flag = True
        choices = [("false",False),("access_rights","Access Rights")]
        _inherit = 'res.users'
        
        @api.model
        def _hider(self):
            print("The choices ",NonAdminHideSettings.choices)
            return NonAdminHideSettings.choices

        @api.model
        def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
                result = super(NonAdminHideSettings, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
                NonAdminHideSettings.choices = [("false",False),("access_rights","Access Rights")]
                NonAdminHideSettings.has_my_group = self.env.user.has_group('cms_ibedc.developers_group')
                
                if NonAdminHideSettings.has_my_group==True:
                        
                        doc = etree.XML(result['arch'])
                        hide = doc.xpath("//tree[@string='Contacts']") 
                        NonAdminHideSettings.choices+=[("settings","Settings")]
                        print("=====================> Hider function ",hide)
                        if view_type == 'form':
                                NonAdminHideSettings.hideflag = False
                        result['arch'] = etree.tostring(doc, encoding='unicode')
                        
                return result
        
        sel_groups_2_3 = fields.Selection(string="Administrations", selection=_hider,default="access_rights")
        
        def serve(integer):
                print("\n\nBoolean ",NonAdminHideSettings.hide_flag,integer)
                return NonAdminHideSettings.hide_flag
        
        

        
