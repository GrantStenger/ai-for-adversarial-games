from Game import Game
from players.HumanPlayer import HumanPlayer
from players.ComputerPlayerV0 import ComputerPlayerV0

def main():
	""" Initializes Players and a Game, then begins the game.
	"""

	# Initializes Players
	players = [ComputerPlayerV0("Player1"), ComputerPlayerV0("Player2")]

	# Initializes a Game
	game = Game(players)

	# Begins the game
	game.play()

if __name__ == "__main__":
    main()
