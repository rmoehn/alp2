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
        """
        Erzeugt einen rosafarbenen Winkel auf schwarzem Hintergrund
        """
        if y<=size/3:
            return "black"
        elif size/3<y<=size/2:
            if x<=(1/3)*size:
                return "black"
            elif size/3<x<=2*size/3:
                return "pink"
            else:
                return "black"
        elif size/2<y<=2*size/3:
            if x<=size/3:
                return "black"
            elif size/3<x<=size/2:
                return "pink"
            else:
                return "black"
        else:
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
        """
        Erzeugt ein schwarzes Flechtmuster auf weißem Hntergrund
        """
        n=(y//20)%2
        if (x//20)%2==n:
            if (y)%4==0:
                return "black"
            else:
                return "white"
        else:
            if (x)%4==0:
                return "black"
            else:
                return "white"

def decide_color_illusion2(x, y, size):
        """
        Erzeugt ein Gitter aus weißen Linien vor schwarzem Hintergrund und ein
        magenta-farbenes Quadrat mittig im Vordergrund:
        """
        # erzeugt Magenta-Quadrat mit Kantenlänge 52 in der Mitte
        if (size/2)-26<=y<=(size/2)+26 and (size/2)-26<=x<=(size/2)+26:
            return "magenta"
        # erzeugt die horizontalen und vertikalen weißen Linien
        elif x%8==0 or x%8==7 or y%8==0 or y%8==7:
            return "white"
        # Hintergrund
        else:
            return "black"
                
def decide_color_own1(x, y, size):
        return "gray"

def decide_color_own2(x, y, size):
        return "gray"

