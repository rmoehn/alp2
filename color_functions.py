# Version 1.2 (ALP II Team)

"""
    blabla
"""
from math import sqrt
import random
random.seed()

def decide_color_rects(x, y, size):
    bigsq_size = size // 3       # Seitenlänge des Quadrates in der Mitte
    smlsq_size = bigsq_size // 2 # Seitenlänge des kleine schwarzen Quadrats

    # Ganz großes schwarzes Quadrat in die untere rechte Ecke setzen
    if bigsq_size + smlsq_size <= x \
        and bigsq_size + smlsq_size <= y:
        return "black"

    # Großes rosanes Quadrat darunter in die Mitte setzen
    if bigsq_size <= x < 2 * bigsq_size \
        and bigsq_size <= y < 2 * bigsq_size:
        return "pink"

    # Rest schwarz
    return "black"

def decide_color_circle(x, y, size):
        """
        Erzeugt einen senkrecht in einen roten und schwarzen Halbkreis
        aufgeteilten Kreis vor einem waagerecht geteilten Hintergrund, welcher
        oben Weiß und unten Grau gefärbt ist.
        """
        # Quadrant links oben
        if y<=(size/2) and x<=(size/2):
            if (size/3)**2>=((x-size/2)**2+(y-size/2)**2):
                return "red"
            else:
                return "white"
        # Quadrant links unten
        if y>(size/2) and x<=(size/2):
            if (size/3)**2>=((x-size/2)**2+(y-size/2)**2):
                return "red"
            else:
                return "gray"
        # Quadrant rechts unten
        if y>(size/2) and x>(size/2):
            if (size/3)**2>=((x-size/2)**2+(y-size/2)**2):
                return "black"
            else:
                return "gray"
        # Quadrant rechts oben
        if y<=(size/2) and x>(size/2):
            if (size/3)**2>=((x-size/2)**2+(y-size/2)**2):
                return "black"
            else:
                return "white"

def decide_color_squares(x, y, size):
        """
        Erzeugt weiße Quadrate mit Mittelpunkt (size/2 / size/2) mit Strich-
        stärke 2 im Abstand von 2 auf blauem Hintergrund
        """
        # Dreieck unten und oben mit waagerechten Linien
        if y>x and y>-x+size or y<x and y<-x+size:
            # weiß, wenn y oder y+1 durch teilbar
            if y%4==0 or y%4==1:
                return "white"
            else:
                return "blue"
        # Dreieck links und rechts mit senkrechten Linien
        else:
            if x%4==0 or x%4==1:
                return "white"
            else:
                return "blue"

def decide_color_illusion(x, y, size):
    sq_size = size // 8    # Kantenlänge der kleinen Quadrate
    ra_size = sq_size // 5 # Breite der kleinen Rechtecke

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
    bigsq_size = size // 3        # Seitenlänge des dicken lilanen Quadrates
    smlsq_size = size // 20       # Seitenlänge der kleinen Quadrate
                                  # einschließlich der Linie links und unten
    line_width = smlsq_size // 4  # Breite der weißen Linien

    # Dickes lilanes Quadrat in der Mitte zeichnen
    if bigsq_size <= x < 2 * bigsq_size \
        and bigsq_size <= y < 2 * bigsq_size:
        return "magenta"

    # Gitter der weißen Linien zeichnen
    if x % smlsq_size < line_width \
        or y % smlsq_size < line_width:
        return "white"

    # Rest schwarz
    return "black"

def decide_color_own1(x, y, size):
    return random.choice(["gray", "gray", "gray", "gray", "gray", "gray",
            "gray", "gray", "gray", "gray", "gray", "gray", "white"])

def decide_color_own2(x, y, size):
    return random.choice(["black", "black", "red", "red", "red", "green"])
