BLANK = "_"

class Game:

	def __init__(self, players):
		self.board = self.makeBoard()
		self.player1 = players[0]
		self.player2 = players[1]
		self.player_to_move = self.player1
		self.playing = True

	def makeBoard(self):
		rows = 6
		columns = 7
		board = [[BLANK for j in range(columns)] for i in range(rows)]
		return board

	def printBoard(self):
		for row in range(len(self.board)):
			for col in range(len(self.board[0])):
				print(self.board[row][col], end=' ')
			print()

	def move(self, slot, board):
		if slot < 7 and slot >= 0:
			if board[0][slot] != BLANK:
				print("slot is full u fuck, try again")
			else:
				height = 5
				while board[height][slot] != BLANK and height > 0:
					height -= 1;
				board[height][slot] = self.player_to_move.token
		elif slot == "q" or slot == "Q" or slot == "quit":
				self.playing = False
		else:
			print("U fucked up. not a slot")

		# Check if anyone has won yet, and return 1 if player 1 won or -1 if lost
		move_val = self.check_board()

		# Display updated board
		self.printBoard()

		print("HERE")
		# Switch whose turn it is
		if self.player_to_move == self.player1:
			print("here1")
			self.player_to_move = self.player2
		else:
			print("here2")
			self.player_to_move = self.player1

		return board, move_val

	# Check for victory (i.e. 4-in-a-row)
	def check_board(self):

		# Check horizontal
		for row in range(len(self.board)):
			count = 1
			curr_val = self.board[row][0]
			for column in range(1, len(self.board[row])):
				if curr_val == self.board[row][column] and curr_val != BLANK:
					count += 1
					if count == 4:
						print(self.player_to_move.name, "wins!")
						self.playing = False
						if self.player_to_move == self.player1:
							return 1
						else:
							return -1
				else:
					count = 1
				curr_val = self.board[row][column]

		# Check vertical connect 4
		# Iterate through each of the columns
		for column in range(len(self.board[0])):
			# Initialize count to 1 and set the current value to the top cell in each column
			count = 1
			curr_val = self.board[0][column]
			# Go down the rows and check if there are 4 tiles of the same color in a row
			for row in range(1, len(self.board)):
				# If next value in column is the same as the previous value
				if curr_val == self.board[row][column] and curr_val != BLANK:
					# Increment count
					count += 1
					# If this is the fourth of the same tile in a row,
					# Then that player has won
					if count == 4:
						# Print the winner
						print(self.player_to_move.name, "wins!")
						# Set playing to false so the game knows not to play anymore
						self.playing = False
						# Exit the function
						if self.player_to_move == self.player1:
							return 1
						else:
							return -1
				# If the next value in the column is different from the previous value
				else:
					# Reset count to 1
					count = 1
				# Set the new current value to value of the tile we just checked
				curr_val = self.board[row][column]

		# Check diagonal
		for row in range(3):
			for column in range(4):
				if self.board[row][column] == self.board[row+1][column+1] == \
				   self.board[row+2][column+2] == self.board[row+3][column+3] != BLANK:
					print(self.player_to_move.name, "wins!")
					self.playing = False
					if self.player_to_move == self.player1:
						return 1
					else:
						return -1

		for row in range(4, 6):
			for column in range(4):
				if self.board[row][column] == self.board[row-1][column+1] == \
				   self.board[row-2][column+2] == self.board[row-3][column+3] != BLANK:
					print(self.player_to_move.name, "wins!")
					self.playing = False
					if self.player_to_move == self.player1:
						return 1
					else:
						return -1

		# If no one has won, return 0
		return 0

	def isPlaying(self):
		return self.playing

	def getBoard(self):
		return self.board

	def getPlayerToMove(self):
		return self.player_to_move

	def play(self):
		""" Runs gameplay until the game is over, then scores bonus Blocks.
		"""

		# Display board
		self.printBoard()

		# Runs game until a player has won
		while self.isPlaying():
			chosen_move = self.player_to_move.chooseMove()
			self.move(int(chosen_move) - 1, self.getBoard())
