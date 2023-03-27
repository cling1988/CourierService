import math


def decimal_truncate(value, decimals):
    return math.floor(value * 10 ** decimals) / 10 ** decimals
