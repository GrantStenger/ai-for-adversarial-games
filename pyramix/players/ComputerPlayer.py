from players.BasePlayer import BasePlayer


class ComputerPlayer(BasePlayer):
    """ Represents a computer player.

        Attributes:
            score: An integer representing the Player's current score.
            blocks_taken: A list of Blocks which belong to the Player.
    """

    def __init__(self):
        """ Initializes a ComputerPlayer.
        """

        # Initializes a Player
        super().__init__()

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

        # Returns dummy values
        return 0, 0
