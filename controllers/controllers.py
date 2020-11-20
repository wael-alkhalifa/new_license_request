# -*- coding: utf-8 -*-
# from odoo import http


# class Decisions(http.Controller):
#     @http.route('/decisions/decisions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/decisions/decisions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('decisions.listing', {
#             'root': '/decisions/decisions',
#             'objects': http.request.env['decisions.decisions'].search([]),
#         })

#     @http.route('/decisions/decisions/objects/<model("decisions.decisions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('decisions.object', {
#             'object': obj
#         })
