# -*- coding: utf-8 -*-
from odoo import http


class test_lab(http.Controller):
    @http.route('/test_lab/test_lab/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/test_lab/test_lab/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('test_lab.listing', {
            'root': '/test_lab/test_lab',
            'objects': http.request.env['test_lab.test_lab'].search([]),
        })

    @http.route('/test_lab/test_lab/objects/<model("test_lab.test_lab"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('test_lab.object', {
            'object': obj
        })
