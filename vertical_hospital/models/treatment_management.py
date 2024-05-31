# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re

class TreatmentManagement(models.Model):
    _name = 'treatment.management'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = 'treatment management'
    

    treatment_code = fields.Char('Código de tratamiento')
    treatment_name = fields.Char('Nombre del tratamiento')
    treatment_doctor = fields.Char('Medico tratante')
    
    def name_get(self):
        result = []
        for tm_line in self.sudo():
            name = tm_line.treatment_code
            result.append((tm_line.id, name))
        return result
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if '026' in vals['treatment_code']:
                raise ValidationError(_('No debe de tener la secuencia 026.'))
                
        return super().create(vals_list)
