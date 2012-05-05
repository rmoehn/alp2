"""
    3.Übungsblatt
    Beispielprogramm für die 4.Aufgabe des 3.Übungsblattes
"""

from ps_functions import *

def red_circle(x,y,radius,filename):
    begin(filename, 400, 400)
    setColor(100,0,0)
    fillCircle(x,y,radius)
    end()
    
def chessboard(size,filename):
    stone = size//8
    begin(filename, size, size)
    setColor(10,10,10)
    color = True
    for i in range(0,8):
        for j in range(0,8):
            if (i+j)%2:
                setColor(10,10,10)
            else:
                setColor(200,0,200)
            color = not color
            fillSquare(i*stone,j*stone,stone)
    end()

    
def test_funktions():
    red_circle(200,200,100,"red_circle.ps")
    chessboard(200,"chessboard.ps")

test_funktions()
