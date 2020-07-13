# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test_lab(models.Model):
    _name = 'test_lab.test_lab'
    _description = 'test_lab.test_lab'

    name = fields.Char(string="the new name")
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(default="it this  working ?")
    number = fields.Integer(string="yup I'm that desprate")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
