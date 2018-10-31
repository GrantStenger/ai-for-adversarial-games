import string
import sys

from players.Greedy import Greedy


class OptColorGreedy(Greedy):
    """ Represents a greedy computer player which selects colors based on distance from leader.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors & the number of 1-point blocks the Player has.
    """

    def __init__(self):
        """ Initializes an OptColorGreedy player.
        """

        # Initializes a Greedy player
        super().__init__()

    def evaluate_moves(self, board, legal_moves, players):
        """ If there is a high-value block, take it; otherwise, select an optimal color.

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
        if max(values) > 1:
            return super().evaluate_moves(board, legal_moves, players)
        # If there are only 1-point blocks, select an optimal color
        else:
            return self.selectOptimalColorByDistance(board, legal_moves, players)

    def selectOptimalColorByDistance(self, board, legal_moves, players):
        """ Selects an optimal color based on distance from color leader.

            Args:
                board: A nested array of Blocks.
                legal_moves: A list of legal moves.
                players: A list of players.
            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # Makes a list of the maximum values of each color over all players
        max_colors = [0] * len(self.bonuses_taken_per_color)
        for player in players:
            for i, color_num in enumerate(list(player.bonuses_taken_per_color.values())):
                max_colors[i] = max(max_colors[i], color_num)

        # Makes a list of differences between max_colors and this Player's colors
        color_differences = [i - j for i, j in zip(max_colors, list(self.bonuses_taken_per_color.values()))]

        # Makes a list of colors "A", "B", etc.
        colors = list(string.ascii_uppercase)[:len(self.bonuses_taken_per_color)]

        # Iterate over colors in order of difference between max_colors and this Player's colors
        for i in range(len(colors)):
            min_diff = min(color_differences)
            min_diff_index = color_differences.index(min_diff)
            min_color = colors[min_diff_index]

            # If the Player leads or is tied for the color
            if min_diff == 0:
                leads = True
                for player in players:
                    if player.bonuses_taken_per_color[min_color] == self.bonuses_taken_per_color[min_color] and player != self:
                        leads = False

                # If the Player leads in the color, don't take it
                if leads:
                    color_differences[min_diff_index] = sys.maxsize

                # If the Player is tied for the color, take it if it exists
                else:
                    for move in legal_moves:
                        i = move[0]
                        j = move[1]
                        if board[i][j].value == 1 and board[i][j].color == min_color:
                            return move
                    # If it doesn't exist, set diff to a large number
                    color_differences[min_diff_index] = sys.maxsize

            # If the Player is behind in the color, take it if it exists
            else:
                for move in legal_moves:
                    i = move[0]
                    j = move[1]
                    if board[i][j].value == 1 and board[i][j].color == min_color:
                        return move
                # If it doesn't exist, set diff to a large number
                color_differences[min_diff_index] = sys.maxsize

            # If the player leads in all colors, pick a random Block.
            return legal_moves[0]
