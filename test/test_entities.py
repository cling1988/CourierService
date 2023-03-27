import unittest
from src.entities import Package, PackagesShipment


class TestEntities(unittest.TestCase):
    p1 = Package('PKG1', 50, 30, 'OFR001', 70)
    p2 = Package('PKG2', 75, 125, 'OFR008', 70)

    def test_package(self):
        self.assertFalse(self.p1 == self.p2)

        result = ('PKG1', 50, 30, 'OFR001')
        self.assertEqual((self.p1.pkg_id, self.p1.weight, self.p1.distance, self.p1.promo_code), result)

    def test_packages_shipment(self):
        ps = PackagesShipment([self.p1, self.p2])
        self.assertEqual(ps.total_weight, 125)
        self.assertEqual(ps.min_distance, 30)
        self.assertEqual(ps.max_distance, 125)


if __name__ == '__main__':
    unittest.main()
