from abc import ABC, abstractmethod


class Player(ABC):
    """ An abstract class representing a Player.

        Attributes:
            score: An integer representing the Player's current score.
            blocks_taken: A list of Blocks which belong to the Player.
    """

    def ___init___(self):
        """ Initializes a Player.
        """

        # Initializes member variables.
        self.score = 0
        self.blocks_taken = []

        # Calls the Abstract Base Class (ABC) constructor
        super().__init__()

        @abstractmethod
        def evaluate_moves(self, legal_moves):
            """ Evaluates and selects an optimum move.

                Args:
                    legal_moves: A list of legal moves.

                Returns:
                i: An integer representing the x position of the chosen move.
                j: An integer representing the y position of the chosen move.
            """

            # Return dummy values
            return 0, 0
