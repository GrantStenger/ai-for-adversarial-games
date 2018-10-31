import os

class Game:

	def __init__(self):
		self.board = self.makeBoard()
		self.gameOver = False

	def makeBoard(self):
		board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
		return board

	def printBoard(self):
		for row in range(3):
			for column in range(3):
				print(self.board[row][column], end=" ")
			print()

	def play(self, player1, player2):
		turn = player1
		move_num = 0
		while not self.gameOver and move_num != 9:
			os.system('clear')
			self.printBoard()

			hasMoved = False
			while not hasMoved:
				decision = turn.move(self.board)
				if self.move(decision, turn.letter):
					hasMoved = True

			if self.hasWon():
				self.gameOver = True
				break

			# It's now the next player's turn
			if turn == player1:
				turn = player2
			else:
				turn = player1

			# Increment move number
			move_num += 1

		os.system('clear')
		self.printBoard()
		if move_num == 9:
			print("It's a tie!")
		else:
			print(str(turn.letter), "has won!")

	def move(self, decision, letter):
		if self.board[(decision-1)//3][(decision-1)%3] == str(decision):
			self.board[(decision-1)//3][(decision-1)%3] = letter
			return True
		else:
			print("Spot has already been played")
			return False

	def hasWon(self):
		for i in range(3):
			if self.board[i][0] == self.board[i][1] == self.board[i][2]:
				return True
			elif self.board[0][i] == self.board[1][i] == self.board[2][i]:
				return True
			elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
				return True
			elif self.board[2][0] == self.board[1][1] == self.board[0][2]:
				return True
		else:
			return False
