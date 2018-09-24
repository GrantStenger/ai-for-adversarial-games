from Game import Game
from HumanPlayer import HumanPlayer


def main():
    """ Initializes Players and a Game, then begins the game.
    """

    # Initializes two human Players
    players = [HumanPlayer(), HumanPlayer()]

    # Initializes a Game with a depth of 3 and 2 colors
    game = Game(players, depth=3, num_colors=2)

    # Begins the game
    game.play()


if __name__ == "__main__":
    main()
