import json


def delivery_cost(base_cost, weight_kg, distance_km) -> float:
    """
    Calculate delivery cost with formula
    Base Delivery Cost + (Package Total Weight * 10) + (Distance to Destination * 5)
    :param base_cost:(float) A 2 decimal float
    :param weight_kg:(float) A 3 decimal float
    :param distance_km:(float) A 1 decimal float
    :return:total_delivery_cost(float): 2 decimal float
    """
    if base_cost < 0 or weight_kg < 0 or distance_km < 0:
        raise TypeError("Input cannot less than 0")

    # Round to valid decimal
    base_cost = round(float(base_cost), 2)
    weight_kg = round(float(weight_kg), 3)
    distance_km = round(float(distance_km), 1)

    # Delivery cost calculation
    total_delivery_cost = base_cost + (weight_kg * 10) + (distance_km * 5)

    # Round result to 2 decimal
    return round(float(total_delivery_cost), 2)


def load_discount_config(config_path):
    """
    Load json config file into dictionary
    :param config_path:(string) Json discount config file path
    :return: Config dict
    """
    with open(config_path) as config_file:
        discount_config = json.load(config_file)
    return discount_config


def get_discount(offer_code, weight_kg, distance_km, discount_config=None):
    """
    Get discount
    :param offer_code:(string) offer code
    :param weight_kg:(float) A 3 decimal float, total package weight in KG
    :param distance_km:(float) A 1 decimal float, total distance to destination in KM
    :param discount_config:(dict) Config dictionary contain offer information.
    :return: discount(int)
    """
    if not discount_config:
        config_path = 'config/discount_config.json'
        discount_config = load_discount_config(config_path)
    if offer_code:
        if weight_kg < 0 or distance_km < 0:
            raise TypeError("Weight and distance cannot less than 0")
        offer_code = str(offer_code).upper()
        discount_detail = discount_config.get(offer_code)
        if not discount_detail:
            return 0
        if discount_detail['weight_min'] <= weight_kg <= discount_detail['weight_max']:
            if discount_detail['distance_min'] <= distance_km <= discount_detail['distance_max']:
                return int(discount_detail['discount'])
    return 0


def discount_cost(total_cost, discount):
    """
    Calculate discount cost with formula
    Cost * (discount)%
    :param total_cost:(float) A 2 decimal float, total cost
    :param discount:(int) Discount percent from 0 to 100
    :return: total_discount_cost(float)
    """
    if total_cost < 0 or discount < 0:
        raise TypeError("Input cannot less than 0")
    if discount > 100:
        raise TypeError("Discount cannot more than 100")

    # Round to valid decimal
    total_cost = round(float(total_cost), 2)
    discount = int(discount)

    # Discount cost calculation
    total_discount_cost = total_cost * discount / 100

    # Round result to 2 decimal
    return round(float(total_discount_cost), 2)
