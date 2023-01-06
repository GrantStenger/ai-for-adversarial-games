from utils import my_print
import random


class Board:
    def __init__(self, board=None):
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

        self.current_player = 1
        self.is_jumping = False

    def show(self):
        # Clear board before showing
        # print("\033[H\033[J")

        # Print the board to the console
        i = 9
        for row in self.board:
            print(" " * i, end=" ")
            i -= 1
            for cell in row:
                print(cell, end="   ")
            print("\n")

    def move(self, start, end, player_id, is_hallucinating=False):
        # Check if the move is valid
        if not self.is_valid_move(start, end, player_id):
            raise Exception("Invalid move")

        # Move the piece
        start_row, start_col = start
        end_row, end_col = end
        self.board[start_row][start_col] = 0
        self.board[end_row][end_col] = player_id

        # Check if the piece is jumping
        if abs(start_row - end_row) > 1 or abs(start_col - end_col) > 1:
            self.is_jumping = True
        else:
            if not is_hallucinating:
                self.end_turn()

    def is_valid_move(self, start, end, player_id):
        start_row, start_col = start
        end_row, end_col = end
        print("here")
        print(self.current_player, player_id)
        # Check if the player id is the current player
        if self.current_player != player_id:
            my_print("It's not your turn")
            return False

        print("here2")
        # Check if the piece to be moved is the player's piece
        if self.board[start_row][start_col] != player_id:
            my_print("You can't move a piece that isn't yours")
            return False
        print("here3")
        # Check if the piece is moving to an occupied cell
        if self.board[end_row][end_col] != 0:
            my_print("You can't move to an occupied cell")
            return False
        print("here4")
        # Check if the piece is moving out of bounds
        if start_row < 0 or start_row > 8 or start_col < 0 or start_col > 8 or end_row < 0 or end_row > 8 or end_col < 0 or end_col > 8:
            my_print("You can't move out of bounds")
            return False
        print("here5")
        # Check if the piece is not moving at all
        if start_row == end_row and start_col == end_col:
            my_print("You didn't move the piece")
            return False
        print("here6")
        # Check valid single step moves
        if self.is_single_step_move(start, end):
            # self.current_player = 1 if self.current_player == 2 else 2
            # self.is_jumping = False
            return True
        print("here7")
        # Check valid jumping moves
        if self.is_jumping_move(start, end):
            # self.is_jumping = True
            return True
        print("here8")
        return False

    def is_single_step_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
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
        return False

    def is_jumping_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
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
    def get_valid_moves(self, player_id):
        valid_moves = []
        # A 4x nested loop is normally horrible but 8281 computations is not that bad
        for row in range(9):
            for col in range(9):
                for row2 in range(9):
                    for col2 in range(9):
                        if self.is_valid_move((row, col), (row2, col2), player_id):
                            valid_moves.append(((row, col), (row2, col2)))
        print("Valid moves: ", valid_moves)
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

    def copy(self):
        new_board = Board()
        for row in range(9):
            for col in range(9):
                new_board.board[row][col] = int(self.board[row][col])
        return new_board

    def get_board(self):
        return self.board

    def get_current_player(self):
        return self.current_player

    def end_turn(self):
        print("ending turn")
        print(self.current_player)
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
        print(self.current_player)
        self.is_jumping = False
