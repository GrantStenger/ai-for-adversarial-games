from players.BasePlayer import BasePlayer
import os

class HumanPlayer(BasePlayer):
    """ Represents a human player.

        Prompts for input instead of calculating the optimum move.

        Attributes:
            name: A string representing the Player's name.
    """

    def __init__(self, name, token):
        """ Initializes a HumanPlayer.
        """

        # Initializes a Player
        super().__init__(name, token)

    def play(self, game):
        game.printBoard()
        while game.isPlaying():
            chosen_move = self.chooseMove()
            game.move(int(chosen_move) - 1, game.getBoard())

    def chooseMove(self):
        chosen_move = input("What move would you like to play? \n")
        os.system('clear')
        return chosen_move
