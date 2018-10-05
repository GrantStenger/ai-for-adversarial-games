from Game import Game
from players.HumanPlayer import HumanPlayer
from players.RandomComputerPlayer import RandomComputerPlayer


def main():
    """ Initializes Players and a Game, then begins the game.
    """

    # Initializes two human Players
    players = [RandomComputerPlayer() for _ in range(3)]

    # Initializes a Game with a depth of 3 and 2 colors
    game = Game(players, depth=7, num_colors=4)

    # Begins the game
    game.play()


if __name__ == "__main__":
    main()
