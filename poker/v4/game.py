# Import Dependencies
from player import Player
from deck import Deck

class Game:

	def __init__(self, num_players):

		# Create a list of players
		self.players = []
		for i in range(num_players):
			self.players.append(Player())

		# Initialize deck
		self.deck = Deck()
