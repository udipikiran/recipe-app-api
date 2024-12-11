"""
Sample Test
"""

from django.test import SimpleTestCase

from . import calc


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        res = calc.subtract(4, 10)
        self.assertEqual(res, -6)
