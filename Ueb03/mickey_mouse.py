#!/usr/bin/env python3.2
"""
Bibliothek und Programm für Mickey-Mouse-Fraktale

Bei Aufruf als Programm wird eine Postscript-Datei mit Mickey-Mouse-Fraktal
generiert.

Parameter:
    1. Größe (Detailliertheit) des Fraktals
    2. Name der Postscript-Datei

"""

import sys
import number
from ps_functions import *

def draw_mm_fractal(size, filename):
    """
    Schreibt ein Mickey-Mouse-Fraktal in eine Postscript-Datei

    Parameter:
        size ... "Größe" des Bildes. Da wir es mit Vektorgrafiken zu tun
                 haben, bestimmt der Parameter hauptsächlich die
                 Rekusionstiefe und damit die Detailliertheit des Bildes.
        filename
             ... Name der Datei, in die geschrieben werden soll
    Rückgabe: Nüschts

    """

    # Dumme Eingaben abfangen
    if not number.is_natural(size):
        raise Exception("Bildgröße muss eine natürliche Zahl sein.")
    if not isinstance(filename, str):
        raise Exception("Dateiname muss ein String sein.")

    # Größe der kleinsten Kreise an Bildgröße anpassen
    resolution = 610 / size

    def rec_circles(x_0, y_0, size):
        """
        Schreibt rekursiv die Befehle für die Kreise des Fraktals

        Parameter:
            x_0, y_0 ... Koordinaten des linken unteren Punktes des Feldes für
                         die aktuelle Rekursion
            size     ... größe des Feldes für die aktuelle Rekursion

        Die Funktion schreibt einen Kreis in jeden Quadranten des aktuellen
        Bildfeldes und ruft sich dann für jeden Quadranten rekursiv auf.

        """

        # Größe der Felder für nächsttiefere Rekursionsebene
        half_size = size / 2

        if size > resolution:
            # Kreis in die linke untere Ecke und rekursiv kleine Kreise
            fillCircle( x_0 +     size, y_0 +     size, size)
            rec_circles(x_0,            y_0,            half_size)

            # Kreis in die rechte untere Ecke und rekursiv kleine Kreise
            fillCircle( x_0 + 3 * size, y_0 +     size, size)
            rec_circles(x_0 + 2 * size, y_0,             half_size)

            # Kreis in die linke obere Ecke und rekursiv kleine Kreise
            fillCircle( x_0 +     size, y_0 + 3 * size, size)
            rec_circles(x_0,            y_0 + 2 * size, half_size)

            # Kreis in die rechte obere Ecke und rekursiv kleine Kreise
            fillCircle( x_0 + 3 * size, y_0 + 3 * size, size)
            rec_circles(x_0 + 2 * size, y_0 + 2 * size, half_size)
        else:
            return


    # Header schreiben
    begin(filename, size, size)

    # Schwarz als Farbe für überall definieren
    setColor(0, 0, 0)

    # großen schwarzen Klecks in die Mitte
    half_size = size / 2
    fillCircle(half_size, half_size, half_size)

    # kleine Kreise rekursiv
    rec_circles(0, 0, size / 2)

    # PS-Datei abschließen
    end()

    return


# Bei Ausführung als Programm PS-Datei schreiben
if __name__ == "__main__":
    draw_mm_fractal(int(sys.argv[1]), sys.argv[2])
