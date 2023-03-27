def input_float(text):
    """
    Standard input to check is float.
    :param text: Display Text.
    :return: float
    """
    result_float = None
    while True:
        try:
            result_float = float(input(text))
        except ValueError:
            print("Please enter valid input")
            continue
        else:
            break
    return result_float


def input_int(text):
    """
    Standard input to check is int.
    :param text: Display Text.
    :return: int
    """
    result_int = None
    while True:
        try:
            result_int = int(input(text))
        except ValueError:
            print("Please enter valid input")
            continue
        else:
            break
    return result_int


def input_package():
    """
    Standard input to check is valid input (str, float, float, str)
    :return: list
    """
    results = None
    while True:
        try:
            results = str(input()).split(' ')
            if len(results) < 3:
                print("Please enter valid input [pkg_id pkg_weight_in_kg distance_in_km offer_code]")
                continue
            pkg_id = str(results[0])
            weight_kg = float(results[1])
            distance_km = float(results[2])
            offer_code = str(results[3]).upper() if len(results) > 3 else None
            results = (pkg_id, weight_kg, distance_km, offer_code)
        except ValueError:
            print("Please enter valid input [pkg_id pkg_weight_in_kg distance_in_km offer_code]")
            continue
        else:
            break
    return results


def input_delivery():
    """
    Standard input to check is valid input (int, int, int)
    :return: list
    """
    results = None
    while True:
        try:
            results = str(input()).split(' ')
            if len(results) < 3:
                print("Please enter valid input [no_of_vehicles max_speed max_carriable_weigh]")
                continue
            no_of_vehicles = int(results[0])
            max_speed = int(results[1])
            max_carriable_weigh = int(results[2])
            results = (no_of_vehicles, max_speed, max_carriable_weigh)
        except ValueError:
            print("Please enter valid input [no_of_vehicles max_speed max_carriable_weigh]")
            continue
        else:
            break
    return results