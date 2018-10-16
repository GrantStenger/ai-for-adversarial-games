from ComputerPlayer import ComputerPlayer

# This AI plays legal moves randomly
class ComputerPlayerLevel0(ComputerPlayer):

	def __init__(self, letter):
		ComputerPlayer.__init__(self, letter)

	def move(self, board):

		# Find and store all open cells
		open_cells = []
		for row in range(3):
			for col in range(3):
				if board[row][col] == str((row)*3 + (col+1)):
					open_cells.append((row)*3 + (col+1))

		# Play a random legal move
		return open_cells[random.randrange(len(open_cells))]
