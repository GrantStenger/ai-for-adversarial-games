from players.Player import Player


class Computer(Player):
    """ Represents a computer player.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors & the number of 1-point blocks the Player has.
    """

    def __init__(self):
        """ Initializes a Computer.
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
