from players.BasePlayer import BasePlayer
from random import randrange

class RandomComputerPlayer(BasePlayer):
    """ Represents a computer player who plays randomly.

        Attributes:
            name: A string representing the Player's name.
            token: Their board tile, X or O.
    """

    def __init__(self, name):
        """ Initializes a HumanPlayer.
        """

        # Initializes a Player
        super().__init__(name)

    def chooseMove(self, board):
        chosen_move = randrange(1, len(board[0]) + 1)
        return chosen_move
