#!/usr/bin/env python3.2
""" Fragt RGB-Wert einer Farbe ab und gibt CMYK-Wert zurück """

def rgb_to_cmyk(rgb_list):
    """
    Wandelt RGB- in CMYK-Werte um

    Parameter: rgb_list = [r, g, b]
    Rückgabe:  [c, m, y, k]

    """
    # Eingabe auf Korrektheit prüfen
    for ch_val in rgb_list:
        if ch_val > 255 or ch_val < 0:
            raise Exception("RGB-Werte müssen im Bereich von 0 bis 255"
                            + " liegen")

    # ominösen Hilfswert berechnen
    aux = max(rgb_list) / 255

    # RGB-Schwarz (0, 0, 0) abfangen
    if aux == 0:
        return [0, 0, 0, 1]

    # C, M und Y berechnen
    cmyk_list = []
    for ch_val in rgb_list:
        cmyk_list.append( (aux - (ch_val/255)) / aux )

    # K berechnen
    cmyk_list.append( 1 - aux )

    return cmyk_list


# Bei Aufruf als Skript wird gefragt...
if __name__ == "__main__":
    # RGB-Werte abfragen
    print("Eingabe der RGB-Farbe:")
    r = input("R = ")
    g = input("G = ")
    b = input("B = ")

    # Umwandeln in int und als Liste speichern
    rgb_val = list( map(int, [r, g, b]) )

    # CMYK berechnen und ausgeben
    print(rgb_to_cmyk(rgb_val))
