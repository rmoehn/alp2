# Version 1.2 (ALP II Team)

"""
	This script creates a window on your screen and visualizes your mosaics.

	Please, don't manipulate this code. It's really not necessary to change
	anything.

	You also don't need to understand all the details of the functions
	on this script to write your solutions.

	If you want to place more than six mosaics on your window you just need
	to add more calls of the 'create_mosaic' function in the main function,
	each one with a new name of your 'decide_color' function.

	Please ask your tutor in your exercise session if you want to learn
	more detail about this script.
"""

from tkinter import Tk, Canvas
import color_functions
from math import sqrt

def create_mosaic(graphic, stone_size, decide_color):
	"""Paints a mosaic in the graphic object using the 'decide_color' function.
           Each piece has the same 'stone_size'."""
	size = int(graphic.cget("height"))
	s = size//stone_size #number of rows, which is equal to the number of columns

	# for each (row, col) position the decide_color function is called
	for row in range(s):
		for col in range(s):
			# calculates the coordinates of the current stone
			x1 = stone_size * row
			y1 = stone_size * col
			x2 = x1 + stone_size
			y2 = y1 + stone_size
			# gets the color of the current stone
			color = decide_color(row, col, s)
			# paints the current stone on the given position
			graphic.create_rectangle(x1, y1, x2, y2, fill = color, outline="")

	# makes the graphic visible
	graphic.pack()

def create_graphic(size):
	"""Creates the graphic object in which the mosaic is painted"""
	return Canvas(root, width = size, height = size)

def main():

	# size of the whole picture and size of each stone of the picture
	size = 160
	stone_size = 1

	# creates a window for the mosaics
	global root
	root = Tk()
	root.title("Mosaics")

	# first mosaic
	pic_one = create_graphic(size)
	create_mosaic(pic_one, stone_size, color_functions.decide_color_rects)
	# sets the position of the first mosaic in the window
	pic_one.grid(row = 0, column = 0)

	# second mosaic
	pic_two = Canvas(root, width = size, height = size)
	create_mosaic(pic_two, stone_size, color_functions.decide_color_circle)
	pic_two.grid(row = 0, column = 1)

	# third mosaic
	pic_three = Canvas(root, width = size, height = size)
	create_mosaic(pic_three, stone_size, color_functions.decide_color_squares)
	pic_three.grid(row = 0, column = 2)

	# fourth mosaic
	pic_three = Canvas(root, width = size, height = size)
	create_mosaic(pic_three, stone_size, color_functions.decide_color_illusion)
	pic_three.grid(row = 1, column = 0)

	# fifth mosaic
	pic_three = Canvas(root, width = size, height = size)
	create_mosaic(pic_three, stone_size, color_functions.decide_color_illusion2)
	pic_three.grid(row = 1, column = 1)

	# own mosaic 1
	pic_own = Canvas(root, width = size, height = size)
	create_mosaic(pic_own, stone_size, color_functions.decide_color_own1)
	pic_own.grid(row = 1, column = 2)

	# own mosaic 2
	pic_own = Canvas(root, width = size, height = size)
	create_mosaic(pic_own, stone_size, color_functions.decide_color_own2)
	pic_own.grid(row = 2, column = 0)

	# shows the picture permanently
	root.mainloop()

main()


