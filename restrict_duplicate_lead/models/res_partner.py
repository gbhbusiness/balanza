# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    @api.model
    def fields_view_get(self, view_id=None, view_type='form',
                        toolbar=False, submenu=False):
        res = super(ResPartner, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form' and self._context.get('remove_lead'):
            self.env['crm.lead'].browse(self._context.get('remove_lead')).unlink()
        return res
