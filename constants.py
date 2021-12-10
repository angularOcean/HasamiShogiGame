import pygame

#constants
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
