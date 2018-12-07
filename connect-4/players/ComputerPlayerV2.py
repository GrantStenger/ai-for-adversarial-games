# Not fully working yet...
from players.BasePlayer import BasePlayer
from random import choice, randrange

class ComputerPlayerV2(BasePlayer):
    """ Represents a computer player who will make immediately winning moves
    and will not make moves which are immediately winning for the opponent.

        Attributes:
            name: A string representing the Player's name.
            token: Their board tile, X or O.
    """

    def __init__(self, name):
        """ Initializes a ComputerPlayerV2.
        """

        # Initializes a Player
        super().__init__(name)

    def chooseMove(self, game):

        # Store valid moves in a list to only need to check once
        valid_moves = []

        # Check each possible move and play if immediately winning
        for column in range(game.columns):

            # First, update the imaginary board
            game.imaginary_board = [row[:] for row in game.board]
            game.imaginary_player_to_move = game.player_to_move

            # If there is a winning move in this column, make it.
            valid_move = game.move(column, game.imaginary_board)
            if valid_move:

                # Add this to the list of valid moves
                valid_moves.append(column)

                # Check if this move is winning
                # (check_board will return 1 if player 1 wins and -1 if player 2 wins)
                move_value = game.check_board(game.imaginary_board, imaginary = True)

                # If this is a winning move, return this move
                if game.imaginary_player_to_move == game.player1 and move_value == 1:
                    return column + 1
                elif game.imaginary_player_to_move == game.player2 and move_value == -1:
                    return column + 1

            # Clear the imaginary board
            self.imaginary_board = None

        # Check if this move creates any immediately winning moves for the opponent and block if so.
        for column in valid_moves:
            # Create the new board that would result in making this legal move
            game.imaginary_board = [row[:] for row in game.board]
            game.imaginary_player_to_move = game.player_to_move

            # Create opponent variable
            if game.imaginary_player_to_move == game.player1:
                opponent = game.player2
            elif game.imaginary_player_to_move == game.player2:
                opponent = game.player1

            # Make this move
            game.move(column, game.imaginary_board)

            # Iterate through each of the opponents move, an if they could win, block them.
            for opponent_column in range(game.columns):
                opponent_new_board = [row[:] for row in game.imaginary_board]

                # If there is a winning move in this column, make it.
                opponent_valid_move = game.move(opponent_column, opponent_new_board, opponent)

                if opponent_valid_move:

                    # Check if this move is winning
                    # (check_board will return 1 if player 1 wins and -1 if player 2 wins)
                    move_value = game.check_board(opponent_new_board, imaginary = True)

                    # If this is a winning move, return this move
                    if opponent_column != column:
                        if opponent == game.player1 and move_value == -1:
                            return opponent_column + 1
                        elif opponent == game.player2 and move_value == 1:
                            return opponent_column + 1
                    else:
                        valid_moves.remove(opponent_column)

                # Clear the imaginary board
                self.imaginary_board = None

        # After checking all columns, if there is no winning move, move randomly.
        if len(valid_moves) > 0:
            chosen_move = choice(valid_moves)
        else:
            # Check each possible move and play if possible
            for column in range(game.columns):
                game.imaginary_board = [row[:] for row in game.board]
                # If there is a winning move in this column, make it.
                valid_move = game.move(column, game.imaginary_board)
                if valid_move:
                    return column + 1
        return chosen_move + 1
