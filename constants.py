#This file contains constants utilized by the main.py and HasamiShogiCode
# files to set the game files graphical user interface components

import pygame

'''Constants for the game include colors, number of pixels for the screen output,
size of the squares, and size of the game pieces, their outline, and highlight size.'''
fps = 60

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gray = (100, 100, 100)
green = (0, 255, 0)
screenHeight = 810
rows, cols = 9,9
padding = 9
outline = 2
highlight = 6
squareSize = screenHeight/cols

#Set the Window

screen = pygame.display.set_mode((screenHeight,screenHeight)) #screen size
