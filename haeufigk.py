def element_freqs_of(ary_of_arys):
    """
    Bestimmt die Häufigkeiten der Elemente in einem Array von Arrays

    Diese Funktion kann natürlich auch verwendet werden, um die Häufigkeit der
    Farben in einem durch ein Array von Arrays repräsentiertes Bild zu
    bestimmen. Das Format für die Farben ist dann frei wählbar und der
    Algorithmus passt auch nicht auf, ob die Zeilen in dem Bild gleich lang
    sind o. ä.

    (Die Arrayelemente müssen gültige Python-Dictionary-Schlüssel
     (unveränderliche Objekte) sein.)

    Rückgabe: Dictionary mit Arrayelementen als Schlüssel und deren
    Häufigkeiten als Werte

    """

    # Häufigkeiten-Dictionary initialisieren
    frequency_of = {}

    # Arrays im Array von Arrays durchgehen
    for ary in ary_of_arys:
        # Elemente in den Arrays durchgehen
        for elem in ary:
            # Häufigkeit des aktuellen Elementes inkrementieren...
            if elem in frequency_of:
                frequency_of[elem] += 1
            # ... oder auf 1 setzen, falls es bisher noch nicht vorkam
            else:
                frequency_of[elem] =  1

    return frequency_of
