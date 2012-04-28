import numbers

def dez_to_bin(number, length):
    """
    Wandelt eine Zahl number in eine Binärzahl der Länge length um

    Rückgabe: [b_(length-1), b_(length-2), ..., b_1, b_0]

    """
    # Prüfen, ob number ganze Zahl ist
    if not isinstance(number, numbers.Integral):
        raise Exception("number muss ganze Zahl sein.")

    # Prüfen, ob length natürliche Zahl > 0 ist
    if not isinstance(length, numbers.Integral) or length < 1:
        raise Exception("length muss natürliche Zahl > 0 sein.")

    # Prüfen, ob die Binärdarstellung von number nicht länger als length ist
    upper_limit =  2**(length-1) - 1
    lower_limit = -2**(length-1)
    if number > upper_limit or number < lower_limit:
        raise Exception("Bei dieser Wortlänge können nur Zahlen von "
                        + str(lower_limit) + " bis "
                        + str(upper_limit)
                        + " binär dargestellt werden.")

    # Ausgabeliste initialisieren
    number_bin = []

    # Stellen der Ausgabeliste berechnen
    for stelle in range(0, length):
        number_bin.insert(0, number % 2)
        number //= 2

    return number_bin
