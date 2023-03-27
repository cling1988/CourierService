import unittest

from src.delivery import delivery_estimate, generate_package_delivery_list
from src.entities import Package, PackagesShipment


class TestDelivery(unittest.TestCase):
    p1 = Package('PKG1', 50, 30, 'OFR001', 70)
    p2 = Package('PKG2', 75, 125, 'OFR008', 70)
    p3 = Package('PKG3', 175, 100, 'OFR003', 70)
    p4 = Package('PKG4', 110, 60, 'OFR002', 70)
    p5 = Package('PKG5', 155, 95, 'NA', 70)

    def test_delivery_estimate(self):
        packages = [self.p1, self.p2, self.p3, self.p4, self.p5]
        self.p1.set_estimate_delivery_hour(3.98)
        self.p2.set_estimate_delivery_hour(1.78)
        self.p3.set_estimate_delivery_hour(1.42)
        self.p4.set_estimate_delivery_hour(0.85)
        self.p5.set_estimate_delivery_hour(4.19)
        result = [self.p1, self.p2, self.p3, self.p4, self.p5]
        self.assertEqual(delivery_estimate(packages, 2, 200), result)

    def test_generate_package_delivery_list(self):
        packages = [self.p1, self.p2, self.p3, self.p4, self.p5]
        result = [PackagesShipment([self.p2, self.p4]), PackagesShipment([self.p3]),
                  PackagesShipment([self.p5]), PackagesShipment([self.p1])]
        self.assertEqual(generate_package_delivery_list(packages, 200), result)


if __name__ == '__main__':
    unittest.main()
