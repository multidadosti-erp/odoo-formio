# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Multidados: Troca de 'partner_id' por 'res_partner_id'
    formio_forms = fields.One2many('formio.form', 'res_partner_id', string='Forms')
    formio_forms_count = fields.Integer(compute='_compute_formio_forms_count')
    formio_this_model_id = fields.Many2one('ir.model', compute='_compute_formio_this_model_id')

    def _compute_formio_forms_count(self):
        for r in self:
            r.formio_forms_count = len(r.formio_forms)

    def _compute_formio_this_model_id(self):
        # Multidados
        # self.ensure_one()
        model_id = self.env.ref('base.model_res_partner').id
        for record in self:
            if record.formio_forms:
                record.formio_this_model_id = model_id

    @api.multi
    def write(self, vals):
        # Simpler to maintain and less risk with extending, than
        # computed field(s) in the formio.form object.
        res = super(ResPartner, self).write(vals)
        for record in self:
            if record.formio_forms:
                form_vals = record._prepare_write_formio_form_vals(vals)
                if form_vals:
                    record.formio_forms.write(form_vals)
        return res

    def _prepare_write_formio_form_vals(self, vals):
        if vals.get('name'):
            form_vals = {
                'res_name': self.name
            }
            return form_vals
        else:
            return False

    @api.multi
    def action_formio_forms(self):
        self.ensure_one()
        res_model_id = self.env.ref('base.model_res_partner').id
        return {
            'name': 'Forms.io',
            'type': 'ir.actions.act_window',
            'domain': [('res_id', '=', self.id), ('res_model_id', '=', res_model_id)],
            'context': {'default_res_id': self.id},
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'res_model': 'formio.form',
            'view_id': False,
        }
