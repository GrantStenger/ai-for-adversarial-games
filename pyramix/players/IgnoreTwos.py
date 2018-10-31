from players.OptColorGreedy import OptColorGreedy


class IgnoreTwos(OptColorGreedy):
    """ Represents an OptColorGreedy player who ignores two-point blocks.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors & the number of 1-point blocks the Player has.
    """

    def __init__(self):
        """ Initializes an IgnoreTwos player.
        """

        # Initializes an OptColorGreedy player
        super().__init__()

    def evaluate_moves(self, board, legal_moves, players):
        """ If there exists a 3-point block, choose it; otherwise, select a 1-point block of optimal color.

            Args:
                board: A nested array of Blocks.
                legal_moves: A list of legal moves.
                players: A list of players.
            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # Gets all the values of the legal moves
        values = [board[move[0]][move[1]].value for move in legal_moves]

        # If there are high-value blocks available, play greedily
        if max(values) == 3:
            return super(OptColorGreedy, self).evaluate_moves(board, legal_moves, players)
        # If there are only 1-point blocks, select an optimal color
        else:
            return super().selectOptimalColorByDistance(board, legal_moves, players)

