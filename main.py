#Hasami Shogi Board Game by Herakles Li

import pygame
from pygame.locals import (MOUSEBUTTONUP, K_ESCAPE, KEYDOWN)
from constants import *
from HasamiShogiCode import *

#Initialize the pygame
pygame.init()

#generate game
new_game = HasamiShogiGame()

#Title, Screen, and Icon
pygame.display.set_caption("Hasami Shogi") #Window caption
icon = pygame.image.load("shogi_icon.jpg")
pygame.display.set_icon(icon)  #icon
game_font = pygame.font.Font('freesansbold.ttf', 32)

#Text to display
fontObj = pygame.font.Font("freesansbold.ttf", 32)
textSurfaceObj = fontObj.render("Hasami Shogi", True, black)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (screenHeight/2, screenHeight/10)

#deal with mouse movement
def get_row_col_mouse(pos):
    x, y = pos
    row = int(y//squareSize)
    col = int(x//squareSize)
    alphaList = ["a", "b", "c", "d", "e","f", "g", "h", "i"]
    numList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    coordinateString = alphaList[row] + numList[col]
    return coordinateString

#Draw Window
def draw_window1(pos):
    screen.fill(white)
    new_game.draw_grid()
    new_game.highlight_piece(get_row_col_mouse(pos), screen, squareSize)
    new_game.draw_pieces(screen, squareSize)
    pygame.display.update()

def draw_window2():
    screen.fill(white)
    new_game.draw_grid()
    new_game.draw_pieces(screen, squareSize)
    pygame.display.update()

#Game Loop
def main():
    running = True
    finished = False
    firstClick = False
    clickSaver = None
    while running:
        clock = pygame.time.Clock()
        clock.tick(fps)
        for event in pygame.event.get():
            #if hit escape, quit the game
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False

            #track mouse movement and mouse left click
            if event.type == MOUSEBUTTONUP:
                pos1 = pygame.mouse.get_pos()

                if firstClick == True:
                    new_game.make_move(get_row_col_mouse(clickSaver), get_row_col_mouse(pos1))
                    firstClick = False
                    clickSaver = None

                elif firstClick == False:
                    if new_game.get_square_occupant(get_row_col_mouse(pos1)) != 'NONE':
                        if new_game.get_square_occupant(get_row_col_mouse(pos1)) == new_game.get_active_player():
                            firstClick = True
                            clickSaver = pos1

            if firstClick == True:
                draw_window1(clickSaver)
            else:
                draw_window2()

        if new_game.get_game_state() != "UNFINISHED":
            running = False
            finished = True

    while finished:
        printWinner = None
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                finished = False
        if new_game.get_game_state() == "RED_WON":
            printWinner = "Red Won!"
        else:
            printWinner = "Black Won!"
        label = game_font.render('Game is over: '+ printWinner, 1, black)
        screen.blit(label, (screenHeight / 4, screenHeight / 2))
        pygame.display.update()

if __name__ == '__main__':
    main()