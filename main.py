import sys

from src.delivery import delivery_estimate
from src.entities import Package
from src.fees import delivery_cost, get_discount, load_discount_config, discount_cost
from src.input import input_float, input_int, input_package, input_delivery, input_argument_float, input_argument_int, \
    input_argument_package

if __name__ == '__main__':
    config_path = 'config/discount_config.json'
    discount_config = load_discount_config(config_path)
    base_delivery_cost = None
    no_of_packages = None
    packages_input = []
    no_of_vehicles = None
    max_speed = None
    max_carriable_weigh = None

    len_arg = len(sys.argv)
    if len_arg > 1:
        base_delivery_cost = input_argument_float(1, sys.argv)
        no_of_packages = input_argument_int(2, sys.argv)
        if no_of_packages > 25:
            no_of_packages = None
        if no_of_packages and no_of_packages > 0:
            packages_input = input_argument_package(sys.argv, no_of_packages)
            delivery_index = no_of_packages * 4 + 3
            no_of_vehicles = input_argument_int(delivery_index, sys.argv)
            max_speed = input_argument_int(delivery_index + 1, sys.argv)
            max_carriable_weigh = input_argument_int(delivery_index + 2, sys.argv)

    if base_delivery_cost is None:
        base_delivery_cost = input_float('Please enter base delivery cost: ')

    if no_of_packages is None:
        no_of_packages = input_int('Please enter number of package(s), max is 25: ')

    if no_of_packages <= 0:
        print('No package to process')
        exit()

    if no_of_packages > 25:
        print('Too much package to process, please retry.')
        exit()

    if packages_input is None or len(packages_input) == 0:
        packages_input = []
        print('Please enter package input with format [pkg_id pkg_weight_in_kg distance_in_km offer_code]')
        for _ in range(no_of_packages):
            packages_input.append(input_package())

    if no_of_vehicles is None or max_speed is None or max_carriable_weigh is None:
        print("Please enter delivery input with format [no_of_vehicles max_speed max_carriable_weigh]")
        no_of_vehicles, max_speed, max_carriable_weigh = input_delivery()

    packages = []
    for pkg_id, pkg_weight, distance, code in packages_input:
        packages.append(Package(pkg_id, pkg_weight, distance, code, max_speed))
    print('-----output-----')
    print('[pkg_id discount total_cost estimated_delivery_time_in_hours]')
    packages = delivery_estimate(packages, no_of_vehicles, max_carriable_weigh)
    for pkg in packages:
        total_delivery = delivery_cost(base_delivery_cost, pkg.weight, pkg.distance)
        total_discount = discount_cost(total_delivery, get_discount(pkg.promo_code, pkg.weight, pkg.distance,
                                                                    discount_config))
        total_delivery_after_discount = total_delivery - total_discount
        if pkg.is_valid:
            format_result = "{} {:.2f} {:.2f} {:.2f}".format(pkg.pkg_id, total_discount, total_delivery_after_discount,
                                                             pkg.estimate_delivery_hour)
        else:
            format_result = "{} {:.2f} {:.2f} N/A".format(pkg.pkg_id, total_discount, total_delivery_after_discount)
        print(format_result)
    exit()
