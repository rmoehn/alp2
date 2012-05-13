from number import is_natural
import numbers

def umnozhaj(fak1, fak2):
    """
    Multipliziert fak1 und fak2 nach der russischen Bauernmethode

    fak1 und fak2 müssen natürliche Zahlen sein

    """

    # Dumme Eingaben abfangen
    if not is_natural(fak1) or not is_natural(fak2):
        raise Exception("Russische Bauern brauchen und können nur"
                        + " natürliche Zahlen multiplizieren.")

    # Akkumulator initialisieren
    if is_even(fak1): # bei gerader Zahl in der ersten Spalte
        prod = 0
    else:
        prod = fak2

    # Iterieren, bis fak1 0 oder 1 erreicht hat
    while fak1 > 1:
        # fak1 ganzzahlig durch zwei teilen
        fak1 >>= 1

        # fak2 mit zwei multiplizieren
        fak2 <<= 1

        # Bei gerader Zahl in der ersten Spalte zweite Spalte streichen
        if is_even(fak1):
            pass
        # Bei ungerader Zahl zum Ergebnis addieren
        else:
            prod += fak2

    return prod


def is_even(n):
    """
    Prüft, ob eine natürliche Zahl gerade ist

    """

    # Dumme Eingaben abfangen
    if not isinstance(n, numbers.Integral):
        raise Exception("Nur ganze Zahlen als Eingabe erlaubt.")

    # n ganzzahlig durch 2 teilen
    half_n = n >> 1

    # wenn n und das verdoppelte n/2 differieren, war es ungerade
    return n == (half_n << 1)
