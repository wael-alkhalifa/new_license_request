import time
from datetime import datetime
import collections
from odoo import api, fields, models



class SampleReportPrint(models.Model):
    _name = 'report.decisions.print_sample_report'


    @api.model
    def _get_report_values(self,docids,data):
        datas = {}
        datas = data['form']
        cr = self.env.cr 
        if data['form']['report_type'] == '1':
            vars =  data['form']['date_from'], data['form']['date_to']
            query = ("""SELECT request_type,p.name AS project,decisions.name AS name,order_number,order_date,s.name AS section FROM decisions_decisions as decisions 
            LEFT JOIN res_partner AS p
            ON  p.id = decisions.project_id

            LEFT JOIN nia_section AS s
            ON  s.id = decisions.section
            WHERE  decisions.order_date >= %s AND decisions.order_date <= %s """)
        if data['form']['report_type'] == '2':
            vars =  data['form']['date_from'], data['form']['date_to'],data['form']['request_type']
            query = ("""SELECT p.name AS project,decisions.name AS name,order_number,order_date, s.name AS section FROM decisions_decisions as decisions 
            LEFT JOIN res_partner AS p
            ON  p.id = decisions.project_id

            LEFT JOIN nia_section AS s
            ON  s.id = decisions.section
            WHERE  decisions.order_date >= %s AND decisions.order_date <= %s AND decisions.request_type = %s""")       
        
        if data['form']['report_type'] == '3':
            vars =  data['form']['date_from'], data['form']['date_to'],data['form']['project'][0]           
            query = ("""SELECT request_type,decisions.name AS name,order_number,order_date,s.name AS section FROM decisions_decisions as decisions 
            LEFT JOIN res_partner AS p
            ON  p.id = decisions.project_id

            LEFT JOIN nia_section AS s
            ON  s.id = decisions.section
            
            WHERE  decisions.order_date >= %s AND decisions.order_date <= %s AND decisions.project_id = %s""")       

        if data['form']['report_type'] == '4':
            vars =  data['form']['date_from'], data['form']['date_to'],data['form']['section'][0] 
            query = ("""SELECT request_type,p.name AS project,decisions.name AS name ,order_number,order_date FROM decisions_decisions as decisions
            LEFT JOIN res_partner AS p
            ON  p.id = decisions.project_id

            LEFT JOIN nia_section AS s
            ON  s.id = decisions.section
             WHERE  decisions.order_date >= %s AND decisions.order_date <= %s AND decisions.section = %s""")    
        
        if data['form']['report_type'] == '5':
            vars =  data['form']['date_from'], data['form']['date_to'],data['form']['name'] 
            query = ("""SELECT request_type,p.name AS project,order_number,order_date,s.name AS section FROM decisions_decisions as decisions 
            LEFT JOIN res_partner AS p
            ON  p.id = decisions.project_id

            LEFT JOIN nia_section AS s
            ON  s.id = decisions.section
            WHERE  decisions.order_date >= %s AND decisions.order_date <= %s AND decisions.name LIKE %s""")    
         
        cr.execute(query,vars)
        record = cr.dictfetchall()
        
        #report_type = data['form'][report_type]
        
        #print ('************************************report_type',data['form'][3])
        return {'docs': record,
                'form_data': datas,
                
                       
            }




# class SampleReportPrint(models.Model):
#     _name = 'report.decisions.print_sample_report'


#     @api.model
#     def _get_report_values(self,docids,data):
#         print ('************************************data',data)
#         print ('************************************dataform',data['form'])
#         cr = self.env.cr 
#         query = ("""SELECT request_type,project,name,order_number,order_date,section FROM decisions_decisions as decisions""")
#         cr.execute(query)
#         record = cr.dictfetchall()
#         print ('************************************datenow',wizard['date_now'])
#         return {'docs': record,
#                 'wizard': data['form']           
#             }


# class SampleReportPrint(models.Model):
#     _name = 'report.decisions.print_sample_report'


#     @api.model
#     def _get_report_values(self,docids,data):
#         print ('************************************data',data)
#         print ('************************************dataform',data['form'])
#         cr = self.env.cr 
#         query = ("""SELECT request_type,project,name,order_number,order_date,section FROM decisions_decisions as decisions""")
#         cr.execute(query)
#         record = cr.dictfetchall()
#         print ('************************************datenow',wizard['date_now'])
#         return {'docs': record,
#                 'wizard': data['form']           
#             }



# class SampleReportPrint(models.Model):
#     _name = 'report.decisions.print_sample_report'


#     @api.model
#     def _get_report_values(self,docids,data):
#         print ('************************************data',data)
#         print ('************************************dataform',data['form'])
#         cr = self.env.cr 
#         query = ("""SELECT request_type,project,name,order_number,order_date,section FROM decisions_decisions as decisions""")
#         cr.execute(query)
#         record = cr.dictfetchall()
#         print ('************************************datenow',wizard['date_now'])
#         return {'docs': record,
#                 'wizard': data['form']           
#             }



# class SampleReportPrint(models.Model):
#     _name = 'report.decisions.print_sample_report'


#     @api.model
#     def _get_report_values(self,docids,data):
#         print ('************************************data',data)
#         print ('************************************dataform',data['form'])
#         cr = self.env.cr 
#         query = ("""SELECT request_type,project,name,order_number,order_date,section FROM decisions_decisions as decisions""")
#         cr.execute(query)
#         record = cr.dictfetchall()
#         print ('************************************datenow',wizard['date_now'])
#         return {'docs': record,
#                 'wizard': data['form']           
#             }
