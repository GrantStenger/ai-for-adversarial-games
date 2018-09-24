class Block:
    """ Represents a Block.

        Attributes:
            color: A string representing the desired Block color (e.g., "A").
            value: An integer representing the desired Block value
    """

    def __init__(self, color, value):
        """ Initializes a Block.

            Args:
                color: A string representing the desired Block color (e.g., "A").
                value: An integer representing the desired Block value
        """

        # Initializes member variables
        self.color = color
        self.value = value

    def __repr__(self):
        """ Overrides the print function to return the Block's color.
        """
        return self.color
