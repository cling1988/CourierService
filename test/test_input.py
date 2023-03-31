import unittest
from unittest.mock import patch

from src.input import input_float, input_int, input_package, input_delivery, input_argument_float, input_argument_int, \
    input_argument_package


class TestDeliveryCost(unittest.TestCase):
    sample_argument = ['main.py', '100.50', 2, 'PKG1', 50, 30, 'OFR001', 'PKG2', 75, 125, 'OFR008']

    @patch('builtins.input', lambda *args: 100.55)
    def test_float_input(self):
        self.assertEqual(input_float('Enter float'), 100.55)

    @patch('builtins.input', lambda *args: 100)
    def test_int_input(self):
        self.assertEqual(input_int('Enter float'), 100)

    @patch('builtins.input', lambda *args: 'PKG1 5 10 OFR001')
    def test_package_input(self):
        self.assertEqual(input_package(), ('PKG1', 5, 10, 'OFR001'))

    @patch('builtins.input', lambda *args: 'PKG1 5 10')
    def test_package_input_without_code(self):
        self.assertEqual(input_package(), ('PKG1', 5, 10, None))

    @patch('builtins.input', lambda *args: '2 70 200')
    def test_delivery_input(self):
        self.assertEqual(input_delivery(), (2, 70, 200))

    def test_input_argument_float(self):
        self.assertEqual(input_argument_float(1, self.sample_argument), 100.5)

    def test_input_argument_int(self):
        self.assertEqual(input_argument_int(2, self.sample_argument), 2)

    def test_input_argument_int(self):
        result = [('PKG1', 50, 30, 'OFR001'), ('PKG2', 75, 125, 'OFR008')]
        self.assertEqual(input_argument_package(self.sample_argument, 2), result)


if __name__ == '__main__':
    unittest.main()
