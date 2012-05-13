from random import seed, randint

def is_sorted(array):
    """
    Prüft, ob eine Eingabeliste korrekt aufsteigend sortiert ist

    Parameter: array ... sortierte (?) Liste
    Rückgabe: True / False

    Funktion für Faltung wäre ganz praktisch hier...

    """

    # Initialise 'former element' for first loop pass
    former_elem = array[0]

    # Loop over array elements
    for elem in array:
        # Überprüfe Einhaltung des Kriteriums für Sortiertheit einer Liste (!)
        if former_elem > elem:
            return False

        # Current element becomes former element of next cycle
        former_elem = elem

    return True


def random_list(my_seed=None):
    """
    Erzeugt eine Liste zufälliger Länge mit zufälligen Zahlen

    Parameter:
        [seed] ... für reproduzierbare Fehler
    Rückgabe:
        zzListe

    """

    # No harvest without tilling
    seed(my_seed)

    # Fill list of random length with random integers out of a random range
    randlist = []
    for index in range(randint(10, 100)):
        randlist.append(randint(randint(-500, 10), randint(10, 723)))
            # Obfuscation even in Python

    return randlist
