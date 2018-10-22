# Not fully working yet...
from players.BasePlayer import BasePlayer
from random import randrange

class ComputerPlayerV2(BasePlayer):
    """ Represents a computer player who will make immediately winning moves
    and will block opponent when there are possible winning moves for them.

        Attributes:
            name: A string representing the Player's name.
            token: Their board tile, X or O.
    """

    def __init__(self, name):
        """ Initializes a HumanPlayer.
        """

        # Initializes a Player
        super().__init__(name)

    def chooseMove(self, game):

        # Check each column for a possible winning move
        for column in range(game.columns):

            # First, update the imaginary board
            game.imaginary_board = [row[:] for row in game.board]
            game.imaginary_player_to_move = game.player_to_move

            # If there is a winning move in this column, make it.
            valid_move = game.move(column, game.imaginary_board)
            if valid_move:

                # Check if this move is winning
                # (check_board will return 1 if player 1 wins and -1 if player 2 wins)
                move_value = game.check_board(game.imaginary_board)

                # If this is a winning move, return this move
                if game.imaginary_player_to_move == game.player1 and move_value == 1:
                    return column + 1
                elif game.imaginary_player_to_move == game.player2 and move_value == -1:
                    return column + 1

            # Clear the imaginary board
            self.imaginary_board = None

        # After checking all columns, if there is no winning move, move randomly.
        chosen_move = randrange(1, game.columns + 1)
        return chosen_move
