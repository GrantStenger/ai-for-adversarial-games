"""
A class storing a Connect-4 position.
Functions are relative to the current player to play.
Positions containing alignment are not supported by this class.
"""

class Position:

    def __init__(self, width, height):
        WIDTH = width
        HEIGHT = height

    # Indicates whether or not a column is playable.
    def canPlay(self, col):
        pass

    """
    Plays a playable column.
    This function should not be called on a non-playble column
    or column making an alignment.
    """
    def play(self, col):
        pass

    """
    Indicates whether the current player wins by playing a given column.
    This function should never be called on a non-playable column.
    """
    def isWinningMove(self, col):
        pass

    # Returns the number of moves played from the beginning of the game
    def numMoves(self):
        pass
