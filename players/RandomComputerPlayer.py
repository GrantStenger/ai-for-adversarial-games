import numpy as np

from players.ComputerPlayer import ComputerPlayer


class RandomComputerPlayer(ComputerPlayer):

    """ Represents a computer player.

        Attributes:
            score: An integer representing the Player's current score.
            blocks_taken: A list of Blocks which belong to the Player.
    """

    def __init__(self):
        """ Initializes a ComputerPlayer.
        """

        # Initializes a ComputerPlayer
        super().__init__()

    def evaluate_moves(self, legal_moves):
        """ Selects a Random Move from the list of legal moves.

            Args:
                legal_moves: A list of legal moves.

            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # Randomly select new position
        ind = np.random.choice(np.arange(len(legal_moves)))
        new_pos = legal_moves[ind]

        # Returns random position
        return new_pos
