from datetime import datetime
from odoo import api, fields, models, exceptions ,_
from odoo.exceptions import UserError

class decisions_wizard(models.TransientModel):
    
    _name = "decisions.wizard"
    _description = "decisions wizard"


    date_from = fields.Date(default=fields.Date.today)
    date_to = fields.Date(default=fields.Date.today)
    report_type = fields.Selection(string='report_type', selection=[('1', 'All'), ('2', 'by request type'),('3', 'by project'),('4', 'by section'),('5', 'by name'), ])
    request_type = fields.Selection([('1', 'rental form'),('2', 'needs statement'),('3', 'license renewal'),('4', ' typical privileges'),('5', 'shapeliness request'),('6', 'transportation recommendation'),('7', 'model exception'),('8', ' resumption request'),('9', 'modify decision'),('10', 'renewal decision'),('11', 'change activity'), ('12', 'conduct request'),('13', 'mortgage_request'),('14', ' enter partner'),('15', 'breakup partnership'),('16', 'change businessname'),('17', 'transfer_ownership'),('18', ' reissued request'),('19', 'cancel license')],string='request type')
    project = fields.Many2one('res.partner', 'project')
    name = fields.Char(string='Order by')
    section = fields.Many2one('nia.section', 'section')
    date_now = fields.Datetime(string='date_now', default=datetime.now(),)


    @api.onchange("date_to")
    def _onchange_field(self):
        vals = {}
    
        # Remove warning if necessary
        if self.date_to < self.date_from :
            vals['warning'] = {
                'title': _('date warning'),
                'message': _('invalid Date')
            }
    
            return vals
    

    def print_report(self,data):



        data['form'].update(self.read(['date_from','date_to','report_type','request_type','project','name','date_now','section'])[0])


        
        return self.env.ref('decisions.print_report_pdf').report_action(self, data=data)


    def check_report(self):
        data = {}
        data['form'] = self.read(['date_from','date_to','report_type','request_type','project','name','date_now','section'])[0]
        return self.print_report(data)
        # if self.report_type == '2':
        #     return self.env.ref('decisions.print_report_pdf').report_action(self, data=data)

        # if self.report_type == '3':
        #     return self.env.ref('decisions.print_report_pdf').report_action(self, data=data)

        # if self.report_type == '4':
        #     return self.env.ref('decisions.print_report_pdf').report_action(self, data=data)


        # if self.report_type == '5':
        #     return self.env.ref('decisions.print_report_pdf').report_action(self, data=data)




# class deleveryWizard(models.TransientModel):
# 	_name = "delevery.wizard"
# 	_description = "delevery wizard"
	

# 	# current_date = fields.Date(string='التاريخ' , required=True)
# 	dateFrom = fields.Date(required=True)
# 	dateTo  =  fields.Date( required=False)
# 	company_id = fields.Many2one('res.company', required=False)

# 	def _print_report(self, data):
# 		data['form'].update(self.read(['dateFrom','dateTo','company_id'])[0])
# 		return self.env.ref('ok.action_report_delevery').report_action(self, data=data)

# 	def check_report(self):
# 		data = {}
# 		data['form'] = self.read(['dateFrom','dateTo','company_id'])[0]
# 		return self._print_report(data)