from players.ComputerPlayer import ComputerPlayer

# This AI can play immeditaly winning moves, but otherwise plays randomly
class ComputerPlayerLevel1(ComputerPlayer):

	def __init__(self, letter):
		ComputerPlayer.__init__(self, letter)

	def move(self, board):

		# Find and store the cells of all legal moves
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

		# Play a random legal move
		return open_cells[random.randrange(len(open_cells))]
