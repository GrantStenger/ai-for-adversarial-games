from Game import Game
from players.HumanPlayer import HumanPlayer
from players.RandomComputerPlayer import RandomComputerPlayer
from players.MinimaxComputerPlayer import MinimaxComputerPlayer

def main():
	""" Initializes Players and a Game, then begins the game.
	"""

	# Initializes Players
	players = [HumanPlayer("White"), HumanPlayer("Black")]

	# Initializes a Game
	game = Game(players)

	# Begins the game
	game.play()

if __name__ == "__main__":
    main()
