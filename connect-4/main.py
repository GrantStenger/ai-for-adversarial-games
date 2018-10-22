from Game import Game
from players.HumanPlayer import HumanPlayer
from players.ComputerPlayerV0 import ComputerPlayerV0
from players.ComputerPlayerV1 import ComputerPlayerV1
from players.ComputerPlayerV2 import ComputerPlayerV2
from players.MinimaxComputerPlayer import MinimaxComputerPlayer

def main():
	""" Initializes Players and a Game, then begins the game.
	"""

	# Initializes Players
	players = [HumanPlayer("White"), ComputerPlayerV1("Black")]

	# Initialize board size
	rows = 5
	columns = 5
	board_size = (rows, columns)

	# Initializes a Game
	game = Game(players, board_size)

	# Begins the game
	game.play()

if __name__ == "__main__":
    main()
