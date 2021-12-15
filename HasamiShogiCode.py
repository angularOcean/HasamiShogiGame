#This file contains

import pygame
from constants import *


class HasamiShogiGame:
    '''This class represents a game of Hasami Shogi.'''

    def __init__(self):
        '''Initializes the start of the game with a turn tracker, new board,
        game state, red pieces captured, black pieces captured,
        and finally a move dictionary which holds all possible moves a user could make
        the dictionary stores x,y coordinates as values for each string notation as a key'''
        self._active_player = "BLACK"
        self._board = self.new_board()
        self._game_state = "UNFINISHED"
        self._red_cap = 0
        self._black_cap = 0
        self._turn = 0
        self._move_dict = {"a1": (1, 1), "a2": (1, 2), "a3": (1, 3), "a4": (1, 4), "a5": (1, 5), "a6": (1, 6),
                           "a7": (1, 7), "a8": (1, 8), "a9": (1, 9),
                           "b1": (2, 1), "b2": (2, 2), "b3": (2, 3), "b4": (2, 4), "b5": (2, 5), "b6": (2, 6),
                           "b7": (2, 7), "b8": (2, 8), "b9": (2, 9),
                           "c1": (3, 1), "c2": (3, 2), "c3": (3, 3), "c4": (3, 4), "c5": (3, 5), "c6": (3, 6),
                           "c7": (3, 7), "c8": (3, 8), "c9": (3, 9),
                           "d1": (4, 1), "d2": (4, 2), "d3": (4, 3), "d4": (4, 4), "d5": (4, 5), "d6": (4, 6),
                           "d7": (4, 7), "d8": (4, 8), "d9": (4, 9),
                           "e1": (5, 1), "e2": (5, 2), "e3": (5, 3), "e4": (5, 4), "e5": (5, 5), "e6": (5, 6),
                           "e7": (5, 7), "e8": (5, 8), "e9": (5, 9),
                           "f1": (6, 1), "f2": (6, 2), "f3": (6, 3), "f4": (6, 4), "f5": (6, 5), "f6": (6, 6),
                           "f7": (6, 7), "f8": (6, 8), "f9": (6, 9),
                           "g1": (7, 1), "g2": (7, 2), "g3": (7, 3), "g4": (7, 4), "g5": (7, 5), "g6": (7, 6),
                           "g7": (7, 7), "g8": (7, 8), "g9": (7, 9),
                           "h1": (8, 1), "h2": (8, 2), "h3": (8, 3), "h4": (8, 4), "h5": (8, 5), "h6": (8, 6),
                           "h7": (8, 7), "h8": (8, 8), "h9": (8, 9),
                           "i1": (9, 1), "i2": (9, 2), "i3": (9, 3), "i4": (9, 4), "i5": (9, 5), "i6": (9, 6),
                           "i7": (9, 7), "i8": (9, 8), "i9": (9, 9)}
        pass

    def __repr__(self):
        pass

    def get_game_state(self):
        '''Fetches current game state.
        Parameters: None
        Returns: current game state(unfinished, red won, or black won)'''
        return self._game_state

    def get_active_player(self):
        '''Fetches who is current active player color
        Parameters: none
        Returns: whose turn it is (Red or Black player)'''
        return self._active_player

    def get_board(self):
        '''Fetches self._board data member
         Parameters: none
         Returns: self._board'''
        return self._board

    def get_num_captured_pieces(self, color):
        '''Fetches how many pieces have been captured of a color
        Parameters: color (red or black)
        Returns: number of pieces captured of parameter color'''
        if color.lower() == "red":
            return self._red_cap
        if color.lower() == "black":
            return self._black_cap
        else:
            print("Sorry that is not a valid color to check captured pieces for.")
            return False
        pass

    def get_square_occupant(self, coordinates):
        """Fetches the occupant of a square
        Parameters: square (string notation of a square on board)
        Returns: Current occupancy of parameter square (Red, Black, None)"""
        location = self._move_dict.get(coordinates, None)
        if location == None:
            print("Sorry that is not a valid board coordinate")
            return False
        else:
            occupant = self._board[location[0]][location[1]]
            if occupant == ".":
                occupant = 'NONE'
            elif occupant == 'R':
                occupant = "RED"
            elif occupant == "B":
                occupant = 'BLACK'
            return occupant
        pass

    def make_move(self, sqr_start, sqr_end):
        """Attempts to move a shogi piece from start square to end square.
        Will call eval_capture, eval_game methods and modify self._board and self._active_player
        Parameters: sqr_start (string notation of square moved from), sqr_end(string notation of square moved to)
        Returns: boolean (False if move is illegal, true if move was successful"""
        if self.get_game_state() != "UNFINISHED":
            print("Sorry you can't make that move the game is over", self.get_game_state())
            return False

        # grab x,y coordinates of start and end locations
        start_loc = self._move_dict.get(sqr_start, None)
        end_loc = self._move_dict.get(sqr_end, None)

        # check if coordinates are on the board
        if start_loc == None or end_loc == None:
            print("Coordinate(s) do not exist on the board! ")
            return False

        # grab occupancy of start and end coordinate
        start_occ = self.get_square_occupant(sqr_start)
        end_occ = self.get_square_occupant(sqr_end)

        # check if start and end loc are the same
        if start_loc == end_loc:
            print("Start and end location cannot be the same!")
            return False

        # check if start and end loc are at a diagonal
        if start_loc[0] != end_loc[0] and start_loc[1] != end_loc[1]:
            print("Cannot move diagonally!")
            return False

        # check if start is empty OR end square is NOT empty, an illegal move
        if start_occ == 'NONE' or end_occ != 'NONE':
            print("Starting square is empty or end square is not empty!")
            return False

        # check if correct players turn for move
        if start_occ != self._active_player:
            print("Cannot move opponents piece!")
            return False

        move_check = True
        # move vertically and check for pieces in between start and end
        if start_loc[0] != end_loc[0]:
            if start_loc[0] > end_loc[0]:  # moving from larger to smaller coord number
                for square in range(start_loc[0] - 1, end_loc[0] - 1, -1):
                    if self._board[square][start_loc[1]] != '.':
                        move_check = False
            if start_loc[0] < end_loc[0]:  # moving from smaller to larger coord number
                for square in range(start_loc[0] + 1, end_loc[0] + 1):
                    if self._board[square][start_loc[1]] != '.':
                        move_check = False

        # move horizontally and check of pieces in between start and end
        if start_loc[1] != end_loc[1]:
            if start_loc[1] > end_loc[1]:  # moving from larger to smaller coord number
                for square in range(start_loc[1] - 1, end_loc[1] - 1, -1):
                    if self._board[start_loc[0]][square] != '.':
                        move_check = False
            if start_loc[1] < end_loc[1]:  # moving from smaller to larger coord number
                for square in range(start_loc[1] + 1, end_loc[1] + 1):
                    if self._board[start_loc[0]][square] != '.':
                        move_check = False

        # if move is blocked
        if move_check == False:
            print("Move blocked by a piece!")
            return False

        # make the legal move and begin updating game state
        else:
            #print(start_occ, " from ", start_loc, " to ", end_loc)
            if self._board[start_loc[0]][start_loc[1]] == "B":  # moving a black piece
                self._board[end_loc[0]][end_loc[1]] = 'B'
                self._active_player = "RED"
            if self._board[start_loc[0]][start_loc[1]] == "R":  # moving a red piece
                self._board[end_loc[0]][end_loc[1]] = 'R'
                self._active_player = "BLACK"
            self._board[start_loc[0]][start_loc[1]] = "."  # empty start location
            self.eval_capture(sqr_end)  # check for captures
            self.eval_game()  # check status of game
            return True

        # print(start_loc, end_loc)
        # print(start_occ, end_occ)
        pass

    def eval_capture(self, coordinate):
        '''Evaluates if a capture has happened based upon the end position of a moved piece
        Checks North, South, East, and West of the piece for potential captures
        As well as for corner captures in all four corners
        Will check all directions for captures and evaluate each separately
        Updates board and red/black capture data members if any captures occurs
        Parameters: string notation of the coordinates passed by make_move method of ending location of moved piece
        Returns: None'''
        start_loc = self._move_dict[coordinate]

        #set who is active
        if self._board[start_loc[0]][start_loc[1]] == "R":
            active_player = "R"
            captured_player = "B"
        else:
            active_player = "B"
            captured_player = "R"

        # evaluate above piece: [0]-1 location
        above_list = []
        if start_loc[0] > 2:
            above_loc = start_loc[0] - 1
            while self._board[above_loc][start_loc[1]] == captured_player and above_loc > 1:
                above_list.append(above_loc)
                above_loc -=1
            if self._board[above_loc][start_loc[1]] == active_player:
                for element in above_list:
                    self._board[element][start_loc[1]] = "."
                    if active_player == "R":
                        self._black_cap +=1
                    else:
                        self._red_cap +=1

        # evaluate below piece: [0]+1 location
        below_list = []
        if start_loc[0] < 8:
            below_loc = start_loc[0] + 1
            while self._board[below_loc][start_loc[1]] == captured_player and below_loc < 9:
                below_list.append(below_loc)
                below_loc +=1
            if self._board[below_loc][start_loc[1]] == active_player:
                for element in below_list:
                    self._board[element][start_loc[1]] = "."
                    if active_player == "R":
                        self._black_cap +=1
                    else:
                        self._red_cap +=1

        # evaluate left of piece: [1]-1 location
        left_list = []
        if start_loc[1] > 2:
            left_loc = start_loc[1] - 1
            while self._board[start_loc[0]][left_loc] == captured_player and left_loc > 1:
                left_list.append(left_loc)
                left_loc -=1
            if self._board[start_loc[0]][left_loc] == active_player:
                for element in left_list:
                    self._board[start_loc[0]][element] = "."
                    if active_player == "R":
                        self._black_cap +=1
                    else:
                        self._red_cap +=1

        # evaluate right of piece: [1]+1 location
        right_list = []
        if start_loc[1] < 8:
            right_loc = start_loc[1] + 1
            while self._board[start_loc[0]][right_loc] == captured_player and right_loc < 9:
                right_list.append(right_loc)
                right_loc +=1
            if self._board[start_loc[0]][right_loc] == active_player:
                for element in right_list:
                    self._board[start_loc[0]][element] = "."
                    if active_player == "R":
                        self._black_cap +=1
                    else:
                        self._red_cap +=1

        #evaluate corner captures
        if active_player == "B":
            orthogonal = "BLACK"
            corner = "RED"
        else:
            orthogonal = "RED"
            corner = "BLACK"

        # top left: b1, a2 capture a1
        if coordinate == "b1" or coordinate == "a2":
            if self.get_square_occupant("b1") == orthogonal and self.get_square_occupant("a2") == orthogonal:
                if self.get_square_occupant("a1") == corner:
                    self._board[1][1] = "."
                    if active_player == "R":
                        self._black_cap +=1
                    if active_player == "B":
                        self._red_cap +=1

        #top right: b9, a8, capture a9
        if coordinate == "b9" or coordinate == "a8":
            if self.get_square_occupant("b9") == orthogonal and self.get_square_occupant("a8") == orthogonal:
                if self.get_square_occupant("a9") == corner:
                    self._board[1][9] = "."
                    if active_player == "R":
                        self._black_cap +=1
                    if active_player == "B":
                        self._red_cap +=1

        #bottom left: h1, i2 capture i1
        if coordinate == "h1" or coordinate == "i2":
            if self.get_square_occupant("h1") == orthogonal and self.get_square_occupant("i2") == orthogonal:
                if self.get_square_occupant("i1") == corner:
                    self._board[9][1] = "."
                    if active_player == "R":
                        self._black_cap +=1
                    if active_player == "B":
                        self._red_cap +=1


        #bottom right: i8, h9 capture i9
        if coordinate == "i8" or coordinate == "h9":
            if self.get_square_occupant("i8") == orthogonal and self.get_square_occupant("h9") == orthogonal:
                if self.get_square_occupant("i9") == corner:
                    self._board[9][9] = "."
                    if active_player == "R":
                        self._black_cap +=1
                    if active_player == "B":
                        self._red_cap +=1

    def eval_game(self):
        '''Evaluates the game state after a move to determine if game has been won or is unfinished.
        Updates self._game_state if self._black_cap or self._red_cap captures equal or exceed 8
        Which indicates the opponent captured enough pieces to win.
        Parameters: None
        Returns: None'''
        if self._black_cap >= 8:
            self._game_state = "RED_WON"
            print("RED WON!")
        elif self._red_cap >= 8:
            self._game_state = "BLACK_WON"
            print("BLACK WON!")
        pass

    def new_board(self):
        '''Generates a new shogi board when initializing the self._board data member
        Used only for a new instance of the Hasami Shogi class.
        Parameters: None
        Returns: a list of lists representing the board game layout'''
        board_list = []
        first_row = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        alpha_row = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        board_list.append(first_row)
        for letter in alpha_row:
            new_row = []
            new_row.append(letter)
            if letter == "a":
                for val in range(0, 9):
                    new_row.append("R")
            elif letter == "i":
                for val in range(0, 9):
                    new_row.append("B")
            else:
                for val in range(0, 9):
                    new_row.append(".")
            board_list.append(new_row)
        return board_list

    def print_board(self):
        '''Prints the board
        Parameters: None
        Returns: None
        Prints: A printout of the shogi board using the self._board data member.
        Prints each row one at a time in order to create the board in a readable format'''
        for row in range(len(self._board)):
            string_row = ""
            for col in range(len(self._board)):
                string_row += str(self._board[row][col])
                string_row += " "
            print(string_row)

    def draw_grid(self):
        gridSize = int(screenHeight / 9)
        for x in range(0, int(screenHeight), gridSize):
            for y in range(0, int(screenHeight), gridSize):
                rect = pygame.Rect(x, y, gridSize, gridSize)
                pygame.draw.rect(screen, black, rect, 1)

    def draw_pieces(self, surface, squareSize):
        def draw(surface, color, x, y):
            radius = squareSize//2 - padding
            center= squareSize//2
            centerX = center + squareSize*(x-1)
            centerY = center + squareSize*(y-1)
            pygame.draw.circle(surface, gray, (centerX, centerY), radius + outline)
            pygame.draw.circle(surface, color, (centerX, centerY), radius)
        for col in range(1, 10):
            for row in range(1, 10):
                if self._board[col][row] == 'R':
                    draw(surface,red, row, col)
                if self._board[col][row] == 'B':
                    draw(surface,black, row, col)

    def highlight_piece(self, coordinate, surface, squareSize):
        location = self._move_dict[coordinate]
        radius = squareSize // 2 - padding
        center = squareSize // 2
        centerX = center + squareSize * (location[1] - 1)
        centerY = center + squareSize * (location[0] - 1)
        pygame.draw.circle(surface, green, (centerX, centerY), radius + highlight)

    def __repr__(self):
        return self.print_board()



