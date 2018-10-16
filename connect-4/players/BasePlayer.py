class BasePlayer(object):
    """ An class representing a Player.

        Attributes:
            name: A string representing the Player's name.
            token: Their board tile, X or O.
    """

    def __init__(self, name):
        """ Initializes a Player.
        """

        # Initializes member variables.
        self.name = name

    def assignToken(self, token):
        """ Assigns the user a token, either X or O
        """
        self.token = token

    def play(self, game):
        """ Plays the game.
        """

    def chooseMove(self):
        return 0
