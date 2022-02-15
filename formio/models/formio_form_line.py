from odoo import api, fields, models


class FormioFormLine(models.Model):
    _name = 'formio.form.line'
    _description = 'Form lines'

    form_id = fields.Many2one(
        'formio.form',
        ondelete='cascade',
        readonly=True,
        string='Form')

    label = fields.Char(
        'Label',
        index=True)

    key = fields.Char(
        'Key')

    value_label = fields.Char(
        'Value Label',
        index=True)

    value_key = fields.Char(
        'Value Key')
