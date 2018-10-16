from Player import Player

class HumanPlayer(Player):

	def __init__(self, letter):
		Player.__init__(self, letter)

	def move(self, board):
		while True:
			decision = input("What move would you like to play? \n")
			if decision.isdigit():
				return int(decision)
			else:
				print("You must input a valid choice")
