from players.BasePlayer import BasePlayer
import random

class ComputerPlayerV0(BasePlayer):
    """ Represents a computer player who plays randomly.

        Attributes:
            name: A string representing the Player's name.
            color: Black or White
    """

    def __init__(self, name):
        """ Initializes a Random Player.
        """

        # Initializes a Player
        super().__init__(name)

    def choose_move(self, game):
        legal_moves = game.board.legal_moves
        chosen_move = game.board.uci(random.choice(list(legal_moves)))
        return chosen_move
