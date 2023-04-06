import unittest
from src.entities import Package, PackagesShipment


class TestEntities(unittest.TestCase):
    p1 = Package('PKG1', 50, 30, 'OFR001', 70)
    p2 = Package('PKG2', 75, 125, 'OFR008', 70)
    p3 = Package('PKG3', 100, 125, 'OFR008', 70)
    p4 = Package('包裹4', 120, 125, 'OFR008', 70)

    def test_package(self):
        self.assertFalse(self.p1 == self.p2)
        self.assertFalse(self.p1 > self.p2)
        result = ('PKG1', 50, 30, 'OFR001')
        self.assertEqual((self.p1.pkg_id, self.p1.weight, self.p1.distance, self.p1.promo_code), result)

        self.assertEqual(self.p4.pkg_id, '包裹4')
        self.assertTrue(self.p4 > self.p3)

    def test_packages_shipment(self):
        ps = PackagesShipment([self.p1, self.p2])
        self.assertEqual(ps.total_weight, 125)
        self.assertEqual(ps.min_distance, 30)
        self.assertEqual(ps.max_distance, 125)
        self.assertEqual(ps.max_delivery_hour, 1.78)
        self.assertFalse(ps.is_packages_exist(self.p3))

        ps2 = PackagesShipment([self.p3])
        self.assertFalse(ps < ps2)


if __name__ == '__main__':
    unittest.main()
