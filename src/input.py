from src.tool import check_positive


def input_float(text):
    """
    Standard input to check is float.
    :param text: Display Text.
    :return: float
    """
    result_float = None
    while True:
        try:
            result_float = check_positive(float(input(text)))
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
            result_int = check_positive(int(input(text)))
            if result_int < 0:
                raise ValueError("Not accept negative value")
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
            weight_kg = check_positive(float(results[1]))
            distance_km = check_positive(float(results[2]))
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
            no_of_vehicles = check_positive(int(results[0]))
            max_speed = check_positive(int(results[1]))
            max_carriable_weigh = check_positive(int(results[2]))

            results = (no_of_vehicles, max_speed, max_carriable_weigh)
        except ValueError:
            print("Please enter valid input [no_of_vehicles max_speed max_carriable_weigh]")
            continue
        else:
            break
    return results


def input_argument_float(index, arg_list):
    """
    Command line argument input to check is float
    :param index: Argument index position.
    :param arg_list: List of argument
    :return: None or Float
    """
    result = None
    if len(arg_list) < 2 or index < 1:
        return None
    if len(arg_list) > index:
        result = arg_list[index]
        try:
            result = check_positive(float(result))
        except ValueError:
            result = None
    return result


def input_argument_int(index, arg_list):
    """
    Command line argument input to check is integer
    :param index: Argument index position.
    :param arg_list: List of argument
    :return: None or integer
    """
    result = None
    if len(arg_list) < 2 or index < 1:
        return None
    if len(arg_list) > index:
        result = arg_list[index]
        try:
            result = check_positive(int(result))
        except ValueError:
            result = None
    return result


def input_argument_package(arg_list, total_packages):
    """
    Command line argument input to check package input [(str, float, float, str)]
    :param arg_list: List of argument
    :param total_packages: Total of package
    :return: None or List of package
    """
    if arg_list is None or total_packages is None:
        return None
    if len(arg_list) < 4 or total_packages < 1:
        return None

    packages_input_index = total_packages * 4 + 3
    if len(arg_list) < packages_input_index:
        return None
    index_of_pacakge = {3: str, 4: float, 5: float, 6: str}
    packages_result = []
    for x in range(0, total_packages):
        tmp_package = []
        for ind, typ in index_of_pacakge.items():
            ind += x * 4
            try:
                if typ == float:
                    tmp_package.append(check_positive(typ(arg_list[ind])))
                else:
                    tmp_package.append(typ(arg_list[ind]))
            except ValueError:
                return None
        packages_result.append(tuple(tmp_package))

    return packages_result
