from functools import total_ordering
from operator import attrgetter

from src.tool import decimal_truncate


@total_ordering
class Package:
    """
    Package object contains package info.

    Parameters:
        pkg_id(str): Package Id.
        weight(float): Package weight in KG.
        distance(float): Destination distance in KM.
        promo_code(str): Package promo code if any.
        max_speed_hour(int): Max speed vehicle per hour.
    """

    def __init__(self, pkg_id, weight, distance, promo_code, max_speed_hour):
        self.pkg_id = pkg_id
        self.weight = weight
        self.distance = distance
        self.promo_code = promo_code
        self.delivery_hour = decimal_truncate(self.distance / max_speed_hour, 2)
        self.estimate_delivery_hour = None
        self.is_valid = True

    def __eq__(self, other):
        return ((self.pkg_id.lower(), self.weight, self.distance, self.promo_code.upper()) ==
                (other.pkg_id.lower(), other.weight, other.distance, other.promo_code.upper()))

    def __lt__(self, other):
        return (self.weight, self.distance) < (other.weight, other.distance)

    def __str__(self):
        return f'{self.pkg_id} {self.weight} {self.distance} {self.promo_code}'

    def __repr__(self):
        return repr((self.pkg_id, self.weight, self.distance, self.promo_code, self.delivery_hour))

    def set_estimate_delivery_hour(self, estimate_delivery_hour):
        self.estimate_delivery_hour = estimate_delivery_hour


@total_ordering
class PackagesShipment:
    """
    PackagesShipment object contains many package(s).

    Parameters:
        packages(list): Collection of Package object.

    Attributes:
        packages(list): Collection of Package object.
        total_weight(float): SUM weight of packages.
        min_distance(float): MIN distance from list of packages.
        max_distance(float): MAX distance from list of packages.
        max_delivery_hour(float): MAX delivery hour from list of packages.

    """

    def __init__(self, packages):
        self.packages = list(packages)
        self.total_weight = sum(pkg.weight for pkg in self.packages)
        self.min_distance = min(self.packages, key=attrgetter('distance')).distance
        self.max_distance = max(self.packages, key=attrgetter('distance')).distance
        self.max_delivery_hour = max(self.packages, key=attrgetter('delivery_hour')).delivery_hour
        self.is_valid = True

    def __eq__(self, other):
        return self.packages == other.packages

    def __lt__(self, other):
        """
        Override comparison less than method.
        Heavier weight first, then nearest distance.
        :param other: PackagesShipment object.
        :return: Return boolean
        """
        size_package = len(self.packages)
        size_other_package = len(other.packages)
        if size_package != size_other_package:
            return size_package < size_other_package
        elif self.total_weight != other.total_weight:
            return self.total_weight < other.total_weight
        else:
            return self.max_distance > other.max_distance

    def __repr__(self):
        return f'{self.packages} {self.total_weight} {self.min_distance} {self.max_distance}'

    def is_packages_exist(self, packages):
        """
        Check the package existed
        :param packages: (List) List of object Packages
        :return: boolean True is existed.
        """
        if packages is None:
            return False
        if isinstance(packages, list):
            if len(packages) <= 0:
                return False
        elif isinstance(packages, Package):
            packages = [packages]

        for pkg in self.packages:
            if pkg in packages:
                return True
        return False
