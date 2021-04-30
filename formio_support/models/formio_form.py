from odoo import api, fields, models, _
from odoo.addons.formio.models.formio_builder import STATE_CURRENT as BUILDER_STATE_CURRENT
from odoo.addons.formio.utils import get_field_selection_label


class Form(models.Model):
    _inherit = 'formio.form'

    ticket_id = fields.Many2one('helpdesk.support', readonly=True, string='Support Ticket')

    def _prepare_create_vals(self, vals):
        vals = super(Form, self)._prepare_create_vals(vals)
        builder = self._get_builder_from_id(vals.get('builder_id'))
        res_id = self._context.get('active_id')

        if not builder or not builder.res_model_id.model == 'helpdesk.support' or not res_id:
            return vals

        ticket = self.env['helpdesk.support'].browse(res_id)
        action = self.env.ref('website_helpdesk_support_ticket.helpdesk_view_kanban')
        url = '/web?#id={id}&view_type=form&model={model}&action={action}'.format(
            id=res_id,
            model='helpdesk.support',
            action=action.id)

        vals['ticket_id'] = res_id
        vals['res_partner_id'] = project.partner_id.id
        vals['res_act_window_url'] = url
        vals['res_name'] = ticket.name
        return vals

    @api.onchange('builder_id')
    def _onchange_builder_domain(self):
        res = super(Form, self)._onchange_builder_domain()
        if self._context.get('active_model') == 'helpdesk.support':
            res_model_id = self.env.ref('website_helpdesk_support_ticket.model_helpdesk_support').id
            domain = [
                ('state', '=', BUILDER_STATE_CURRENT),
                ('res_model_id', '=', res_model_id),
            ]
            res['domain'] = {'builder_id': domain}
        return res
