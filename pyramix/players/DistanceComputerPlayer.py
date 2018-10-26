from players.ComputerPlayer import ComputerPlayer
import string
import sys


class DistanceComputerPlayer(ComputerPlayer):

    """ Represents a distance computer player.

        If within a small distance of top player, play greedily. Otherwise, choose an optimal color.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors and the number of 1-point blocks the Player has of them. 
            distance: The distance at which point the Player stops being greedy.
    """

    def __init__(self, distance):
        """ Initializes a ComputerPlayer.
        """

        # Initializes a ComputerPlayer
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

        # Gets all the values of the legal moves
        values = [board[move[0]][move[1]].value for move in legal_moves]

        # Gets the maximum score of all players
        scores = [player.score for player in players]
        max_score = [player.score for player in players if player.score == max(scores)][0]

        # If within a distance of top player and there are high-value blocks available, play greedily
        if self.score >= max_score - self.distance and max(values) > 1:
            # Return the highest points move
            best_move = [move for move in legal_moves if board[move[0]][move[1]].value == max(values)][0]
            return best_move

        # Select an optimal color
        else:
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
                    if leads == True:
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
