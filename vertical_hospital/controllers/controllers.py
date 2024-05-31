# -*- coding: utf-8 -*-
# from odoo import http


# class VerticalHospital(http.Controller):
#     @http.route('/vertical_hospital/vertical_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vertical_hospital/vertical_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vertical_hospital.listing', {
#             'root': '/vertical_hospital/vertical_hospital',
#             'objects': http.request.env['vertical_hospital.vertical_hospital'].search([]),
#         })

#     @http.route('/vertical_hospital/vertical_hospital/objects/<model("vertical_hospital.vertical_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vertical_hospital.object', {
#             'object': obj
#         })
