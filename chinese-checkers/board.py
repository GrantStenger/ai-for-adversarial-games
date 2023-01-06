from utils import my_print
import random


class Board:
    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 0]
        ]

    def show(self):
        # Clear board before showing
        print("\033[H\033[J")

        # Print the board to the console
        i = 9
        for row in self.board:
            print(" " * i, end=" ")
            i -= 1
            for cell in row:
                print(cell, end="   ")
            print("\n")

    def move(self, start, end, player_id):
        # Check if the move is valid
        if not self.is_valid_move(start, end, player_id):
            raise Exception("Invalid move")

        # Move the piece
        start_row, start_col = start
        end_row, end_col = end
        self.board[start_row][start_col] = 0
        self.board[end_row][end_col] = player_id

    def is_valid_move(self, start, end, player_id):
        start_row, start_col = start
        end_row, end_col = end

        # Check if the piece to be moved is the player's piece
        if self.board[start_row][start_col] != player_id:
            my_print("You can't move a piece that isn't yours")
            return False

        # Check if the piece is moving to an occupied cell
        if self.board[end_row][end_col] != 0:
            my_print("You can't move to an occupied cell")
            return False

        # Check if the piece is moving out of bounds
        if start_row < 0 or start_row > 8 or start_col < 0 or start_col > 8 or end_row < 0 or end_row > 8 or end_col < 0 or end_col > 8:
            my_print("You can't move out of bounds")
            return False

        # Check if the piece is not moving at all
        if start_row == end_row and start_col == end_col:
            my_print("You didn't move the piece")
            return False

        # Check valid single step moves
        if start_row - 1 == end_row and start_col - 1 == end_col:
            return True
        if start_row - 1 == end_row and start_col == end_col:
            return True
        if start_row == end_row and start_col - 1 == end_col:
            return True
        if start_row == end_row and start_col + 1 == end_col:
            return True
        if start_row + 1 == end_row and start_col == end_col:
            return True
        if start_row + 1 == end_row and start_col + 1 == end_col:
            return True

        # Check valid jumping moves
        if start_row - 2 == end_row and start_col - 2 == end_col:
            if self.board[start_row - 1][start_col - 1] != 0:
                return True
        if start_row - 2 == end_row and start_col == end_col:
            if self.board[start_row - 1][start_col] != 0:
                return True
        if start_row == end_row and start_col - 2 == end_col:
            if self.board[start_row][start_col - 1] != 0:
                return True
        if start_row == end_row and start_col + 2 == end_col:
            if self.board[start_row][start_col + 1] != 0:
                return True
        if start_row + 2 == end_row and start_col == end_col:
            if self.board[start_row + 1][start_col] != 0:
                return True
        if start_row + 2 == end_row and start_col + 2 == end_col:
            if self.board[start_row + 1][start_col + 1] != 0:
                return True

        return False

    # Get all valid moves for a player
    def get_valid_moves(self):
        valid_moves = []
        # A 4x nested loop is normally horrible but 8281 computations is not that bad
        for row in range(9):
            for col in range(9):
                for row2 in range(9):
                    for col2 in range(9):
                        if self.is_valid_move((row, col), (row2, col2), 2):
                            valid_moves.append(((row, col), (row2, col2)))

        return valid_moves

    # A player wins if they get all of their pieces to the opposite corner of the board
    def check_win(self):
        # Check if player 1 has won
        player_1_promoted_pieces = 0
        for row in range(5):
            for col in range(5+row, 9):
                # print(row, col)
                if self.board[row][col] == 1:
                    player_1_promoted_pieces += 1
        if player_1_promoted_pieces == 10:
            return 1

        # Check if player 2 has won
        player_2_promoted_pieces = 0
        for row in range(4, 9):
            for col in range(row-4):
                if self.board[row][col] == 2:
                    player_2_promoted_pieces += 1
        if player_2_promoted_pieces == 10:
            return 2

        return 0
