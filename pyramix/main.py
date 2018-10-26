import sys
import argparse
from Game import Game
from players.HumanPlayer import HumanPlayer
from players.RandomComputerPlayer import RandomComputerPlayer
from players.GreedyComputerPlayer import GreedyComputerPlayer
from players.DistanceComputerPlayer import DistanceComputerPlayer

def main(_):
    """ Initializes Players and a Game, then begins the game.
    """

    # Initializes Players
    players = [HumanPlayer(), DistanceComputerPlayer(4), DistanceComputerPlayer(3)]

    # Initializes a Game
    game = Game(players, depth=FLAGS.depth, num_colors=FLAGS.num_colors, vprint=print)

    # Begins the game
    game.play()


if __name__ == "__main__":
    # Instantiates an arg parser
    parser = argparse.ArgumentParser()

    # Establishes default arguments
    parser.add_argument("--depth", type=int, default=3, help="Depth of game")
    parser.add_argument("--num_colors", type=int, default=2, help="Number of colors in the game")

    # Parse known arguments
    FLAGS, unparsed = parser.parse_known_args()

    # Run the game
    main([sys.argv[0]] + unparsed)
