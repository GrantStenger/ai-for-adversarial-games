from board import Board
from utils import my_print
import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id

    @abstractmethod
    def make_turn(self, board):
        pass


class HumanPlayer(Player):
    def make_turn(self, board):
        # While loop allows the player to make infinite errors inputting their move (until proper move is executed)
        while True:
            try:
                start = tuple(
                    map(int, input("Which piece would you like to move (row, col): ").replace('(', '').replace(')', '') .split(",")))
                end = tuple(map(int, input(
                    "Where would you like to move this piece (row,col): ").replace('(', '').replace(')', '') .split(",")))
                board.move(start, end, player_id=1)
                while board.is_jumping:
                    board.show()
                    jump_location = input(
                        "Where would you like to jump (row,col) or \"end\": ")
                    if jump_location == "end":
                        board.end_turn()
                        break
                    jump_location = tuple(map(int, jump_location.replace(
                        '(', '').replace(')', '') .split(",")))
                    board.move(end, jump_location, player_id=1)
                    end = jump_location
                break
            except Exception as e:
                print(e)


class ComputerPlayer(Player):
    def select_best_move(self, board, valid_moves):
        pass

    def make_turn(self, board):
        valid_moves = board.get_valid_moves(player_id=2)

        if len(valid_moves) > 0:
            start, end = self.select_best_move(board, valid_moves)
            board.move(start, end, player_id=2)
        else:
            my_print("No valid moves")


class BeginnerComputerPlayer(ComputerPlayer):
    def select_best_move(self, board, valid_moves):
        return random.choice(valid_moves)


class IntermediateComputerPlayer(ComputerPlayer):
    def select_best_move(self, board, valid_moves):

        # Select the move that results in a board configuration with pieces closest to the goal corner
        move_scores = {}
        for move in valid_moves:
            start, end = move
            board_copy = board.copy()
            print("start", start)
            print("end", end)
            board_copy.show()
            board_copy.move(start, end, player_id=2)
            move_scores[move] = self.get_score(board_copy)

        return max(move_scores, key=move_scores.get)

    def get_score(self, board):
        score = 0
        for row in range(9):
            for col in range(9):
                if board.board[row][col] == 2:
                    score += 8 - col + row
        return score


class ExpertComputerPlayer(ComputerPlayer):
    def select_best_move(self, board, valid_moves):
        return random.choice(valid_moves)
