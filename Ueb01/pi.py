import numbers
from math import sqrt

def pi_approx_euler(n):
    """
    Approximiert π mit einer Formel nach Euler bis zum Grad n

    Parameter: n ... Anzahl der Summanden in der Summenformel
    Rückgabe: Näherung von Pi

    """

    # Sicherstellen, dass n natürliche Zahl und > 0
    if not isinstance(n, numbers.Integral) or n < 1:
        raise Exception("n muss natürliche Zahl >= 1 sein.")

    # Summe berechnen...
    fast_pi = 0
    for i in range(1, n + 1):
        fast_pi += 1 / i**2

    return sqrt(fast_pi * 6)
