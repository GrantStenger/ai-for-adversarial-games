from players.BasePlayer import BasePlayer
from BoardTree import BoardTree

class NewMiniMaxPlayer(BasePlayer):

    def __init__(self, name):
        """ Initializes a MiniMaxPlayer.
        """

        # Initializes a Player
        super().__init__(name)

    def chooseMove(self, game):

        # Create a BoardTree of depth D
        DEPTH = 2
        board_tree = BoardTree(game, game.board, game.player_to_move, DEPTH)

        # board_tree.print_tree()

        # Given a calculated board tree, select the best move
        chosen_move = board_tree.get_best_move().move_to_make

        return chosen_move
