import numpy as np

from players.Computer import Computer


class Random(Computer):
    """ Represents a random computer player.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors & the number of 1-point blocks the Player has.
    """

    def __init__(self):
        """ Initializes a Random player.
        """

        # Initializes a Computer
        super().__init__()

    def evaluate_moves(self, board, legal_moves, players):
        """ Selects a random move from the list of legal moves.

            Args:
                board: A nested array of Blocks.
                legal_moves: A list of legal moves.
                players: A list of players.
            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # Randomly select new position
        ind = np.random.choice(np.arange(len(legal_moves)))
        new_pos = legal_moves[ind]

        # Returns random position
        return new_pos
