class BasePlayer(object):
    """ An class representing a Player.

        Attributes:
            name: A string representing the Player's name.
    """

    def __init__(self, name, token):
        """ Initializes a Player.
        """

        # Initializes member variables.
        self.name = name
        self.token = token

    def play(self, game):
        """ Plays the game.
        """

    def chooseMove(self):
        return 0
