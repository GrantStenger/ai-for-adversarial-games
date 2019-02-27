from players.BasePlayer import BasePlayer
import PythonChess.chess as chess

class ComputerPlayerV1(BasePlayer):
    """ Represents a player who always plays the move the immediately maximizes
    "board score".

        Attributes:
            name: A string representing the Player's name.
            color: Black or White
    """

    def __init__(self, name):
        """ Initializes Computer Player V1.
        """

        # Initializes a Player
        super().__init__(name)

    def choose_move(self, game):
        legal_moves = list(game.board.legal_moves)
        print(legal_moves)

        for move in legal_moves:

            # First, update the imaginary board
            game.imaginary_board = chess.Board(game.board.board_fen())
            # game.imaginary_player_to_move = game.player_to_move

            print(move)

        # chosen_move = game.board.uci(random.choice(list(legal_moves)))
        # return chosen_move

    def connect4_choose_move(self, game):

        valid_moves = []

        # Check each column for a possible winning move
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
                move_value = game.check_board(game.imaginary_board)

                # If this is a winning move, return this move
                if game.imaginary_player_to_move == game.player1 and move_value == 1:
                    return column + 1
                elif game.imaginary_player_to_move == game.player2 and move_value == -1:
                    return column + 1

            # Clear the imaginary board
            self.imaginary_board = None

        # After checking all columns, if there is no winning move, move randomly.
        chosen_move = choice(valid_moves)
        return chosen_move + 1
