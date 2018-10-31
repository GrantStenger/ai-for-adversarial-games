from players.OptColorGreedy import OptColorGreedy


class Distance(OptColorGreedy):
    """ Represents a distance computer player.

        If within a small distance of top player, play greedily. Otherwise, choose an optimal color.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors & the number of 1-point blocks the Player has.
            distance: The distance at which point the Player stops being greedy.
    """

    def __init__(self, distance):
        """ Initializes a Distance player.
        """

        # Initializes an OptColorGreedy player
        super().__init__()

        # Sets distance
        self.distance = distance

    def evaluate_moves(self, board, legal_moves, players):
        """ If within a small distance of top player, play greedily. Otherwise, choose an optimal color.

            Args:
                board: A nested array of Blocks.
                legal_moves: A list of legal moves.
                players: A list of players.
            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # Gets the maximum score of all players
        scores = [player.score for player in players]
        max_score = [player.score for player in players if player.score == max(scores)][0]

        # If within a distance of top player and there are high-value blocks available, play greedily
        if self.score >= max_score - self.distance:
            return super().evaluate_moves(board, legal_moves, players)
        # If not within distance, select an optimal color
        else:
            return super().selectOptimalColorByDistance(board, legal_moves, players)
