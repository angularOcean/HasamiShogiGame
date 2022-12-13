# Hasami Shogi Game
This repository is for a terminal based version of the board game Hasami Shogi coded using Python.

# Game Synopsis
Hasami Shogi is a variant of traditional Shogi which is a Japanese chess-like game and is itself made up of two main variants, Variant 1 and Variant 2.

This version of the game employs Variant 1's rules.

# Gameplay
Gameplay involves a single type of game piece which can move any number of squares vertically or horizontally on the board similar to a rook piece in chess.

Players take turns moving a piece in an attempt to capture their opponents pieces.

Pieces are captured by 'sandwiching' the opponents piece or pieces between two of their own pieces either vertically or horizontally in neighboring board spaces.

Corner pieces can also be captured by a player placing two of their pieces on the board tiles orthogonally adjacent to the corner piece.

Multiple pieces can be captured in one sandwich as long as all the board spaces between the players two capturing pieces are filled with the opponents pieces.

A player wins when they have captured all or all but one of the opponents pieces.

More about the game can be read here: https://en.wikipedia.org/wiki/Hasami_shogi

# Running the Game/Getting Started
Download the contents of this repository which contains three files: constants.py, HasamiShogiCode.py, and main.py, into a single folder

The game can be run through the main.py file.

<b>constants.py:</b> Provides set constants for HasamiShogiCode.py and main.py

<b>HasamiShogiCode.py:</b> Contains the codebase for the Hasami Shogi game itself

<b>main.py:</b> Generates a simple graphical user interface of the pieces and Shogi board for the game utilizing pygame.

# Dependencies
This game requires pygame to run. More about pygame can be found at: https://www.pygame.org/wiki/GettingStarted
