from Player import Player

class HumanPlayer(Player):
    """ Represents a human player.

        Prompts for input instead of calculating the optimum move.

        Attributes:
            score: An integer representing the Player's current score.
            blocks_taken: A list of Blocks which belong to the Player.
    """

    def __init__(self):
        """ Initializes a HumanPlayer.
        """
        # Initializes a Player
        Player.__init__(self)

    def evaluate_moves(self, legal_moves):
        """ Prompts the player to select a move.

            TODO: Restrict them to the list of legal moves.

            Args:
                legal_moves: A list of legal moves.

            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # Prompt the user for input
        user_input = input('Enter the coordinates of the block you wish to take (in the form "i,j"): ')

        # Parse input
        i, j = user_input.split(',')

        # Return chosen position
        return int(i), int(j)
