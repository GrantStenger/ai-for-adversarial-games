from players.BasePlayer import BasePlayer
from random import randrange

class ComputerPlayerV1(BasePlayer):
    """ Represents a computer player who plays almost randomly.

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

        # Check each column for a possible winning move
        for column in range(len(board[0])):

            print(column)
            # Make a copy of the board (do not want to pass by reference)
            new_board = [row[:] for row in board]

            # If there is a winning move in this column, make it.
            game.move(column, board)

        # After checking all columns, if there is no winning move, move randomly.
        chosen_move = randrange(1, len(board[0]) + 1)
        return chosen_move
