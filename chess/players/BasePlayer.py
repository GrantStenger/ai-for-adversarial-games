class BasePlayer(object):
    """ An class representing a Player.

        Attributes:
            name: A string representing the Player's name.
            color: White or Black
    """

    def __init__(self, name):
        """ Initializes a Player.
        """

        # Initializes member variables
        self.name = name

    def assign_color(self, color):
        """ Assigns the user a color, either White or Black
        """
        self.color = color

    def play(self, game):
        """ Plays the game.
        """
        pass

    def chooseMove(self):
        """ Makes a move
        """
        pass
