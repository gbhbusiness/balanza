
from odoo import models, fields, api


class CrmLeadWizard(models.TransientModel):

    _name = 'crm.lead.wizard'
    _description = 'Crm Lead Wizard'

    partner_id = fields.Many2one('res.partner', 'Already Customer Exists')
    lead_id = fields.Many2one('crm.lead', 'Already Lead Exists')
    note = fields.Char()
    lead_type = fields.Selection([('lead', 'Lead'),
                                  ('oppo', 'Opportunity')], string="Lead Type")
    active_lead_id = fields.Many2one('crm.lead', 'Active Lead')

    @api.model
    def default_get(self, fields):
        res = super(CrmLeadWizard, self).default_get(fields)
        lead = self.env['crm.lead'].browse(res.get('lead_id'))
        res['active_lead_id'] = self._context.get('active_id')
        if lead.type == 'lead':
            res['lead_type'] = 'lead'
        elif lead.type == 'opportunity':
            res['lead_type'] = 'oppo'
        else:
            res['lead_type'] = False
        return res

    def delete_data(self):
        self.ensure_one()
        self.name = "CRM Wizard"
        lead = self.env['crm.lead'].browse(self._context.get('active_id'))
        lead.unlink()
        action = self.env.ref('crm.crm_lead_all_leads').read()[0]
        return action
