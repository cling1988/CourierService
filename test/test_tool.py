import unittest

from src.tool import decimal_truncate, check_positive


class TestEntities(unittest.TestCase):

    def test_decimal_truncate(self):
        self.assertEqual(decimal_truncate(19.999, 2), 19.99)
        self.assertEqual(decimal_truncate(20.009, 2), 20.0)
        self.assertEqual(decimal_truncate(500.1, 5), 500.1)
        self.assertEqual(decimal_truncate(-20.009, 3), -20.009)

    def test_check_positive(self):
        self.assertEqual(check_positive(19.999), 19.999)
        with self.assertRaises(ValueError):
            check_positive(-19.999)


if __name__ == '__main__':
    unittest.main()
