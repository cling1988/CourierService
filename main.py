from src.delivery import delivery_estimate
from src.entities import Package
from src.fees import delivery_cost, get_discount, load_discount_config, discount_cost
from src.input import input_float, input_int, input_package, input_delivery

if __name__ == '__main__':
    config_path = 'config/discount_config.json'
    discount_config = load_discount_config(config_path)
    base_delivery_cost = input_float('Please enter base delivery cost: ')
    no_of_packages = input_int('Please enter number of package(s): ')

    if no_of_packages <= 0:
        print('No package to process')
        exit()
    packages_input = []
    print('Please enter package input with format [pkg_id pkg_weight_in_kg distance_in_km offer_code]')
    for _ in range(no_of_packages):
        packages_input.append(input_package())

    print("Please enter delivery input with format [no_of_vehicles max_speed max_carriable_weigh]")
    no_of_vehicles, max_speed, max_carriable_weigh = input_delivery()

    packages = []
    for pkg_id, pkg_weight, distance, code in packages_input:
        packages.append(Package(pkg_id, pkg_weight, distance, code, max_speed))

    print('-----output-----')
    packages = delivery_estimate(packages, no_of_vehicles, max_carriable_weigh)
    for pkg in packages:
        total_delivery = delivery_cost(base_delivery_cost, pkg.weight, pkg.distance)
        total_discount = discount_cost(total_delivery, get_discount(pkg.promo_code, pkg.weight, pkg.distance,
                                                                    discount_config))
        total_delivery_after_discount = total_delivery - total_discount
        format_result = "{} {:.2f} {:.2f} {:.2f}".format(pkg.pkg_id, total_discount, total_delivery_after_discount,
                                                         pkg.estimate_delivery_hour)
        print(format_result)
    exit()
