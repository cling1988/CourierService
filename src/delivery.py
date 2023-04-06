from itertools import combinations
from decimal import Decimal, getcontext

from src.entities import PackagesShipment


def generate_package_delivery_list(packages, max_carriable_weight):
    """
    Generate possible combination match with max carriable weight
    :param packages:(list) list of Package object
    :param max_carriable_weight:(int) Max carriable weight per transport.
    :return: list of available PackagesShipment object
    """
    if packages is None or len(packages) <= 0:
        raise TypeError("Input packages cannot be empty")
    if max_carriable_weight is None or max_carriable_weight <= 0:
        raise TypeError("Input cannot less than or equal 0")
    if len(packages) > 25:
        raise ValueError("Packages size not more than 25.")
    # Calculate sum of all packages weight is more than max carriable weight.
    packages_shipment_all = PackagesShipment(packages)
    if packages_shipment_all.total_weight <= max_carriable_weight:
        return [packages_shipment_all]

    # Generate match available combinations
    match_packages = []
    for i in range(1, len(packages)):
        available_combination = list(combinations(packages, i))
        for pkgs in available_combination:
            ps = PackagesShipment(pkgs)
            if ps.total_weight <= max_carriable_weight:
                match_packages.append(ps)
                match_packages.sort(reverse=True)
            elif len(pkgs) == 1:
                ps.is_valid = False
                match_packages.append(ps)
                match_packages.sort(reverse=True)

    # Remove duplicate package
    valid_match_packages_shipment = []
    valid_match_packages = []
    for pkg_ship in match_packages:
        if pkg_ship.is_packages_exist(valid_match_packages):
            continue
        valid_match_packages_shipment.append(pkg_ship)
        valid_match_packages.extend(pkg_ship.packages)

    return valid_match_packages_shipment


def delivery_estimate(packages, no_of_vehicles, max_carriable_weight):
    """
    Generate delivery estimate for packages
    :param packages: (list)
    :param no_of_vehicles: (int) Total available vehicle
    :param max_carriable_weight: (int) Max weight per vehicle
    :return: list of package with estimate hour
    """
    if packages is None or len(packages) <= 0:
        raise TypeError("Input packages cannot be empty")
    if no_of_vehicles is None or max_carriable_weight is None or no_of_vehicles <= 0 or max_carriable_weight <= 0:
        raise TypeError("Input cannot less than or equal 0")
    if len(packages) > 25:
        raise ValueError("Packages size not more than 25.")
    getcontext().prec = 3
    result = []
    waiting_time = []
    # Init 0 waiting time
    for i in range(0, min(no_of_vehicles, len(packages))):
        waiting_time.append(0)
    package_shipments = generate_package_delivery_list(packages, max_carriable_weight)
    if len(package_shipments) > 0:
        for pkg_ship in package_shipments:
            if pkg_ship.is_valid:
                min_time = min(waiting_time)
                index_waiting = waiting_time.index(min_time)
                for package in pkg_ship.packages:
                    min_time_dec = Decimal(min_time)
                    del_hour_dec = Decimal(package.delivery_hour)
                    delivery_hours = min_time_dec + del_hour_dec
                    package.set_estimate_delivery_hour(float(delivery_hours))
                    result.append(package)
                waiting_time[index_waiting] = min_time_dec + Decimal(pkg_ship.max_delivery_hour) * 2
            else:
                for package in pkg_ship.packages:
                    package.set_estimate_delivery_hour(0)
                    package.is_valid = False
                    result.append(package)

    result = sorted(result, key=lambda x: x.pkg_id)
    return result
