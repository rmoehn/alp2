# Version 1.2 (ALP II Team)

"""
        You only have to write some code inside the 'decide_color' functions.
        Your decide_color functions calculate a color for each (x,y) position
        and give it back with a return statement.
        The 'six 'decide_color' functions are called in the 'Mosaic_GUI.py'
        script to paint the six mosaics in a window.
        For an easy start we wrote some simple examples.
        Please overwrite them with your own solutions.

        Both files have to be in the same directory and you must run the
        'Mosaic_GUI.py' script to show your mosaics.

        In the following page you can find a table of colors to be used
        in your functions
               'http://tmml.sourceforge.net/doc/tk/colors.html'
"""
from math import sqrt

def decide_color_rects(x, y, size):
        # write your code here
        return "black"

def decide_color_circle(x, y, size):
        # write your code here
        return "red"

def decide_color_squares(x, y, size):
        # write your code here
        return "blue"

def decide_color_illusion(x, y, size):
    sq_size = size // 8    # Kantenlänge der kleinen Quadrate
    ra_size = sq_size // 5 # Breite der kleinen Rechtecke

    """
    Man könnte alle ifs mit ors verbinden, aber dann wird es noch
    unübersichtlicher.

    """

    # Alle senkrechten Linien malen. Die Bedingung ist notwendig,
    # damit nur jeweils an den Kanten der Rechtecke Linien gezeichnet und
    # nicht die Rechtecke ganz ausgemalt werden.
    # (Python erlaubt mir nicht ganz, die Kommentaren so zu formatieren, wie
    # ich das will.)
    if x % ra_size == 0:
        # Senkrechte Linien in den geraden Spalten malen aber, nur in
        # ungeraden Zeilen
        if x % (2 * sq_size) >= sq_size      \
            and y % (2 * sq_size) <  sq_size \
        or x % (2 * sq_size) <  sq_size      \
            and y % (2 * sq_size) >= sq_size:
        # Senkrechte Linien in den ungeraden Spalten malen aber, nur in
        # geraden Zeilen
            return "black"

    # Alle waagerechten Linien malen
    if y % ra_size == 0:
        # Waagerechte Linien in den ungeraden Zeilen malen, aber nur in
        # ungeraden Spalten
        if y % (2 * sq_size) <  sq_size      \
            and x % (2 * sq_size) <  sq_size \
        or y % (2 * sq_size) >= sq_size      \
            and x % (2 * sq_size) >= sq_size:
        # Waagerechte Linien in den geraden Zeilen malen, aber nur in geraden
        # Spalten
            return "black"

    # Weißer Hintergrund, wenn nichts anderes gezeichnet wird
    return "white"

def decide_color_illusion2(x, y, size):
        return "magenta"

def decide_color_own1(x, y, size):
        return "gray"

def decide_color_own2(x, y, size):
        return "gray"

