class BoardTree:

	def __init__(self, board, letter, indentation):
		self.board = board
		self.letter = letter

		# Find and store all children nodes with legal moves
		self.children = []
		if not isTerminal(board):
			for row in range(3):
				for col in range(3):
					if self.board[row][col] == str((row)*3 + (col+1)):
						move = (row)*3 + (col+1)
						new_board = updateBoard([row[:] for row in board], move, letter)
						# if indentation <= 1:
						# 	PrintBoardIndented(new_board, indentation+1)
						if not isWinning(new_board, letter):
							self.children.append(BoardTree(new_board, otherLetter(letter), indentation+1))
						else:
							self.children.append(BoardTree(new_board, otherLetter(letter), indentation+1))

	def Print(self, indentation):
		PrintBoardIndented(self.board, indentation)
		for child in self.children:
			PrintBoardIndented(child.board, indentation+1)

	def minimax(self):
		# if terminal return utility(board, letter)
		if isTerminal(self.board):
			return score(self.board)
		# else if player == "X" return max(minimax(result(s, a)))
		elif self.letter == "X":
			possible_scores = []
			for child in self.children:
				possible_scores.append(int(child.minimax()))
			return max(possible_scores)
		# else if player == "O" return min(minimax(result(s, a)))
		elif self.letter == "O":
			possible_scores = []
			for child in self.children:
				possible_scores.append(int(child.minimax()))
			return min(possible_scores)

	def __str__(self):
		return PrintBoard(self.board)

def isTerminal(board):
	# Check if board is winning for any players
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2]:
			return True
		elif board[0][i] == board[1][i] == board[2][i]:
			return True
		elif board[0][0] == board[1][1] == board[2][2]:
			return True
		elif board[2][0] == board[1][1] == board[0][2]:
			return True

	# Check if the board is full, if it's not, it's not terminal
	for row in range(3):
		for col in range(3):
			if board[row][col] != "O" and board[row][col] != "X":
				return False

	# If there are no empty spots, it's a tie
	return True

# Checks if any board is winning (general function, will fix code structure soon)
def isWinning(board, letter):
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] == letter:
			return True
		elif board[0][i] == board[1][i] == board[2][i] == letter:
			return True
		elif board[0][0] == board[1][1] == board[2][2] == letter:
			return True
		elif board[2][0] == board[1][1] == board[0][2] == letter:
			return True
	return False

def updateBoard(board, cell_num, letter):
	board[(cell_num-1)//3][(cell_num-1)%3] = letter
	return board

def otherLetter(letter):
	if letter == "X":
		return "O"
	else:
		return "X"

def score(board):

	# Check if board is winning for any players
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2]:
			if board[i][0] == "X":
				return 1
			else:
				return -1
		elif board[0][i] == board[1][i] == board[2][i]:
			if board[0][i] == "X":
				return 1
			else:
				return -1
		elif board[0][0] == board[1][1] == board[2][2]:
			if board[0][0] == "X":
				return 1
			else:
				return -1
		elif board[2][0] == board[1][1] == board[0][2]:
			if board[2][0] == "X":
				return 1
			else:
				return -1

	# Check if the board is full, if it's not, it's not terminal
	for row in range(3):
		for col in range(3):
			if board[row][col] != "O" and board[row][col] != "X":
				print("Error: not a terminal board")

	# If there are no empty spots, it's a tie
	return 0

def PrintBoard(board):
	for row in range(3):
		for column in range(3):
			print(board[row][column], end=" ")
		print()

def PrintBoardIndented(board, indentation):
	for row in range(3):
		for i in range(indentation):
			print(" ", end=" ")
		for column in range(3):
			print(board[row][column], end=" ")
		print()
