#!/usr/bin/env python3.2
""" Einige Messungen der Ausführungszeit für die binomk-Funktionen """

from binomk import *
from time import clock
from timeit import Timer

def time_func(func, *args):
    """
    Misst die Ausführungszeit einer Funktion auf sehr naive Weise

    Parameter:
        1. Funktionsname
        2. der Funktion zu übergebende Argumente
    Rückgabe: Ausführungszeit in Sekunden

    """

    # CPU-Zeit vor Ausführung der Funktion speichern
    before_time = clock()

    # Funktion ausführen
    func(*args)

    # CPU-Zeit nach Ausführung der Funktion speichern
    after_time  = clock()

    # Differenz zurückgeben
    return after_time - before_time



#print(time_func(binomk_rek, 34, 5))

t = Timer("binomk_iter(34, 5)", "from binomk import binomk_iter")
print(t.repeat(3, 1000))
