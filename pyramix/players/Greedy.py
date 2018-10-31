from players.Computer import Computer


class Greedy(Computer):
    """ Represents a greedy computer player.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors & the number of 1-point blocks the Player has.
    """

    def __init__(self):
        """ Initializes a Greedy player.
        """

        # Initializes a Computer
        super().__init__()

    def evaluate_moves(self, board, legal_moves, players):
        """ Selects the highest points move from the list of legal moves.

            Args:
                board: A nested array of Blocks.
                legal_moves: A list of legal moves.
                players: A list of players.
            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # Find the move with highest value
        values = [board[move[0]][move[1]].value for move in legal_moves]
        best_move = [move for move in legal_moves if board[move[0]][move[1]].value == max(values)][0]

        # Return the move of highest value
        return best_move
