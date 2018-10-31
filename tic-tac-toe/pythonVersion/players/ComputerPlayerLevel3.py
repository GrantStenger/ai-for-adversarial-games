from players.ComputerPlayer import ComputerPlayer
from BoardTree import BoardTree

class ComputerPlayerLevel3(ComputerPlayer):

	def __init__(self, letter):
		ComputerPlayer.__init__(self, letter)

	def move(self, board):

		# Construct tree of all possible games
		boardTree = BoardTree(board, self.letter, 0)

		# Play the correct minimax move
		move = self.minimax(boardTree)
		return move

	def minimax(self, boardTree):
		possible_moves = []
		for row in range(3):
			for col in range(3):
				if boardTree.board[row][col] == str((row)*3 + (col+1)):
					move = (row)*3 + (col+1)
					new_board = updateBoard([row[:] for row in boardTree.board], move, self.letter)
					score = BoardTree(new_board, otherLetter(self.letter), 1).minimax()
					possible_moves.append((move, score))

		if self.letter == "X":
			max_score = -1
			for move in possible_moves:
				if move[1] > max_score:
					max_score = move[1]
					best_move = move[0]
		else:
			min_score = 1
			for move in possible_moves:
				if move[1] < min_score:
					min_score = move[1]
					best_move = move[0]

		return best_move

def updateBoard(board, cell_num, letter):
	board[(cell_num-1)//3][(cell_num-1)%3] = letter
	return board

def otherLetter(letter):
	if letter == "X":
		return "O"
	else:
		return "X"
