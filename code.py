#MawandeNcamani
#I created this plagirism free and in good spirit, have fun
#The programme has no bugs, please copy this original format and run
#2 player tic tac toe

import os
import random

class Grid():
    """This class is the actual visual of the grid"""
    def __init__(self):
        self.board = [i for i in range(10)]
        self._win_combinations = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 5, 9),
            (3, 5, 7),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9)]
        self.game_over = False
#
    def drawGrid(self):
        
        """Draws the grid to the terminal"""
        print("---------")
        print(self.board[7], "|", self.board[8], "|", self.board[9])
        print(self.board[4], "|", self.board[5], "|", self.board[6])
        print(self.board[1], "|", self.board[2], "|", self.board[3])
        print("---------")

    def winnerCheck(self, player):
        """Checks if the move the player just made, made him/her win the game"""
        for a, b, c in self._win_combinations:
            if self.board[a] == self.board[b] == self.board[c]:
                print(f"Winner, player {player} won the game. Keep this up and you'll earn a chance to play the great Mawande!")
                self.game_over = True

    def update(self, input, choice):
        """Update the current board"""
        self.board[input] = choice
        os.system("clear")
        self.drawGrid()
        self.winnerCheck(choice)

    def boardReset(self):
        """a function to reset the board"""
        self.board = [i for i in range(10)]

    def tie(self):
        """Stops the game if tie"""
        list_ = list(filter(lambda x: type(x) != int, self.board))
        return len(list_) == 9


class TicTacToe():
    def __init__(self):
        os.system("clear")
        self.board = Grid()
        self.player_1_char = ""
        self.player_2_char = ""
        self.corret_choice = False
        self.playerChara()

    def reset(self):
        """To declutter the board, a reset function"""
        self.player_1_char = ""
        self.player_2_char = ""
        self.board.reset_board()

    def playerChara(self):
        """Character Choice"""
        while True:
            print ('TIC TAC TOE, Gimme a High, Gimme a Low, Gimme 3 in a row!')
            player_1_char = input("Are you going with the X for X-Men or O for Omnitrix? ")
            print()
            if player_1_char == "X":
                self.player_1_char = "X"
                self.player_2_char = "O"
                print("Starting player selected X")
                break
            elif player_1_char == "O":
                self.player_1_char = "O"
                self.player_2_char = "X"
                print("Starting player selected O")
                break
            else:
                print("Please input a valid X or O")
        os.system("clear")

    def playerInput(self, player_char):
        while True:
            while True:
                x = input(f"{player_char} You're up, select a number to play")
                if x.isdigit():
                    x = int(x)
                    break
                else:
                    print("Please input a valid number! ")

            if x > 0 and x < 10 and type(self.board.board[x]) != str:
                self.board.update(x, player_char)
                break
            elif x == 10:
                quit()
            else: 
                print("Focus, that spot is taken, try again: ")

    def tieCheck(self):
        if self.board.tie():
            self.board.game_over = True
            print("That was pathetic, neither of you are fit to take on the legendary Mawande!")
            return True
        return False

    def run(self):
        self.board.drawGrid()

        while not self.board.game_over:
            self.correct_player_1 = False
            self.correct_player_2 = False

            self.playerInput(self.player_1_char)
            if self.board.game_over:
                break
            if self.tieCheck():
                break

            self.playerInput(self.player_2_char)
            if self.board.game_over:
                break
            if self.tieCheck():
                break


while True:
    TicTacToe().run()

    user_input = "a"
    while user_input not in "ny":
        user_input = input("Play again? (y/n)").lower()

    if user_input == "y":
        continue
    else:
        break
