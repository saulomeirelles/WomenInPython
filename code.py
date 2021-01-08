# CircuitPython demo - NeoPixel
from time import sleep
import board
import neopixel
from math import ceil
from random import randrange

pixel_pin  = board.NEOPIXEL
num_pixels = 64
num_row    = 8
num_col    = 8

RED    = (255, 0, 0)
ORANGE = (255,50,0)
YELLOW = (255, 200, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
PURPLE = (50,0,50)
VIOLET = (148,0,211)
BLACK  = (0, 0, 0)

rainbow_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, VIOLET]

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        sleep(wait)
        pixels.show()
    sleep(0.5)

def clear():
    pixels.fill(BLACK)
    pixels.show()

def anima_square(ndelrowcol=3, color1=RED, color2=RED):
    for col in range(ndelrowcol, num_col - ndelrowcol ):
        if ndelrowcol % 2 == 0:
            for ind in range( int(ndelrowcol/2), num_row/2 - int(ndelrowcol/2) ):
                pixels[ (2*num_row)*ind+col ]                         = color1
            for ind in range( int(ndelrowcol/2), num_row/2 - int(ndelrowcol/2) ):
                pixels[ ( (2*num_row)*ind-1 ) + ( (2*num_row)-col ) ] = color2
        else:
            for ind in range( ceil(ndelrowcol/2) , num_row/2 - (ceil(ndelrowcol/2) - 1) ):
                pixels[ (2*num_row)*ind+col ]                         = color1
            for ind in range( (ceil(ndelrowcol/2) - 1) , num_row/2 - ceil(ndelrowcol/2) ):
                pixels[ ( (2*num_row)*ind-1 ) + ( (2*num_row)-col ) ] = color2

    pixels.show()

def col_sel(col,color1=RED,color2=None):
    if not color2:
        color2=color1
    for ind in range( num_row/2 ):
        pixels[  (2*num_row)*ind+col ]                        = color1
        pixels[ ( (2*num_row)*ind-1 ) + ( (2*num_row)-col ) ] = color2
    # pixels.show()

def lin_sel(line,color1=RED,color2=None):
    if not color2:
        color2=color1
    for ind in range( num_row ):
        if ind % 2 == 0:
            pixels[  ind + (num_row)*line ] = color1
        else:
            pixels[  ind + (num_row)*line ] = color2
    # pixels.show()


while True:

    for i in range(0,7):
        lin_sel(i,color1=rainbow_colors[i])
    pixels.show()
    clear()
    for i in range(0,7):
        col_sel(i,color1=rainbow_colors[i])
    pixels.show()
    clear()

    # for i in range(num_col/2):
    #     anima_square(i,
    #          color1=rainbow_colors[randrange(6)],
    #          color2=rainbow_colors[randrange(6)] )
    #     clear()
    #
    # for i in range(num_col):
    #     lin_sel(i,
    #         color1=rainbow_colors[randrange(6)],
    #         color2=rainbow_colors[randrange(6)] )
    #     clear()
    #     col_sel(i,
    #         color1=rainbow_colors[randrange(6)],
    #         color2=rainbow_colors[randrange(6)] )
    #     clear()
