import numbers

def mersenne_zahl_nr(n):
    """
    berechnet eine Mersenne-Zahl 2^n-1 mit einer Schleife

    Parameter: n
    Rückgabe:  2^n-1

    """
    # Sicherstellen, dass n natürliche Zahl
    if not isinstance(n, numbers.Integral) or n < 0:
        raise Exception("n muss natürliche Zahl sein")

    # Mersenne-Zahl berechnen
    mersenne_nr = 1
    for factors in range(0, n):
        mersenne_nr *= 2

    return(mersenne_nr - 1)
