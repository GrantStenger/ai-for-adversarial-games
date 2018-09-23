from random import shuffle
import string

class Game:

	def __init__(self, players, depth, num_colors):
		self.players = players
		self.colors = ["A", "B", "C", "D"]
		self.depth = depth
		self.board = self.initialize_board(depth, num_colors)
		self.legal_moves = self.initialize_legal_moves()
		self.current_player = 0
		self.game_over = False
		self.blocks_left = depth * (depth + 1) / 2

	def generate_colors(self, num_colors):
		colors = list(string.ascii_uppercase)
		return colors[:num_colors]

	def initialize_board(self, depth, num_colors):

		total_blocks = depth * (depth + 1) / 2
		blocks_per_color = total_blocks / num_colors

		# If the colors can't be divided evenly, then raise an error
		if blocks_per_color != int(blocks_per_color):
			raise ValueError("Colors can't be divided evenly given this depth.")
		else:
			blocks_per_color = int(blocks_per_color)

		blocks = []
		for i in range(num_colors):
			for j in range(blocks_per_color):
				blocks.append(Block(self.colors[i], 1))
		shuffle(blocks)

		board = []
		for i in range(depth):
			row = []
			for j in range(depth - i):
				row.append(blocks.pop())
			board.append(row)

		return board

	def make_move(self, position):
		print()

	def score_bonus_blocks(self):
		return 0

	def initialize_legal_moves(self):
		legal_moves = []

		for i in range(len(self.board)):
			for j in range(len(self.board[i])):

				# If the move is on the edge of the board and there's not an empty cell above it (e.g. it's locked on the bottom)
				# Or the move is in the center with an empty cell above it,
				# Then add it to the list of legal moves
				if (i == 0 and self.board[i][j-1].color != "0") or \
				   (j == 0 and self.board[i-1][j].color != "0") or \
				   self.board[i-1][j].color == "0" or \
				   self.board[i][j-1].color == "0":
					legal_moves.append((i, j))

		print(legal_moves)
		return legal_moves

	def update_legal_moves(self, move):
		i = move[0]
		j = move[1]

		# For every axis, we iterate down until we hit an empty block
		# Then, all adjacent blocks become legal moves
		current_block = self.board[i][j]

		# First, we check the x axis
		while current_block.color != "0" and j - 1 >= 0:
			j -= 1
			current_block = self.board[i][j]

		# Make adjacent blocks legal
		if (i-1, j) not in self.legal_moves:
			self.legal_moves.append((i-1, j))
		if (i, j-1) not in self.legal_moves:
			self.legal_moves.append((i, j-1))

		# Reset i and j
		i = move[0]
		j = move[1]

		# Then, we check the y axis
		while current_block.color != "0" and i - 1 >= 0:
			i -= 1
			current_block = self.board[i][j]

		# Make adjacent blocks legal
		if (i-1, j) not in self.legal_moves:
			self.legal_moves.append((i-1, j))
		if (i, j-1) not in self.legal_moves:
			self.legal_moves.append((i, j-1))

		print(self.legal_moves)

	def play(self):
		while not self.game_over:
			print(self.board)

			move = self.players[self.current_player].evaluate_moves(self.legal_moves)

			self.make_move(move)

			if self.blocks_left == self.depth:
				self.game_over = True

			self.update_legal_moves(move)

			# Make next player current player
			self.current_player = (self.current_player + 1) % len(self.players)
		score_bonus_blocks()
		return 0

class Block:

	def __init__(self, color, value):
		self.color = color
		self.value = value

	def __repr__(self):
		return self.color

class HumanPlayer:

	def __init__(self):
		score = 0
		blocks_taken = []

	def evaluate_moves(self, legal_moves):
		user_input = input('Enter the coordinates of the block you wish to take (in the form "i,j"): ')
		i, j = user_input.split(',')
		print("i: ", i)
		print("j: ", j)
		return i, j

class ComputerPlayer:

	def __init__(self):
		score = 0
		blocks_taken = []

	def evaluate_moves(self, legal_moves):
		i = 0
		j = 0
		chosen_move = (i, j)
		return chosen_move

def main():
	players = [HumanPlayer(), HumanPlayer()]
	game = Game(players, 3, 2)
	game.play()

if __name__ == "__main__":
	main()