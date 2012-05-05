import numbers

def is_natural(x):
    """ testet, ob eine Variable eine natürliche Zahl ist """

    return isinstance(x, numbers.Integral) and x >= 0
