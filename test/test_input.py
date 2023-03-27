import unittest
from unittest.mock import patch

from src.input import input_float, input_int, input_package, input_delivery


class TestDeliveryCost(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
