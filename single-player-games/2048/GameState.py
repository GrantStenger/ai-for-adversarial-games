"""
To Do:
* Fix camelCase
* Combine move funtions by rotating the board
Write function descriptions
Fix terminal case when board if full but moves still possible
"""

import numpy as np
import os
import math

# Define Constants
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

class GameState:

	def __init__(self, depth_to_search, current_depth = 0, board = [], score = 0):

		# print()
		# print()
		# print("NEW GAMESTATE!")
		# print()
		# print()

		# Read in high score from file and initialize
		f = open("highscore.txt", "r")
		self.highscore = int(f.read())
		f.close()

		self.score = 0
		self.depth_to_search = depth_to_search
		self.current_depth = current_depth
		self.value = 0

		# If a board is not being passed in...
		if board == []:
			# Initialize the board with two random tiles
			self.board = np.zeros((4, 4), dtype=np.int)
			self.total_tiles = 0 # Incremented by add_tile
			self.add_tile()
			self.add_tile()
			# Initialize current score as 0
			self.score = 0
		else:
			self.board = board
			self.score = score
			self.total_tiles = self.get_total_tiles()

		# Use boolean to check if the game is over
		self.game_over = False

		# Calculate the value of this position and best move
		if current_depth < depth_to_search:
			self.get_best_action()

	# Add a new tile to an empty cell of the board
	def add_tile(self):

		# Make a list of tuples of all the empty cells
		x_val, y_val = np.where(self.board == 0)
		empty_cells = list(zip(x_val,y_val))

		# Select one of these cells at random
		empty_cell = empty_cells[np.random.choice(len(empty_cells))]

		# Select a value of 2 or 4 with a ratio of 9:1
		tile_val = np.random.choice([2, 4], p=[0.9, 0.1])

		# Update the board
		self.board[empty_cell[0]][empty_cell[1]] = tile_val

		# Update total_tiles
		self.total_tiles += 1

		# Check if high score needs to be updated
		self.check_high_score()

		# Check for game over
		self.check_for_game_over()

	def get_total_tiles(self):
		total_tiles = 0
		for row in self.board:
			for col in row:
				if col != 0:
					total_tiles += 1
		return total_tiles

	# Print the board and all other necessary information
	def display(self):

		# Clear the screen and print the score
		os.system('clear')
		print()
		print("Current Score: " + str(self.score))
		print("High Score: " + str(self.highscore))
		print()

		# Iterate through each tile and print accordingly
		for row in range(4):
			print(end="  ")
			for col in range(4):
				if self.board[row][col] == 0:
					print(end=".   ")
				elif int(math.log10(self.board[row][col])) == 0:
					print(self.board[row][col], end="   ")
				elif int(math.log10(self.board[row][col])) == 1:
					print(self.board[row][col], end="  ")
				elif int(math.log10(self.board[row][col])) == 2:
					print(self.board[row][col], end=" ")
				elif self.board[row][col] == 1024:
					print("1k", end="  ")
				elif self.board[row][col] == 2048:
					print("2k", end="  ")
				elif self.board[row][col] == 4096:
					print("4k", end="  ")
				else:
					print(self.board[row][col])
			print()
		print()

	# Implements slide logic by rotating the board as necessary, sliding left,
	# and rotating back. If the move is real, change the board of this object,
	# otherwise create a new state with the new board.
	def move(self, input_action, real = True):

		# Deep copy the board
		board = [x[:] for x in self.board]
		score = self.score
		total_tiles = self.total_tiles

		# The logic slides left, so to slide up, for example, rotate counter-clockwise
		num_rotations = input_action
		board = np.rot90(board, num_rotations)

		# The cells changed counter makes sure we don't make moves where the
		# board does not change.
		cells_changed = 0

		# Store the original score to later determine how many points were earned
		# from this turn specifically.
		original_score = score

		# Iterate through each row to perform sliding logic
		for row in range(4):

			# As we move across the row, we will keep track of the value that
			# a tile "could be merged with".
			possible_merge_val = 0

			next_open_index = 0

			for col in range(4):
				curr_val = board[row][col]

				# If the tile is not empty (i.e. curr_val is not 0), check if
				# merge logic is necessary.
				if curr_val != 0:
					# If the value of the current column is the mergable value,
					# then merge.
					if curr_val == possible_merge_val:
						# Change the left cell to be merged to 2 times itself
						board[row][next_open_index-1] = (curr_val * 2)
						# Set the current cell to 0
						board[row][col] = 0
						# Update the score
						score += (curr_val * 2)
						# Decrement the counter for total tiles on the board
						total_tiles -= 1
						# Increment the counter for cells changed
						cells_changed += 1
						# After we've merged, no more cells can merge with this
						possible_merge_val = 0
					# If the current tile is empty,
					else:
						# If there's an open spot somewhere to the left, slide.
						if next_open_index != col:
							# Put this tile in the leftmost open spot
							board[row][next_open_index] = curr_val
							# Empty the current cell
							board[row][col] = 0
							# Increment the cell changed counter
							cells_changed += 1
						# Update the "mergable value"
						possible_merge_val = curr_val
						# Update the next open index
						next_open_index += 1

		# Rotate the board back to its original orientation
		board = np.rot90(board, 4-num_rotations)

		# Add a new tile to an empty cell of the board only if the board has changed
		if cells_changed != 0:

			# Make a list of tuples of all the empty cells
			x_val, y_val = np.where(board == 0)
			empty_cells = list(zip(x_val,y_val))

			# Select one of these cells at random
			empty_cell = empty_cells[np.random.choice(len(empty_cells))]

			# Select a value of 2 or 4 with a ratio of 9:1
			tile_val = np.random.choice([2, 4], p=[0.9, 0.1])

			# Update the board
			board[empty_cell[0]][empty_cell[1]] = tile_val

			# Update total_tiles
			total_tiles += 1

			# Check if high score needs to be updated
			self.check_high_score()

			# Check for game over
			self.check_for_game_over()

		if real:
			self.board = board
			self.score = score
			self.total_tiles = total_tiles
		else:
			new_state = GameState(self.depth_to_search, self.current_depth + 1, board, score)
			reward = score - original_score
			if cells_changed == 0:
				reward = -1000000000
			return new_state, reward

	def check_high_score(self):
		# If the score is greater than the high score...
		if self.score > self.highscore:
			# Update high score
			self.highscore = self.score

	def check_for_game_over(self):
		# If there are 16 non-zero tiles...
		if self.total_tiles == 16:
			# The game is over
			self.game_over = True

	def update_high_score(self):
		# Write high score to file
		f = open("highscore.txt", "w")
		f.write(str(self.highscore))
		f.close()

	def reset(self):

		# Set score back to 0
		self.score = 0

		# Clear board and re-initilize with two random tiles
		self.board = np.zeros((4, 4), dtype=np.int)
		self.total_tiles = 0 # Incremented by add_tile
		self.add_tile()
		self.add_tile()

		self.game_over = False

	def get_best_action(self):

		# print("self.current_depth", self.current_depth)
		# self.display()

		# Store the outcome after moving left
		left_new_state, left_reward = self.move(LEFT, real = False)
		left_val = left_new_state.value + left_reward
		# left_new_state.display()
		# print("left_val", left_val, self.current_depth)

		# Store the outcome after moving up
		up_new_state, up_reward = self.move(UP, real = False)
		up_val = up_new_state.value + up_reward
		# print("up_val", up_val, self.current_depth)

		# Store the outcome after moving right
		right_new_state, right_reward = self.move(RIGHT, real = False)
		right_val = right_new_state.value + right_reward
		# print("right_val", right_val, self.current_depth)

		# Store the outcome after moving down
		down_new_state, down_reward = self.move(DOWN, real = False)
		down_val = down_new_state.value + down_reward
		# print("down_val", down_val, self.current_depth)

		self.value = max(left_val, up_val, right_val, down_val)
		self.best_action = [left_val, up_val, right_val, down_val].index(self.value)

		# print("value", self.value, self.current_depth)
		# print("best_action", self.best_action, self.current_depth)

		return self.best_action
