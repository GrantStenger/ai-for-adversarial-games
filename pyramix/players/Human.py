from players.Player import Player


class Human(Player):
    """ Represents a human player.

        Prompts for input instead of calculating the optimum move.

        Attributes:
            score: An integer representing the Player's current score.
            bonuses_taken_per_color: A dict of colors & the number of 1-point blocks the Player has.
    """

    def __init__(self):
        """ Initializes a Human.
        """

        # Initializes a Player
        super().__init__()

    def evaluate_moves(self, board, legal_moves, players):
        """ Prompts the player to select a move.

            Args:
                board: A nested array of Blocks.
                legal_moves: A list of legal moves.
                players: A list of players.
            Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
        """

        # Prompt the user for input, restricting them to the list of legal moves
        while True:
            try:
                user_input = input('Enter the coordinates of the block you wish to take (in the form "i,j"): ')
                user_input = tuple([int(i) for i in user_input.split(',')])

                while user_input not in legal_moves:
                    print()
                    print('That is not a legal move.')
                    user_input = input('Enter the coordinates of the block you wish to take (in the form "i,j"): ')
                    user_input = tuple([int(i) for i in user_input.split(',')])

                break
            except ValueError:
                print()

        # Return chosen position
        return (int(user_input[0]), int(user_input[1]))
