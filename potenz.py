from number import is_natural

def pow_rek(base, expon):
    """
    Berechnet endrekursiv base^expon für natürliche Zahlen

    0^0 wird als 1 festgelegt.

    """

    # Dumme Eingaben abfangen
    if not is_natural(base) or not is_natural(expon):
        raise Exception("Basis und Exponent müssen natürliche Zahlen sein")

    # rekursive Hilfsfunktion mit kumulativem Parameter definieren
    def pow_helper(prod, base, expon):
        if expon == 0:
            return prod
        else:
            return pow_helper(prod * base, base, expon - 1)

    # Aufruf der Hilfsfunktion
    return pow_helper(1, base, expon)


def pow_iter(base, expon):
    """
    Berechnet endrekursiv base^expon für natürliche Zahlen

    0^0 wird als 1 festgelegt.

    """

    # Dumme Eingaben abfangen
    if not is_natural(base) or not is_natural(expon):
        raise Exception("Basis und Exponent müssen natürliche Zahlen sein")

    # Potenz berechnen
    prod = 1
    for factor_nr in range(expon):
        prod *= base

    return prod
