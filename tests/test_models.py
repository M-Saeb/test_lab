# -*- coding: utf-8 -*-

from odoo.tests import common, tagged

@tagged('-standard', 'nice')
class TestCaseA(common.TransactionCase):
    
    def test_value(self):
        # this is the first test

        rcd = self.env['test_lab.test_lab'].create({
            'name': 'Mike',
            'value': 30
        })
        self.assertEqual(rcd.name, 'Mike')