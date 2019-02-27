from Game import Game
from players.HumanPlayer import HumanPlayer
from players.ComputerPlayerV0 import ComputerPlayerV0
from players.ComputerPlayerV1 import ComputerPlayerV1
import argparse

def main():
	""" Initializes Players and a Game, then begins the game.
	"""

	# Initializes Players
	players = [ComputerPlayerV1("Player1"), ComputerPlayerV0("Player2")]

	# Initializes a Game
	game = Game(players, FLAGS.unicode, FLAGS.simulating)

	# Begins the game
	game.play()

if __name__ == "__main__":
    # Instantiates an arg parser
    PARSER = argparse.ArgumentParser()

    # Adds arguments
    PARSER.add_argument("--unicode", type=bool, default=False,
                        help="True or False, display pieces as unicode")
    PARSER.add_argument("--simulating", type=str, default=None,
                        help="If similating is True, then there will be no console output.")
    # PARSER.add_argument("--out_dir", type=str, default="data",
    #                     help="path to export directory")
    # PARSER.add_argument("--x_dir", type=str, default=None,
    #                     help="path to x data directory")
    # PARSER.add_argument("--y_dir", type=str, default=None,
    #                     help="path to y data directory")
    # PARSER.add_argument("--batch_size", type=int, default=8,
    #                     help="batch size")
    # PARSER.add_argument("--epochs", type=int, default=100,
    #                     help="number of GAN epochs")
    # PARSER.add_argument("--start_epoch", type=int, default=0,
    #                     help="starting epoch for GAN")
    # PARSER.add_argument("--ginit_epochs", type=int, default=10,
    #                     help="number of generator init epochs")
    # PARSER.add_argument("--ginit_start_epoch", type=int, default=0,
    #                     help="starting epoch for generator init")

    # Parses known arguments
    FLAGS, _ = PARSER.parse_known_args()

    main()
