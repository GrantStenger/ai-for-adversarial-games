from players.BasePlayer import BasePlayer

class HumanPlayer(BasePlayer):
    """ Represents a human player.

        Prompts for input instead of calculating the optimum move.

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
        has_chosen_valid_move = False
        while not has_chosen_valid_move:

            chosen_move = input("What move would you like to play? \n")
            columns = game.columns
            rows = game.rows
            BLANK = "_"
            quit_strings = ["q", "quit", "Q", "Quit"]

            # Check if the input is a string
            if not chosen_move.isdigit() and not chosen_move in quit_strings:
                print("You must input a valid column number")
            # Check if the input is in the valid range
            elif int(chosen_move) > columns or int(chosen_move) <= 0:
                print("Input not in the valid column range")
            # If it is the valid range, check if the column is full
            elif game.board[0][int(chosen_move)-1] != BLANK:
                print("This column is full")
            else:
                has_chosen_valid_move = True

        return int(chosen_move)
