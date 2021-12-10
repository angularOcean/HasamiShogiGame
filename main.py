#Hasami Shogi Board Game by Herakles Li

import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Hasami Shogi")
icon = pygame.image.load('shogi_icon.jpg')
pygame.display.set_icon(icon)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RBG fill for white screen background
    screen.fill((255,255,255))
    pygame.display.update()