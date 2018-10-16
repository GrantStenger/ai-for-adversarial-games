from Game import Game
from players.HumanPlayer import HumanPlayer
from players.ComputerPlayer import ComputerPlayer

def main():
	""" Initializes Players and a Game, then begins the game.
	"""

	# Initializes Players
	players = [HumanPlayer("White", "X"), HumanPlayer("Black", "O")]

	# Initializes a Game
	game = Game(players)

	# Begins the game
	game.play()

if __name__ == "__main__":
    main()
