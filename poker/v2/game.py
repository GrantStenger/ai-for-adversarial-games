from player import Player
from deck import Deck

class Game:

	def __init__(self, num_players, initial_stack_size, big_blind, small_blind):

		# Create a list of players
		self.players = []

		# Each player should have a position number and an initial stack size
		for i in range(num_players):
			self.players.append(Player(i+1, initial_stack_size))

		# Assign players to be initial dealer, small blind, and big blind
		self.dealer = self.players[0]
		self.small_blind_player = self.players[1]
		self.big_blind_player = self.players[num_players % 2]

		# Assign blind values
		self.big_blind = big_blind
		self.small_blind = small_blind

		# Initialize deck
		self.deck = Deck()

		self.shuffle()

	# Shuffle deck
	def shuffle(self):
		self.deck.shuffle()

	# Deal 2 hole cards to each player
	def deal(self):
		for player in self.players:
			player.set_hole_cards(self.deck.deal(2))

	def play(self):

		### Start
		self.shuffle()
		self.deal()

		for player in self.players:
			print("Player", player.position)
			print("Cards: " + str(player.hole_cards[0]) + " and " + str(player.hole_cards[1]))
			print("Stack Size:", player.stack_size)
			print()

		### Pre-Flop

		### Flop

		### Turn

		### River

		### End
		print()
