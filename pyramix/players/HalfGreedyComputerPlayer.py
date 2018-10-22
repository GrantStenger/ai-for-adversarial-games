from random import randint
import numpy as np

from players.ComputerPlayer import ComputerPlayer


class HalfGreedyComputerPlayer(ComputerPlayer):

    """ Represents a half greedy computer player.

        Attributes:
            score: An integer representing the Player's current score.
            blocks_taken: A list of Blocks which belong to the Player.
    """

    def __init__(self):
        """ Initializes a ComputerPlayer.
        """

        # Initializes a ComputerPlayer
        super().__init__()

    def evaluate_moves(self, board, legal_moves):
        """ 50/50 chance to either be greedy or random.

            Args:
                board: A nested array of Blocks.
                legal_moves: A list of legal moves.
            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """
        
        # 50/50 chance to be greedy or random
        if (randint(0,1) == 0):
            # Return the highest points move
            values = [board[move[0]][move[1]].value for move in legal_moves]
            best_move = [move for move in legal_moves if board[move[0]][move[1]].value == max(values)][0]
            return best_move
        else:
            # Randomly select new position
            ind = np.random.choice(np.arange(len(legal_moves)))
            new_pos = legal_moves[ind]

            # Returns random position
            return new_pos
