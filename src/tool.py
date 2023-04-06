import math


def decimal_truncate(value, decimals):
    return math.floor(value * 10 ** decimals) / 10 ** decimals


def check_positive(value):
    if value < 0:
        raise ValueError("Not accept negative value")
    return value