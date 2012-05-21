from boolarray import Boolarray

# Copy & Paste ist sehr praktisch, wenn man zu viele Aufgaben hat. Das Auge
# des aufmerksamen Betrachters wird allerdings feine Unterschiede zur Vorlage
# bemerken.

from math import sqrt

def eratosthenes(grenze):
    """
    Berechnet die Primzahlen im Bereich von 0 bis grenze.

    Zurückgegeben wird ein Boolarray, in dem die Werte an allen primen Indizes
    False und an allen nicht-primen Indizes True sind.

    """

    # Nur arbeiten, wenn eine sinnvolle Obergrenze gewählt wurde
    if grenze >= 2:
        # 0 und 1 sind keine Primzahlen, der Rest erstmal schon
        primzahlen = Boolarray([True, True])

        # Berechnen, wann wir Feierabend machen können
        berechnungsgrenze = int(sqrt(grenze)) + 1

        # Von 2 bis Feierabend alle ganzen Zahlen durchlaufen
        for i in range(2, berechnungsgrenze):
            # Wenn man eine Primzahl findet, alle Vielfache entprimen
            if primzahlen.get(i) == False:
                for j in range(2*i, grenze + 1, i):
                    primzahlen.set(j, True)  # True == nicht prim!

        return primzahlen

    else:
        return None


def extract_primes_from(boolarray, grenze):
    """
    Gibt die im von eratosthenes() im boolarray kodierten Primzahlen zurück

    Da sich allein aus boolarray nicht feststellen lässt, bis zu welcher Zahl
    auf Primität getestet wurde, muss die grenze des eratosthenes-Aufrufs mit
    angegeben werden.

    """

    # Walk through the array and find the prime indices (marked False)
    primes = []
    for ind in range(2, grenze + 1):
        if boolarray.get(ind) == False:
            primes.append(ind)

    return primes


def calc_primes_through(grenze):
    """ kleine Convenience-Funktion """

    return extract_primes_from(eratosthenes(grenze), grenze)
