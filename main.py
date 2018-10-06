from Game import Game
from players.HumanPlayer import HumanPlayer
from players.RandomComputerPlayer import RandomComputerPlayer


def main():
    """ Initializes Players and a Game, then begins the game.
    """

    # Initializes Players
    players = [HumanPlayer(), RandomComputerPlayer(), RandomComputerPlayer()]

    # Initializes a Game
    game = Game(players, depth=7, num_colors=4)

    # Begins the game
    game.play()


if __name__ == "__main__":
    main()
