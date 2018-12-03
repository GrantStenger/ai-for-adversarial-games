import sys
sys.path.append('..')
from DQN import DQN
import numpy as np
import random

from players.Computer import Computer


class Neural(Computer):
    """ Represents a Neural player with DQN.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors & the number of 1-point blocks the Player has.
    """

    def __init__(self, dqn):
        """ Initializes a Neural player.
        """

        # Initializes a Player
        super().__init__()

        # Initializes a DQN
        self.dqn = dqn

    def evaluate_moves(self, board, legal_moves, players):
        """ Calculates and selects the optimal move.

            Args:
                board: A nested array of Blocks.
                legal_moves: A list of legal moves.
                players: A list of players.
            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        matrix = self.export_matrix_for_cnn(board)

        tensor = self.dqn.game_matrix_to_tensor(matrix)
        inference = self.dqn.forward(tensor)
        inference = inference.detach().numpy()

        index = np.argmax(inference)

        depth = len(board[0])
        row = int(index / depth)
        move = (row, index % (row + 1))

        if move in legal_moves:
            return move
        else:
            return legal_moves[random.randint(0, len(legal_moves))]

    def export_matrix_for_cnn(self, board):
        depth = len(board[0])
        colors = list(self.bonuses_taken_per_color.keys())

        matrix = np.zeros((3 * len(colors), depth, depth), dtype=np.int) 

        for i in range(len(board)):
            for j in range(len(board[i])):
                block = board[i][j]
                if block.color != "0":
                    matrix[3 * colors.index(block.color) + block.value - 1][i][j] = 1

        return matrix

