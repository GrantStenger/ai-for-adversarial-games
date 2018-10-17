from players.ComputerPlayer import ComputerPlayer

# This AI blocks the opponent from playing immediately winning moves
# It will also play immediately winning moves for itself, otherwise it plays randomly
class ComputerPlayerLevel2(ComputerPlayer):

	def __init__(self, letter):
		ComputerPlayer.__init__(self, letter)

	def move(self, board):

		# Find and store all open cells
		open_cells = []
		for row in range(3):
			for col in range(3):
				if board[row][col] == str((row)*3 + (col+1)):
					open_cells.append((row)*3 + (col+1))

		# If any of these moves result in an immediate win, do this.
		for cell_num in open_cells:

			# Make a copy of the board (do not want to pass by reference)
			new_board = [row[:] for row in board]

			# Check if executing this move will result in a win
			new_board = updateBoard(new_board, cell_num, self.letter)
			if isWinning(new_board, self.letter):
				# If so, execute this move
				return cell_num

		# Check if this move creates any immediately winning moves for the opponent
		for cell_num in open_cells:

			# Create the new board that would result in making this legal move
			new_board = [row[:] for row in board]
			new_board = updateBoard(new_board, cell_num, self.letter)

			# Iterate through each of the opponents move, an if they could win, block them.
			opponent_open_cells = []
			for row in range(3):
				for col in range(3):
					if new_board[row][col] == str((row)*3 + (col+1)):
						opponent_open_cells.append((row)*3 + (col+1))
			for opponent_cell_num in opponent_open_cells:
				opponent_new_board = [row[:] for row in new_board]
				opponent_new_board = updateBoard(opponent_new_board, opponent_cell_num, otherLetter(self.letter))
				if isWinning(opponent_new_board, otherLetter(self.letter)):
					return opponent_cell_num

		# Play a random legal move
		return open_cells[random.randrange(len(open_cells))]
