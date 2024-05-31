# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re

class PacientManagement(models.Model):
    _name = 'patient.management'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = 'patient management'
    

    sequence = fields.Char(
        'Pacient Sequence',
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    name = fields.Char('Pacient name',required=True)
    dni = fields.Char('DNI',tracking=1)
    create_date = fields.Datetime(
        string="Creation Date", index=True, readonly=True)
    write_date = fields.Datetime(
        string="Write Date", index=True, readonly=True,traking=True)
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('enable', "Enable"),
            ('disabled', "Disabled"),
        ],
        string="Status",
        copy=False, index=True,
        tracking=2,
        default='draft')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="User",
        default=lambda self: self.env.context.get('user_id', self.env.user.id),
        tracking=3
        )
    
    
    _sql_constraints = [
        ('dni_unique',
         'UNIQUE(dni)',
         "Debe de ser unico el DNI."),
    ]
    
    
    @api.model_create_multi
    def create(self, vals_list):
        pattern ="^[0-9]$"
        for vals in vals_list:
            if vals.get('sequence', _("New")) == _("New"):
                seq_date = fields.Datetime.context_timestamp(
                    self, fields.Datetime.to_datetime(vals['create_date'])
                ) if 'create_date' in vals else None
                vals['sequence'] = self.env['ir.sequence'].next_by_code(
                    'vertical.hospital', sequence_date=seq_date) or _("New")
            dni = vals['dni']
            if dni.isdigit():#re.match(pattern, vals['dni']):
                continue
            else:
                raise ValidationError(_('Solo se puede agregar numeros.'))
        return super().create(vals_list)
