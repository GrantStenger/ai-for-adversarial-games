from board import Board
from utils import my_print
import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self, board):
        pass


class HumanPlayer(Player):
    def move(self, board):
        while True:
            try:
                start = tuple(
                    map(int, input("Which piece would you like to move (row, col): ").replace('(', '').replace(')', '') .split(",")))
                end = tuple(map(int, input(
                    "Where would you like to move this piece (row,col): ").replace('(', '').replace(')', '') .split(",")))
                board.move(start, end, player_id=1)
                break
            except Exception as e:
                print(e)


class ComputerPlayer(Player):
    def move(self, board):
        valid_moves = board.get_valid_moves()
        if len(valid_moves) > 0:
            start, end = random.choice(valid_moves)
            board.move(start, end, player_id=2)
        else:
            my_print("No valid moves")

        return valid_moves
