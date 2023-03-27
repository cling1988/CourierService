import unittest

from src.fees import delivery_cost, get_discount, discount_cost


class TestDeliveryCost(unittest.TestCase):
    valid_sample_data = ((100, 10, 100, 700), (50.1, 5.5, 6.7, 138.6), (100.555, 70.5555, 20.255, 907.61))

    invalid_sample_data = ((None, None, None), (-100, 25, 50), ("base", "100", "23.1"), (100, -30, 20))

    def test_valid_input(self):
        for base, weight, distance, result in self.valid_sample_data:
            self.assertEqual(delivery_cost(base, weight, distance), result)

    def test_invalid_input(self):
        for base, weight, distance in self.invalid_sample_data:
            with self.assertRaises(TypeError):
                delivery_cost(base, weight, distance)


class TestDiscount(unittest.TestCase):
    sample_data = (("OFR001", 10, 100, 0), ("ofr003", 10, 100, 5), ("OFR004", 70, 100, 0), (None, None, None, 0))

    def test_get_discount(self):
        for code, weight, distance, result in self.sample_data:
            self.assertEqual(get_discount(code, weight, distance), result)


class TestDiscountCost(unittest.TestCase):
    sample_data = ((700, 5, 35), (175, 0, 0), (600.50, 10, 60.05))

    invalid_sample_data = ((None, None), (-100, 25), ("base", "5"), (100, -10))

    def test_discount_cost(self):
        for total_cost, discount, result in self.sample_data:
            self.assertEqual(discount_cost(total_cost, discount), result)

    def test_invalid_input(self):
        for total_cost, discount in self.invalid_sample_data:
            with self.assertRaises(TypeError):
                discount_cost(total_cost, discount)


if __name__ == '__main__':
    unittest.main()
