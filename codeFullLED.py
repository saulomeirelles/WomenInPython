# CircuitPython demo - NeoPixel
from time import sleep
import board
from random import randrange
from matrix_LED_utils import *

import matrix_LED_utils



n = 1
while True:
#     anima_from_gimp("/8x8-" + str(n) + ".data")
# #	sleep(0.25)
#     n += 1
#     if(n == 5):
#         n = 1

    anima_from_gimp("heart.data")
    anima_from_gimp("black.data")


# while True:

#     lin_sel(3-1)
#     lin_sel(6-1)
#     col_sel(3-1)
#     col_sel(6-1)
#     put_pixel(0,0,YELLOW)
#     put_pixel(0,7,VIOLET)
#     put_pixel(7,0,BLUE)
#     put_pixel(7,7,ORANGE)
#     square(6,3,PURPLE,2)
#     pixels.show()

#     anima_square(3,color1=BLUE,color2=BLUE)

    # for i in range(0,7):
    #     lin_sel(i,color1=rainbow_colors[i])
    # pixels.show()
    # clear()
    # for i in range(0,7):
    #     col_sel(i,color1=rainbow_colors[i])
    # pixels.show()
    # clear()

    # for i in range(num_col/2):
    #     anima_square(i,
    #          color1=rainbow_colors[randrange(6)],
    #          color2=rainbow_colors[randrange(6)] )
    #     clear()
    
    # for i in range(num_col):
    #     lin_sel(i,
    #         color1=rainbow_colors[randrange(6)],
    #         color2=rainbow_colors[randrange(6)] )
    #     clear()
    #     col_sel(i,
    #         color1=rainbow_colors[randrange(6)],
    #         color2=rainbow_colors[randrange(6)] )
    #     clear()
