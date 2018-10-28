from random import randint
import numpy as np

from players.Greedy import Greedy
from players.Random import Random


class HalfGreedy(Greedy, Random):
    """ Represents a half greedy, half random computer player.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors & the number of 1-point blocks the Player has.
    """

    def __init__(self):
        """ Initializes a HalfGreedy player.
        """

        # Initializes a Greedy player
        super().__init__()

    def evaluate_moves(self, board, legal_moves, players):
        """ 50/50 chance to either be greedy or random.

            Args:
                board: A nested array of Blocks.
                legal_moves: A list of legal moves.
                players: A list of players.
            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # 50/50 chance to be greedy or random
        if randint(0, 1):
            return Greedy.evaluate_moves(board, legal_moves, players)
        else:
            return Random.evaluate_moves(board, legal_moves, players)
