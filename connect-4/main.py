from Game import Game
from players.HumanPlayer import HumanPlayer
from players.RandomComputerPlayer import RandomComputerPlayer
from players.MinimaxComputerPlayer import MinimaxComputerPlayer

def main():
	""" Initializes Players and a Game, then begins the game.
	"""

	# Initializes Players
	players = [RandomComputerPlayer("White"), RandomComputerPlayer("Black")]

	# Initialize board size
	rows = 8
	columns = 8
	board_size = (rows, columns)

	# Initializes a Game
	game = Game(players, board_size)

	# Begins the game
	game.play()

if __name__ == "__main__":
    main()
