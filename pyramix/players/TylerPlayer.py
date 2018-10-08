from players.BasePlayer import BasePlayer


class TylerPlayer(BasePlayer):
    """ Represents a computer player.

        Attributes:
            score: An integer representing the Player's current score.
            blocks_taken: A list of Blocks which belong to the Player.
    """

    def __init__(self):
        """ Initializes a TylerPlayer.
        """

        # Initializes a Player
        super().__init__()

    def evaluate_moves(self, legal_moves):
        """ Calculates and selects the optimal move.

            Args:
                legal_moves: A list of legal moves.

            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # Returns dummy values
        return 0, 0
