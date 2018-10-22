from Game import Game
from players.HumanPlayer import HumanPlayer
from players.ComputerPlayerV0 import ComputerPlayerV0
from players.ComputerPlayerV1 import ComputerPlayerV1
from players.ComputerPlayerV2 import ComputerPlayerV2
from players.MinimaxComputerPlayer import MinimaxComputerPlayer

""" CONSTANTS """
ROWS = 6
COLUMNS = 7

def simulate(rows, columns):
	""" Initializes Players and a Game, then begins the game.
	"""

	global player1_wins
	global player2_wins
	global ties

	# Initializes Players
	player1_name = "White"
	player2_name = "Black"
	players = [ComputerPlayerV2(player1_name), ComputerPlayerV2(player2_name)]

	# Initialize board size
	board_size = (rows, columns)

	# Initializes a Game
	game = Game(players, board_size, simulating = True)

	# Begins the game
	game.play()

	if game.winner_name == player1_name:
		player1_wins += 1
	elif game.winner_name == player2_name:
		player2_wins += 1
	else:
		ties += 1

if __name__ == "__main__":
	global player1_wins
	global player2_wins
	global ties
	player1_wins = 0
	player2_wins = 0
	ties = 0

	for i in range(10000):
		if i % 10000 == 0:
			print(i)
		simulate(ROWS, COLUMNS)
	print("Player 1 wins:", player1_wins)
	print("Player 2 wins:", player2_wins)
	print("Ties:", ties)
