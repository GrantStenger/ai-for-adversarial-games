# This currently does not work. This will be fixed soon.

from players.BasePlayer import BasePlayer

class MinimaxComputerPlayer(BasePlayer):

	def __init__(self, name):
		self.name = name

		# When performing minimax, we will be manipulating this mental board
		self.mental_game = Game()

	def play(self, game):
		# Establish real game
		self.real_game = game

		# Print Board
		self.real_game.printBoard()

		# Play until game is over
		while self.real_game.isPlaying():

			# Clear the terminal (purely aesthetic)
			os.system('clear')

			# Decide move
			move = self.minimax(self.real_game.getBoard(), self.real_game.getPlayerToMove())

			# Make move
			self.real_game.move(move, self.real_game.getBoard())

	def minimax(self, board, player_to_move):
		# There are 7 possible moves (i.e. slots to place a tile). Store each possibility here.
		children = []

		# Iterate through each possibility
		for i in range(7):
			self.mental_game = self.real_game
			board, score = self.mental_game.move(i, board)
			if player_to_move == "white" and score == 1:
				print("return 1")
				return 1
			elif player_to_move == "black" and score == -1:
				print("return 1")
				return 1
			else:
				children.append(board)

		if player_to_move == "white":
			return self.max(children)
		else:
			return self.min(children)

	def max(self, children):
		curr_val = self.minimax(children[0], "white")
		move = 0
		for i in range(1, 7):
			move_currently_exploring = self.minimax(children[i], "white")
			if move_currently_exploring > curr_val:
				curr_val = move_currently_exploring
				move = i
		print("return move", move)
		return move

	def min(self, children):
		curr_val = self.minimax(children[0], "black")
		move = 0
		for i in range(1, 7):
			move_currently_exploring = self.minimax(children[i], "black")
			if move_currently_exploring < curr_val:
				curr_val = move_currently_exploring
				move = i
		return move
