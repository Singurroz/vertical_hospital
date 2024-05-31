# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class PacientPortal():
    @http.route(['/pacientes/consulta/<string:sequence>'], type='json', auth="public", website=True)
    def pacient_INFO(self, sequence, access_token=None, report_type=None, download=False, **kw):
        pacient = request.env['res.partner'].sudo().search([('sequence','=', sequence)])
        if pacient:
            return {
                'sequence': pacient.sequence,
                'name': pacient.name,
                'dni': pacient.dni,
                'state': pacient.state,
            }
        else:
            return False